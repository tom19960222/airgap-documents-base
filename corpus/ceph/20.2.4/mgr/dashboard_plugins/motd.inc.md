---
collection: ceph
version: "20.2.4"
title: "motd.inc"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/mgr/dashboard_plugins/motd.inc.rst
fetched_at: 2026-08-18T01:32:45Z
---
<a id="dashboard-motd"></a>

### Message of the day (MOTD)

Displays a configured "message of the day" (MOTD) at the top of the Ceph
Dashboard.

The importance of an MOTD can be configured by its severity, which is
``info``, ``warning`` or ``danger``. The MOTD can expire after a given time,
this means it will not be displayed in the UI anymore. Use the following
syntax to specify the expiration time: ``Ns|m|h|d|w``, where ``N`` is an
integer followed by seconds, minutes, hours, days and weeks. If the MOTD
should expire after 2 hours, use ``2h`` or ``5w`` for 5 weeks. Use ``0`` to
configure a MOTD that does not expire.

To configure a MOTD, run the following command:

```bash
ceph dashboard motd set <severity:info|warning|danger> <expires> <message>
```

To show the configured MOTD:

```bash
ceph dashboard motd get
```

To clear the configured MOTD run:

```bash
ceph dashboard motd clear
```

A MOTD with a severity of ``info`` or ``warning`` can be closed by the user.
The ``info`` MOTD is not displayed until the local storage cookies are
cleared or a new MOTD with a different severity is displayed. A MOTD with a
``warning`` severity will be displayed again in a new session.
