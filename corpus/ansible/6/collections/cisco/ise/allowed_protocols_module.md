---
collection: ansible
version: "6"
title: "cisco.ise.allowed_protocols module – Resource module for Allowed Protocols"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ise/allowed_protocols_module.html
fetched_at: 2026-07-27T16:56:11+00:00
---
# cisco.ise.allowed_protocols module – Resource module for Allowed Protocols

> **Note:**
>
> This module is part of the [cisco.ise collection](https://galaxy.ansible.com/cisco/ise) (version 2.5.9).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ise`.
> You need further requirements to be able to use this module,
> see [Requirements](allowed_protocols_module.md#ansible-collections-cisco-ise-allowed-protocols-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.allowed_protocols`.

New in cisco.ise 1.0.0

- [Synopsis](allowed_protocols_module.md#synopsis)
- [Requirements](allowed_protocols_module.md#requirements)
- [Parameters](allowed_protocols_module.md#parameters)
- [Notes](allowed_protocols_module.md#notes)
- [Examples](allowed_protocols_module.md#examples)
- [Return Values](allowed_protocols_module.md#return-values)

## [Synopsis](allowed_protocols_module.md#id1)

- Manage operations create, update and delete of the resource Allowed Protocols.
- This API creates an allowed protocol.
- This API deletes an allowed protocol.
- This API allows the client to update an allowed protocol.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](allowed_protocols_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.0.8
- python >= 3.5

## [Parameters](allowed_protocols_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allowChap**  boolean | AllowChap flag.  Choices:   - `false` - `true` |
| **allowEapFast**  boolean | AllowEapFast flag.  Choices:   - `false` - `true` |
| **allowEapMd5**  boolean | AllowEapMd5 flag.  Choices:   - `false` - `true` |
| **allowEapTls**  boolean | AllowEapTls flag.  Choices:   - `false` - `true` |
| **allowEapTtls**  boolean | AllowEapTtls flag.  Choices:   - `false` - `true` |
| **allowLeap**  boolean | AllowLeap flag.  Choices:   - `false` - `true` |
| **allowMsChapV1**  boolean | AllowMsChapV1 flag.  Choices:   - `false` - `true` |
| **allowMsChapV2**  boolean | AllowMsChapV2 flag.  Choices:   - `false` - `true` |
| **allowPapAscii**  boolean | AllowPapAscii flag.  Choices:   - `false` - `true` |
| **allowPeap**  boolean | AllowPeap flag.  Choices:   - `false` - `true` |
| **allowPreferredEapProtocol**  boolean | AllowPreferredEapProtocol flag.  Choices:   - `false` - `true` |
| **allowTeap**  boolean | AllowTeap flag.  Choices:   - `false` - `true` |
| **allowWeakCiphersForEap**  boolean | AllowWeakCiphersForEap flag.  Choices:   - `false` - `true` |
| **description**  string | Allowed Protocols’s description. |
| **eapFast**  dictionary | The eapFast is required only if allowEapFast is true, otherwise it must be ignored. The object eapFast contains the settings for EAP FAST protocol. |
| **allowEapFastEapGtc**  boolean | AllowEapFastEapGtc flag.  Choices:   - `false` - `true` |
| **allowEapFastEapGtcPwdChange**  boolean | The allowEapFastEapGtcPwdChange is required only if allowEapFastEapGtc is true, otherwise it must be ignored.  Choices:   - `false` - `true` |
| **allowEapFastEapGtcPwdChangeRetries**  integer | The allowEapFastEapGtcPwdChangeRetries is required only if allowEapFastEapGtc is true, otherwise it must be ignored. Valid range is 0-3. |
| **allowEapFastEapMsChapV2**  boolean | AllowEapFastEapMsChapV2 flag.  Choices:   - `false` - `true` |
| **allowEapFastEapMsChapV2PwdChange**  boolean | The allowEapFastEapMsChapV2PwdChange is required only if allowEapFastEapMsChapV2 is true, otherwise it must be ignored.  Choices:   - `false` - `true` |
| **allowEapFastEapMsChapV2PwdChangeRetries**  integer | The allowEapFastEapMsChapV2PwdChangeRetries is required only if eapTtlsEapMsChapV2 is true, otherwise it must be ignored. Valid range is 0-3. |
| **allowEapFastEapTls**  boolean | AllowEapFastEapTls flag.  Choices:   - `false` - `true` |
| **allowEapFastEapTlsAuthOfExpiredCerts**  boolean | The allowEapFastEapTlsAuthOfExpiredCerts is required only if allowEapFastEapTls is true, otherwise it must be ignored.  Choices:   - `false` - `true` |
| **eapFastDontUsePacsAcceptClientCert**  boolean | The eapFastDontUsePacsAcceptClientCert is required only if eapFastUsePacs is FALSE, otherwise it must be ignored.  Choices:   - `false` - `true` |
| **eapFastDontUsePacsAllowMachineAuthentication**  boolean | The eapFastDontUsePacsAllowMachineAuthentication is required only if eapFastUsePacs is FALSE, otherwise it must be ignored.  Choices:   - `false` - `true` |
| **eapFastEnableEAPChaining**  boolean | EapFastEnableEAPChaining flag.  Choices:   - `false` - `true` |
| **eapFastUsePacs**  boolean | EapFastUsePacs flag.  Choices:   - `false` - `true` |
| **eapFastUsePacsAcceptClientCert**  boolean | The eapFastUsePacsAcceptClientCert is required only if eapFastUsePacsAllowAuthenProvisioning is true, otherwise it must be ignored.  Choices:   - `false` - `true` |
| **eapFastUsePacsAllowAnonymProvisioning**  boolean | The eapFastUsePacsAllowAnonymProvisioning is required only if eapFastUsePacs is true, otherwise it must be ignored.  Choices:   - `false` - `true` |
| **eapFastUsePacsAllowAuthenProvisioning**  boolean | The eapFastUsePacsAllowAuthenProvisioning is required only if eapFastUsePacs is true, otherwise it must be ignored.  Choices:   - `false` - `true` |
| **eapFastUsePacsAllowMachineAuthentication**  boolean | EapFastUsePacsAllowMachineAuthentication flag.  Choices:   - `false` - `true` |
| **eapFastUsePacsAuthorizationPacTtl**  integer | The eapFastUsePacsAuthorizationPacTtl is required only if eapFastUsePacsStatelessSessionResume is true, otherwise it must be ignored. |
| **eapFastUsePacsAuthorizationPacTtlUnits**  string | The eapFastUsePacsAuthorizationPacTtlUnits is required only if eapFastUsePacsStatelessSessionResume is true, otherwise it must be ignored. Allowed Values - SECONDS, - MINUTES, - HOURS, - DAYS, - WEEKS. |
| **eapFastUsePacsMachinePacTtl**  integer | The eapFastUsePacsMachinePacTtl is required only if eapFastUsePacsAllowMachineAuthentication is true, otherwise it must be ignored. |
| **eapFastUsePacsMachinePacTtlUnits**  string | The eapFastUsePacsMachinePacTtlUnits is required only if eapFastUsePacsAllowMachineAuthentication is true, otherwise it must be ignored. Allowed Values - SECONDS, - MINUTES, - HOURS, - DAYS, - WEEKS. |
| **eapFastUsePacsReturnAccessAcceptAfterAuthenticatedProvisioning**  boolean | The eapFastUsePacsReturnAccessAcceptAfterAuthenticatedProvisioning is required only if eapFastUsePacsAllowAuthenProvisioning is true, otherwise it must be ignored.  Choices:   - `false` - `true` |
| **eapFastUsePacsStatelessSessionResume**  boolean | The eapFastUsePacsStatelessSessionResume is required only if eapFastUsePacs is true, otherwise it must be ignored.  Choices:   - `false` - `true` |
| **eapFastUsePacsTunnelPacTtl**  integer | The eapFastUsePacsTunnelPacTtl is required only if eapFastUsePacs is true, otherwise it must be ignored. |
| **eapFastUsePacsTunnelPacTtlUnits**  string | The eapFastUsePacsTunnelPacTtlUnits is required only if eapFastUsePacs is true, otherwise it must be ignored. Allowed Values - SECONDS, - MINUTES, - HOURS, - DAYS, - WEEKS. |
| **eapFastUsePacsUseProactivePacUpdatePrecentage**  integer | The eapFastUsePacsUseProactivePacUpdatePrecentage is required only if eapFastUsePacs is true, otherwise it must be ignored. |
| **eapTls**  dictionary | The eapTls is required only if allowEapTls is true, otherwise it must be ignored. The object eapTls contains the settings for EAP TLS protocol. |
| **allowEapTlsAuthOfExpiredCerts**  boolean | AllowEapTlsAuthOfExpiredCerts flag.  Choices:   - `false` - `true` |
| **eapTlsEnableStatelessSessionResume**  boolean | EapTlsEnableStatelessSessionResume flag.  Choices:   - `false` - `true` |
| **eapTlsSessionTicketPrecentage**  integer | The eapTlsSessionTicketPrecentage is required only if eapTlsEnableStatelessSessionResume is true, otherwise it must be ignored. |
| **eapTlsSessionTicketTtl**  integer | Time to live. The eapTlsSessionTicketTtl is required only if eapTlsEnableStatelessSessionResume is true, otherwise it must be ignored. |
| **eapTlsSessionTicketTtlUnits**  string | Time to live time units. The eapTlsSessionTicketTtlUnits is required only if eapTlsEnableStatelessSessionResume is true, otherwise it must be ignored. Allowed Values - SECONDS, - MINUTES, - HOURS, - DAYS, - WEEKS. |
| **eapTlsLBit**  boolean | EapTlsLBit flag.  Choices:   - `false` - `true` |
| **eapTtls**  dictionary | The eapTtls is required only if allowEapTtls is true, otherwise it must be ignored. The object eapTtls contains the settings for EAP TTLS protocol. |
| **eapTtlsChap**  boolean | EapTtlsChap flag.  Choices:   - `false` - `true` |
| **eapTtlsEapMd5**  boolean | EapTtlsEapMd5 flag.  Choices:   - `false` - `true` |
| **eapTtlsEapMsChapV2**  boolean | EapTtlsEapMsChapV2 flag.  Choices:   - `false` - `true` |
| **eapTtlsEapMsChapV2PwdChange**  boolean | The eapTtlsEapMsChapV2PwdChange is required only if eapTtlsEapMsChapV2 is true, otherwise it must be ignored.  Choices:   - `false` - `true` |
| **eapTtlsEapMsChapV2PwdChangeRetries**  integer | The eapTtlsEapMsChapV2PwdChangeRetries is required only if eapTtlsEapMsChapV2 is true, otherwise it must be ignored. Valid range is 0-3. |
| **eapTtlsMsChapV1**  boolean | EapTtlsMsChapV1 flag.  Choices:   - `false` - `true` |
| **eapTtlsMsChapV2**  boolean | EapTtlsMsChapV2 flag.  Choices:   - `false` - `true` |
| **eapTtlsPapAscii**  boolean | EapTtlsPapAscii flag.  Choices:   - `false` - `true` |
| **id**  string | Resource UUID, Mandatory for update. |
| **ise_debug**  boolean | Flag for Identity Services Engine SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **ise_hostname**  string / required | The Identity Services Engine hostname. |
| **ise_password**  string / required | The Identity Services Engine password to authenticate. |
| **ise_username**  string / required | The Identity Services Engine username to authenticate. |
| **ise_uses_api_gateway**  boolean  added in cisco.ise 1.1.0 | Flag that informs the SDK whether to use the Identity Services Engine’s API Gateway to send requests.  If it is true, it uses the ISE’s API Gateway and sends requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}.  If it is false, it sends the requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}:{{port}}, where the port value depends on the Service used (ERS, Mnt, UI, PxGrid).  Choices:   - `false` - `true` ← (default) |
| **ise_uses_csrf_token**  boolean  added in cisco.ise 3.0.0 | Flag that informs the SDK whether we send the CSRF token to ISE’s ERS APIs.  If it is True, the SDK assumes that your ISE CSRF Check is enabled.  If it is True, it assumes you need the SDK to manage the CSRF token automatically for you.  Choices:   - `false` ← (default) - `true` |
| **ise_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **ise_version**  string | Informs the SDK which version of Identity Services Engine to use.  Default: `"3.1_Patch_1"` |
| **ise_wait_on_rate_limit**  boolean | Flag for Identity Services Engine SDK to enable automatic rate-limit handling.  Choices:   - `false` - `true` ← (default) |
| **name**  string | Resource Name. |
| **peap**  dictionary | Allowed Protocols’s peap. |
| **allowPeapEapGtc**  boolean | AllowPeapEapGtc flag.  Choices:   - `false` - `true` |
| **allowPeapEapGtcPwdChange**  boolean | The allowPeapEapGtcPwdChange is required only if allowPeapEapGtc is true, otherwise it must be ignored.  Choices:   - `false` - `true` |
| **allowPeapEapGtcPwdChangeRetries**  integer | The allowPeapEapGtcPwdChangeRetries is required only if allowPeapEapGtc is true, otherwise it must be ignored. Valid range is 0-3. |
| **allowPeapEapMsChapV2**  boolean | AllowPeapEapMsChapV2 flag.  Choices:   - `false` - `true` |
| **allowPeapEapMsChapV2PwdChange**  boolean | The allowPeapEapMsChapV2PwdChange is required only if allowPeapEapMsChapV2 is true, otherwise it must be ignored.  Choices:   - `false` - `true` |
| **allowPeapEapMsChapV2PwdChangeRetries**  integer | The allowPeapEapMsChapV2PwdChangeRetries is required only if allowPeapEapMsChapV2 is true, otherwise it must be ignored. Valid range is 0-3. |
| **allowPeapEapTls**  boolean | AllowPeapEapTls flag.  Choices:   - `false` - `true` |
| **allowPeapEapTlsAuthOfExpiredCerts**  boolean | The allowPeapEapTlsAuthOfExpiredCerts is required only if allowPeapEapTls is true, otherwise it must be ignored.  Choices:   - `false` - `true` |
| **allowPeapV0**  boolean | AllowPeapV0 flag.  Choices:   - `false` - `true` |
| **requireCryptobinding**  boolean | RequireCryptobinding flag.  Choices:   - `false` - `true` |
| **preferredEapProtocol**  string | The preferredEapProtocol is required only if allowPreferredEapProtocol is true, otherwise it must be ignored. Allowed Values - EAP_FAST, - PEAP, - LEAP, - EAP_MD5, - EAP_TLS, - EAP_TTLS, - TEAP. |
| **processHostLookup**  boolean | ProcessHostLookup flag.  Choices:   - `false` - `true` |
| **requireMessageAuth**  boolean | RequireMessageAuth flag.  Choices:   - `false` - `true` |
| **teap**  dictionary | The teap is required only if allowTeap is true, otherwise it must be ignored. The object teap contains the settings for TEAP protocol. |
| **acceptClientCertDuringTunnelEst**  boolean | AcceptClientCertDuringTunnelEst flag.  Choices:   - `false` - `true` |
| **allowDowngradeMsk**  boolean | AllowDowngradeMsk flag.  Choices:   - `false` - `true` |
| **allowTeapEapMsChapV2**  boolean | AllowTeapEapMsChapV2 flag.  Choices:   - `false` - `true` |
| **allowTeapEapMsChapV2PwdChange**  boolean | The allowTeapEapMsChapV2PwdChange is required only if allowTeapEapMsChapV2 is true, otherwise it must be ignored.  Choices:   - `false` - `true` |
| **allowTeapEapMsChapV2PwdChangeRetries**  integer | The allowTeapEapMsChapV2PwdChangeRetries is required only if allowTeapEapMsChapV2 is true, otherwise it must be ignored. Valid range is 0-3. |
| **allowTeapEapTls**  boolean | AllowTeapEapTls flag.  Choices:   - `false` - `true` |
| **allowTeapEapTlsAuthOfExpiredCerts**  boolean | The allowTeapEapTlsAuthOfExpiredCerts is required only if allowTeapEapTls is true, otherwise it must be ignored.  Choices:   - `false` - `true` |
| **enableEapChaining**  boolean | EnableEapChaining flag.  Choices:   - `false` - `true` |

## [Notes](allowed_protocols_module.md#id4)

> **Note:**
>
> - SDK Method used are allowed_protocols.AllowedProtocols.create_allowed_protocol, allowed_protocols.AllowedProtocols.delete_allowed_protocol_by_id, allowed_protocols.AllowedProtocols.update_allowed_protocol_by_id,
> - Paths used are post /ers/config/allowedprotocols, delete /ers/config/allowedprotocols/{id}, put /ers/config/allowedprotocols/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [Examples](allowed_protocols_module.md#id5)

```yaml+jinja
- name: Update by id
  cisco.ise.allowed_protocols:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    allowChap: true
    allowEapFast: true
    allowEapMd5: true
    allowEapTls: true
    allowEapTtls: true
    allowLeap: true
    allowMsChapV1: true
    allowMsChapV2: true
    allowPapAscii: true
    allowPeap: true
    allowPreferredEapProtocol: true
    allowTeap: true
    allowWeakCiphersForEap: true
    description: string
    eapFast:
      allowEapFastEapGtc: true
      allowEapFastEapGtcPwdChange: true
      allowEapFastEapGtcPwdChangeRetries: 0
      allowEapFastEapMsChapV2: true
      allowEapFastEapMsChapV2PwdChange: true
      allowEapFastEapMsChapV2PwdChangeRetries: 0
      allowEapFastEapTls: true
      allowEapFastEapTlsAuthOfExpiredCerts: true
      eapFastDontUsePacsAcceptClientCert: true
      eapFastDontUsePacsAllowMachineAuthentication: true
      eapFastEnableEAPChaining: true
      eapFastUsePacs: true
      eapFastUsePacsAcceptClientCert: true
      eapFastUsePacsAllowAnonymProvisioning: true
      eapFastUsePacsAllowAuthenProvisioning: true
      eapFastUsePacsAllowMachineAuthentication: true
      eapFastUsePacsAuthorizationPacTtl: 0
      eapFastUsePacsAuthorizationPacTtlUnits: string
      eapFastUsePacsMachinePacTtl: 0
      eapFastUsePacsMachinePacTtlUnits: string
      eapFastUsePacsReturnAccessAcceptAfterAuthenticatedProvisioning: true
      eapFastUsePacsStatelessSessionResume: true
      eapFastUsePacsTunnelPacTtl: 0
      eapFastUsePacsTunnelPacTtlUnits: string
      eapFastUsePacsUseProactivePacUpdatePrecentage: 0
    eapTls:
      allowEapTlsAuthOfExpiredCerts: true
      eapTlsEnableStatelessSessionResume: true
      eapTlsSessionTicketPrecentage: 0
      eapTlsSessionTicketTtl: 0
      eapTlsSessionTicketTtlUnits: string
    eapTlsLBit: true
    eapTtls:
      eapTtlsChap: true
      eapTtlsEapMd5: true
      eapTtlsEapMsChapV2: true
      eapTtlsEapMsChapV2PwdChange: true
      eapTtlsEapMsChapV2PwdChangeRetries: 0
      eapTtlsMsChapV1: true
      eapTtlsMsChapV2: true
      eapTtlsPapAscii: true
    id: string
    name: string
    peap:
      allowPeapEapGtc: true
      allowPeapEapGtcPwdChange: true
      allowPeapEapGtcPwdChangeRetries: 0
      allowPeapEapMsChapV2: true
      allowPeapEapMsChapV2PwdChange: true
      allowPeapEapMsChapV2PwdChangeRetries: 0
      allowPeapEapTls: true
      allowPeapEapTlsAuthOfExpiredCerts: true
      allowPeapV0: true
      requireCryptobinding: true
    preferredEapProtocol: string
    processHostLookup: true
    requireMessageAuth: true
    teap:
      acceptClientCertDuringTunnelEst: true
      allowDowngradeMsk: true
      allowTeapEapMsChapV2: true
      allowTeapEapMsChapV2PwdChange: true
      allowTeapEapMsChapV2PwdChangeRetries: 0
      allowTeapEapTls: true
      allowTeapEapTlsAuthOfExpiredCerts: true
      enableEapChaining: true

- name: Delete by id
  cisco.ise.allowed_protocols:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.allowed_protocols:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    allowChap: true
    allowEapFast: true
    allowEapMd5: true
    allowEapTls: true
    allowEapTtls: true
    allowLeap: true
    allowMsChapV1: true
    allowMsChapV2: true
    allowPapAscii: true
    allowPeap: true
    allowPreferredEapProtocol: true
    allowTeap: true
    allowWeakCiphersForEap: true
    description: string
    eapFast:
      allowEapFastEapGtc: true
      allowEapFastEapGtcPwdChange: true
      allowEapFastEapGtcPwdChangeRetries: 0
      allowEapFastEapMsChapV2: true
      allowEapFastEapMsChapV2PwdChange: true
      allowEapFastEapMsChapV2PwdChangeRetries: 0
      allowEapFastEapTls: true
      allowEapFastEapTlsAuthOfExpiredCerts: true
      eapFastDontUsePacsAcceptClientCert: true
      eapFastDontUsePacsAllowMachineAuthentication: true
      eapFastEnableEAPChaining: true
      eapFastUsePacs: true
      eapFastUsePacsAcceptClientCert: true
      eapFastUsePacsAllowAnonymProvisioning: true
      eapFastUsePacsAllowAuthenProvisioning: true
      eapFastUsePacsAllowMachineAuthentication: true
      eapFastUsePacsAuthorizationPacTtl: 0
      eapFastUsePacsAuthorizationPacTtlUnits: string
      eapFastUsePacsMachinePacTtl: 0
      eapFastUsePacsMachinePacTtlUnits: string
      eapFastUsePacsReturnAccessAcceptAfterAuthenticatedProvisioning: true
      eapFastUsePacsStatelessSessionResume: true
      eapFastUsePacsTunnelPacTtl: 0
      eapFastUsePacsTunnelPacTtlUnits: string
      eapFastUsePacsUseProactivePacUpdatePrecentage: 0
    eapTls:
      allowEapTlsAuthOfExpiredCerts: true
      eapTlsEnableStatelessSessionResume: true
      eapTlsSessionTicketPrecentage: 0
      eapTlsSessionTicketTtl: 0
      eapTlsSessionTicketTtlUnits: string
    eapTlsLBit: true
    eapTtls:
      eapTtlsChap: true
      eapTtlsEapMd5: true
      eapTtlsEapMsChapV2: true
      eapTtlsEapMsChapV2PwdChange: true
      eapTtlsEapMsChapV2PwdChangeRetries: 0
      eapTtlsMsChapV1: true
      eapTtlsMsChapV2: true
      eapTtlsPapAscii: true
    name: string
    peap:
      allowPeapEapGtc: true
      allowPeapEapGtcPwdChange: true
      allowPeapEapGtcPwdChangeRetries: 0
      allowPeapEapMsChapV2: true
      allowPeapEapMsChapV2PwdChange: true
      allowPeapEapMsChapV2PwdChangeRetries: 0
      allowPeapEapTls: true
      allowPeapEapTlsAuthOfExpiredCerts: true
      allowPeapV0: true
      requireCryptobinding: true
    preferredEapProtocol: string
    processHostLookup: true
    requireMessageAuth: true
    teap:
      acceptClientCertDuringTunnelEst: true
      allowDowngradeMsk: true
      allowTeapEapMsChapV2: true
      allowTeapEapMsChapV2PwdChange: true
      allowTeapEapMsChapV2PwdChangeRetries: 0
      allowTeapEapTls: true
      allowTeapEapTlsAuthOfExpiredCerts: true
      enableEapChaining: true
```

## [Return Values](allowed_protocols_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"allowChap": true, "allowEapFast": true, "allowEapMd5": true, "allowEapTls": true, "allowEapTtls": true, "allowLeap": true, "allowMsChapV1": true, "allowMsChapV2": true, "allowPapAscii": true, "allowPeap": true, "allowPreferredEapProtocol": true, "allowTeap": true, "allowWeakCiphersForEap": true, "description": "string", "eapFast": {"allowEapFastEapGtc": true, "allowEapFastEapGtcPwdChange": true, "allowEapFastEapGtcPwdChangeRetries": 0, "allowEapFastEapMsChapV2": true, "allowEapFastEapMsChapV2PwdChange": true, "allowEapFastEapMsChapV2PwdChangeRetries": 0, "allowEapFastEapTls": true, "allowEapFastEapTlsAuthOfExpiredCerts": true, "eapFastDontUsePacsAcceptClientCert": true, "eapFastDontUsePacsAllowMachineAuthentication": true, "eapFastEnableEAPChaining": true, "eapFastUsePacs": true, "eapFastUsePacsAcceptClientCert": true, "eapFastUsePacsAllowAnonymProvisioning": true, "eapFastUsePacsAllowAuthenProvisioning": true, "eapFastUsePacsAllowMachineAuthentication": true, "eapFastUsePacsAuthorizationPacTtl": 0, "eapFastUsePacsAuthorizationPacTtlUnits": "string", "eapFastUsePacsMachinePacTtl": 0, "eapFastUsePacsMachinePacTtlUnits": "string", "eapFastUsePacsReturnAccessAcceptAfterAuthenticatedProvisioning": true, "eapFastUsePacsStatelessSessionResume": true, "eapFastUsePacsTunnelPacTtl": 0, "eapFastUsePacsTunnelPacTtlUnits": "string", "eapFastUsePacsUseProactivePacUpdatePrecentage": 0}, "eapTls": {"allowEapTlsAuthOfExpiredCerts": true, "eapTlsEnableStatelessSessionResume": true, "eapTlsSessionTicketPrecentage": 0, "eapTlsSessionTicketTtl": 0, "eapTlsSessionTicketTtlUnits": "string"}, "eapTlsLBit": true, "eapTtls": {"eapTtlsChap": true, "eapTtlsEapMd5": true, "eapTtlsEapMsChapV2": true, "eapTtlsEapMsChapV2PwdChange": true, "eapTtlsEapMsChapV2PwdChangeRetries": 0, "eapTtlsMsChapV1": true, "eapTtlsMsChapV2": true, "eapTtlsPapAscii": true}, "id": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "name": "string", "peap": {"allowPeapEapGtc": true, "allowPeapEapGtcPwdChange": true, "allowPeapEapGtcPwdChangeRetries": 0, "allowPeapEapMsChapV2": true, "allowPeapEapMsChapV2PwdChange": true, "allowPeapEapMsChapV2PwdChangeRetries": 0, "allowPeapEapTls": true, "allowPeapEapTlsAuthOfExpiredCerts": true, "allowPeapV0": true, "requireCryptobinding": true}, "preferredEapProtocol": "string", "processHostLookup": true, "requireMessageAuth": true, "teap": {"acceptClientCertDuringTunnelEst": true, "allowDowngradeMsk": true, "allowTeapEapMsChapV2": true, "allowTeapEapMsChapV2PwdChange": true, "allowTeapEapMsChapV2PwdChangeRetries": 0, "allowTeapEapTls": true, "allowTeapEapTlsAuthOfExpiredCerts": true, "enableEapChaining": true}}` |
| **ise_update_response**  dictionary  added in cisco.ise 1.1.0 | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"UpdatedFieldsList": {"field": "string", "newValue": "string", "oldValue": "string", "updatedField": [{"field": "string", "newValue": "string", "oldValue": "string"}]}}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
[Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
