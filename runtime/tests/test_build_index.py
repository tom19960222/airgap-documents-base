import os
import sqlite3
import sys
import tempfile
import unittest
from contextlib import closing
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
        with patch.object(build, 'page_chunks', side_effect=AssertionError('unchanged page parsed')):
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
        with closing(sqlite3.connect(self.db)) as db, db:
            self.assertEqual(db.execute('PRAGMA integrity_check').fetchone()[0], 'ok')
            db.execute("INSERT INTO chunks_fts(chunks_fts, rank) VALUES('integrity-check', 1)")

    def test_failures_preserve_previous_index(self):
        self.page('a.md', '# A\nstable\n')
        self.run_build()
        before = self.snapshot(self.db)
        self.page('a.md', '# A\nchanged\n')
        self.page('z.md', '# Z\nnew\n')
        (self.corpus / 'z.md').write_text('---\nunterminated frontmatter\n')
        for full in (False, True):
            with self.assertRaises(ValueError):
                self.run_build(full=full)
            self.assertEqual(self.snapshot(self.db), before)
        self.assertEqual(list(self.db.parent.glob('*.tmp')), [])

    def test_old_schema_and_changed_rules_rebuild(self):
        self.db.parent.mkdir()
        with closing(sqlite3.connect(self.db)) as db, db:
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
        self.page('a.md', '# A\nfirst\n')
        self.run_build()
        path = self.corpus / 'a.md'
        old = path.stat()
        self.page('a.md', '# A\nother\n')
        os.utime(path, ns=(old.st_atime_ns, old.st_mtime_ns))
        self.assertEqual(self.run_build()['modified'], 1)

    @unittest.skipUnless(os.name == 'posix', '檔案狀態快取需要 POSIX ctime')
    def test_unchanged_does_not_read_file_contents(self):
        self.page('a.md', '# A\nfresh\n')
        self.run_build()
        with patch.object(build, 'read_page', side_effect=AssertionError('unchanged page read')):
            stats = self.run_build()
        self.assertEqual(stats['cached'], 1)
        self.assertEqual(stats['hashed'], 0)

    def test_verify_content_reads_all_files(self):
        self.page('a.md', '# A\nfresh\n')
        self.run_build()
        stats = self.run_build(verify_content=True)
        self.assertEqual(stats['cached'], 0)
        self.assertEqual(stats['hashed'], 1)
        self.assertEqual(stats['skipped'], 1)

    @unittest.skipUnless(os.name == 'posix', '檔案狀態快取需要 POSIX ctime')
    def test_metadata_change_without_content_change_refreshes_cache(self):
        self.page('a.md', '# A\nfresh\n')
        self.run_build()
        path = self.corpus / 'a.md'
        old = path.stat()
        os.utime(path, ns=(old.st_atime_ns, old.st_mtime_ns + 1_000_000_000))
        with patch.object(build, 'page_chunks', side_effect=AssertionError('unchanged content parsed')):
            stats = self.run_build()
        self.assertEqual((stats['hashed'], stats['skipped']), (1, 1))
        self.assertEqual(self.run_build()['cached'], 1)

    def test_old_manifest_upgrades_without_reindexing(self):
        self.page('a.md', '# A\nfresh\n')
        self.run_build()
        with closing(sqlite3.connect(self.db)) as db, db:
            db.executescript("""
                ALTER TABLE pages RENAME TO old_pages;
                CREATE TABLE pages (page_path TEXT PRIMARY KEY, sha256 TEXT NOT NULL,
                                    chunk_count INTEGER NOT NULL);
                INSERT INTO pages SELECT page_path, sha256, chunk_count FROM old_pages;
                DROP TABLE old_pages;
            """)
        with patch.object(build, 'page_chunks', side_effect=AssertionError('old manifest reparsed')):
            stats = self.run_build()
        self.assertEqual((stats['mode'], stats['hashed'], stats['skipped']), ('incremental', 1, 1))
        self.assertEqual(self.run_build()['cached'], 1 if os.name == 'posix' else 0)

    def test_repeated_headings_keep_ids_without_quadratic_slug_work(self):
        body = '# Repeat\nfirst\n# Repeat-2\nsecond\n' + '# Repeat\nmore\n' * 1000
        self.page('a.md', body)
        with patch.object(build, 'slugify', wraps=build.slugify) as slug:
            self.run_build()
        self.assertLessEqual(slug.call_count, 1002)
        with closing(sqlite3.connect(self.db)) as db, db:
            ids = [r[0] for r in db.execute('SELECT chunk_id FROM chunks ORDER BY id')]
        self.assertEqual(ids[:4], ['a.md#repeat', 'a.md#repeat-2', 'a.md#repeat-3', 'a.md#repeat-4'])
        self.assertEqual(ids[-1], 'a.md#repeat-1002')

    def test_verify_content_detects_change_even_if_metadata_is_unreliable(self):
        with patch.object(build, 'file_fingerprint', return_value='unreliable'):
            self.page('a.md', '# A\nfirst\n')
            self.run_build()
            self.page('a.md', '# A\nother\n')
            stats = self.run_build(verify_content=True)
        self.assertEqual((stats['hashed'], stats['modified']), (1, 1))

    def test_unsupported_metadata_always_hashes(self):
        self.page('a.md', '# A\nfresh\n')
        with patch.object(build, 'file_fingerprint', return_value=None):
            self.run_build()
            stats = self.run_build()
        self.assertEqual((stats['cached'], stats['hashed'], stats['skipped']), (0, 1, 1))

    def test_replaced_file_with_same_size_and_mtime_is_detected(self):
        self.page('a.md', '# A\nfirst\n')
        self.run_build()
        path = self.corpus / 'a.md'
        old = path.stat()
        self.page('replacement.md', '# A\nother\n')
        replacement = self.corpus / 'replacement.md'
        os.utime(replacement, ns=(old.st_atime_ns, old.st_mtime_ns))
        replacement.replace(path)
        self.assertEqual(self.run_build()['modified'], 1)

    def test_changing_file_during_read_does_not_cache_fingerprint(self):
        self.page('a.md', '# A\nfresh\n')
        with patch.object(build, 'file_fingerprint', side_effect=['before', 'after']):
            data, fingerprint = build.read_page(self.corpus / 'a.md')
        self.assertIn(b'fresh', data)
        self.assertIsNone(fingerprint)

    def test_scan_order_keeps_chunk_ids_and_neighbors(self):
        self.page('a.md', '# A\nfresh\n')
        (self.corpus / 'a').mkdir()
        self.page('a/nested.md', '# Nested\nfresh\n')
        self.page('a!.md', '# Earlier\nfresh\n')
        self.run_build()
        expected = [p.relative_to(self.corpus).as_posix() for p in sorted(self.corpus.rglob('*.md'))]
        with closing(sqlite3.connect(self.db)) as db:
            actual = [r[0] for r in db.execute('SELECT page_path FROM chunks ORDER BY id')]
        self.assertEqual(actual, expected)

    def test_parallel_matches_serial_and_incremental(self):
        for i in range(70):
            self.page(f'{i:03}.md', f'# Same\nfresh {i}\n## Same\nmore\n')
        serial = self.root / 'serial.db'
        build.build_index(self.corpus, serial, jobs=1)
        stats = self.run_build(jobs=2)
        self.assertEqual(stats['jobs'], 2)
        self.assertEqual(self.snapshot(self.db), self.snapshot(serial))
        for i in range(70):
            self.page(f'{i:03}.md', f'# Changed\nfresh changed {i}\n')
        self.assertEqual(self.run_build(jobs=2)['modified'], 70)
        build.build_index(self.corpus, serial, full=True)
        self.assertEqual(self.snapshot(self.db), self.snapshot(serial))
        with closing(sqlite3.connect(self.db)) as db:
            db.execute("INSERT INTO chunks_fts(chunks_fts, rank) VALUES('integrity-check', 1)")

    def test_parallel_worker_failure_preserves_previous_index(self):
        for i in range(70):
            self.page(f'{i:03}.md', '# A\nfresh\n')
        self.run_build()
        before = self.snapshot(self.db)
        for i in range(70):
            self.page(f'{i:03}.md', '# A\nchanged\n')
        (self.corpus / '069.md').write_text('---\nunterminated frontmatter\n')
        for full in (False, True):
            with self.assertRaises(ValueError):
                self.run_build(full=full, jobs=2)
            self.assertEqual(self.snapshot(self.db), before)
        self.assertEqual(list(self.db.parent.glob('*.tmp')), [])

    def test_invalid_jobs_does_not_modify_database(self):
        self.page('a.md', '# A\nfresh\n')
        self.run_build()
        before = self.db.read_bytes()
        for jobs in (0, -1):
            with self.assertRaisesRegex(ValueError, 'jobs'):
                self.run_build(jobs=jobs)
        self.assertEqual(self.db.read_bytes(), before)

    def test_writer_failure_rolls_back_and_closes_parallel_pipeline(self):
        for i in range(70):
            self.page(f'{i:03}.md', '# A\nfresh\n')
        self.run_build()
        before = self.snapshot(self.db)
        for i in range(70):
            self.page(f'{i:03}.md', '# A\nchanged\n')
        insert = build.insert_chunks
        for full in (False, True):
            calls = 0
            def fail(cursor, rows):
                nonlocal calls
                calls += 1
                if calls == 40:
                    raise RuntimeError('injected write failure')
                return insert(cursor, rows)
            with patch.object(build, 'insert_chunks', side_effect=fail):
                with self.assertRaisesRegex(RuntimeError, 'injected write failure'):
                    self.run_build(full=full, jobs=2)
            self.assertEqual(self.snapshot(self.db), before)
        self.assertEqual(list(self.db.parent.glob('*.tmp')), [])

    def test_full_fts_restores_incremental_merge_settings(self):
        self.page('a.md', '# A\nfresh\n')
        self.run_build()
        with closing(sqlite3.connect(self.db)) as db:
            settings = dict(db.execute('SELECT k,v FROM chunks_fts_config'))
        self.assertEqual((settings['automerge'], settings['crisismerge']), (4, 16))
        self.page('a.md', '# A\nchanged\n')
        self.run_build()
        core = SearchCore(self.db)
        try:
            self.assertEqual(core.search('fresh'), [])
            self.assertEqual(len(core.search('changed')), 1)
        finally:
            core.db.close()

    def test_fts_failure_preserves_previous_index(self):
        self.page('a.md', '# A\nfresh\n')
        self.run_build()
        before = self.db.read_bytes()
        self.page('a.md', '# A\nchanged\n')
        rebuild = build.rebuild_fts
        def fail(cursor):
            rebuild(cursor)
            raise RuntimeError('injected FTS failure')
        with patch.object(build, 'rebuild_fts', side_effect=fail):
            with self.assertRaisesRegex(RuntimeError, 'injected FTS failure'):
                self.run_build(full=True)
        self.assertEqual(self.db.read_bytes(), before)
        self.assertEqual(list(self.db.parent.glob('*.tmp')), [])


if __name__ == '__main__':
    unittest.main()
