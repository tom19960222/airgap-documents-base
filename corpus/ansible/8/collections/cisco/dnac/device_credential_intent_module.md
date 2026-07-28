---
collection: ansible
version: "8"
title: "cisco.dnac.device_credential_intent module – Resource module for Global Device Credentials and Assigning Credentials to sites."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/device_credential_intent_module.html
fetched_at: 2026-07-28T01:21:52+00:00
---
# cisco.dnac.device_credential_intent module – Resource module for Global Device Credentials and Assigning Credentials to sites.

> **Note:**
>
> This module is part of the [cisco.dnac collection](https://galaxy.ansible.com/ui/repo/published/cisco/dnac/) (version 6.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.dnac`.
> You need further requirements to be able to use this module,
> see [Requirements](device_credential_intent_module.md#ansible-collections-cisco-dnac-device-credential-intent-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.device_credential_intent`.

New in cisco.dnac 6.8.0

- [Synopsis](device_credential_intent_module.md#synopsis)
- [Requirements](device_credential_intent_module.md#requirements)
- [Parameters](device_credential_intent_module.md#parameters)
- [Notes](device_credential_intent_module.md#notes)
- [See Also](device_credential_intent_module.md#see-also)
- [Examples](device_credential_intent_module.md#examples)
- [Return Values](device_credential_intent_module.md#return-values)

## [Synopsis](device_credential_intent_module.md#id1)

- Manage operations on Global Device Credentials and Assigning Credentials to sites.
- API to create global device credentials.
- API to update global device credentials.
- API to delete global device credentials.
- API to assign the device credential to the site.

## [Requirements](device_credential_intent_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](device_credential_intent_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary / required | List of details of global device credentials and site names. |
| **AssignCredentialsToSite**  dictionary | Assign Device Credentials to Site. |
| **cliDescription**  string | CLI Credential Description. |
| **cliId**  string | CLI Credential Id. Use (Description, Username) or Id. |
| **cliUsername**  string | CLI Credential Username. |
| **httpRead**  string | HTTP(S) Read Credential Id. Use (Description, Username) or Id. |
| **httpReadDescription**  string | HTTP(S) Read Credential Description. |
| **httpReadUsername**  string | HTTP(S) Read Credential Username. |
| **httpWrite**  string | HTTP(S) Write Credential Id. Use (Description, Username) or Id. |
| **httpWriteDescription**  string | HTTP(S) Write Credential Description. |
| **httpWriteUsername**  string | HTTP(S) Write Credential Username. |
| **siteName**  list / elements=string | Site Name to assign credential. |
| **snmpV2ReadDescription**  string | SNMPv2c Read Credential Description. |
| **snmpV2ReadId**  string | SNMPv2c Read Credential Id. Use Description or Id. |
| **snmpV2WriteDescription**  string | SNMPv2c Write Credential Description. |
| **snmpV2WriteId**  string | SNMPv2c Write Credential Id. Use Description or Id. |
| **snmpV3Description**  string | SNMPv3 Credential Description. |
| **snmpV3Id**  string | SNMPv3 Credential Id. Use Description or Id. |
| **GlobalCredentialDetails**  dictionary | Manages global device credentials |
| **cliCredential**  list / elements=dictionary | Global Credential V2’s cliCredential. |
| **description**  string | Description. Required for creating the credential. |
| **enablePassword**  string | cliCredential credential Enable Password.  Password cannot contain spaces or angle brackets (< >) |
| **id**  string | Credential Id. Use this for updating the device credential. |
| **old_description**  string | Old Description. Use this for updating the description/Username. |
| **old_username**  string | Old Username. Use this for updating the description/Username. |
| **password**  string | cliCredential credential Password.  Required for creating/updating the credential.  Password cannot contain spaces or angle brackets (< >). |
| **username**  string | cliCredential credential Username.  Username cannot contain spaces or angle brackets (< >). |
| **httpsRead**  list / elements=dictionary | Global Credential V2’s httpsRead. |
| **id**  string | Credential Id. Use this for updating the device credential. |
| **name**  string | Name. Required for creating the credential. |
| **old_description**  string | Old Description. Use this for updating the description/Username. |
| **old_username**  string | Old Username. Use this for updating the description/Username. |
| **password**  string | httpsRead credential Password.  Required for creating/updating the credential.  Password cannot contain spaces or angle brackets (< >). |
| **port**  integer | Port. Default port is 443. |
| **username**  string | httpsRead credential Username.  Username cannot contain spaces or angle brackets (< >). |
| **httpsWrite**  list / elements=dictionary | Global Credential V2’s httpsWrite. |
| **id**  string | Credential Id. Use this for updating the device credential. |
| **name**  string | Name. Required for creating the credential. |
| **old_description**  string | Old Description. Use this for updating the description/Username. |
| **old_username**  string | Old Username. Use this for updating the description/Username. |
| **password**  string | httpsWrite credential Password.  Required for creating/updating the credential.  Password cannot contain spaces or angle brackets (< >). |
| **port**  integer | Port. Default port is 443. |
| **username**  string | httpsWrite credential Username.  Username cannot contain spaces or angle brackets (< >). |
| **snmpV2cRead**  list / elements=dictionary | Global Credential V2’s snmpV2cRead. |
| **description**  string | Description. Required for creating the credential. |
| **id**  string | Credential Id. Use this for updating the device credential. |
| **old_description**  string | Old Description. Use this for updating the description. |
| **readCommunity**  string | snmpV2cRead Read Community.  Password cannot contain spaces or angle brackets (< >). |
| **snmpV2cWrite**  list / elements=dictionary | Global Credential V2’s snmpV2cWrite. |
| **description**  string | Description. Required for creating the credential. |
| **id**  string | Credential Id. Use this for updating the device credential. |
| **old_description**  string | Old Description. Use this for updating the description. |
| **writeCommunity**  string | snmpV2cWrite Write Community.  Password cannot contain spaces or angle brackets (< >). |
| **snmpV3**  list / elements=dictionary | Global Credential V2’s snmpV3. |
| **authPassword**  string | snmpV3 Auth Password.  Password must contain minimum 8 characters.  Password cannot contain spaces or angle brackets (< >). |
| **authType**  string | Auth Type. [“SHA”, “MD5”]. |
| **description**  string | snmpV3 Description.  Should be unique from other snmpV3 credentials. |
| **id**  string | Credential Id. Use this for updating the device credential. |
| **old_description**  string | Old Description. Use this for updating the description. |
| **privacyPassword**  string | snmpV3 Privacy Password.  Password must contain minimum 8 characters.  Password cannot contain spaces or angle brackets (< >). |
| **privacyType**  string | Privacy Type. [“AES128”, “AES192”, “AES256”]. |
| **snmpMode**  string | Snmp Mode. [“AUTHPRIV”, “AUTHNOPRIV”, “NOAUTHNOPRIV”]. |
| **username**  string | snmpV3 credential Username.  Username cannot contain spaces or angle brackets (< >). |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_log**  boolean | Flag for logging playbook execution details. If set to true the log file will be created at the location of the execution with the name dnac.log  **Choices:**   - `false` ← (default) - `true` |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  string | The Cisco DNA Center port.  **Default:** `"443"` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.2.3.3"` |
| **state**  string | The state of Cisco DNA Center after module completion.  **Choices:**   - `"merged"` ← (default) - `"deleted"` |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](device_credential_intent_module.md#id4)

> **Note:**
>
> - SDK Method used are discovery.Discovery.create_global_credentials_v2, discovery.Discovery.delete_global_credential_v2, discovery.Discovery.update_global_credentials_v2, network_settings.NetworkSettings.assign_device_credential_to_site_v2,
> - Paths used are post /dna/intent/api/v2/global-credential, delete /dna/intent/api/v2/global-credential/{id}, put /dna/intent/api/v2/global-credential, post /dna/intent/api/v2/credential-to-site/{siteId},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](device_credential_intent_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Discovery CreateGlobalCredentialsV2](https://developer.cisco.com/docs/dna-center/#!create-global-credentials-v-2)
> :   Complete reference of the CreateGlobalCredentialsV2 API.
>
> [Cisco DNA Center documentation for Discovery DeleteGlobalCredentialV2](https://developer.cisco.com/docs/dna-center/#!delete-global-credential-v-2)
> :   Complete reference of the DeleteGlobalCredentialV2 API.
>
> [Cisco DNA Center documentation for Discovery UpdateGlobalCredentialsV2](https://developer.cisco.com/docs/dna-center/#!update-global-credentials-v-2)
> :   Complete reference of the UpdateGlobalCredentialsV2 API.
>
> [Cisco DNA Center documentation for Network Settings AssignDeviceCredentialToSiteV2](https://developer.cisco.com/docs/dna-center/#!assign-device-credential-to-site-v-2)
> :   Complete reference of the AssignDeviceCredentialToSiteV2 API.

## [Examples](device_credential_intent_module.md#id6)

```yaml+jinja
---
  - name: Create Credentials and assign it to a site.
    cisco.dnac.device_credential_intent:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: True
    state: merged
    config:
    - GlobalCredentialDetails:
        cliCredential:
        - description: string
          username: string
          password: string
          enablePassword: string
        snmpV2cRead:
        - description: string
          readCommunity: string
        snmpV2cWrite:
        - description: string
          writeCommunity: string
        snmpV3:
        - authPassword: string
          authType: SHA
          snmpMode: AUTHPRIV
          privacyPassword: string
          privacyType: AES128
          username: string
          description: string
        httpsRead:
        - description: string
          username: string
          password: string
          port: 443
        httpsWrite:
        - description: string
          username: string
          password: string
          port: 443
      AssignCredentialsToSite:
        cliId: string
        snmpV2ReadId: string
        snmpV2WriteId: string
        snmpV3Id: string
        httpRead: string
        httpWrite: string
        siteName:
        - string

  - name: Create Multiple Credentials.
    cisco.dnac.device_credential_intent:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: True
    state: merged
    config:
    - GlobalCredentialDetails:
        cliCredential:
        - description: string
          username: string
          password: string
          enablePassword: string
        - description: string
          username: string
          password: string
          enablePassword: string
        snmpV2cRead:
        - description: string
          readCommunity: string
        - description: string
          readCommunity: string
        snmpV2cWrite:
        - description: string
          writeCommunity: string
        - description: string
          writeCommunity: string
        snmpV3:
        - authPassword: string
          authType: SHA
          snmpMode: AUTHPRIV
          privacyPassword: string
          privacyType: AES128
          username: string
          description: string
        - authPassword: string
          authType: SHA
          snmpMode: AUTHPRIV
          privacyPassword: string
          privacyType: AES128
          username: string
          description: string
        httpsRead:
        - description: string
          username: string
          password: string
          port: 443
        - description: string
          username: string
          password: string
          port: 443
        httpsWrite:
        - description: string
          username: string
          password: string
          port: 443
        - description: string
          username: string
          password: string
          port: 443

  - name: Update global device credentials using id
    cisco.dnac.device_credential_intent:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: True
    state: merged
    config:
    - GlobalCredentialDetails:
        cliCredential:
        - description: string
          username: string
          password: string
          enablePassword: string
          id: string
        snmpV2cRead:
        - description: string
          readCommunity: string
          id: string
        snmpV2cWrite:
        - description: string
          writeCommunity: string
          id: string
        snmpV3:
        - authPassword: string
          authType: SHA
          snmpMode: AUTHPRIV
          privacyPassword: string
          privacyType: AES128
          username: string
          description: string
          id: string
        httpsRead:
        - description: string
          username: string
          password: string
          port: 443
          id: string
        httpsWrite:
        - description: string
          username: string
          password: string
          port: 443
          id: string

  - name: Update multiple global device credentials using id
    cisco.dnac.device_credential_intent:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: True
    state: merged
    config:
    - GlobalCredentialDetails:
        cliCredential:
        - description: string
          username: string
          password: string
          enablePassword: string
          id: string
        - description: string
          username: string
          password: string
          enablePassword: string
          id: string
        snmpV2cRead:
        - description: string
          readCommunity: string
          id: string
        - description: string
          readCommunity: string
          id: string
        snmpV2cWrite:
        - description: string
          writeCommunity: string
          id: string
        - description: string
          writeCommunity: string
          id: string
        snmpV3:
        - authPassword: string
          authType: SHA
          snmpMode: AUTHPRIV
          privacyPassword: string
          privacyType: AES128
          username: string
          description: string
          id: string
        - authPassword: string
          authType: SHA
          snmpMode: AUTHPRIV
          privacyPassword: string
          privacyType: AES128
          username: string
          description: string
          id: string
        httpsRead:
        - description: string
          username: string
          password: string
          port: 443
          id: string
        - description: string
          username: string
          password: string
          port: 443
          id: string
        httpsWrite:
        - description: string
          username: string
          password: string
          port: 443
          id: string
        - description: string
          username: string
          password: string
          port: 443
          id: string

  - name: Update global device credential name/description using old name and description.
    cisco.dnac.device_credential_intent:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: True
    state: merged
    config:
    - GlobalCredentialDetails:
        cliCredential:
        - description: string
          username: string
          password: string
          enablePassword: string
          old_description: string
          old_username: string
        snmpV2cRead:
        - description: string
          readCommunity: string
          old_description: string
        snmpV2cWrite:
        - description: string
          writeCommunity: string
          old_description: string
        snmpV3:
        - authPassword: string
          authType: string
          snmpMode: string
          privacyPassword: string
          privacyType: string
          username: string
          description: string
        httpsRead:
        - description: string
          username: string
          password: string
          port: string
          old_description: string
          old_username: string
        httpsWrite:
        - description: string
          username: string
          password: string
          port: string
          old_description: string
          old_username: string

  - name: Assign Credentials to sites using old description and username.
    cisco.dnac.device_credential_intent:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: True
    state: merged
    config:
    - AssignCredentialsToSite:
        cliDescription: string
        cliUsername: string
        snmpV2ReadDescription: string
        snmpV2WriteDescription: string
        snmpV3Description: string
        httpReadDescription: string
        httpReadUsername: string
        httpWriteUsername: string
        httpWriteDescription: string
        siteName:
        - string
        - string
```

## [Return Values](device_credential_intent_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response1**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": {"taskId": "string", "url": "string"}, "version": "string"}` |
| **dnac_response2**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": {"taskId": "string", "url": "string"}, "version": "string"}` |

### Authors

- Muthu Rakesh (@MUTHU-RAKESH-27) Madhan Sankaranarayanan (@madhansansel)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
