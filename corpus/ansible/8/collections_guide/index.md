---
collection: ansible
version: "8"
title: "Using Ansible collections"
source_url: https://docs.ansible.com/projects/ansible/8/collections_guide/index.html
fetched_at: 2026-07-28T00:57:44+00:00
---
# Using Ansible collections

> **Note:**
>
> **Making Open Source More Inclusive**
>
> Red Hat is committed to replacing problematic language in our code, documentation, and web properties. We are beginning with these four terms: master, slave, blacklist, and whitelist. We ask that you open an issue or pull request if you come upon a term that we have missed. For more details, see [our CTO Chris Wright’s message](https://www.redhat.com/en/blog/making-open-source-more-inclusive-eradicating-problematic-language).

Welcome to the Ansible guide for working with collections.

Collections are a distribution format for Ansible content that can include playbooks, roles, modules, and plugins.
You can install and use collections through a distribution server, such as Ansible Galaxy, or a Pulp 3 Galaxy server.

- [Installing collections](collections_installing.md)
  - [Installing collections with `ansible-galaxy`](collections_installing.md#installing-collections-with-ansible-galaxy)
  - [Installing collections with signature verification](collections_installing.md#installing-collections-with-signature-verification)
  - [Installing an older version of a collection](collections_installing.md#installing-an-older-version-of-a-collection)
  - [Install multiple collections with a requirements file](collections_installing.md#install-multiple-collections-with-a-requirements-file)
  - [Downloading a collection for offline use](collections_installing.md#downloading-a-collection-for-offline-use)
  - [Installing a collection from source files](collections_installing.md#installing-a-collection-from-source-files)
  - [Installing a collection from a git repository](collections_installing.md#installing-a-collection-from-a-git-repository)
  - [Configuring the `ansible-galaxy` client](collections_installing.md#configuring-the-ansible-galaxy-client)
- [Removing a collection](collections_installing.md#removing-a-collection)
- [Downloading collections](collections_downloading.md)
- [Listing collections](collections_listing.md)
- [Verifying collections](collections_verifying.md)
  - [Verifying collections with `ansible-galaxy`](collections_verifying.md#verifying-collections-with-ansible-galaxy)
  - [Verifying signed collections](collections_verifying.md#verifying-signed-collections)
- [Using collections in a playbook](collections_using_playbooks.md)
  - [Simplifying module names with the `collections` keyword](collections_using_playbooks.md#simplifying-module-names-with-the-collections-keyword)
  - [Using `collections` in roles](collections_using_playbooks.md#using-collections-in-roles)
  - [Using `collections` in playbooks](collections_using_playbooks.md#using-collections-in-playbooks)
  - [Using a playbook from a collection](collections_using_playbooks.md#using-a-playbook-from-a-collection)
- [Collections index](collections_index.md)
