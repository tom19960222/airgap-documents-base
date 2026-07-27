"""BFS 爬取 manifest 指定的文件站，存成 raw archive。

用法：python crawl.py manifests/ceph-19.toml [--max-pages N]

頁面身分以 redirect 後的 canonical URL 為準：跳轉出範圍的不保存、不抽連結，
被跳轉合併的 URL 只記一筆 alias。可中斷重跑：只有「HTML 已落盤」的頁面算完成，
transport error 與未落盤的條目會在下次執行時重試。
"""

from __future__ import annotations

import argparse
import gzip
import json
import sys
import time
from collections import deque
from datetime import datetime, timezone
from hashlib import sha256

import requests
from bs4 import BeautifulSoup

from common import Manifest, canonicalize, in_scope, load_manifest, url_key

USER_AGENT = "airgap-documents-base/0.1 (docs archiver for offline use)"


def extract_links(html: str, page_url: str, manifest: Manifest) -> list[str]:
    soup = BeautifulSoup(html, "lxml")
    links = []
    for a in soup.find_all("a", href=True):
        url = canonicalize(a["href"], page_url)
        if in_scope(url, manifest):
            links.append(url)
    return links


def load_done(manifest: Manifest) -> dict[str, dict]:
    """讀取並壓實 pages.jsonl。

    只保留可信條目：已落盤的頁（archived）、alias、確定的非 HTML。
    壞掉的半行（中斷殘留）與 transport/HTTP error 一律丟棄，讓這次重試。
    """
    index_path = manifest.raw_dir / "pages.jsonl"
    pages_dir = manifest.raw_dir / "pages"
    done: dict[str, dict] = {}
    if not index_path.exists():
        return done
    for line in index_path.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        url = entry.get("url")
        if not url:
            continue
        if entry.get("archived"):
            if (pages_dir / f"{url_key(url)}.html.gz").exists():
                done[url] = entry
        elif entry.get("alias") or entry.get("non_html"):
            done[url] = entry
    with index_path.open("w") as f:
        for entry in done.values():
            f.write(json.dumps(entry) + "\n")
    return done


def crawl(manifest: Manifest, max_pages: int) -> None:
    pages_dir = manifest.raw_dir / "pages"
    pages_dir.mkdir(parents=True, exist_ok=True)
    index_path = manifest.raw_dir / "pages.jsonl"

    done = load_done(manifest)
    queue = deque([manifest.base_url])
    seen = {manifest.base_url}
    session = requests.Session()
    session.headers["User-Agent"] = USER_AGENT
    archived_count = sum(1 for e in done.values() if e.get("archived"))
    errors = 0

    def enqueue(url: str) -> None:
        if url not in seen:
            seen.add(url)
            queue.append(url)

    def enqueue_links(html: str, page_url: str) -> None:
        for link in extract_links(html, page_url, manifest):
            enqueue(link)

    def record(index_file, entry: dict) -> None:
        done[entry["url"]] = entry
        index_file.write(json.dumps(entry) + "\n")
        index_file.flush()

    with index_path.open("a") as index_file:
        while queue and archived_count < max_pages:
            url = queue.popleft()

            if url in done:
                entry = done[url]
                if entry.get("archived"):
                    html_path = pages_dir / f"{url_key(url)}.html.gz"
                    html = gzip.decompress(html_path.read_bytes()).decode("utf-8", "replace")
                    enqueue_links(html, url)
                elif entry.get("alias") and in_scope(entry.get("final_url", ""), manifest):
                    enqueue(entry["final_url"])
                continue

            try:
                resp = session.get(url, timeout=30)
            except requests.RequestException as exc:
                print(f"ERROR {url}: {exc}", file=sys.stderr)
                errors += 1
                time.sleep(manifest.delay_seconds)
                continue  # 不記入 done：下次執行重試

            final = canonicalize(resp.url, resp.url)
            fetched_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
            content_type = resp.headers.get("content-type", "")

            if final != url:
                record(index_file, {
                    "url": url, "final_url": final, "status": resp.status_code,
                    "alias": True, "fetched_at": fetched_at,
                })
                if not in_scope(final, manifest):
                    time.sleep(manifest.delay_seconds)
                    continue  # 跳轉出範圍：不保存、不抽連結
                url = final  # 內容以 canonical URL 身分處理
                if url in done:
                    time.sleep(manifest.delay_seconds)
                    continue
                seen.add(url)

            if resp.status_code != 200:
                errors += 1  # HTTP error 不記入 done，下次重試
            elif "text/html" not in content_type:
                record(index_file, {
                    "url": url, "status": 200, "non_html": True,
                    "content_type": content_type, "fetched_at": fetched_at,
                })
            else:
                html = resp.text
                (pages_dir / f"{url_key(url)}.html.gz").write_bytes(gzip.compress(html.encode()))
                record(index_file, {
                    "url": url, "status": 200, "archived": True, "fetched_at": fetched_at,
                    "content_hash": "sha256:" + sha256(html.encode()).hexdigest(),
                })
                archived_count += 1
                enqueue_links(html, url)
                if archived_count % 25 == 0:
                    print(f"[{manifest.name}] archived {archived_count}, queue {len(queue)}")

            time.sleep(manifest.delay_seconds)

    print(f"[{manifest.name}] done: {archived_count} pages archived, "
          f"{errors} errors (will retry next run), queue left {len(queue)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest")
    parser.add_argument("--max-pages", type=int, default=None)
    args = parser.parse_args()
    manifest = load_manifest(args.manifest)
    crawl(manifest, args.max_pages or manifest.max_pages)


if __name__ == "__main__":
    main()
