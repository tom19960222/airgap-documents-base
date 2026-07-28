---
collection: ansible
version: "6"
title: "sensu.sensu_go.asset module – Manage Sensu assets"
source_url: https://docs.ansible.com/projects/ansible/6/collections/sensu/sensu_go/asset_module.html
fetched_at: 2026-07-28T00:19:19+00:00
---
# sensu.sensu_go.asset module – Manage Sensu assets

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
> see [Requirements](asset_module.md#ansible-collections-sensu-sensu-go-asset-module-requirements) for details.
>
> To use it in a playbook, specify: `sensu.sensu_go.asset`.

New in sensu.sensu_go 1.0.0

- [Synopsis](asset_module.md#synopsis)
- [Requirements](asset_module.md#requirements)
- [Parameters](asset_module.md#parameters)
- [See Also](asset_module.md#see-also)
- [Examples](asset_module.md#examples)
- [Return Values](asset_module.md#return-values)

## [Synopsis](asset_module.md#id1)

- Create, update or delete Sensu Go asset.
- For more information, refer to the Sensu documentation at <https://docs.sensu.io/sensu-go/latest/reference/assets/>.

## [Requirements](asset_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7

## [Parameters](asset_module.md#id3)

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
| **builds**  list / elements=dictionary | A list of asset builds used to define multiple artefacts which provide the named asset.  Required if *state* is `present`. |
| **filters**  list / elements=string | A set of Sensu query expressions used to determine if the asset should be installed. |
| **headers**  dictionary | Additional headers to send when retrieving the asset, e.g. for authorization. |
| **sha512**  string / required | The checksum of the asset. |
| **url**  string / required | The URL location of the asset. |
| **labels**  dictionary | Custom metadata fields that can be accessed within Sensu, as key/value pairs. |
| **name**  string / required | The Sensu resource’s name. This name (in combination with the namespace where applicable) uniquely identifies the resource that Ansible operates on.  If the resource with selected name already exists, Ansible module will update it to match the specification in the task.  Consult the *name* metadata attribute specification in the upstream docs on <https://docs.sensu.io/sensu-go/latest/reference/> for more details about valid names and other restrictions. |
| **namespace**  string | RBAC namespace to operate in. If this is not set the value of the SENSU_NAMESPACE environment variable will be used.  Default: `"default"` |
| **state**  string | Target state of the Sensu object.  Choices:   - `"present"` ← (default) - `"absent"` |

## [See Also](asset_module.md#id4)

> **See also:**
>
> [sensu.sensu_go.asset_info](asset_info_module.md#ansible-collections-sensu-sensu-go-asset-info-module)
> :   List Sensu assets.
>
> [sensu.sensu_go.bonsai_asset](bonsai_asset_module.md#ansible-collections-sensu-sensu-go-bonsai-asset-module)
> :   Add Sensu assets from Bonsai.

## [Examples](asset_module.md#id5)

```yaml+jinja
- name: Create a multiple-build asset
  sensu.sensu_go.asset:
    name: sensu-plugins-cpu-checks
    builds:
      - url: https://assets.bonsai.sensu.io/68546e739d96fd695655b77b35b5aabfbabeb056/sensu-plugins-cpu-checks_4.0.0_centos_linux_amd64.tar.gz
        sha512: 518e7c17cf670393045bff4af318e1d35955bfde166e9ceec2b469109252f79043ed133241c4dc96501b6636a1ec5e008ea9ce055d1609865635d4f004d7187b
        filters:
          - entity.system.os == 'linux'
          - entity.system.arch == 'amd64'
          - entity.system.platform == 'rhel'
      - url: https://assets.bonsai.sensu.io/68546e739d96fd695655b77b35b5aabfbabeb056/sensu-plugins-cpu-checks_4.0.0_alpine_linux_amd64.tar.gz
        sha512: b2da25ecd7642e6de41fde37d674fe19dcb6ee3d680e145e32289f7cfc352e6b5f9413ee9b701d61faeaa47b399aa30b25885dbc1ca432c4061c8823774c28f3
        filters:
          - entity.system.os == 'linux'
          - entity.system.arch == 'amd64'
          - entity.system.platform == 'alpine'

- name: Delete an asset
  sensu.sensu_go.asset:
    name: sensu-plugins-cpu-check
    state: absent
```

## [Return Values](asset_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **object**  dictionary | Object representing Sensu asset.  Returned: success  Sample: `{"builds": [{"sha512": "4f926bf4328f...2c58ad9ab40c9e2edc31b288d066b195b21b", "url": "http://example.com/asset.tar.gz"}], "metadata": {"name": "check_script", "namespace": "default"}}` |

### Authors

- Cameron Hurst (@wakemaster39)
- Aljaz Kosir (@aljazkosir)
- Manca Bizjak (@mancabizjak)
- Miha Plesko (@miha-plesko)
- Tadej Borovsak (@tadeboro)

### Collection links

[Issue Tracker](https://github.com/sensu/sensu-go-ansible/issues)
[Repository (Sources)](https://github.com/sensu/sensu-go-ansible)
