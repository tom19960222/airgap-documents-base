---
collection: ansible
version: "8"
title: "Ansible 2.3 Porting Guide"
source_url: https://docs.ansible.com/projects/ansible/8/porting_guides/porting_guide_2.3.html
fetched_at: 2026-07-28T00:58:26+00:00
---
# [Ansible 2.3 Porting Guide](porting_guide_2.3.md#id1)

This section discusses the behavioral changes between Ansible 2.2 and Ansible 2.3.

It is intended to assist in updating your playbooks, plugins and other parts of your Ansible infrastructure so they will work with this version of Ansible.

We suggest you read this page along with [Ansible Changelog for 2.3](https://github.com/ansible/ansible/blob/stable-2.3/CHANGELOG.md) to understand what updates you may need to make.

This document is part of a collection on porting. The complete list of porting guides can be found at [porting guides](porting_guides.md#porting-guides).

Topics

- [Ansible 2.3 Porting Guide](porting_guide_2.3.md#ansible-2-3-porting-guide)

  - [Playbook](porting_guide_2.3.md#playbook)

    - [Restructured async to work with action plugins](porting_guide_2.3.md#restructured-async-to-work-with-action-plugins)
    - [OpenBSD version facts](porting_guide_2.3.md#openbsd-version-facts)
    - [Names Blocks](porting_guide_2.3.md#names-blocks)
    - [Use of multiple tags](porting_guide_2.3.md#use-of-multiple-tags)
    - [Other caveats](porting_guide_2.3.md#other-caveats)
  - [Modules](porting_guide_2.3.md#modules)

    - [Modules removed](porting_guide_2.3.md#modules-removed)
    - [Deprecation notices](porting_guide_2.3.md#deprecation-notices)
    - [Noteworthy module changes](porting_guide_2.3.md#noteworthy-module-changes)

      - [AWS lambda](porting_guide_2.3.md#aws-lambda)
      - [Mount](porting_guide_2.3.md#mount)
  - [Plugins](porting_guide_2.3.md#plugins)
  - [Porting custom scripts](porting_guide_2.3.md#porting-custom-scripts)
  - [Networking](porting_guide_2.3.md#networking)

    - [Deprecation of top-level connection arguments](porting_guide_2.3.md#deprecation-of-top-level-connection-arguments)
    - [ProxyCommand replaces delegate_to](porting_guide_2.3.md#proxycommand-replaces-delegate-to)

## [Playbook](porting_guide_2.3.md#id2)

### [Restructured async to work with action plugins](porting_guide_2.3.md#id3)

In Ansible 2.2 (and possibly earlier) the async: keyword could not be used in conjunction with the action plugins such as service. This limitation has been removed in Ansible 2.3

**NEW** In Ansible 2.3:

```yaml
- name: Install nginx asynchronously
  service:
    name: nginx
    state: restarted
  async: 45
```

### [OpenBSD version facts](porting_guide_2.3.md#id4)

The ansible_distribution_release and ansible_distribution_version facts on OpenBSD hosts were reversed in Ansible 2.2 and earlier. This has been changed so that version has the numeric portion and release has the name of the release.

**OLD** In Ansible 2.2 (and earlier)

```bash
"ansible_distribution": "OpenBSD"
"ansible_distribution_release": "6.0",
"ansible_distribution_version": "release",
```

**NEW** In Ansible 2.3:

```bash
"ansible_distribution": "OpenBSD",
"ansible_distribution_release": "release",
"ansible_distribution_version": "6.0",
```

### [Names Blocks](porting_guide_2.3.md#id5)

Blocks can now have names, this allows you to avoid the ugly # this block is for… comments.

**NEW** In Ansible 2.3:

```yaml
- name: Block test case
  hosts: localhost
  tasks:
   - name: Attempt to setup foo
     block:
       - debug: msg='I execute normally'
       - command: /bin/false
       - debug: msg='I never execute, cause ERROR!'
     rescue:
       - debug: msg='I caught an error'
       - command: /bin/false
       - debug: msg='I also never execute :-('
     always:
       - debug: msg="this always executes"
```

### [Use of multiple tags](porting_guide_2.3.md#id6)

Specifying `--tags` (or `--skip-tags`) multiple times on the command line currently leads to the last specified tag overriding all the other specified tags. This behaviour is deprecated. In the future, if you specify –tags multiple times the tags will be merged together. From now on, using `--tags` multiple times on one command line will emit a deprecation warning. Setting the `merge_multiple_cli_tags` option to True in the `ansible.cfg` file will enable the new behaviour.

In 2.4, the default will be to merge the tags. You can enable the old overwriting behavior through the config option.
In 2.5, multiple `--tags` options will be merged with no way to go back to the old behaviour.

### [Other caveats](porting_guide_2.3.md#id7)

Here are some rare cases that might be encountered when updating. These are mostly caused by the more stringent parser validation and the capture of errors that were previously ignored.

- Made `any_errors_fatal` inheritable from play to task and all other objects in between.

## [Modules](porting_guide_2.3.md#id8)

No major changes in this version.

### [Modules removed](porting_guide_2.3.md#id9)

No major changes in this version.

### [Deprecation notices](porting_guide_2.3.md#id10)

The following modules will be removed in Ansible 2.5. Please update your playbooks accordingly.

- ec2_vpc
- cl_bond
- cl_bridge
- cl_img_install
- cl_interface
- cl_interface_policy
- cl_license
- cl_ports
- nxos_mtu use [nxos_system](https://docs.ansible.com/ansible/2.9/modules/nxos_system_module.html#nxos-system-module "(in Ansible v2.9)") instead

> **Note:**
>
> These modules may no longer have documentation in the current release. Please see the
> [Ansible 2.3 module documentation](https://docs.ansible.com/ansible/2.3/list_of_all_modules.html) if you need
> to know how they worked for porting your playbooks.

### [Noteworthy module changes](porting_guide_2.3.md#id11)

#### [AWS lambda](porting_guide_2.3.md#id12)

Previously ignored changes that only affected one parameter. Existing deployments may have outstanding changes that this bug fix will apply.

#### [Mount](porting_guide_2.3.md#id13)

Mount: Some fixes so bind mounts are not mounted each time the playbook runs.

## [Plugins](porting_guide_2.3.md#id14)

No major changes in this version.

## [Porting custom scripts](porting_guide_2.3.md#id15)

No major changes in this version.

## [Networking](porting_guide_2.3.md#id16)

There have been a number of changes to number of changes to how Networking Modules operate.

Playbooks should still use `connection: local`.

The following changes apply to:

- dellos6
- dellos9
- dellos10
- eos
- ios
- iosxr
- junos
- sros
- vyos

### [Deprecation of top-level connection arguments](porting_guide_2.3.md#id17)

**OLD** In Ansible 2.2:

```yaml
- name: example of using top-level options for connection properties
  ios_command:
    commands: show version
    host: "{{ inventory_hostname }}"
    username: cisco
    password: cisco
    authorize: yes
    auth_pass: cisco
```

Will result in:

```bash
[WARNING]: argument username has been deprecated and will be removed in a future version
[WARNING]: argument host has been deprecated and will be removed in a future version
[WARNING]: argument password has been deprecated and will be removed in a future version
```

**NEW** In Ansible 2.3:

```yaml
- name: Gather facts
  eos_facts:
    gather_subset: all
    provider:
      username: myuser
      password: "{{ networkpassword }}"
      transport: cli
      host: "{{ ansible_host }}"
```

### [ProxyCommand replaces delegate_to](porting_guide_2.3.md#id18)

The new connection framework for Network Modules in Ansible 2.3 that uses `cli` transport
no longer supports the use of the `delegate_to` directive.
In order to use a bastion or intermediate jump host to connect to network devices over `cli`
transport, network modules now support the use of `ProxyCommand`.

To use `ProxyCommand` configure the proxy settings in the Ansible inventory
file to specify the proxy host through `ansible_ssh_common_args`.

For details on how to do this see the [network proxy guide](../network/user_guide/network_debug_troubleshooting.md#network-delegate-to-vs-proxycommand).
