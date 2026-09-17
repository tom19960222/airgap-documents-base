import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from crawl import response_text

PAGE = "<html><head><meta charset=\"utf-8\"></head><body><p>os — 說明</p></body></html>"


class FakeResponse:
    """requests.Response 的最小替身：只有 response_text 會用到的部分。"""

    def __init__(self, content: bytes, content_type: str, encoding: str | None):
        self.content = content
        self.headers = {"content-type": content_type}
        self.encoding = encoding

    @property
    def apparent_encoding(self) -> str:
        return "utf-8"

    @property
    def text(self) -> str:
        return self.content.decode(self.encoding or "utf-8", "replace")


class ResponseTextTests(unittest.TestCase):
    def test_meta_charset_wins_when_the_header_omits_one(self):
        # requests 對沒有 charset 的 text/* 會把 encoding 設成 ISO-8859-1。
        resp = FakeResponse(PAGE.encode("utf-8"), "text/html", "ISO-8859-1")
        self.assertEqual(response_text(resp), PAGE)

    def test_header_charset_is_trusted(self):
        resp = FakeResponse(PAGE.encode("utf-8"), "text/html; charset=utf-8", "utf-8")
        self.assertEqual(response_text(resp), PAGE)

    def test_falls_back_to_content_detection_without_any_declaration(self):
        body = "<html><body><p>os — 說明</p></body></html>"
        resp = FakeResponse(body.encode("utf-8"), "text/html", "ISO-8859-1")
        self.assertEqual(response_text(resp), body)

    def test_unknown_declared_codec_does_not_crash(self):
        body = '<html><head><meta charset="x-not-a-codec"></head><body>ok</body></html>'
        resp = FakeResponse(body.encode("utf-8"), "text/html", "ISO-8859-1")
        self.assertEqual(response_text(resp), body)


if __name__ == "__main__":
    unittest.main()
