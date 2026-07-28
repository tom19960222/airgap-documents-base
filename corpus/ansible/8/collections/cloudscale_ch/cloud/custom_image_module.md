---
collection: ansible
version: "8"
title: "cloudscale_ch.cloud.custom_image module – Manage custom images on the cloudscale.ch IaaS service"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cloudscale_ch/cloud/custom_image_module.html
fetched_at: 2026-07-28T01:39:52+00:00
---
# cloudscale_ch.cloud.custom_image module – Manage custom images on the cloudscale.ch IaaS service

> **Note:**
>
> This module is part of the [cloudscale_ch.cloud collection](https://galaxy.ansible.com/ui/repo/published/cloudscale_ch/cloud/) (version 2.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cloudscale_ch.cloud`.
>
> To use it in a playbook, specify: `cloudscale_ch.cloud.custom_image`.

New in cloudscale_ch.cloud 2.2.0

- [Synopsis](custom_image_module.md#synopsis)
- [Parameters](custom_image_module.md#parameters)
- [Notes](custom_image_module.md#notes)
- [Examples](custom_image_module.md#examples)
- [Return Values](custom_image_module.md#return-values)

## [Synopsis](custom_image_module.md#id1)

- Import, modify and delete custom images.

## [Parameters](custom_image_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | Timeout in seconds for calls to the cloudscale.ch API.  This can also be passed in the `CLOUDSCALE_API_TIMEOUT` environment variable.  **Default:** `45` |
| **api_token**  string / required | cloudscale.ch API token.  This can also be passed in the `CLOUDSCALE_API_TOKEN` environment variable. |
| **api_url**  string  *added in cloudscale_ch.cloud 1.3.0* | cloudscale.ch API URL.  This can also be passed in the `CLOUDSCALE_API_URL` environment variable.  **Default:** `"https://api.cloudscale.ch/v1"` |
| **firmware_type**  string | The firmware type that will be used for servers created with this image.  **Choices:**   - `"bios"` ← (default) - `"uefi"` |
| **force_retry**  boolean | Retry the image import even if a failed import using the same name and URL already exists. This is necessary to recover from download errors.  **Choices:**   - `false` ← (default) - `true` |
| **name**  string | The human readable name of the custom image. Either name or UUID must be present to change an existing image. |
| **slug**  string | A string identifying the custom image for use within the API. |
| **source_format**  string | The file format of the image referenced in the url. Currently only raw is supported. |
| **state**  string | State of the coustom image.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  dictionary | The tags assigned to the custom image. |
| **url**  string | The URL used to download the image. |
| **user_data_handling**  string | How user_data will be handled when creating a server. There are currently two options, “pass-through” and “extend-cloud-config”.  **Choices:**   - `"pass-through"` - `"extend-cloud-config"` |
| **uuid**  string | The unique identifier of the custom image import. Either name or UUID must be present to change an existing image. |
| **zones**  list / elements=string | Specify zones in which the custom image will be available (e.g. `lpg1` or `rma1`). |

## [Notes](custom_image_module.md#id3)

> **Note:**
>
> - To import a new custom-image the *url* and *name* options are required.
> - All operations are performed using the cloudscale.ch public API v1.
> - For details consult the full API documentation: <https://www.cloudscale.ch/en/api/v1>.
> - A valid API token is required for all operations. You can create as many tokens as you like using the cloudscale.ch control panel at <https://control.cloudscale.ch>.

## [Examples](custom_image_module.md#id4)

```yaml+jinja
- name: Import custom image
  cloudscale_ch.cloud.custom_image:
    name: "My Custom Image"
    url: https://ubuntu.com/downloads/hirsute.img
    slug: my-custom-image
    user_data_handling: extend-cloud-config
    zones: lpg1
    tags:
      project: luna
    state: present
  register: my_custom_image

- name: Wait until import succeeded
  cloudscale_ch.cloud.custom_image:
    uuid: "{{ my_custom_image.uuid }}"
  retries: 15
  delay: 5
  register: image
  until: image.import_status == 'success'
  failed_when: image.import_status == 'failed'

- name: Import custom image and wait until import succeeded
  cloudscale_ch.cloud.custom_image:
    name: "My Custom Image"
    url: https://ubuntu.com/downloads/hirsute.img
    slug: my-custom-image
    user_data_handling: extend-cloud-config
    zones: lpg1
    tags:
      project: luna
    state: present
  retries: 15
  delay: 5
  register: image
  until: image.import_status == 'success'
  failed_when: image.import_status == 'failed'

- name: Import custom image with UEFI firmware type
  cloudscale_ch.cloud.custom_image:
    name: "My Custom UEFI Image"
    url: https://ubuntu.com/downloads/hirsute.img
    slug: my-custom-uefi-image
    user_data_handling: extend-cloud-config
    zones: lpg1
    firmware_type: uefi
    tags:
      project: luna
    state: present
  register: my_custom_image

- name: Update custom image
  cloudscale_ch.cloud.custom_image:
    name: "My Custom Image"
    slug: my-custom-image
    user_data_handling: extend-cloud-config
    tags:
      project: luna
    state: present

- name: Delete custom image
  cloudscale_ch.cloud.custom_image:
    uuid: '{{ my_custom_image.uuid }}'
    state: absent

- name: List all custom images
  uri:
    url: 'https://api.cloudscale.ch/v1/custom-images'
    headers:
      Authorization: 'Bearer {{ query("env", "CLOUDSCALE_API_TOKEN") }}'
    status_code: 200
  register: image_list
- name: Search the image list for all images with name 'My Custom Image'
  set_fact:
    my_custom_images: '{{ image_list.json | selectattr("name","search", "My Custom Image" ) }}'
```

## [Return Values](custom_image_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **checksums**  dictionary | The checksums of the custom image as key and value pairs. The algorithm (e.g. sha256) name is in the key and the checksum in the value. The set of algorithms used might change in the future.  **Returned:** success  **Sample:** `{"md5": "5b3a1f21cde154cfb522b582f44f1a87", "sha256": "5b03bcbd00b687e08791694e47d235a487c294e58ca3b1af704120123aa3f4e6"}` |
| **created_at**  string | The creation date and time of the resource.  **Returned:** success  **Sample:** `"2020-05-29T13:18:42.511407Z"` |
| **error_message**  string | Error message in case of a failed import.  **Returned:** success  **Sample:** `"Expected HTTP 200, got HTTP 403"` |
| **href**  string | The API URL to get details about this resource.  **Returned:** success when state == present  **Sample:** `"https://api.cloudscale.ch/v1/custom-imges/11111111-1864-4608-853a-0771b6885a3a"` |
| **import_status**  string | Shows the progress of an import. Values are one of “started”, “in_progress”, “success” or “failed”.  **Returned:** success  **Sample:** `"in_progress"` |
| **name**  string | The human readable name of the custom image.  **Returned:** success  **Sample:** `"alan"` |
| **slug**  string | A string identifying the custom image for use within the API.  **Returned:** success  **Sample:** `"foo"` |
| **state**  string | The current status of the custom image.  **Returned:** success  **Sample:** `"present"` |
| **tags**  dictionary | Tags assosiated with the custom image.  **Returned:** success  **Sample:** `{"project": "my project"}` |
| **user_data_handling**  string | How user_data will be handled when creating a server. There are currently two options, “pass-through” and “extend-cloud-config”.  **Returned:** success  **Sample:** `"pass-through"` |
| **uuid**  string | The unique identifier of the custom image.  **Returned:** success  **Sample:** `"11111111-1864-4608-853a-0771b6885a3a"` |

### Authors

- Ciril Troxler (@ctx)
- Gaudenz Steinlin (@gaudenz)

### Collection links

- [Issue Tracker](https://github.com/cloudscale-ch/ansible-collection-cloudscale/issues)
- [Repository (Sources)](https://github.com/cloudscale-ch/ansible-collection-cloudscale)
