---
collection: ansible
version: "8"
title: "community.grafana.grafana_annotations callback – send ansible events as annotations on charts to grafana over http api."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/grafana/grafana_annotations_callback.html
fetched_at: 2026-07-28T01:53:19+00:00
---
# community.grafana.grafana_annotations callback – send ansible events as annotations on charts to grafana over http api.

> **Note:**
>
> This callback plugin is part of the [community.grafana collection](https://galaxy.ansible.com/ui/repo/published/community/grafana/) (version 1.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.grafana`.
> You need further requirements to be able to use this callback plugin,
> see [Requirements](grafana_annotations_callback.md#ansible-collections-community-grafana-grafana-annotations-callback-requirements) for details.
>
> To use it in a playbook, specify: `community.grafana.grafana_annotations`.

- [Callback plugin](grafana_annotations_callback.md#callback-plugin)
- [Synopsis](grafana_annotations_callback.md#synopsis)
- [Requirements](grafana_annotations_callback.md#requirements)
- [Parameters](grafana_annotations_callback.md#parameters)

## [Callback plugin](grafana_annotations_callback.md#id1)

This plugin is a **notification callback**. It sends information for a playbook run to other applications, services, or systems.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](grafana_annotations_callback.md#id2)

- This callback will report start, failed and stats events to Grafana as annotations (<https://grafana.com>)

## [Requirements](grafana_annotations_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- whitelisting in configuration

## [Parameters](grafana_annotations_callback.md#id4)

| Parameter | Comments |
| --- | --- |
| **grafana_api_key**  string | Grafana API key, allowing to authenticate when posting on the HTTP API. If not provided, grafana_login and grafana_password will be required.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_grafana_annotations]   grafana_api_key = VALUE   ``` - Environment variable: [`GRAFANA_API_KEY`](../../environment_variables.md#envvar-GRAFANA_API_KEY) |
| **grafana_dashboard_id**  integer | The grafana dashboard id where the annotation shall be created.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_grafana_annotations]   grafana_dashboard_id = VALUE   ``` - Environment variable: [`GRAFANA_DASHBOARD_ID`](../../environment_variables.md#envvar-GRAFANA_DASHBOARD_ID) |
| **grafana_panel_ids**  list / elements=integer | The grafana panel ids where the annotation shall be created. Give a single integer or a comma-separated list of integers.  **Default:** `[]`  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_grafana_annotations]   grafana_panel_ids =   ``` - Environment variable: [`GRAFANA_PANEL_IDS`](../../environment_variables.md#envvar-GRAFANA_PANEL_IDS) |
| **grafana_password**  string | Grafana password used for authentication. Ignored if grafana_api_key is provided.  **Default:** `"ansible"`  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_grafana_annotations]   grafana_password = ansible   ``` - Environment variable: [`GRAFANA_PASSWORD`](../../environment_variables.md#envvar-GRAFANA_PASSWORD) |
| **grafana_url**  string / required | Grafana annotations api URL  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_grafana_annotations]   grafana_url = VALUE   ``` - Environment variable: [`GRAFANA_URL`](../../environment_variables.md#envvar-GRAFANA_URL) |
| **grafana_user**  string | Grafana user used for authentication. Ignored if grafana_api_key is provided.  **Default:** `"ansible"`  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_grafana_annotations]   grafana_user = ansible   ``` - Environment variable: [`GRAFANA_USER`](../../environment_variables.md#envvar-GRAFANA_USER) |
| **http_agent**  string | The HTTP ‘User-agent’ value to set in HTTP requets.  **Default:** `"Ansible (grafana_annotations callback)"`  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_grafana_annotations]   http_agent = Ansible (grafana_annotations callback)   ``` - Environment variable: [`HTTP_AGENT`](../../environment_variables.md#envvar-HTTP_AGENT) |
| **validate_certs**  aliases: validate_grafana_certs  boolean | validate the SSL certificate of the Grafana server. (For HTTPS url)  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - INI entries:  ```YAML+Jinja   [callback_grafana_annotations]   validate_grafana_certs = true   ```  ```YAML+Jinja   [callback_grafana_annotations]   validate_certs = true   ``` - Environment variable: [`GRAFANA_VALIDATE_CERT`](../../environment_variables.md#envvar-GRAFANA_VALIDATE_CERT) |

### Authors

- Rémi REY (@rrey)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.grafana/issues)
- [Homepage](https://github.com/ansible-collections/grafana)
- [Repository (Sources)](https://github.com/ansible-collections/community.grafana.git)
