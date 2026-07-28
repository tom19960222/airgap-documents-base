---
collection: ansible
version: "8"
title: "community.zabbix.zabbix_host module – Create/update/delete Zabbix hosts"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/zabbix/zabbix_host_module.html
fetched_at: 2026-07-28T02:02:44+00:00
---
# community.zabbix.zabbix_host module – Create/update/delete Zabbix hosts

> **Note:**
>
> This module is part of the [community.zabbix collection](https://galaxy.ansible.com/ui/repo/published/community/zabbix/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.zabbix`.
> You need further requirements to be able to use this module,
> see [Requirements](zabbix_host_module.md#ansible-collections-community-zabbix-zabbix-host-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_host`.

- [Synopsis](zabbix_host_module.md#synopsis)
- [Requirements](zabbix_host_module.md#requirements)
- [Parameters](zabbix_host_module.md#parameters)
- [Examples](zabbix_host_module.md#examples)

## [Synopsis](zabbix_host_module.md#id1)

- This module allows you to create, modify and delete Zabbix host entries and associated group and template data.

## [Requirements](zabbix_host_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.9

## [Parameters](zabbix_host_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_cert**  aliases: tls_issuer  string | Required certificate issuer. |
| **description**  string | Description of the host in Zabbix. |
| **force**  boolean | Overwrite the host configuration, even if already present.  **Choices:**   - `false` - `true` ← (default) |
| **host_groups**  list / elements=string | List of host groups the host is part of.  Make sure the Zabbix user used for Ansible can read these groups. |
| **host_name**  string / required | Name of the host in Zabbix.  *host_name* is the unique identifier used and cannot be updated using this module. |
| **http_login_password**  string | Basic Auth password |
| **http_login_user**  string | Basic Auth login |
| **interfaces**  list / elements=dictionary | List of interfaces to be created for the host (see example below).  For more information, review host interface documentation at  <https://www.zabbix.com/documentation/current/en/manual/api/reference/hostinterface/object#host-interface>  **Default:** `[]` |
| **details**  dictionary | Additional details for SNMP host interfaces.  Required when *type=”snmp”*.  **Default:** `{}` |
| **authpassphrase**  string | SNMPv3 authentication passphrase.  Used when *securitylevel=1*(authNoPriv) or *securitylevel=2*(AuthPriv).  **Default:** `""` |
| **authprotocol**  integer | SNMPv3 authentication protocol.  Used when *securitylevel=1*(authNoPriv) or *securitylevel=2*(AuthPriv).  Variants 2,3,4,5 are supported only on Zabbix 5.4 or greater  0 (MD5), 1 (SHA1), 2 (SHA224), 3 (SHA256), 4 (SHA384), 5 (SHA512)  **Choices:**   - `0` ← (default) - `1` - `2` - `3` - `4` - `5` |
| **bulk**  integer | Whether to use bulk SNMP requests.  0 (don’t use bulk requests), 1 (use bulk requests)  **Choices:**   - `0` - `1` ← (default) |
| **community**  string | SNMPv1 and SNMPv2 community string.  Required when *version=1* or *version=2*.  **Default:** `""` |
| **contextname**  string | SNMPv3 context name.  **Default:** `""` |
| **privpassphrase**  string | SNMPv3 privacy passphrase.  Used when *securitylevel=2*(AuthPriv).  **Default:** `""` |
| **privprotocol**  integer | SNMPv3 privacy protocol.  Used when *securitylevel=2*(authPriv).  Variants 2,3,4,5 are supported only on Zabbix 5.4 or greater  0 (DES), 1 (AES128), 2 (AES192), 3 (AES256), 4 (AES192C), 5 (AES256C)  **Choices:**   - `0` ← (default) - `1` - `2` - `3` - `4` - `5` |
| **securitylevel**  integer | SNMPv3 security level.  0 (noAuthNoPriv), 1 (authNoPriv), 2 (authPriv).  **Choices:**   - `0` ← (default) - `1` - `2` |
| **securityname**  string | SNMPv3 security name.  **Default:** `""` |
| **version**  integer | SNMP version.  1 (SNMPv1), 2 (SNMPv2c), 3 (SNMPv3)  **Choices:**   - `1` - `2` ← (default) - `3` |
| **dns**  string | DNS name of the host interface.  Required if *useip=0*. |
| **ip**  string | IP address used by host interface.  Required if *useip=1*. |
| **main**  integer | Whether the interface is used as default.  If multiple interfaces with the same type are provided, only one can be default.  0 (not default), 1 (default)  **Choices:**   - `0` ← (default) - `1` |
| **port**  string | Port used by host interface.  If not specified, default port for each type of interface is used  10050 if *type=”agent”*  161 if *type=”snmp”*  623 if *type=”ipmi”*  12345 if *type=”jmx”* |
| **type**  string / required | Interface type to add  Numerical values are also accepted for interface type  1 = agent  2 = snmp  3 = ipmi  4 = jmx  **Choices:**   - `"agent"` - `"1"` - `"snmp"` - `"2"` - `"ipmi"` - `"3"` - `"jmx"` - `"4"` |
| **useip**  integer | Connect to host interface with IP address instead of DNS name.  0 (don’t use ip), 1 (use ip)  **Choices:**   - `0` ← (default) - `1` |
| **inventory_mode**  string | Configure the inventory mode.  **Choices:**   - `"automatic"` - `"manual"` - `"disabled"` |
| **inventory_zabbix**  dictionary | Add Facts for a zabbix inventory (e.g. Tag) (see example below).  Please review the interface documentation for more information on the supported properties  <https://www.zabbix.com/documentation/current/en/manual/api/reference/host/object#host-inventory> |
| **ipmi_authtype**  integer | IPMI authentication algorithm.  Please review the Host object documentation for more information on the supported properties  <https://www.zabbix.com/documentation/3.4/manual/api/reference/host/object>  Possible values are, `0` (none), `1` (MD2), `2` (MD5), `4` (straight), `5` (OEM), `6` (RMCP+), with -1 being the API default.  Please note that the Zabbix API will treat absent settings as default when updating any of the *ipmi_*-options; this means that if you attempt to set any of the four options individually, the rest will be reset to default values. |
| **ipmi_password**  string | IPMI password.  also see the last note in the *ipmi_authtype* documentation |
| **ipmi_privilege**  integer | IPMI privilege level.  Please review the Host object documentation for more information on the supported properties  <https://www.zabbix.com/documentation/3.4/manual/api/reference/host/object>  Possible values are `1` (callback), `2` (user), `3` (operator), `4` (admin), `5` (OEM), with `2` being the API default.  also see the last note in the *ipmi_authtype* documentation |
| **ipmi_username**  string | IPMI username.  also see the last note in the *ipmi_authtype* documentation |
| **link_templates**  list / elements=string | List of templates linked to the host. |
| **macros**  aliases: user_macros  list / elements=dictionary | List of user macros to assign to the zabbix host.  Providing *macros=[]* with *force=yes* will clean all of the existing user macros from the host. |
| **description**  string | Description of the user macro.  **Default:** `""` |
| **macro**  string / required | Name of the user macro.  Can be in zabbix native format “{$MACRO}” or short format “MACRO”. |
| **type**  string | Type of the macro.  Since value is not returned by API for secret macros, there is no reliable way to detect changes in the content of secret macro value.  To update secret macro value, please update description alongside it so it passes the check.  **Choices:**   - `"text"` ← (default) - `"secret"` |
| **value**  string / required | Value of the user macro. |
| **proxy**  string | The name of the Zabbix proxy to be used. |
| **state**  string | State of the host.  On `present`, it will create if host does not exist or update the host if the associated data is different.  On `absent` will remove a host if it exists.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **status**  string | Monitoring status of the host.  **Choices:**   - `"enabled"` ← (default) - `"disabled"` |
| **tags**  aliases: host_tags  list / elements=dictionary | List of host tags to assign to the zabbix host.  Providing *tags=[]* with *force=yes* will clean all of the tags from the host. |
| **tag**  string / required | Name of the host tag. |
| **value**  string | Value of the host tag.  **Default:** `""` |
| **tls_accept**  integer | Specifies what types of connections are allowed for incoming connections.  The tls_accept parameter accepts values of 1 to 7  Possible values, 1 (no encryption), 2 (PSK), 4 (certificate).  Values can be combined. |
| **tls_connect**  integer | Specifies what encryption to use for outgoing connections.  Possible values, 1 (no encryption), 2 (PSK), 4 (certificate). |
| **tls_psk**  string | PSK value is a hard to guess string of hexadecimal digits.  The preshared key, at least 32 hex digits. Required if either *tls_connect* or *tls_accept* has PSK enabled.  Using this parameter makes this module non-idempotent. |
| **tls_psk_identity**  string | It is a unique name by which this specific PSK is referred to by Zabbix components  Do not put sensitive information in the PSK identity string, it is transmitted over the network unencrypted.  Works only with >= Zabbix 3.0  Using this parameter with Zabbix >= 5.4 makes this module non-idempotent. |
| **tls_subject**  string | Required certificate subject. |
| **visible_name**  string | Visible name of the host in Zabbix. |

## [Examples](zabbix_host_module.md#id4)

```yaml+jinja
# If you want to use Username and Password to be authenticated by Zabbix Server
- name: Set credentials to access Zabbix Server API
  ansible.builtin.set_fact:
    ansible_user: Admin
    ansible_httpapi_pass: zabbix

# If you want to use API token to be authenticated by Zabbix Server
# https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/administration/general#api-tokens
- name: Set API token
  ansible.builtin.set_fact:
    ansible_zabbix_auth_key: 8ec0d52432c15c91fcafe9888500cf9a607f44091ab554dbee860f6b44fac895

- name: Create a new host or rewrite an existing host's info
# Set task level following variables for Zabbix Server host in task
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
  become: false
  delegate_to: zabbix-example-fqdn.org# you can use delegate_to or task level ansible_host like next example
  community.zabbix.zabbix_host:
    host_name: ExampleHost
    visible_name: ExampleName
    description: My ExampleHost Description
    host_groups:
      - Example group1
      - Example group2
    link_templates:
      - Example template1
      - Example template2
    status: enabled
    state: present
    inventory_mode: manual
    inventory_zabbix:
      tag: "{{ your_tag }}"
      alias: "{{ your_alias }}"
      notes: "Special Informations: {{ your_informations | default('None') }}"
      location: "{{ your_location }}"
      site_rack: "{{ your_site_rack }}"
      os: "{{ your_os }}"
      hardware: "{{ your_hardware }}"
    ipmi_authtype: 2
    ipmi_privilege: 4
    ipmi_username: username
    ipmi_password: password
    interfaces:
      - type: 1
        main: 1
        useip: 1
        ip: 10.xx.xx.xx
        dns: ""
        port: "10050"
      - type: 4
        main: 1
        useip: 1
        ip: 10.xx.xx.xx
        dns: ""
        port: "12345"
    proxy: a.zabbix.proxy
    macros:
      - macro: "{$EXAMPLEMACRO}"
        value: ExampleMacroValue
      - macro: EXAMPLEMACRO2
        value: ExampleMacroValue2
        description: Example desc that work only with Zabbix 4.4 and higher
    tags:
      - tag: ExampleHostsTag
      - tag: ExampleHostsTag2
        value: ExampleTagValue

- name: Update an existing host's TLS settings
# Set current task level variables for Zabbix Server host in task
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org # you can use task level ansible_host or delegate_to like in previous example
  become: false
  community.zabbix.zabbix_host:
    host_name: ExampleHost
    visible_name: ExampleName
    host_groups:
      - Example group1
    tls_psk_identity: test
    tls_connect: 2
    tls_psk: 123456789abcdef123456789abcdef12
    force: false
```

### Authors

- Cove (@cove)
- Tony Minfei Ding
- Harrison Gu (@harrisongu)
- Werner Dijkerman (@dj-wasabi)
- Eike Frost (@eikef)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
- [Homepage](https://github.com/ansible-collections/community.zabbix)
- [Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
