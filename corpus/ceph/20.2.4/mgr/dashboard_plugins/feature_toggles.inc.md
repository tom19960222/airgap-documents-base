---
collection: ceph
version: "20.2.4"
title: "feature_toggles.inc"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/mgr/dashboard_plugins/feature_toggles.inc.rst
fetched_at: 2026-08-18T01:32:45Z
---
<a id="dashboard-feature-toggles"></a>

### Feature Toggles

This plug-in allows to enable or disable some features from the Ceph Dashboard
on-demand. When a feature becomes disabled:

- Its front-end elements (web pages, menu entries, charts, etc.) will become
  hidden.
- Its associated REST API endpoints will reject any further requests (404, Not
  Found Error).

The main purpose of this plug-in is to allow ad hoc customizations of the
workflows exposed by the dashboard. Additionally, it could allow for dynamically
enabling experimental features with minimal configuration burden and no service
impact.

The list of features that can be enabled/disabled is:

- **Block (RBD)**:
   - Image Management: ``rbd``
   - Mirroring: ``mirroring``
   - iSCSI: ``iscsi``
- **Filesystem (Cephfs)**: ``cephfs``
- **Objects (RGW)**: ``rgw`` (including daemon, user and bucket management).
- **NFS**: ``nfs-ganesha`` exports.

By default all features come enabled.

To retrieve a list of features and their current statuses:

```bash
ceph dashboard feature status
```

:

```
Feature 'cephfs': 'enabled'
Feature 'iscsi': 'enabled'
Feature 'nvmeof': 'enabled'
Feature 'mirroring': 'enabled'
Feature 'rbd': 'enabled'
Feature 'rgw': 'enabled'
Feature 'nfs': 'enabled'
```

To enable or disable the status of a single or multiple features:

```bash
ceph dashboard feature disable iscsi mirroring
```

:

```
Feature 'iscsi': disabled
Feature 'mirroring': disabled
```

After a feature status has changed, the API REST endpoints immediately respond
to that change, but it may take up to twenty (20) seconds for the front-end UI
elements seconds to reflect the change.
