---
collection: ansible
version: "8"
title: "Index of all Callback Plugins"
source_url: https://docs.ansible.com/projects/ansible/8/collections/index_callback.html
fetched_at: 2026-07-28T01:03:06+00:00
---
# Index of all Callback Plugins

List of callback plugins by callback type

- [Index of all Aggregate Callback Plugins](callback_index_aggregate.md)
- [Index of all Notification Callback Plugins](callback_index_notification.md)
- [Index of all Stdout Callback Plugins](callback_index_stdout.md)

## amazon.aws

- [amazon.aws.aws_resource_actions](amazon/aws/aws_resource_actions_callback.md#ansible-collections-amazon-aws-aws-resource-actions-callback) – summarizes all “resource:actions” completed

## ansible.builtin

- [ansible.builtin.default](ansible/builtin/default_callback.md#ansible-collections-ansible-builtin-default-callback) – default Ansible screen output
- [ansible.builtin.junit](ansible/builtin/junit_callback.md#ansible-collections-ansible-builtin-junit-callback) – write playbook output to a JUnit file.
- [ansible.builtin.minimal](ansible/builtin/minimal_callback.md#ansible-collections-ansible-builtin-minimal-callback) – minimal Ansible screen output
- [ansible.builtin.oneline](ansible/builtin/oneline_callback.md#ansible-collections-ansible-builtin-oneline-callback) – oneline Ansible screen output
- [ansible.builtin.tree](ansible/builtin/tree_callback.md#ansible-collections-ansible-builtin-tree-callback) – Save host events to files

## ansible.posix

- [ansible.posix.cgroup_perf_recap](ansible/posix/cgroup_perf_recap_callback.md#ansible-collections-ansible-posix-cgroup-perf-recap-callback) – Profiles system activity of tasks and full execution using cgroups
- [ansible.posix.debug](ansible/posix/debug_callback.md#ansible-collections-ansible-posix-debug-callback) – formatted stdout/stderr display
- [ansible.posix.json](ansible/posix/json_callback.md#ansible-collections-ansible-posix-json-callback) – Ansible screen output as JSON
- [ansible.posix.jsonl](ansible/posix/jsonl_callback.md#ansible-collections-ansible-posix-jsonl-callback) – Ansible screen output as JSONL (lines in json format)
- [ansible.posix.profile_roles](ansible/posix/profile_roles_callback.md#ansible-collections-ansible-posix-profile-roles-callback) – adds timing information to roles
- [ansible.posix.profile_tasks](ansible/posix/profile_tasks_callback.md#ansible-collections-ansible-posix-profile-tasks-callback) – adds time information to tasks
- [ansible.posix.skippy](ansible/posix/skippy_callback.md#ansible-collections-ansible-posix-skippy-callback) – Ansible screen output that ignores skipped status
- [ansible.posix.timer](ansible/posix/timer_callback.md#ansible-collections-ansible-posix-timer-callback) – Adds time to play stats

## community.general

- [community.general.cgroup_memory_recap](community/general/cgroup_memory_recap_callback.md#ansible-collections-community-general-cgroup-memory-recap-callback) – Profiles maximum memory usage of tasks and full execution using cgroups
- [community.general.context_demo](community/general/context_demo_callback.md#ansible-collections-community-general-context-demo-callback) – demo callback that adds play/task context
- [community.general.counter_enabled](community/general/counter_enabled_callback.md#ansible-collections-community-general-counter-enabled-callback) – adds counters to the output items (tasks and hosts/task)
- [community.general.dense](community/general/dense_callback.md#ansible-collections-community-general-dense-callback) – minimal stdout output
- [community.general.diy](community/general/diy_callback.md#ansible-collections-community-general-diy-callback) – Customize the output
- [community.general.elastic](community/general/elastic_callback.md#ansible-collections-community-general-elastic-callback) – Create distributed traces for each Ansible task in Elastic APM
- [community.general.hipchat](community/general/hipchat_callback.md#ansible-collections-community-general-hipchat-callback) – post task events to hipchat
- [community.general.jabber](community/general/jabber_callback.md#ansible-collections-community-general-jabber-callback) – post task events to a jabber server
- [community.general.log_plays](community/general/log_plays_callback.md#ansible-collections-community-general-log-plays-callback) – write playbook output to log file
- [community.general.loganalytics](community/general/loganalytics_callback.md#ansible-collections-community-general-loganalytics-callback) – Posts task results to Azure Log Analytics
- [community.general.logdna](community/general/logdna_callback.md#ansible-collections-community-general-logdna-callback) – Sends playbook logs to LogDNA
- [community.general.logentries](community/general/logentries_callback.md#ansible-collections-community-general-logentries-callback) – Sends events to Logentries
- [community.general.logstash](community/general/logstash_callback.md#ansible-collections-community-general-logstash-callback) – Sends events to Logstash
- [community.general.mail](community/general/mail_callback.md#ansible-collections-community-general-mail-callback) – Sends failure events via email
- [community.general.nrdp](community/general/nrdp_callback.md#ansible-collections-community-general-nrdp-callback) – Post task results to a Nagios server through nrdp
- [community.general.null](community/general/null_callback.md#ansible-collections-community-general-null-callback) – Don’t display stuff to screen
- [community.general.opentelemetry](community/general/opentelemetry_callback.md#ansible-collections-community-general-opentelemetry-callback) – Create distributed traces with OpenTelemetry
- [community.general.say](community/general/say_callback.md#ansible-collections-community-general-say-callback) – notify using software speech synthesizer
- [community.general.selective](community/general/selective_callback.md#ansible-collections-community-general-selective-callback) – only print certain tasks
- [community.general.slack](community/general/slack_callback.md#ansible-collections-community-general-slack-callback) – Sends play events to a Slack channel
- [community.general.splunk](community/general/splunk_callback.md#ansible-collections-community-general-splunk-callback) – Sends task result events to Splunk HTTP Event Collector
- [community.general.sumologic](community/general/sumologic_callback.md#ansible-collections-community-general-sumologic-callback) – Sends task result events to Sumologic
- [community.general.syslog_json](community/general/syslog_json_callback.md#ansible-collections-community-general-syslog-json-callback) – sends JSON events to syslog
- [community.general.unixy](community/general/unixy_callback.md#ansible-collections-community-general-unixy-callback) – condensed Ansible output
- [community.general.yaml](community/general/yaml_callback.md#ansible-collections-community-general-yaml-callback) – YAML-ized Ansible screen output

## community.grafana

- [community.grafana.grafana_annotations](community/grafana/grafana_annotations_callback.md#ansible-collections-community-grafana-grafana-annotations-callback) – send ansible events as annotations on charts to grafana over http api.

## ovirt.ovirt

- [ovirt.ovirt.stdout](ovirt/ovirt/stdout_callback.md#ansible-collections-ovirt-ovirt-stdout-callback) – Output the log of ansible

## theforeman.foreman

- [theforeman.foreman.foreman](theforeman/foreman/foreman_callback.md#ansible-collections-theforeman-foreman-foreman-callback) – Sends events to Foreman
