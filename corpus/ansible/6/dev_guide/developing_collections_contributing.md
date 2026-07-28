---
collection: ansible
version: "6"
title: "Contributing to collections"
source_url: https://docs.ansible.com/projects/ansible/6/dev_guide/developing_collections_contributing.html
fetched_at: 2026-07-27T16:40:54+00:00
---
# Contributing to collections

If you want to add functionality to an existing collection, modify a collection you are using to fix a bug, or change the behavior of a module in a collection, clone the git repository for that collection and make changes on a branch. You can combine changes to a collection with a local checkout of Ansible (`source hacking/env-setup`).
You should first check the collection repository to see if it has specific contribution guidelines. These are typically listed in the README.md or CONTRIBUTING.md files within the repository.

## Contributing to a collection: community.general

These instructions apply to collections hosted in the [ansible_collections GitHub organization](https://github.com/ansible-collections). For other collections, especially for collections not hosted on GitHub, check the `README.md` of the collection for information on contributing to it.

This example uses the [community.general collection](https://github.com/ansible-collections/community.general/). To contribute to other collections in the same GitHub org, replace the folder names `community` and `general` with the namespace and collection name of a different collection.

### Prerequisites

- Include `~/dev/ansible/collections/` in [COLLECTIONS_PATHS](../reference_appendices/config.md#collections-paths)
- If that path mentions multiple directories, make sure that no other directory earlier in the search path contains a copy of `community.general`.

### Creating a PR

- Create the directory `~/dev/ansible/collections/ansible_collections/community`:

```shell
mkdir -p ~/dev/ansible/collections/ansible_collections/community
```

- Clone [the community.general Git repository](https://github.com/ansible-collections/community.general/) or a fork of it into the directory `general`:

```shell
cd ~/dev/ansible/collections/ansible_collections/community
git clone git@github.com:ansible-collections/community.general.git general
```

- If you clone from a fork, add the original repository as a remote `upstream`:

```shell
cd ~/dev/ansible/collections/ansible_collections/community/general
git remote add upstream git@github.com:ansible-collections/community.general.git
```

- Create a branch and commit your changes on the branch.
- Remember to add tests for your changes, see [Testing collections](developing_collections_testing.md#testing-collections).
- Push your changes to your fork of the collection and create a Pull Request.

You can test your changes by using this checkout of `community.general` in playbooks and roles with whichever version of Ansible you have installed locally, including a local checkout of `ansible/ansible`’s `devel` branch.

> **See also:**
>
> [Using collections](../user_guide/collections_using.md#collections)
> :   Learn how to install and use collections.
>
> [Contributing to Ansible-maintained Collections](../community/contributing_maintained_collections.md#contributing-maintained-collections)
> :   Guidelines for contributing to selected collections
>
> [Mailing List](https://groups.google.com/group/ansible-devel)
> :   The development mailing list
>
> [Real-time chat](../community/communication.md#communication-irc)
> :   How to join Ansible chat channels
