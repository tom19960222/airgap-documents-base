---
collection: python
version: "3.10.21"
title: "nis — Interface to Sun’s NIS (Yellow Pages)"
source_url: https://docs.python.org/3.10/library/nis.html
fetched_at: 2026-09-17T15:15:22+00:00
---
# `nis` — Interface to Sun’s NIS (Yellow Pages)

Deprecated since version 3.11: The [`nis`](nis.md#module-nis "nis: Interface to Sun's NIS (Yellow Pages) library. (deprecated) (Unix)") module is deprecated
(see [**PEP 594**](https://www.python.org/dev/peps/pep-0594#nis) for details).

---

The [`nis`](nis.md#module-nis "nis: Interface to Sun's NIS (Yellow Pages) library. (deprecated) (Unix)") module gives a thin wrapper around the NIS library, useful for
central administration of several hosts.

Because NIS exists only on Unix systems, this module is only available for Unix.

The [`nis`](nis.md#module-nis "nis: Interface to Sun's NIS (Yellow Pages) library. (deprecated) (Unix)") module defines the following functions:

`nis.match(key, mapname, domain=default_domain)`
:   Return the match for *key* in map *mapname*, or raise an error
    ([`nis.error`](nis.md#nis.error "nis.error")) if there is none. Both should be strings, *key* is 8-bit
    clean. Return value is an arbitrary array of bytes (may contain `NULL` and
    other joys).

    Note that *mapname* is first checked if it is an alias to another name.

    The *domain* argument allows overriding the NIS domain used for the lookup. If
    unspecified, lookup is in the default NIS domain.

`nis.cat(mapname, domain=default_domain)`
:   Return a dictionary mapping *key* to *value* such that `match(key,
    mapname)==value`. Note that both keys and values of the dictionary are
    arbitrary arrays of bytes.

    Note that *mapname* is first checked if it is an alias to another name.

    The *domain* argument allows overriding the NIS domain used for the lookup. If
    unspecified, lookup is in the default NIS domain.

`nis.maps(domain=default_domain)`
:   Return a list of all valid maps.

    The *domain* argument allows overriding the NIS domain used for the lookup. If
    unspecified, lookup is in the default NIS domain.

`nis.get_default_domain()`
:   Return the system default NIS domain.

The [`nis`](nis.md#module-nis "nis: Interface to Sun's NIS (Yellow Pages) library. (deprecated) (Unix)") module defines the following exception:

`exception nis.error`
:   An error raised when a NIS function returns an error code.
