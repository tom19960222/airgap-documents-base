---
collection: ansible
version: "8"
title: "community.general.linode_v4 module – Manage instances on the Linode cloud"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/linode_v4_module.html
fetched_at: 2026-07-28T01:47:31+00:00
---
# community.general.linode_v4 module – Manage instances on the Linode cloud

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](linode_v4_module.md#ansible-collections-community-general-linode-v4-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.linode_v4`.

- [Synopsis](linode_v4_module.md#synopsis)
- [Requirements](linode_v4_module.md#requirements)
- [Parameters](linode_v4_module.md#parameters)
- [Attributes](linode_v4_module.md#attributes)
- [Notes](linode_v4_module.md#notes)
- [Examples](linode_v4_module.md#examples)
- [Return Values](linode_v4_module.md#return-values)

## [Synopsis](linode_v4_module.md#id1)

- Manage instances on the Linode cloud.

Aliases: cloud.linode.linode_v4

## [Requirements](linode_v4_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- linode_api4 >= 2.0.0

## [Parameters](linode_v4_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string / required | The Linode API v4 access token. It may also be specified by exposing the [`LINODE_ACCESS_TOKEN`](../../environment_variables.md#envvar-LINODE_ACCESS_TOKEN) environment variable. See <https://www.linode.com/docs/api#access-and-authentication>. |
| **authorized_keys**  list / elements=string | A list of SSH public key parts to deploy for the root user. |
| **group**  string | The group that the instance should be marked under. Please note, that group labelling is deprecated but still supported. The encouraged method for marking instances is to use tags. |
| **image**  string | The image of the instance. This is a required parameter only when creating Linode instances. See <https://www.linode.com/docs/api/images/>. |
| **label**  string / required | The instance label. This label is used as the main determiner for idempotence for the module and is therefore mandatory. |
| **private_ip**  boolean  *added in community.general 3.0.0* | If `true`, the created Linode will have private networking enabled and assigned a private IPv4 address.  **Choices:**   - `false` ← (default) - `true` |
| **region**  string | The region of the instance. This is a required parameter only when creating Linode instances. See <https://www.linode.com/docs/api/regions/>. |
| **root_pass**  string | The password for the root user. If not specified, one will be generated. This generated password will be available in the task success JSON. |
| **stackscript_data**  dictionary  *added in community.general 1.3.0* | An object containing arguments to any User Defined Fields present in the StackScript used when creating the instance. Only valid when a stackscript_id is provided. See <https://www.linode.com/docs/api/stackscripts/>. |
| **stackscript_id**  integer  *added in community.general 1.3.0* | The numeric ID of the StackScript to use when creating the instance. See <https://www.linode.com/docs/api/stackscripts/>. |
| **state**  string / required | The desired instance state.  **Choices:**   - `"present"` - `"absent"` |
| **tags**  list / elements=string | The tags that the instance should be marked under. See <https://www.linode.com/docs/api/tags/>. |
| **type**  string | The type of the instance. This is a required parameter only when creating Linode instances. See <https://www.linode.com/docs/api/linode-types/>. |

## [Attributes](linode_v4_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](linode_v4_module.md#id5)

> **Note:**
>
> - No Linode resizing is currently implemented. This module will, in time, replace the current Linode module which uses deprecated API bindings on the Linode side.

## [Examples](linode_v4_module.md#id6)

```yaml+jinja
- name: Create a new Linode.
  community.general.linode_v4:
    label: new-linode
    type: g6-nanode-1
    region: eu-west
    image: linode/debian9
    root_pass: passw0rd
    authorized_keys:
      - "ssh-rsa ..."
    stackscript_id: 1337
    stackscript_data:
      variable: value
    state: present

- name: Delete that new Linode.
  community.general.linode_v4:
    label: new-linode
    state: absent
```

## [Return Values](linode_v4_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **instance**  dictionary | The instance description in JSON serialized form.  **Returned:** Always.  **Sample:** `{"alerts": {"cpu": 90, "io": 10000, "network_in": 10, "network_out": 10, "transfer_quota": 80}, "backups": {"enabled": false, "schedule": {"day": null, "window": null}}, "created": "2018-09-26T08:12:33", "group": "Foobar Group", "hypervisor": "kvm", "id": 10480444, "image": "linode/centos7", "ipv4": ["130.132.285.233"], "ipv6": "2a82:7e00::h03c:46ff:fe04:5cd2/64", "label": "lin-foo", "region": "eu-west", "root_pass": "foobar", "specs": {"disk": 25600, "memory": 1024, "transfer": 1000, "vcpus": 1}, "status": "running", "tags": [], "type": "g6-nanode-1", "updated": "2018-09-26T10:10:14", "watchdog_enabled": true}` |

### Authors

- Luke Murphy (@decentral1se)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
