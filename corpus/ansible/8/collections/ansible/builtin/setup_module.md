---
collection: ansible
version: "8"
title: "ansible.builtin.setup module – Gathers facts about remote hosts"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/setup_module.html
fetched_at: 2026-07-28T01:04:00+00:00
---
# ansible.builtin.setup module – Gathers facts about remote hosts

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `setup` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.setup` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](setup_module.md#synopsis)
- [Parameters](setup_module.md#parameters)
- [Attributes](setup_module.md#attributes)
- [Notes](setup_module.md#notes)
- [Examples](setup_module.md#examples)

## [Synopsis](setup_module.md#id1)

- This module is automatically called by playbooks to gather useful variables about remote hosts that can be used in playbooks. It can also be executed directly by `/usr/bin/ansible` to check what variables are available to a host. Ansible provides many *facts* about the system, automatically.
- This module is also supported for Windows targets.

## [Parameters](setup_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **fact_path**  path | Path used for local ansible facts (`*.fact`) - files in this dir will be run (if executable) and their results be added to `ansible_local` facts. If a file is not executable it is read instead. File/results format can be JSON or INI-format. The default `fact_path` can be specified in `ansible.cfg` for when setup is automatically called as part of `gather_facts`. NOTE - For windows clients, the results will be added to a variable named after the local file (without extension suffix), rather than `ansible_local`.  Since Ansible 2.1, Windows hosts can use `fact_path`. Make sure that this path exists on the target host. Files in this path MUST be PowerShell scripts `.ps1` which outputs an object. This object will be formatted by Ansible as json so the script should be outputting a raw hashtable, array, or other primitive object.  **Default:** `"/etc/ansible/facts.d"` |
| **filter**  list / elements=string | If supplied, only return facts that match one of the shell-style (fnmatch) pattern. An empty list basically means ‘no filter’. As of Ansible 2.11, the type has changed from string to list and the default has became an empty list. A simple string is still accepted and works as a single pattern. The behaviour prior to Ansible 2.11 remains.  **Default:** `[]` |
| **gather_subset**  list / elements=string | If supplied, restrict the additional facts collected to the given subset. Possible values: `all`, `all_ipv4_addresses`, `all_ipv6_addresses`, `apparmor`, `architecture`, `caps`, `chroot`,`cmdline`, `date_time`, `default_ipv4`, `default_ipv6`, `devices`, `distribution`, `distribution_major_version`, `distribution_release`, `distribution_version`, `dns`, `effective_group_ids`, `effective_user_id`, `env`, `facter`, `fips`, `hardware`, `interfaces`, `is_chroot`, `iscsi`, `kernel`, `local`, `lsb`, `machine`, `machine_id`, `mounts`, `network`, `ohai`, `os_family`, `pkg_mgr`, `platform`, `processor`, `processor_cores`, `processor_count`, `python`, `python_version`, `real_user_id`, `selinux`, `service_mgr`, `ssh_host_key_dsa_public`, `ssh_host_key_ecdsa_public`, `ssh_host_key_ed25519_public`, `ssh_host_key_rsa_public`, `ssh_host_pub_keys`, `ssh_pub_keys`, `system`, `system_capabilities`, `system_capabilities_enforced`, `user`, `user_dir`, `user_gecos`, `user_gid`, `user_id`, `user_shell`, `user_uid`, `virtual`, `virtualization_role`, `virtualization_type`. Can specify a list of values to specify a larger subset. Values can also be used with an initial `!` to specify that that specific subset should not be collected. For instance: `!hardware,!network,!virtual,!ohai,!facter`. If `!all` is specified then only the min subset is collected. To avoid collecting even the min subset, specify `!all,!min`. To collect only specific facts, use `!all,!min`, and specify the particular fact subsets. Use the filter parameter if you do not want to display some collected facts.  **Default:** `["all"]` |
| **gather_timeout**  integer | Set the default timeout in seconds for individual fact gathering.  **Default:** `10` |

## [Attributes](setup_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **facts** | **Support:** **full** | Action returns an `ansible_facts` dictionary that will update existing host facts |
| **platform** | **Platforms:** **posix**, **windows** | Target OS/families that can be operated against |

## [Notes](setup_module.md#id4)

> **Note:**
>
> - More ansible facts will be added with successive releases. If *facter* or *ohai* are installed, variables from these programs will also be snapshotted into the JSON file for usage in templating. These variables are prefixed with `facter_` and `ohai_` so it’s easy to tell their source. All variables are bubbled up to the caller. Using the ansible facts and choosing to not install *facter* and *ohai* means you can avoid Ruby-dependencies on your remote systems. (See also [community.general.facter](../../community/general/facter_module.md#ansible-collections-community-general-facter-module) and [community.general.ohai](../../community/general/ohai_module.md#ansible-collections-community-general-ohai-module).)
> - The filter option filters only the first level subkey below ansible_facts.
> - If the target host is Windows, you will not currently have the ability to use `filter` as this is provided by a simpler implementation of the module.
> - This module should be run with elevated privileges on BSD systems to gather facts like ansible_product_version.
> - For more information about delegated facts, please check <https://docs.ansible.com/ansible/latest/user_guide/playbooks_delegation.html#delegating-facts>.

## [Examples](setup_module.md#id5)

```yaml+jinja
# Display facts from all hosts and store them indexed by `hostname` at `/tmp/facts`.
# ansible all -m ansible.builtin.setup --tree /tmp/facts

# Display only facts regarding memory found by ansible on all hosts and output them.
# ansible all -m ansible.builtin.setup -a 'filter=ansible_*_mb'

# Display only facts returned by facter.
# ansible all -m ansible.builtin.setup -a 'filter=facter_*'

# Collect only facts returned by facter.
# ansible all -m ansible.builtin.setup -a 'gather_subset=!all,facter'

- name: Collect only facts returned by facter
  ansible.builtin.setup:
    gather_subset:
      - '!all'
      - '!<any valid subset>'
      - facter

- name: Filter and return only selected facts
  ansible.builtin.setup:
    filter:
      - 'ansible_distribution'
      - 'ansible_machine_id'
      - 'ansible_*_mb'

# Display only facts about certain interfaces.
# ansible all -m ansible.builtin.setup -a 'filter=ansible_eth[0-2]'

# Restrict additional gathered facts to network and virtual (includes default minimum facts)
# ansible all -m ansible.builtin.setup -a 'gather_subset=network,virtual'

# Collect only network and virtual (excludes default minimum facts)
# ansible all -m ansible.builtin.setup -a 'gather_subset=!all,network,virtual'

# Do not call puppet facter or ohai even if present.
# ansible all -m ansible.builtin.setup -a 'gather_subset=!facter,!ohai'

# Only collect the default minimum amount of facts:
# ansible all -m ansible.builtin.setup -a 'gather_subset=!all'

# Collect no facts, even the default minimum subset of facts:
# ansible all -m ansible.builtin.setup -a 'gather_subset=!all,!min'

# Display facts from Windows hosts with custom facts stored in C:\custom_facts.
# ansible windows -m ansible.builtin.setup -a "fact_path='c:\custom_facts'"

# Gathers facts for the machines in the dbservers group (a.k.a Delegating facts)
- hosts: app_servers
  tasks:
    - name: Gather facts from db servers
      ansible.builtin.setup:
      delegate_to: "{{ item }}"
      delegate_facts: true
      loop: "{{ groups['dbservers'] }}"
```

### Authors

- Ansible Core Team
- Michael DeHaan

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
