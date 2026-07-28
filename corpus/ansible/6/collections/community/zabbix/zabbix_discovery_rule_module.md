---
collection: ansible
version: "6"
title: "community.zabbix.zabbix_discovery_rule module – Create/delete/update Zabbix discovery rules"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/zabbix/zabbix_discovery_rule_module.html
fetched_at: 2026-07-27T17:24:09+00:00
---
# community.zabbix.zabbix_discovery_rule module – Create/delete/update Zabbix discovery rules

> **Note:**
>
> This module is part of the [community.zabbix collection](https://galaxy.ansible.com/community/zabbix) (version 1.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.zabbix`.
> You need further requirements to be able to use this module,
> see [Requirements](zabbix_discovery_rule_module.md#ansible-collections-community-zabbix-zabbix-discovery-rule-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_discovery_rule`.

- [Synopsis](zabbix_discovery_rule_module.md#synopsis)
- [Requirements](zabbix_discovery_rule_module.md#requirements)
- [Parameters](zabbix_discovery_rule_module.md#parameters)
- [Notes](zabbix_discovery_rule_module.md#notes)
- [Examples](zabbix_discovery_rule_module.md#examples)
- [Return Values](zabbix_discovery_rule_module.md#return-values)

## [Synopsis](zabbix_discovery_rule_module.md#id1)

- Create discovery rule.
- Delete existing discovery rule.
- Update existing discovery rule with new options.

## [Requirements](zabbix_discovery_rule_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](zabbix_discovery_rule_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dchecks**  aliases: dcheck  list / elements=dictionary | List of dictionaries of discovery check objects.  For more information, review discovery check object documentation at <https://www.zabbix.com/documentation/current/manual/api/reference/dcheck/object> |
| **host_source**  string | Source for host name.  Possible values:  DNS (default)  IP  discovery - discovery value of this check  Options is available since Zabbix 4.4  Choices:   - `"DNS"` ← (default) - `"IP"` - `"discovery"` |
| **key**  string | The value of this property differs depending on the type of the check:   - key to query for Zabbix agent checks - SNMP OID for SNMPv1, SNMPv2 and SNMPv3 checks |
| **name_source**  string | Source for visible name.  Possible values:  none - (default) not specified  DNS  IP  discovery - discovery value of this check  Options is available since Zabbix 4.4  Choices:   - `"None"` ← (default) - `"DNS"` - `"IP"` - `"discovery"` |
| **ports**  string | One or several port ranges to check separated by commas. Used for all checks except for ICMP. |
| **snmp_community**  string | SNMP community.  Required for SNMPv1 and SNMPv2 agent checks. |
| **snmpv3_authpassphrase**  string | Authentication passphrase used for SNMPv3 agent checks with security level set to authNoPriv or authPriv. |
| **snmpv3_authprotocol**  string | Authentication protocol used for SNMPv3 agent checks with security level set to authNoPriv or authPriv.  Possible values:  MD5  SHA  Choices:   - `"MD5"` - `"SHA"` |
| **snmpv3_contextname**  string | SNMPv3 context name. Used only by SNMPv3 checks. |
| **snmpv3_privpassphrase**  string | Privacy passphrase used for SNMPv3 agent checks with security level set to authPriv. |
| **snmpv3_privprotocol**  string | Privacy protocol used for SNMPv3 agent checks with security level set to authPriv.  Possible values:  DES  AES  Choices:   - `"DES"` - `"AES"` |
| **snmpv3_securitylevel**  string | Security level used for SNMPv3 agent checks.  Possible values:  noAuthNoPriv  authNoPriv  authPriv  Choices:   - `"noAuthNoPriv"` - `"authNoPriv"` - `"authPriv"` |
| **snmpv3_securityname**  string | Security name used for SNMPv3 agent checks. |
| **type**  string | Type of check.  Choices:   - `"SSH"` - `"LDAP"` - `"SMTP"` - `"FTP"` - `"HTTP"` - `"POP"` - `"NNTP"` - `"IMAP"` - `"TCP"` - `"Zabbix"` - `"SNMPv1"` - `"SNMPv2"` - `"ICMP"` - `"SNMPv3"` - `"HTTPS"` - `"Telnet"` |
| **uniq**  boolean | Whether to use this check as a device uniqueness criteria.  Only a single unique check can be configured for a discovery rule.  Used for Zabbix agent, SNMPv1, SNMPv2 and SNMPv3 agent checks.  Possible values:  no - (default) do not use this check as a uniqueness criteria  yes - use this check as a uniqueness criteria  Choices:   - `false` ← (default) - `true` |
| **delay**  string | Execution interval of the discovery rule.  Accepts seconds, time unit with suffix and user macro.  Default: `"1h"` |
| **iprange**  list / elements=string | One or several IP ranges to check separated by commas. |
| **login_password**  string | Zabbix user password.  If not set the environment variable `ZABBIX_PASSWORD` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **login_user**  string | Zabbix user name.  If not set the environment variable `ZABBIX_USERNAME` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **name**  string / required | Name of the discovery rule. |
| **proxy**  string | Name of the proxy used for discovery. |
| **server_url**  aliases: url  string | URL of Zabbix server, with protocol (http or https). `url` is an alias for `server_url`.  If not set the environment variable `ZABBIX_SERVER` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **state**  string | Create or delete discovery rules.  Choices:   - `"present"` ← (default) - `"absent"` |
| **status**  string | Whether the discovery rule is enabled.  Possible values:  enabled (default)  disabled  Choices:   - `"enabled"` ← (default) - `"disabled"` |
| **timeout**  integer | The timeout of API request (seconds).  This option is deprecated with the move to httpapi connection and will be removed in the next release  Default: `10` |
| **validate_certs**  boolean | If set to False, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If not set the environment variable `ZABBIX_VALIDATE_CERTS` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release  Choices:   - `false` - `true` ← (default) |

## [Notes](zabbix_discovery_rule_module.md#id4)

> **Note:**
>
> - Only Zabbix >= 4.0 is supported.
> - If you use *login_password=zabbix*, the word “zabbix” is replaced by “\*\*\*\*\*\*\*\*” in all module output, because *login_password* uses `no_log`. See [this FAQ](https://docs.ansible.com/ansible/latest/network/user_guide/faq.html#why-is-my-output-sometimes-replaced-with) for more information.

## [Examples](zabbix_discovery_rule_module.md#id5)

```yaml+jinja
# Set following variables for Zabbix Server host in play or inventory
- name: Set connection specific variables
  set_fact:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 80
    ansible_httpapi_use_ssl: false
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: 'zabbixeu'  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu

# If you want to use Username and Password to be authenticated by Zabbix Server
- name: Set credentials to access Zabbix Server API
  set_fact:
    ansible_user: Admin
    ansible_httpapi_pass: zabbix

# If you want to use API token to be authenticated by Zabbix Server
# https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/administration/general#api-tokens
- name: Set API token
  set_fact:
    ansible_zabbix_auth_key: 8ec0d52432c15c91fcafe9888500cf9a607f44091ab554dbee860f6b44fac895

# Base create discovery rule example
- name: Create discovery rule with ICMP and zabbix agent checks
  community.zabbix.zabbix_discovery_rule:
    name: ACME
    state: present
    iprange: 192.168.1.1-255
    dchecks:
        - type: ICMP
        - type: Zabbix
          key: "system.hostname"
          ports: 10050
          uniq: yes
          host_source: "discovery"

# Base update (add new dcheck) discovery rule example
- name: Create discovery rule with ICMP and zabbix agent checks
  community.zabbix.zabbix_discovery_rule:
    name: ACME
    state: present
    iprange: 192.168.1.1-255
    dchecks:
        - type: SNMPv3
          snmp_community: CUSTOMER@snmp3-readonly
          ports: "161"
          key: iso.3.6.1.2.1.1.1.0
          snmpv3_contextname: "ContextName"
          snmpv3_securityname: "SecurityName"
          snmpv3_securitylevel: "authPriv"
          snmpv3_authprotocol: "SHA"
          snmpv3_authpassphrase: "SeCrEt"
          snmpv3_privprotocol: "AES"
          snmpv3_privpassphrase: "TopSecret"
          uniq: no
          host_source: "DNS"
          name_source: "None"

# Base delete discovery rule example
- name: Delete discovery rule
  community.zabbix.zabbix_discovery_rule:
    name: ACME
    state: absent
```

## [Return Values](zabbix_discovery_rule_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **drule**  string | Discovery rule name.  Returned: on success  Sample: `"ACME"` |
| **druleid**  string | Discovery rule id.  Returned: on success  Sample: `"42"` |
| **msg**  string | The result of the operation  Returned: always  Sample: `"Discovery rule created: ACME, ID: 42"` |
| **state**  string | Discovery rule state at the end of execution.  Returned: on success  Sample: `"present"` |

### Authors

- Tobias Birkefeld (@tcraxs)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
[Homepage](https://github.com/ansible-collections/community.zabbix)
[Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
