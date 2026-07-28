---
collection: ansible
version: "8"
title: "Developer Guide"
source_url: https://docs.ansible.com/projects/ansible/8/dev_guide/index.html
fetched_at: 2026-07-28T00:57:49+00:00
---
# Developer Guide

> **Note:**
>
> **Making Open Source More Inclusive**
>
> Red Hat is committed to replacing problematic language in our code, documentation, and web properties. We are beginning with these four terms: master, slave, blacklist, and whitelist. We ask that you open an issue or pull request if you come upon a term that we have missed. For more details, see [our CTO Chris Wright’s message](https://www.redhat.com/en/blog/making-open-source-more-inclusive-eradicating-problematic-language).

Welcome to the Ansible Developer Guide!

**Who should use this guide?**

If you want to extend Ansible by using a custom module or plugin locally, creating a module or plugin, adding functionality to an existing module, or expanding test coverage, this guide is for you. We’ve included detailed information for developers on how to test and document modules, as well as the prerequisites for getting your module or plugin accepted into the main Ansible repository.

Find the task that best describes what you want to do:

- I’m looking for a way to address a use case:

  > - I want to [add a custom plugin or module locally](developing_locally.md#developing-locally).
  > - I want to figure out if [developing a module is the right approach](developing_modules.md#module-dev-should-you) for my use case.
  > - I want to [develop a collection](developing_collections.md#developing-collections).
  > - I want to [contribute to an Ansible-maintained collection](../community/contributing_maintained_collections.md#contributing-maintained-collections).
  > - I want to [contribute to a community-maintained collection](developing_collections_contributing.md#hacking-collections).
  > - I want to [migrate a role to a collection](migrating_roles.md#migrating-roles).
- I’ve read the info above, and I’m sure I want to develop a module:

  > - What do I need to know before I start coding?
  > - I want to [set up my Python development environment](developing_modules_general.md#environment-setup).
  > - I want to [get started writing a module](developing_modules_general.md#developing-modules-general).
  > - I want to write a specific kind of module:
  >   :   - a [network module](../network/dev_guide/developing_plugins_network.md#developing-modules-network)
  >       - a [Windows module](developing_modules_general_windows.md#developing-modules-general-windows).
  >       - an [Amazon module](../collections/amazon/aws/docsite/dev_guidelines.md#ansible-collections-amazon-aws-docsite-dev-guide-intro).
  >       - an oVirt/RHV module.
  >       - a [VMware module](../collections/community/vmware/docsite/dev_guide.md#ansible-collections-community-vmware-docsite-vmware-ansible-devguide).
  > - I want to [write a series of related modules](developing_modules_in_groups.md#developing-modules-in-groups) that integrate Ansible with a new product (for example, a database, cloud provider, network platform, and so on).
- I want to refine my code:

  > - I want to [debug my module code](debugging.md#debugging-modules).
  > - I want to [add tests](testing.md#developing-testing).
  > - I want to [document my module](developing_modules_documenting.md#module-documenting).
  > - I want to [document my set of modules for a network platform](../network/dev_guide/documenting_modules_network.md#documenting-modules-network).
  > - I want to follow [conventions and tips for clean, usable module code](developing_modules_best_practices.md#developing-modules-best-practices).
  > - I want to [make sure my code runs on Python 2 and Python 3](developing_python_3.md#developing-python-3).
- I want to work on other development projects:

  > - I want to [write a plugin](developing_plugins.md#developing-plugins).
  > - I want to [connect Ansible to a new source of inventory](developing_inventory.md#developing-inventory).
  > - I want to [deprecate an outdated module](module_lifecycle.md#deprecating-modules).
- I want to contribute back to the Ansible project:

  - I want to [understand how to contribute to Ansible](../community/index.md#ansible-community-guide).
  - I want to [contribute my module or plugin](developing_modules_checklist.md#developing-modules-checklist).
  - I want to [understand the DCO agreement](../community/developer_certificate_of_origin.md#developer-certificate-of-origin) for contributions to the [Ansible Core](https://github.com/ansible/ansible) and [Ansible Documentation](https://github.com/ansible/ansible-documentation) repositories.

If you prefer to read the entire guide, here’s a list of the pages in order.

- [Adding modules and plugins locally](developing_locally.md)
  - [Modules and plugins: what is the difference?](developing_locally.md#modules-and-plugins-what-is-the-difference)
  - [Adding modules and plugins in collections](developing_locally.md#adding-modules-and-plugins-in-collections)
  - [Adding a module or plugin outside of a collection](developing_locally.md#adding-a-module-or-plugin-outside-of-a-collection)
  - [Adding a non-module plugin locally outside of a collection](developing_locally.md#adding-a-non-module-plugin-locally-outside-of-a-collection)
  - [Using `ansible.legacy` to access custom versions of an `ansible.builtin` module](developing_locally.md#using-ansible-legacy-to-access-custom-versions-of-an-ansible-builtin-module)
- [Should you develop a module?](developing_modules.md)
- [Developing modules](developing_modules_general.md)
  - [Preparing an environment for developing Ansible modules](developing_modules_general.md#preparing-an-environment-for-developing-ansible-modules)
  - [Creating a module](developing_modules_general.md#creating-a-module)
  - [Creating an info or a facts module](developing_modules_general.md#creating-an-info-or-a-facts-module)
  - [Verifying your module code](developing_modules_general.md#verifying-your-module-code)
  - [Testing your newly-created module](developing_modules_general.md#testing-your-newly-created-module)
  - [Contributing back to Ansible](developing_modules_general.md#contributing-back-to-ansible)
  - [Communication and development support](developing_modules_general.md#communication-and-development-support)
  - [Credit](developing_modules_general.md#credit)
- [Contributing your module to an existing Ansible collection](developing_modules_checklist.md)
  - [Contributing modules: objective requirements](developing_modules_checklist.md#contributing-modules-objective-requirements)
  - [Contributing to Ansible: subjective requirements](developing_modules_checklist.md#contributing-to-ansible-subjective-requirements)
  - [Other checklists](developing_modules_checklist.md#other-checklists)
- [Conventions, tips, and pitfalls](developing_modules_best_practices.md)
  - [Scoping your module(s)](developing_modules_best_practices.md#scoping-your-module-s)
  - [Designing module interfaces](developing_modules_best_practices.md#designing-module-interfaces)
  - [General guidelines & tips](developing_modules_best_practices.md#general-guidelines-tips)
  - [Functions and Methods](developing_modules_best_practices.md#functions-and-methods)
  - [Python tips](developing_modules_best_practices.md#python-tips)
  - [Importing and using shared code](developing_modules_best_practices.md#importing-and-using-shared-code)
  - [Handling module failures](developing_modules_best_practices.md#handling-module-failures)
  - [Handling exceptions (bugs) gracefully](developing_modules_best_practices.md#handling-exceptions-bugs-gracefully)
  - [Creating correct and informative module output](developing_modules_best_practices.md#creating-correct-and-informative-module-output)
  - [Following Ansible conventions](developing_modules_best_practices.md#following-ansible-conventions)
  - [Module Security](developing_modules_best_practices.md#module-security)
- [Ansible and Python 3](developing_python_3.md)
  - [Minimum version of Python 3.x and Python 2.x](developing_python_3.md#minimum-version-of-python-3-x-and-python-2-x)
  - [Developing Ansible code that supports Python 2 and Python 3](developing_python_3.md#developing-ansible-code-that-supports-python-2-and-python-3)
- [Debugging modules](debugging.md)
  - [Detailed debugging steps](debugging.md#detailed-debugging-steps)
  - [Simple debugging](debugging.md#simple-debugging)
- [Module format and documentation](developing_modules_documenting.md)
  - [Python shebang & UTF-8 coding](developing_modules_documenting.md#python-shebang-utf-8-coding)
  - [Copyright and license](developing_modules_documenting.md#copyright-and-license)
  - [ANSIBLE_METADATA block](developing_modules_documenting.md#ansible-metadata-block)
  - [DOCUMENTATION block](developing_modules_documenting.md#documentation-block)
  - [EXAMPLES block](developing_modules_documenting.md#examples-block)
  - [RETURN block](developing_modules_documenting.md#return-block)
  - [Python imports](developing_modules_documenting.md#python-imports)
  - [Testing module documentation](developing_modules_documenting.md#testing-module-documentation)
- [Adjacent YAML documentation files](sidecar.md)
  - [YAML documentation for plugins](sidecar.md#yaml-documentation-for-plugins)
  - [YAML format](sidecar.md#yaml-format)
  - [Supported plugin types](sidecar.md#supported-plugin-types)
- [Windows module development walkthrough](developing_modules_general_windows.md)
  - [Windows environment setup](developing_modules_general_windows.md#windows-environment-setup)
  - [Create a Windows server in a VM](developing_modules_general_windows.md#create-a-windows-server-in-a-vm)
  - [Create an Ansible inventory](developing_modules_general_windows.md#create-an-ansible-inventory)
  - [Provisioning the environment](developing_modules_general_windows.md#provisioning-the-environment)
  - [Windows new module development](developing_modules_general_windows.md#windows-new-module-development)
  - [Windows module utilities](developing_modules_general_windows.md#windows-module-utilities)
  - [Windows playbook module testing](developing_modules_general_windows.md#windows-playbook-module-testing)
  - [Windows debugging](developing_modules_general_windows.md#windows-debugging)
  - [Windows unit testing](developing_modules_general_windows.md#windows-unit-testing)
  - [Windows integration testing](developing_modules_general_windows.md#windows-integration-testing)
  - [Windows communication and development support](developing_modules_general_windows.md#windows-communication-and-development-support)
- [Creating a new collection](developing_modules_in_groups.md)
  - [Before you start coding](developing_modules_in_groups.md#before-you-start-coding)
  - [Naming conventions](developing_modules_in_groups.md#naming-conventions)
  - [Speak to us](developing_modules_in_groups.md#speak-to-us)
  - [Where to get support](developing_modules_in_groups.md#where-to-get-support)
  - [Required files](developing_modules_in_groups.md#required-files)
  - [New to git or GitHub](developing_modules_in_groups.md#new-to-git-or-github)
- [Testing Ansible](testing.md)
  - [Why test your Ansible contributions?](testing.md#why-test-your-ansible-contributions)
  - [Types of tests](testing.md#types-of-tests)
  - [Testing within GitHub & Azure Pipelines](testing.md#testing-within-github-azure-pipelines)
  - [How to test a PR](testing.md#how-to-test-a-pr)
  - [Want to know more about testing?](testing.md#want-to-know-more-about-testing)
- [The lifecycle of an Ansible module or plugin](module_lifecycle.md)
  - [Deprecating modules and plugins in the Ansible main repository](module_lifecycle.md#deprecating-modules-and-plugins-in-the-ansible-main-repository)
  - [Deprecating modules and plugins in a collection](module_lifecycle.md#deprecating-modules-and-plugins-in-a-collection)
  - [Changing a module or plugin name in the Ansible main repository](module_lifecycle.md#changing-a-module-or-plugin-name-in-the-ansible-main-repository)
  - [Renaming a module or plugin in a collection, or redirecting a module or plugin to another collection](module_lifecycle.md#renaming-a-module-or-plugin-in-a-collection-or-redirecting-a-module-or-plugin-to-another-collection)
  - [Tombstoning a module or plugin in a collection](module_lifecycle.md#tombstoning-a-module-or-plugin-in-a-collection)
- [Developing plugins](developing_plugins.md)
  - [Writing plugins in Python](developing_plugins.md#writing-plugins-in-python)
  - [Raising errors](developing_plugins.md#raising-errors)
  - [String encoding](developing_plugins.md#string-encoding)
  - [Plugin configuration & documentation standards](developing_plugins.md#plugin-configuration-documentation-standards)
  - [Developing particular plugin types](developing_plugins.md#developing-particular-plugin-types)
- [Developing dynamic inventory](developing_inventory.md)
  - [Inventory sources](developing_inventory.md#inventory-sources)
  - [Inventory plugins](developing_inventory.md#inventory-plugins)
  - [Inventory scripts](developing_inventory.md#developing-inventory-scripts)
- [Developing `ansible-core`](developing_core.md)
  - [`ansible-core` project branches and tags](core_branches_and_tags.md)
  - [Ansible module architecture](developing_program_flow_modules.md)
- [Ansible module architecture](developing_program_flow_modules.md)
  - [Types of modules](developing_program_flow_modules.md#types-of-modules)
  - [How modules are executed](developing_program_flow_modules.md#how-modules-are-executed)
- [Python API](developing_api.md)
  - [Python API example](developing_api.md#python-api-example)
- [Rebasing a pull request](developing_rebasing.md)
  - [Configuring your remotes](developing_rebasing.md#configuring-your-remotes)
  - [Rebasing your branch](developing_rebasing.md#rebasing-your-branch)
  - [Updating your pull request](developing_rebasing.md#updating-your-pull-request)
  - [Getting help rebasing](developing_rebasing.md#getting-help-rebasing)
- [Using and developing module utilities](developing_module_utilities.md)
  - [Naming and finding module utilities](developing_module_utilities.md#naming-and-finding-module-utilities)
  - [Standard module utilities](developing_module_utilities.md#standard-module-utilities)
- [Developing collections](developing_collections.md)
  - [Creating collections](developing_collections_creating.md)
  - [Using shared resources in collections](developing_collections_shared.md)
  - [Testing collections](developing_collections_testing.md)
  - [Distributing collections](developing_collections_distributing.md)
  - [Documenting collections](developing_collections_documenting.md)
  - [Migrating Ansible content to a different collection](developing_collections_migrating.md)
  - [Contributing to collections](developing_collections_contributing.md)
  - [Generating changelogs and porting guide entries in a collection](developing_collections_changelogs.md)
  - [Collection structure](developing_collections_structure.md)
  - [Collection Galaxy metadata structure](collections_galaxy_meta.md)
- [Migrating Roles to Roles in Collections on Galaxy](migrating_roles.md)
  - [Comparing standalone roles to collection roles](migrating_roles.md#comparing-standalone-roles-to-collection-roles)
  - [Migrating a role to a collection](migrating_roles.md#migrating-a-role-to-a-collection)
  - [Migrating a role that contains plugins to a collection](migrating_roles.md#migrating-a-role-that-contains-plugins-to-a-collection)
  - [Using `ansible.legacy` to access local custom modules from collections-based roles](migrating_roles.md#using-ansible-legacy-to-access-local-custom-modules-from-collections-based-roles)
- [Collection Galaxy metadata structure](collections_galaxy_meta.md)
  - [Structure](collections_galaxy_meta.md#structure)
  - [Examples](collections_galaxy_meta.md#examples)
- [Ansible architecture](overview_architecture.md)
  - [Modules](overview_architecture.md#modules)
  - [Module utilities](overview_architecture.md#module-utilities)
  - [Plugins](overview_architecture.md#plugins)
  - [Inventory](overview_architecture.md#inventory)
  - [Playbooks](overview_architecture.md#playbooks)
  - [The Ansible search path](overview_architecture.md#the-ansible-search-path)
