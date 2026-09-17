"""Validate the generated Ceph corpus without network access.

The validator distinguishes real output failures from source constructs that are
deliberately preserved in code blocks, diagrams, or unresolved-reference
classifications. Upstream example values remain ordinary document text.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import Manifest, load_manifest  # noqa: E402
from git_source import (  # noqa: E402
    ASSET_SUFFIXES,
    _discover_source_files,
    _grid_border_positions,
    _istio_site_config,
    _istio_normalize_route,
    _simple_border_spans,
    _source_url,
)


FRONTMATTER_END = "\n---\n"
RST_LINK_PATTERN = re.compile(r":(?P<kind>ref|doc|download|numref):`", re.IGNORECASE)
RST_SHORTHAND_PATTERN = re.compile(r":(?P<kind>ref|doc|download|numref):[A-Za-z0-9_./#-]+", re.IGNORECASE)
RST_NAMED_PATTERN = re.compile(r"(?<![\w`])`[^`\n]+`_")
RESIDUAL_NAMED_SUFFIX_PATTERN = re.compile(r"-->_")
RST_IMAGE_INCLUDE_PATTERN = re.compile(r"^\s*\.\.\s+(?:image|figure|include)::", re.IGNORECASE)
DIRECTIVE_PATTERN = re.compile(r"^(?P<indent> *)\.\.\s+(?P<name>[A-Za-z0-9_.-]+)::")
GFM_SEPARATOR_PATTERN = re.compile(r"^\s*\|(?:\s*:?-{3,}:?\s*\|)+\s*$")
MARKDOWN_LINK_OPEN_PATTERN = re.compile(r"!?\[[^\]\n]*\]\(")
BARE_URL_PATTERN = re.compile(r"(?<![A-Za-z0-9_@])https?://[^\s<>\"]+", re.IGNORECASE)
UNRESOLVED_PATTERN = re.compile(
    r"<!--\s*unresolved-rst-link:\s*kind=(?P<kind>\S+)\s+target=(?P<target>.*?)\s*-->"
)
UNRESOLVED_SOURCE_PATTERN = re.compile(
    r"<!--\s*unresolved-source-link:\s*target=(?P<target>.*?)\s*-->"
)
UNRESOLVED_SITE_PATTERN = re.compile(
    r"<!--\s*unresolved-site-link:\s*route=(?P<route>.*?)\s*-->"
)
FENCE_LINE_PATTERN = re.compile(r"^\s*(?:>\s*)*(?P<fence>`{3,}|~{3,})")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find(FRONTMATTER_END, 4)
    if end < 0:
        return {}, text
    metadata: dict[str, str] = {}
    for line in text[4:end].splitlines():
        key, separator, value = line.partition(":")
        if not separator:
            continue
        value = value.strip()
        if value.startswith('"'):
            try:
                value = str(json.loads(value))
            except json.JSONDecodeError:
                value = value.strip('"')
        metadata[key.strip()] = value
    return metadata, text[end + len(FRONTMATTER_END) :]


def _normalise_repo_url(value: str) -> str:
    value = value.strip()
    if value.endswith(".git"):
        value = value[:-4]
    if value.startswith("git@") and ":" in value:
        host, path = value.split(":", 1)
        value = f"https://{host.removeprefix('git@')}/{path}"
    return value.rstrip("/")


def _validate_raw_checkout(raw_repo: Path, manifest: Manifest) -> list[str]:
    """Verify that the raw directory is the manifest's fixed git checkout."""

    failures: list[str] = []
    meta_path = raw_repo.parent / "git_meta.json"
    if not meta_path.is_file():
        failures.append(f"raw checkout metadata missing: {meta_path}")
    else:
        try:
            metadata = json.loads(meta_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            failures.append(f"raw checkout metadata unreadable: {meta_path}: {error}")
        else:
            if _normalise_repo_url(str(metadata.get("repo_url", ""))) != _normalise_repo_url(manifest.repo_url):
                failures.append("raw checkout metadata repo_url does not match manifest")
            if metadata.get("git_ref") != manifest.git_ref:
                failures.append("raw checkout metadata git_ref does not match manifest")
            if metadata.get("commit_hash") != manifest.git_ref:
                failures.append("raw checkout metadata commit_hash does not match manifest")

    def git_value(*args: str) -> str | None:
        try:
            result = subprocess.run(
                ["git", "-C", str(raw_repo), *args],
                check=True,
                capture_output=True,
                text=True,
            )
        except (OSError, subprocess.CalledProcessError):
            return None
        return result.stdout.strip()

    head = git_value("rev-parse", "--verify", "HEAD")
    if head is None:
        failures.append(f"raw checkout is not a readable git repository: {raw_repo}")
    elif head != manifest.git_ref:
        failures.append(f"raw checkout HEAD {head} does not match manifest git_ref {manifest.git_ref}")
    remote = git_value("config", "--get", "remote.origin.url")
    if remote is None:
        failures.append(f"raw checkout origin remote missing: {raw_repo}")
    elif _normalise_repo_url(remote) != _normalise_repo_url(manifest.repo_url):
        failures.append("raw checkout origin remote does not match manifest repo_url")
    return failures


def extract_markdown_targets(text: str) -> list[str]:
    """Extract balanced Markdown link/image targets, including URL parentheses."""

    targets: list[str] = []
    cursor = 0
    while True:
        match = MARKDOWN_LINK_OPEN_PATTERN.search(text, cursor)
        if match is None:
            break
        index = match.end()
        depth = 0
        escaped = False
        end: int | None = None
        while index < len(text):
            char = text[index]
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == "(":
                depth += 1
            elif char == ")":
                if depth == 0:
                    end = index
                    break
                depth -= 1
            index += 1
        if end is None:
            break
        targets.append(text[match.end() : end].strip())
        cursor = end + 1
    return targets


def _split_target(target: str) -> tuple[str, str]:
    target = target.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")].strip()
    path, hash_mark, fragment = target.partition("#")
    path, query_mark, query = path.partition("?")
    suffix = (f"?{query}" if query_mark else "") + (f"#{fragment}" if hash_mark else "")
    return path, suffix


def _is_external(target: str) -> bool:
    return bool(
        re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target)
        or target.startswith("//")
        or re.match(r"^[^/\s@]+@[^/\s@]+$", target)
        or re.match(r"^[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+){1,}(?:/|$)", target)
    )


def _is_manifest_site_target(path_part: str, manifest: Manifest) -> bool:
    """Identify site-root or same-origin links for an opted-in manifest."""

    site_config = _istio_site_config(manifest)
    if site_config is None:
        return False
    site_root, _ = site_config
    root = urlsplit(site_root)
    if path_part.startswith("/") and not path_part.startswith("//"):
        return True
    try:
        parsed = urlsplit(path_part)
    except ValueError:
        return False
    return (
        parsed.scheme.lower() in {"http", "https"}
        and parsed.netloc.lower() == root.netloc.lower()
    )


def _manifest_site_route(path_part: str, manifest: Manifest) -> str | None:
    """Return the marker route represented by one rendered Istio site URL."""

    site_config = _istio_site_config(manifest)
    if site_config is None:
        return None
    site_root, _ = site_config
    root = urlsplit(site_root)
    target = path_part.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()
    try:
        parsed = urlsplit(target)
    except ValueError:
        return None
    if target.startswith("/") and not target.startswith("//"):
        path = parsed.path
    elif (
        parsed.scheme.lower() in {"http", "https"}
        and parsed.netloc.lower() == root.netloc.lower()
    ):
        path = parsed.path or "/"
        base_path = root.path.rstrip("/")
        if base_path and (path == base_path or path.startswith(f"{base_path}/")):
            path = path[len(base_path) :] or "/"
    else:
        return None
    return _istio_normalize_route(path)


def _iter_body_lines(body: str):
    """Yield ``(line_number, line, context)`` for rendered Markdown lines."""

    fence: tuple[str, int] | None = None
    directive: tuple[str, int] | None = None
    for line_number, line in enumerate(body.splitlines(), 1):
        fence_match = FENCE_LINE_PATTERN.match(line)
        if fence_match is not None:
            marker = fence_match.group("fence")
            if fence is None:
                fence = (marker[0], len(marker))
            elif marker[0] == fence[0] and len(marker) >= fence[1]:
                fence = None
            yield line_number, line, "fenced-code"
            continue
        if fence is not None:
            yield line_number, line, "fenced-code"
            continue
        if directive is not None:
            name, indent = directive
            if line.strip() and len(line) - len(line.lstrip(" ")) <= indent:
                directive = None
            else:
                yield line_number, line, f"directive:{name}"
                continue
        match = DIRECTIVE_PATTERN.match(line)
        if match:
            directive = (match.group("name").lower(), len(match.group("indent")))
            yield line_number, line, "normal"
            continue
        yield line_number, line, "normal"


def _page_link_failures(
    page_path: Path,
    body: str,
    corpus_dir: Path,
    manifest: Manifest,
) -> tuple[list[str], int, list[str]]:
    failures: list[str] = []
    unresolved: list[str] = []
    pinned_assets = 0
    normal_lines = [line for _, line, context in _iter_body_lines(body) if context == "normal"]
    normal_body = "\n".join(normal_lines)
    site_targets: Counter[str] = Counter()
    site_markers = Counter(
        match.group("route") for match in UNRESOLVED_SITE_PATTERN.finditer(normal_body)
    )

    repository = urlsplit(manifest.repo_url.rstrip("/"))
    blob_prefix = repository.path.rstrip("/") + "/blob/"
    for raw_target in extract_markdown_targets(normal_body):
        path_part, _ = _split_target(raw_target)
        if _is_manifest_site_target(path_part, manifest):
            route = _manifest_site_route(path_part, manifest)
            if route is not None:
                site_targets[route] += 1
            continue
        if not path_part or path_part.startswith("/") or _is_external(path_part):
            parsed = urlsplit(path_part)
            if parsed.scheme == repository.scheme and parsed.netloc == repository.netloc:
                if parsed.path.startswith(blob_prefix):
                    remainder = parsed.path[len(blob_prefix) :].split("/", 1)
                    if len(remainder) == 2 and Path(remainder[1]).suffix.lower() in ASSET_SUFFIXES:
                        if remainder[0] != manifest.git_ref:
                            failures.append(f"{page_path}: asset URL is not pinned to {manifest.git_ref}")
                        else:
                            pinned_assets += 1
            continue

        target_path = (page_path.parent / path_part).resolve()
        if target_path.suffix == "":
            target_path = target_path.with_suffix(".md")
        try:
            target_path.relative_to(corpus_dir.resolve())
        except ValueError:
            unresolved.append(f"{page_path}: link escapes corpus: {raw_target}")
            continue
        if target_path.suffix.lower() != ".md":
            unresolved.append(f"{page_path}: relative link is not a corpus Markdown page: {raw_target}")
        elif not target_path.is_file():
            unresolved.append(f"{page_path}: missing local link target: {raw_target}")

    # A site URL can also occur as ordinary prose (or an autolink) rather than
    # a Markdown destination.  Keep the same manifest-gated classification so
    # those links cannot bypass validation merely by changing syntax.
    bare_body = re.sub(r"`+[^`\n]*`+", "", normal_body)
    for match in BARE_URL_PATTERN.finditer(bare_body):
        target = match.group(0)
        if match.start() >= 2 and bare_body[match.start() - 2 : match.start()] == "](":
            continue
        if _is_manifest_site_target(target, manifest):
            route = _manifest_site_route(target, manifest)
            if route is not None:
                site_targets[route] += 1
    for route, count in site_targets.items():
        missing = count - site_markers[route]
        if missing > 0:
            failures.append(
                f"{page_path}: {missing} unclassified site link(s) for route: {route}"
            )
    return failures, pinned_assets, unresolved


def _table_report(page_path: Path, body: str) -> dict[str, object]:
    report: dict[str, object] = {"residual": [], "fenced": 0, "directives": Counter(), "gfm": 0}
    residual = report["residual"]
    directives: Counter[str] = report["directives"]  # type: ignore[assignment]
    for line_number, line, context in _iter_body_lines(body):
        is_border = _grid_border_positions(line) is not None or _simple_border_spans(line) is not None
        if is_border:
            if context == "fenced-code":
                report["fenced"] = int(report["fenced"]) + 1
            elif context.startswith("directive:"):
                directives[context.split(":", 1)[1]] += 1
            else:
                residual.append(f"{page_path}:{line_number}")  # type: ignore[union-attr]
        if context == "normal" and GFM_SEPARATOR_PATTERN.match(line):
            report["gfm"] = int(report["gfm"]) + 1
    return report


def validate_corpus(
    corpus_dir: Path,
    manifest: Manifest,
    raw_repo: Path | None = None,
    *,
    raw_required: bool = True,
) -> dict[str, object]:
    pages = sorted(corpus_dir.rglob("*.md")) if corpus_dir.exists() else []
    failures: list[str] = []
    metadata_failures: list[str] = []
    link_failures: list[str] = []
    unresolved_source_links: list[str] = []
    residual_tables: list[str] = []
    fenced_tables = 0
    directive_tables: Counter[str] = Counter()
    gfm_tables = 0
    unresolved_refs: Counter[str] = Counter()
    unresolved_link_markers: Counter[str] = Counter()
    pinned_assets = 0
    page_meta: dict[Path, dict[str, str]] = {}

    expected: dict[Path, tuple[Path, str]] = {}
    raw_source_count = None
    raw_nonempty_count = None
    raw_available = raw_repo is not None and raw_repo.exists()
    if raw_required and not raw_available:
        failures.append(
            "raw repo unavailable for source inventory/link classification; "
            "pass --allow-missing-raw only for content-only validation"
        )
    if raw_available:
        failures.extend(_validate_raw_checkout(raw_repo, manifest))  # type: ignore[arg-type]
        files = _discover_source_files(manifest, raw_repo)  # type: ignore[arg-type]
        raw_source_count = len(files)
        raw_nonempty_count = 0
        if not files:
            failures.append(f"raw checkout contains no source files under {manifest.docs_paths}")
        for file_path, rel_out_path in files:
            try:
                raw_text = file_path.read_text(encoding="utf-8", errors="replace")
            except OSError as error:
                failures.append(f"raw source unreadable: {file_path}: {error}")
                continue
            repo_rel = file_path.relative_to(raw_repo).as_posix()  # type: ignore[arg-type]
            if not raw_text.strip():
                continue
            raw_nonempty_count += 1
            output_rel = Path(rel_out_path).with_suffix(".md")
            expected[output_rel] = (file_path, _source_url(manifest, repo_rel, rel_out_path))

    for page_path in pages:
        relative_page = page_path.relative_to(corpus_dir)
        text = page_path.read_text(encoding="utf-8", errors="replace")
        metadata, body = parse_frontmatter(text)
        page_meta[relative_page] = metadata
        required_metadata = ("collection", "version", "title", "source_url", "fetched_at")
        if manifest.app_version:
            required_metadata += ("app_version",)
        if manifest.chart_version:
            required_metadata += ("chart_version",)
        for key in required_metadata:
            if not metadata.get(key):
                metadata_failures.append(f"{relative_page}: missing frontmatter {key}")
        if metadata.get("collection") != manifest.collection:
            metadata_failures.append(f"{relative_page}: collection={metadata.get('collection')!r}")
        if metadata.get("version") != manifest.version:
            metadata_failures.append(f"{relative_page}: version={metadata.get('version')!r}")
        if manifest.app_version and metadata.get("app_version") != manifest.app_version:
            metadata_failures.append(
                f"{relative_page}: app_version={metadata.get('app_version')!r}"
            )
        if manifest.chart_version and metadata.get("chart_version") != manifest.chart_version:
            metadata_failures.append(
                f"{relative_page}: chart_version={metadata.get('chart_version')!r}"
            )

        table_report = _table_report(relative_page, body)
        residual_tables.extend(table_report["residual"])  # type: ignore[arg-type]
        fenced_tables += int(table_report["fenced"])
        directive_tables.update(table_report["directives"])  # type: ignore[arg-type]
        gfm_tables += int(table_report["gfm"])

        normal_lines = [(n, line) for n, line, context in _iter_body_lines(body) if context == "normal"]
        for line_number, line in normal_lines:
            if RST_IMAGE_INCLUDE_PATTERN.match(line):
                metadata_failures.append(f"{relative_page}:{line_number}: residual RST image/include")
            if RESIDUAL_NAMED_SUFFIX_PATTERN.search(line):
                metadata_failures.append(f"{relative_page}:{line_number}: corrupted unresolved RST named-link suffix")
        normal_body = "\n".join(line for _, line in normal_lines)
        # RST role syntax inside a preserved double-backtick teaching example
        # is content, not an unresolved output construct.
        construct_body = re.sub(r"``[^\n]*?``", "", normal_body)
        for pattern, label in (
            (RST_LINK_PATTERN, "residual RST link role"),
            (RST_SHORTHAND_PATTERN, "residual RST shorthand role"),
            (RST_NAMED_PATTERN, "residual RST named link"),
        ):
            for match in pattern.finditer(construct_body):
                line_number = construct_body.count("\n", 0, match.start()) + 1
                metadata_failures.append(f"{relative_page}:{line_number}: {label}")

        for match in UNRESOLVED_PATTERN.finditer(body):
            unresolved_refs[match.group("kind")] += 1
            unresolved_link_markers["rst"] += 1
        for _ in UNRESOLVED_SOURCE_PATTERN.finditer(normal_body):
            unresolved_link_markers["source"] += 1
        for _ in UNRESOLVED_SITE_PATTERN.finditer(normal_body):
            unresolved_link_markers["site"] += 1
        page_link_errors, page_pinned_assets, page_unresolved_links = _page_link_failures(
            page_path, body, corpus_dir, manifest
        )
        link_failures.extend(page_link_errors)
        unresolved_source_links.extend(page_unresolved_links)
        pinned_assets += page_pinned_assets

        expected_source = expected.get(relative_page)
        if expected_source is not None and metadata.get("source_url") != expected_source[1]:
            metadata_failures.append(f"{relative_page}: source_url does not match pinned source")

    actual_relatives = set(page_meta)
    expected_relatives = set(expected)
    if expected:
        for missing in sorted(expected_relatives - actual_relatives):
            metadata_failures.append(f"missing generated page: {missing}")
        for extra in sorted(actual_relatives - expected_relatives):
            metadata_failures.append(f"unexpected generated page: {extra}")
    if not pages:
        failures.append(f"corpus directory is empty or missing: {corpus_dir}")

    failures.extend(metadata_failures)
    failures.extend(link_failures)
    failures.extend(f"residual RST table border: {item}" for item in residual_tables)

    return {
        "page_count": len(pages),
        "raw_source_count": raw_source_count,
        "raw_nonempty_count": raw_nonempty_count,
        "expected_page_count": len(expected) if expected else None,
        "raw_repo_available": raw_available,
        "gfm_table_separator_rows": gfm_tables,
        "residual_table_borders": residual_tables,
        "preserved_fenced_table_borders": fenced_tables,
        "preserved_directive_table_borders": dict(sorted(directive_tables.items())),
        "pinned_asset_links": pinned_assets,
        "unresolved_refs": dict(sorted(unresolved_refs.items())),
        "unresolved_link_markers": dict(sorted(unresolved_link_markers.items())),
        "unresolved_source_links": unresolved_source_links,
        "failures": failures,
    }


def _print_report(report: dict[str, object]) -> None:
    print(
        "pages: "
        f"{report['page_count']} (raw sources={report['raw_source_count']}, "
        f"non-empty={report['raw_nonempty_count']}, expected={report['expected_page_count']})"
    )
    print(
        "tables: "
        f"gfm-separator-rows={report['gfm_table_separator_rows']}, "
        f"residual={len(report['residual_table_borders'])}, "
        f"fenced-code={report['preserved_fenced_table_borders']}, "
        f"directives={report['preserved_directive_table_borders']}"
    )
    print(
        "links: "
        f"pinned-assets={report['pinned_asset_links']}, "
        f"unresolved-rst-classified={report['unresolved_refs']}, "
        f"unresolved-markers={report['unresolved_link_markers']}, "
        f"unresolved-source-classified={len(report['unresolved_source_links'])}"
    )
    if report["failures"]:
        print(f"FAIL: {len(report['failures'])} validation issue(s)")
        for item in report["failures"]:
            print(f"  {item}")
    else:
        print("PASS: Ceph corpus metadata/content/link/table checks")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=Path("builder/manifests/ceph-20.2.toml"))
    parser.add_argument("--corpus-dir", type=Path, default=Path("corpus/ceph/20.2.4"))
    parser.add_argument("--raw-repo", type=Path, default=Path("raw/ceph/20.2.4/repo"))
    parser.add_argument(
        "--allow-missing-raw",
        action="store_true",
        help="run content-only checks when the pinned raw source checkout is unavailable",
    )
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()
    manifest = load_manifest(args.manifest)
    raw_repo = args.raw_repo if args.raw_repo.exists() else None
    report = validate_corpus(
        args.corpus_dir,
        manifest,
        raw_repo,
        raw_required=not args.allow_missing_raw,
    )
    if args.as_json:
        print(json.dumps(report, ensure_ascii=False, indent=2, default=dict))
    else:
        _print_report(report)
    return 1 if report["failures"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
