---
collection: ansible
version: "8"
title: "Developing collections"
source_url: https://docs.ansible.com/projects/ansible/8/dev_guide/developing_collections.html
fetched_at: 2026-07-28T00:59:18+00:00
---
# Developing collections

Collections are a distribution format for Ansible content. You can package and distribute playbooks, roles, modules, and plugins using collections. A typical collection addresses a set of related use cases. For example, the `cisco.ios` collection automates management of Cisco IOS devices.

You can create a collection and publish it to [Ansible Galaxy](https://galaxy.ansible.com) or to a private Automation Hub instance. You can publish certified collections to the Red Hat Automation Hub, part of the Red Hat Ansible Automation Platform.

Developing new collections

- [Creating collections](developing_collections_creating.md)
  - [Creating a collection skeleton](developing_collections_creating.md#creating-a-collection-skeleton)
- [Using shared resources in collections](developing_collections_shared.md)
  - [Using documentation fragments in collections](developing_collections_shared.md#using-documentation-fragments-in-collections)
  - [Leveraging optional module utilities in collections](developing_collections_shared.md#leveraging-optional-module-utilities-in-collections)
  - [Listing collection dependencies](developing_collections_shared.md#listing-collection-dependencies)
- [Testing collections](developing_collections_testing.md)
  - [Testing tools](developing_collections_testing.md#testing-tools)
- [Distributing collections](developing_collections_distributing.md)
  - [Initial configuration of your distribution server or servers](developing_collections_distributing.md#initial-configuration-of-your-distribution-server-or-servers)
  - [Building your collection tarball](developing_collections_distributing.md#building-your-collection-tarball)
  - [Preparing to publish your collection](developing_collections_distributing.md#preparing-to-publish-your-collection)
  - [Publishing your collection](developing_collections_distributing.md#publishing-your-collection)
- [Documenting collections](developing_collections_documenting.md)
  - [Documenting modules and plugins](developing_collections_documenting.md#documenting-modules-and-plugins)
  - [Documenting roles](developing_collections_documenting.md#documenting-roles)
  - [Build a docsite with antsibull-docs](developing_collections_documenting.md#build-a-docsite-with-antsibull-docs)

Working with existing collections

- [Migrating Ansible content to a different collection](developing_collections_migrating.md)
  - [Migrating content](developing_collections_migrating.md#migrating-content)
- [Contributing to collections](developing_collections_contributing.md)
  - [Contributing to a collection: community.general](developing_collections_contributing.md#contributing-to-a-collection-community-general)
- [Generating changelogs and porting guide entries in a collection](developing_collections_changelogs.md)
  - [Understanding antsibull-changelog](developing_collections_changelogs.md#understanding-antsibull-changelog)
  - [Including collection changelogs into Ansible](developing_collections_changelogs.md#including-collection-changelogs-into-ansible)

Collections references

- [Collection structure](developing_collections_structure.md)
  - [Collection directories and files](developing_collections_structure.md#collection-directories-and-files)
- [Collection Galaxy metadata structure](collections_galaxy_meta.md)
  - [Structure](collections_galaxy_meta.md#structure)
  - [Examples](collections_galaxy_meta.md#examples)

For instructions on developing modules, see [Developing modules](developing_modules_general.md#developing-modules-general).

> **See also:**
>
> [Using Ansible collections](../collections_guide/index.md#collections)
> :   Learn how to install and use collections in playbooks and roles
>
> [Contributing to Ansible-maintained Collections](../community/contributing_maintained_collections.md#contributing-maintained-collections)
> :   Guidelines for contributing to selected collections
>
> [Ansible Collections Overview and FAQ](https://github.com/ansible-collections/overview/blob/main/README.rst)
> :   Current development status of community collections and FAQ
>
> [Mailing List](https://groups.google.com/group/ansible-devel)
> :   The development mailing list
>
> [Real-time chat](../community/communication.md#communication-irc)
> :   How to join Ansible chat channels
