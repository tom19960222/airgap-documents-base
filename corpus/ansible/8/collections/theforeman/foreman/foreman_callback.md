---
collection: ansible
version: "8"
title: "theforeman.foreman.foreman callback – Sends events to Foreman"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/foreman_callback.html
fetched_at: 2026-07-28T02:56:50+00:00
---
# theforeman.foreman.foreman callback – Sends events to Foreman

> **Note:**
>
> This callback plugin is part of the [theforeman.foreman collection](https://galaxy.ansible.com/ui/repo/published/theforeman/foreman/) (version 3.15.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install theforeman.foreman`.
> You need further requirements to be able to use this callback plugin,
> see [Requirements](foreman_callback.md#ansible-collections-theforeman-foreman-foreman-callback-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.foreman`.

- [Callback plugin](foreman_callback.md#callback-plugin)
- [Synopsis](foreman_callback.md#synopsis)
- [Requirements](foreman_callback.md#requirements)
- [Parameters](foreman_callback.md#parameters)

## [Callback plugin](foreman_callback.md#id1)

This plugin is a **notification callback**. It sends information for a playbook run to other applications, services, or systems.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](foreman_callback.md#id2)

- This callback will report facts and task events to Foreman

## [Requirements](foreman_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- whitelisting in configuration
- requests (python library)

## [Parameters](foreman_callback.md#id4)

| Parameter | Comments |
| --- | --- |
| **client_cert**  aliases: ssl_cert  string | X509 certificate to authenticate to Foreman if https is used  **Default:** `"/etc/foreman/client_cert.pem"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [callback_foreman]   ssl_cert = /etc/foreman/client_cert.pem   ```  ```YAML+Jinja   [callback_foreman]   client_cert = /etc/foreman/client_cert.pem   ``` - Environment variable: [`FOREMAN_SSL_CERT`](../../environment_variables.md#envvar-FOREMAN_SSL_CERT) |
| **client_key**  aliases: ssl_key  string | the corresponding private key  **Default:** `"/etc/foreman/client_key.pem"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [callback_foreman]   ssl_key = /etc/foreman/client_key.pem   ```  ```YAML+Jinja   [callback_foreman]   client_key = /etc/foreman/client_key.pem   ``` - Environment variable: [`FOREMAN_SSL_KEY`](../../environment_variables.md#envvar-FOREMAN_SSL_KEY) |
| **dir_store**  string | When set, callback does not perform HTTP calls but stores results in a given directory.  For each report, new file in the form of SEQ_NO-hostname.json is created.  For each facts, new file in the form of SEQ_NO-hostname.json is created.  The value must be a valid directory.  This is meant for debugging and testing purposes.  When set to blank (default) this functionality is turned off.  **Default:** `""`  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_foreman]   dir_store = ""   ``` - Environment variable: [`FOREMAN_DIR_STORE`](../../environment_variables.md#envvar-FOREMAN_DIR_STORE) |
| **disable_callback**  string | Toggle to make the callback plugin disable itself even if it is loaded.  It can be set to ‘1’ to prevent the plugin from being used even if it gets loaded.  **Default:** `0`  **Configuration:**   - Environment variable: [`FOREMAN_CALLBACK_DISABLE`](../../environment_variables.md#envvar-FOREMAN_CALLBACK_DISABLE) |
| **proxy_url**  string | URL of the Foreman Smart Proxy server.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_foreman]   proxy_url = VALUE   ``` - Environment variable: [`FOREMAN_PROXY_URL`](../../environment_variables.md#envvar-FOREMAN_PROXY_URL) |
| **report_type**  string | endpoint type for reports: foreman or proxy  **Default:** `"foreman"`  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_foreman]   report_type = foreman   ``` - Environment variable: [`FOREMAN_REPORT_TYPE`](../../environment_variables.md#envvar-FOREMAN_REPORT_TYPE) |
| **url**  string / required | URL of the Foreman server.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_foreman]   url = VALUE   ``` - Environment variable: [`FOREMAN_URL`](../../environment_variables.md#envvar-FOREMAN_URL) - Environment variable: [`FOREMAN_SERVER_URL`](../../environment_variables.md#envvar-FOREMAN_SERVER_URL) - Environment variable: [`FOREMAN_SERVER`](../../environment_variables.md#envvar-FOREMAN_SERVER) |
| **verify_certs**  string | Toggle to decide whether to verify the Foreman certificate.  It can be set to ‘1’ to verify SSL certificates using the installed CAs or to a path pointing to a CA bundle.  Set to ‘0’ to disable certificate checking.  **Default:** `1`  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_foreman]   verify_certs = 1   ``` - Environment variable: [`FOREMAN_SSL_VERIFY`](../../environment_variables.md#envvar-FOREMAN_SSL_VERIFY) |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
