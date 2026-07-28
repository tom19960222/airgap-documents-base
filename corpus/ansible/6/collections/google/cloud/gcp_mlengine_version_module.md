---
collection: ansible
version: "6"
title: "google.cloud.gcp_mlengine_version module – Creates a GCP Version"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_mlengine_version_module.html
fetched_at: 2026-07-27T17:49:12+00:00
---
# google.cloud.gcp_mlengine_version module – Creates a GCP Version

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
> see [Requirements](gcp_mlengine_version_module.md#ansible-collections-google-cloud-gcp-mlengine-version-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_mlengine_version`.

- [Synopsis](gcp_mlengine_version_module.md#synopsis)
- [Requirements](gcp_mlengine_version_module.md#requirements)
- [Parameters](gcp_mlengine_version_module.md#parameters)
- [Examples](gcp_mlengine_version_module.md#examples)
- [Return Values](gcp_mlengine_version_module.md#return-values)

## [Synopsis](gcp_mlengine_version_module.md#id1)

- Each version is a trained model deployed in the cloud, ready to handle prediction requests. A model can have multiple versions .

## [Requirements](gcp_mlengine_version_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_mlengine_version_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **auto_scaling**  dictionary | Automatically scale the number of nodes used to serve the model in response to increases and decreases in traffic. Care should be taken to ramp up traffic according to the model’s ability to scale or you will start seeing increases in latency and 429 response codes. |
| **min_nodes**  integer | The minimum number of nodes to allocate for this mode. |
| **deployment_uri**  string / required | The Cloud Storage location of the trained model used to create the version. |
| **description**  string | The description specified for the version when it was created. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **framework**  string | The machine learning framework AI Platform uses to train this version of the model.  Some valid choices include: “FRAMEWORK_UNSPECIFIED”, “TENSORFLOW”, “SCIKIT_LEARN”, “XGBOOST” |
| **is_default**  aliases: default  boolean | If true, this version will be used to handle prediction requests that do not specify a version.  Choices:   - `false` - `true` |
| **labels**  dictionary | One or more labels that you can add, to organize your model versions. |
| **machine_type**  string | The type of machine on which to serve the model. Currently only applies to online prediction service.  Some valid choices include: “mls1-c1-m2”, “mls1-c4-m2” |
| **manual_scaling**  dictionary | Manually select the number of nodes to use for serving the model. You should generally use autoScaling with an appropriate minNodes instead, but this option is available if you want more predictable billing. Beware that latency and error rates will increase if the traffic exceeds that capability of the system to serve it based on the selected number of nodes. |
| **nodes**  integer | The number of nodes to allocate for this model. These nodes are always up, starting from the time the model is deployed. |
| **model**  dictionary / required | The model that this version belongs to.  This field represents a link to a Model resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘name’ and value of your resource’s name Alternatively, you can add `register: name-of-resource` to a gcp_mlengine_model task and then set this model field to “{{ name-of-resource }}” |
| **name**  string / required | The name specified for the version when it was created.  The version name must be unique within the model it is created in. |
| **prediction_class**  string | The fully qualified name (module_name.class_name) of a class that implements the Predictor interface described in this reference field. The module containing this class should be included in a package provided to the packageUris field. |
| **project**  string | The Google Cloud Platform project to use. |
| **python_version**  string | The version of Python used in prediction. If not set, the default version is ‘2.7’. Python ‘3.5’ is available when runtimeVersion is set to ‘1.4’ and above. Python ‘2.7’ works with all supported runtime versions.  Some valid choices include: “2.7”, “3.5” |
| **runtime_version**  string | The AI Platform runtime version to use for this deployment. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account**  string | Specifies the service account for resource access control. |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  Choices:   - `"present"` ← (default) - `"absent"` |

## [Examples](gcp_mlengine_version_module.md#id4)

```yaml+jinja
- name: create a model
  google.cloud.gcp_mlengine_model:
    name: model_version
    description: My model
    regions:
    - us-central1
    online_prediction_logging: 'true'
    online_prediction_console_logging: 'true'
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: model

- name: create a version
  google.cloud.gcp_mlengine_version:
    name: "{{ resource_name | replace('-', '_') }}"
    model: "{{ model }}"
    runtime_version: 1.13
    python_version: 3.5
    is_default: 'true'
    deployment_uri: gs://ansible-cloudml-bucket/
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_mlengine_version_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **autoScaling**  complex | Automatically scale the number of nodes used to serve the model in response to increases and decreases in traffic. Care should be taken to ramp up traffic according to the model’s ability to scale or you will start seeing increases in latency and 429 response codes.  Returned: success |
| **minNodes**  integer | The minimum number of nodes to allocate for this mode.  Returned: success |
| **createTime**  string | The time the version was created.  Returned: success |
| **deploymentUri**  string | The Cloud Storage location of the trained model used to create the version.  Returned: success |
| **description**  string | The description specified for the version when it was created.  Returned: success |
| **errorMessage**  string | The details of a failure or cancellation.  Returned: success |
| **framework**  string | The machine learning framework AI Platform uses to train this version of the model.  Returned: success |
| **isDefault**  boolean | If true, this version will be used to handle prediction requests that do not specify a version.  Returned: success |
| **labels**  dictionary | One or more labels that you can add, to organize your model versions.  Returned: success |
| **lastUseTime**  string | The time the version was last used for prediction.  Returned: success |
| **machineType**  string | The type of machine on which to serve the model. Currently only applies to online prediction service.  Returned: success |
| **manualScaling**  complex | Manually select the number of nodes to use for serving the model. You should generally use autoScaling with an appropriate minNodes instead, but this option is available if you want more predictable billing. Beware that latency and error rates will increase if the traffic exceeds that capability of the system to serve it based on the selected number of nodes.  Returned: success |
| **nodes**  integer | The number of nodes to allocate for this model. These nodes are always up, starting from the time the model is deployed.  Returned: success |
| **model**  dictionary | The model that this version belongs to.  Returned: success |
| **name**  string | The name specified for the version when it was created.  The version name must be unique within the model it is created in.  Returned: success |
| **packageUris**  list / elements=string | Cloud Storage paths (gs://…) of packages for custom prediction routines or scikit-learn pipelines with custom code.  Returned: success |
| **predictionClass**  string | The fully qualified name (module_name.class_name) of a class that implements the Predictor interface described in this reference field. The module containing this class should be included in a package provided to the packageUris field.  Returned: success |
| **pythonVersion**  string | The version of Python used in prediction. If not set, the default version is ‘2.7’. Python ‘3.5’ is available when runtimeVersion is set to ‘1.4’ and above. Python ‘2.7’ works with all supported runtime versions.  Returned: success |
| **runtimeVersion**  string | The AI Platform runtime version to use for this deployment.  Returned: success |
| **serviceAccount**  string | Specifies the service account for resource access control.  Returned: success |
| **state**  string | The state of a version.  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
