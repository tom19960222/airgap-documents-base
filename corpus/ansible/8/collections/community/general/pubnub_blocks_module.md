---
collection: ansible
version: "8"
title: "community.general.pubnub_blocks module – PubNub blocks management module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/pubnub_blocks_module.html
fetched_at: 2026-07-28T01:49:26+00:00
---
# community.general.pubnub_blocks module – PubNub blocks management module

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
> see [Requirements](pubnub_blocks_module.md#ansible-collections-community-general-pubnub-blocks-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.pubnub_blocks`.

- [Synopsis](pubnub_blocks_module.md#synopsis)
- [Requirements](pubnub_blocks_module.md#requirements)
- [Parameters](pubnub_blocks_module.md#parameters)
- [Attributes](pubnub_blocks_module.md#attributes)
- [Examples](pubnub_blocks_module.md#examples)
- [Return Values](pubnub_blocks_module.md#return-values)

## [Synopsis](pubnub_blocks_module.md#id1)

- This module allows Ansible to interface with the PubNub BLOCKS infrastructure by providing the following operations: create / remove, start / stop and rename for blocks and create / modify / remove for event handlers.

Aliases: cloud.pubnub.pubnub_blocks

## [Requirements](pubnub_blocks_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- pubnub_blocks_client >= 1.0

## [Parameters](pubnub_blocks_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account**  string | Name of PubNub account for from which `application` will be used to manage blocks.  User’s account will be used if value not set or empty.  **Default:** `""` |
| **application**  string / required | Name of target PubNub application for which blocks configuration on specific `keyset` will be done. |
| **cache**  dictionary | In case if single play use blocks management module few times it is preferred to enabled ‘caching’ by making previous module to share gathered artifacts and pass them to this parameter.  **Default:** `{}` |
| **changes**  dictionary | List of fields which should be changed by block itself (doesn’t affect any event handlers).  Possible options for change is: `name`.  **Default:** `{}` |
| **description**  string | Short block description which will be later visible on admin.pubnub.com. Used only if block doesn’t exists and won’t change description for existing block. |
| **email**  string | Email from account for which new session should be started.  Not required if `cache` contains result of previous module call (in same play).  **Default:** `""` |
| **event_handlers**  list / elements=dictionary | List of event handlers which should be updated for specified block `name`.  Each entry for new event handler should contain: `name`, `src`, `channels`, `event`. `name` used as event handler name which can be used later to make changes to it.  `src` is full path to file with event handler code.  `channels` is name of channel from which event handler is waiting for events.  `event` is type of event which is able to trigger event handler: `js-before-publish`, `js-after-publish`, `js-after-presence`.  Each entry for existing handlers should contain `name` (so target handler can be identified). Rest parameters (`src`, `channels` and `event`) can be added if changes required for them.  It is possible to rename event handler by adding `changes` key to event handler payload and pass dictionary, which will contain single key `name`, where new name should be passed.  To remove particular event handler it is possible to set `state` for it to `absent` and it will be removed.  **Default:** `[]` |
| **keyset**  string / required | Name of application’s keys set which is bound to managed blocks. |
| **name**  string / required | Name of managed block which will be later visible on admin.pubnub.com. |
| **password**  string | Password which match to account to which specified `email` belong.  Not required if `cache` contains result of previous module call (in same play).  **Default:** `""` |
| **state**  string | Intended block state after event handlers creation / update process will be completed.  **Choices:**   - `"started"` - `"stopped"` - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | This key allow to try skip certificates check when performing REST API calls. Sometimes host may have issues with certificates on it and this will cause problems to call PubNub REST API.  If check should be ignored `false` should be passed to this parameter.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](pubnub_blocks_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](pubnub_blocks_module.md#id5)

```yaml+jinja
# Event handler create example.
- name: Create single event handler
  community.general.pubnub_blocks:
    email: '{{ email }}'
    password: '{{ password }}'
    application: '{{ app_name }}'
    keyset: '{{ keyset_name }}'
    name: '{{ block_name }}'
    event_handlers:
      -
        src: '{{ path_to_handler_source }}'
        name: '{{ handler_name }}'
        event: 'js-before-publish'
        channels: '{{ handler_channel }}'

# Change event handler trigger event type.
- name: Change event handler 'event'
  community.general.pubnub_blocks:
    email: '{{ email }}'
    password: '{{ password }}'
    application: '{{ app_name }}'
    keyset: '{{ keyset_name }}'
    name: '{{ block_name }}'
    event_handlers:
      -
        name: '{{ handler_name }}'
        event: 'js-after-publish'

# Stop block and event handlers.
- name: Stopping block
  community.general.pubnub_blocks:
    email: '{{ email }}'
    password: '{{ password }}'
    application: '{{ app_name }}'
    keyset: '{{ keyset_name }}'
    name: '{{ block_name }}'
    state: stop

# Multiple module calls with cached result passing
- name: Create '{{ block_name }}' block
  register: module_cache
  community.general.pubnub_blocks:
    email: '{{ email }}'
    password: '{{ password }}'
    application: '{{ app_name }}'
    keyset: '{{ keyset_name }}'
    name: '{{ block_name }}'
    state: present
- name: Add '{{ event_handler_1_name }}' handler to '{{ block_name }}'
  register: module_cache
  community.general.pubnub_blocks:
    cache: '{{ module_cache }}'
    application: '{{ app_name }}'
    keyset: '{{ keyset_name }}'
    name: '{{ block_name }}'
    state: present
    event_handlers:
      -
        src: '{{ path_to_handler_1_source }}'
        name: '{{ event_handler_1_name }}'
        channels: '{{ event_handler_1_channel }}'
        event: 'js-before-publish'
- name: Add '{{ event_handler_2_name }}' handler to '{{ block_name }}'
  register: module_cache
  community.general.pubnub_blocks:
    cache: '{{ module_cache }}'
    application: '{{ app_name }}'
    keyset: '{{ keyset_name }}'
    name: '{{ block_name }}'
    state: present
    event_handlers:
      -
        src: '{{ path_to_handler_2_source }}'
        name: '{{ event_handler_2_name }}'
        channels: '{{ event_handler_2_channel }}'
        event: 'js-before-publish'
- name: Start '{{ block_name }}' block
  register: module_cache
  community.general.pubnub_blocks:
    cache: '{{ module_cache }}'
    application: '{{ app_name }}'
    keyset: '{{ keyset_name }}'
    name: '{{ block_name }}'
    state: started
```

## [Return Values](pubnub_blocks_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **module_cache**  dictionary | Cached account information. In case if with single play module used few times it is better to pass cached data to next module calls to speed up process.  **Returned:** always |

### Authors

- PubNub (@pubnub)
- Sergey Mamontov (@parfeon)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
