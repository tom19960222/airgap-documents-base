---
collection: ceph
version: "20.2.4"
title: "debug.inc"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/mgr/dashboard_plugins/debug.inc.rst
fetched_at: 2026-08-18T01:32:45Z
---
<a id="dashboard-debug"></a>

### Debug

This plugin allows to customize the behaviour of the dashboard according to the
debug mode. It can be enabled, disabled or checked with the following command:

```bash
ceph dashboard debug status
```

:

```
Debug: 'disabled'
```

```bash
ceph dashboard debug enable
```

:

```
Debug: 'enabled'
```

```bash
ceph dashboard debug disable
```

:

```
Debug: 'disabled'
```

By default, it's disabled. This is the recommended setting for production
deployments. If required, debug mode can be enabled without need of restarting.
Currently, disabled debug mode equals to CherryPy ``production`` environment,
while when enabled, it uses ``test_suite`` defaults (please refer to
[CherryPy Environments](https://docs.cherrypy.org/en/latest/config.html#environments) for more
details).

It also adds request uuid (``unique_id``) to Cherrypy on versions that don't
support this. It additionally prints the ``unique_id`` to error responses and
log messages.
