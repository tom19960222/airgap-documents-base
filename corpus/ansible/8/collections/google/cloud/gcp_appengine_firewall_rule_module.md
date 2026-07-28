---
collection: ansible
version: "8"
title: "google.cloud.gcp_appengine_firewall_rule module – Creates a GCP FirewallRule"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_appengine_firewall_rule_module.html
fetched_at: 2026-07-28T02:31:39+00:00
---
# google.cloud.gcp_appengine_firewall_rule module – Creates a GCP FirewallRule

> **Note:**
>
> This module is part of the [google.cloud collection](https://galaxy.ansible.com/ui/repo/published/google/cloud/) (version 1.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install google.cloud`.
> You need further requirements to be able to use this module,
> see [Requirements](gcp_appengine_firewall_rule_module.md#ansible-collections-google-cloud-gcp-appengine-firewall-rule-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_appengine_firewall_rule`.

- [Synopsis](gcp_appengine_firewall_rule_module.md#synopsis)
- [Requirements](gcp_appengine_firewall_rule_module.md#requirements)
- [Parameters](gcp_appengine_firewall_rule_module.md#parameters)
- [Notes](gcp_appengine_firewall_rule_module.md#notes)
- [Examples](gcp_appengine_firewall_rule_module.md#examples)
- [Return Values](gcp_appengine_firewall_rule_module.md#return-values)

## [Synopsis](gcp_appengine_firewall_rule_module.md#id1)

- A single firewall rule that is evaluated against incoming traffic and provides an action to take on matched requests.

## [Requirements](gcp_appengine_firewall_rule_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_appengine_firewall_rule_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **action**  string / required | The action to take if this rule matches.  Some valid choices include: “UNSPECIFIED_ACTION”, “ALLOW”, “DENY” |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **description**  string | An optional string description of this rule. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **priority**  integer | A positive integer that defines the order of rule evaluation.  Rules with the lowest priority are evaluated first.  A default rule at priority Int32.MaxValue matches all IPv4 and IPv6 traffic when no previous rule matches. Only the action of this rule can be modified by the user. |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **source_range**  string / required | IP address or range, defined using CIDR notation, of requests that this rule applies to. |
| **state**  string | Whether the given object should exist in GCP  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](gcp_appengine_firewall_rule_module.md#id4)

> **Note:**
>
> - API Reference: <https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.firewall.ingressRules>
> - Official Documentation: <https://cloud.google.com/appengine/docs/standard/python/creating-firewalls#creating_firewall_rules>
> - for authentication, you can set service_account_file using the `GCP_SERVICE_ACCOUNT_FILE` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set access_token using the `GCP_ACCESS_TOKEN` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_appengine_firewall_rule_module.md#id5)

```yaml+jinja
- name: create a firewall rule
  google.cloud.gcp_appengine_firewall_rule:
    priority: 1000
    source_range: 10.0.0.0
    action: ALLOW
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_appengine_firewall_rule_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **action**  string | The action to take if this rule matches.  **Returned:** success |
| **description**  string | An optional string description of this rule.  **Returned:** success |
| **priority**  integer | A positive integer that defines the order of rule evaluation.  Rules with the lowest priority are evaluated first.  A default rule at priority Int32.MaxValue matches all IPv4 and IPv6 traffic when no previous rule matches. Only the action of this rule can be modified by the user.  **Returned:** success |
| **sourceRange**  string | IP address or range, defined using CIDR notation, of requests that this rule applies to.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
