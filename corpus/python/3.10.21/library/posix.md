---
collection: python
version: "3.10.21"
title: "posix — The most common POSIX system calls"
source_url: https://docs.python.org/3.10/library/posix.html
fetched_at: 2026-09-17T15:15:13+00:00
---
# `posix` — The most common POSIX system calls

---

This module provides access to operating system functionality that is
standardized by the C Standard and the POSIX standard (a thinly disguised Unix
interface).

**Do not import this module directly.** Instead, import the module [`os`](os.md#module-os "os: Miscellaneous operating system interfaces."),
which provides a *portable* version of this interface. On Unix, the [`os`](os.md#module-os "os: Miscellaneous operating system interfaces.")
module provides a superset of the [`posix`](posix.md#module-posix "posix: The most common POSIX system calls (normally used via module os). (Unix)") interface. On non-Unix operating
systems the [`posix`](posix.md#module-posix "posix: The most common POSIX system calls (normally used via module os). (Unix)") module is not available, but a subset is always
available through the [`os`](os.md#module-os "os: Miscellaneous operating system interfaces.") interface. Once [`os`](os.md#module-os "os: Miscellaneous operating system interfaces.") is imported, there is
*no* performance penalty in using it instead of [`posix`](posix.md#module-posix "posix: The most common POSIX system calls (normally used via module os). (Unix)"). In addition,
[`os`](os.md#module-os "os: Miscellaneous operating system interfaces.") provides some additional functionality, such as automatically calling
[`putenv()`](os.md#os.putenv "os.putenv") when an entry in `os.environ` is changed.

Errors are reported as exceptions; the usual exceptions are given for type
errors, while errors reported by the system calls raise [`OSError`](exceptions.md#OSError "OSError").

## Large File Support

Several operating systems (including AIX and Solaris) provide
support for files that are larger than 2 GiB from a C programming model where
`int` and `long` are 32-bit values. This is typically accomplished
by defining the relevant size and offset types as 64-bit values. Such files are
sometimes referred to as *large files*.

Large file support is enabled in Python when the size of an `off_t` is
larger than a `long` and the `long long` is at least as large
as an `off_t`.
It may be necessary to configure and compile Python with certain compiler flags
to enable this mode. For example, with Solaris 2.6 and 2.7 you need to do
something like:

```python3
CFLAGS="`getconf LFS_CFLAGS`" OPT="-g -O2 $CFLAGS" \
        ./configure
```

On large-file-capable Linux systems, this might work:

```python3
CFLAGS='-D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64' OPT="-g -O2 $CFLAGS" \
        ./configure
```

## Notable Module Contents

In addition to many functions described in the [`os`](os.md#module-os "os: Miscellaneous operating system interfaces.") module documentation,
[`posix`](posix.md#module-posix "posix: The most common POSIX system calls (normally used via module os). (Unix)") defines the following data item:

`posix.environ`
:   A dictionary representing the string environment at the time the interpreter
    was started. Keys and values are bytes on Unix and str on Windows. For
    example, `environ[b'HOME']` (`environ['HOME']` on Windows) is the
    pathname of your home directory, equivalent to `getenv("HOME")` in C.

    Modifying this dictionary does not affect the string environment passed on by
    [`execv()`](os.md#os.execv "os.execv"), [`popen()`](os.md#os.popen "os.popen") or [`system()`](os.md#os.system "os.system"); if you need to
    change the environment, pass `environ` to [`execve()`](os.md#os.execve "os.execve") or add
    variable assignments and export statements to the command string for
    [`system()`](os.md#os.system "os.system") or [`popen()`](os.md#os.popen "os.popen").

    Changed in version 3.2: On Unix, keys and values are bytes.

    > **Note:**
    >
    > The [`os`](os.md#module-os "os: Miscellaneous operating system interfaces.") module provides an alternate implementation of `environ`
    > which updates the environment on modification. Note also that updating
    > [`os.environ`](os.md#os.environ "os.environ") will render this dictionary obsolete. Use of the
    > [`os`](os.md#module-os "os: Miscellaneous operating system interfaces.") module version of this is recommended over direct access to the
    > [`posix`](posix.md#module-posix "posix: The most common POSIX system calls (normally used via module os). (Unix)") module.
