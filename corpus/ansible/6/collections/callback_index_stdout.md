---
collection: ansible
version: "6"
title: "Index of all Stdout Callback Plugins"
source_url: https://docs.ansible.com/projects/ansible/6/collections/callback_index_stdout.html
fetched_at: 2026-07-28T00:24:23+00:00
---
# Index of all Stdout Callback Plugins

See [Index of all Callback Plugins](index_callback.md#list-of-callback-plugins) for the list of *all* callback plugins.

## ansible.builtin

- [ansible.builtin.default](ansible/builtin/default_callback.md#ansible-collections-ansible-builtin-default-callback) – default Ansible screen output
- [ansible.builtin.minimal](ansible/builtin/minimal_callback.md#ansible-collections-ansible-builtin-minimal-callback) – minimal Ansible screen output
- [ansible.builtin.oneline](ansible/builtin/oneline_callback.md#ansible-collections-ansible-builtin-oneline-callback) – oneline Ansible screen output

## ansible.posix

- [ansible.posix.debug](ansible/posix/debug_callback.md#ansible-collections-ansible-posix-debug-callback) – formatted stdout/stderr display
- [ansible.posix.json](ansible/posix/json_callback.md#ansible-collections-ansible-posix-json-callback) – Ansible screen output as JSON
- [ansible.posix.skippy](ansible/posix/skippy_callback.md#ansible-collections-ansible-posix-skippy-callback) – Ansible screen output that ignores skipped status

## community.general

- [community.general.counter_enabled](community/general/counter_enabled_callback.md#ansible-collections-community-general-counter-enabled-callback) – adds counters to the output items (tasks and hosts/task)
- [community.general.dense](community/general/dense_callback.md#ansible-collections-community-general-dense-callback) – minimal stdout output
- [community.general.diy](community/general/diy_callback.md#ansible-collections-community-general-diy-callback) – Customize the output
- [community.general.null](community/general/null_callback.md#ansible-collections-community-general-null-callback) – Don’t display stuff to screen
- [community.general.selective](community/general/selective_callback.md#ansible-collections-community-general-selective-callback) – only print certain tasks
- [community.general.unixy](community/general/unixy_callback.md#ansible-collections-community-general-unixy-callback) – condensed Ansible output
- [community.general.yaml](community/general/yaml_callback.md#ansible-collections-community-general-yaml-callback) – yaml-ized Ansible screen output
