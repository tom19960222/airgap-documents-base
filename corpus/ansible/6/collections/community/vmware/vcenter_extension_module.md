---
collection: ansible
version: "6"
title: "community.vmware.vcenter_extension module – Register/deregister vCenter Extensions"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vcenter_extension_module.html
fetched_at: 2026-07-27T17:21:17+00:00
---
# community.vmware.vcenter_extension module – Register/deregister vCenter Extensions

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/community/vmware) (version 2.10.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
>
> To use it in a playbook, specify: `community.vmware.vcenter_extension`.

- [Synopsis](vcenter_extension_module.md#synopsis)
- [Parameters](vcenter_extension_module.md#parameters)
- [Notes](vcenter_extension_module.md#notes)
- [Examples](vcenter_extension_module.md#examples)
- [Return Values](vcenter_extension_module.md#return-values)

## [Synopsis](vcenter_extension_module.md#id1)

- This module can be used to register/deregister vCenter Extensions.

## [Parameters](vcenter_extension_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **client_type**  string | Required for `state=present`. Type of client the extension is (win32, .net, linux, etc.).  Default: `"vsphere-client-serenity"` |
| **company**  string | Required for `state=present`. The name of the company that makes the extension. |
| **description**  string | Required for `state=present`. A short description of the extension. |
| **email**  string | Required for `state=present`. Administrator email to use for extension. |
| **extension_key**  string / required | The extension key of the extension to install or uninstall. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **name**  string | Required for `state=present`. The name of the extension you are installing. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **server_type**  string | Required for `state=present`. Type of server being used to install the extension (SOAP, REST, HTTP, etc.).  Default: `"vsphere-client-serenity"` |
| **ssl_thumbprint**  string | Required for `state=present`. SSL thumbprint of the extension hosting server. |
| **state**  string | Add or remove vCenter Extension.  Choices:   - `"absent"` - `"present"` ← (default) |
| **url**  string | Required for `state=present`. Link to server hosting extension zip file to install. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |
| **version**  string / required | The version of the extension you are installing or uninstalling. |
| **visible**  boolean | Show the extension in solution manager inside vCenter.  Choices:   - `false` - `true` ← (default) |

## [Notes](vcenter_extension_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vcenter_extension_module.md#id4)

```yaml+jinja
- name: Register vCenter Extension
  community.vmware.vcenter_extension:
     hostname: "{{ groups['vcsa'][0] }}"
     username: "{{ vcenter_username }}"
     password: "{{ site_password }}"
     extension_key: "{{ extension_key }}"
     version: "1.0"
     company: "Acme"
     name: "Acme Extension"
     description: "acme management"
     email: "user@example.com"
     url: "https://10.0.0.1/ACME-vSphere-web-plugin-1.0.zip"
     ssl_thumbprint: "{{ ssl_thumbprint }}"
     state: present
  delegate_to: localhost
  register: register_extension

- name: Deregister vCenter Extension
  community.vmware.vcenter_extension:
     hostname: "{{ groups['vcsa'][0] }}"
     username: "{{ vcenter_username }}"
     password: "{{ site_password }}"
     extension_key: "{{ extension_key }}"
     version: "1.0"
     state: absent
  delegate_to: localhost
  register: deregister_extension
```

## [Return Values](vcenter_extension_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  string | information about performed operation  Returned: always  Sample: `"'com.acme.Extension' installed."` |

### Authors

- Michael Tipton (@castawayegr)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
