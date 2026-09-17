---
collection: python
version: "3.10.21"
title: "pipes — Interface to shell pipelines"
source_url: https://docs.python.org/3.10/library/pipes.html
fetched_at: 2026-09-17T15:15:24+00:00
---
# `pipes` — Interface to shell pipelines

**Source code:** [Lib/pipes.py](https://github.com/python/cpython/tree/3.10/Lib/pipes.py)

Deprecated since version 3.11: The [`pipes`](pipes.md#module-pipes "pipes: A Python interface to Unix shell pipelines. (deprecated) (Unix)") module is deprecated
(see [**PEP 594**](https://www.python.org/dev/peps/pep-0594#pipes) for details).
Please use the [`subprocess`](subprocess.md#module-subprocess "subprocess: Subprocess management.") module instead.

---

The [`pipes`](pipes.md#module-pipes "pipes: A Python interface to Unix shell pipelines. (deprecated) (Unix)") module defines a class to abstract the concept of a *pipeline*
— a sequence of converters from one file to another.

Because the module uses **/bin/sh** command lines, a POSIX or compatible
shell for [`os.system()`](os.md#os.system "os.system") and [`os.popen()`](os.md#os.popen "os.popen") is required.

[Availability](intro.md#availability): Unix. Not available on VxWorks.

The [`pipes`](pipes.md#module-pipes "pipes: A Python interface to Unix shell pipelines. (deprecated) (Unix)") module defines the following class:

`class pipes.Template`
:   An abstraction of a pipeline.

Example:

```python3
>>> import pipes
>>> t = pipes.Template()
>>> t.append('tr a-z A-Z', '--')
>>> f = t.open('pipefile', 'w')
>>> f.write('hello world')
>>> f.close()
>>> open('pipefile').read()
'HELLO WORLD'
```

## Template Objects

Template objects following methods:

`Template.reset()`
:   Restore a pipeline template to its initial state.

`Template.clone()`
:   Return a new, equivalent, pipeline template.

`Template.debug(flag)`
:   If *flag* is true, turn debugging on. Otherwise, turn debugging off. When
    debugging is on, commands to be executed are printed, and the shell is given
    `set -x` command to be more verbose.

`Template.append(cmd, kind)`
:   Append a new action at the end. The *cmd* variable must be a valid bourne shell
    command. The *kind* variable consists of two letters.

    The first letter can be either of `'-'` (which means the command reads its
    standard input), `'f'` (which means the commands reads a given file on the
    command line) or `'.'` (which means the commands reads no input, and hence
    must be first.)

    Similarly, the second letter can be either of `'-'` (which means the command
    writes to standard output), `'f'` (which means the command writes a file on
    the command line) or `'.'` (which means the command does not write anything,
    and hence must be last.)

`Template.prepend(cmd, kind)`
:   Add a new action at the beginning. See [`append()`](pipes.md#pipes.Template.append "pipes.Template.append") for explanations of the
    arguments.

`Template.open(file, mode)`
:   Return a file-like object, open to *file*, but read from or written to by the
    pipeline. Note that only one of `'r'`, `'w'` may be given.

`Template.copy(infile, outfile)`
:   Copy *infile* to *outfile* through the pipe.
