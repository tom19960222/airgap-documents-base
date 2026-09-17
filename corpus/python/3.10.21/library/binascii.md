---
collection: python
version: "3.10.21"
title: "binascii — Convert between binary and ASCII"
source_url: https://docs.python.org/3.10/library/binascii.html
fetched_at: 2026-09-17T15:14:19+00:00
---
# `binascii` — Convert between binary and ASCII

---

The [`binascii`](binascii.md#module-binascii "binascii: Tools for converting between binary and various ASCII-encoded binary representations.") module contains a number of methods to convert between
binary and various ASCII-encoded binary representations. Normally, you will not
use these functions directly but use wrapper modules like [`uu`](uu.md#module-uu "uu: Encode and decode files in uuencode format. (deprecated)"),
[`base64`](base64.md#module-base64 "base64: RFC 4648: Base16, Base32, Base64 Data Encodings; Base85 and Ascii85"), or [`binhex`](binhex.md#module-binhex "binhex: Encode and decode files in binhex4 format.") instead. The [`binascii`](binascii.md#module-binascii "binascii: Tools for converting between binary and various ASCII-encoded binary representations.") module contains
low-level functions written in C for greater speed that are used by the
higher-level modules.

> **Note:**
>
> `a2b_*` functions accept Unicode strings containing only ASCII characters.
> Other functions only accept [bytes-like objects](https://docs.python.org/3.10/glossary.html#term-bytes-like-object) (such as
> [`bytes`](stdtypes.md#bytes "bytes"), [`bytearray`](stdtypes.md#bytearray "bytearray") and other objects that support the buffer
> protocol).
>
> Changed in version 3.3: ASCII-only unicode strings are now accepted by the `a2b_*` functions.

The [`binascii`](binascii.md#module-binascii "binascii: Tools for converting between binary and various ASCII-encoded binary representations.") module defines the following functions:

`binascii.a2b_uu(string)`
:   Convert a single line of uuencoded data back to binary and return the binary
    data. Lines normally contain 45 (binary) bytes, except for the last line. Line
    data may be followed by whitespace.

`binascii.b2a_uu(data, *, backtick=False)`
:   Convert binary data to a line of ASCII characters, the return value is the
    converted line, including a newline char. The length of *data* should be at most
    45. If *backtick* is true, zeros are represented by `` '`' `` instead of spaces.

    Changed in version 3.7: Added the *backtick* parameter.

`binascii.a2b_base64(string)`
:   Convert a block of base64 data back to binary and return the binary data. More
    than one line may be passed at a time.

`binascii.b2a_base64(data, *, newline=True)`
:   Convert binary data to a line of ASCII characters in base64 coding. The return
    value is the converted line, including a newline char if *newline* is
    true. The output of this function conforms to [**RFC 3548**](https://datatracker.ietf.org/doc/html/rfc3548.html).

    Changed in version 3.6: Added the *newline* parameter.

`binascii.a2b_qp(data, header=False)`
:   Convert a block of quoted-printable data back to binary and return the binary
    data. More than one line may be passed at a time. If the optional argument
    *header* is present and true, underscores will be decoded as spaces.

`binascii.b2a_qp(data, quotetabs=False, istext=True, header=False)`
:   Convert binary data to a line(s) of ASCII characters in quoted-printable
    encoding. The return value is the converted line(s). If the optional argument
    *quotetabs* is present and true, all tabs and spaces will be encoded. If the
    optional argument *istext* is present and true, newlines are not encoded but
    trailing whitespace will be encoded. If the optional argument *header* is
    present and true, spaces will be encoded as underscores per [**RFC 1522**](https://datatracker.ietf.org/doc/html/rfc1522.html). If the
    optional argument *header* is present and false, newline characters will be
    encoded as well; otherwise linefeed conversion might corrupt the binary data
    stream.

`binascii.a2b_hqx(string)`
:   Convert binhex4 formatted ASCII data to binary, without doing RLE-decompression.
    The string should contain a complete number of binary bytes, or (in case of the
    last portion of the binhex4 data) have the remaining bits zero.

    Deprecated since version 3.9.

`binascii.rledecode_hqx(data)`
:   Perform RLE-decompression on the data, as per the binhex4 standard. The
    algorithm uses `0x90` after a byte as a repeat indicator, followed by a count.
    A count of `0` specifies a byte value of `0x90`. The routine returns the
    decompressed data, unless data input data ends in an orphaned repeat indicator,
    in which case the [`Incomplete`](binascii.md#binascii.Incomplete "binascii.Incomplete") exception is raised.

    Changed in version 3.2: Accept only bytestring or bytearray objects as input.

    Deprecated since version 3.9.

`binascii.rlecode_hqx(data)`
:   Perform binhex4 style RLE-compression on *data* and return the result.

    Deprecated since version 3.9.

`binascii.b2a_hqx(data)`
:   Perform hexbin4 binary-to-ASCII translation and return the resulting string. The
    argument should already be RLE-coded, and have a length divisible by 3 (except
    possibly the last fragment).

    Deprecated since version 3.9.

`binascii.crc_hqx(data, value)`
:   Compute a 16-bit CRC value of *data*, starting with *value* as the
    initial CRC, and return the result. This uses the CRC-CCITT polynomial
    *x*16 + *x*12 + *x*5 + 1, often represented as
    0x1021. This CRC is used in the binhex4 format.

`binascii.crc32(data[, value])`
:   Compute CRC-32, the unsigned 32-bit checksum of *data*, starting with an
    initial CRC of *value*. The default initial CRC is zero. The algorithm
    is consistent with the ZIP file checksum. Since the algorithm is designed for
    use as a checksum algorithm, it is not suitable for use as a general hash
    algorithm. Use as follows:

    ```python3
    print(binascii.crc32(b"hello world"))
    # Or, in two pieces:
    crc = binascii.crc32(b"hello")
    crc = binascii.crc32(b" world", crc)
    print('crc32 = {:#010x}'.format(crc))
    ```

    Changed in version 3.0: The result is always unsigned.
    To generate the same numeric value when using Python 2 or earlier,
    use `crc32(data) & 0xffffffff`.

`binascii.b2a_hex(data[, sep[, bytes_per_sep=1]])`

`binascii.hexlify(data[, sep[, bytes_per_sep=1]])`
:   Return the hexadecimal representation of the binary *data*. Every byte of
    *data* is converted into the corresponding 2-digit hex representation. The
    returned bytes object is therefore twice as long as the length of *data*.

    Similar functionality (but returning a text string) is also conveniently
    accessible using the [`bytes.hex()`](stdtypes.md#bytes.hex "bytes.hex") method.

    If *sep* is specified, it must be a single character str or bytes object.
    It will be inserted in the output after every *bytes_per_sep* input bytes.
    Separator placement is counted from the right end of the output by default,
    if you wish to count from the left, supply a negative *bytes_per_sep* value.

    ```
    >>> import binascii
    >>> binascii.b2a_hex(b'\xb9\x01\xef')
    b'b901ef'
    >>> binascii.hexlify(b'\xb9\x01\xef', '-')
    b'b9-01-ef'
    >>> binascii.b2a_hex(b'\xb9\x01\xef', b'_', 2)
    b'b9_01ef'
    >>> binascii.b2a_hex(b'\xb9\x01\xef', b' ', -2)
    b'b901 ef'
    ```

    Changed in version 3.8: The *sep* and *bytes_per_sep* parameters were added.

`binascii.a2b_hex(hexstr)`

`binascii.unhexlify(hexstr)`
:   Return the binary data represented by the hexadecimal string *hexstr*. This
    function is the inverse of [`b2a_hex()`](binascii.md#binascii.b2a_hex "binascii.b2a_hex"). *hexstr* must contain an even number
    of hexadecimal digits (which can be upper or lower case), otherwise an
    [`Error`](binascii.md#binascii.Error "binascii.Error") exception is raised.

    Similar functionality (accepting only text string arguments, but more
    liberal towards whitespace) is also accessible using the
    [`bytes.fromhex()`](stdtypes.md#bytes.fromhex "bytes.fromhex") class method.

`exception binascii.Error`
:   Exception raised on errors. These are usually programming errors.

`exception binascii.Incomplete`
:   Exception raised on incomplete data. These are usually not programming errors,
    but may be handled by reading a little more data and trying again.

> **See also:**
>
> Module [`base64`](base64.md#module-base64 "base64: RFC 4648: Base16, Base32, Base64 Data Encodings; Base85 and Ascii85")
> :   Support for RFC compliant base64-style encoding in base 16, 32, 64,
>     and 85.
>
> Module [`binhex`](binhex.md#module-binhex "binhex: Encode and decode files in binhex4 format.")
> :   Support for the binhex format used on the Macintosh.
>
> Module [`uu`](uu.md#module-uu "uu: Encode and decode files in uuencode format. (deprecated)")
> :   Support for UU encoding used on Unix.
>
> Module [`quopri`](quopri.md#module-quopri "quopri: Encode and decode files using the MIME quoted-printable encoding.")
> :   Support for quoted-printable encoding used in MIME email messages.
