---
collection: python
version: "3.10.21"
title: "tkinter.scrolledtext — Scrolled Text Widget"
source_url: https://docs.python.org/3.10/library/tkinter.scrolledtext.html
fetched_at: 2026-09-17T15:14:42+00:00
---
# `tkinter.scrolledtext` — Scrolled Text Widget

**Source code:** [Lib/tkinter/scrolledtext.py](https://github.com/python/cpython/tree/3.10/Lib/tkinter/scrolledtext.py)

---

The [`tkinter.scrolledtext`](tkinter.scrolledtext.md#module-tkinter.scrolledtext "tkinter.scrolledtext: Text widget with a vertical scroll bar. (Tk)") module provides a class of the same name which
implements a basic text widget which has a vertical scroll bar configured to do
the “right thing.” Using the [`ScrolledText`](tkinter.scrolledtext.md#tkinter.scrolledtext.ScrolledText "tkinter.scrolledtext.ScrolledText") class is a lot easier than
setting up a text widget and scroll bar directly.

The text widget and scrollbar are packed together in a `Frame`, and the
methods of the `Grid` and `Pack` geometry managers are acquired
from the `Frame` object. This allows the [`ScrolledText`](tkinter.scrolledtext.md#tkinter.scrolledtext.ScrolledText "tkinter.scrolledtext.ScrolledText") widget to
be used directly to achieve most normal geometry management behavior.

Should more specific control be necessary, the following attributes are
available:

`class tkinter.scrolledtext.ScrolledText(master=None, **kw)`
:   `frame`
    :   The frame which surrounds the text and scroll bar widgets.

    `vbar`
    :   The scroll bar widget.
