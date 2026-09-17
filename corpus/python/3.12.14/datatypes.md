---
collection: python
version: "3.12.14"
title: "Data Types"
source_url: https://docs.python.org/3.12/library/datatypes.html
fetched_at: 2026-09-17T15:32:20+00:00
---
# Data Types

The modules described in this chapter provide a variety of specialized data
types such as dates and times, fixed-type arrays, heap queues, double-ended
queues, and enumerations.

Python also provides some built-in data types, in particular,
[`dict`](stdtypes.md#dict "dict"), [`list`](stdtypes.md#list "list"), [`set`](stdtypes.md#set "set") and [`frozenset`](stdtypes.md#frozenset "frozenset"), and
[`tuple`](stdtypes.md#tuple "tuple"). The [`str`](stdtypes.md#str "str") class is used to hold
Unicode strings, and the [`bytes`](stdtypes.md#bytes "bytes") and [`bytearray`](stdtypes.md#bytearray "bytearray") classes are used
to hold binary data.

The following modules are documented in this chapter:

- [`datetime` — Basic date and time types](datetime.md)
  - [Aware and Naive Objects](datetime.md#aware-and-naive-objects)
  - [Constants](datetime.md#constants)
  - [Available Types](datetime.md#available-types)
    - [Common Properties](datetime.md#common-properties)
    - [Determining if an Object is Aware or Naive](datetime.md#determining-if-an-object-is-aware-or-naive)
  - [`timedelta` Objects](datetime.md#timedelta-objects)
    - [Examples of usage: `timedelta`](datetime.md#examples-of-usage-timedelta)
  - [`date` Objects](datetime.md#date-objects)
    - [Examples of Usage: `date`](datetime.md#examples-of-usage-date)
  - [`datetime` Objects](datetime.md#datetime-objects)
    - [Examples of Usage: `datetime`](datetime.md#examples-of-usage-datetime)
  - [`time` Objects](datetime.md#time-objects)
    - [Examples of Usage: `time`](datetime.md#examples-of-usage-time)
  - [`tzinfo` Objects](datetime.md#tzinfo-objects)
  - [`timezone` Objects](datetime.md#timezone-objects)
  - [`strftime()` and `strptime()` Behavior](datetime.md#strftime-and-strptime-behavior)
    - [`strftime()` and `strptime()` Format Codes](datetime.md#strftime-and-strptime-format-codes)
    - [Technical Detail](datetime.md#technical-detail)
- [`zoneinfo` — IANA time zone support](zoneinfo.md)
  - [Using `ZoneInfo`](zoneinfo.md#using-zoneinfo)
  - [Data sources](zoneinfo.md#data-sources)
    - [Configuring the data sources](zoneinfo.md#configuring-the-data-sources)
      - [Compile-time configuration](zoneinfo.md#compile-time-configuration)
      - [Environment configuration](zoneinfo.md#environment-configuration)
      - [Runtime configuration](zoneinfo.md#runtime-configuration)
  - [The `ZoneInfo` class](zoneinfo.md#the-zoneinfo-class)
    - [String representations](zoneinfo.md#string-representations)
    - [Pickle serialization](zoneinfo.md#pickle-serialization)
  - [Functions](zoneinfo.md#functions)
  - [Globals](zoneinfo.md#globals)
  - [Exceptions and warnings](zoneinfo.md#exceptions-and-warnings)
- [`calendar` — General calendar-related functions](calendar.md)
  - [Command-Line Usage](calendar.md#command-line-usage)
- [`collections` — Container datatypes](collections.md)
  - [`ChainMap` objects](collections.md#chainmap-objects)
    - [`ChainMap` Examples and Recipes](collections.md#chainmap-examples-and-recipes)
  - [`Counter` objects](collections.md#counter-objects)
  - [`deque` objects](collections.md#deque-objects)
    - [`deque` Recipes](collections.md#deque-recipes)
  - [`defaultdict` objects](collections.md#defaultdict-objects)
    - [`defaultdict` Examples](collections.md#defaultdict-examples)
  - [`namedtuple()` Factory Function for Tuples with Named Fields](collections.md#namedtuple-factory-function-for-tuples-with-named-fields)
  - [`OrderedDict` objects](collections.md#ordereddict-objects)
    - [`OrderedDict` Examples and Recipes](collections.md#ordereddict-examples-and-recipes)
  - [`UserDict` objects](collections.md#userdict-objects)
  - [`UserList` objects](collections.md#userlist-objects)
  - [`UserString` objects](collections.md#userstring-objects)
- [`collections.abc` — Abstract Base Classes for Containers](collections.abc.md)
  - [Collections Abstract Base Classes](collections.abc.md#collections-abstract-base-classes)
  - [Collections Abstract Base Classes – Detailed Descriptions](collections.abc.md#collections-abstract-base-classes-detailed-descriptions)
  - [Examples and Recipes](collections.abc.md#examples-and-recipes)
- [`heapq` — Heap queue algorithm](heapq.md)
  - [Basic Examples](heapq.md#basic-examples)
  - [Priority Queue Implementation Notes](heapq.md#priority-queue-implementation-notes)
  - [Theory](heapq.md#theory)
- [`bisect` — Array bisection algorithm](bisect.md)
  - [Performance Notes](bisect.md#performance-notes)
  - [Searching Sorted Lists](bisect.md#searching-sorted-lists)
  - [Examples](bisect.md#examples)
- [`array` — Efficient arrays of numeric values](array.md)
- [`weakref` — Weak references](weakref.md)
  - [Weak Reference Objects](weakref.md#weak-reference-objects)
  - [Example](weakref.md#example)
  - [Finalizer Objects](weakref.md#finalizer-objects)
  - [Comparing finalizers with `__del__()` methods](weakref.md#comparing-finalizers-with-del-methods)
- [`types` — Dynamic type creation and names for built-in types](types.md)
  - [Dynamic Type Creation](types.md#dynamic-type-creation)
  - [Standard Interpreter Types](types.md#standard-interpreter-types)
  - [Additional Utility Classes and Functions](types.md#additional-utility-classes-and-functions)
  - [Coroutine Utility Functions](types.md#coroutine-utility-functions)
- [`copy` — Shallow and deep copy operations](copy.md)
- [`pprint` — Data pretty printer](pprint.md)
  - [Functions](pprint.md#functions)
  - [PrettyPrinter Objects](pprint.md#prettyprinter-objects)
  - [Example](pprint.md#example)
- [`reprlib` — Alternate `repr()` implementation](reprlib.md)
  - [Repr Objects](reprlib.md#repr-objects)
  - [Subclassing Repr Objects](reprlib.md#subclassing-repr-objects)
- [`enum` — Support for enumerations](enum.md)
  - [Module Contents](enum.md#module-contents)
  - [Data Types](enum.md#data-types)
    - [Supported `__dunder__` names](enum.md#supported-dunder-names)
    - [Supported `_sunder_` names](enum.md#supported-sunder-names)
  - [Utilities and Decorators](enum.md#utilities-and-decorators)
  - [Notes](enum.md#notes)
- [`graphlib` — Functionality to operate with graph-like structures](graphlib.md)
  - [Exceptions](graphlib.md#exceptions)
