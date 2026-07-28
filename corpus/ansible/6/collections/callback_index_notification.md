---
collection: ansible
version: "6"
title: "Index of all Notification Callback Plugins"
source_url: https://docs.ansible.com/projects/ansible/6/collections/callback_index_notification.html
fetched_at: 2026-07-28T00:24:22+00:00
---
# Index of all Notification Callback Plugins

See [Index of all Callback Plugins](index_callback.md#list-of-callback-plugins) for the list of *all* callback plugins.

## ansible.builtin

- [ansible.builtin.tree](ansible/builtin/tree_callback.md#ansible-collections-ansible-builtin-tree-callback) – Save host events to files

## community.general

- [community.general.elastic](community/general/elastic_callback.md#ansible-collections-community-general-elastic-callback) – Create distributed traces for each Ansible task in Elastic APM
- [community.general.hipchat](community/general/hipchat_callback.md#ansible-collections-community-general-hipchat-callback) – post task events to hipchat
- [community.general.jabber](community/general/jabber_callback.md#ansible-collections-community-general-jabber-callback) – post task events to a jabber server
- [community.general.log_plays](community/general/log_plays_callback.md#ansible-collections-community-general-log-plays-callback) – write playbook output to log file
- [community.general.logentries](community/general/logentries_callback.md#ansible-collections-community-general-logentries-callback) – Sends events to Logentries
- [community.general.logstash](community/general/logstash_callback.md#ansible-collections-community-general-logstash-callback) – Sends events to Logstash
- [community.general.mail](community/general/mail_callback.md#ansible-collections-community-general-mail-callback) – Sends failure events via email
- [community.general.nrdp](community/general/nrdp_callback.md#ansible-collections-community-general-nrdp-callback) – Post task results to a Nagios server through nrdp
- [community.general.opentelemetry](community/general/opentelemetry_callback.md#ansible-collections-community-general-opentelemetry-callback) – Create distributed traces with OpenTelemetry
- [community.general.say](community/general/say_callback.md#ansible-collections-community-general-say-callback) – notify using software speech synthesizer
- [community.general.slack](community/general/slack_callback.md#ansible-collections-community-general-slack-callback) – Sends play events to a Slack channel
- [community.general.syslog_json](community/general/syslog_json_callback.md#ansible-collections-community-general-syslog-json-callback) – sends JSON events to syslog

## community.grafana

- [community.grafana.grafana_annotations](community/grafana/grafana_annotations_callback.md#ansible-collections-community-grafana-grafana-annotations-callback) – send ansible events as annotations on charts to grafana over http api.

## theforeman.foreman

- [theforeman.foreman.foreman](theforeman/foreman/foreman_callback.md#ansible-collections-theforeman-foreman-foreman-callback) – Sends events to Foreman
