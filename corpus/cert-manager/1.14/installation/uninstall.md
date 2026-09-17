---
collection: cert-manager
version: "1.14"
title: "Uninstalling cert-manager"
source_url: https://github.com/cert-manager/website/blob/d2e1bdfbbe23fcf24dcb68ab54353a65a4131c20/content/v1.14-docs/installation/uninstall.md
fetched_at: 2026-09-15T21:21:15Z
app_version: "1.14.7"
---
cert-manager supports running on [Kubernetes](https://kubernetes.io) and
[OpenShift](https://www.openshift.com). The uninstallation process between the
two platforms is similar. Select the method that was used for installing
cert-manager to go to the relevant uninstall documentation.

- [kubectl](kubectl.md#uninstalling)
- [helm](helm.md#uninstalling)

If you need to preserve cert-manager custom resources (`Certificate`s, `Issuer`s etc), that are not version controlled or backed up by other means, take a look at our [backup and restore guide](../devops-tips/backup.md).
