---
collection: ansible
version: "8"
title: "community.rabbitmq.rabbitmq_user module – Manage RabbitMQ users"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/rabbitmq/rabbitmq_user_module.html
fetched_at: 2026-07-28T01:58:55+00:00
---
# community.rabbitmq.rabbitmq_user module – Manage RabbitMQ users

> **Note:**
>
> This module is part of the [community.rabbitmq collection](https://galaxy.ansible.com/ui/repo/published/community/rabbitmq/) (version 1.2.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.rabbitmq`.
>
> To use it in a playbook, specify: `community.rabbitmq.rabbitmq_user`.

- [Synopsis](rabbitmq_user_module.md#synopsis)
- [Parameters](rabbitmq_user_module.md#parameters)
- [Examples](rabbitmq_user_module.md#examples)

## [Synopsis](rabbitmq_user_module.md#id1)

- Add or remove users to RabbitMQ and assign permissions

## [Parameters](rabbitmq_user_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **configure_priv**  string | Regular expression to restrict configure actions on a resource for the specified vhost.  By default all actions are restricted.  This option will be ignored when permissions option is used.  **Default:** `"^$"` |
| **force**  boolean | Deletes and recreates the user.  **Choices:**   - `false` ← (default) - `true` |
| **node**  string | erlang node name of the rabbit we wish to configure  **Default:** `"rabbit"` |
| **password**  string | Password of user to add.  To change the password of an existing user, you must also specify `update_password=always`. |
| **permissions**  list / elements=dictionary | a list of dicts, each dict contains vhost, configure_priv, write_priv, and read_priv, and represents a permission rule for that vhost.  This option should be preferable when you care about all permissions of the user.  You should use vhost, configure_priv, write_priv, and read_priv options instead if you care about permissions for just some vhosts.  **Default:** `[]` |
| **read_priv**  string | Regular expression to restrict configure actions on a resource for the specified vhost.  By default all actions are restricted.  This option will be ignored when permissions option is used.  **Default:** `"^$"` |
| **state**  string | Specify if user is to be added or removed  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  string | User tags specified as comma delimited |
| **topic_permissions**  list / elements=dictionary  *added in community.rabbitmq 1.2.0* | A list of dicts, each dict contains vhost, exchange, read_priv and write_priv, and represents a topic permission rule for that vhost.  By default vhost is `/` and exchange is `amq.topic`.  Supported since RabbitMQ 3.7.0. If RabbitMQ is older and topic_permissions are set, the module will fail.  **Default:** `[]` |
| **update_password**  string | `on_create` will only set the password for newly created users. `always` will update passwords if they differ.  **Choices:**   - `"on_create"` ← (default) - `"always"` |
| **user**  aliases: username, name  string / required | Name of user to add |
| **vhost**  string | vhost to apply access privileges.  This option will be ignored when permissions option is used.  **Default:** `"/"` |
| **write_priv**  string | Regular expression to restrict configure actions on a resource for the specified vhost.  By default all actions are restricted.  This option will be ignored when permissions option is used.  **Default:** `"^$"` |

## [Examples](rabbitmq_user_module.md#id3)

```yaml+jinja
- name: |-
    Add user to server and assign full access control on / vhost.
    The user might have permission rules for other vhost but you don't care.
  community.rabbitmq.rabbitmq_user:
    user: joe
    password: changeme
    vhost: /
    configure_priv: .*
    read_priv: .*
    write_priv: .*
    state: present

- name: |-
    Add user to server and assign full access control on / vhost.
    The user doesn't have permission rules for other vhosts
  community.rabbitmq.rabbitmq_user:
    user: joe
    password: changeme
    permissions:
      - vhost: /
        configure_priv: .*
        read_priv: .*
        write_priv: .*
    state: present

- name: |-
    Add user to server and assign some topic permissions on / vhost.
    The user doesn't have topic permission rules for other vhosts
  community.rabbitmq.rabbitmq_user:
    user: joe
    password: changeme
    topic_permissions:
      - vhost: /
        exchange: amq.topic
        read_priv: .*
        write_priv: 'prod\\.logging\\..*'
    state: present
```

### Authors

- Chris Hoffman (@chrishoffman)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.rabbitmq/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.rabbitmq)
