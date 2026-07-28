---
collection: ansible
version: "8"
title: "microsoft.ad.debug_ldap_client module – Get host information for debugging LDAP connections"
source_url: https://docs.ansible.com/projects/ansible/8/collections/microsoft/ad/debug_ldap_client_module.html
fetched_at: 2026-07-28T02:40:48+00:00
---
# microsoft.ad.debug_ldap_client module – Get host information for debugging LDAP connections

> **Note:**
>
> This module is part of the [microsoft.ad collection](https://galaxy.ansible.com/ui/repo/published/microsoft/ad/) (version 1.4.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install microsoft.ad`.
>
> To use it in a playbook, specify: `microsoft.ad.debug_ldap_client`.

New in microsoft.ad 1.1.0

- [Synopsis](debug_ldap_client_module.md#synopsis)
- [Attributes](debug_ldap_client_module.md#attributes)
- [Notes](debug_ldap_client_module.md#notes)
- [Examples](debug_ldap_client_module.md#examples)
- [Return Values](debug_ldap_client_module.md#return-values)

## [Synopsis](debug_ldap_client_module.md#id1)

- Get information about the current Ansible host to debug LDAP connections and their capabilities.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Attributes](debug_ldap_client_module.md#id2)

| Attribute | Support | Description |
| --- | --- | --- |
| **action** | **Support:** **full** | Indicates this has a corresponding action plugin so some parts of the options can be executed on the controller |
| **async** | **Support:** **full** | Supports being used with the `async` keyword |
| **bypass_host_loop** | **Support:** **none** | Forces a ‘global’ task that does not execute per host, this bypasses per host templating and serial, throttle and other loop considerations  Conditionals will work as if `run_once` is being used, variables used will be from the first available host  This action will not work normally outside of lockstep strategies |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platform:** **posix** | Target OS/families that can be operated against |

## [Notes](debug_ldap_client_module.md#id3)

> **Note:**
>
> - See [LDAP connection help](docsite/guide_ldap_connection.md#ansible-collections-microsoft-ad-docsite-guide-ldap-connection) for more information about LDAP connections.
> - The return values are not part of any contract and can change in the future. It is meant to give a snapshot of the Ansible host that can help debug LDAP connection issues and not be used as part of a normal playbook.

## [Examples](debug_ldap_client_module.md#id4)

```yaml+jinja
- name: Get information about the Ansible host's LDAP capabilities
  microsoft.ad.debug_ldap_client:
```

## [Return Values](debug_ldap_client_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dns**  complex | Details about the SRV LDAP server lookup.  The values will only be populated if dnspython is installed.  **Returned:** always |
| **default_port**  integer | The default port of the SRV record chosen.  **Returned:** dnspython is installed  **Sample:** `389` |
| **default_server**  string | The default hostname of the SRV record chosen.  **Returned:** dnspython is installed  **Sample:** `"dc01.domain.com"` |
| **exception**  string | Any exceptions that occurred when getting the SRV records.  **Returned:** dnspython is installed  **Sample:** `""` |
| **records**  list / elements=string | The SRV records that were found during the LDAP server lookup.  **Returned:** dnspython is installed |
| **port**  integer | The port of this SRV record.  **Returned:** dnspython is installed and default_realm is found  **Sample:** `389` |
| **priority**  integer | The record priority value.  **Returned:** dnspython is installed and default_realm is found  **Sample:** `0` |
| **target**  string | The target name of the SRV record.  **Returned:** dnspython is installed and default_realm is found  **Sample:** `"dc01.domain.com."` |
| **weight**  integer | The record weight value.  **Returned:** dnspython is installed and default_realm is found  **Sample:** `100` |
| **kerberos**  complex | Details about the host Kerberos setup.  The values will only be populated if krb5 is installed.  **Returned:** always |
| **default_cc**  complex | Details about the default Kerberos credential cache.  **Returned:** krb5 is installed |
| **creds**  complex | A list of credentials that is stored in the ccache.  This requires `krb5 >= 0.5.0` to be populated.  **Returned:** krb5 is installed |
| **client**  string | The client principal name the credential is for.  **Returned:** krb5 >= 0.5.0 is installed  **Sample:** `"username@DOMAIN.COM"` |
| **server**  string | The server principal name the credential is for.  **Returned:** krb5 >= 0.5.0 is installed  **Sample:** `"krbtgt/DOMAIN.COM@DOMAIN.COM"` |
| **exception**  string | Any exceptions that occurred when getting the ccache information.  **Returned:** krb5 is installed  **Sample:** `""` |
| **name**  string | The default ccache type and name.  **Returned:** krb5 is installed  **Sample:** `"FILE:/tmp/krb5cc_1000"` |
| **principal**  string | The default principal of the ccache  **Returned:** krb5 is installed  **Sample:** `"username@DOMAIN.COM"` |
| **default_realm**  string | The default_realm as reported by Kerberos.  This value is used for the automatic server lookup.  **Returned:** krb5 is installed  **Sample:** `"domain.com"` |
| **exception**  string | Exception details if the default realm could not be retrieved.  **Returned:** krb5 is installed  **Sample:** `""` |
| **packages**  complex | All the packages used by this collection for LDAP connections and their installed versions.  If the package is not installed, or failed to import, the value is the traceback from the import process.  This can be used to determine the availability of optional features like Kerberos authentication or server lookups.  **Returned:** always |
| **dnspython**  string | The installed version of `dnspython` or the import error if not installed.  **Returned:** always  **Sample:** `"2.3.0"` |
| **dpapi_ng**  string | The installed version of `dpapi-ng` or the import error if not installed.  **Returned:** always  **Sample:** `"0.1.0"` |
| **krb5**  string | The installed version of `krb5` or the import error if not installed.  **Returned:** always  **Sample:** `"0.5.0"` |
| **pyspnego**  string | The installed version of `pyspnego` or the import error if not installed.  **Returned:** always  **Sample:** `"0.8.0"` |
| **sansldap**  string | The installed version of `sansldap` or the import error if not installed.  **Returned:** always  **Sample:** `"0.1.0"` |

### Authors

- Jordan Borean (@jborean93)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/microsoft.ad/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/microsoft.ad)
- [Report an issue](https://github.com/ansible-collections/microsoft.ad/issues/new/choose)
- [Communication](index.md#communication-for-microsoft-ad)
