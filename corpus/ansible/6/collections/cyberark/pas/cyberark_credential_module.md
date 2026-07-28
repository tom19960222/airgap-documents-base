---
collection: ansible
version: "6"
title: "cyberark.pas.cyberark_credential module – Credential retrieval using AAM Central Credential Provider."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cyberark/pas/cyberark_credential_module.html
fetched_at: 2026-07-27T17:24:45+00:00
---
# cyberark.pas.cyberark_credential module – Credential retrieval using AAM Central Credential Provider.

> **Note:**
>
> This module is part of the [cyberark.pas collection](https://galaxy.ansible.com/cyberark/pas) (version 1.0.14).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cyberark.pas`.
>
> To use it in a playbook, specify: `cyberark.pas.cyberark_credential`.

New in cyberark.pas 2.4

- [Synopsis](cyberark_credential_module.md#synopsis)
- [Parameters](cyberark_credential_module.md#parameters)
- [Examples](cyberark_credential_module.md#examples)
- [Return Values](cyberark_credential_module.md#return-values)

## [Synopsis](cyberark_credential_module.md#id1)

- Creates a URI for retrieving a credential from a password object stored in the Cyberark Vault. The request uses the Privileged Account Security Web Services SDK through the Central Credential Provider by requesting access with an Application ID.

## [Parameters](cyberark_credential_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_base_url**  string / required | A string containing the base URL of the server hosting the Central Credential Provider. |
| **app_id**  string / required | A string containing the Application ID authorized for retrieving the credential. |
| **client_cert**  string | A string containing the file location and name of the client certificate used for authentication. |
| **client_key**  string | A string containing the file location and name of the private key of the client certificate used for authentication. |
| **connection_timeout**  integer | An integer value of the allowed time before the request returns failed.  Default: `30` |
| **fail_request_on_password_change**  boolean | A boolean parameter for completing the request in the middle of a password change of the requested credential.  Choices:   - `false` ← (default) - `true` |
| **query**  string / required | A string containing details of the object being queried;  Possible parameters could be Safe, Folder, Object  (internal account name), UserName, Address, Database,  PolicyID. |
| **query_format**  string | The format for which your Query will be received by the CCP.  Choices:   - `"Exact"` ← (default) - `"Regexp"` |
| **reason**  string | Reason for requesting credential if required by policy;  It must be specified if the Policy managing the object  requires it. |
| **validate_certs**  boolean | If `false`, SSL certificate chain will not be validated. This should only set to `true` if you have a root CA certificate installed on each node.  Choices:   - `false` - `true` ← (default) |

## [Examples](cyberark_credential_module.md#id3)

```yaml+jinja
tasks:
  - name: credential retrieval basic
    cyberark_credential:
      api_base_url: "http://10.10.0.1"
      app_id: "TestID"
      query: "Safe=test;UserName=admin"
    register: result

  - name: credential retrieval advanced
    cyberark_credential:
      api_base_url: "https://components.cyberark.local"
      validate_certs: yes
      client_cert: /etc/pki/ca-trust/source/client.pem
      client_key: /etc/pki/ca-trust/source/priv-key.pem
      app_id: "TestID"
      query: "Safe=test;UserName=admin"
      connection_timeout: 60
      query_format: Exact
      fail_request_on_password_change: True
      reason: "requesting credential for Ansible deployment"
    register: result
```

## [Return Values](cyberark_credential_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Identify if the playbook run resulted in a change to the account in any way.  Returned: always |
| **failed**  boolean | Whether playbook run resulted in a failure of any kind.  Returned: always |
| **result**  complex | A json dump of the resulting action.  Returned: success |
| **Address**  string | The target address of the credential being queried  Returned: if required |
| **Content**  string | The password for the object being queried  Returned: always |
| **CPMDisabled**  string | A description of why this vaulted credential is not being managed by the CPM.  Returned: if CPM management is disabled and a reason is given |
| **CreationMethod**  string | This is how the object was created in the Vault  Returned: always |
| **DeviceType**  string | An internal File Category for more granular management of Platforms.  Returned: always |
| **Folder**  string | The folder within the Safe where the credential is stored.  Returned: always |
| **LogonDomain**  string | The Address friendly name resolved by the CPM  Returned: if populated |
| **Name**  string | The Cyberark unique object ID of the credential being queried.  Returned: always |
| **PasswordChangeInProcess**  boolean | If the password has a change flag placed by the CPM  Returned: always |
| **PolicyID**  string | Whether or not SSL certificates should be validated.  Returned: if assigned to a policy |
| **Safe**  string | The safe where the queried credential is stored  Returned: always |
| **Username**  string | The username of the credential being queried  Returned: if required |
| **status_code**  integer | Result HTTP Status code.  Returned: success  Sample: `"200, 201, -1, 204"` |

### Authors

- Edward Nunez (@enunez-cyberark)
- CyberArk BizDev (@cyberark-bizdev)
- Erasmo Acosta (@erasmix)
- James Stutes (@JimmyJamCABD)

### Collection links

[Issue Tracker](https://github.com/cyberark/ansible-security-automation-collection/issues)
[Repository (Sources)](https://github.com/cyberark/ansible-security-automation-collection)
