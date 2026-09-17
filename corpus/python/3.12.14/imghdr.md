---
collection: python
version: "3.12.14"
title: "imghdr — Determine the type of an image"
source_url: https://docs.python.org/3.12/library/imghdr.html
fetched_at: 2026-09-17T15:35:38+00:00
---
# `imghdr` — Determine the type of an image

**Source code:** [Lib/imghdr.py](https://github.com/python/cpython/tree/3.12/Lib/imghdr.py)

Deprecated since version 3.11, will be removed in version 3.13: The [`imghdr`](imghdr.md#module-imghdr "imghdr: Determine the type of image contained in a file or byte stream. (deprecated)") module is deprecated
(see [**PEP 594**](https://peps.python.org/pep-0594/#imghdr) for details and alternatives).

---

The [`imghdr`](imghdr.md#module-imghdr "imghdr: Determine the type of image contained in a file or byte stream. (deprecated)") module determines the type of image contained in a file or
byte stream.

The [`imghdr`](imghdr.md#module-imghdr "imghdr: Determine the type of image contained in a file or byte stream. (deprecated)") module defines the following function:

`imghdr.what(file, h=None)`
:   Test the image data contained in the file named *file* and return a
    string describing the image type. If *h* is provided, the *file*
    argument is ignored and *h* is assumed to contain the byte stream to test.

    Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.12/glossary.html#term-path-like-object).

The following image types are recognized, as listed below with the return value
from [`what()`](imghdr.md#imghdr.what "imghdr.what"):

| Value | Image format |
| --- | --- |
| `'rgb'` | SGI ImgLib Files |
| `'gif'` | GIF 87a and 89a Files |
| `'pbm'` | Portable Bitmap Files |
| `'pgm'` | Portable Graymap Files |
| `'ppm'` | Portable Pixmap Files |
| `'tiff'` | TIFF Files |
| `'rast'` | Sun Raster Files |
| `'xbm'` | X Bitmap Files |
| `'jpeg'` | JPEG data in JFIF or Exif formats |
| `'bmp'` | BMP files |
| `'png'` | Portable Network Graphics |
| `'webp'` | WebP files |
| `'exr'` | OpenEXR Files |

Added in version 3.5: The *exr* and *webp* formats were added.

You can extend the list of file types [`imghdr`](imghdr.md#module-imghdr "imghdr: Determine the type of image contained in a file or byte stream. (deprecated)") can recognize by appending
to this variable:

`imghdr.tests`
:   A list of functions performing the individual tests. Each function takes two
    arguments: the byte-stream and an open file-like object. When [`what()`](imghdr.md#imghdr.what "imghdr.what") is
    called with a byte-stream, the file-like object will be `None`.

    The test function should return a string describing the image type if the test
    succeeded, or `None` if it failed.

Example:

```python3
>>> import imghdr
>>> imghdr.what('bass.gif')
'gif'
```
