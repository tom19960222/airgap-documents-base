---
collection: ansible
version: "6"
title: "google.cloud.gcp_mlengine_model module – Creates a GCP Model"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_mlengine_model_module.html
fetched_at: 2026-07-27T17:49:11+00:00
---
# google.cloud.gcp_mlengine_model module – Creates a GCP Model

> **Note:**
>
> This module is part of the [google.cloud collection](https://galaxy.ansible.com/google/cloud) (version 1.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install google.cloud`.
> You need further requirements to be able to use this module,
> see [Requirements](gcp_mlengine_model_module.md#ansible-collections-google-cloud-gcp-mlengine-model-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_mlengine_model`.

- [Synopsis](gcp_mlengine_model_module.md#synopsis)
- [Requirements](gcp_mlengine_model_module.md#requirements)
- [Parameters](gcp_mlengine_model_module.md#parameters)
- [Examples](gcp_mlengine_model_module.md#examples)
- [Return Values](gcp_mlengine_model_module.md#return-values)

## [Synopsis](gcp_mlengine_model_module.md#id1)

- Represents a machine learning solution.
- A model can have multiple versions, each of which is a deployed, trained model ready to receive prediction requests. The model itself is just a container.

## [Requirements](gcp_mlengine_model_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_mlengine_model_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **default_version**  dictionary | The default version of the model. This version will be used to handle prediction requests that do not specify a version. |
| **name**  string / required | The name specified for the version when it was created. |
| **description**  string | The description specified for the model when it was created. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **labels**  dictionary | One or more labels that you can add, to organize your models. |
| **name**  string / required | The name specified for the model. |
| **online_prediction_console_logging**  boolean | If true, online prediction nodes send stderr and stdout streams to Stackdriver Logging.  Choices:   - `false` - `true` |
| **online_prediction_logging**  boolean | If true, online prediction access logs are sent to StackDriver Logging.  Choices:   - `false` - `true` |
| **project**  string | The Google Cloud Platform project to use. |
| **regions**  list / elements=string | The list of regions where the model is going to be deployed.  Currently only one region per model is supported . |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  Choices:   - `"present"` ← (default) - `"absent"` |

## [Examples](gcp_mlengine_model_module.md#id4)

```yaml+jinja
- name: create a model
  google.cloud.gcp_mlengine_model:
    name: "{{ resource_name | replace('-', '_') }}"
    description: My model
    regions:
    - us-central1
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_mlengine_model_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **defaultVersion**  complex | The default version of the model. This version will be used to handle prediction requests that do not specify a version.  Returned: success |
| **name**  string | The name specified for the version when it was created.  Returned: success |
| **description**  string | The description specified for the model when it was created.  Returned: success |
| **labels**  dictionary | One or more labels that you can add, to organize your models.  Returned: success |
| **name**  string | The name specified for the model.  Returned: success |
| **onlinePredictionConsoleLogging**  boolean | If true, online prediction nodes send stderr and stdout streams to Stackdriver Logging.  Returned: success |
| **onlinePredictionLogging**  boolean | If true, online prediction access logs are sent to StackDriver Logging.  Returned: success |
| **regions**  list / elements=string | The list of regions where the model is going to be deployed.  Currently only one region per model is supported .  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
