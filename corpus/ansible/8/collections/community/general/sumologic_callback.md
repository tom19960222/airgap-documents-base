---
collection: ansible
version: "8"
title: "community.general.sumologic callback – Sends task result events to Sumologic"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/sumologic_callback.html
fetched_at: 2026-07-28T01:52:06+00:00
---
# community.general.sumologic callback – Sends task result events to Sumologic

> **Note:**
>
> This callback plugin is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this callback plugin,
> see [Requirements](sumologic_callback.md#ansible-collections-community-general-sumologic-callback-requirements) for details.
>
> To use it in a playbook, specify: `community.general.sumologic`.

- [Callback plugin](sumologic_callback.md#callback-plugin)
- [Synopsis](sumologic_callback.md#synopsis)
- [Requirements](sumologic_callback.md#requirements)
- [Parameters](sumologic_callback.md#parameters)
- [Examples](sumologic_callback.md#examples)

## [Callback plugin](sumologic_callback.md#id1)

This plugin is a **notification callback**. It sends information for a playbook run to other applications, services, or systems.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](sumologic_callback.md#id2)

- This callback plugin will send task results as JSON formatted events to a Sumologic HTTP collector source.

## [Requirements](sumologic_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- Whitelisting this callback plugin
- Create a HTTP collector source in Sumologic and specify a custom timestamp format of `yyyy-MM-dd HH:mm:ss ZZZZ` and a custom timestamp locator of `"timestamp": "(.*)"`

## [Parameters](sumologic_callback.md#id4)

| Parameter | Comments |
| --- | --- |
| **url**  string | URL to the Sumologic HTTP collector source.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_sumologic]   url = VALUE   ``` - Environment variable: [`SUMOLOGIC_URL`](../../environment_variables.md#envvar-SUMOLOGIC_URL) |

## [Examples](sumologic_callback.md#id5)

```yaml+jinja
examples: |
  To enable, add this to your ansible.cfg file in the defaults block
    [defaults]
    callback_whitelist = community.general.sumologic

  Set the environment variable
    export SUMOLOGIC_URL=https://endpoint1.collection.us2.sumologic.com/receiver/v1/http/R8moSv1d8EW9LAUFZJ6dbxCFxwLH6kfCdcBfddlfxCbLuL-BN5twcTpMk__pYy_cDmp==

  Set the ansible.cfg variable in the callback_sumologic block
    [callback_sumologic]
    url = https://endpoint1.collection.us2.sumologic.com/receiver/v1/http/R8moSv1d8EW9LAUFZJ6dbxCFxwLH6kfCdcBfddlfxCbLuL-BN5twcTpMk__pYy_cDmp==
```

### Authors

- Ryan Currah (@ryancurrah)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
