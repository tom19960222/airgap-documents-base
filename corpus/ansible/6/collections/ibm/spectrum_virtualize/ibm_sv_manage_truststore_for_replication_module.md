---
collection: ansible
version: "6"
title: "ibm.spectrum_virtualize.ibm_sv_manage_truststore_for_replication module – This module manages certificate trust stores for replication on IBM Spectrum Virtualize family storage systems"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ibm/spectrum_virtualize/ibm_sv_manage_truststore_for_replication_module.html
fetched_at: 2026-07-27T17:50:23+00:00
---
# ibm.spectrum_virtualize.ibm_sv_manage_truststore_for_replication module – This module manages certificate trust stores for replication on IBM Spectrum Virtualize family storage systems

> **Note:**
>
> This module is part of the [ibm.spectrum_virtualize collection](https://galaxy.ansible.com/ibm/spectrum_virtualize) (version 1.10.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ibm.spectrum_virtualize`.
>
> To use it in a playbook, specify: `ibm.spectrum_virtualize.ibm_sv_manage_truststore_for_replication`.

New in ibm.spectrum_virtualize 1.10.0

- [Synopsis](ibm_sv_manage_truststore_for_replication_module.md#synopsis)
- [Parameters](ibm_sv_manage_truststore_for_replication_module.md#parameters)
- [Notes](ibm_sv_manage_truststore_for_replication_module.md#notes)
- [Examples](ibm_sv_manage_truststore_for_replication_module.md#examples)

## [Synopsis](ibm_sv_manage_truststore_for_replication_module.md#id1)

- Ansible interface to manage mktruststore and rmtruststore commands.
- This module transfers the certificate from a remote system to the local system.
- This module works on SSH and uses paramiko to establish an SSH connection.
- Once transfer is done successfully, it also adds the certificate to the trust store of the local system.
- This module can be used to set up mutual TLS (mTLS) for policy-based replication inter-system communication using cluster endpoint certificates (usually system-signed which are exported by the [ibm.spectrum_virtualize.ibm_sv_manage_ssl_certificate](ibm_sv_manage_ssl_certificate_module.md#ansible-collections-ibm-spectrum-virtualize-ibm-sv-manage-ssl-certificate-module) module).

## [Parameters](ibm_sv_manage_truststore_for_replication_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **clustername**  string / required | The hostname or management IP of the Spectrum Virtualize storage system. |
| **key_filename**  string | SSH client private key filename. By default, ~/.ssh/id_rsa is used. |
| **log_path**  string | Path of debug log file. |
| **name**  string | Specifies the name of the trust store.  If not specified, the module generates a name automatically with format store_I(remote_clustername). |
| **password**  string | Password for the Spectrum Virtualize storage system.  Mandatory, when *usesshkey=no*. |
| **remote_clustername**  string / required | Specifies the name of the partner remote cluster with which mTLS partnership needs to be setup. |
| **remote_password**  string | Password for remote cluster.  Applies when *state=present* to create a trust store. |
| **remote_username**  string | Username for remote cluster.  Applies when *state=present* to create a trust store. |
| **state**  string / required | Creates (`present`) or deletes (`absent`) a trust store.  Choices:   - `"present"` - `"absent"` |
| **username**  string / required | Username for the Spectrum Virtualize storage system. |
| **usesshkey**  string | For key-pair based SSH connection, set this field as “yes”. Provide full path of key in key_filename field. If not provided, default path of SSH key is used.  Choices:   - `"yes"` - `"no"` ← (default) |

## [Notes](ibm_sv_manage_truststore_for_replication_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_sv_manage_truststore_for_replication_module.md#id4)

```yaml+jinja
- name: Create truststore
  ibm.spectrum_virtualize.ibm_sv_manage_truststore_for_replication:
    clustername: "{{clustername}}"
    username: "{{username}}"
    password: "{{password}}"
    name: "{{name}}"
    remote_clustername: "{{remote_clustername}}"
    remote_username: "{{remote_username}}"
    remote_password: "{{remote_password}}"
    log_path: "{{log_path}}"
    state: "present"
- name: Delete truststore
  ibm.spectrum_virtualize.ibm_sv_manage_truststore_for_replication:
    clustername: "{{clustername}}"
    username: "{{username}}"
    password: "{{password}}"
    name: "{{name}}"
    remote_clustername: "{{remote_clustername}}"
    log_path: "{{log_path}}"
    state: "absent"
```

### Authors

- Sanjaikumaar M(@sanjaikumaar)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ibm.spectrum_virtualize/issues)
[Repository (Sources)](https://github.com/ansible-collections/ibm.spectrum_virtualize)
