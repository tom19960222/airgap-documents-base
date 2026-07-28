---
collection: ansible
version: "6"
title: "Ansible concepts"
source_url: https://docs.ansible.com/projects/ansible/6/user_guide/basic_concepts.html
fetched_at: 2026-07-27T16:40:14+00:00
---
# Ansible concepts

These concepts are common to all uses of Ansible. You need to understand them to use Ansible for any kind of automation. This basic introduction provides the background you need to follow the rest of the User Guide.

- [Control node](basic_concepts.md#control-node)
- [Managed nodes](basic_concepts.md#managed-nodes)
- [Inventory](basic_concepts.md#inventory)
- [Playbooks](basic_concepts.md#playbooks)

  - [Plays](basic_concepts.md#plays)

    - [Roles](basic_concepts.md#roles)
    - [Tasks](basic_concepts.md#tasks)
    - [Handlers](basic_concepts.md#handlers)
- [Modules](basic_concepts.md#modules)
- [Plugins](basic_concepts.md#plugins)
- [Collections](basic_concepts.md#collections)
- [AAP](basic_concepts.md#aap)

## [Control node](basic_concepts.md#id1)

The machine from which you run the Ansible CLI tools (`ansible-playbook` , `ansible`, `ansible-vault` and others).
You can use any computer that meets the software requirements as a control node - laptops, shared desktops, and servers can all run Ansible.
Multiple control nodes are possible, but Ansible itself does not coordinate across them, see `AAP` for such features.

## [Managed nodes](basic_concepts.md#id2)

Also referred to as ‘hosts’, these are the target devices (servers, network appliances or any computer) you aim to manage with Ansible.
Ansible is not normally installed on managed nodes, unless you are using `ansible-pull`, but this is rare and not the recommended setup.

## [Inventory](basic_concepts.md#id3)

A list of managed nodes provided by one or more ‘inventory sources’. Your inventory can specify information specific to each node, like IP address.
It is also used for assigning groups, that both allow for node selection in the Play and bulk variable assignment.
To learn more about inventory, see [the Working with Inventory](intro_inventory.md#intro-inventory) section. Sometimes an inventory source file is also referred to as a ‘hostfile’.

## [Playbooks](basic_concepts.md#id4)

They contain Plays (which are the basic unit of Ansible execution). This is both an ‘execution concept’ and how we describe the files on which `ansible-playbook` operates.
Playbooks are written in YAML and are easy to read, write, share and understand. To learn more about playbooks, see [Intro to playbooks](playbooks_intro.md#about-playbooks).

### [Plays](basic_concepts.md#id5)

The main context for Ansible execution, this playbook object maps managed nodes (hosts) to tasks.
The Play contains variables, roles and an ordered lists of tasks and can be run repeatedly.
It basically consists of an implicit loop over the mapped hosts and tasks and defines how to iterate over them.

#### [Roles](basic_concepts.md#id6)

A limited distribution of reusable Ansible content (tasks, handlers, variables, plugins, templates and files) for use inside of a Play.
To use any Role resource, the Role itself must be imported into the Play.

#### [Tasks](basic_concepts.md#id7)

The definition of an ‘action’ to be applied to the managed host. Tasks must always be contained in a Play, directly or indirectly (Role, or imported/included task list file).
You can execute a single task once with an ad hoc command using `ansible` or `ansible-console` (both create a virtual Play).

#### [Handlers](basic_concepts.md#id8)

A special form of a Task, that only executes when notified by a previous task which resulted in a ‘changed’ status.

## [Modules](basic_concepts.md#id9)

The code or binaries that Ansible copies to and executes on each managed node (when needed) to accomplish the action defined in each Task.
Each module has a particular use, from administering users on a specific type of database to managing VLAN interfaces on a specific type of network device.
You can invoke a single module with a task, or invoke several different modules in a playbook.
Ansible modules are grouped in collections. For an idea of how many collections Ansible includes, see the [Collection Index](../collections/index.md#list-of-collections).

## [Plugins](basic_concepts.md#id10)

Pieces of code that expand Ansible’s core capabilities, they can control how you connect to a managed node (connection plugins),
manipulate data (filter plugins) and even control what is displayed in the console (callback plugins).
See [Working with plugins](../plugins/plugins.md#working-with-plugins) for details.

## [Collections](basic_concepts.md#id11)

A format in which Ansible content is distributed that can contain playbooks, roles, modules, and plugins. You can install and use collections through [Ansible Galaxy](https://galaxy.ansible.com). To learn more about collections, see [Using collections](collections_using.md#collections). Collection resources can be used independently and discretely from each other.

## [AAP](basic_concepts.md#id12)

Short for ‘Ansible Automation Platform’. This is a product that includes enterprise level features and integrates many tools of the Ansible ecosystem: ansible-core, awx, galaxyNG, and so on.
