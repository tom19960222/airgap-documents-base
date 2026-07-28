---
collection: ansible
version: "8"
title: "cisco.intersight.intersight_local_user_policy module – Local User Policy configuration for Cisco Intersight"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/intersight/intersight_local_user_policy_module.html
fetched_at: 2026-07-28T01:25:58+00:00
---
# cisco.intersight.intersight_local_user_policy module – Local User Policy configuration for Cisco Intersight

> **Note:**
>
> This module is part of the [cisco.intersight collection](https://galaxy.ansible.com/ui/repo/published/cisco/intersight/) (version 1.0.27).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.intersight`.
>
> To use it in a playbook, specify: `cisco.intersight.intersight_local_user_policy`.

New in cisco.intersight 2.10

- [Synopsis](intersight_local_user_policy_module.md#synopsis)
- [Parameters](intersight_local_user_policy_module.md#parameters)
- [Examples](intersight_local_user_policy_module.md#examples)
- [Return Values](intersight_local_user_policy_module.md#return-values)

## [Synopsis](intersight_local_user_policy_module.md#id1)

- Local User Policy configuration for Cisco Intersight.
- Used to configure local users on endpoint devices.
- For more information see [Cisco Intersight](https://intersight.com/apidocs).

## [Parameters](intersight_local_user_policy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **always_update_password**  string | Since passwords are not returned by the API and are encrypted on the endpoint, this option will instruct the module when to change the password.  If true, the password for each user will always be updated in the policy.  If false, the password will be updated only if the user is created.  **Default:** `false` |
| **api_key_id**  string / required | Public API Key ID associated with the private key.  If not set, the value of the INTERSIGHT_API_KEY_ID environment variable is used. |
| **api_private_key**  string / required | Filename (absolute path) or string of PEM formatted private key data to be used for Intersight API authentication.  If a string is used, Ansible vault should be used to encrypt string data.  Ex. ansible-vault encrypt_string –vault-id [tme@/Users/dsoper/Documents/vault_password_file](mailto:tme%40/Users/dsoper/Documents/vault_password_file) ‘—–BEGIN EC PRIVATE KEY—–  <your private key data>  —–END EC PRIVATE KEY—–’  If not set, the value of the INTERSIGHT_API_PRIVATE_KEY environment variable is used. |
| **api_uri**  string | URI used to access the Intersight API.  If not set, the value of the INTERSIGHT_API_URI environment variable is used.  **Default:** `"https://intersight.com/api/v1"` |
| **description**  aliases: descr  string | The user-defined description of the Local User policy.  Description can contain letters(a-z, A-Z), numbers(0-9), hyphen(-), period(.), colon(:), or an underscore(_). |
| **enable_password_expiry**  boolean | Enables password expiry on the endpoint.  **Choices:**   - `false` ← (default) - `true` |
| **enforce_strong_password**  boolean | If true, enables a strong password policy.  Strong password requirements:.   1. The password must have a minimum of 8 and a maximum of 20 characters. 2. The password must not contain the User’s Name. 3. The password must contain characters from three of the following four categories.  1. English uppercase characters (A through Z). 2. English lowercase characters (a through z). 3. Base 10 digits (0 through 9). 4. Non-alphabetic characters (! , @, ‘#’, $, %, ^, &, \*, -, _, +, =).   **Choices:**   - `false` - `true` ← (default) |
| **local_users**  string | List of local users on the endpoint.  An admin user already exists on the endpoint.  Add the admin user here only if you want to change the password, or enable or disable the user.  To add admin user, provide a username as ‘admin’, select the admin user role, and then proceed. |
| **enable**  boolean | Enable or disable the user.  **Choices:**   - `false` - `true` ← (default) |
| **password**  string / required | Valid login password of the user. |
| **role**  string / required | Roles associated with the user on the endpoint.  **Choices:**   - `"admin"` - `"readonly"` - `"user"` |
| **username**  string / required | Name of the user created on the endpoint. |
| **name**  string / required | The name assigned to the Local User Policy.  The name must be between 1 and 62 alphanumeric characters, allowing special characters :-_. |
| **organization**  string | The name of the Organization this resource is assigned to.  Profiles and Policies that are created within a Custom Organization are applicable only to devices in the same Organization.  **Default:** `"default"` |
| **password_history**  integer | Specifies number of times a password cannot repeat when changed (value between 0 and 5).  Entering 0 disables this option.  **Default:** `5` |
| **purge**  string | The purge argument instructs the module to consider the resource definition absolute.  If true, any previously configured usernames will be removed from the policy with the exception of the `admin` user which cannot be deleted.  **Default:** `false` |
| **state**  string | If `present`, will verify the resource is present and will create if needed.  If `absent`, will verify the resource is absent and will delete if needed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  string | List of tags in Key:<user-defined key> Value:<user-defined value> format. |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` - `true` ← (default) |
| **validate_certs**  boolean | Boolean control for verifying the api_uri TLS certificate  **Choices:**   - `false` - `true` ← (default) |

## [Examples](intersight_local_user_policy_module.md#id3)

```yaml+jinja
- name: Configure Local User policy
  intersight_local_user_policy:
    api_private_key: "{{ api_private_key }}"
    api_key_id: "{{ api_key_id }}"
    name: guest-admin
    tags:
      - Key: username
        Value: guest
    description: User named guest with admin role
    local_users:
      - username: guest
        role: admin
        password: vault_guest_password
      - username: reader
        role: readonly
        password: vault_reader_password

- name: Delete Local User policy
  intersight_local_user_policy:
    api_private_key: "{{ api_private_key }}"
    api_key_id: "{{ api_key_id }}"
    name: guest-admin
    state: absent
```

## [Return Values](intersight_local_user_policy_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_repsonse**  dictionary | The API response output returned by the specified resource.  **Returned:** always  **Sample:** `{"api_response": {"Description": "User named guest with admin role", "EndPointUserRoles": [{"ChangePassword": true, "Enabled": true}]}}` |

### Authors

- David Soper (@dsoper2)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/intersight-ansible)
- [Repository (Sources)](https://github.com/CiscoDevNet/intersight-ansible)
