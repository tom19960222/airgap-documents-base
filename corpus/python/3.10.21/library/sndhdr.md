---
collection: python
version: "3.10.21"
title: "sndhdr — Determine type of sound file"
source_url: https://docs.python.org/3.10/library/sndhdr.html
fetched_at: 2026-09-17T15:15:25+00:00
---
# `sndhdr` — Determine type of sound file

**Source code:** [Lib/sndhdr.py](https://github.com/python/cpython/tree/3.10/Lib/sndhdr.py)

Deprecated since version 3.11: The [`sndhdr`](sndhdr.md#module-sndhdr "sndhdr: Determine type of a sound file. (deprecated)") module is deprecated
(see [**PEP 594**](https://www.python.org/dev/peps/pep-0594#sndhdr) for details and alternatives).

---

The [`sndhdr`](sndhdr.md#module-sndhdr "sndhdr: Determine type of a sound file. (deprecated)") provides utility functions which attempt to determine the type
of sound data which is in a file. When these functions are able to determine
what type of sound data is stored in a file, they return a
[`namedtuple()`](collections.md#collections.namedtuple "collections.namedtuple"), containing five attributes: (`filetype`,
`framerate`, `nchannels`, `nframes`, `sampwidth`). The value for *type*
indicates the data type and will be one of the strings `'aifc'`, `'aiff'`,
`'au'`, `'hcom'`, `'sndr'`, `'sndt'`, `'voc'`, `'wav'`, `'8svx'`,
`'sb'`, `'ub'`, or `'ul'`. The *sampling_rate* will be either the actual
value or `0` if unknown or difficult to decode. Similarly, *channels* will be
either the number of channels or `0` if it cannot be determined or if the
value is difficult to decode. The value for *frames* will be either the number
of frames or `-1`. The last item in the tuple, *bits_per_sample*, will either
be the sample size in bits or `'A'` for A-LAW or `'U'` for u-LAW.

`sndhdr.what(filename)`
:   Determines the type of sound data stored in the file *filename* using
    [`whathdr()`](sndhdr.md#sndhdr.whathdr "sndhdr.whathdr"). If it succeeds, returns a namedtuple as described above, otherwise
    `None` is returned.

    Changed in version 3.5: Result changed from a tuple to a namedtuple.

`sndhdr.whathdr(filename)`
:   Determines the type of sound data stored in a file based on the file header.
    The name of the file is given by *filename*. This function returns a namedtuple as
    described above on success, or `None`.

    Changed in version 3.5: Result changed from a tuple to a namedtuple.
