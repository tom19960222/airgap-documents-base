---
collection: python
version: "3.12.14"
title: "trace — Trace or track Python statement execution"
source_url: https://docs.python.org/3.12/library/trace.html
fetched_at: 2026-09-17T15:34:48+00:00
---
# `trace` — Trace or track Python statement execution

**Source code:** [Lib/trace.py](https://github.com/python/cpython/tree/3.12/Lib/trace.py)

---

The [`trace`](trace.md#module-trace "trace: Trace or track Python statement execution.") module allows you to trace program execution, generate
annotated statement coverage listings, print caller/callee relationships and
list functions executed during a program run. It can be used in another program
or from the command line.

> **See also:**
>
> [Coverage.py](https://coverage.readthedocs.io/)
> :   A popular third-party coverage tool that provides HTML
>     output along with advanced features such as branch coverage.

## Command-Line Usage

The [`trace`](trace.md#module-trace "trace: Trace or track Python statement execution.") module can be invoked from the command line. It can be as
simple as

```python3
python -m trace --count -C . somefile.py ...
```

The above will execute `somefile.py` and generate annotated listings of
all Python modules imported during the execution into the current directory.

`--help`
:   Display usage and exit.

`--version`
:   Display the version of the module and exit.

Added in version 3.8: Added `--module` option that allows to run an executable module.

### Main options

At least one of the following options must be specified when invoking
[`trace`](trace.md#module-trace "trace: Trace or track Python statement execution."). The [`--listfuncs`](trace.md#cmdoption-trace-l) option is mutually exclusive with
the [`--trace`](trace.md#cmdoption-trace-t) and [`--count`](trace.md#cmdoption-trace-c) options. When
[`--listfuncs`](trace.md#cmdoption-trace-l) is provided, neither [`--count`](trace.md#cmdoption-trace-c) nor
[`--trace`](trace.md#cmdoption-trace-t) are accepted, and vice versa.

`-c, --count`
:   Produce a set of annotated listing files upon program completion that shows
    how many times each statement was executed. See also
    [`--coverdir`](trace.md#cmdoption-trace-C), [`--file`](trace.md#cmdoption-trace-f) and
    [`--no-report`](trace.md#cmdoption-trace-R) below.

`-t, --trace`
:   Display lines as they are executed.

`-l, --listfuncs`
:   Display the functions executed by running the program.

`-r, --report`
:   Produce an annotated list from an earlier program run that used the
    [`--count`](trace.md#cmdoption-trace-c) and [`--file`](trace.md#cmdoption-trace-f) option. This does not
    execute any code.

`-T, --trackcalls`
:   Display the calling relationships exposed by running the program.

### Modifiers

`-f, --file=<file>`
:   Name of a file to accumulate counts over several tracing runs. Should be
    used with the [`--count`](trace.md#cmdoption-trace-c) option.

`-C, --coverdir=<dir>`
:   Directory where the report files go. The coverage report for
    `package.module` is written to file `dir/package/module.cover`.

`-m, --missing`
:   When generating annotated listings, mark lines which were not executed with
    `>>>>>>`.

`-s, --summary`
:   When using [`--count`](trace.md#cmdoption-trace-c) or [`--report`](trace.md#cmdoption-trace-r), write a brief
    summary to stdout for each file processed.

`-R, --no-report`
:   Do not generate annotated listings. This is useful if you intend to make
    several runs with [`--count`](trace.md#cmdoption-trace-c), and then produce a single set of
    annotated listings at the end.

`-g, --timing`
:   Prefix each line with the time since the program started. Only used while
    tracing.

### Filters

These options may be repeated multiple times.

`--ignore-module=<mod>`
:   Ignore each of the given module names and its submodules (if it is a
    package). The argument can be a list of names separated by a comma.

`--ignore-dir=<dir>`
:   Ignore all modules and packages in the named directory and subdirectories.
    The argument can be a list of directories separated by [`os.pathsep`](os.md#os.pathsep "os.pathsep").

## Programmatic Interface

`class trace.Trace(count=1, trace=1, countfuncs=0, countcallers=0, ignoremods=(), ignoredirs=(), infile=None, outfile=None, timing=False)`
:   Create an object to trace execution of a single statement or expression. All
    parameters are optional. *count* enables counting of line numbers. *trace*
    enables line execution tracing. *countfuncs* enables listing of the
    functions called during the run. *countcallers* enables call relationship
    tracking. *ignoremods* is a list of modules or packages to ignore.
    *ignoredirs* is a list of directories whose modules or packages should be
    ignored. *infile* is the name of the file from which to read stored count
    information. *outfile* is the name of the file in which to write updated
    count information. *timing* enables a timestamp relative to when tracing was
    started to be displayed.

    `run(cmd)`
    :   Execute the command and gather statistics from the execution with
        the current tracing parameters. *cmd* must be a string or code object,
        suitable for passing into [`exec()`](functions.md#exec "exec").

    `runctx(cmd, globals=None, locals=None)`
    :   Execute the command and gather statistics from the execution with the
        current tracing parameters, in the defined global and local
        environments. If not defined, *globals* and *locals* default to empty
        dictionaries.

    `runfunc(func, /, *args, **kwds)`
    :   Call *func* with the given arguments under control of the [`Trace`](trace.md#trace.Trace "trace.Trace")
        object with the current tracing parameters.

    `results()`
    :   Return a [`CoverageResults`](trace.md#trace.CoverageResults "trace.CoverageResults") object that contains the cumulative
        results of all previous calls to `run`, `runctx` and `runfunc`
        for the given [`Trace`](trace.md#trace.Trace "trace.Trace") instance. Does not reset the accumulated
        trace results.

`class trace.CoverageResults`
:   A container for coverage results, created by [`Trace.results()`](trace.md#trace.Trace.results "trace.Trace.results"). Should
    not be created directly by the user.

    `update(other)`
    :   Merge in data from another [`CoverageResults`](trace.md#trace.CoverageResults "trace.CoverageResults") object.

    `write_results(show_missing=True, summary=False, coverdir=None)`
    :   Write coverage results. Set *show_missing* to show lines that had no
        hits. Set *summary* to include in the output the coverage summary per
        module. *coverdir* specifies the directory into which the coverage
        result files will be output. If `None`, the results for each source
        file are placed in its directory.

A simple example demonstrating the use of the programmatic interface:

```python3
import sys
import trace

# create a Trace object, telling it what to ignore, and whether to
# do tracing or line-counting or both.
tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=0,
    count=1)

# run the new command using the given tracer
tracer.run('main()')

# make a report, placing output in the current directory
r = tracer.results()
r.write_results(show_missing=True, coverdir=".")
```
