---
collection: python
version: "3.12.14"
title: "collections.abc — Abstract Base Classes for Containers"
source_url: https://docs.python.org/3.12/library/collections.abc.html
fetched_at: 2026-09-17T15:32:26+00:00
---
# `collections.abc` — Abstract Base Classes for Containers

Added in version 3.3: Formerly, this module was part of the [`collections`](collections.md#module-collections "collections: Container datatypes") module.

**Source code:** [Lib/_collections_abc.py](https://github.com/python/cpython/tree/3.12/Lib/_collections_abc.py)

---

This module provides [abstract base classes](https://docs.python.org/3.12/glossary.html#term-abstract-base-class) that
can be used to test whether a class provides a particular interface; for
example, whether it is [hashable](https://docs.python.org/3.12/glossary.html#term-hashable) or whether it is a [mapping](https://docs.python.org/3.12/glossary.html#term-mapping).

An [`issubclass()`](functions.md#issubclass "issubclass") or [`isinstance()`](functions.md#isinstance "isinstance") test for an interface works in one
of three ways.

1. A newly written class can inherit directly from one of the
   abstract base classes. The class must supply the required abstract
   methods. The remaining mixin methods come from inheritance and can be
   overridden if desired. Other methods may be added as needed:

   ```python
   class C(Sequence):                      # Direct inheritance
       def __init__(self): ...             # Extra method not required by the ABC
       def __getitem__(self, index):  ...  # Required abstract method
       def __len__(self):  ...             # Required abstract method
       def count(self, value): ...         # Optionally override a mixin method
   ```

   ```pycon
   >>> issubclass(C, Sequence)
   True
   >>> isinstance(C(), Sequence)
   True
   ```
2. Existing classes and built-in classes can be registered as “virtual
   subclasses” of the ABCs. Those classes should define the full API
   including all of the abstract methods and all of the mixin methods.
   This lets users rely on [`issubclass()`](functions.md#issubclass "issubclass") or [`isinstance()`](functions.md#isinstance "isinstance") tests
   to determine whether the full interface is supported. The exception to
   this rule is for methods that are automatically inferred from the rest
   of the API:

   ```python
   class D:                                 # No inheritance
       def __init__(self): ...              # Extra method not required by the ABC
       def __getitem__(self, index):  ...   # Abstract method
       def __len__(self):  ...              # Abstract method
       def count(self, value): ...          # Mixin method
       def index(self, value): ...          # Mixin method

   Sequence.register(D)                     # Register instead of inherit
   ```

   ```pycon
   >>> issubclass(D, Sequence)
   True
   >>> isinstance(D(), Sequence)
   True
   ```

   In this example, class `D` does not need to define
   `__contains__`, `__iter__`, and `__reversed__` because the
   [in-operator](https://docs.python.org/3.12/reference/expressions.html#comparisons), the [iteration](https://docs.python.org/3.12/glossary.html#term-iterable)
   logic, and the [`reversed()`](functions.md#reversed "reversed") function automatically fall back to
   using `__getitem__` and `__len__`.
3. Some simple interfaces are directly recognizable by the presence of
   the required methods (unless those methods have been set to [`None`](constants.md#None "None")):

   ```python
   class E:
       def __iter__(self): ...
       def __next__(self): ...
   ```

   ```pycon
   >>> issubclass(E, Iterable)
   True
   >>> isinstance(E(), Iterable)
   True
   ```

   Complex interfaces do not support this last technique because an
   interface is more than just the presence of method names. Interfaces
   specify semantics and relationships between methods that cannot be
   inferred solely from the presence of specific method names. For
   example, knowing that a class supplies `__getitem__`, `__len__`, and
   `__iter__` is insufficient for distinguishing a [`Sequence`](collections.abc.md#collections.abc.Sequence "collections.abc.Sequence") from
   a [`Mapping`](collections.abc.md#collections.abc.Mapping "collections.abc.Mapping").

Added in version 3.9: These abstract classes now support `[]`. See [Generic Alias Type](stdtypes.md#types-genericalias)
and [**PEP 585**](https://peps.python.org/pep-0585/).

## Collections Abstract Base Classes

The collections module offers the following [ABCs](https://docs.python.org/3.12/glossary.html#term-abstract-base-class):

| ABC | Inherits from | Abstract Methods | Mixin Methods |
| --- | --- | --- | --- |
| [`Container`](collections.abc.md#collections.abc.Container "collections.abc.Container") [[1]](collections.abc.md#id18) |  | `__contains__` |  |
| [`Hashable`](collections.abc.md#collections.abc.Hashable "collections.abc.Hashable") [[1]](collections.abc.md#id18) |  | `__hash__` |  |
| [`Iterable`](collections.abc.md#collections.abc.Iterable "collections.abc.Iterable") [[1]](collections.abc.md#id18) [[2]](collections.abc.md#id19) |  | `__iter__` |  |
| [`Iterator`](collections.abc.md#collections.abc.Iterator "collections.abc.Iterator") [[1]](collections.abc.md#id18) | [`Iterable`](collections.abc.md#collections.abc.Iterable "collections.abc.Iterable") | `__next__` | `__iter__` |
| [`Reversible`](collections.abc.md#collections.abc.Reversible "collections.abc.Reversible") [[1]](collections.abc.md#id18) | [`Iterable`](collections.abc.md#collections.abc.Iterable "collections.abc.Iterable") | `__reversed__` |  |
| [`Generator`](collections.abc.md#collections.abc.Generator "collections.abc.Generator") [[1]](collections.abc.md#id18) | [`Iterator`](collections.abc.md#collections.abc.Iterator "collections.abc.Iterator") | `send`, `throw` | `close`, `__iter__`, `__next__` |
| [`Sized`](collections.abc.md#collections.abc.Sized "collections.abc.Sized") [[1]](collections.abc.md#id18) |  | `__len__` |  |
| [`Callable`](collections.abc.md#collections.abc.Callable "collections.abc.Callable") [[1]](collections.abc.md#id18) |  | `__call__` |  |
| [`Collection`](collections.abc.md#collections.abc.Collection "collections.abc.Collection") [[1]](collections.abc.md#id18) | [`Sized`](collections.abc.md#collections.abc.Sized "collections.abc.Sized"), [`Iterable`](collections.abc.md#collections.abc.Iterable "collections.abc.Iterable"), [`Container`](collections.abc.md#collections.abc.Container "collections.abc.Container") | `__contains__`, `__iter__`, `__len__` |  |
| [`Sequence`](collections.abc.md#collections.abc.Sequence "collections.abc.Sequence") | [`Reversible`](collections.abc.md#collections.abc.Reversible "collections.abc.Reversible"), [`Collection`](collections.abc.md#collections.abc.Collection "collections.abc.Collection") | `__getitem__`, `__len__` | `__contains__`, `__iter__`, `__reversed__`, `index`, and `count` |
| [`MutableSequence`](collections.abc.md#collections.abc.MutableSequence "collections.abc.MutableSequence") | [`Sequence`](collections.abc.md#collections.abc.Sequence "collections.abc.Sequence") | `__getitem__`, `__setitem__`, `__delitem__`, `__len__`, `insert` | Inherited [`Sequence`](collections.abc.md#collections.abc.Sequence "collections.abc.Sequence") methods and `append`, `clear`, `reverse`, `extend`, `pop`, `remove`, and `__iadd__` |
| [`ByteString`](collections.abc.md#collections.abc.ByteString "collections.abc.ByteString") | [`Sequence`](collections.abc.md#collections.abc.Sequence "collections.abc.Sequence") | `__getitem__`, `__len__` | Inherited [`Sequence`](collections.abc.md#collections.abc.Sequence "collections.abc.Sequence") methods |
| [`Set`](collections.abc.md#collections.abc.Set "collections.abc.Set") | [`Collection`](collections.abc.md#collections.abc.Collection "collections.abc.Collection") | `__contains__`, `__iter__`, `__len__` | `__le__`, `__lt__`, `__eq__`, `__ne__`, `__gt__`, `__ge__`, `__and__`, `__or__`, `__sub__`, `__rsub__`, `__xor__`, `__rxor__` and `isdisjoint` |
| [`MutableSet`](collections.abc.md#collections.abc.MutableSet "collections.abc.MutableSet") | [`Set`](collections.abc.md#collections.abc.Set "collections.abc.Set") | `__contains__`, `__iter__`, `__len__`, `add`, `discard` | Inherited [`Set`](collections.abc.md#collections.abc.Set "collections.abc.Set") methods and `clear`, `pop`, `remove`, `__ior__`, `__iand__`, `__ixor__`, and `__isub__` |
| [`Mapping`](collections.abc.md#collections.abc.Mapping "collections.abc.Mapping") | [`Collection`](collections.abc.md#collections.abc.Collection "collections.abc.Collection") | `__getitem__`, `__iter__`, `__len__` | `__contains__`, `keys`, `items`, `values`, `get`, `__eq__`, and `__ne__` |
| [`MutableMapping`](collections.abc.md#collections.abc.MutableMapping "collections.abc.MutableMapping") | [`Mapping`](collections.abc.md#collections.abc.Mapping "collections.abc.Mapping") | `__getitem__`, `__setitem__`, `__delitem__`, `__iter__`, `__len__` | Inherited [`Mapping`](collections.abc.md#collections.abc.Mapping "collections.abc.Mapping") methods and `pop`, `popitem`, `clear`, `update`, and `setdefault` |
| [`MappingView`](collections.abc.md#collections.abc.MappingView "collections.abc.MappingView") | [`Sized`](collections.abc.md#collections.abc.Sized "collections.abc.Sized") |  | `__init__`, `__len__` and `__repr__` |
| [`ItemsView`](collections.abc.md#collections.abc.ItemsView "collections.abc.ItemsView") | [`MappingView`](collections.abc.md#collections.abc.MappingView "collections.abc.MappingView"), [`Set`](collections.abc.md#collections.abc.Set "collections.abc.Set") |  | `__contains__`, `__iter__` |
| [`KeysView`](collections.abc.md#collections.abc.KeysView "collections.abc.KeysView") | [`MappingView`](collections.abc.md#collections.abc.MappingView "collections.abc.MappingView"), [`Set`](collections.abc.md#collections.abc.Set "collections.abc.Set") |  | `__contains__`, `__iter__` |
| [`ValuesView`](collections.abc.md#collections.abc.ValuesView "collections.abc.ValuesView") | [`MappingView`](collections.abc.md#collections.abc.MappingView "collections.abc.MappingView"), [`Collection`](collections.abc.md#collections.abc.Collection "collections.abc.Collection") |  | `__contains__`, `__iter__` |
| [`Awaitable`](collections.abc.md#collections.abc.Awaitable "collections.abc.Awaitable") [[1]](collections.abc.md#id18) |  | `__await__` |  |
| [`Coroutine`](collections.abc.md#collections.abc.Coroutine "collections.abc.Coroutine") [[1]](collections.abc.md#id18) | [`Awaitable`](collections.abc.md#collections.abc.Awaitable "collections.abc.Awaitable") | `send`, `throw` | `close` |
| [`AsyncIterable`](collections.abc.md#collections.abc.AsyncIterable "collections.abc.AsyncIterable") [[1]](collections.abc.md#id18) |  | `__aiter__` |  |
| [`AsyncIterator`](collections.abc.md#collections.abc.AsyncIterator "collections.abc.AsyncIterator") [[1]](collections.abc.md#id18) | [`AsyncIterable`](collections.abc.md#collections.abc.AsyncIterable "collections.abc.AsyncIterable") | `__anext__` | `__aiter__` |
| [`AsyncGenerator`](collections.abc.md#collections.abc.AsyncGenerator "collections.abc.AsyncGenerator") [[1]](collections.abc.md#id18) | [`AsyncIterator`](collections.abc.md#collections.abc.AsyncIterator "collections.abc.AsyncIterator") | `asend`, `athrow` | `aclose`, `__aiter__`, `__anext__` |
| [`Buffer`](collections.abc.md#collections.abc.Buffer "collections.abc.Buffer") [[1]](collections.abc.md#id18) |  | `__buffer__` |  |

Footnotes

[1]
([1](collections.abc.md#id2),[2](collections.abc.md#id3),[3](collections.abc.md#id4),[4](collections.abc.md#id6),[5](collections.abc.md#id7),[6](collections.abc.md#id8),[7](collections.abc.md#id9),[8](collections.abc.md#id10),[9](collections.abc.md#id11),[10](collections.abc.md#id12),[11](collections.abc.md#id13),[12](collections.abc.md#id14),[13](collections.abc.md#id15),[14](collections.abc.md#id16),[15](collections.abc.md#id17))

These ABCs override [`__subclasshook__()`](abc.md#abc.ABCMeta.__subclasshook__ "abc.ABCMeta.__subclasshook__") to support
testing an interface by verifying the required methods are present
and have not been set to [`None`](constants.md#None "None"). This only works for simple
interfaces. More complex interfaces require registration or direct
subclassing.

[[2](collections.abc.md#id5)]

Checking `isinstance(obj, Iterable)` detects classes that are
registered as [`Iterable`](collections.abc.md#collections.abc.Iterable "collections.abc.Iterable") or that have an [`__iter__()`](stdtypes.md#container.__iter__ "container.__iter__")
method, but it does not detect classes that iterate with the
[`__getitem__()`](https://docs.python.org/3.12/reference/datamodel.html#object.__getitem__ "object.__getitem__") method. The only reliable way to determine
whether an object is [iterable](https://docs.python.org/3.12/glossary.html#term-iterable) is to call `iter(obj)`.

## Collections Abstract Base Classes – Detailed Descriptions

`class collections.abc.Container`
:   ABC for classes that provide the [`__contains__()`](https://docs.python.org/3.12/reference/datamodel.html#object.__contains__ "object.__contains__") method.

`class collections.abc.Hashable`
:   ABC for classes that provide the [`__hash__()`](https://docs.python.org/3.12/reference/datamodel.html#object.__hash__ "object.__hash__") method.

`class collections.abc.Sized`
:   ABC for classes that provide the [`__len__()`](https://docs.python.org/3.12/reference/datamodel.html#object.__len__ "object.__len__") method.

`class collections.abc.Callable`
:   ABC for classes that provide the [`__call__()`](https://docs.python.org/3.12/reference/datamodel.html#object.__call__ "object.__call__") method.

    See [Annotating callable objects](typing.md#annotating-callables) for details on how to use
    `Callable` in type annotations.

`class collections.abc.Iterable`
:   ABC for classes that provide the [`__iter__()`](stdtypes.md#container.__iter__ "container.__iter__") method.

    Checking `isinstance(obj, Iterable)` detects classes that are registered
    as [`Iterable`](collections.abc.md#collections.abc.Iterable "collections.abc.Iterable") or that have an [`__iter__()`](stdtypes.md#container.__iter__ "container.__iter__") method,
    but it does
    not detect classes that iterate with the [`__getitem__()`](https://docs.python.org/3.12/reference/datamodel.html#object.__getitem__ "object.__getitem__") method.
    The only reliable way to determine whether an object is [iterable](https://docs.python.org/3.12/glossary.html#term-iterable)
    is to call `iter(obj)`.

`class collections.abc.Collection`
:   ABC for sized iterable container classes.

    Added in version 3.6.

`class collections.abc.Iterator`
:   ABC for classes that provide the [`__iter__()`](stdtypes.md#iterator.__iter__ "iterator.__iter__") and
    [`__next__()`](stdtypes.md#iterator.__next__ "iterator.__next__") methods. See also the definition of
    [iterator](https://docs.python.org/3.12/glossary.html#term-iterator).

`class collections.abc.Reversible`
:   ABC for iterable classes that also provide the [`__reversed__()`](https://docs.python.org/3.12/reference/datamodel.html#object.__reversed__ "object.__reversed__")
    method.

    Added in version 3.6.

`class collections.abc.Generator`
:   ABC for [generator](https://docs.python.org/3.12/glossary.html#term-generator) classes that implement the protocol defined in
    [**PEP 342**](https://peps.python.org/pep-0342/) that extends [iterators](https://docs.python.org/3.12/glossary.html#term-iterator) with the
    [`send()`](https://docs.python.org/3.12/reference/expressions.html#generator.send "generator.send"),
    [`throw()`](https://docs.python.org/3.12/reference/expressions.html#generator.throw "generator.throw") and [`close()`](https://docs.python.org/3.12/reference/expressions.html#generator.close "generator.close") methods.

    See [Annotating generators and coroutines](typing.md#annotating-generators-and-coroutines)
    for details on using `Generator` in type annotations.

    Added in version 3.5.

`class collections.abc.Sequence`

`class collections.abc.MutableSequence`

`class collections.abc.ByteString`
:   ABCs for read-only and mutable [sequences](https://docs.python.org/3.12/glossary.html#term-sequence).

    Implementation note: Some of the mixin methods, such as
    [`__iter__()`](stdtypes.md#container.__iter__ "container.__iter__"), [`__reversed__()`](https://docs.python.org/3.12/reference/datamodel.html#object.__reversed__ "object.__reversed__") and `index()`, make
    repeated calls to the underlying [`__getitem__()`](https://docs.python.org/3.12/reference/datamodel.html#object.__getitem__ "object.__getitem__") method.
    Consequently, if [`__getitem__()`](https://docs.python.org/3.12/reference/datamodel.html#object.__getitem__ "object.__getitem__") is implemented with constant
    access speed, the mixin methods will have linear performance;
    however, if the underlying method is linear (as it would be with a
    linked list), the mixins will have quadratic performance and will
    likely need to be overridden.

    Changed in version 3.5: The index() method added support for *stop* and *start*
    arguments.

    Deprecated since version 3.12, will be removed in version 3.14: The [`ByteString`](collections.abc.md#collections.abc.ByteString "collections.abc.ByteString") ABC has been deprecated.
    For use in typing, prefer a union, like `bytes | bytearray`, or
    [`collections.abc.Buffer`](collections.abc.md#collections.abc.Buffer "collections.abc.Buffer").
    For use as an ABC, prefer [`Sequence`](collections.abc.md#collections.abc.Sequence "collections.abc.Sequence") or [`collections.abc.Buffer`](collections.abc.md#collections.abc.Buffer "collections.abc.Buffer").

`class collections.abc.Set`

`class collections.abc.MutableSet`
:   ABCs for read-only and mutable [sets](stdtypes.md#types-set).

`class collections.abc.Mapping`

`class collections.abc.MutableMapping`
:   ABCs for read-only and mutable [mappings](https://docs.python.org/3.12/glossary.html#term-mapping).

`class collections.abc.MappingView`

`class collections.abc.ItemsView`

`class collections.abc.KeysView`

`class collections.abc.ValuesView`
:   ABCs for mapping, items, keys, and values [views](https://docs.python.org/3.12/glossary.html#term-dictionary-view).

`class collections.abc.Awaitable`
:   ABC for [awaitable](https://docs.python.org/3.12/glossary.html#term-awaitable) objects, which can be used in [`await`](https://docs.python.org/3.12/reference/expressions.html#await)
    expressions. Custom implementations must provide the
    [`__await__()`](https://docs.python.org/3.12/reference/datamodel.html#object.__await__ "object.__await__") method.

    [Coroutine](https://docs.python.org/3.12/glossary.html#term-coroutine) objects and instances of the
    [`Coroutine`](collections.abc.md#collections.abc.Coroutine "collections.abc.Coroutine") ABC are all instances of this ABC.

    > **Note:**
    >
    > In CPython, generator-based coroutines ([generators](https://docs.python.org/3.12/glossary.html#term-generator)
    > decorated with [`@types.coroutine`](types.md#types.coroutine "types.coroutine")) are
    > *awaitables*, even though they do not have an [`__await__()`](https://docs.python.org/3.12/reference/datamodel.html#object.__await__ "object.__await__") method.
    > Using `isinstance(gencoro, Awaitable)` for them will return `False`.
    > Use [`inspect.isawaitable()`](inspect.md#inspect.isawaitable "inspect.isawaitable") to detect them.

    Added in version 3.5.

`class collections.abc.Coroutine`
:   ABC for [coroutine](https://docs.python.org/3.12/glossary.html#term-coroutine) compatible classes. These implement the
    following methods, defined in [Coroutine Objects](https://docs.python.org/3.12/reference/datamodel.html#coroutine-objects):
    [`send()`](https://docs.python.org/3.12/reference/datamodel.html#coroutine.send "coroutine.send"), [`throw()`](https://docs.python.org/3.12/reference/datamodel.html#coroutine.throw "coroutine.throw"), and
    [`close()`](https://docs.python.org/3.12/reference/datamodel.html#coroutine.close "coroutine.close"). Custom implementations must also implement
    [`__await__()`](https://docs.python.org/3.12/reference/datamodel.html#object.__await__ "object.__await__"). All [`Coroutine`](collections.abc.md#collections.abc.Coroutine "collections.abc.Coroutine") instances are also
    instances of [`Awaitable`](collections.abc.md#collections.abc.Awaitable "collections.abc.Awaitable").

    > **Note:**
    >
    > In CPython, generator-based coroutines ([generators](https://docs.python.org/3.12/glossary.html#term-generator)
    > decorated with [`@types.coroutine`](types.md#types.coroutine "types.coroutine")) are
    > *awaitables*, even though they do not have an [`__await__()`](https://docs.python.org/3.12/reference/datamodel.html#object.__await__ "object.__await__") method.
    > Using `isinstance(gencoro, Coroutine)` for them will return `False`.
    > Use [`inspect.isawaitable()`](inspect.md#inspect.isawaitable "inspect.isawaitable") to detect them.

    See [Annotating generators and coroutines](typing.md#annotating-generators-and-coroutines)
    for details on using `Coroutine` in type annotations.
    The variance and order of type parameters correspond to those of
    [`Generator`](collections.abc.md#collections.abc.Generator "collections.abc.Generator").

    Added in version 3.5.

`class collections.abc.AsyncIterable`
:   ABC for classes that provide an `__aiter__` method. See also the
    definition of [asynchronous iterable](https://docs.python.org/3.12/glossary.html#term-asynchronous-iterable).

    Added in version 3.5.

`class collections.abc.AsyncIterator`
:   ABC for classes that provide `__aiter__` and `__anext__`
    methods. See also the definition of [asynchronous iterator](https://docs.python.org/3.12/glossary.html#term-asynchronous-iterator).

    Added in version 3.5.

`class collections.abc.AsyncGenerator`
:   ABC for [asynchronous generator](https://docs.python.org/3.12/glossary.html#term-asynchronous-generator) classes that implement the protocol
    defined in [**PEP 525**](https://peps.python.org/pep-0525/) and [**PEP 492**](https://peps.python.org/pep-0492/).

    See [Annotating generators and coroutines](typing.md#annotating-generators-and-coroutines)
    for details on using `AsyncGenerator` in type annotations.

    Added in version 3.6.

`class collections.abc.Buffer`
:   ABC for classes that provide the [`__buffer__()`](https://docs.python.org/3.12/reference/datamodel.html#object.__buffer__ "object.__buffer__") method,
    implementing the [buffer protocol](https://docs.python.org/3.12/c-api/buffer.html#bufferobjects). See [**PEP 688**](https://peps.python.org/pep-0688/).

    Added in version 3.12.

## Examples and Recipes

ABCs allow us to ask classes or instances if they provide
particular functionality, for example:

```python3
size = None
if isinstance(myvar, collections.abc.Sized):
    size = len(myvar)
```

Several of the ABCs are also useful as mixins that make it easier to develop
classes supporting container APIs. For example, to write a class supporting
the full [`Set`](collections.abc.md#collections.abc.Set "collections.abc.Set") API, it is only necessary to supply the three underlying
abstract methods: [`__contains__()`](https://docs.python.org/3.12/reference/datamodel.html#object.__contains__ "object.__contains__"), [`__iter__()`](stdtypes.md#container.__iter__ "container.__iter__"), and
[`__len__()`](https://docs.python.org/3.12/reference/datamodel.html#object.__len__ "object.__len__"). The ABC supplies the remaining methods such as
`__and__()` and [`isdisjoint()`](stdtypes.md#frozenset.isdisjoint "frozenset.isdisjoint"):

```python3
class ListBasedSet(collections.abc.Set):
    ''' Alternate set implementation favoring space over speed
        and not requiring the set elements to be hashable. '''
    def __init__(self, iterable):
        self.elements = lst = []
        for value in iterable:
            if value not in lst:
                lst.append(value)

    def __iter__(self):
        return iter(self.elements)

    def __contains__(self, value):
        return value in self.elements

    def __len__(self):
        return len(self.elements)

s1 = ListBasedSet('abcdef')
s2 = ListBasedSet('defghi')
overlap = s1 & s2            # The __and__() method is supported automatically
```

Notes on using [`Set`](collections.abc.md#collections.abc.Set "collections.abc.Set") and [`MutableSet`](collections.abc.md#collections.abc.MutableSet "collections.abc.MutableSet") as a mixin:

1. Since some set operations create new sets, the default mixin methods need
   a way to create new instances from an [iterable](https://docs.python.org/3.12/glossary.html#term-iterable). The class constructor is
   assumed to have a signature in the form `ClassName(iterable)`.
   That assumption is factored-out to an internal [`classmethod`](functions.md#classmethod "classmethod") called
   `_from_iterable()` which calls `cls(iterable)` to produce a new set.
   If the [`Set`](collections.abc.md#collections.abc.Set "collections.abc.Set") mixin is being used in a class with a different
   constructor signature, you will need to override `_from_iterable()`
   with a classmethod or regular method that can construct new instances from
   an iterable argument.
2. To override the comparisons (presumably for speed, as the
   semantics are fixed), redefine [`__le__()`](https://docs.python.org/3.12/reference/datamodel.html#object.__le__ "object.__le__") and
   [`__ge__()`](https://docs.python.org/3.12/reference/datamodel.html#object.__ge__ "object.__ge__"),
   then the other operations will automatically follow suit.
3. The [`Set`](collections.abc.md#collections.abc.Set "collections.abc.Set") mixin provides a `_hash()` method to compute a hash value
   for the set; however, [`__hash__()`](https://docs.python.org/3.12/reference/datamodel.html#object.__hash__ "object.__hash__") is not defined because not all sets
   are [hashable](https://docs.python.org/3.12/glossary.html#term-hashable) or immutable. To add set hashability using mixins,
   inherit from both [`Set()`](collections.abc.md#collections.abc.Set "collections.abc.Set") and [`Hashable()`](collections.abc.md#collections.abc.Hashable "collections.abc.Hashable"), then define
   `__hash__ = Set._hash`.

> **See also:**
>
> - [OrderedSet recipe](https://code.activestate.com/recipes/576694/) for an
>   example built on [`MutableSet`](collections.abc.md#collections.abc.MutableSet "collections.abc.MutableSet").
> - For more about ABCs, see the [`abc`](abc.md#module-abc "abc: Abstract base classes according to :pep:`3119`.") module and [**PEP 3119**](https://peps.python.org/pep-3119/).
