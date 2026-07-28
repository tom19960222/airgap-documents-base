---
collection: ansible
version: "6"
title: "google.cloud.gcp_compute_reservation module – Creates a GCP Reservation"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_compute_reservation_module.html
fetched_at: 2026-07-27T17:48:30+00:00
---
# google.cloud.gcp_compute_reservation module – Creates a GCP Reservation

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
> see [Requirements](gcp_compute_reservation_module.md#ansible-collections-google-cloud-gcp-compute-reservation-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_reservation`.

- [Synopsis](gcp_compute_reservation_module.md#synopsis)
- [Requirements](gcp_compute_reservation_module.md#requirements)
- [Parameters](gcp_compute_reservation_module.md#parameters)
- [Notes](gcp_compute_reservation_module.md#notes)
- [Examples](gcp_compute_reservation_module.md#examples)
- [Return Values](gcp_compute_reservation_module.md#return-values)

## [Synopsis](gcp_compute_reservation_module.md#id1)

- Represents a reservation resource. A reservation ensures that capacity is held in a specific zone even if the reserved VMs are not running.
- Reservations apply only to Compute Engine, Cloud Dataproc, and Google Kubernetes Engine VM usage.Reservations do not apply to `f1-micro` or `g1-small` machine types, preemptible VMs, sole tenant nodes, or other services not listed above like Cloud SQL and Dataflow.

## [Requirements](gcp_compute_reservation_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_reservation_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **description**  string | An optional description of this resource. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **name**  string / required | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **specific_reservation**  dictionary / required | Reservation for instances with specific machine shapes. |
| **count**  integer / required | The number of resources that are allocated. |
| **instance_properties**  dictionary / required | The instance properties for the reservation. |
| **guest_accelerators**  list / elements=dictionary | Guest accelerator type and count. |
| **accelerator_count**  integer / required | The number of the guest accelerator cards exposed to this instance. |
| **accelerator_type**  string / required | The full or partial URL of the accelerator type to attach to this instance. For example: `projects/my-project/zones/us-central1-c/acceleratorTypes/nvidia-tesla-p100` If you are creating an instance template, specify only the accelerator name. |
| **local_ssds**  list / elements=dictionary | The amount of local ssd to reserve with each instance. This reserves disks of type `local-ssd`. |
| **disk_size_gb**  integer / required | The size of the disk in base-2 GB. |
| **interface**  string | The disk interface to use for attaching this disk.  Some valid choices include: “SCSI”, “NVME”  Default: `"SCSI"` |
| **machine_type**  string / required | The name of the machine type to reserve. |
| **min_cpu_platform**  string | The minimum CPU platform for the reservation. For example, `”Intel Skylake”`. See <https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform#availablezones> for information on available CPU platforms. |
| **specific_reservation_required**  boolean | When set to true, only VMs that target this reservation by name can consume this reservation. Otherwise, it can be consumed by VMs with affinity for any reservation. Defaults to false.  Choices:   - `false` ← (default) - `true` |
| **state**  string | Whether the given object should exist in GCP  Choices:   - `"present"` ← (default) - `"absent"` |
| **zone**  string / required | The zone where the reservation is made. |

## [Notes](gcp_compute_reservation_module.md#id4)

> **Note:**
>
> - API Reference: <https://cloud.google.com/compute/docs/reference/rest/v1/reservations>
> - Reserving zonal resources: <https://cloud.google.com/compute/docs/instances/reserving-zonal-resources>
> - for authentication, you can set service_account_file using the `gcp_service_account_file` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_compute_reservation_module.md#id5)

```yaml+jinja
- name: create a reservation
  google.cloud.gcp_compute_reservation:
    name: test_object
    zone: us-central1-a
    specific_reservation:
      count: 1
      instance_properties:
        min_cpu_platform: Intel Cascade Lake
        machine_type: n2-standard-2
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_compute_reservation_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commitment**  string | Full or partial URL to a parent commitment. This field displays for reservations that are tied to a commitment.  Returned: success |
| **creationTimestamp**  string | Creation timestamp in RFC3339 text format.  Returned: success |
| **description**  string | An optional description of this resource.  Returned: success |
| **id**  integer | The unique identifier for the resource.  Returned: success |
| **name**  string | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  Returned: success |
| **specificReservation**  complex | Reservation for instances with specific machine shapes.  Returned: success |
| **count**  integer | The number of resources that are allocated.  Returned: success |
| **instanceProperties**  complex | The instance properties for the reservation.  Returned: success |
| **guestAccelerators**  complex | Guest accelerator type and count.  Returned: success |
| **acceleratorCount**  integer | The number of the guest accelerator cards exposed to this instance.  Returned: success |
| **acceleratorType**  string | The full or partial URL of the accelerator type to attach to this instance. For example: `projects/my-project/zones/us-central1-c/acceleratorTypes/nvidia-tesla-p100` If you are creating an instance template, specify only the accelerator name.  Returned: success |
| **localSsds**  complex | The amount of local ssd to reserve with each instance. This reserves disks of type `local-ssd`.  Returned: success |
| **diskSizeGb**  integer | The size of the disk in base-2 GB.  Returned: success |
| **interface**  string | The disk interface to use for attaching this disk.  Returned: success |
| **machineType**  string | The name of the machine type to reserve.  Returned: success |
| **minCpuPlatform**  string | The minimum CPU platform for the reservation. For example, `”Intel Skylake”`. See <https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform#availablezones> for information on available CPU platforms.  Returned: success |
| **inUseCount**  integer | How many instances are in use.  Returned: success |
| **specificReservationRequired**  boolean | When set to true, only VMs that target this reservation by name can consume this reservation. Otherwise, it can be consumed by VMs with affinity for any reservation. Defaults to false.  Returned: success |
| **status**  string | The status of the reservation.  Returned: success |
| **zone**  string | The zone where the reservation is made.  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
