---
collection: ansible
version: "8"
title: "community.windows.laps_password lookup – Retrieves the LAPS password for a server."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/laps_password_lookup.html
fetched_at: 2026-07-28T02:02:37+00:00
---
# community.windows.laps_password lookup – Retrieves the LAPS password for a server.

> **Note:**
>
> This lookup plugin is part of the [community.windows collection](https://galaxy.ansible.com/ui/repo/published/community/windows/) (version 1.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](laps_password_lookup.md#ansible-collections-community-windows-laps-password-lookup-requirements) for details.
>
> To use it in a playbook, specify: `community.windows.laps_password`.

- [Synopsis](laps_password_lookup.md#synopsis)
- [Requirements](laps_password_lookup.md#requirements)
- [Terms](laps_password_lookup.md#terms)
- [Keyword parameters](laps_password_lookup.md#keyword-parameters)
- [Notes](laps_password_lookup.md#notes)
- [Examples](laps_password_lookup.md#examples)
- [Return Value](laps_password_lookup.md#return-value)

## [Synopsis](laps_password_lookup.md#id1)

- This lookup returns the LAPS password set for a server from the Active Directory database.
- See <https://github.com/jborean93/ansible-lookup-laps_password> for more information around installing pre-requisites and testing.

## [Requirements](laps_password_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- python-ldap

## [Terms](laps_password_lookup.md#id3)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | The host name to retrieve the LAPS password for.  This is the `Common Name (CN`) of the host. |

## [Keyword parameters](laps_password_lookup.md#id4)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.windows.laps_password', key1=value1, key2=value2, ...)` and `query('community.windows.laps_password', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **allow_plaintext**  boolean | When set to `yes`, will allow traffic to be sent unencrypted.  It is highly recommended to not touch this to avoid any credentials being exposed over the network.  Use `scheme=ldaps`, `auth=gssapi`, or `start_tls=yes` to ensure the traffic is encrypted.  **Choices:**   - `false` ← (default) - `true` |
| **auth**  string | The type of authentication to use when connecting to the Active Directory server  When using `simple`, the *username* and *password* options must be set. If not using `scheme=ldaps` or `start_tls=True` then these credentials are exposed in plaintext in the network traffic.  It is recommended ot use `gssapi` as it will encrypt the traffic automatically.  When using `gssapi`, run `kinit` before running Ansible to get a valid Kerberos ticket.  You cannot use `gssapi` when either `scheme=ldaps` or `start_tls=True` is set.  **Choices:**   - `"simple"` - `"gssapi"` ← (default) |
| **ca_cert**  aliases: cacert_file  string | The path to a CA certificate PEM file to use for certificate validation.  Certificate validation is used when `scheme=ldaps` or `start_tls=yes`.  This may fail on hosts with an older OpenLDAP install like MacOS, this will have to be updated before reinstalling python-ldap to get working again. |
| **domain**  string / required | The domain to search in to retrieve the LAPS password.  This could either be a Windows domain name visible to the Ansible controller from DNS or a specific domain controller FQDN.  Supports either just the domain/host name or an explicit LDAP URI with the domain/host already filled in.  If the URI is set, *port* and *scheme* are ignored. |
| **password**  string | The password for `username`.  Required when `username` is set. |
| **port**  integer | The LDAP port to communicate over.  If *kdc* is already an LDAP URI then this is ignored. |
| **scheme**  string | The LDAP scheme to use.  When using `ldap`, it is recommended to set `auth=gssapi`, or `start_tls=yes`, otherwise traffic will be in plaintext.  The Active Directory host must be configured for `ldaps` with a certificate before it can be used.  If *kdc* is already an LDAP URI then this is ignored.  **Choices:**   - `"ldap"` ← (default) - `"ldaps"` |
| **search_base**  string | Changes the search base used when searching for the host in Active Directory.  Will default to search in the `defaultNamingContext` of the Active Directory server.  If multiple matches are found then a more explicit search_base is required so only 1 host is found.  If searching a larger Active Directory database, it is recommended to narrow the search_base for performance reasons. |
| **start_tls**  boolean | When `scheme=ldap`, will use the StartTLS extension to encrypt traffic sent over the wire.  This requires the Active Directory to be set up with a certificate that supports StartTLS.  This is ignored when `scheme=ldaps` as the traffic is already encrypted.  **Choices:**   - `false` ← (default) - `true` |
| **username**  string | Required when using `auth=simple`.  The username to authenticate with.  Recommended to use the username in the UPN format, e.g. `username@DOMAIN.COM`.  This is required when `auth=simple` and is not supported when `auth=gssapi`.  Call `kinit` outside of Ansible if `auth=gssapi` is required. |
| **validate_certs**  string | When using `scheme=ldaps` or `start_tls=yes`, this controls the certificate validation behaviour.  `demand` will fail if no certificate or an invalid certificate is provided.  `try` will fail for invalid certificates but will continue if no certificate is provided.  `allow` will request and check a certificate but will continue even if it is invalid.  `never` will not request a certificate from the server so no validation occurs.  **Choices:**   - `"never"` - `"allow"` - `"try"` - `"demand"` ← (default) |

## [Notes](laps_password_lookup.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('community.windows.laps_password', term1, term2, key1=value1, key2=value2)` and `query('community.windows.laps_password', term1, term2, key1=value1, key2=value2)`
> - If a host was found but had no LAPS password attribute `ms-Mcs-AdmPwd`, the lookup will fail.
> - Due to the sensitive nature of the data travelling across the network, it is highly recommended to run with either `auth=gssapi`, `scheme=ldaps`, or `start_tls=yes`.
> - Failing to run with one of the above settings will result in the account credentials as well as the LAPS password to be sent in plaintext.
> - Some scenarios may not work when running on a host with an older OpenLDAP install like MacOS. It is recommended to install the latest OpenLDAP version and build python-ldap against this, see <https://keathmilligan.net/python-ldap-and-macos> for more information.

## [Examples](laps_password_lookup.md#id6)

```yaml+jinja
# This isn't mandatory but it is a way to call kinit from within Ansible before calling the lookup
- name: call kinit to retrieve Kerberos token
  expect:
    command: kinit username@ANSIBLE.COM
    responses:
      (?i)password: SecretPass1
  no_log: True

- name: Get the LAPS password using Kerberos auth, relies on kinit already being called
  set_fact:
    ansible_password: "{{ lookup('community.windows.laps_password', 'SERVER', domain='dc01.ansible.com') }}"

- name: Specific the domain host using an explicit LDAP URI
  set_fact:
    ansible_password: "{{ lookup('community.windows.laps_password', 'SERVER', domain='ldap://ansible.com:389') }}"

- name: Use Simple auth over LDAPS
  set_fact:
    ansible_password: "{{ lookup('community.windows.laps_password', 'server',
                                 domain='dc01.ansible.com',
                                 auth='simple',
                                 scheme='ldaps',
                                 username='username@ANSIBLE.COM',
                                 password='SuperSecret123') }}"

- name: Use Simple auth with LDAP and StartTLS
  set_fact:
    ansible_password: "{{ lookup('community.windows.laps_password', 'app01',
                                 domain='dc01.ansible.com',
                                 auth='simple',
                                 start_tls=True,
                                 username='username@ANSIBLE.COM',
                                 password='SuperSecret123') }}"

- name: Narrow down the search base to a an OU
  set_fact:
    ansible_password: "{{ lookup('community.windows.laps_password', 'sql10',
                                 domain='dc01.ansible.com',
                                 search_base='OU=Databases,DC=ansible,DC=com') }}"

- name: Set certificate file to use when validating the TLS certificate
  set_fact:
    ansible_password: "{{ lookup('community.windows.laps_password', 'windows-pc',
                                 domain='dc01.ansible.com',
                                 start_tls=True,
                                 ca_cert='/usr/local/share/certs/ad.pem') }}"
```

## [Return Value](laps_password_lookup.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  string | The LAPS password(s) for the host(s) requested.  **Returned:** success |

### Authors

- Jordan Borean (@jborean93)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
