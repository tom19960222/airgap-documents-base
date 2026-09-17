---
collection: python
version: "3.10.21"
title: "tkinter.colorchooser — Color choosing dialog"
source_url: https://docs.python.org/3.10/library/tkinter.colorchooser.html
fetched_at: 2026-09-17T15:14:41+00:00
---
# `tkinter.colorchooser` — Color choosing dialog

**Source code:** [Lib/tkinter/colorchooser.py](https://github.com/python/cpython/tree/3.10/Lib/tkinter/colorchooser.py)

---

The [`tkinter.colorchooser`](tkinter.colorchooser.md#module-tkinter.colorchooser "tkinter.colorchooser: Color choosing dialog (Tk)") module provides the [`Chooser`](tkinter.colorchooser.md#tkinter.colorchooser.Chooser "tkinter.colorchooser.Chooser") class
as an interface to the native color picker dialog. `Chooser` implements
a modal color choosing dialog window. The `Chooser` class inherits from
the [`Dialog`](dialog.md#tkinter.commondialog.Dialog "tkinter.commondialog.Dialog") class.

`class tkinter.colorchooser.Chooser(master=None, **options)`

`tkinter.colorchooser.askcolor(color=None, **options)`
:   Create a color choosing dialog. A call to this method will show the window,
    wait for the user to make a selection, and return the selected color (or
    `None`) to the caller.

> **See also:**
>
> Module [`tkinter.commondialog`](dialog.md#module-tkinter.commondialog "tkinter.commondialog: Tkinter base class for dialogs (Tk)")
> :   Tkinter standard dialog module
