---
collection: python
version: "3.12.14"
title: "spwd — The shadow password database"
source_url: https://docs.python.org/3.12/library/spwd.html
fetched_at: 2026-09-17T15:35:44+00:00
---
# `spwd` — The shadow password database

Deprecated since version 3.11, will be removed in version 3.13: The [`spwd`](spwd.md#module-spwd "spwd: The shadow password database (getspnam() and friends). (deprecated) (Unix)") module is deprecated
(see [**PEP 594**](https://peps.python.org/pep-0594/#spwd) for details and alternatives).

---

This module provides access to the Unix shadow password database. It is
available on various Unix versions.

[Availability](intro.md#availability): not Emscripten, not WASI.

This module does not work or is not available on WebAssembly platforms
`wasm32-emscripten` and `wasm32-wasi`. See
[WebAssembly platforms](intro.md#wasm-availability) for more information.

You must have enough privileges to access the shadow password database (this
usually means you have to be root).

Shadow password database entries are reported as a tuple-like object, whose
attributes correspond to the members of the `spwd` structure (Attribute field
below, see `<shadow.h>`):

| Index | Attribute | Meaning |
| --- | --- | --- |
| 0 | `sp_namp` | Login name |
| 1 | `sp_pwdp` | Encrypted password |
| 2 | `sp_lstchg` | Date of last change |
| 3 | `sp_min` | Minimal number of days between changes |
| 4 | `sp_max` | Maximum number of days between changes |
| 5 | `sp_warn` | Number of days before password expires to warn user about it |
| 6 | `sp_inact` | Number of days after password expires until account is disabled |
| 7 | `sp_expire` | Number of days since 1970-01-01 when account expires |
| 8 | `sp_flag` | Reserved |

The sp_namp and sp_pwdp items are strings, all others are integers.
[`KeyError`](exceptions.md#KeyError "KeyError") is raised if the entry asked for cannot be found.

The following functions are defined:

`spwd.getspnam(name)`
:   Return the shadow password database entry for the given user name.

    Changed in version 3.6: Raises a [`PermissionError`](exceptions.md#PermissionError "PermissionError") instead of [`KeyError`](exceptions.md#KeyError "KeyError") if the user
    doesn’t have privileges.

`spwd.getspall()`
:   Return a list of all available shadow password database entries, in arbitrary
    order.

> **See also:**
>
> Module [`grp`](grp.md#module-grp "grp: The group database (getgrnam() and friends). (Unix)")
> :   An interface to the group database, similar to this.
>
> Module [`pwd`](pwd.md#module-pwd "pwd: The password database (getpwnam() and friends). (Unix)")
> :   An interface to the normal password database, similar to this.
