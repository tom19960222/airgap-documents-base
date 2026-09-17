---
collection: python
version: "3.12.14"
title: "traceback — Print or retrieve a stack traceback"
source_url: https://docs.python.org/3.12/library/traceback.html
fetched_at: 2026-09-17T15:35:03+00:00
---
# `traceback` — Print or retrieve a stack traceback

**Source code:** [Lib/traceback.py](https://github.com/python/cpython/tree/3.12/Lib/traceback.py)

---

This module provides a standard interface to extract, format and print
stack traces of Python programs. It is more flexible than the
interpreter’s default traceback display, and therefore makes it
possible to configure certain aspects of the output. Finally,
it contains a utility for capturing enough information about an
exception to print it later, without the need to save a reference
to the actual exception. Since exceptions can be the roots of large
objects graph, this utility can significantly improve
memory management.

The module uses [traceback objects](https://docs.python.org/3.12/reference/datamodel.html#traceback-objects) — these are
objects of type [`types.TracebackType`](types.md#types.TracebackType "types.TracebackType"),
which are assigned to the [`__traceback__`](exceptions.md#BaseException.__traceback__ "BaseException.__traceback__") field of
[`BaseException`](exceptions.md#BaseException "BaseException") instances.

> **See also:**
>
> Module [`faulthandler`](faulthandler.md#module-faulthandler "faulthandler: Dump the Python traceback.")
> :   Used to dump Python tracebacks explicitly, on a fault, after a timeout, or on a user signal.
>
> Module [`pdb`](pdb.md#module-pdb "pdb: The Python debugger for interactive interpreters.")
> :   Interactive source code debugger for Python programs.

The module’s API can be divided into two parts:

- Module-level functions offering basic functionality, which are useful for interactive
  inspection of exceptions and tracebacks.
- [`TracebackException`](traceback.md#traceback.TracebackException "traceback.TracebackException") class and its helper classes
  [`StackSummary`](traceback.md#traceback.StackSummary "traceback.StackSummary") and [`FrameSummary`](traceback.md#traceback.FrameSummary "traceback.FrameSummary"). These offer both more
  flexibility in the output generated and the ability to store the information
  necessary for later formatting without holding references to actual exception
  and traceback objects.

## Module-Level Functions

traceback.print_tb(*tb*, *limit=None*, *file=None*)
:   Print up to *limit* stack trace entries from
    [traceback object](https://docs.python.org/3.12/reference/datamodel.html#traceback-objects) *tb* (starting
    from the caller’s frame) if *limit* is positive. Otherwise, print the last
    `abs(limit)` entries. If *limit* is omitted or `None`, all entries are
    printed. If *file* is omitted or `None`, the output goes to
    [`sys.stderr`](sys.md#sys.stderr "sys.stderr"); otherwise it should be an open
    [file](https://docs.python.org/3.12/glossary.html#term-file-object) or [file-like object](https://docs.python.org/3.12/glossary.html#term-file-like-object) to
    receive the output.

    > **Note:**
    >
    > The meaning of the *limit* parameter is different than the meaning
    > of [`sys.tracebacklimit`](sys.md#sys.tracebacklimit "sys.tracebacklimit"). A negative *limit* value corresponds to
    > a positive value of `sys.tracebacklimit`, whereas the behaviour of
    > a positive *limit* value cannot be achieved with
    > `sys.tracebacklimit`.

    Changed in version 3.5: Added negative *limit* support.

traceback.print_exception(*exc*, */*, [*value*, *tb*, ]*limit=None*, *file=None*, *chain=True*)
:   Print exception information and stack trace entries from
    [traceback object](https://docs.python.org/3.12/reference/datamodel.html#traceback-objects)
    *tb* to *file*. This differs from [`print_tb()`](traceback.md#traceback.print_tb "traceback.print_tb") in the following
    ways:

    - if *tb* is not `None`, it prints a header `Traceback (most recent
      call last):`
    - it prints the exception type and *value* after the stack trace

    - if *type(value)* is [`SyntaxError`](exceptions.md#SyntaxError "SyntaxError") and *value* has the appropriate
      format, it prints the line where the syntax error occurred with a caret
      indicating the approximate position of the error.

    Since Python 3.10, instead of passing *value* and *tb*, an exception object
    can be passed as the first argument. If *value* and *tb* are provided, the
    first argument is ignored in order to provide backwards compatibility.

    The optional *limit* argument has the same meaning as for [`print_tb()`](traceback.md#traceback.print_tb "traceback.print_tb").
    If *chain* is true (the default), then chained exceptions (the
    [`__cause__`](exceptions.md#BaseException.__cause__ "BaseException.__cause__") or [`__context__`](exceptions.md#BaseException.__context__ "BaseException.__context__")
    attributes of the exception) will be
    printed as well, like the interpreter itself does when printing an unhandled
    exception.

    Changed in version 3.5: The *etype* argument is ignored and inferred from the type of *value*.

    Changed in version 3.10: The *etype* parameter has been renamed to *exc* and is now
    positional-only.

traceback.print_exc(*limit=None*, *file=None*, *chain=True*)
:   This is a shorthand for `print_exception(sys.exception(), limit=limit, file=file,
    chain=chain)`.

traceback.print_last(*limit=None*, *file=None*, *chain=True*)
:   This is a shorthand for `print_exception(sys.last_exc, limit=limit, file=file,
    chain=chain)`. In general it will work only after an exception has reached
    an interactive prompt (see [`sys.last_exc`](sys.md#sys.last_exc "sys.last_exc")).

traceback.print_stack(*f=None*, *limit=None*, *file=None*)
:   Print up to *limit* stack trace entries (starting from the invocation
    point) if *limit* is positive. Otherwise, print the last `abs(limit)`
    entries. If *limit* is omitted or `None`, all entries are printed.
    The optional *f* argument can be used to specify an alternate
    [stack frame](https://docs.python.org/3.12/reference/datamodel.html#frame-objects)
    to start. The optional *file* argument has the same meaning as for
    [`print_tb()`](traceback.md#traceback.print_tb "traceback.print_tb").

    Changed in version 3.5: Added negative *limit* support.

traceback.extract_tb(*tb*, *limit=None*)
:   Return a [`StackSummary`](traceback.md#traceback.StackSummary "traceback.StackSummary") object representing a list of “pre-processed”
    stack trace entries extracted from the
    [traceback object](https://docs.python.org/3.12/reference/datamodel.html#traceback-objects) *tb*. It is useful
    for alternate formatting of stack traces. The optional *limit* argument has
    the same meaning as for [`print_tb()`](traceback.md#traceback.print_tb "traceback.print_tb"). A “pre-processed” stack trace
    entry is a [`FrameSummary`](traceback.md#traceback.FrameSummary "traceback.FrameSummary") object containing attributes
    [`filename`](traceback.md#traceback.FrameSummary.filename "traceback.FrameSummary.filename"), [`lineno`](traceback.md#traceback.FrameSummary.lineno "traceback.FrameSummary.lineno"),
    [`name`](traceback.md#traceback.FrameSummary.name "traceback.FrameSummary.name"), and [`line`](traceback.md#traceback.FrameSummary.line "traceback.FrameSummary.line") representing the
    information that is usually printed for a stack trace.

traceback.extract_stack(*f=None*, *limit=None*)
:   Extract the raw traceback from the current
    [stack frame](https://docs.python.org/3.12/reference/datamodel.html#frame-objects). The return value has
    the same format as for [`extract_tb()`](traceback.md#traceback.extract_tb "traceback.extract_tb"). The optional *f* and *limit*
    arguments have the same meaning as for [`print_stack()`](traceback.md#traceback.print_stack "traceback.print_stack").

traceback.print_list(*extracted_list*, *file=None*)
:   Print the list of tuples as returned by [`extract_tb()`](traceback.md#traceback.extract_tb "traceback.extract_tb") or
    [`extract_stack()`](traceback.md#traceback.extract_stack "traceback.extract_stack") as a formatted stack trace to the given file.
    If *file* is `None`, the output is written to [`sys.stderr`](sys.md#sys.stderr "sys.stderr").

traceback.format_list(*extracted_list*)
:   Given a list of tuples or [`FrameSummary`](traceback.md#traceback.FrameSummary "traceback.FrameSummary") objects as returned by
    [`extract_tb()`](traceback.md#traceback.extract_tb "traceback.extract_tb") or [`extract_stack()`](traceback.md#traceback.extract_stack "traceback.extract_stack"), return a list of strings ready
    for printing. Each string in the resulting list corresponds to the item with
    the same index in the argument list. Each string ends in a newline; the
    strings may contain internal newlines as well, for those items whose source
    text line is not `None`.

traceback.format_exception_only(*exc*, */*[, *value*])
:   Format the exception part of a traceback using an exception value such as
    given by [`sys.last_value`](sys.md#sys.last_value "sys.last_value"). The return value is a list of strings, each
    ending in a newline. The list contains the exception’s message, which is
    normally a single string; however, for [`SyntaxError`](exceptions.md#SyntaxError "SyntaxError") exceptions, it
    contains several lines that (when printed) display detailed information
    about where the syntax error occurred. Following the message, the list
    contains the exception’s [`notes`](exceptions.md#BaseException.__notes__ "BaseException.__notes__").

    Since Python 3.10, instead of passing *value*, an exception object
    can be passed as the first argument. If *value* is provided, the first
    argument is ignored in order to provide backwards compatibility.

    Changed in version 3.10: The *etype* parameter has been renamed to *exc* and is now
    positional-only.

    Changed in version 3.11: The returned list now includes any
    [`notes`](exceptions.md#BaseException.__notes__ "BaseException.__notes__") attached to the exception.

traceback.format_exception(*exc*, */*, [*value*, *tb*, ]*limit=None*, *chain=True*)
:   Format a stack trace and the exception information. The arguments have the
    same meaning as the corresponding arguments to [`print_exception()`](traceback.md#traceback.print_exception "traceback.print_exception"). The
    return value is a list of strings, each ending in a newline and some
    containing internal newlines. When these lines are concatenated and printed,
    exactly the same text is printed as does [`print_exception()`](traceback.md#traceback.print_exception "traceback.print_exception").

    Changed in version 3.5: The *etype* argument is ignored and inferred from the type of *value*.

    Changed in version 3.10: This function’s behavior and signature were modified to match
    [`print_exception()`](traceback.md#traceback.print_exception "traceback.print_exception").

traceback.format_exc(*limit=None*, *chain=True*)
:   This is like `print_exc(limit)` but returns a string instead of printing to
    a file.

traceback.format_tb(*tb*, *limit=None*)
:   A shorthand for `format_list(extract_tb(tb, limit))`.

traceback.format_stack(*f=None*, *limit=None*)
:   A shorthand for `format_list(extract_stack(f, limit))`.

traceback.clear_frames(*tb*)
:   Clears the local variables of all the stack frames in a
    [traceback](https://docs.python.org/3.12/reference/datamodel.html#traceback-objects) *tb*
    by calling the [`clear()`](https://docs.python.org/3.12/reference/datamodel.html#frame.clear "frame.clear") method of each
    [frame object](https://docs.python.org/3.12/reference/datamodel.html#frame-objects).

    Added in version 3.4.

traceback.walk_stack(*f*)
:   Walk a stack following [`f.f_back`](https://docs.python.org/3.12/reference/datamodel.html#frame.f_back "frame.f_back") from the given frame,
    yielding the frame
    and line number for each frame. If *f* is `None`, the current stack is
    used. This helper is used with [`StackSummary.extract()`](traceback.md#traceback.StackSummary.extract "traceback.StackSummary.extract").

    Added in version 3.5.

traceback.walk_tb(*tb*)
:   Walk a traceback following [`tb_next`](https://docs.python.org/3.12/reference/datamodel.html#traceback.tb_next "traceback.tb_next") yielding the frame and
    line number
    for each frame. This helper is used with [`StackSummary.extract()`](traceback.md#traceback.StackSummary.extract "traceback.StackSummary.extract").

    Added in version 3.5.

## `TracebackException` Objects

Added in version 3.5.

`TracebackException` objects are created from actual exceptions to
capture data for later printing. They offer a more lightweight method of
storing this information by avoiding holding references to
[traceback](https://docs.python.org/3.12/reference/datamodel.html#traceback-objects) and [frame](https://docs.python.org/3.12/reference/datamodel.html#frame-objects) objects.
In addition, they expose more options to configure the output compared to
the module-level functions described above.

*class* traceback.TracebackException(*exc_type*, *exc_value*, *exc_traceback*, *\**, *limit=None*, *lookup_lines=True*, *capture_locals=False*, *compact=False*, *max_group_width=15*, *max_group_depth=10*)
:   Capture an exception for later rendering. The meaning of *limit*,
    *lookup_lines* and *capture_locals* are as for the [`StackSummary`](traceback.md#traceback.StackSummary "traceback.StackSummary")
    class.

    If *compact* is true, only data that is required by
    `TracebackException`’s [`format()`](functions.md#format "format") method
    is saved in the class attributes. In particular, the
    [`__context__`](traceback.md#traceback.TracebackException.__context__ "traceback.TracebackException.__context__") field is calculated only if [`__cause__`](traceback.md#traceback.TracebackException.__cause__ "traceback.TracebackException.__cause__") is
    `None` and [`__suppress_context__`](traceback.md#traceback.TracebackException.__suppress_context__ "traceback.TracebackException.__suppress_context__") is false.

    Note that when locals are captured, they are also shown in the traceback.

    *max_group_width* and *max_group_depth* control the formatting of exception
    groups (see [`BaseExceptionGroup`](exceptions.md#BaseExceptionGroup "BaseExceptionGroup")). The depth refers to the nesting
    level of the group, and the width refers to the size of a single exception
    group’s exceptions array. The formatted output is truncated when either
    limit is exceeded.

    Changed in version 3.10: Added the *compact* parameter.

    Changed in version 3.11: Added the *max_group_width* and *max_group_depth* parameters.

    __cause__
    :   A `TracebackException` of the original
        [`__cause__`](exceptions.md#BaseException.__cause__ "BaseException.__cause__").

    __context__
    :   A `TracebackException` of the original
        [`__context__`](exceptions.md#BaseException.__context__ "BaseException.__context__").

    exceptions
    :   If `self` represents an [`ExceptionGroup`](exceptions.md#ExceptionGroup "ExceptionGroup"), this field holds a list of
        `TracebackException` instances representing the nested exceptions.
        Otherwise it is `None`.

        Added in version 3.11.

    __suppress_context__
    :   The [`__suppress_context__`](exceptions.md#BaseException.__suppress_context__ "BaseException.__suppress_context__") value from the original
        exception.

    __notes__
    :   The [`__notes__`](exceptions.md#BaseException.__notes__ "BaseException.__notes__") value from the original exception,
        or `None`
        if the exception does not have any notes. If it is not `None`
        is it formatted in the traceback after the exception string.

        Added in version 3.11.

    stack
    :   A [`StackSummary`](traceback.md#traceback.StackSummary "traceback.StackSummary") representing the traceback.

    exc_type
    :   The class of the original traceback.

    filename
    :   For syntax errors - the file name where the error occurred.

    lineno
    :   For syntax errors - the line number where the error occurred.

    end_lineno
    :   For syntax errors - the end line number where the error occurred.
        Can be `None` if not present.

        Added in version 3.10.

    text
    :   For syntax errors - the text where the error occurred.

    offset
    :   For syntax errors - the offset into the text where the error occurred.

    end_offset
    :   For syntax errors - the end offset into the text where the error occurred.
        Can be `None` if not present.

        Added in version 3.10.

    msg
    :   For syntax errors - the compiler error message.

    *classmethod* from_exception(*exc*, *\**, *limit=None*, *lookup_lines=True*, *capture_locals=False*)
    :   Capture an exception for later rendering. *limit*, *lookup_lines* and
        *capture_locals* are as for the [`StackSummary`](traceback.md#traceback.StackSummary "traceback.StackSummary") class.

        Note that when locals are captured, they are also shown in the traceback.

    print(*\**, *file=None*, *chain=True*)
    :   Print to *file* (default `sys.stderr`) the exception information returned by
        [`format()`](functions.md#format "format").

        Added in version 3.11.

    format(*\**, *chain=True*)
    :   Format the exception.

        If *chain* is not `True`, [`__cause__`](traceback.md#traceback.TracebackException.__cause__ "traceback.TracebackException.__cause__") and [`__context__`](traceback.md#traceback.TracebackException.__context__ "traceback.TracebackException.__context__")
        will not be formatted.

        The return value is a generator of strings, each ending in a newline and
        some containing internal newlines. [`print_exception()`](traceback.md#traceback.print_exception "traceback.print_exception")
        is a wrapper around this method which just prints the lines to a file.

    format_exception_only()
    :   Format the exception part of the traceback.

        The return value is a generator of strings, each ending in a newline.

        The generator emits the exception’s message followed by its notes
        (if it has any). The exception message is normally a single string;
        however, for [`SyntaxError`](exceptions.md#SyntaxError "SyntaxError") exceptions, it consists of several
        lines that (when printed) display detailed information about where
        the syntax error occurred.

        Changed in version 3.11: The exception’s [`notes`](exceptions.md#BaseException.__notes__ "BaseException.__notes__") are now
        included in the output.

## `StackSummary` Objects

Added in version 3.5.

`StackSummary` objects represent a call stack ready for formatting.

*class* traceback.StackSummary
:   *classmethod* extract(*frame_gen*, *\**, *limit=None*, *lookup_lines=True*, *capture_locals=False*)
    :   Construct a `StackSummary` object from a frame generator (such as
        is returned by [`walk_stack()`](traceback.md#traceback.walk_stack "traceback.walk_stack") or
        [`walk_tb()`](traceback.md#traceback.walk_tb "traceback.walk_tb")).

        If *limit* is supplied, only this many frames are taken from *frame_gen*.
        If *lookup_lines* is `False`, the returned [`FrameSummary`](traceback.md#traceback.FrameSummary "traceback.FrameSummary")
        objects will not have read their lines in yet, making the cost of
        creating the `StackSummary` cheaper (which may be valuable if it
        may not actually get formatted). If *capture_locals* is `True` the
        local variables in each `FrameSummary` are captured as object
        representations.

        Changed in version 3.12: Exceptions raised from [`repr()`](functions.md#repr "repr") on a local variable (when
        *capture_locals* is `True`) are no longer propagated to the caller.

    *classmethod* from_list(*a_list*)
    :   Construct a `StackSummary` object from a supplied list of
        [`FrameSummary`](traceback.md#traceback.FrameSummary "traceback.FrameSummary") objects or old-style list of tuples. Each tuple
        should be a 4-tuple with *filename*, *lineno*, *name*, *line* as the
        elements.

    format()
    :   Returns a list of strings ready for printing. Each string in the
        resulting list corresponds to a single [frame](https://docs.python.org/3.12/reference/datamodel.html#frame-objects) from
        the stack.
        Each string ends in a newline; the strings may contain internal
        newlines as well, for those items with source text lines.

        For long sequences of the same frame and line, the first few
        repetitions are shown, followed by a summary line stating the exact
        number of further repetitions.

        Changed in version 3.6: Long sequences of repeated frames are now abbreviated.

    format_frame_summary(*frame_summary*)
    :   Returns a string for printing one of the [frames](https://docs.python.org/3.12/reference/datamodel.html#frame-objects)
        involved in the stack.
        This method is called for each [`FrameSummary`](traceback.md#traceback.FrameSummary "traceback.FrameSummary") object to be
        printed by [`StackSummary.format()`](traceback.md#traceback.StackSummary.format "traceback.StackSummary.format"). If it returns `None`, the
        frame is omitted from the output.

        Added in version 3.11.

## `FrameSummary` Objects

Added in version 3.5.

A `FrameSummary` object represents a single [frame](https://docs.python.org/3.12/reference/datamodel.html#frame-objects)
in a [traceback](https://docs.python.org/3.12/reference/datamodel.html#traceback-objects).

*class* traceback.FrameSummary(*filename*, *lineno*, *name*, *\**, *lookup_line=True*, *locals=None*, *line=None*, *end_lineno=None*, *colno=None*, *end_colno=None*)
:   Represents a single [frame](https://docs.python.org/3.12/reference/datamodel.html#frame-objects) in the
    [traceback](https://docs.python.org/3.12/reference/datamodel.html#traceback-objects) or stack that is being formatted
    or printed. It may optionally have a stringified version of the frame’s
    locals included in it. If *lookup_line* is `False`, the source code is not
    looked up until the `FrameSummary` has the [`line`](traceback.md#traceback.FrameSummary.line "traceback.FrameSummary.line")
    attribute accessed (which also happens when casting it to a [`tuple`](stdtypes.md#tuple "tuple")).
    [`line`](traceback.md#traceback.FrameSummary.line "traceback.FrameSummary.line") may be directly provided, and will prevent line
    lookups happening at all. *locals* is an optional local variable
    dictionary, and if supplied the variable representations are stored in the
    summary for later display.

    `FrameSummary` instances have the following attributes:

    filename
    :   The filename of the source code for this frame. Equivalent to accessing
        [`f.f_code.co_filename`](https://docs.python.org/3.12/reference/datamodel.html#codeobject.co_filename "codeobject.co_filename") on a
        [frame object](https://docs.python.org/3.12/reference/datamodel.html#frame-objects) *f*.

    lineno
    :   The line number of the source code for this frame.

    name
    :   Equivalent to accessing [`f.f_code.co_name`](https://docs.python.org/3.12/reference/datamodel.html#codeobject.co_name "codeobject.co_name") on
        a [frame object](https://docs.python.org/3.12/reference/datamodel.html#frame-objects) *f*.

    line
    :   A string representing the source code for this frame, with leading and
        trailing whitespace stripped.
        If the source is not available, it is `None`.

    end_lineno
    :   The last line number of the source code for this frame.
        By default, it is set to `None` and indexation starts from 1.

    colno
    :   The column number of the source code for this frame.
        By default, it is `None` and indexation starts from 0.

    end_colno
    :   The last column number of the source code for this frame.
        By default, it is `None` and indexation starts from 0.

## Examples of Using the Module-Level Functions

This simple example implements a basic read-eval-print loop, similar to (but
less useful than) the standard Python interactive interpreter loop. For a more
complete implementation of the interpreter loop, refer to the [`code`](code.md#module-code "code: Facilities to implement read-eval-print loops.")
module.

```python3
import sys, traceback

def run_user_code(envdir):
    source = input(">>> ")
    try:
        exec(source, envdir)
    except Exception:
        print("Exception in user code:")
        print("-"*60)
        traceback.print_exc(file=sys.stdout)
        print("-"*60)

envdir = {}
while True:
    run_user_code(envdir)
```

The following example demonstrates the different ways to print and format the
exception and traceback:

```python
import sys, traceback

def lumberjack():
    bright_side_of_life()

def bright_side_of_life():
    return tuple()[0]

try:
    lumberjack()
except IndexError as exc:
    print("*** print_tb:")
    traceback.print_tb(exc.__traceback__, limit=1, file=sys.stdout)
    print("*** print_exception:")
    traceback.print_exception(exc, limit=2, file=sys.stdout)
    print("*** print_exc:")
    traceback.print_exc(limit=2, file=sys.stdout)
    print("*** format_exc, first and last line:")
    formatted_lines = traceback.format_exc().splitlines()
    print(formatted_lines[0])
    print(formatted_lines[-1])
    print("*** format_exception:")
    print(repr(traceback.format_exception(exc)))
    print("*** extract_tb:")
    print(repr(traceback.extract_tb(exc.__traceback__)))
    print("*** format_tb:")
    print(repr(traceback.format_tb(exc.__traceback__)))
    print("*** tb_lineno:", exc.__traceback__.tb_lineno)
```

The output for the example would look similar to this:

```
*** print_tb:
  File "<doctest...>", line 10, in <module>
    lumberjack()
*** print_exception:
Traceback (most recent call last):
  File "<doctest...>", line 10, in <module>
    lumberjack()
  File "<doctest...>", line 4, in lumberjack
    bright_side_of_life()
IndexError: tuple index out of range
*** print_exc:
Traceback (most recent call last):
  File "<doctest...>", line 10, in <module>
    lumberjack()
  File "<doctest...>", line 4, in lumberjack
    bright_side_of_life()
IndexError: tuple index out of range
*** format_exc, first and last line:
Traceback (most recent call last):
IndexError: tuple index out of range
*** format_exception:
['Traceback (most recent call last):\n',
 '  File "<doctest default[0]>", line 10, in <module>\n    lumberjack()\n',
 '  File "<doctest default[0]>", line 4, in lumberjack\n    bright_side_of_life()\n',
 '  File "<doctest default[0]>", line 7, in bright_side_of_life\n    return tuple()[0]\n           ~~~~~~~^^^\n',
 'IndexError: tuple index out of range\n']
*** extract_tb:
[<FrameSummary file <doctest...>, line 10 in <module>>,
 <FrameSummary file <doctest...>, line 4 in lumberjack>,
 <FrameSummary file <doctest...>, line 7 in bright_side_of_life>]
*** format_tb:
['  File "<doctest default[0]>", line 10, in <module>\n    lumberjack()\n',
 '  File "<doctest default[0]>", line 4, in lumberjack\n    bright_side_of_life()\n',
 '  File "<doctest default[0]>", line 7, in bright_side_of_life\n    return tuple()[0]\n           ~~~~~~~^^^\n']
*** tb_lineno: 10
```

The following example shows the different ways to print and format the stack:

```python3
>>> import traceback
>>> def another_function():
...     lumberstack()
...
>>> def lumberstack():
...     traceback.print_stack()
...     print(repr(traceback.extract_stack()))
...     print(repr(traceback.format_stack()))
...
>>> another_function()
  File "<doctest>", line 10, in <module>
    another_function()
  File "<doctest>", line 3, in another_function
    lumberstack()
  File "<doctest>", line 6, in lumberstack
    traceback.print_stack()
[('<doctest>', 10, '<module>', 'another_function()'),
 ('<doctest>', 3, 'another_function', 'lumberstack()'),
 ('<doctest>', 7, 'lumberstack', 'print(repr(traceback.extract_stack()))')]
['  File "<doctest>", line 10, in <module>\n    another_function()\n',
 '  File "<doctest>", line 3, in another_function\n    lumberstack()\n',
 '  File "<doctest>", line 8, in lumberstack\n    print(repr(traceback.format_stack()))\n']
```

This last example demonstrates the final few formatting functions:

```pycon
>>> import traceback
>>> traceback.format_list([('spam.py', 3, '<module>', 'spam.eggs()'),
...                        ('eggs.py', 42, 'eggs', 'return "bacon"')])
['  File "spam.py", line 3, in <module>\n    spam.eggs()\n',
 '  File "eggs.py", line 42, in eggs\n    return "bacon"\n']
>>> an_error = IndexError('tuple index out of range')
>>> traceback.format_exception_only(an_error)
['IndexError: tuple index out of range\n']
```

## Examples of Using `TracebackException`

With the helper class, we have more options:

```python3
>>> import sys
>>> from traceback import TracebackException
>>>
>>> def lumberjack():
...     bright_side_of_life()
...
>>> def bright_side_of_life():
...     t = "bright", "side", "of", "life"
...     return t[5]
...
>>> try:
...     lumberjack()
... except IndexError as e:
...     exc = e
...
>>> try:
...     try:
...         lumberjack()
...     except:
...         1/0
... except Exception as e:
...     chained_exc = e
...
>>> # limit works as with the module-level functions
>>> TracebackException.from_exception(exc, limit=-2).print()
Traceback (most recent call last):
  File "<python-input-1>", line 6, in lumberjack
    bright_side_of_life()
    ~~~~~~~~~~~~~~~~~~~^^
  File "<python-input-1>", line 10, in bright_side_of_life
    return t[5]
           ~^^^
IndexError: tuple index out of range

>>> # capture_locals adds local variables in frames
>>> TracebackException.from_exception(exc, limit=-2, capture_locals=True).print()
Traceback (most recent call last):
  File "<python-input-1>", line 6, in lumberjack
    bright_side_of_life()
    ~~~~~~~~~~~~~~~~~~~^^
  File "<python-input-1>", line 10, in bright_side_of_life
    return t[5]
           ~^^^
    t = ("bright", "side", "of", "life")
IndexError: tuple index out of range

>>> # The *chain* kwarg to print() controls whether chained
>>> # exceptions are displayed
>>> TracebackException.from_exception(chained_exc).print()
Traceback (most recent call last):
  File "<python-input-19>", line 4, in <module>
    lumberjack()
    ~~~~~~~~~~^^
  File "<python-input-8>", line 7, in lumberjack
    bright_side_of_life()
    ~~~~~~~~~~~~~~~~~~~^^
  File "<python-input-8>", line 11, in bright_side_of_life
    return t[5]
           ~^^^
IndexError: tuple index out of range

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<python-input-19>", line 6, in <module>
    1/0
    ~^~
ZeroDivisionError: division by zero

>>> TracebackException.from_exception(chained_exc).print(chain=False)
Traceback (most recent call last):
  File "<python-input-19>", line 6, in <module>
    1/0
    ~^~
ZeroDivisionError: division by zero
```
