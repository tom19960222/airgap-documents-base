---
collection: ansible
version: "6"
title: "Introduction to modules"
source_url: https://docs.ansible.com/projects/ansible/6/user_guide/modules_intro.html
fetched_at: 2026-07-27T16:40:37+00:00
---
# Introduction to modules

Modules (also referred to as “task plugins” or “library plugins”) are discrete units of code that can be used from the command line or in a playbook task. Ansible executes each module, usually on the remote managed node, and collects return values. In Ansible 2.10 and later, most modules are hosted in collections.

You can execute modules from the command line.

```shell-session
ansible webservers -m service -a "name=httpd state=started"
ansible webservers -m ping
ansible webservers -m command -a "/sbin/reboot -t now"
```

Each module supports taking arguments. Nearly all modules take `key=value` arguments, space delimited. Some modules take no arguments, and the command/shell modules simply take the string of the command you want to run.

From playbooks, Ansible modules are executed in a very similar way.

```yaml
- name: reboot the servers
  command: /sbin/reboot -t now
```

Another way to pass arguments to a module is using YAML syntax, also called ‘complex args’.

```yaml
- name: restart webserver
  service:
    name: httpd
    state: restarted
```

All modules return JSON format data. This means modules can be written in any programming language. Modules should be idempotent, and should avoid making any changes if they detect that the current state matches the desired final state. When used in an Ansible playbook, modules can trigger ‘change events’ in the form of notifying [handlers](playbooks_handlers.md#handlers) to run additional tasks.

You can access the documentation for each module from the command line with the ansible-doc tool.

```shell-session
ansible-doc yum
```

For a list of all available modules, see the [Collection docs](../collections/index.md#list-of-collections), or run the following at a command prompt.

```shell-session
ansible-doc -l
```

> **See also:**
>
> [Introduction to ad hoc commands](intro_adhoc.md#intro-adhoc)
> :   Examples of using modules in /usr/bin/ansible
>
> [Working with playbooks](playbooks.md#working-with-playbooks)
> :   Examples of using modules with /usr/bin/ansible-playbook
>
> [Should you develop a module?](../dev_guide/developing_modules.md#developing-modules)
> :   How to write your own modules
>
> [Python API](../dev_guide/developing_api.md#developing-api)
> :   Examples of using modules with the Python API
>
> [Mailing List](https://groups.google.com/group/ansible-project)
> :   Questions? Help? Ideas? Stop by the list on Google Groups
>
> [Real-time chat](../community/communication.md#communication-irc)
> :   How to join Ansible chat channels
