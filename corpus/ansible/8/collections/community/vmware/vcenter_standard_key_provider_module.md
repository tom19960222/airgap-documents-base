---
collection: ansible
version: "8"
title: "community.vmware.vcenter_standard_key_provider module – Add, reconfigure or remove Standard Key Provider on vCenter server"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vcenter_standard_key_provider_module.html
fetched_at: 2026-07-28T01:59:33+00:00
---
# community.vmware.vcenter_standard_key_provider module – Add, reconfigure or remove Standard Key Provider on vCenter server

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/ui/repo/published/community/vmware/) (version 3.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
>
> To use it in a playbook, specify: `community.vmware.vcenter_standard_key_provider`.

- [Synopsis](vcenter_standard_key_provider_module.md#synopsis)
- [Parameters](vcenter_standard_key_provider_module.md#parameters)
- [Notes](vcenter_standard_key_provider_module.md#notes)
- [Examples](vcenter_standard_key_provider_module.md#examples)
- [Return Values](vcenter_standard_key_provider_module.md#return-values)

## [Synopsis](vcenter_standard_key_provider_module.md#id1)

- This module is used for adding, reconfiguring or removing Standard Key Provider on vCenter server. Refer to VMware docs for more information: [Standard Key Provider](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-6DB1E745-9624-43EA-847C-DD2F767CB94B.html)

## [Parameters](vcenter_standard_key_provider_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **kms_info**  list / elements=dictionary | The information of an external key server (KMS).  `kms_name`, `kms_ip` are required when adding a Standard Key Provider.  If `kms_port` is not specified, the default port 5696 will be used.  `kms_ip`, `kms_port` can be reconfigured for an existing KMS with name `kms_name`.  **Default:** `[]` |
| **kms_ip**  string | IP address of the external KMS. |
| **kms_name**  string | Name of the KMS to be configured. |
| **kms_port**  integer | Port of the external KMS. |
| **remove_kms**  boolean | Remove the configured KMS with name `kms_name` from the KMIP cluster.  **Choices:**   - `false` - `true` |
| **kms_password**  string | Password to authenticate to the KMS. |
| **kms_username**  string | Username to authenticate to the KMS. |
| **make_kms_trust_vc**  dictionary | After adding the Standard Key Provider to the vCenter Server, you can establish a trusted connection, the exact process depends on the certificates that the key provider accepts, and on your company policy.  Three methods implemented here, (1) upload client certificate and private key through `upload_client_cert` and `upload_client_key` parameters, (2) generate, update, download vCenter self signed certificate through `download_self_signed_cert` parameter, (3) download generated Certificate Signing Request(CSR) through `download_client_csr` parameter, send it to KMS then upload the KMS signed CSR through `upload_kms_signed_client_csr` parameter.  This is not set to be mandatory, if not set, please go to vCenter to setup trust connection with KMS manually. |
| **download_client_csr**  path | The absolute path on local machine for keeping vCenter generated CSR.  Then upload the KMS signed CSR using `upload_kms_signed_client_csr` to vCenter. |
| **download_self_signed_cert**  path | The absolute path on local machine for keeping vCenter generated self signed client cert. |
| **upload_client_cert**  path | The absolute file path of client certificate.  Request a certificate and private key from the KMS vendor. The files are X509 files in PEM format.  The certificate might be already trusted by the KMS server. |
| **upload_client_key**  path | The absolute file path of client private key to be uploaded together with `upload_client_cert`. |
| **upload_kms_signed_client_csr**  path | The absolute file path of KMS signed CSR downloaded from `download_client_csr`. |
| **mark_default**  boolean | Set specified Key Provider with name `name` as the default Key Provider.  If new added Key Provider is the only key provider in vCenter, then will mark it as default after adding.  **Choices:**   - `false` ← (default) - `true` |
| **name**  string / required | Name of the Key Provider to be added, reconfigured or removed from vCenter. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the proxy server. |
| **proxy_server**  string | Address of the proxy server to connect to KMS. |
| **state**  string | If set to `absent`, the named Key Provider will be removed from vCenter.  If set to `present`, the named existing Key Provider will be reconfigured or new Key Provider will be added.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vcenter_standard_key_provider_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vcenter_standard_key_provider_module.md#id4)

```yaml+jinja
- name: Add a new Standard Key Provider with client certificate and private key
  community.vmware.vcenter_standard_key_provider:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    name: 'test_standard_kp'
    state: 'present'
    mark_default: true
    kms_info:
      - kms_name: test_kms_1
        kms_ip: 192.168.1.10
    make_kms_trust_vc:
      upload_client_cert: "/tmp/test_cert.pem"
      upload_client_key: "/tmp/test_cert_key.pem"
  register: add_skp_result

- name: Remove the KMS from the key provider cluster
  community.vmware.vcenter_standard_key_provider:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    name: 'test_standard_kp'
    state: 'present'
    kms_info:
      - kms_name: test_kms_1
        remove_kms: true
  register: remove_kms_result

- name: Remove the Standard Key Provider
  community.vmware.vcenter_standard_key_provider:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    name: 'test_standard_kp'
    state: 'absent'
  register: remove_kp_result
```

## [Return Values](vcenter_standard_key_provider_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **key_provider_clusters**  list / elements=string | the Key Provider cluster info  **Returned:** always  **Sample:** `[{"has_backup": null, "key_id": null, "key_provide_id": "test_standard", "management_type": null, "servers": [{"address": "192.168.1.10", "name": "test_kms", "port": 5696, "protocol": "", "proxy": "", "proxy_port": null, "user_name": ""}], "tpm_required": null, "use_as_default": true}]` |

### Authors

- Diane Wang (@Tomorrow9)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
