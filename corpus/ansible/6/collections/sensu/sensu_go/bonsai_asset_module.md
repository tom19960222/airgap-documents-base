---
collection: ansible
version: "6"
title: "sensu.sensu_go.bonsai_asset module – Add Sensu assets from Bonsai"
source_url: https://docs.ansible.com/projects/ansible/6/collections/sensu/sensu_go/bonsai_asset_module.html
fetched_at: 2026-07-28T00:19:21+00:00
---
# sensu.sensu_go.bonsai_asset module – Add Sensu assets from Bonsai

> **Note:**
>
> This module is part of the [sensu.sensu_go collection](https://galaxy.ansible.com/sensu/sensu_go) (version 1.13.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install sensu.sensu_go`.
> You need further requirements to be able to use this module,
> see [Requirements](bonsai_asset_module.md#ansible-collections-sensu-sensu-go-bonsai-asset-module-requirements) for details.
>
> To use it in a playbook, specify: `sensu.sensu_go.bonsai_asset`.

New in sensu.sensu_go 1.0.0

- [Synopsis](bonsai_asset_module.md#synopsis)
- [Requirements](bonsai_asset_module.md#requirements)
- [Parameters](bonsai_asset_module.md#parameters)
- [Notes](bonsai_asset_module.md#notes)
- [See Also](bonsai_asset_module.md#see-also)
- [Examples](bonsai_asset_module.md#examples)
- [Return Values](bonsai_asset_module.md#return-values)

## [Synopsis](bonsai_asset_module.md#id1)

- Create or update a Sensu Go asset whose definition is available in the Bonsai, the Sensu asset index.
- For more information, refer to the Sensu documentation at <https://docs.sensu.io/sensu-go/latest/reference/assets/> and <https://bonsai.sensu.io/>.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](bonsai_asset_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7

## [Parameters](bonsai_asset_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **annotations**  dictionary | Custom metadata fields with fewer restrictions, as key/value pairs.  These are preserved by Sensu but not accessible as tokens or identifiers, and are mainly intended for use with external tools. |
| **auth**  dictionary | Authentication parameters. Can define each of them with ENV as well. |
| **api_key**  string  added in sensu.sensu_go 1.3.0 | The API key that should be used when authenticating. If this is not set, the value of the SENSU_API_KEY environment variable will be checked.  This replaces *auth.user* and *auth.password* parameters.  For more information about the API key, refer to the official Sensu documentation at <https://docs.sensu.io/sensu-go/latest/guides/use-apikey-feature/>. |
| **ca_path**  path  added in sensu.sensu_go 1.5.0 | Path to the CA bundle that should be used to validate the backend certificate.  If this parameter is not set, module will use the CA bundle that python is using.  It is also possible to set this parameter via the *SENSU_CA_PATH* environment variable. |
| **password**  string | The Sensu user’s password. If this is not set the value of the SENSU_PASSWORD environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  Default: `"P@ssw0rd!"` |
| **url**  string | Location of the Sensu backend API. If this is not set the value of the SENSU_URL environment variable will be checked.  Default: `"http://localhost:8080"` |
| **user**  string | The username to use for connecting to the Sensu API. If this is not set the value of the SENSU_USER environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  Default: `"admin"` |
| **verify**  boolean  added in sensu.sensu_go 1.5.0 | Flag that controls the certificate validation.  If you are using self-signed certificates, you can set this parameter to `false`.  ONLY USE THIS PARAMETER IN DEVELOPMENT SCENARIOS! In you use self-signed certificates in production, see the *auth.ca_path* parameter.  It is also possible to set this parameter via the *SENSU_VERIFY* environment variable.  Choices:   - `false` - `true` ← (default) |
| **labels**  dictionary | Custom metadata fields that can be accessed within Sensu, as key/value pairs. |
| **name**  string / required | The Sensu resource’s name. This name (in combination with the namespace where applicable) uniquely identifies the resource that Ansible operates on.  If the resource with selected name already exists, Ansible module will update it to match the specification in the task.  Consult the *name* metadata attribute specification in the upstream docs on <https://docs.sensu.io/sensu-go/latest/reference/> for more details about valid names and other restrictions. |
| **namespace**  string | RBAC namespace to operate in. If this is not set the value of the SENSU_NAMESPACE environment variable will be used.  Default: `"default"` |
| **on_remote**  boolean  added in sensu.sensu_go 1.13.0 | If set to `true`, module will download asset defnition on remote host.  If not set or set to `false`, ansible downloads asset definition on control node.  Choices:   - `false` - `true` |
| **rename**  string | The name that will be used when adding the asset to Sensu.  If not present, value of the *name* parameter will be used. |
| **version**  string / required | Version number of the asset to install. |

## [Notes](bonsai_asset_module.md#id4)

> **Note:**
>
> - *labels* and *annotations* values are merged with the values obtained from Bonsai. Values passed-in as parameters take precedence over the values obtained from Bonsai.
> - To delete an asset, use regular [sensu.sensu_go.asset](asset_module.md#ansible-collections-sensu-sensu-go-asset-module) module.

## [See Also](bonsai_asset_module.md#id5)

> **See also:**
>
> [sensu.sensu_go.asset](asset_module.md#ansible-collections-sensu-sensu-go-asset-module)
> :   Manage Sensu assets.
>
> [sensu.sensu_go.asset_info](asset_info_module.md#ansible-collections-sensu-sensu-go-asset-info-module)
> :   List Sensu assets.

## [Examples](bonsai_asset_module.md#id6)

```yaml+jinja
- name: Make sure specific version of asset is installed
  sensu.sensu_go.bonsai_asset:
    name: sensu/monitoring-plugins
    version: 2.2.0-1

- name: Remove previously added asset
  sensu.sensu_go.asset:
    name: sensu/monitoring-plugins
    state: absent

- name: Store Bonsai asset under a different name
  sensu.sensu_go.bonsai_asset:
    name: sensu/monitoring-plugins
    version: 2.2.0-1
    rename: sensu-monitoring-2.2.0-1

- name: Display asset info
  sensu.sensu_go.asset_info:
    name: sensu-monitoring-2.2.0-1  # value from rename field
```

## [Return Values](bonsai_asset_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **object**  dictionary | Object representing Sensu asset.  Returned: success  Sample: `{"builds": [{"sha512": "4f926bf4328f...2c58ad9ab40c9e2edc31b288d066b195b21b", "url": "http://example.com/asset.tar.gz"}], "metadata": {"name": "check_script", "namespace": "default"}}` |

### Authors

- Aljaz Kosir (@aljazkosir)
- Manca Bizjak (@mancabizjak)
- Tadej Borovsak (@tadeboro)

### Collection links

[Issue Tracker](https://github.com/sensu/sensu-go-ansible/issues)
[Repository (Sources)](https://github.com/sensu/sensu-go-ansible)
