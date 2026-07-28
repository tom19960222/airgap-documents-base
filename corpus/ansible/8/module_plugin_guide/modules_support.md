---
collection: ansible
version: "8"
title: "Module maintenance and support"
source_url: https://docs.ansible.com/projects/ansible/8/module_plugin_guide/modules_support.html
fetched_at: 2026-07-28T00:58:39+00:00
---
# Module maintenance and support

If you are using a module and you discover a bug, you may want to know where to report that bug, who is responsible for fixing it, and how you can track changes to the module. If you are a Red Hat subscriber, you may want to know whether you can get support for the issue you are facing.

Starting in Ansible 2.10, most modules live in collections. The distribution method for each collection reflects the maintenance and support for the modules in that collection.

- [Maintenance](modules_support.md#maintenance)
- [Issue Reporting](modules_support.md#issue-reporting)
- [Support](modules_support.md#support)

## [Maintenance](modules_support.md#id2)

| Collection | Code location | Maintained by |
| --- | --- | --- |
| ansible.builtin | [ansible/ansible repo](https://github.com/ansible/ansible/tree/devel/lib/ansible/modules) on GitHub | core team |
| distributed on Galaxy | various; follow `repo` link | community or partners |
| distributed on Automation Hub | various; follow `repo` link | content team or partners |

## [Issue Reporting](modules_support.md#id3)

If you find a bug that affects a plugin in the main Ansible repo, also known as `ansible-core`:

> 1. Confirm that you are running the latest stable version of Ansible or the devel branch.
> 2. Look at the [issue tracker in the Ansible repo](https://github.com/ansible/ansible/issues) to see if an issue has already been filed.
> 3. Create an issue if one does not already exist. Include as much detail as you can about the behavior you discovered.

If you find a bug that affects a plugin in a Galaxy collection:

> 1. Find the collection on Galaxy.
> 2. Find the issue tracker for the collection.
> 3. Look there to see if an issue has already been filed.
> 4. Create an issue if one does not already exist. Include as much detail as you can about the behavior you discovered.

Some partner collections may be hosted in private repositories.

If you are not sure whether the behavior you see is a bug, if you have questions, if you want to discuss development-oriented topics, or if you just want to get in touch, use one of our Google mailing lists or chat channels (using Matrix at ansible.im or using IRC at [irc.libera.chat](https://libera.chat/)) to [communicate with Ansiblers](../community/communication.md#communication).

If you find a bug that affects a module in an Automation Hub collection:

> 1. If the collection offers an Issue Tracker link on Automation Hub, click there and open an issue on the collection repository. If it does not, follow the standard process for reporting issues on the [Red Hat Customer Portal](https://access.redhat.com/). You must have a subscription to the Red Hat Ansible Automation Platform to create an issue on the portal.

## [Support](modules_support.md#id4)

All plugins that remain in `ansible-core` and all collections hosted in Automation Hub are supported by Red Hat. No other plugins or collections are supported by Red Hat. If you have a subscription to the Red Hat Ansible Automation Platform, you can find more information and resources on the [Red Hat Customer Portal.](https://access.redhat.com/)

> **See also:**
>
> [Introduction to ad hoc commands](../command_guide/intro_adhoc.md#intro-adhoc)
> :   Examples of using modules in /usr/bin/ansible
>
> [Working with playbooks](../playbook_guide/playbooks.md#working-with-playbooks)
> :   Examples of using modules with /usr/bin/ansible-playbook
>
> [Mailing List](https://groups.google.com/group/ansible-project)
> :   Questions? Help? Ideas? Stop by the list on Google Groups
>
> [Real-time chat](../community/communication.md#communication-irc)
> :   How to join Ansible chat channels
