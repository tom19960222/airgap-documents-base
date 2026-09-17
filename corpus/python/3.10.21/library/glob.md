---
collection: python
version: "3.10.21"
title: "glob — Unix style pathname pattern expansion"
source_url: https://docs.python.org/3.10/library/glob.html
fetched_at: 2026-09-17T15:13:47+00:00
---
# `glob` — Unix style pathname pattern expansion

**Source code:** [Lib/glob.py](https://github.com/python/cpython/tree/3.10/Lib/glob.py)

---

The [`glob`](glob.md#module-glob "glob: Unix shell style pathname pattern expansion.") module finds all the pathnames matching a specified pattern
according to the rules used by the Unix shell, although results are returned in
arbitrary order. No tilde expansion is done, but `*`, `?`, and character
ranges expressed with `[]` will be correctly matched. This is done by using
the [`os.scandir()`](os.md#os.scandir "os.scandir") and [`fnmatch.fnmatch()`](fnmatch.md#fnmatch.fnmatch "fnmatch.fnmatch") functions in concert, and
not by actually invoking a subshell.

Note that files beginning with a dot (`.`) can only be matched by
patterns that also start with a dot,
unlike [`fnmatch.fnmatch()`](fnmatch.md#fnmatch.fnmatch "fnmatch.fnmatch") or [`pathlib.Path.glob()`](pathlib.md#pathlib.Path.glob "pathlib.Path.glob").
(For tilde and shell variable expansion, use [`os.path.expanduser()`](os.path.md#os.path.expanduser "os.path.expanduser") and
[`os.path.expandvars()`](os.path.md#os.path.expandvars "os.path.expandvars").)

For a literal match, wrap the meta-characters in brackets.
For example, `'[?]'` matches the character `'?'`.

> **See also:**
>
> The [`pathlib`](pathlib.md#module-pathlib "pathlib: Object-oriented filesystem paths") module offers high-level path objects.

`glob.glob(pathname, *, root_dir=None, dir_fd=None, recursive=False)`
:   Return a possibly empty list of path names that match *pathname*, which must be
    a string containing a path specification. *pathname* can be either absolute
    (like `/usr/src/Python-1.5/Makefile`) or relative (like
    `../../Tools/*/*.gif`), and can contain shell-style wildcards. Broken
    symlinks are included in the results (as in the shell). Whether or not the
    results are sorted depends on the file system. If a file that satisfies
    conditions is removed or added during the call of this function, whether
    a path name for that file be included is unspecified.

    If *root_dir* is not `None`, it should be a [path-like object](https://docs.python.org/3.10/glossary.html#term-path-like-object)
    specifying the root directory for searching. It has the same effect on
    [`glob()`](glob.md#module-glob "glob: Unix shell style pathname pattern expansion.") as changing the current directory before calling it. If
    *pathname* is relative, the result will contain paths relative to
    *root_dir*.

    This function can support [paths relative to directory descriptors](os.md#dir-fd) with the *dir_fd* parameter.

    If *recursive* is true, the pattern “`**`” will match any files and zero or
    more directories, subdirectories and symbolic links to directories. If the
    pattern is followed by an [`os.sep`](os.md#os.sep "os.sep") or [`os.altsep`](os.md#os.altsep "os.altsep") then files will not
    match.

    Raises an [auditing event](sys.md#auditing) `glob.glob` with arguments `pathname`, `recursive`.

    Raises an [auditing event](sys.md#auditing) `glob.glob/2` with arguments `pathname`, `recursive`, `root_dir`, `dir_fd`.

    > **Note:**
    >
    > Using the “`**`” pattern in large directory trees may consume
    > an inordinate amount of time.

    Changed in version 3.5: Support for recursive globs using “`**`”.

    Changed in version 3.10: Added the *root_dir* and *dir_fd* parameters.

`glob.iglob(pathname, *, root_dir=None, dir_fd=None, recursive=False)`
:   Return an [iterator](https://docs.python.org/3.10/glossary.html#term-iterator) which yields the same values as [`glob()`](glob.md#module-glob "glob: Unix shell style pathname pattern expansion.")
    without actually storing them all simultaneously.

    Raises an [auditing event](sys.md#auditing) `glob.glob` with arguments `pathname`, `recursive`.

    Raises an [auditing event](sys.md#auditing) `glob.glob/2` with arguments `pathname`, `recursive`, `root_dir`, `dir_fd`.

    Changed in version 3.5: Support for recursive globs using “`**`”.

    Changed in version 3.10: Added the *root_dir* and *dir_fd* parameters.

`glob.escape(pathname)`
:   Escape all special characters (`'?'`, `'*'` and `'['`).
    This is useful if you want to match an arbitrary literal string that may
    have special characters in it. Special characters in drive/UNC
    sharepoints are not escaped, e.g. on Windows
    `escape('//?/c:/Quo vadis?.txt')` returns `'//?/c:/Quo vadis[?].txt'`.

    New in version 3.4.

For example, consider a directory containing the following files:
`1.gif`, `2.txt`, `card.gif` and a subdirectory `sub`
which contains only the file `3.txt`. [`glob()`](glob.md#module-glob "glob: Unix shell style pathname pattern expansion.") will produce
the following results. Notice how any leading components of the path are
preserved.

```python3
>>> import glob
>>> glob.glob('./[0-9].*')
['./1.gif', './2.txt']
>>> glob.glob('*.gif')
['1.gif', 'card.gif']
>>> glob.glob('?.gif')
['1.gif']
>>> glob.glob('**/*.txt', recursive=True)
['2.txt', 'sub/3.txt']
>>> glob.glob('./**/', recursive=True)
['./', './sub/']
```

If the directory contains files starting with `.` they won’t be matched by
default. For example, consider a directory containing `card.gif` and
`.card.gif`:

```python3
>>> import glob
>>> glob.glob('*.gif')
['card.gif']
>>> glob.glob('.c*')
['.card.gif']
```

> **See also:**
>
> Module [`fnmatch`](fnmatch.md#module-fnmatch "fnmatch: Unix shell style filename pattern matching.")
> :   Shell-style filename (not path) expansion
