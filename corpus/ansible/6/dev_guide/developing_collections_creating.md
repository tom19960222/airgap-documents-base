---
collection: ansible
version: "6"
title: "Creating collections"
source_url: https://docs.ansible.com/projects/ansible/6/dev_guide/developing_collections_creating.html
fetched_at: 2026-07-27T16:40:55+00:00
---
# Creating collections

To create a collection:

1. Create a [collection skeleton](developing_collections_creating.md#creating-collections-skeleton) with the `collection init` command.
2. Add modules and other content to the collection.
3. Build the collection into a collection artifact with [ansible-galaxy collection build](developing_collections_distributing.md#building-collections).
4. Publish the collection artifact to Galaxy with [ansible-galaxy collection publish](https://docs.ansible.com/ansible/3/dev_guide/developing_collections.html#publishing-collections "(in Ansible v3)").

A user can then install your collection on their systems.

- [Creating a collection skeleton](developing_collections_creating.md#creating-a-collection-skeleton)

## [Creating a collection skeleton](developing_collections_creating.md#id2)

To start a new collection, run the following command in your collections directory:

```bash
ansible_collections#> ansible-galaxy collection init my_namespace.my_collection
```

> **Note:**
>
> Both the namespace and collection names use the same strict set of requirements. See [Galaxy namespaces](https://galaxy.ansible.com/docs/contributing/namespaces.html#galaxy-namespaces) on the Galaxy docsite for those requirements.

It will create the structure `[my_namespace]/[my_collection]/[collection skeleton]`.
.. hint:: If Git is used for version control, the corresponding repository should be initialized in the collection directory.
Once the skeleton exists, you can populate the directories with the content you want inside the collection. See [ansible-collections](https://github.com/ansible-collections/) GitHub Org to get a better idea of what you can place inside a collection.

Reference: the `ansible-galaxy collection` command

Currently the `ansible-galaxy collection` command implements the following sub commands:

- `init`: Create a basic collection skeleton based on the default template included with Ansible or your own template.
- `build`: Create a collection artifact that can be uploaded to Galaxy or your own repository.
- `publish`: Publish a built collection artifact to Galaxy.
- `install`: Install one or more collections.

To learn more about the `ansible-galaxy` command-line tool, see the [ansible-galaxy](../cli/ansible-galaxy.md#ansible-galaxy) man page.

> **See also:**
>
> [Using collections](../user_guide/collections_using.md#collections)
> :   Learn how to install and use collections.
>
> [Collection structure](developing_collections_structure.md#collection-structure)
> :   Directories and files included in the collection skeleton
>
> [Mailing List](https://groups.google.com/group/ansible-devel)
> :   The development mailing list
>
> [Real-time chat](../community/communication.md#communication-irc)
> :   How to join Ansible chat channels
