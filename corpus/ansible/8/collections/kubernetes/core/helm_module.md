---
collection: ansible
version: "8"
title: "kubernetes.core.helm module – Manages Kubernetes packages with the Helm package manager"
source_url: https://docs.ansible.com/projects/ansible/8/collections/kubernetes/core/helm_module.html
fetched_at: 2026-07-28T02:40:03+00:00
---
# kubernetes.core.helm module – Manages Kubernetes packages with the Helm package manager

> **Note:**
>
> This module is part of the [kubernetes.core collection](https://galaxy.ansible.com/ui/repo/published/kubernetes/core/) (version 2.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install kubernetes.core`.
> You need further requirements to be able to use this module,
> see [Requirements](helm_module.md#ansible-collections-kubernetes-core-helm-module-requirements) for details.
>
> To use it in a playbook, specify: `kubernetes.core.helm`.

New in kubernetes.core 0.11.0

- [Synopsis](helm_module.md#synopsis)
- [Requirements](helm_module.md#requirements)
- [Parameters](helm_module.md#parameters)
- [Notes](helm_module.md#notes)
- [Examples](helm_module.md#examples)
- [Return Values](helm_module.md#return-values)

## [Synopsis](helm_module.md#id1)

- Install, upgrade, delete packages with the Helm package manager.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](helm_module.md#id2)

The below requirements are needed on the host that executes this module.

- helm (<https://github.com/helm/helm/releases>)
- yaml (<https://pypi.org/project/PyYAML/>)

## [Parameters](helm_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_key**  string  *added in kubernetes.core 1.2.0* | Token used to authenticate with the API. Can also be specified via `K8S_AUTH_API_KEY` environment variable. |
| **atomic**  boolean | If set, the installation process deletes the installation on failure.  **Choices:**   - `false` ← (default) - `true` |
| **binary_path**  path | The path of a helm binary to use. |
| **ca_cert**  aliases: ssl_ca_cert  path  *added in kubernetes.core 1.2.0* | Path to a CA certificate used to authenticate with the API. The full certificate chain must be provided to avoid certificate validation errors. Can also be specified via `K8S_AUTH_SSL_CA_CERT` environment variable. |
| **chart_ref**  path | chart_reference on chart repository.  path to a packaged chart.  path to an unpacked chart directory.  absolute URL.  Required when *release_state* is set to `present`. |
| **chart_repo_url**  string | Chart repository URL where to locate the requested chart. |
| **chart_version**  string | Chart version to install. If this is not specified, the latest version is installed. |
| **context**  aliases: kube_context  string | Helm option to specify which kubeconfig context to use.  If the value is not specified in the task, the value of environment variable `K8S_AUTH_CONTEXT` will be used instead. |
| **create_namespace**  boolean  *added in kubernetes.core 0.11.1* | Create the release namespace if not present.  **Choices:**   - `false` ← (default) - `true` |
| **dependency_update**  aliases: dep_up  boolean  *added in kubernetes.core 2.4.0* | Run standalone `helm dependency update CHART` before the operation.  Run inline `--dependency-update` with `helm install` command. This feature is not supported yet with the `helm upgrade` command.  So we should consider to use *dependency_update* options with *replace* option enabled when specifying *chart_repo_url*.  The *dependency_update* option require the add of `dependencies` block in `Chart.yaml/requirements.yaml` file.  For more information please visit <https://helm.sh/docs/helm/helm_dependency/>  **Choices:**   - `false` ← (default) - `true` |
| **disable_hook**  boolean | Helm option to disable hook on install/upgrade/delete.  **Choices:**   - `false` ← (default) - `true` |
| **force**  boolean | Helm option to force reinstall, ignore on new install.  **Choices:**   - `false` ← (default) - `true` |
| **history_max**  integer  *added in kubernetes.core 2.2.0* | Limit the maximum number of revisions saved per release.  mutually exclusive with with `replace`. |
| **host**  string  *added in kubernetes.core 1.2.0* | Provide a URL for accessing the API. Can also be specified via `K8S_AUTH_HOST` environment variable. |
| **kubeconfig**  aliases: kubeconfig_path  any | Helm option to specify kubeconfig path to use.  If the value is not specified in the task, the value of environment variable `K8S_AUTH_KUBECONFIG` will be used instead.  The configuration can be provided as dictionary. Added in version 2.4.0. |
| **post_renderer**  string  *added in kubernetes.core 2.4.0* | Path to an executable to be used for post rendering. |
| **purge**  boolean | Remove the release from the store and make its name free for later use.  **Choices:**   - `false` - `true` ← (default) |
| **release_name**  aliases: name  string / required | Release name to manage. |
| **release_namespace**  aliases: namespace  string / required | Kubernetes namespace where the chart should be installed. |
| **release_state**  aliases: state  string | Desirated state of release.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **release_values**  aliases: values  dictionary | Value to pass to chart.  **Default:** `{}` |
| **replace**  boolean  *added in kubernetes.core 1.11.0* | Reuse the given name, only if that name is a deleted release which remains in the history.  This is unsafe in production environment.  mutually exclusive with with `history_max`.  **Choices:**   - `false` ← (default) - `true` |
| **set_values**  list / elements=dictionary  *added in kubernetes.core 2.4.0* | Values to pass to chart configuration |
| **value**  string / required | Value to pass to chart configuration (e.g phase=prod). |
| **value_type**  string | Use `raw` set individual value.  Use `string` to force a string for an individual value.  Use `file` to set individual values from a file when the value itself is too long for the command line or is dynamically generated.  Use `json` to set json values (scalars/objects/arrays). This feature requires helm>=3.10.0.  **Choices:**   - `"raw"` ← (default) - `"string"` - `"json"` - `"file"` |
| **skip_crds**  boolean  *added in kubernetes.core 1.2.0* | Skip custom resource definitions when installing or upgrading.  **Choices:**   - `false` ← (default) - `true` |
| **timeout**  string  *added in kubernetes.core 2.3.0* | A Go duration (described here *https://pkg.go.dev/time#ParseDuration*) value to wait for Kubernetes commands to complete. This defaults to 5m0s.  similar to `wait_timeout` but does not required `wait` to be activated.  Mutually exclusive with `wait_timeout`. |
| **update_repo_cache**  boolean | Run `helm repo update` before the operation. Can be run as part of the package installation or as a separate step (see Examples).  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  aliases: verify_ssl  boolean  *added in kubernetes.core 1.2.0* | Whether or not to verify the API server’s SSL certificates. Can also be specified via `K8S_AUTH_VERIFY_SSL` environment variable.  **Choices:**   - `false` - `true` ← (default) |
| **values_files**  list / elements=string  *added in kubernetes.core 1.1.0* | Value files to pass to chart.  Paths will be read from the target host’s filesystem, not the host running ansible.  values_files option is evaluated before values option if both are used.  Paths are evaluated in the order the paths are specified.  **Default:** `[]` |
| **wait**  boolean | When *release_state* is set to `present`, wait until all Pods, PVCs, Services, and minimum number of Pods of a Deployment are in a ready state before marking the release as successful.  When *release_state* is set to `absent`, will wait until all the resources are deleted before returning. It will wait for as long as *wait_timeout*. This feature requires helm>=3.7.0. Added in version 2.3.0.  **Choices:**   - `false` ← (default) - `true` |
| **wait_timeout**  string | Timeout when wait option is enabled (helm2 is a number of seconds, helm3 is a duration).  The use of *wait_timeout* to wait for kubernetes commands to complete has been deprecated and will be removed after 2022-12-01. |

## [Notes](helm_module.md#id4)

> **Note:**
>
> - The default idempotency check can fail to report changes when `release_state` is set to `present` and `chart_repo_url` is defined. Install helm diff >= 3.4.1 for better results.

## [Examples](helm_module.md#id5)

```yaml+jinja
- name: Deploy latest version of Prometheus chart inside monitoring namespace (and create it)
  kubernetes.core.helm:
    name: test
    chart_ref: stable/prometheus
    release_namespace: monitoring
    create_namespace: true

# From repository
- name: Add stable chart repo
  kubernetes.core.helm_repository:
    name: stable
    repo_url: "https://kubernetes.github.io/ingress-nginx"

- name: Deploy latest version of Grafana chart inside monitoring namespace with values
  kubernetes.core.helm:
    name: test
    chart_ref: stable/grafana
    release_namespace: monitoring
    values:
      replicas: 2

- name: Deploy Grafana chart on 5.0.12 with values loaded from template
  kubernetes.core.helm:
    name: test
    chart_ref: stable/grafana
    chart_version: 5.0.12
    values: "{{ lookup('template', 'somefile.yaml') | from_yaml }}"

- name: Deploy Grafana chart using values files on target
  kubernetes.core.helm:
    name: test
    chart_ref: stable/grafana
    release_namespace: monitoring
    values_files:
      - /path/to/values.yaml

- name: Remove test release and waiting suppression ending
  kubernetes.core.helm:
    name: test
    state: absent
    wait: true

- name: Separately update the repository cache
  kubernetes.core.helm:
    name: dummy
    namespace: kube-system
    state: absent
    update_repo_cache: true

- name: Deploy Grafana chart using set values on target
  kubernetes.core.helm:
    name: test
    chart_ref: stable/grafana
    release_namespace: monitoring
    set_values:
      - value: phase=prod
        value_type: string

# From git
- name: Git clone stable repo on HEAD
  ansible.builtin.git:
    repo: "http://github.com/helm/charts.git"
    dest: /tmp/helm_repo

- name: Deploy Grafana chart from local path
  kubernetes.core.helm:
    name: test
    chart_ref: /tmp/helm_repo/stable/grafana
    release_namespace: monitoring

# From url
- name: Deploy Grafana chart on 5.6.0 from url
  kubernetes.core.helm:
    name: test
    chart_ref: "https://github.com/grafana/helm-charts/releases/download/grafana-5.6.0/grafana-5.6.0.tgz"
    release_namespace: monitoring

# Using complex Values
- name: Deploy new-relic client chart
  kubernetes.core.helm:
    name: newrelic-bundle
    chart_ref: newrelic/nri-bundle
    release_namespace: default
    force: True
    wait: True
    replace: True
    update_repo_cache: True
    disable_hook: True
    values:
      global:
        licenseKey: "{{ nr_license_key }}"
        cluster: "{{ site_name }}"
      newrelic-infrastructure:
        privileged: True
      ksm:
        enabled: True
      prometheus:
        enabled: True
      kubeEvents:
        enabled: True
      logging:
        enabled: True
```

## [Return Values](helm_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **command**  string | Full `helm` command built by this module, in case you want to re-run the command outside the module or debug a problem.  **Returned:** always  **Sample:** `"helm upgrade ..."` |
| **status**  complex | A dictionary of status output  **Returned:** on success Creation/Upgrade/Already deploy |
| **appversion**  string | Version of app deployed  **Returned:** always |
| **chart**  string | Chart name and chart version  **Returned:** always |
| **name**  string | Name of the release  **Returned:** always |
| **namespace**  string | Namespace where the release is deployed  **Returned:** always |
| **revision**  string | Number of time where the release has been updated  **Returned:** always |
| **status**  string | Status of release (can be DEPLOYED, FAILED, …)  **Returned:** always |
| **updated**  string | The Date of last update  **Returned:** always |
| **values**  string | Dict of Values used to deploy  **Returned:** always |
| **stderr**  string | Full `helm` command stderr, in case you want to display it or examine the event log  **Returned:** always  **Sample:** `""` |
| **stdout**  string | Full `helm` command stdout, in case you want to display it or examine the event log  **Returned:** always  **Sample:** `""` |

### Authors

- Lucas Boisserie (@LucasBoisserie)
- Matthieu Diehr (@d-matt)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/kubernetes.core/issues)
- [Repository (Sources)](https://github.com/ansible-collections/kubernetes.core)
