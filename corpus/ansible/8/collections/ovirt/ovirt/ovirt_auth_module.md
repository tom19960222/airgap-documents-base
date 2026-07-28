---
collection: ansible
version: "8"
title: "ovirt.ovirt.ovirt_auth module – Module to manage authentication to oVirt/RHV"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ovirt/ovirt/ovirt_auth_module.html
fetched_at: 2026-07-28T02:49:15+00:00
---
# ovirt.ovirt.ovirt_auth module – Module to manage authentication to oVirt/RHV

> **Note:**
>
> This module is part of the [ovirt.ovirt collection](https://galaxy.ansible.com/ui/repo/published/ovirt/ovirt/) (version 3.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ovirt.ovirt`.
> You need further requirements to be able to use this module,
> see [Requirements](ovirt_auth_module.md#ansible-collections-ovirt-ovirt-ovirt-auth-module-requirements) for details.
>
> To use it in a playbook, specify: `ovirt.ovirt.ovirt_auth`.

New in ovirt.ovirt 1.0.0

- [Synopsis](ovirt_auth_module.md#synopsis)
- [Requirements](ovirt_auth_module.md#requirements)
- [Parameters](ovirt_auth_module.md#parameters)
- [Notes](ovirt_auth_module.md#notes)
- [Examples](ovirt_auth_module.md#examples)
- [Return Values](ovirt_auth_module.md#return-values)

## [Synopsis](ovirt_auth_module.md#id1)

- This module authenticates to oVirt/RHV engine and creates SSO token, which should be later used in all other oVirt/RHV modules, so all modules don’t need to perform login and logout. This module returns an Ansible fact called *ovirt_auth*. Every module can use this fact as `auth` parameter, to perform authentication.

## [Requirements](ovirt_auth_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- ovirt-engine-sdk-python >= 4.4.0

## [Parameters](ovirt_auth_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_file**  path | A PEM file containing the trusted CA certificates. The certificate presented by the server will be verified using these CA certificates. If `ca_file` parameter is not set, system wide CA certificate store is used. Default value is set by *OVIRT_CAFILE* environment variable. |
| **compress**  boolean | A boolean flag indicating if the SDK should ask the server to send compressed responses. The default is *True*. Note that this is a hint for the server, and that it may return uncompressed data even when this parameter is set to *True*.  **Choices:**   - `false` - `true` ← (default) |
| **headers**  dictionary | A dictionary of HTTP headers to be added to each API call. |
| **hostname**  string | A string containing the hostname of the server. For example: *server.example.com*. Default value is set by *OVIRT_HOSTNAME* environment variable.  Either `url` or `hostname` is required. |
| **insecure**  boolean | A boolean flag that indicates if the server TLS certificate and host name should be checked.  **Choices:**   - `false` - `true` |
| **kerberos**  boolean | A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.  **Choices:**   - `false` ← (default) - `true` |
| **ovirt_auth**  dictionary | Previous run of the ovirt_auth used with `state` absent  Closes connection with the engine. |
| **password**  string | The password of the user. Default value is set by *OVIRT_PASSWORD* environment variable. |
| **state**  string | Specifies if a token should be created or revoked.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | The maximum total time to wait for the response, in seconds. A value of zero (the default) means wait forever. If the timeout expires before the response is received an exception will be raised. |
| **token**  string | SSO token to be used instead of login with username/password. Default value is set by *OVIRT_TOKEN* environment variable. |
| **url**  string | A string containing the API URL of the server. For example: *https://server.example.com/ovirt-engine/api*. Default value is set by *OVIRT_URL* environment variable.  Either `url` or `hostname` is required. |
| **username**  string | The name of the user. For example: *admin@internal* Default value is set by *OVIRT_USERNAME* environment variable. |

## [Notes](ovirt_auth_module.md#id4)

> **Note:**
>
> - Everytime you use ovirt_auth module to obtain ticket, you need to also revoke the ticket, when you no longer need it, otherwise the ticket would be revoked by engine when it expires. For an example of how to achieve that, please take a look at *examples* section.
> - In order to use this module you have to install oVirt/RHV Python SDK. To ensure it’s installed with correct version you can create the following task: *pip: name=ovirt-engine-sdk-python version=4.4.0*
> - Note that in oVirt/RHV 4.1 if you want to use a user which is not administrator you must enable the *ENGINE_API_FILTER_BY_DEFAULT* variable in engine. In oVirt/RHV 4.2 and later it’s enabled by default.

## [Examples](ovirt_auth_module.md#id5)

```yaml+jinja
  - block:
       # Create a vault with `ovirt_password` variable which store your
       # oVirt/RHV user's password, and include that yaml file with variable:
       - ansible.builtin.include_vars: ovirt_password.yml

       - name: Obtain SSO token with using username/password credentials
         ovirt.ovirt.ovirt_auth:
           url: https://ovirt.example.com/ovirt-engine/api
           username: admin@internal
           ca_file: ca.pem
           password: "{{ ovirt_password }}"

       # Previous task generated I(ovirt_auth) fact, which you can later use
       # in different modules as follows:
       - ovirt.ovirt.ovirt_vm:
           auth: "{{ ovirt_auth }}"
           state: absent
           name: myvm

    always:
      - name: Always revoke the SSO token
        ovirt.ovirt.ovirt_auth:
          state: absent
          ovirt_auth: "{{ ovirt_auth }}"

# When user will set following environment variables:
#   OVIRT_URL = https://fqdn/ovirt-engine/api
#   OVIRT_USERNAME = admin@internal
#   OVIRT_PASSWORD = the_password
# User can login the oVirt using environment variable instead of variables
# in yaml file.
# This is mainly useful when using Ansible Tower or AWX, as it will work
# for Red Hat Virtualization credentials type.
  - name: Obtain SSO token
    ovirt_auth:
      state: present
```

## [Return Values](ovirt_auth_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ovirt_auth**  complex | Authentication facts, needed to perform authentication to oVirt/RHV.  **Returned:** success |
| **ca_file**  string | CA file, which is used to verify SSL/TLS connection.  **Returned:** success  **Sample:** `"ca.pem"` |
| **compress**  boolean | Flag indicating if compression is used for connection.  **Returned:** success  **Sample:** `true` |
| **headers**  dictionary | Dictionary of HTTP headers to be added to each API call.  **Returned:** success |
| **insecure**  boolean | Flag indicating if insecure connection is used.  **Returned:** success  **Sample:** `false` |
| **kerberos**  boolean | Flag indicating if kerberos is used for authentication.  **Returned:** success  **Sample:** `false` |
| **timeout**  integer | Number of seconds to wait for response.  **Returned:** success  **Sample:** `0` |
| **token**  string | SSO token which is used for connection to oVirt/RHV engine.  **Returned:** success  **Sample:** `"kdfVWp9ZgeewBXV-iq3Js1-xQJZPSEQ334FLb3eksoEPRaab07DhZ8ED8ghz9lJd-MQ2GqtRIeqhvhCkrUWQPw"` |
| **url**  string | URL of the oVirt/RHV engine API endpoint.  **Returned:** success  **Sample:** `"https://ovirt.example.com/ovirt-engine/api"` |

### Authors

- Ondra Machacek (@machacekondra)

### Collection links

- [Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
- [Homepage](https://www.ovirt.org/)
- [Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
