---
collection: ansible
version: "8"
title: "community.general.imc_rest module – Manage Cisco IMC hardware through its REST API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/imc_rest_module.html
fetched_at: 2026-07-28T01:46:26+00:00
---
# community.general.imc_rest module – Manage Cisco IMC hardware through its REST API

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
> see [Requirements](imc_rest_module.md#ansible-collections-community-general-imc-rest-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.imc_rest`.

- [Synopsis](imc_rest_module.md#synopsis)
- [Requirements](imc_rest_module.md#requirements)
- [Parameters](imc_rest_module.md#parameters)
- [Attributes](imc_rest_module.md#attributes)
- [Notes](imc_rest_module.md#notes)
- [Examples](imc_rest_module.md#examples)
- [Return Values](imc_rest_module.md#return-values)

## [Synopsis](imc_rest_module.md#id1)

- Provides direct access to the Cisco IMC REST API.
- Perform any configuration changes and actions that the Cisco IMC supports.
- More information about the IMC REST API is available from <http://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/c/sw/api/3_0/b_Cisco_IMC_api_301.html>.

Aliases: remote_management.imc.imc_rest

## [Requirements](imc_rest_module.md#id2)

The below requirements are needed on the host that executes this module.

- lxml
- xmljson >= 0.1.8

## [Parameters](imc_rest_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **content**  string | When used instead of `path`, sets the content of the API requests directly.  This may be convenient to template simple requests, for anything complex use the [ansible.builtin.template](../../ansible/builtin/template_module.md#ansible-collections-ansible-builtin-template-module) module.  You can collate multiple IMC XML fragments and they will be processed sequentially in a single stream, the Cisco IMC output is subsequently merged.  Parameter `content` is mutual exclusive with parameter `path`. |
| **hostname**  aliases: host, ip  string / required | IP Address or hostname of Cisco IMC, resolvable by Ansible control host. |
| **password**  string | The password to use for authentication.  **Default:** `"password"` |
| **path**  aliases: src, config_file  path | Name of the absolute path of the filename that includes the body of the http request being sent to the Cisco IMC REST API.  Parameter `path` is mutual exclusive with parameter `content`. |
| **protocol**  string | Connection protocol to use.  **Choices:**   - `"http"` - `"https"` ← (default) |
| **timeout**  integer | The socket level timeout in seconds.  This is the time that every single connection (every fragment) can spend. If this `timeout` is reached, the module will fail with a `Connection failure` indicating that `The read operation timed out`.  **Default:** `60` |
| **username**  aliases: user  string | Username used to login to the switch.  **Default:** `"admin"` |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only set to `false` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](imc_rest_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](imc_rest_module.md#id5)

> **Note:**
>
> - The XML fragments don’t need an authentication cookie, this is injected by the module automatically.
> - The Cisco IMC XML output is being translated to JSON using the Cobra convention.
> - Any configConfMo change requested has a return status of ‘modified’, even if there was no actual change from the previous configuration. As a result, this module will always report a change on subsequent runs. In case this behaviour is fixed in a future update to Cisco IMC, this module will automatically adapt.
> - If you get a `Connection failure` related to `The read operation timed out` increase the `timeout` parameter. Some XML fragments can take longer than the default timeout.
> - More information about the IMC REST API is available from <http://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/c/sw/api/3_0/b_Cisco_IMC_api_301.html>

## [Examples](imc_rest_module.md#id6)

```yaml+jinja
- name: Power down server
  community.general.imc_rest:
    hostname: '{{ imc_hostname }}'
    username: '{{ imc_username }}'
    password: '{{ imc_password }}'
    validate_certs: false
    content: |
      <configConfMo><inConfig>
        <computeRackUnit dn="sys/rack-unit-1" adminPower="down"/>
      </inConfig></configConfMo>
  delegate_to: localhost

- name: Configure IMC using multiple XML fragments
  community.general.imc_rest:
    hostname: '{{ imc_hostname }}'
    username: '{{ imc_username }}'
    password: '{{ imc_password }}'
    validate_certs: false
    timeout: 120
    content: |
      <!-- Configure Serial-on-LAN -->
      <configConfMo><inConfig>
        <solIf dn="sys/rack-unit-1/sol-if" adminState="enable" speed=="115200" comport="com0"/>
      </inConfig></configConfMo>

      <!-- Configure Console Redirection -->
      <configConfMo><inConfig>
        <biosVfConsoleRedirection dn="sys/rack-unit-1/bios/bios-settings/Console-redirection"
          vpBaudRate="115200"
          vpConsoleRedirection="com-0"
          vpFlowControl="none"
          vpTerminalType="vt100"
          vpPuttyKeyPad="LINUX"
          vpRedirectionAfterPOST="Always Enable"/>
      </inConfig></configConfMo>
  delegate_to: localhost

- name: Enable PXE boot and power-cycle server
  community.general.imc_rest:
    hostname: '{{ imc_hostname }}'
    username: '{{ imc_username }}'
    password: '{{ imc_password }}'
    validate_certs: false
    content: |
      <!-- Configure PXE boot -->
      <configConfMo><inConfig>
        <lsbootLan dn="sys/rack-unit-1/boot-policy/lan-read-only" access="read-only" order="1" prot="pxe" type="lan"/>
      </inConfig></configConfMo>

      <!-- Power cycle server -->
      <configConfMo><inConfig>
        <computeRackUnit dn="sys/rack-unit-1" adminPower="cycle-immediate"/>
      </inConfig></configConfMo>
  delegate_to: localhost

- name: Reconfigure IMC to boot from storage
  community.general.imc_rest:
    hostname: '{{ imc_host }}'
    username: '{{ imc_username }}'
    password: '{{ imc_password }}'
    validate_certs: false
    content: |
      <configConfMo><inConfig>
        <lsbootStorage dn="sys/rack-unit-1/boot-policy/storage-read-write" access="read-write" order="1" type="storage"/>
      </inConfig></configConfMo>
  delegate_to: localhost

- name: Add customer description to server
  community.general.imc_rest:
    hostname: '{{ imc_host }}'
    username: '{{ imc_username }}'
    password: '{{ imc_password }}'
    validate_certs: false
    content: |
        <configConfMo><inConfig>
          <computeRackUnit dn="sys/rack-unit-1" usrLbl="Customer Lab - POD{{ pod_id }} - {{ inventory_hostname_short }}"/>
        </inConfig></configConfMo>
    delegate_to: localhost

- name: Disable HTTP and increase session timeout to max value 10800 secs
  community.general.imc_rest:
    hostname: '{{ imc_host }}'
    username: '{{ imc_username }}'
    password: '{{ imc_password }}'
    validate_certs: false
    timeout: 120
    content: |
        <configConfMo><inConfig>
          <commHttp dn="sys/svc-ext/http-svc" adminState="disabled"/>
        </inConfig></configConfMo>

        <configConfMo><inConfig>
          <commHttps dn="sys/svc-ext/https-svc" adminState="enabled" sessionTimeout="10800"/>
        </inConfig></configConfMo>
    delegate_to: localhost
```

## [Return Values](imc_rest_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **aaLogin**  dictionary | Cisco IMC XML output for the login, translated to JSON using Cobra convention  **Returned:** success  **Sample:** `"\"attributes\": {\n    \"cookie\": \"\",\n    \"outCookie\": \"1498902428/9de6dc36-417c-157c-106c-139efe2dc02a\",\n    \"outPriv\": \"admin\",\n    \"outRefreshPeriod\": \"600\",\n    \"outSessionId\": \"114\",\n    \"outVersion\": \"2.0(13e)\",\n    \"response\": \"yes\"\n}\n"` |
| **configConfMo**  dictionary | Cisco IMC XML output for any configConfMo XML fragments, translated to JSON using Cobra convention  **Returned:** success  **Sample:** `""` |
| **elapsed**  integer | Elapsed time in seconds  **Returned:** always  **Sample:** `31` |
| **error**  dictionary | Cisco IMC XML error output for last request, translated to JSON using Cobra convention  **Returned:** failed  **Sample:** `"\"attributes\": {\n    \"cookie\": \"\",\n    \"errorCode\": \"ERR-xml-parse-error\",\n    \"errorDescr\": \"XML PARSING ERROR: Element 'computeRackUnit', attribute 'admin_Power': The attribute 'admin_Power' is not allowed. \",\n    \"invocationResult\": \"594\",\n    \"response\": \"yes\"\n}\n"` |
| **error_code**  string | Cisco IMC error code  **Returned:** failed  **Sample:** `"ERR-xml-parse-error"` |
| **error_text**  string | Cisco IMC error message  **Returned:** failed  **Sample:** `"XML PARSING ERROR: Element 'computeRackUnit', attribute 'admin_Power': The attribute 'admin_Power' is not allowed.\n"` |
| **input**  string | RAW XML input sent to the Cisco IMC, causing the error  **Returned:** failed  **Sample:** `"<configConfMo><inConfig><computeRackUnit dn=\"sys/rack-unit-1\" admin_Power=\"down\"/></inConfig></configConfMo>\n"` |
| **output**  string | RAW XML output received from the Cisco IMC, with error details  **Returned:** failed  **Sample:** `"<error cookie=\"\"\n  response=\"yes\"\n  errorCode=\"ERR-xml-parse-error\"\n  invocationResult=\"594\"\n  errorDescr=\"XML PARSING ERROR: Element 'computeRackUnit', attribute 'admin_Power': The attribute 'admin_Power' is not allowed.\\n\"/>\n"` |
| **response**  string | HTTP response message, including content length  **Returned:** always  **Sample:** `"OK (729 bytes)"` |
| **status**  dictionary | The HTTP response status code  **Returned:** always  **Sample:** `200` |

### Authors

- Dag Wieers (@dagwieers)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
