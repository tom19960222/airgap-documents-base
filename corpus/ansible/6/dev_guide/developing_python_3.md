---
collection: ansible
version: "6"
title: "Ansible and Python 3"
source_url: https://docs.ansible.com/projects/ansible/6/dev_guide/developing_python_3.html
fetched_at: 2026-07-27T16:39:53+00:00
---
# Ansible and Python 3

The `ansible-core` code runs Python 3 (for specific versions check [Control Node Requirements](../installation_guide/intro_installation.md#control-node-requirements)
Contributors to `ansible-core` and to Ansible Collections should be aware of the tips in this document so that they can write code
that will run on the same versions of Python as the rest of Ansible.

- [Minimum version of Python 3.x and Python 2.x](developing_python_3.md#minimum-version-of-python-3-x-and-python-2-x)
- [Developing Ansible code that supports Python 2 and Python 3](developing_python_3.md#developing-ansible-code-that-supports-python-2-and-python-3)

  - [Understanding strings in Python 2 and Python 3](developing_python_3.md#understanding-strings-in-python-2-and-python-3)

    - [Controller string strategy: the Unicode Sandwich](developing_python_3.md#controller-string-strategy-the-unicode-sandwich)
  - [Unicode Sandwich common borders: places to convert bytes to text in controller code](developing_python_3.md#unicode-sandwich-common-borders-places-to-convert-bytes-to-text-in-controller-code)

    - [Reading and writing to files](developing_python_3.md#reading-and-writing-to-files)
    - [Filesystem interaction](developing_python_3.md#filesystem-interaction)
    - [Interacting with other programs](developing_python_3.md#interacting-with-other-programs)
    - [Module string strategy: Native String](developing_python_3.md#module-string-strategy-native-string)
    - [Module_utils string strategy: hybrid](developing_python_3.md#module-utils-string-strategy-hybrid)
  - [Tips, tricks, and idioms for Python 2/Python 3 compatibility](developing_python_3.md#tips-tricks-and-idioms-for-python-2-python-3-compatibility)

    - [Use forward-compatibility boilerplate](developing_python_3.md#use-forward-compatibility-boilerplate)
    - [Prefix byte strings with `b_`](developing_python_3.md#prefix-byte-strings-with-b)
    - [Import Ansible’s bundled Python `six` library](developing_python_3.md#import-ansible-s-bundled-python-six-library)
    - [Handle exceptions with `as`](developing_python_3.md#handle-exceptions-with-as)
    - [Update octal numbers](developing_python_3.md#update-octal-numbers)
  - [String formatting for controller code](developing_python_3.md#string-formatting-for-controller-code)

    - [Use `str.format()` for Python 2.6 compatibility](developing_python_3.md#use-str-format-for-python-2-6-compatibility)
    - [Use percent format with byte strings](developing_python_3.md#use-percent-format-with-byte-strings)

We do have some considerations depending on the types of Ansible code:

1. controller-side code - code that runs on the machine where you invoke **/usr/bin/ansible**, only needs to support the controller’s Python versions.
2. modules - the code which Ansible transmits to and invokes on the managed machine. Modules need to support the ‘managed node’ Python versions, with some exceptions.
3. shared `module_utils` code - the common code that is used by modules to perform tasks and sometimes used by controller-side code as well. Shared `module_utils` code needs to support the same range of Python as the modules.

However, the three types of code do not use the same string strategy. If you’re developing a module or some `module_utils` code, be sure to read the section on string strategy carefully.

## [Minimum version of Python 3.x and Python 2.x](developing_python_3.md#id1)

See [Control Node Requirements](../installation_guide/intro_installation.md#control-node-requirements) and [Managed Node Requirements](:ref:managed-node-requirements.md) for the
specific versions supported.

Your custom modules can support any version of Python (or other languages) you want, but the above are the requirements for the code contributed to the Ansible project.

## [Developing Ansible code that supports Python 2 and Python 3](developing_python_3.md#id2)

The best place to start learning about writing code that supports both Python 2 and Python 3
is [Lennart Regebro’s book: Porting to Python 3](http://python3porting.com/).
The book describes several strategies for porting to Python 3. The one we’re
using is [to support Python 2 and Python 3 from a single code base](http://python3porting.com/strategies.html#python-2-and-python-3-without-conversion)

### [Understanding strings in Python 2 and Python 3](developing_python_3.md#id3)

Python 2 and Python 3 handle strings differently, so when you write code that supports Python 3
you must decide what string model to use. Strings can be an array of bytes (like in C) or
they can be an array of text. Text is what we think of as letters, digits,
numbers, other printable symbols, and a small number of unprintable “symbols”
(control codes).

In Python 2, the two types for these ([`str`](https://docs.python.org/2/library/functions.html#str "(in Python v2.7)") for bytes and
[`unicode`](https://docs.python.org/2/library/functions.html#unicode "(in Python v2.7)") for text) are often used interchangeably. When dealing only
with ASCII characters, the strings can be combined, compared, and converted
from one type to another automatically. When non-ASCII characters are
introduced, Python 2 starts throwing exceptions due to not knowing what encoding
the non-ASCII characters should be in.

Python 3 changes this behavior by making the separation between bytes ([`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.11)"))
and text ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.11)")) more strict. Python 3 will throw an exception when
trying to combine and compare the two types. The programmer has to explicitly
convert from one type to the other to mix values from each.

In Python 3 it’s immediately apparent to the programmer when code is
mixing the byte and text types inappropriately, whereas in Python 2, code that mixes those types
may work until a user causes an exception by entering non-ASCII input.
Python 3 forces programmers to proactively define a strategy for
working with strings in their program so that they don’t mix text and byte strings unintentionally.

Ansible uses different strategies for working with strings in controller-side code, in
:ref: modules <module_string_strategy>, and in [module_utils](developing_python_3.md#module-utils-string-strategy) code.

#### [Controller string strategy: the Unicode Sandwich](developing_python_3.md#id4)

Until recently `ansible-core` supported Python 2.x and followed this strategy, known as the Unicode Sandwich (named
after Python 2’s [`unicode`](https://docs.python.org/2/library/functions.html#unicode "(in Python v2.7)") text type). For Unicode Sandwich we know that
at the border of our code and the outside world (for example, file and network IO,
environment variables, and some library calls) we are going to receive bytes.
We need to transform these bytes into text and use that throughout the
internal portions of our code. When we have to send those strings back out to
the outside world we first convert the text back into bytes.
To visualize this, imagine a ‘sandwich’ consisting of a top and bottom layer
of bytes, a layer of conversion between, and all text type in the center.

For compatibility reasons you will see a bunch of custom functions we developed (`to_text`/`to_bytes`/`to_native`)
and while Python 2 is not a concern anymore we will continue to use them as they apply for other cases that make
dealing with unicode problematic.

While we will not be using it most of it anymore, the documentation below is still useful for those developing modules
that still need to support both Python 2 and 3 simultaneouslly.

### [Unicode Sandwich common borders: places to convert bytes to text in controller code](developing_python_3.md#id5)

This is a partial list of places where we have to convert to and from bytes
when using the Unicode Sandwich string strategy. It’s not exhaustive but
it gives you an idea of where to watch for problems.

#### [Reading and writing to files](developing_python_3.md#id6)

In Python 2, reading from files yields bytes. In Python 3, it can yield text.
To make code that’s portable to both we don’t make use of Python 3’s ability
to yield text but instead do the conversion explicitly ourselves. For example:

```python
from ansible.module_utils.common.text.converters import to_text

with open('filename-with-utf8-data.txt', 'rb') as my_file:
    b_data = my_file.read()
    try:
        data = to_text(b_data, errors='surrogate_or_strict')
    except UnicodeError:
        # Handle the exception gracefully -- usually by displaying a good
        # user-centric error message that can be traced back to this piece
        # of code.
        pass
```

> **Note:**
>
> Much of Ansible assumes that all encoded text is UTF-8. At some
> point, if there is demand for other encodings we may change that, but for
> now it is safe to assume that bytes are UTF-8.

Writing to files is the opposite process:

```python
from ansible.module_utils.common.text.converters import to_bytes

with open('filename.txt', 'wb') as my_file:
    my_file.write(to_bytes(some_text_string))
```

Note that we don’t have to catch [`UnicodeError`](https://docs.python.org/3/library/exceptions.html#UnicodeError "(in Python v3.11)") here because we’re
transforming to UTF-8 and all text strings in Python can be transformed back
to UTF-8.

#### [Filesystem interaction](developing_python_3.md#id7)

Dealing with filenames often involves dropping back to bytes because on UNIX-like
systems filenames are bytes. On Python 2, if we pass a text string to these
functions, the text string will be converted to a byte string inside of the
function and a traceback will occur if non-ASCII characters are present. In
Python 3, a traceback will only occur if the text string can’t be decoded in
the current locale, but it’s still good to be explicit and have code which
works on both versions:

```python
import os.path

from ansible.module_utils.common.text.converters import to_bytes

filename = u'/var/tmp/くらとみ.txt'
f = open(to_bytes(filename), 'wb')
mtime = os.path.getmtime(to_bytes(filename))
b_filename = os.path.expandvars(to_bytes(filename))
if os.path.exists(to_bytes(filename)):
    pass
```

When you are only manipulating a filename as a string without talking to the
filesystem (or a C library which talks to the filesystem) you can often get
away without converting to bytes:

```python
import os.path

os.path.join(u'/var/tmp/café', u'くらとみ')
os.path.split(u'/var/tmp/café/くらとみ')
```

On the other hand, if the code needs to manipulate the filename and also talk
to the filesystem, it can be more convenient to transform to bytes right away
and manipulate in bytes.

> **Warning:**
>
> Make sure all variables passed to a function are the same type.
> If you’re working with something like [`os.path.join()`](https://docs.python.org/3/library/os.path.html#os.path.join "(in Python v3.11)") which takes
> multiple strings and uses them in combination, you need to make sure that
> all the types are the same (either all bytes or all text). Mixing
> bytes and text will cause tracebacks.

#### [Interacting with other programs](developing_python_3.md#id8)

Interacting with other programs goes through the operating system and
C libraries and operates on things that the UNIX kernel defines. These
interfaces are all byte-oriented so the Python interface is byte oriented as
well. On both Python 2 and Python 3, byte strings should be given to Python’s
subprocess library and byte strings should be expected back from it.

One of the main places in Ansible’s controller code that we interact with
other programs is the connection plugins’ `exec_command` methods. These
methods transform any text strings they receive in the command (and arguments
to the command) to execute into bytes and return stdout and stderr as byte strings
Higher level functions (like action plugins’ `_low_level_execute_command`)
transform the output into text strings.

#### [Module string strategy: Native String](developing_python_3.md#id9)

In modules we use a strategy known as Native Strings. This makes things
easier on the community members who maintain so many of Ansible’s
modules, by not breaking backwards compatibility by
mandating that all strings inside of modules are text and converting between
text and bytes at the borders.

Native strings refer to the type that Python uses when you specify a bare
string literal:

```python
"This is a native string"
```

In Python 2, these are byte strings. In Python 3 these are text strings. Modules should be
coded to expect bytes on Python 2 and text on Python 3.

#### [Module_utils string strategy: hybrid](developing_python_3.md#id10)

In `module_utils` code we use a hybrid string strategy. Although Ansible’s
`module_utils` code is largely like module code, some pieces of it are
used by the controller as well. So it needs to be compatible with modules
and with the controller’s assumptions, particularly the string strategy.
The module_utils code attempts to accept native strings as input
to its functions and emit native strings as their output.

In `module_utils` code:

- Functions **must** accept string parameters as either text strings or byte strings.
- Functions may return either the same type of string as they were given or the native string type for the Python version they are run on.
- Functions that return strings **must** document whether they return strings of the same type as they were given or native strings.

Module-utils functions are therefore often very defensive in nature.
They convert their string parameters into text (using `ansible.module_utils.common.text.converters.to_text`)
at the beginning of the function, do their work, and then convert
the return values into the native string type (using `ansible.module_utils.common.text.converters.to_native`)
or back to the string type that their parameters received.

### [Tips, tricks, and idioms for Python 2/Python 3 compatibility](developing_python_3.md#id11)

#### [Use forward-compatibility boilerplate](developing_python_3.md#id12)

Use the following boilerplate code at the top of all python files
to make certain constructs act the same way on Python 2 and Python 3:

```python
# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
```

`__metaclass__ = type` makes all classes defined in the file into new-style
classes without explicitly inheriting from [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.11)").

The `__future__` imports do the following:

absolute_import:
:   Makes imports look in [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "(in Python v3.11)") for the modules being
    imported, skipping the directory in which the module doing the importing
    lives. If the code wants to use the directory in which the module doing
    the importing, there’s a new dot notation to do so.

division:
:   Makes division of integers always return a float. If you need to
    find the quotient use `x // y` instead of `x / y`.

print_function:
:   Changes [`print`](https://docs.python.org/3/library/functions.html#print "(in Python v3.11)") from a keyword into a function.

> **See also:**
>
> - [PEP 0328: Absolute Imports](https://www.python.org/dev/peps/pep-0328/#guido-s-decision)
> - [PEP 0238: Division](https://www.python.org/dev/peps/pep-0238)
> - [PEP 3105: Print function](https://www.python.org/dev/peps/pep-3105)

#### [Prefix byte strings with `b_`](developing_python_3.md#id13)

Since mixing text and bytes types leads to tracebacks we want to be clear
about what variables hold text and what variables hold bytes. We do this by
prefixing any variable holding bytes with `b_`. For instance:

```python
filename = u'/var/tmp/café.txt'
b_filename = to_bytes(filename)
with open(b_filename) as f:
    data = f.read()
```

We do not prefix the text strings instead because we only operate
on byte strings at the borders, so there are fewer variables that need bytes
than text.

#### [Import Ansible’s bundled Python `six` library](developing_python_3.md#id14)

The third-party Python [six](https://pypi.org/project/six/) library exists
to help projects create code that runs on both Python 2 and Python 3. Ansible
includes a version of the library in module_utils so that other modules can use it
without requiring that it is installed on the remote system. To make use of
it, import it like this:

```python
from ansible.module_utils import six
```

> **Note:**
>
> Ansible can also use a system copy of six
>
> Ansible will use a system copy of six if the system copy is a later
> version than the one Ansible bundles.

#### [Handle exceptions with `as`](developing_python_3.md#id15)

In order for code to function on Python 2.6+ and Python 3, use the
new exception-catching syntax which uses the `as` keyword:

```python
try:
    a = 2/0
except ValueError as e:
    module.fail_json(msg="Tried to divide by zero: %s" % e)
```

Do **not** use the following syntax as it will fail on every version of Python 3:

```
try:
    a = 2/0
except ValueError, e:
    module.fail_json(msg="Tried to divide by zero: %s" % e)
```

#### [Update octal numbers](developing_python_3.md#id16)

In Python 2.x, octal literals could be specified as `0755`. In Python 3,
octals must be specified as `0o755`.

### [String formatting for controller code](developing_python_3.md#id17)

#### [Use `str.format()` for Python 2.6 compatibility](developing_python_3.md#id18)

Starting in Python 2.6, strings gained a method called `format()` to put
strings together. However, one commonly used feature of `format()` wasn’t
added until Python 2.7, so you need to remember not to use it in Ansible code:

```python
# Does not work in Python 2.6!
new_string = "Dear {}, Welcome to {}".format(username, location)

# Use this instead
new_string = "Dear {0}, Welcome to {1}".format(username, location)
```

Both of the format strings above map positional arguments of the `format()`
method into the string. However, the first version doesn’t work in
Python 2.6. Always remember to put numbers into the placeholders so the code
is compatible with Python 2.6.

> **See also:**
>
> Python documentation on format strings:
>
> - [format strings in 2.6](https://docs.python.org/2.6/library/string.html#formatstrings)
> - [format strings in 3.x](https://docs.python.org/3/library/string.html#formatstrings)

#### [Use percent format with byte strings](developing_python_3.md#id19)

In Python 3.x, byte strings do not have a `format()` method. However, it
does have support for the older, percent-formatting.

```python
b_command_line = b'ansible-playbook --become-user %s -K %s' % (user, playbook_file)
```

> **Note:**
>
> Percent formatting added in Python 3.5
>
> Percent formatting of byte strings was added back into Python 3 in 3.5.
> This isn’t a problem for us because Python 3.5 is our minimum version.
> However, if you happen to be testing Ansible code with Python 3.4 or
> earlier, you will find that the byte string formatting here won’t work.
> Upgrade to Python 3.5 to test.

> **See also:**
>
> Python documentation on [percent formatting](https://docs.python.org/3/library/stdtypes.html#string-formatting)
