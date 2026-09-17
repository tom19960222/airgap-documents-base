---
collection: python
version: "3.10.21"
title: "types — Dynamic type creation and names for built-in types"
source_url: https://docs.python.org/3.10/library/types.html
fetched_at: 2026-09-17T15:13:36+00:00
---
# `types` — Dynamic type creation and names for built-in types

**Source code:** [Lib/types.py](https://github.com/python/cpython/tree/3.10/Lib/types.py)

---

This module defines utility functions to assist in dynamic creation of
new types.

It also defines names for some object types that are used by the standard
Python interpreter, but not exposed as builtins like [`int`](functions.md#int "int") or
[`str`](stdtypes.md#str "str") are.

Finally, it provides some additional type-related utility classes and functions
that are not fundamental enough to be builtins.

## Dynamic Type Creation

`types.new_class(name, bases=(), kwds=None, exec_body=None)`
:   Creates a class object dynamically using the appropriate metaclass.

    The first three arguments are the components that make up a class
    definition header: the class name, the base classes (in order), the
    keyword arguments (such as `metaclass`).

    The *exec_body* argument is a callback that is used to populate the
    freshly created class namespace. It should accept the class namespace
    as its sole argument and update the namespace directly with the class
    contents. If no callback is provided, it has the same effect as passing
    in `lambda ns: None`.

    New in version 3.3.

`types.prepare_class(name, bases=(), kwds=None)`
:   Calculates the appropriate metaclass and creates the class namespace.

    The arguments are the components that make up a class definition header:
    the class name, the base classes (in order) and the keyword arguments
    (such as `metaclass`).

    The return value is a 3-tuple: `metaclass, namespace, kwds`

    *metaclass* is the appropriate metaclass, *namespace* is the
    prepared class namespace and *kwds* is an updated copy of the passed
    in *kwds* argument with any `'metaclass'` entry removed. If no *kwds*
    argument is passed in, this will be an empty dict.

    New in version 3.3.

    Changed in version 3.6: The default value for the `namespace` element of the returned
    tuple has changed. Now an insertion-order-preserving mapping is
    used when the metaclass does not have a `__prepare__` method.

> **See also:**
>
> [Metaclasses](https://docs.python.org/3.10/reference/datamodel.html#metaclasses)
> :   Full details of the class creation process supported by these functions
>
> [**PEP 3115**](https://www.python.org/dev/peps/pep-3115) - Metaclasses in Python 3000
> :   Introduced the `__prepare__` namespace hook

`types.resolve_bases(bases)`
:   Resolve MRO entries dynamically as specified by [**PEP 560**](https://www.python.org/dev/peps/pep-0560).

    This function looks for items in *bases* that are not instances of
    [`type`](functions.md#type "type"), and returns a tuple where each such object that has
    an `__mro_entries__` method is replaced with an unpacked result of
    calling this method. If a *bases* item is an instance of [`type`](functions.md#type "type"),
    or it doesn’t have an `__mro_entries__` method, then it is included in
    the return tuple unchanged.

    New in version 3.7.

> **See also:**
>
> [**PEP 560**](https://www.python.org/dev/peps/pep-0560) - Core support for typing module and generic types

## Standard Interpreter Types

This module provides names for many of the types that are required to
implement a Python interpreter. It deliberately avoids including some of
the types that arise only incidentally during processing such as the
`listiterator` type.

Typical use of these names is for [`isinstance()`](functions.md#isinstance "isinstance") or
[`issubclass()`](functions.md#issubclass "issubclass") checks.

If you instantiate any of these types, note that signatures may vary between Python versions.

Standard names are defined for the following types:

`types.NoneType`
:   The type of [`None`](constants.md#None "None").

    New in version 3.10.

`types.FunctionType`

`types.LambdaType`
:   The type of user-defined functions and functions created by
    [`lambda`](https://docs.python.org/3.10/reference/expressions.html#lambda) expressions.

    Raises an [auditing event](sys.md#auditing) `function.__new__` with argument `code`.

    The audit event only occurs for direct instantiation of function objects,
    and is not raised for normal compilation.

`types.GeneratorType`
:   The type of [generator](https://docs.python.org/3.10/glossary.html#term-generator)-iterator objects, created by
    generator functions.

`types.CoroutineType`
:   The type of [coroutine](https://docs.python.org/3.10/glossary.html#term-coroutine) objects, created by
    [`async def`](https://docs.python.org/3.10/reference/compound_stmts.html#async-def) functions.

    New in version 3.5.

`types.AsyncGeneratorType`
:   The type of [asynchronous generator](https://docs.python.org/3.10/glossary.html#term-asynchronous-generator)-iterator objects, created by
    asynchronous generator functions.

    New in version 3.6.

`class types.CodeType(**kwargs)`
:   The type for code objects such as returned by [`compile()`](functions.md#compile "compile").

    Raises an [auditing event](sys.md#auditing) `code.__new__` with arguments `code`, `filename`, `name`, `argcount`, `posonlyargcount`, `kwonlyargcount`, `nlocals`, `stacksize`, `flags`.

    Note that the audited arguments may not match the names or positions
    required by the initializer. The audit event only occurs for direct
    instantiation of code objects, and is not raised for normal compilation.

    `replace(**kwargs)`
    :   Return a copy of the code object with new values for the specified fields.

        New in version 3.8.

`types.CellType`
:   The type for cell objects: such objects are used as containers for
    a function’s free variables.

    New in version 3.8.

`types.MethodType`
:   The type of methods of user-defined class instances.

`types.BuiltinFunctionType`

`types.BuiltinMethodType`
:   The type of built-in functions like [`len()`](functions.md#len "len") or [`sys.exit()`](sys.md#sys.exit "sys.exit"), and
    methods of built-in classes. (Here, the term “built-in” means “written in
    C”.)

`types.WrapperDescriptorType`
:   The type of methods of some built-in data types and base classes such as
    [`object.__init__()`](https://docs.python.org/3.10/reference/datamodel.html#object.__init__ "object.__init__") or [`object.__lt__()`](https://docs.python.org/3.10/reference/datamodel.html#object.__lt__ "object.__lt__").

    New in version 3.7.

`types.MethodWrapperType`
:   The type of *bound* methods of some built-in data types and base classes.
    For example it is the type of `object().__str__`.

    New in version 3.7.

`types.NotImplementedType`
:   The type of [`NotImplemented`](constants.md#NotImplemented "NotImplemented").

    New in version 3.10.

`types.MethodDescriptorType`
:   The type of methods of some built-in data types such as [`str.join()`](stdtypes.md#str.join "str.join").

    New in version 3.7.

`types.ClassMethodDescriptorType`
:   The type of *unbound* class methods of some built-in data types such as
    `dict.__dict__['fromkeys']`.

    New in version 3.7.

`class types.ModuleType(name, doc=None)`
:   The type of [modules](https://docs.python.org/3.10/glossary.html#term-module). The constructor takes the name of the
    module to be created and optionally its [docstring](https://docs.python.org/3.10/glossary.html#term-docstring).

    > **Note:**
    >
    > Use [`importlib.util.module_from_spec()`](importlib.md#importlib.util.module_from_spec "importlib.util.module_from_spec") to create a new module if you
    > wish to set the various import-controlled attributes.

    `__doc__`
    :   The [docstring](https://docs.python.org/3.10/glossary.html#term-docstring) of the module. Defaults to `None`.

    `__loader__`
    :   The [loader](https://docs.python.org/3.10/glossary.html#term-loader) which loaded the module. Defaults to `None`.

        This attribute is to match [`importlib.machinery.ModuleSpec.loader`](importlib.md#importlib.machinery.ModuleSpec.loader "importlib.machinery.ModuleSpec.loader")
        as stored in the [`__spec__`](https://docs.python.org/3.10/reference/import.html#spec__ "__spec__") object.

        > **Note:**
        >
        > A future version of Python may stop setting this attribute by default.
        > To guard against this potential change, preferably read from the
        > [`__spec__`](https://docs.python.org/3.10/reference/import.html#spec__ "__spec__") attribute instead or use
        > `getattr(module, "__loader__", None)` if you explicitly need to use
        > this attribute.

        Changed in version 3.4: Defaults to `None`. Previously the attribute was optional.

    `__name__`
    :   The name of the module. Expected to match
        [`importlib.machinery.ModuleSpec.name`](importlib.md#importlib.machinery.ModuleSpec.name "importlib.machinery.ModuleSpec.name").

    `__package__`
    :   Which [package](https://docs.python.org/3.10/glossary.html#term-package) a module belongs to. If the module is top-level
        (i.e. not a part of any specific package) then the attribute should be set
        to `''`, else it should be set to the name of the package (which can be
        [`__name__`](https://docs.python.org/3.10/reference/import.html#name__ "__name__") if the module is a package itself). Defaults to `None`.

        This attribute is to match [`importlib.machinery.ModuleSpec.parent`](importlib.md#importlib.machinery.ModuleSpec.parent "importlib.machinery.ModuleSpec.parent")
        as stored in the [`__spec__`](https://docs.python.org/3.10/reference/import.html#spec__ "__spec__") object.

        > **Note:**
        >
        > A future version of Python may stop setting this attribute by default.
        > To guard against this potential change, preferably read from the
        > [`__spec__`](https://docs.python.org/3.10/reference/import.html#spec__ "__spec__") attribute instead or use
        > `getattr(module, "__package__", None)` if you explicitly need to use
        > this attribute.

        Changed in version 3.4: Defaults to `None`. Previously the attribute was optional.

    `__spec__`
    :   A record of the module’s import-system-related state. Expected to be an
        instance of [`importlib.machinery.ModuleSpec`](importlib.md#importlib.machinery.ModuleSpec "importlib.machinery.ModuleSpec").

        New in version 3.4.

`types.EllipsisType`
:   The type of [`Ellipsis`](constants.md#Ellipsis "Ellipsis").

    New in version 3.10.

`class types.GenericAlias(t_origin, t_args)`
:   The type of [parameterized generics](stdtypes.md#types-genericalias) such as
    `list[int]`.

    `t_origin` should be a non-parameterized generic class, such as `list`,
    `tuple` or `dict`. `t_args` should be a [`tuple`](stdtypes.md#tuple "tuple") (possibly of
    length 1) of types which parameterize `t_origin`:

    ```python3
    >>> from types import GenericAlias

    >>> list[int] == GenericAlias(list, (int,))
    True
    >>> dict[str, int] == GenericAlias(dict, (str, int))
    True
    ```

    New in version 3.9.

    Changed in version 3.9.2: This type can now be subclassed.

`class types.UnionType`
:   The type of [union type expressions](stdtypes.md#types-union).

    New in version 3.10.

`class types.TracebackType(tb_next, tb_frame, tb_lasti, tb_lineno)`
:   The type of traceback objects such as found in `sys.exc_info()[2]`.

    See [the language reference](https://docs.python.org/3.10/reference/datamodel.html#traceback-objects) for details of the
    available attributes and operations, and guidance on creating tracebacks
    dynamically.

`types.FrameType`
:   The type of frame objects such as found in `tb.tb_frame` if `tb` is a
    traceback object.

    See [the language reference](https://docs.python.org/3.10/reference/datamodel.html#frame-objects) for details of the
    available attributes and operations.

`types.GetSetDescriptorType`
:   The type of objects defined in extension modules with `PyGetSetDef`, such
    as `FrameType.f_locals` or `array.array.typecode`. This type is used as
    descriptor for object attributes; it has the same purpose as the
    [`property`](functions.md#property "property") type, but for classes defined in extension modules.

`types.MemberDescriptorType`
:   The type of objects defined in extension modules with `PyMemberDef`, such
    as `datetime.timedelta.days`. This type is used as descriptor for simple C
    data members which use standard conversion functions; it has the same purpose
    as the [`property`](functions.md#property "property") type, but for classes defined in extension modules.

    **CPython implementation detail:** In other implementations of Python, this type may be identical to
    `GetSetDescriptorType`.

`class types.MappingProxyType(mapping)`
:   Read-only proxy of a mapping. It provides a dynamic view on the mapping’s
    entries, which means that when the mapping changes, the view reflects these
    changes.

    New in version 3.3.

    Changed in version 3.9: Updated to support the new union (`|`) operator from [**PEP 584**](https://www.python.org/dev/peps/pep-0584), which
    simply delegates to the underlying mapping.

    `key in proxy`
    :   Return `True` if the underlying mapping has a key *key*, else
        `False`.

    `proxy[key]`
    :   Return the item of the underlying mapping with key *key*. Raises a
        [`KeyError`](exceptions.md#KeyError "KeyError") if *key* is not in the underlying mapping.

    `iter(proxy)`
    :   Return an iterator over the keys of the underlying mapping. This is a
        shortcut for `iter(proxy.keys())`.

    `len(proxy)`
    :   Return the number of items in the underlying mapping.

    `copy()`
    :   Return a shallow copy of the underlying mapping.

    `get(key[, default])`
    :   Return the value for *key* if *key* is in the underlying mapping, else
        *default*. If *default* is not given, it defaults to `None`, so that
        this method never raises a [`KeyError`](exceptions.md#KeyError "KeyError").

    `items()`
    :   Return a new view of the underlying mapping’s items (`(key, value)`
        pairs).

    `keys()`
    :   Return a new view of the underlying mapping’s keys.

    `values()`
    :   Return a new view of the underlying mapping’s values.

    `reversed(proxy)`
    :   Return a reverse iterator over the keys of the underlying mapping.

        New in version 3.9.

## Additional Utility Classes and Functions

`class types.SimpleNamespace`
:   A simple [`object`](functions.md#object "object") subclass that provides attribute access to its
    namespace, as well as a meaningful repr.

    Unlike [`object`](functions.md#object "object"), with `SimpleNamespace` you can add and remove
    attributes. If a `SimpleNamespace` object is initialized with keyword
    arguments, those are directly added to the underlying namespace.

    The type is roughly equivalent to the following code:

    ```python3
    class SimpleNamespace:
        def __init__(self, /, **kwargs):
            self.__dict__.update(kwargs)

        def __repr__(self):
            items = (f"{k}={v!r}" for k, v in self.__dict__.items())
            return "{}({})".format(type(self).__name__, ", ".join(items))

        def __eq__(self, other):
            if isinstance(self, SimpleNamespace) and isinstance(other, SimpleNamespace):
               return self.__dict__ == other.__dict__
            return NotImplemented
    ```

    `SimpleNamespace` may be useful as a replacement for `class NS: pass`.
    However, for a structured record type use [`namedtuple()`](collections.md#collections.namedtuple "collections.namedtuple")
    instead.

    New in version 3.3.

    Changed in version 3.9: Attribute order in the repr changed from alphabetical to insertion (like
    `dict`).

`types.DynamicClassAttribute(fget=None, fset=None, fdel=None, doc=None)`
:   Route attribute access on a class to __getattr__.

    This is a descriptor, used to define attributes that act differently when
    accessed through an instance and through a class. Instance access remains
    normal, but access to an attribute through a class will be routed to the
    class’s __getattr__ method; this is done by raising AttributeError.

    This allows one to have properties active on an instance, and have virtual
    attributes on the class with the same name (see [`enum.Enum`](enum.md#enum.Enum "enum.Enum") for an example).

    New in version 3.4.

## Coroutine Utility Functions

`types.coroutine(gen_func)`
:   This function transforms a [generator](https://docs.python.org/3.10/glossary.html#term-generator) function into a
    [coroutine function](https://docs.python.org/3.10/glossary.html#term-coroutine-function) which returns a generator-based coroutine.
    The generator-based coroutine is still a [generator iterator](https://docs.python.org/3.10/glossary.html#term-generator-iterator),
    but is also considered to be a [coroutine](https://docs.python.org/3.10/glossary.html#term-coroutine) object and is
    [awaitable](https://docs.python.org/3.10/glossary.html#term-awaitable). However, it may not necessarily implement
    the [`__await__()`](https://docs.python.org/3.10/reference/datamodel.html#object.__await__ "object.__await__") method.

    If *gen_func* is a generator function, it will be modified in-place.

    If *gen_func* is not a generator function, it will be wrapped. If it
    returns an instance of [`collections.abc.Generator`](collections.abc.md#collections.abc.Generator "collections.abc.Generator"), the instance
    will be wrapped in an *awaitable* proxy object. All other types
    of objects will be returned as is.

    New in version 3.5.
