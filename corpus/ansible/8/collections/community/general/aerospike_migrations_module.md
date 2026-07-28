---
collection: ansible
version: "8"
title: "community.general.aerospike_migrations module – Check or wait for migrations between nodes"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/aerospike_migrations_module.html
fetched_at: 2026-07-28T01:44:30+00:00
---
# community.general.aerospike_migrations module – Check or wait for migrations between nodes

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.aerospike_migrations`.

- [Synopsis](aerospike_migrations_module.md#synopsis)
- [Parameters](aerospike_migrations_module.md#parameters)
- [Attributes](aerospike_migrations_module.md#attributes)
- [Examples](aerospike_migrations_module.md#examples)

## [Synopsis](aerospike_migrations_module.md#id1)

- This can be used to check for migrations in a cluster. This makes it easy to do a rolling upgrade/update on Aerospike nodes.
- If waiting for migrations is not desired, simply just poll until port 3000 if available or asinfo -v status returns ok

Aliases: database.aerospike.aerospike_migrations

## [Parameters](aerospike_migrations_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **connect_timeout**  integer | How long to try to connect before giving up (milliseconds)  **Default:** `1000` |
| **consecutive_good_checks**  integer | How many times should the cluster report “no migrations” consecutively before returning OK back to ansible?  **Default:** `3` |
| **fail_on_cluster_change**  boolean | Fail if the cluster key changes if something else is changing the cluster, we may want to fail  **Choices:**   - `false` - `true` ← (default) |
| **host**  string | Which host do we use as seed for info connection  **Default:** `"localhost"` |
| **local_only**  boolean / required | Do you wish to only check for migrations on the local node before returning, or do you want all nodes in the cluster to finish before returning?  **Choices:**   - `false` - `true` |
| **migrate_rx_key**  string | The metric key used to determine if we have rx migrations remaining. Changeable due to backwards compatibility.  **Default:** `"migrate_rx_partitions_remaining"` |
| **migrate_tx_key**  string | The metric key used to determine if we have tx migrations remaining. Changeable due to backwards compatibility.  **Default:** `"migrate_tx_partitions_remaining"` |
| **min_cluster_size**  integer | Check will return bad until cluster size is met or until tries is exhausted  **Default:** `1` |
| **port**  integer | Which port to connect to Aerospike on (service port)  **Default:** `3000` |
| **sleep_between_checks**  integer | How long to sleep between each check (seconds).  **Default:** `60` |
| **target_cluster_size**  integer | When all aerospike builds in the cluster are greater than version 4.3, then the `cluster-stable` info command will be used. Inside this command, you can optionally specify what the target cluster size is - but it is not necessary. You can still rely on min_cluster_size if you don’t want to use this option.  If this option is specified on a cluster that has at least 1 host <4.3 then it will be ignored until the min version reaches 4.3. |
| **tries_limit**  integer | How many times do we poll before giving up and failing?  **Default:** `300` |

## [Attributes](aerospike_migrations_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](aerospike_migrations_module.md#id4)

```yaml+jinja
# check for migrations on local node
- name: Wait for migrations on local node before proceeding
  community.general.aerospike_migrations:
    host: "localhost"
    connect_timeout: 2000
    consecutive_good_checks: 5
    sleep_between_checks: 15
    tries_limit: 600
    local_only: false

# example playbook:
- name: Upgrade aerospike
  hosts: all
  become: true
  serial: 1
  tasks:
    - name: Install dependencies
      ansible.builtin.apt:
        name:
            - python
            - python-pip
            - python-setuptools
        state: latest
    - name: Setup aerospike
      ansible.builtin.pip:
          name: aerospike
# check for migrations every (sleep_between_checks)
# If at least (consecutive_good_checks) checks come back OK in a row, then return OK.
# Will exit if any exception, which can be caused by bad nodes,
# nodes not returning data, or other reasons.
# Maximum runtime before giving up in this case will be:
# Tries Limit * Sleep Between Checks * delay * retries
    - name: Wait for aerospike migrations
      community.general.aerospike_migrations:
          local_only: true
          sleep_between_checks: 1
          tries_limit: 5
          consecutive_good_checks: 3
          fail_on_cluster_change: true
          min_cluster_size: 3
          target_cluster_size: 4
      register: migrations_check
      until: migrations_check is succeeded
      changed_when: false
      delay: 60
      retries: 120
    - name: Another thing
      ansible.builtin.shell: |
          echo foo
    - name: Reboot
      ansible.builtin.reboot:
```

### Authors

- Albert Autin (@Alb0t)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
