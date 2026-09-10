import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build_index as build
from search_core import SearchCore


class BuildIndexTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.corpus = self.root / 'corpus'
        self.corpus.mkdir()
        self.db = self.root / 'index' / 'docs.db'

    def page(self, name, body):
        (self.corpus / name).write_text(
            '---\ncollection: demo\nversion: 1\ntitle: Demo\nsource_url: https://example.org\n---\n' + body,
            encoding='utf-8',
        )

    def run_build(self, **kwargs):
        return build.build_index(self.corpus, self.db, **kwargs)

    def snapshot(self, path):
        core = SearchCore(path)
        try:
            ids = [r[0] for r in core.db.execute('SELECT chunk_id FROM chunks ORDER BY chunk_id')]
            return ([core.get_section(i) for i in ids],
                    sorted(core.search('fresh', limit=20), key=lambda r: r['chunk_id']),
                    core.list_collections())
        finally:
            core.db.close()

    def test_incremental_matches_full_and_skips_unchanged(self):
        self.page('a.md', '# Same\nstale\n## Same\nold\n')
        self.page('b.md', '# B\nobsolete\n')
        self.page('empty.md', '')
        self.run_build()
        before = self.db.read_bytes()
        statements = []
        connect = sqlite3.connect
        def traced_connect(*args, **kwargs):
            db = connect(*args, **kwargs)
            db.set_trace_callback(statements.append)
            return db
        with patch.object(build, 'index_page', side_effect=AssertionError('unchanged page parsed')):
            with patch.object(build.sqlite3, 'connect', side_effect=traced_connect):
                stats = self.run_build()
        self.assertFalse(any(sql.lstrip().upper().startswith(('INSERT', 'UPDATE', 'DELETE'))
                             for sql in statements))
        self.assertEqual(stats['skipped'], 3)
        self.assertEqual(before, self.db.read_bytes())
        self.page('a.md', '# Same\nfresh\n## Same\nfresh second\n')
        (self.corpus / 'b.md').unlink()
        self.page('c.md', '# C\nfresh third\n')
        stats = self.run_build()
        self.assertEqual([stats[k] for k in ('added', 'modified', 'deleted', 'skipped')], [1, 1, 1, 1])
        core = SearchCore(self.db)
        self.assertEqual(core.search('stale'), [])
        self.assertEqual(core.search('obsolete'), [])
        core.db.close()
        full = self.root / 'full.db'
        build.build_index(self.corpus, full, full=True)
        self.assertEqual(self.snapshot(self.db), self.snapshot(full))
        with sqlite3.connect(self.db) as db:
            self.assertEqual(db.execute('PRAGMA integrity_check').fetchone()[0], 'ok')
            db.execute("INSERT INTO chunks_fts(chunks_fts, rank) VALUES('integrity-check', 1)")

    def test_failures_preserve_previous_index(self):
        self.page('a.md', '# A\nstable\n')
        self.run_build()
        before = self.snapshot(self.db)
        self.page('a.md', '# A\nchanged\n')
        self.page('z.md', '# Z\nnew\n')
        original = build.index_page
        def fail(cursor, path, *args, **kwargs):
            if path.name == 'z.md':
                raise RuntimeError('injected failure')
            return original(cursor, path, *args, **kwargs)
        for full in (False, True):
            with patch.object(build, 'index_page', side_effect=fail):
                with self.assertRaisesRegex(RuntimeError, 'injected'):
                    self.run_build(full=full)
            self.assertEqual(self.snapshot(self.db), before)
        self.assertEqual(list(self.db.parent.glob('*.tmp')), [])

    def test_old_schema_and_changed_rules_rebuild(self):
        self.db.parent.mkdir()
        with sqlite3.connect(self.db) as db:
            db.execute('CREATE TABLE old_schema (id INTEGER)')
        self.page('a.md', '# A\nfresh\n')
        self.assertEqual(self.run_build()['mode'], 'full')
        with patch.object(build, 'INDEX_VERSION', build.INDEX_VERSION + 1):
            self.assertEqual(self.run_build()['mode'], 'full')

    def test_empty_page_and_removing_all_documents(self):
        self.page('a.md', '# A\nfresh\n')
        self.run_build()
        self.page('a.md', '')
        self.assertEqual(self.run_build()['chunks'], 0)
        self.assertEqual(self.run_build()['skipped'], 1)
        (self.corpus / 'a.md').unlink()
        stats = self.run_build()
        self.assertEqual((stats['pages'], stats['chunks'], stats['deleted']), (0, 0, 1))
        self.page('a.md', '# A\nfresh\n')
        self.assertEqual(self.run_build()['added'], 1)
        self.assertEqual(len(self.snapshot(self.db)[1]), 1)

    def test_content_change_with_same_size_and_mtime(self):
        import os
        self.page('a.md', '# A\nfirst\n')
        self.run_build()
        path = self.corpus / 'a.md'
        old = path.stat()
        self.page('a.md', '# A\nother\n')
        os.utime(path, ns=(old.st_atime_ns, old.st_mtime_ns))
        self.assertEqual(self.run_build()['modified'], 1)


if __name__ == '__main__':
    unittest.main()
