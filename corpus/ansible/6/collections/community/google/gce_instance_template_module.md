---
collection: ansible
version: "6"
title: "community.google.gce_instance_template module – create or destroy instance templates of Compute Engine of GCP."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/google/gce_instance_template_module.html
fetched_at: 2026-07-27T17:15:17+00:00
---
# community.google.gce_instance_template module – create or destroy instance templates of Compute Engine of GCP.

> **Note:**
>
> This module is part of the [community.google collection](https://galaxy.ansible.com/community/google) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.google`.
> You need further requirements to be able to use this module,
> see [Requirements](gce_instance_template_module.md#ansible-collections-community-google-gce-instance-template-module-requirements) for details.
>
> To use it in a playbook, specify: `community.google.gce_instance_template`.

- [Synopsis](gce_instance_template_module.md#synopsis)
- [Requirements](gce_instance_template_module.md#requirements)
- [Parameters](gce_instance_template_module.md#parameters)
- [Notes](gce_instance_template_module.md#notes)
- [Examples](gce_instance_template_module.md#examples)

## [Synopsis](gce_instance_template_module.md#id1)

- Creates or destroy Google instance templates of Compute Engine of Google Cloud Platform.

## [Requirements](gce_instance_template_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- apache-libcloud >= 0.13.3, >= 0.17.0 if using JSON credentials, >= 0.20.0 if using preemptible option

## [Parameters](gce_instance_template_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **automatic_restart**  boolean | Defines whether the instance should be automatically restarted when it is terminated by Compute Engine.  Choices:   - `false` - `true` |
| **can_ip_forward**  boolean | Set to `yes` to allow instance to send/receive non-matching src/dst packets.  Choices:   - `false` ← (default) - `true` |
| **credentials_file**  path | path to the JSON file associated with the service account email |
| **description**  string | description of instance template |
| **disk_auto_delete**  boolean | Indicate that the boot disk should be deleted when the Node is deleted.  Choices:   - `false` - `true` ← (default) |
| **disk_type**  string | Specify a `pd-standard` disk or `pd-ssd` for an SSD disk.  Choices:   - `"pd-standard"` ← (default) - `"pd-ssd"` |
| **disks**  list / elements=string | a list of persistent disks to attach to the instance; a string value gives the name of the disk; alternatively, a dictionary value can define ‘name’ and ‘mode’ (‘READ_ONLY’ or ‘READ_WRITE’). The first entry will be the boot disk (which must be READ_WRITE). |
| **disks_gce_struct**  list / elements=string | Support passing in the GCE-specific formatted formatted disks[] structure. Case sensitive. see <https://cloud.google.com/compute/docs/reference/latest/instanceTemplates#resource> for detailed information |
| **external_ip**  string | The external IP address to use. If `ephemeral`, a new non-static address will be used. If `None`, then no external address will be used. To use an existing static IP address specify address name.  Default: `"ephemeral"` |
| **image**  string | The image to use to create the instance. Cannot specify both both *image* and *source*. |
| **image_family**  string | The image family to use to create the instance. If *image* has been used *image_family* is ignored. Cannot specify both *image* and *source*.  Default: `"debian-8"` |
| **metadata**  string | a hash/dictionary of custom data for the instance; ‘{“key”:”value”, …}’ |
| **name**  aliases: base_name  string / required | The name of the GCE instance template. |
| **network**  string | The network to associate with the instance.  Default: `"default"` |
| **nic_gce_struct**  list / elements=string | Support passing in the GCE-specific formatted networkInterfaces[] structure. |
| **pem_file**  path | path to the pem file associated with the service account email This option is deprecated. Use ‘credentials_file’. |
| **preemptible**  boolean | Defines whether the instance is preemptible.  Choices:   - `false` - `true` |
| **project_id**  string | your GCE project ID |
| **service_account_email**  string | service account email |
| **service_account_permissions**  list / elements=string | service account permissions (see <https://cloud.google.com/sdk/gcloud/reference/compute/instances/create>, –scopes section for detailed information)  Available choices are: `bigquery`, `cloud-platform`, `compute-ro`, `compute-rw`, `useraccounts-ro`, `useraccounts-rw`, `datastore`, `logging-write`, `monitoring`, `sql-admin`, `storage-full`, `storage-ro`, `storage-rw`, `taskqueue`, `userinfo-email`. |
| **size**  string | The desired machine type for the instance template.  Default: `"f1-micro"` |
| **source**  string | A source disk to attach to the instance. Cannot specify both *image* and *source*. |
| **state**  string | The desired state for the instance template.  Choices:   - `"present"` ← (default) - `"absent"` |
| **subnetwork**  string | The Subnetwork resource name for this instance. |
| **subnetwork_region**  string | Region that subnetwork resides in. (Required for subnetwork to successfully complete) |
| **tags**  list / elements=string | a comma-separated list of tags to associate with the instance |

## [Notes](gce_instance_template_module.md#id4)

> **Note:**
>
> - JSON credentials strongly preferred.

## [Examples](gce_instance_template_module.md#id5)

```yaml+jinja
# Usage
- name: Create instance template named foo
  community.google.gce_instance_template:
    name: foo
    size: n1-standard-1
    image_family: ubuntu-1604-lts
    state: present
    project_id: "your-project-name"
    credentials_file: "/path/to/your-key.json"
    service_account_email: "your-sa@your-project-name.iam.gserviceaccount.com"

# Example Playbook
- name: Compute Engine Instance Template Examples
  hosts: localhost
  vars:
    service_account_email: "your-sa@your-project-name.iam.gserviceaccount.com"
    credentials_file: "/path/to/your-key.json"
    project_id: "your-project-name"
  tasks:
    - name: Create instance template
      community.google.gce_instance_template:
        name: my-test-instance-template
        size: n1-standard-1
        image_family: ubuntu-1604-lts
        state: present
        project_id: "{{ project_id }}"
        credentials_file: "{{ credentials_file }}"
        service_account_email: "{{ service_account_email }}"
    - name: Delete instance template
      community.google.gce_instance_template:
        name: my-test-instance-template
        size: n1-standard-1
        image_family: ubuntu-1604-lts
        state: absent
        project_id: "{{ project_id }}"
        credentials_file: "{{ credentials_file }}"
        service_account_email: "{{ service_account_email }}"

# Example playbook using disks_gce_struct
- name: Compute Engine Instance Template Examples
  hosts: localhost
  vars:
    service_account_email: "your-sa@your-project-name.iam.gserviceaccount.com"
    credentials_file: "/path/to/your-key.json"
    project_id: "your-project-name"
  tasks:
    - name: Create instance template
      community.google.gce_instance_template:
        name: foo
        size: n1-standard-1
        state: present
        project_id: "{{ project_id }}"
        credentials_file: "{{ credentials_file }}"
        service_account_email: "{{ service_account_email }}"
        disks_gce_struct:
          - device_name: /dev/sda
            boot: true
            autoDelete: true
            initializeParams:
              diskSizeGb: 30
              diskType: pd-ssd
              sourceImage: projects/debian-cloud/global/images/family/debian-8
```

### Authors

- Gwenael Pellen (@GwenaelPellenArkeup)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.google/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.google)
