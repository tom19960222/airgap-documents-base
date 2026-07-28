---
collection: ansible
version: "8"
title: "kubernetes.core.helm_template module – Render chart templates"
source_url: https://docs.ansible.com/projects/ansible/8/collections/kubernetes/core/helm_template_module.html
fetched_at: 2026-07-28T02:40:08+00:00
---
# kubernetes.core.helm_template module – Render chart templates

> **Note:**
>
> This module is part of the [kubernetes.core collection](https://galaxy.ansible.com/ui/repo/published/kubernetes/core/) (version 2.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install kubernetes.core`.
>
> To use it in a playbook, specify: `kubernetes.core.helm_template`.

- [Synopsis](helm_template_module.md#synopsis)
- [Parameters](helm_template_module.md#parameters)
- [Examples](helm_template_module.md#examples)
- [Return Values](helm_template_module.md#return-values)

## [Synopsis](helm_template_module.md#id1)

- Render chart templates to an output directory or as text of concatenated yaml documents.

## [Parameters](helm_template_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **binary_path**  path | The path of a helm binary to use. |
| **chart_ref**  path / required | Chart reference with repo prefix, for example, `nginx-stable/nginx-ingress`.  Path to a packaged chart.  Path to an unpacked chart directory.  Absolute URL. |
| **chart_repo_url**  string | Chart repository URL where the requested chart is located. |
| **chart_version**  string | Chart version to use. If this is not specified, the latest version is installed. |
| **dependency_update**  aliases: dep_up  boolean  *added in kubernetes.core 2.4.0* | Run helm dependency update before the operation.  The *dependency_update* option require the add of `dependencies` block in `Chart.yaml/requirements.yaml` file.  For more information please visit <https://helm.sh/docs/helm/helm_dependency/>  **Choices:**   - `false` ← (default) - `true` |
| **disable_hook**  boolean  *added in kubernetes.core 2.4.0* | Prevent hooks from running during install.  **Choices:**   - `false` ← (default) - `true` |
| **include_crds**  boolean | Include custom resource descriptions in rendered templates.  **Choices:**   - `false` ← (default) - `true` |
| **output_dir**  path | Output directory where templates will be written.  If the directory already exists, it will be overwritten. |
| **release_name**  aliases: name  string  *added in kubernetes.core 2.4.0* | Release name to use in rendered templates. |
| **release_namespace**  string  *added in kubernetes.core 2.4.0* | namespace scope for this request. |
| **release_values**  aliases: values  dictionary | Values to pass to chart.  **Default:** `{}` |
| **set_values**  list / elements=dictionary  *added in kubernetes.core 2.4.0* | Values to pass to chart configuration. |
| **value**  string / required | Value to pass to chart configuration (e.g phase=prod). |
| **value_type**  string | Use `raw` set individual value.  Use `string` to force a string for an individual value.  Use `file` to set individual values from a file when the value itself is too long for the command line or is dynamically generated.  Use `json` to set json values (scalars/objects/arrays). This feature requires helm>=3.10.0.  **Choices:**   - `"raw"` ← (default) - `"string"` - `"json"` - `"file"` |
| **show_only**  list / elements=string  *added in kubernetes.core 2.4.0* | Only show manifests rendered from the given templates. |
| **update_repo_cache**  boolean | Run `helm repo update` before the operation. Can be run as part of the template generation or as a separate step.  **Choices:**   - `false` ← (default) - `true` |
| **values_files**  list / elements=string | Value files to pass to chart.  Paths will be read from the target host’s filesystem, not the host running ansible.  *values_files* option is evaluated before *values* option if both are used.  Paths are evaluated in the order the paths are specified.  **Default:** `[]` |

## [Examples](helm_template_module.md#id3)

```yaml+jinja
- name: Render templates to specified directory
  kubernetes.core.helm_template:
    chart_ref: stable/prometheus
    output_dir: mycharts

- name: Render templates
  kubernetes.core.helm_template:
    chart_ref: stable/prometheus
  register: result

- name: Write templates to file
  copy:
    dest: myfile.yaml
    content: "{{ result.stdout }}"

- name: Render MutatingWebhooksConfiguration for revision tag "canary", rev "1-13-0"
  kubernetes.core.helm_template:
    chart_ref: istio/istiod
    chart_version: "1.13.0"
    release_namespace: "istio-system"
    show_only:
      - "templates/revision-tags.yaml"
    release_values:
      revision: "1-13-0"
      revisionTags:
        - "canary"
  register: result

- name: Write templates to file
  copy:
    dest: myfile.yaml
    content: "{{ result.stdout }}"
```

## [Return Values](helm_template_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **command**  string | Full `helm` command run by this module, in case you want to re-run the command outside the module or debug a problem.  **Returned:** always  **Sample:** `"helm template --output-dir mychart nginx-stable/nginx-ingress"` |
| **stderr**  string | Full `helm` command stderr, in case you want to display it or examine the event log.  **Returned:** always  **Sample:** `""` |
| **stdout**  string | Full `helm` command stdout. If no *output_dir* has been provided this will contain the rendered templates as concatenated yaml documents.  **Returned:** always  **Sample:** `""` |

### Authors

- Mike Graves (@gravesm)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/kubernetes.core/issues)
- [Repository (Sources)](https://github.com/ansible-collections/kubernetes.core)
