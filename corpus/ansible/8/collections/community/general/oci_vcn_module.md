---
collection: ansible
version: "8"
title: "community.general.oci_vcn module – Manage Virtual Cloud Networks(VCN) in OCI"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/oci_vcn_module.html
fetched_at: 2026-07-28T01:48:15+00:00
---
# community.general.oci_vcn module – Manage Virtual Cloud Networks(VCN) in OCI

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
> see [Requirements](oci_vcn_module.md#ansible-collections-community-general-oci-vcn-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.oci_vcn`.

- [Synopsis](oci_vcn_module.md#synopsis)
- [Requirements](oci_vcn_module.md#requirements)
- [Parameters](oci_vcn_module.md#parameters)
- [Attributes](oci_vcn_module.md#attributes)
- [Notes](oci_vcn_module.md#notes)
- [Examples](oci_vcn_module.md#examples)
- [Return Values](oci_vcn_module.md#return-values)

## [Synopsis](oci_vcn_module.md#id1)

- This module allows the user to create, delete and update virtual cloud networks(VCNs) in OCI. The complete Oracle Cloud Infrastructure Ansible Modules can be downloaded from <https://github.com/oracle/oci-ansible-modules/releases>.

Aliases: cloud.oracle.oci_vcn

## [Requirements](oci_vcn_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- Python SDK for Oracle Cloud Infrastructure <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io>

## [Parameters](oci_vcn_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_user**  string | The OCID of the user, on whose behalf, OCI APIs are invoked. If not set, then the value of the `OCI_USER_OCID` environment variable, if any, is used. This option is required if the user is not specified through a configuration file (See `config_file_location`). To get the user’s OCID, please refer <https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm>. |
| **api_user_fingerprint**  string | Fingerprint for the key pair being used. If not set, then the value of the `OCI_USER_FINGERPRINT` environment variable, if any, is used. This option is required if the key fingerprint is not specified through a configuration file (See `config_file_location`). To get the key pair’s fingerprint value please refer <https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm>. |
| **api_user_key_file**  path | Full path and filename of the private key (in PEM format). If not set, then the value of the OCI_USER_KEY_FILE variable, if any, is used. This option is required if the private key is not specified through a configuration file (See `config_file_location`). If the key is encrypted with a pass-phrase, the `api_user_key_pass_phrase` option must also be provided. |
| **api_user_key_pass_phrase**  string | Passphrase used by the key referenced in `api_user_key_file`, if it is encrypted. If not set, then the value of the OCI_USER_KEY_PASS_PHRASE variable, if any, is used. This option is required if the key passphrase is not specified through a configuration file (See `config_file_location`). |
| **auth_type**  string | The type of authentication to use for making API requests. By default `auth_type=api_key` based authentication is performed and the API key (see `api_user_key_file`) in your config file will be used. If this ‘auth_type’ module option is not specified, the value of the OCI_ANSIBLE_AUTH_TYPE, if any, is used. Use `auth_type=instance_principal` to use instance principal based authentication when running ansible playbooks within an OCI compute instance.  **Choices:**   - `"api_key"` ← (default) - `"instance_principal"` |
| **cidr_block**  string | The CIDR IP address block of the VCN. Required when creating a VCN with `state=present`. |
| **compartment_id**  string | The OCID of the compartment to contain the VCN. Required when creating a VCN with `state=present`. This option is mutually exclusive with `vcn_id`. |
| **config_file_location**  string | Path to configuration file. If not set then the value of the `OCI_CONFIG_FILE` environment variable, if any, is used. Otherwise, defaults to ~/.oci/config. |
| **config_profile_name**  string | The profile to load from the config file referenced by `config_file_location`. If not set, then the value of the `OCI_CONFIG_PROFILE` environment variable, if any, is used. Otherwise, defaults to the “DEFAULT” profile in `config_file_location`.  **Default:** `"DEFAULT"` |
| **defined_tags**  dictionary | Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see <https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm>. |
| **display_name**  aliases: name  string | A user-friendly name. Does not have to be unique, and it’s changeable. |
| **dns_label**  string | A DNS label for the VCN, used in conjunction with the VNIC’s hostname and subnet’s DNS label to form a fully qualified domain name (FQDN) for each VNIC within this subnet (for example, bminstance-1.subnet123.vcn1.oraclevcn.com). Not required to be unique, but it’s a best practice to set unique DNS labels for VCNs in your tenancy. Must be an alphanumeric string that begins with a letter. The value cannot be changed. |
| **force_create**  boolean | Whether to attempt non-idempotent creation of a resource. By default, create resource is an idempotent operation, and doesn’t create the resource if it already exists. Setting this option to true, forcefully creates a copy of the resource, even if it already exists.This option is mutually exclusive with `key_by`.  **Choices:**   - `false` ← (default) - `true` |
| **freeform_tags**  dictionary | Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see <https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm>. |
| **key_by**  list / elements=string | The list of comma-separated attributes of this resource which should be used to uniquely identify an instance of the resource. By default, all the attributes of a resource except `freeform_tags` are used to uniquely identify a resource. |
| **region**  string | The Oracle Cloud Infrastructure region to use for all OCI API requests. If not set, then the value of the OCI_REGION variable, if any, is used. This option is required if the region is not specified through a configuration file (See `config_file_location`). Please refer to <https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm> for more information on OCI regions. |
| **state**  string | Create or update a VCN with `state=present`. Use `state=absent` to delete a VCN.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tenancy**  string | OCID of your tenancy. If not set, then the value of the OCI_TENANCY variable, if any, is used. This option is required if the tenancy OCID is not specified through a configuration file (See `config_file_location`). To get the tenancy OCID, please refer <https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm> |
| **vcn_id**  aliases: id  string | The OCID of the VCN. Required when deleting a VCN with `state=absent` or updating a VCN with `state=present`. This option is mutually exclusive with `compartment_id`. |
| **wait**  boolean | Whether to wait for create or delete operation to complete.  **Choices:**   - `false` - `true` ← (default) |
| **wait_timeout**  integer | Time, in seconds, to wait when `wait=true`.  **Default:** `1200` |
| **wait_until**  string | The lifecycle state to wait for the resource to transition into when `wait=true`. By default, when `wait=true`, we wait for the resource to get into ACTIVE/ATTACHED/AVAILABLE/PROVISIONED/ RUNNING applicable lifecycle state during create operation & to get into DELETED/DETACHED/ TERMINATED lifecycle state during delete operation. |

## [Attributes](oci_vcn_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](oci_vcn_module.md#id5)

> **Note:**
>
> - For OCI python sdk configuration, please refer to <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/configuration.html>

## [Examples](oci_vcn_module.md#id6)

```yaml+jinja
- name: Create a VCN
  community.general.oci_vcn:
    cidr_block: '10.0.0.0/16'
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'
    display_name: my_vcn
    dns_label: ansiblevcn

- name: Updates the specified VCN's display name
  community.general.oci_vcn:
    vcn_id: ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx
    display_name: ansible_vcn

- name: Delete the specified VCN
  community.general.oci_vcn:
    vcn_id: ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx
    state: absent
```

## [Return Values](oci_vcn_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vcn**  dictionary | Information about the VCN  **Returned:** On successful create and update operation  **Sample:** `{"cidr_block": "10.0.0.0/16", "compartment_id\"": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx", "default_dhcp_options_id": "ocid1.dhcpoptions.oc1.phx.xxxxxEXAMPLExxxxx", "default_route_table_id": "ocid1.routetable.oc1.phx.xxxxxEXAMPLExxxxx", "default_security_list_id": "ocid1.securitylist.oc1.phx.xxxxxEXAMPLExxxxx", "display_name": "ansible_vcn", "dns_label": "ansiblevcn", "id": "ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx", "lifecycle_state": "AVAILABLE", "time_created": "2017-11-13T20:22:40.626000+00:00", "vcn_domain_name": "ansiblevcn.oraclevcn.com"}` |

### Authors

- Rohit Chaware (@rohitChaware)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
