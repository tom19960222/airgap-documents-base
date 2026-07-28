---
collection: ansible
version: "8"
title: "community.general.cyberarkpassword lookup – get secrets from CyberArk AIM"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/cyberarkpassword_lookup.html
fetched_at: 2026-07-28T01:52:44+00:00
---
# community.general.cyberarkpassword lookup – get secrets from CyberArk AIM

> **Note:**
>
> This lookup plugin is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](cyberarkpassword_lookup.md#ansible-collections-community-general-cyberarkpassword-lookup-requirements) for details.
>
> To use it in a playbook, specify: `community.general.cyberarkpassword`.

- [Synopsis](cyberarkpassword_lookup.md#synopsis)
- [Requirements](cyberarkpassword_lookup.md#requirements)
- [Keyword parameters](cyberarkpassword_lookup.md#keyword-parameters)
- [Notes](cyberarkpassword_lookup.md#notes)
- [Examples](cyberarkpassword_lookup.md#examples)
- [Return Value](cyberarkpassword_lookup.md#return-value)

## [Synopsis](cyberarkpassword_lookup.md#id1)

- Get secrets from CyberArk AIM.

## [Requirements](cyberarkpassword_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- CyberArk AIM tool installed

## [Keyword parameters](cyberarkpassword_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.general.cyberarkpassword', key1=value1, key2=value2, ...)` and `query('community.general.cyberarkpassword', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **_command**  string | Cyberark CLI utility.  **Default:** `"/opt/CARKaim/sdk/clipasswordsdk"`  **Configuration:**   - Environment variable: [`AIM_CLIPASSWORDSDK_CMD`](../../environment_variables.md#envvar-AIM_CLIPASSWORDSDK_CMD) |
| **_extra**  string | for extra_params values please check parameters for clipasswordsdk in CyberArk’s “Credential Provider and ASCP Implementation Guide” |
| **appid**  string / required | Defines the unique ID of the application that is issuing the password request. |
| **output**  string | Specifies the desired output fields separated by commas.  They could be: Password, PassProps.<property>, PasswordChangeInProcess  **Default:** `"password"` |
| **query**  string / required | Describes the filter criteria for the password retrieval. |

## [Notes](cyberarkpassword_lookup.md#id4)

> **Note:**
>
> - For Ansible on Windows, please change the -parameters (-p, -d, and -o) to /parameters (/p, /d, and /o) and change the location of CLIPasswordSDK.exe.

## [Examples](cyberarkpassword_lookup.md#id5)

```yaml+jinja
- name: passing options to the lookup
  ansible.builtin.debug:
      msg: '{{ lookup("community.general.cyberarkpassword", cyquery) }}'
  vars:
    cyquery:
      appid: "app_ansible"
      query: "safe=CyberArk_Passwords;folder=root;object=AdminPass"
      output: "Password,PassProps.UserName,PassProps.Address,PasswordChangeInProcess"

- name: used in a loop
  ansible.builtin.debug:
      msg: "{{item}}"
  with_community.general.cyberarkpassword:
      appid: 'app_ansible'
      query: 'safe=CyberArk_Passwords;folder=root;object=AdminPass'
      output: 'Password,PassProps.UserName,PassProps.Address,PasswordChangeInProcess'
```

## [Return Value](cyberarkpassword_lookup.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=dictionary | A list containing one dictionary.  **Returned:** success |
| **passprops**  dictionary | properties assigned to the entry  **Returned:** success |
| **password**  string | The actual value stored  **Returned:** success |
| **passwordchangeinprocess**  string | did the password change?  **Returned:** success |

### Authors

- Unknown

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
