import sys
import unittest
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from crawl import decode_html


def make_response(body: bytes, content_type: str) -> requests.Response:
    resp = requests.Response()
    resp._content = body
    resp.status_code = 200
    resp.headers["content-type"] = content_type
    resp.encoding = requests.utils.get_encoding_from_headers(resp.headers)
    return resp


class DecodeHtmlTests(unittest.TestCase):
    def test_utf8_page_without_header_charset_uses_meta_charset(self):
        # docs.python.org serves bare ``text/html``; requests would fall back to
        # ISO-8859-1 and mojibake every non-ASCII character.
        body = '<meta charset="utf-8"><h1>os.path — pathnames</h1>'.encode()
        self.assertIn("—", decode_html(make_response(body, "text/html")))

    def test_header_charset_wins_over_document_declaration(self):
        body = '<meta charset="utf-8"><p>caf\xe9</p>'.encode("iso-8859-1")
        resp = make_response(body, "text/html; charset=iso-8859-1")
        self.assertIn("café", decode_html(resp))

    def test_http_equiv_content_type_is_honored(self):
        body = (
            '<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">'
            "<p>caf\xe9</p>"
        ).encode("iso-8859-1")
        self.assertIn("café", decode_html(make_response(body, "text/html")))

    def test_undeclared_charset_defaults_to_utf8(self):
        body = "<p>café</p>".encode()
        self.assertIn("café", decode_html(make_response(body, "text/html")))

    def test_unknown_declared_charset_falls_back_to_utf8(self):
        body = '<meta charset="x-nonexistent-codec"><p>café</p>'.encode()
        self.assertIn("café", decode_html(make_response(body, "text/html")))

    def test_undecodable_bytes_are_replaced_instead_of_raising(self):
        body = b'<meta charset="utf-8"><p>\xff\xfe</p>'
        self.assertIn("�", decode_html(make_response(body, "text/html")))


if __name__ == "__main__":
    unittest.main()
