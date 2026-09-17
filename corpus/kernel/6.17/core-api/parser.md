---
collection: kernel
version: "6.17"
title: "Generic parser"
source_url: https://www.kernel.org/doc/html/v6.17/core-api/parser.html
fetched_at: 2026-09-16T16:19:09+00:00
---
# Generic parser

## Overview

The generic parser is a simple parser for parsing mount options,
filesystem options, driver options, subsystem options, etc.

## Parser API

int match_token(char \*s, const match_table_t table, substring_t args[])
:   Find a token (and optional args) in a string

**Parameters**

`char *s`
:   the string to examine for token/argument pairs

`const match_table_t table`
:   match_table_t describing the set of allowed option tokens and the
    arguments that may be associated with them. Must be terminated with a
    [`struct match_token`](parser.md#c.match_token "match_token") whose pattern is set to the NULL pointer.

`substring_t args[]`
:   array of `MAX_OPT_ARGS` `substring_t` elements. Used to return match
    locations.

**Description**

Detects which if any of a set of token strings has been passed
to it. Tokens can include up to `MAX_OPT_ARGS` instances of basic c-style
format identifiers which will be taken into account when matching the
tokens, and whose locations will be returned in the **args** array.

int match_int(substring_t \*s, int \*result)
:   scan a decimal representation of an integer from a substring_t

**Parameters**

`substring_t *s`
:   substring_t to be scanned

`int *result`
:   resulting integer on success

**Description**

Attempts to parse the `substring_t` **s** as a decimal integer.

**Return**

On success, sets **result** to the integer represented by the string
and returns 0. Returns -EINVAL or -ERANGE on failure.

int match_uint(substring_t \*s, unsigned int \*result)
:   scan a decimal representation of an integer from a substring_t

**Parameters**

`substring_t *s`
:   substring_t to be scanned

`unsigned int *result`
:   resulting integer on success

**Description**

Attempts to parse the `substring_t` **s** as a decimal integer.

**Return**

On success, sets **result** to the integer represented by the string
and returns 0. Returns -EINVAL or -ERANGE on failure.

int match_u64(substring_t \*s, u64 \*result)
:   scan a decimal representation of a u64 from a substring_t

**Parameters**

`substring_t *s`
:   substring_t to be scanned

`u64 *result`
:   resulting unsigned long long on success

**Description**

Attempts to parse the `substring_t` **s** as a long decimal
integer.

**Return**

On success, sets **result** to the integer represented by the string
and returns 0. Returns -EINVAL or -ERANGE on failure.

int match_octal(substring_t \*s, int \*result)
:   scan an octal representation of an integer from a substring_t

**Parameters**

`substring_t *s`
:   substring_t to be scanned

`int *result`
:   resulting integer on success

**Description**

Attempts to parse the `substring_t` **s** as an octal integer.

**Return**

On success, sets **result** to the integer represented by the string
and returns 0. Returns -EINVAL or -ERANGE on failure.

int match_hex(substring_t \*s, int \*result)
:   scan a hex representation of an integer from a substring_t

**Parameters**

`substring_t *s`
:   substring_t to be scanned

`int *result`
:   resulting integer on success

**Description**

Attempts to parse the `substring_t` **s** as a hexadecimal integer.

**Return**

On success, sets **result** to the integer represented by the string
and returns 0. Returns -EINVAL or -ERANGE on failure.

bool match_wildcard(const char \*pattern, const char \*str)
:   parse if a string matches given wildcard pattern

**Parameters**

`const char *pattern`
:   wildcard pattern

`const char *str`
:   the string to be parsed

**Description**

Parse the string **str** to check if matches wildcard
pattern **pattern**. The pattern may contain two types of wildcards:

- ‘\*’ - matches zero or more characters
- ‘?’ - matches one character

**Return**

If the **str** matches the **pattern**, return true, else return false.

size_t match_strlcpy(char \*dest, const substring_t \*src, size_t size)
:   Copy the characters from a substring_t to a sized buffer

**Parameters**

`char *dest`
:   where to copy to

`const substring_t *src`
:   `substring_t` to copy

`size_t size`
:   size of destination buffer

**Description**

Copy the characters in `substring_t` **src** to the
c-style string **dest**. Copy no more than **size** - 1 characters, plus
the terminating NUL.

**Return**

length of **src**.

char \*match_strdup(const substring_t \*s)
:   allocate a new string with the contents of a substring_t

**Parameters**

`const substring_t *s`
:   `substring_t` to copy

**Description**

Allocates and returns a string filled with the contents of
the `substring_t` **s**. The caller is responsible for freeing the returned
string with [`kfree()`](mm-api.md#c.kfree "kfree").

**Return**

the address of the newly allocated NUL-terminated string or
`NULL` on error.
