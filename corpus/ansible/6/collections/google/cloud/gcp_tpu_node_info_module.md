---
collection: ansible
version: "6"
title: "google.cloud.gcp_tpu_node_info module – Gather info for GCP Node"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_tpu_node_info_module.html
fetched_at: 2026-07-27T17:49:36+00:00
---
# google.cloud.gcp_tpu_node_info module – Gather info for GCP Node

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
> see [Requirements](gcp_tpu_node_info_module.md#ansible-collections-google-cloud-gcp-tpu-node-info-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_tpu_node_info`.

- [Synopsis](gcp_tpu_node_info_module.md#synopsis)
- [Requirements](gcp_tpu_node_info_module.md#requirements)
- [Parameters](gcp_tpu_node_info_module.md#parameters)
- [Notes](gcp_tpu_node_info_module.md#notes)
- [Examples](gcp_tpu_node_info_module.md#examples)
- [Return Values](gcp_tpu_node_info_module.md#return-values)

## [Synopsis](gcp_tpu_node_info_module.md#id1)

- Gather info for GCP Node

## [Requirements](gcp_tpu_node_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_tpu_node_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **zone**  string | The GCP location for the TPU. If it is not provided, the provider zone is used. |

## [Notes](gcp_tpu_node_info_module.md#id4)

> **Note:**
>
> - for authentication, you can set service_account_file using the `gcp_service_account_file` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_tpu_node_info_module.md#id5)

```yaml+jinja
- name: get info on a node
  gcp_tpu_node_info:
    zone: us-central1-b
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
```

## [Return Values](gcp_tpu_node_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resources**  complex | List of resources  Returned: always |
| **acceleratorType**  string | The type of hardware accelerators associated with this node.  Returned: success |
| **cidrBlock**  string | The CIDR block that the TPU node will use when selecting an IP address. This CIDR block must be a /29 block; the Compute Engine networks API forbids a smaller block, and using a larger block would be wasteful (a node can only consume one IP address).  Errors will occur if the CIDR block has already been used for a currently existing TPU node, the CIDR block conflicts with any subnetworks in the user’s provided network, or the provided network is peered with another network that is using that CIDR block.  Returned: success |
| **description**  string | The user-supplied description of the TPU. Maximum of 512 characters.  Returned: success |
| **labels**  dictionary | Resource labels to represent user provided metadata.  Returned: success |
| **name**  string | The immutable name of the TPU.  Returned: success |
| **network**  string | The name of a network to peer the TPU node to. It must be a preexisting Compute Engine network inside of the project on which this API has been activated. If none is provided, “default” will be used.  Returned: success |
| **networkEndpoints**  complex | The network endpoints where TPU workers can be accessed and sent work.  It is recommended that Tensorflow clients of the node first reach out to the first (index 0) entry.  Returned: success |
| **ipAddress**  string | The IP address of this network endpoint.  Returned: success |
| **port**  integer | The port of this network endpoint.  Returned: success |
| **schedulingConfig**  complex | Sets the scheduling options for this TPU instance.  Returned: success |
| **preemptible**  boolean | Defines whether the TPU instance is preemptible.  Returned: success |
| **serviceAccount**  string | The service account used to run the tensor flow services within the node. To share resources, including Google Cloud Storage data, with the Tensorflow job running in the Node, this account must have permissions to that data.  Returned: success |
| **tensorflowVersion**  string | The version of Tensorflow running in the Node.  Returned: success |
| **useServiceNetworking**  boolean | Whether the VPC peering for the node is set up through Service Networking API.  The VPC Peering should be set up before provisioning the node. If this field is set, cidr_block field should not be specified. If the network that you want to peer the TPU Node to is a Shared VPC network, the node must be created with this this field enabled.  Returned: success |
| **zone**  string | The GCP location for the TPU. If it is not provided, the provider zone is used.  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
