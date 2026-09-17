---
collection: python
version: "3.12.14"
title: "tkinter.dnd — Drag and drop support"
source_url: https://docs.python.org/3.12/library/tkinter.dnd.html
fetched_at: 2026-09-17T15:34:29+00:00
---
# `tkinter.dnd` — Drag and drop support

**Source code:** [Lib/tkinter/dnd.py](https://github.com/python/cpython/tree/3.12/Lib/tkinter/dnd.py)

---

> **Note:**
>
> This is experimental and due to be deprecated when it is replaced
> with the Tk DND.

The [`tkinter.dnd`](tkinter.dnd.md#module-tkinter.dnd "tkinter.dnd: Tkinter drag-and-drop interface (Tk)") module provides drag-and-drop support for objects within
a single application, within the same window or between windows. To enable an
object to be dragged, you must create an event binding for it that starts the
drag-and-drop process. Typically, you bind a ButtonPress event to a callback
function that you write (see [Bindings and Events](tkinter.md#bindings-and-events)). The function should
call [`dnd_start()`](tkinter.dnd.md#tkinter.dnd.dnd_start "tkinter.dnd.dnd_start"), where ‘source’ is the object to be dragged, and ‘event’
is the event that invoked the call (the argument to your callback function).

Selection of a target object occurs as follows:

1. Top-down search of area under mouse for target widget

> - Target widget should have a callable *dnd_accept* attribute
> - If *dnd_accept* is not present or returns `None`, search moves to parent widget
> - If no target widget is found, then the target object is `None`

2. Call to *<old_target>.dnd_leave(source, event)*
3. Call to *<new_target>.dnd_enter(source, event)*
4. Call to *<target>.dnd_commit(source, event)* to notify of drop
5. Call to *<source>.dnd_end(target, event)* to signal end of drag-and-drop

`class tkinter.dnd.DndHandler(source, event)`
:   The *DndHandler* class handles drag-and-drop events tracking Motion and
    ButtonRelease events on the root of the event widget.

    `cancel(event=None)`
    :   Cancel the drag-and-drop process.

    `finish(event, commit=0)`
    :   Execute end of drag-and-drop functions.

    `on_motion(event)`
    :   Inspect area below mouse for target objects while drag is performed.

    `on_release(event)`
    :   Signal end of drag when the release pattern is triggered.

`tkinter.dnd.dnd_start(source, event)`
:   Factory function for drag-and-drop process.

> **See also:**
>
> [Bindings and Events](tkinter.md#bindings-and-events)
