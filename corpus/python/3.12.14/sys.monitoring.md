---
collection: python
version: "3.12.14"
title: "sys.monitoring — Execution event monitoring"
source_url: https://docs.python.org/3.12/library/sys.monitoring.html
fetched_at: 2026-09-17T15:34:54+00:00
---
# `sys.monitoring` — Execution event monitoring

Added in version 3.12.

---

> **Note:**
>
> [`sys.monitoring`](sys.monitoring.md#module-sys.monitoring "sys.monitoring: Access and control event monitoring") is a namespace within the [`sys`](sys.md#module-sys "sys: Access system-specific parameters and functions.") module,
> not an independent module, so there is no need to
> `import sys.monitoring`, simply `import sys` and then use
> `sys.monitoring`.

This namespace provides access to the functions and constants necessary to
activate and control event monitoring.

As programs execute, events occur that might be of interest to tools that
monitor execution. The [`sys.monitoring`](sys.monitoring.md#module-sys.monitoring "sys.monitoring: Access and control event monitoring") namespace provides means to
receive callbacks when events of interest occur.

The monitoring API consists of three components:

- [Tool identifiers](sys.monitoring.md#tool-identifiers)
- [Events](sys.monitoring.md#events)
- [Callbacks](sys.monitoring.md#callbacks)

## Tool identifiers

A tool identifier is an integer and the associated name.
Tool identifiers are used to discourage tools from interfering with each
other and to allow multiple tools to operate at the same time.
Currently tools are completely independent and cannot be used to
monitor each other. This restriction may be lifted in the future.

Before registering or activating events, a tool should choose an identifier.
Identifiers are integers in the range 0 to 5 inclusive.

### Registering and using tools

sys.monitoring.use_tool_id(*tool_id: [int](functions.md#int "int")*, *name: [str](stdtypes.md#str "str")*, */*) → [None](constants.md#None "None")
:   Must be called before *tool_id* can be used.
    *tool_id* must be in the range 0 to 5 inclusive.
    Raises a [`ValueError`](exceptions.md#ValueError "ValueError") if *tool_id* is in use.

sys.monitoring.free_tool_id(*tool_id: [int](functions.md#int "int")*, */*) → [None](constants.md#None "None")
:   Should be called once a tool no longer requires *tool_id*.

> **Note:**
>
> [`free_tool_id()`](sys.monitoring.md#sys.monitoring.free_tool_id "sys.monitoring.free_tool_id") will not disable global or local events associated
> with *tool_id*, nor will it unregister any callback functions. This
> function is only intended to be used to notify the VM that the
> particular *tool_id* is no longer in use.

sys.monitoring.get_tool(*tool_id: [int](functions.md#int "int")*, */*) → [str](stdtypes.md#str "str") | [None](constants.md#None "None")
:   Returns the name of the tool if *tool_id* is in use,
    otherwise it returns `None`.
    *tool_id* must be in the range 0 to 5 inclusive.

All IDs are treated the same by the VM with regard to events, but the
following IDs are pre-defined to make co-operation of tools easier:

```python3
sys.monitoring.DEBUGGER_ID = 0
sys.monitoring.COVERAGE_ID = 1
sys.monitoring.PROFILER_ID = 2
sys.monitoring.OPTIMIZER_ID = 5
```

There is no obligation to set an ID, nor is there anything preventing a tool
from using an ID even it is already in use.
However, tools are encouraged to use a unique ID and respect other tools.

## Events

The following events are supported:

sys.monitoring.events.BRANCH
:   A conditional branch is taken (or not).

sys.monitoring.events.CALL
:   A call in Python code (event occurs before the call).

sys.monitoring.events.C_RAISE
:   An exception raised from any callable, except for Python functions (event occurs after the exit).

sys.monitoring.events.C_RETURN
:   Return from any callable, except for Python functions (event occurs after the return).

sys.monitoring.events.EXCEPTION_HANDLED
:   An exception is handled.

sys.monitoring.events.INSTRUCTION
:   A VM instruction is about to be executed.

sys.monitoring.events.JUMP
:   An unconditional jump in the control flow graph is made.

sys.monitoring.events.LINE
:   An instruction is about to be executed that has a different line number from the preceding instruction.

sys.monitoring.events.PY_RESUME
:   Resumption of a Python function (for generator and coroutine functions), except for `throw()` calls.

sys.monitoring.events.PY_RETURN
:   Return from a Python function (occurs immediately before the return, the callee’s frame will be on the stack).

sys.monitoring.events.PY_START
:   Start of a Python function (occurs immediately after the call, the callee’s frame will be on the stack)

sys.monitoring.events.PY_THROW
:   A Python function is resumed by a `throw()` call.

sys.monitoring.events.PY_UNWIND
:   Exit from a Python function during exception unwinding.

sys.monitoring.events.PY_YIELD
:   Yield from a Python function (occurs immediately before the yield, the callee’s frame will be on the stack).

sys.monitoring.events.RAISE
:   An exception is raised, except those that cause a [`STOP_ITERATION`](sys.monitoring.md#monitoring-event-STOP_ITERATION) event.

sys.monitoring.events.RERAISE
:   An exception is re-raised, for example at the end of a [`finally`](https://docs.python.org/3.12/reference/compound_stmts.html#finally) block.

sys.monitoring.events.STOP_ITERATION
:   An artificial [`StopIteration`](exceptions.md#StopIteration "StopIteration") is raised; see [the STOP_ITERATION event](sys.monitoring.md#the-stop-iteration-event).

More events may be added in the future.

These events are attributes of the `sys.monitoring.events` namespace.
Each event is represented as a power-of-2 integer constant.
To define a set of events, simply bitwise or the individual events together.
For example, to specify both [`PY_RETURN`](sys.monitoring.md#monitoring-event-PY_RETURN) and [`PY_START`](sys.monitoring.md#monitoring-event-PY_START)
events, use the expression `PY_RETURN | PY_START`.

sys.monitoring.events.NO_EVENTS
:   An alias for `0` so users can do explicit comparisons like:

    ```python3
    if get_events(DEBUGGER_ID) == NO_EVENTS:
        ...
    ```

Events are divided into three groups:

### Local events

Local events are associated with normal execution of the program and happen
at clearly defined locations. All local events can be disabled.
The local events are:

- [`PY_START`](sys.monitoring.md#monitoring-event-PY_START)
- [`PY_RESUME`](sys.monitoring.md#monitoring-event-PY_RESUME)
- [`PY_RETURN`](sys.monitoring.md#monitoring-event-PY_RETURN)
- [`PY_YIELD`](sys.monitoring.md#monitoring-event-PY_YIELD)
- [`CALL`](sys.monitoring.md#monitoring-event-CALL)
- [`LINE`](sys.monitoring.md#monitoring-event-LINE)
- [`INSTRUCTION`](sys.monitoring.md#monitoring-event-INSTRUCTION)
- [`JUMP`](sys.monitoring.md#monitoring-event-JUMP)
- [`BRANCH`](sys.monitoring.md#monitoring-event-BRANCH)
- [`STOP_ITERATION`](sys.monitoring.md#monitoring-event-STOP_ITERATION)

### Ancillary events

Ancillary events can be monitored like other events, but are controlled
by another event:

- [`C_RAISE`](sys.monitoring.md#monitoring-event-C_RAISE)
- [`C_RETURN`](sys.monitoring.md#monitoring-event-C_RETURN)

The [`C_RETURN`](sys.monitoring.md#monitoring-event-C_RETURN) and [`C_RAISE`](sys.monitoring.md#monitoring-event-C_RAISE) events
are controlled by the [`CALL`](sys.monitoring.md#monitoring-event-CALL) event.
[`C_RETURN`](sys.monitoring.md#monitoring-event-C_RETURN) and [`C_RAISE`](sys.monitoring.md#monitoring-event-C_RAISE) events will only be seen if the
corresponding [`CALL`](sys.monitoring.md#monitoring-event-CALL) event is being monitored.

### Other events

Other events are not necessarily tied to a specific location in the
program and cannot be individually disabled.

The other events that can be monitored are:

- [`PY_THROW`](sys.monitoring.md#monitoring-event-PY_THROW)
- [`PY_UNWIND`](sys.monitoring.md#monitoring-event-PY_UNWIND)
- [`RAISE`](sys.monitoring.md#monitoring-event-RAISE)
- [`EXCEPTION_HANDLED`](sys.monitoring.md#monitoring-event-EXCEPTION_HANDLED)

### The STOP_ITERATION event

[**PEP 380**](https://peps.python.org/pep-0380/#use-of-stopiteration-to-return-values)
specifies that a [`StopIteration`](exceptions.md#StopIteration "StopIteration") exception is raised when returning a value
from a generator or coroutine. However, this is a very inefficient way to
return a value, so some Python implementations, notably CPython 3.12+, do not
raise an exception unless it would be visible to other code.

To allow tools to monitor for real exceptions without slowing down generators
and coroutines, the [`STOP_ITERATION`](sys.monitoring.md#monitoring-event-STOP_ITERATION) event is provided.
[`STOP_ITERATION`](sys.monitoring.md#monitoring-event-STOP_ITERATION) can be locally disabled, unlike [`RAISE`](sys.monitoring.md#monitoring-event-RAISE).

## Turning events on and off

In order to monitor an event, it must be turned on and a corresponding callback
must be registered.
Events can be turned on or off by setting the events either globally or
for a particular code object.

### Setting events globally

Events can be controlled globally by modifying the set of events being monitored.

sys.monitoring.get_events(*tool_id: [int](functions.md#int "int")*, */*) → [int](functions.md#int "int")
:   Returns the `int` representing all the active events.

sys.monitoring.set_events(*tool_id: [int](functions.md#int "int")*, *event_set: [int](functions.md#int "int")*, */*) → [None](constants.md#None "None")
:   Activates all events which are set in *event_set*.
    Raises a [`ValueError`](exceptions.md#ValueError "ValueError") if *tool_id* is not in use.

No events are active by default.

### Per code object events

Events can also be controlled on a per code object basis.

sys.monitoring.get_local_events(*tool_id: [int](functions.md#int "int")*, *code: [CodeType](types.md#types.CodeType "types.CodeType")*, */*) → [int](functions.md#int "int")
:   Returns all the local events for *code*

sys.monitoring.set_local_events(*tool_id: [int](functions.md#int "int")*, *code: [CodeType](types.md#types.CodeType "types.CodeType")*, *event_set: [int](functions.md#int "int")*, */*) → [None](constants.md#None "None")
:   Activates all the local events for *code* which are set in *event_set*.
    Raises a [`ValueError`](exceptions.md#ValueError "ValueError") if *tool_id* is not in use.

Local events add to global events, but do not mask them.
In other words, all global events will trigger for a code object,
regardless of the local events.

### Disabling events

sys.monitoring.DISABLE
:   A special value that can be returned from a callback function to disable
    events for the current code location.

Local events can be disabled for a specific code location by returning
[`sys.monitoring.DISABLE`](sys.monitoring.md#sys.monitoring.DISABLE "sys.monitoring.DISABLE") from a callback function. This does not change
which events are set, or any other code locations for the same event.

Disabling events for specific locations is very important for high
performance monitoring. For example, a program can be run under a
debugger with no overhead if the debugger disables all monitoring
except for a few breakpoints.

sys.monitoring.restart_events() → [None](constants.md#None "None")
:   Enable all the events that were disabled by [`sys.monitoring.DISABLE`](sys.monitoring.md#sys.monitoring.DISABLE "sys.monitoring.DISABLE")
    for all tools.

## Registering callback functions

To register a callable for events call

sys.monitoring.register_callback(*tool_id: [int](functions.md#int "int")*, *event: [int](functions.md#int "int")*, *func: [Callable](collections.abc.md#collections.abc.Callable "collections.abc.Callable") | [None](constants.md#None "None")*, */*) → [Callable](collections.abc.md#collections.abc.Callable "collections.abc.Callable") | [None](constants.md#None "None")
:   Registers the callable *func* for the *event* with the given *tool_id*

    If another callback was registered for the given *tool_id* and *event*,
    it is unregistered and returned.
    Otherwise [`register_callback()`](sys.monitoring.md#sys.monitoring.register_callback "sys.monitoring.register_callback") returns `None`.

Functions can be unregistered by calling
`sys.monitoring.register_callback(tool_id, event, None)`.

Callback functions can be registered and unregistered at any time.

Registering or unregistering a callback function will generate a [`sys.audit()`](sys.md#sys.audit "sys.audit") event.

### Callback function arguments

sys.monitoring.MISSING
:   A special value that is passed to a callback function to indicate
    that there are no arguments to the call.

When an active event occurs, the registered callback function is called.
Different events will provide the callback function with different arguments, as follows:

- [`PY_START`](sys.monitoring.md#monitoring-event-PY_START) and [`PY_RESUME`](sys.monitoring.md#monitoring-event-PY_RESUME):

  ```python3
  func(code: CodeType, instruction_offset: int) -> DISABLE | Any
  ```
- [`PY_RETURN`](sys.monitoring.md#monitoring-event-PY_RETURN) and [`PY_YIELD`](sys.monitoring.md#monitoring-event-PY_YIELD):

  ```python3
  func(code: CodeType, instruction_offset: int, retval: object) -> DISABLE | Any
  ```
- [`CALL`](sys.monitoring.md#monitoring-event-CALL), [`C_RAISE`](sys.monitoring.md#monitoring-event-C_RAISE) and [`C_RETURN`](sys.monitoring.md#monitoring-event-C_RETURN):

  ```python3
  func(code: CodeType, instruction_offset: int, callable: object, arg0: object | MISSING) -> DISABLE | Any
  ```

  If there are no arguments, *arg0* is set to [`sys.monitoring.MISSING`](sys.monitoring.md#sys.monitoring.MISSING "sys.monitoring.MISSING").
- [`RAISE`](sys.monitoring.md#monitoring-event-RAISE), [`RERAISE`](sys.monitoring.md#monitoring-event-RERAISE), [`EXCEPTION_HANDLED`](sys.monitoring.md#monitoring-event-EXCEPTION_HANDLED),
  [`PY_UNWIND`](sys.monitoring.md#monitoring-event-PY_UNWIND), [`PY_THROW`](sys.monitoring.md#monitoring-event-PY_THROW) and [`STOP_ITERATION`](sys.monitoring.md#monitoring-event-STOP_ITERATION):

  ```python3
  func(code: CodeType, instruction_offset: int, exception: BaseException) -> DISABLE | Any
  ```
- [`LINE`](sys.monitoring.md#monitoring-event-LINE):

  ```python3
  func(code: CodeType, line_number: int) -> DISABLE | Any
  ```
- [`BRANCH`](sys.monitoring.md#monitoring-event-BRANCH) and [`JUMP`](sys.monitoring.md#monitoring-event-JUMP):

  ```python3
  func(code: CodeType, instruction_offset: int, destination_offset: int) -> DISABLE | Any
  ```

  Note that the *destination_offset* is where the code will next execute.
  For an untaken branch this will be the offset of the instruction following
  the branch.
- [`INSTRUCTION`](sys.monitoring.md#monitoring-event-INSTRUCTION):

  ```python3
  func(code: CodeType, instruction_offset: int) -> DISABLE | Any
  ```
