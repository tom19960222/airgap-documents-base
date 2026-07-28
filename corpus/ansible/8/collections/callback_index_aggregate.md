---
collection: ansible
version: "8"
title: "Index of all Aggregate Callback Plugins"
source_url: https://docs.ansible.com/projects/ansible/8/collections/callback_index_aggregate.html
fetched_at: 2026-07-28T03:00:18+00:00
---
# Index of all Aggregate Callback Plugins

See [Index of all Callback Plugins](index_callback.md#list-of-callback-plugins) for the list of *all* callback plugins.

## amazon.aws

- [amazon.aws.aws_resource_actions](amazon/aws/aws_resource_actions_callback.md#ansible-collections-amazon-aws-aws-resource-actions-callback) – summarizes all “resource:actions” completed

## ansible.builtin

- [ansible.builtin.junit](ansible/builtin/junit_callback.md#ansible-collections-ansible-builtin-junit-callback) – write playbook output to a JUnit file.

## ansible.posix

- [ansible.posix.cgroup_perf_recap](ansible/posix/cgroup_perf_recap_callback.md#ansible-collections-ansible-posix-cgroup-perf-recap-callback) – Profiles system activity of tasks and full execution using cgroups
- [ansible.posix.profile_roles](ansible/posix/profile_roles_callback.md#ansible-collections-ansible-posix-profile-roles-callback) – adds timing information to roles
- [ansible.posix.profile_tasks](ansible/posix/profile_tasks_callback.md#ansible-collections-ansible-posix-profile-tasks-callback) – adds time information to tasks
- [ansible.posix.timer](ansible/posix/timer_callback.md#ansible-collections-ansible-posix-timer-callback) – Adds time to play stats

## community.general

- [community.general.cgroup_memory_recap](community/general/cgroup_memory_recap_callback.md#ansible-collections-community-general-cgroup-memory-recap-callback) – Profiles maximum memory usage of tasks and full execution using cgroups
- [community.general.context_demo](community/general/context_demo_callback.md#ansible-collections-community-general-context-demo-callback) – demo callback that adds play/task context

## ovirt.ovirt

- [ovirt.ovirt.stdout](ovirt/ovirt/stdout_callback.md#ansible-collections-ovirt-ovirt-stdout-callback) – Output the log of ansible
