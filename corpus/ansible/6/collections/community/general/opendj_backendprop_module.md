---
collection: ansible
version: "6"
title: "community.general.opendj_backendprop module – Will update the backend configuration of OpenDJ via the dsconfig set-backend-prop command"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/opendj_backendprop_module.html
fetched_at: 2026-07-27T17:11:34+00:00
---
# community.general.opendj_backendprop module – Will update the backend configuration of OpenDJ via the dsconfig set-backend-prop command

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.opendj_backendprop`.

- [Synopsis](opendj_backendprop_module.md#synopsis)
- [Parameters](opendj_backendprop_module.md#parameters)
- [Examples](opendj_backendprop_module.md#examples)

## [Synopsis](opendj_backendprop_module.md#id1)

- This module will update settings for OpenDJ with the command set-backend-prop.
- It will check first via de get-backend-prop if configuration needs to be applied.

## [Parameters](opendj_backendprop_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **backend**  string / required | The name of the backend on which the property needs to be updated. |
| **hostname**  string / required | The hostname of the OpenDJ server. |
| **name**  string / required | The configuration setting to update. |
| **opendj_bindir**  path | The path to the bin directory of OpenDJ.  Default: `"/opt/opendj/bin"` |
| **password**  string | The password for the cn=Directory Manager user.  Either password or passwordfile is needed. |
| **passwordfile**  path | Location to the password file which holds the password for the cn=Directory Manager user.  Either password or passwordfile is needed. |
| **port**  string / required | The Admin port on which the OpenDJ instance is available. |
| **state**  string | If configuration needs to be added/updated  Default: `"present"` |
| **username**  string | The username to connect to.  Default: `"cn=Directory Manager"` |
| **value**  string / required | The value for the configuration item. |

## [Examples](opendj_backendprop_module.md#id3)

```yaml+jinja
- name: Add or update OpenDJ backend properties
  action: opendj_backendprop
          hostname=localhost
          port=4444
          username="cn=Directory Manager"
          password=password
          backend=userRoot
          name=index-entry-limit
          value=5000
```

### Authors

- Werner Dijkerman (@dj-wasabi)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
