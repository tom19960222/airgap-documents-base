---
collection: ansible
version: "8"
title: "cyberark.pas.cyberark_account module – Module for CyberArk Account object creation, deletion, and modification using PAS Web Services SDK."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cyberark/pas/cyberark_account_module.html
fetched_at: 2026-07-28T02:03:22+00:00
---
# cyberark.pas.cyberark_account module – Module for CyberArk Account object creation, deletion, and modification using PAS Web Services SDK.

> **Note:**
>
> This module is part of the [cyberark.pas collection](https://galaxy.ansible.com/ui/repo/published/cyberark/pas/) (version 1.0.23).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cyberark.pas`.
>
> To use it in a playbook, specify: `cyberark.pas.cyberark_account`.

New in cyberark.pas 1.0.0

- [Synopsis](cyberark_account_module.md#synopsis)
- [Parameters](cyberark_account_module.md#parameters)
- [Examples](cyberark_account_module.md#examples)
- [Return Values](cyberark_account_module.md#return-values)

## [Synopsis](cyberark_account_module.md#id1)

- Creates a URI for adding, deleting, modifying a privileged credential within the Cyberark Vault. The request uses the Privileged Account Security Web Services SDK.

## [Parameters](cyberark_account_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **address**  string | The address of the endpoint where the privileged account is located. |
| **api_base_url**  string | A string containing the base URL of the server hosting CyberArk’s Privileged Account Security Web Services SDK.  Example <https://%3CIIS_Server_Ip%3E/PasswordVault/api/> |
| **cyberark_session**  dictionary / required | Dictionary set by a CyberArk authentication containing the different values to perform actions on a logged-on CyberArk session, please see [cyberark.pas.cyberark_authentication](cyberark_authentication_module.md#ansible-collections-cyberark-pas-cyberark-authentication-module) module for an example of cyberark_session. |
| **identified_by**  string | When an API call is made to Get Accounts, often times the default parameters passed will identify more than one account. This parameter is used to confidently identify a single account when the default query can return multiple results.  **Default:** `"username,address,platform_id"` |
| **logging_file**  string | Setting the log file name and location for troubleshooting logs.  **Default:** `"/tmp/ansible_cyberark.log"` |
| **logging_level**  string | Parameter used to define the level of troubleshooting output to the `logging_file` value.  **Choices:**   - `"NOTSET"` - `"DEBUG"` - `"INFO"` |
| **name**  string | The ObjectID of the account |
| **new_secret**  string | The new secret/password to be stored in CyberArk Vault. |
| **platform_account_properties**  dictionary | Object containing key-value pairs to associate with the account, as defined by the account platform. These properties are validated against the mandatory and optional properties of the specified platform’s definition. Optional properties that do not exist on the account will not be returned here. Internal properties are not returned. |
| **KEY**  aliases: Port, ExtrPass1Name, database  string | Freeform key value associated to the mandatory or optional property assigned to the specified Platform’s definition. |
| **platform_id**  string | The PolicyID of the Platform that is to be managing the account |
| **remote_machines_access**  dictionary | Set of parameters for defining PSM endpoint access targets. |
| **access_restricted_to_remote_machines**  boolean | Whether or not to restrict access only to specified remote machines.  **Choices:**   - `false` - `true` |
| **remote_machines**  string | List of targets allowed for this account. |
| **safe**  string / required | The safe in the Vault where the privileged account is to be located. |
| **secret**  string | The initial password for the creation of the account |
| **secret_management**  dictionary | Set of parameters associated with the management of the credential. |
| **automatic_management_enabled**  boolean | Parameter that indicates whether the CPM will manage the password or not.  **Choices:**   - `false` ← (default) - `true` |
| **management_action**  string | CPM action flag to be placed on the account object for credential rotation.  **Choices:**   - `"change"` - `"change_immediately"` - `"reconcile"` |
| **manual_management_reason**  string | String value indicating why the CPM will NOT manage the password. |
| **new_secret**  string | The actual password value that will be assigned for the CPM action to be taken. |
| **perform_management_action**  string | `always` will perform the management action in every action.  `on_create` will only perform the management action right after the account is created.  **Choices:**   - `"always"` ← (default) - `"on_create"` |
| **secret_type**  string | The value that identifies what type of account it will be.  **Choices:**   - `"password"` ← (default) - `"key"` |
| **state**  string | Assert the desired state of the account `present` to creat or update and account object. Set to `absent` for deletion of an account object.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **username**  string | The username associated with the account. |
| **validate_certs**  boolean | If `false`, SSL certificate chain will not be validated. This should only set to `true` if you have a root CA certificate installed on each node.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](cyberark_account_module.md#id3)

```yaml+jinja
collections:
  - cyberark.pas

tasks:

  - name: Logon to CyberArk Vault using PAS Web Services SDK
    cyberark_authentication:
      api_base_url: "http://components.cyberark.local"
      validate_certs: false
      username: "bizdev"
      password: "Cyberark1"

  - name: Creating an Account using the PAS WebServices SDK
    cyberark_account:
      logging_level: DEBUG
      identified_by: "address,username"
      safe: "Test"
      address: "cyberark.local"
      username: "administrator-x"
      platform_id: WinServerLocal
      secret: "@N&Ibl3!"
      platform_account_properties:
          LogonDomain: "cyberark"
          OwnerName: "ansible_user"
      secret_management:
          automatic_management_enabled: true
      state: present
      cyberark_session: "{{ cyberark_session }}"
    register: cyberarkaction

  - name:
      - Rotate credential via reconcile and providing the password to
        bechanged to.
    cyberark_account:
      identified_by: "address,username"
      safe: "Domain_Admins"
      address: "prod.cyberark.local"
      username: "admin"
      platform_id: WinDomain
      platform_account_properties:
          LogonDomain: "PROD"
      secret_management:
          new_secret: "Ama123ah12@#!Xaamdjbdkl@#112"
          management_action: "reconcile"
          automatic_management_enabled: true
      state: present
      cyberark_session: "{{ cyberark_session }}"
    register: reconcileaccount

  - name: Logoff from CyberArk Vault
    cyberark_authentication:
      state: absent
      cyberark_session: "{{ cyberark_session }}"
```

## [Return Values](cyberark_account_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Identify if the playbook run resulted in a change to the account in any way.  **Returned:** always |
| **failed**  boolean | Whether playbook run resulted in a failure of any kind.  **Returned:** always |
| **result**  complex | A json dump of the resulting action.  **Returned:** success |
| **address**  string | The adress of the endpoint where the privileged account is located.  **Returned:** successful addition and modification  **Sample:** `"dev.local"` |
| **createdTime**  integer | Timeframe calculation of the timestamp of account creation.  **Returned:** successful addition and modification  **Sample:** `1567824520` |
| **id**  integer | Internal ObjectID for the account object identified  **Returned:** successful addition and modification  **Sample:** `2521` |
| **name**  string | The external ObjectID of the account  **Returned:** successful addition and modification  **Sample:** `"['Operating System-WinServerLocal-cyberark.local-administrator']"` |
| **platformAccountProperties**  complex | Object containing key-value pairs to associate with the account, as defined by the account platform.  **Returned:** successful addition and modification |
| **KEY VALUE**  string | Object containing key-value pairs to associate with the account, as defined by the account platform.  **Returned:** successful addition and modification  **Sample:** `"[{'LogonDomain': 'cyberark'}, {'Port': '22'}]"` |
| **platformId**  string | The PolicyID of the Platform that is to be managing the account.  **Returned:** successful addition and modification  **Sample:** `"WinServerLocal"` |
| **safeName**  string | The safe in the Vault where the privileged account is to be located.  **Returned:** successful addition and modification  **Sample:** `"Domain_Admins"` |
| **secretManagement**  complex | Set of parameters associated with the management of the credential.  **Returned:** successful addition and modification |
| **automaticManagementEnabled**  boolean | Parameter that indicates whether the CPM will manage the password or not.  **Returned:** successful addition and modification |
| **lastModifiedTime**  integer | Timeframe calculation of the timestamp of account modification.  **Returned:** successful addition and modification  **Sample:** `1567824520` |
| **manualManagementReason**  string | Reason for disabling automatic management of the account  **Returned:** if `automaticManagementEnabled` is set to false  **Sample:** `"This is a static account"` |
| **secretType**  list / elements=string | The value that identifies what type of account it will be  **Returned:** successful addition and modification  **Sample:** `["key", "password"]` |
| **userName**  string | The username associated with the account  **Returned:** successful addition and modification  **Sample:** `"administrator"` |
| **status_code**  integer | Result HTTP Status code.  **Returned:** success  **Sample:** `"200, 201, -1, 204"` |

### Authors

- CyberArk BizDev (@cyberark-bizdev)
- Edward Nunez (@enunez-cyberark)
- James Stutes (@jimmyjamcabd)

### Collection links

- [Issue Tracker](https://github.com/cyberark/ansible-security-automation-collection/issues)
- [Repository (Sources)](https://github.com/cyberark/ansible-security-automation-collection)
