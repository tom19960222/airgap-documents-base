import io
import json
import re
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import common
from common import Manifest
from git_source import _discover_source_files, normalize
from opencode_source import render_mdx, render_openapi, rewrite_site_links
from validate_ceph_corpus import validate_corpus


class OpenCodeSourceTests(unittest.TestCase):
    def test_mdx_validator_treats_inline_underscores_as_markdown_literals(self):
        with TemporaryDirectory() as temporary:
            corpus = Path(temporary)
            page = corpus / 'guide.md'
            page.write_text('---\ncollection: opencode\nversion: "1"\ntitle: Guide\nsource_url: https://example.com/source\nfetched_at: now\n---\nUse _!`command`_, `<server>_<tool>`, `/`, `_`, and `-`.\n')
            manifest = Manifest(name='opencode', collection='opencode', version='1', shortcode_profile='opencode')
            self.assertEqual(validate_corpus(corpus, manifest, raw_required=False)['failures'], [])
            page.write_text(page.read_text() + '\n.. include:: missing.rst\n')
            self.assertTrue(any('residual RST image/include' in item for item in validate_corpus(corpus, manifest, raw_required=False)['failures']))

    def test_mdx_keeps_all_tabs_callouts_and_literal_examples(self):
        source = '''import { Tabs } from "components"
export const console = config.console
export const typesUrl = `${config.github}/blob/dev/types.ts`
<Tabs><TabItem label="npm">
```bash
npm install -g opencode-ai
```
</TabItem><TabItem label="Bun">
```js
import { Plugin } from "example"
export const Demo = () => "<Tabs>"
```
</TabItem></Tabs>
:::tip[Setup]
Use <a href={console}>Console</a> and <a href={typesUrl}><code>Types</code></a>.
:::
<Callout type="warning">Read this.</Callout>
<PlanTabs><div slot="go-plus">
    | Model | Limit |
    | --- | --- |
    | A | 40 |
</div></PlanTabs>
`<Callout>literal</Callout>`
'''
        output = render_mdx(source, {"console": "https://opencode.ai/auth", "github": "https://github.com/anomalyco/opencode"})
        self.assertNotIn('import { Tabs }', output)
        self.assertIn('**npm**', output)
        self.assertIn('**Bun**', output)
        self.assertIn('import { Plugin } from "example"\nexport const Demo = () => "<Tabs>"', output)
        self.assertIn('[Console](https://opencode.ai/auth)', output)
        self.assertIn('[`Types`](https://github.com/anomalyco/opencode/blob/dev/types.ts)', output)
        self.assertIn('**Tip: Setup:**', output)
        self.assertIn('**Warning:**', output)
        self.assertIn('**Go Plus**\n\n| Model | Limit |', output)
        self.assertIn('`<Callout>literal</Callout>`', output)

    def test_code_tabs_decode_every_command_without_evaluating_javascript(self):
        output = render_mdx('''<CodeTabs id="install" tabs={[
  { label: "npm", code: "npm install -g @opencode/cli" },
  { label: "curl", code: "echo \\"one\\"\\necho two" },
]} />''', {})
        self.assertIn('npm install -g @opencode/cli', output)
        self.assertIn('echo "one"\necho two', output)
        with self.assertRaises(ValueError):
            render_mdx('<CodeTabs tabs={runCode()} />', {})
        with self.assertRaises(ValueError):
            render_mdx('<FutureComponent />', {})
        with self.assertRaises(ValueError):
            render_mdx('export const value = config.missing', {})

    def test_site_routes_resolve_nested_indexes_api_queries_and_fragments(self):
        manifest = Manifest(name='opencode', collection='opencode', version='2.0.30', site_overrides={'docs_url': 'https://opencode.ai/v2/docs'})
        outputs = {'intro.mdx': 'index.md', 'build.mdx': 'build/index.md', 'openapi.json': 'api.md'}
        output = rewrite_site_links('''[Build](/build/?view=1#setup)
[API](https://opencode.ai/v2/docs/api#session.list)
[Missing](/future)
`[Literal](/build)`
```md
[Literal](/build)
```
''', Path('cli/config.md'), outputs, manifest)
        self.assertIn('[Build](../build/index.md?view=1#setup)', output)
        self.assertIn('[API](../api.md#session.list)', output)
        self.assertIn('[Missing](https://opencode.ai/v2/docs/future) <!-- unresolved-site-link: route=/future -->', output)
        self.assertIn('`[Literal](/build)`', output)
        self.assertIn('```md\n[Literal](/build)\n```', output)

    def test_openapi_retains_every_json_node_including_shared_path_metadata(self):
        schema = {
            'openapi': '3.1.0', 'info': {'version': '0.0.1'}, 'security': [{'token': []}],
            'paths': {'/session': {'parameters': [{'name': 'shared'}], 'get': {'operationId': 'session.list', 'responses': {'200': {'description': 'OK'}}}, 'post': {'requestBody': {'required': True}}}},
            'components': {'schemas': {'Session': {'properties': {'id': {'type': 'string'}}}}, 'securitySchemes': {'token': {'type': 'http', 'scheme': 'bearer'}}},
        }
        title, body = render_openapi(json.dumps(schema))
        self.assertEqual(title, 'HTTP API')
        blocks = [json.loads(value) for value in re.findall(r'```json\n(.*?)\n```', body, re.DOTALL)]
        self.assertEqual(blocks, [
            {k: v for k, v in schema.items() if k not in {'paths', 'components'}},
            {'parameters': [{'name': 'shared'}]},
            schema['paths']['/session']['get'], schema['paths']['/session']['post'],
            schema['components']['schemas']['Session'], schema['components']['securitySchemes']['token'],
        ])
        self.assertIn('<a id="session.list"></a>', body)
        self.assertIn('<a id="schemas"></a>', body)
        self.assertIn('<a id="schema-Session"></a>', body)

    def test_normalize_discovers_only_opted_in_mdx_and_emits_versioned_api(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            repo = root / 'raw/opencode/2.0.30/repo'
            (repo / 'docs').mkdir(parents=True)
            (repo / 'docs/index.mdx').write_text('---\ntitle: Intro\ndescription: Start here.\n---\n[Config](/config)\n[Sibling](config)\n[API](/api#list)\n')
            (repo / 'docs/config.mdx').write_text('---\ntitle: Config\n---\nConfiguration body.\n')
            (repo / 'openapi.json').write_text(json.dumps({'openapi': '3.1.0', 'info': {'version': '0.0.1'}, 'paths': {}}))
            manifest = Manifest(name='opencode-2', collection='opencode', version='2.0.30', source_type='git', repo_url='https://github.com/anomalyco/opencode', git_ref='a' * 40, docs_paths=['docs', 'openapi.json'], shortcode_profile='opencode', preserve_description=True, site_overrides={'docs_url': 'https://opencode.ai/v2/docs'})
            legacy = Manifest(name='legacy', collection='legacy', version='1', docs_paths=['docs'])
            self.assertEqual(_discover_source_files(legacy, repo), [])
            with patch.object(common, 'REPO_ROOT', root), redirect_stdout(io.StringIO()):
                normalize(manifest)
            corpus = root / 'corpus/opencode/2.0.30'
            self.assertEqual(sorted(p.name for p in corpus.iterdir()), ['api.md', 'config.md', 'index.md'])
            intro = (corpus / 'index.md').read_text()
            self.assertIn('[Config](config.md)', intro)
            self.assertIn('[Sibling](config.md)', intro)
            self.assertIn('[API](api.md#list)', intro)
            self.assertNotIn('unresolved-', intro)
            self.assertIn('description: "Start here."', intro)
            api = (corpus / 'api.md').read_text()
            self.assertIn('version: "2.0.30"', api)
            self.assertIn('/blob/' + 'a' * 40 + '/openapi.json', api)


if __name__ == '__main__':
    unittest.main()
