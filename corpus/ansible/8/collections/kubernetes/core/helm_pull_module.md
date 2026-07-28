---
collection: ansible
version: "8"
title: "kubernetes.core.helm_pull module – download a chart from a repository and (optionally) unpack it in local directory."
source_url: https://docs.ansible.com/projects/ansible/8/collections/kubernetes/core/helm_pull_module.html
fetched_at: 2026-07-28T02:40:06+00:00
---
# kubernetes.core.helm_pull module – download a chart from a repository and (optionally) unpack it in local directory.

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
> see [Requirements](helm_pull_module.md#ansible-collections-kubernetes-core-helm-pull-module-requirements) for details.
>
> To use it in a playbook, specify: `kubernetes.core.helm_pull`.

New in kubernetes.core 2.4.0

- [Synopsis](helm_pull_module.md#synopsis)
- [Requirements](helm_pull_module.md#requirements)
- [Parameters](helm_pull_module.md#parameters)
- [Examples](helm_pull_module.md#examples)
- [Return Values](helm_pull_module.md#return-values)

## [Synopsis](helm_pull_module.md#id1)

- Retrieve a package from a package repository, and download it locally.
- It can also be used to perform cryptographic verification of a chart without installing the chart.
- There are options for unpacking the chart after download.

## [Requirements](helm_pull_module.md#id2)

The below requirements are needed on the host that executes this module.

- helm >= 3.0 (<https://github.com/helm/helm/releases>)

## [Parameters](helm_pull_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **binary_path**  path | The path of a helm binary to use. |
| **chart_ca_cert**  path | Verify certificates of HTTPS-enabled servers using this CA bundle.  Requires helm >= 3.1.0. |
| **chart_devel**  boolean | Use development versions, too. Equivalent to version ‘>0.0.0-0’.  Mutually exclusive with `chart_version`.  **Choices:**   - `false` - `true` |
| **chart_ref**  string / required | chart name on chart repository.  absolute URL. |
| **chart_ssl_cert_file**  path | Identify HTTPS client using this SSL certificate file.  Requires helm >= 3.1.0. |
| **chart_ssl_key_file**  path | Identify HTTPS client using this SSL key file  Requires helm >= 3.1.0. |
| **chart_version**  string | Specify a version constraint for the chart version to use.  This constraint can be a specific tag (e.g. 1.1.1) or it may reference a valid range (e.g. ^2.0.0).  Mutually exclusive with `chart_devel`. |
| **destination**  path / required | location to write the chart. |
| **pass_credentials**  boolean | Pass credentials to all domains.  **Choices:**   - `false` ← (default) - `true` |
| **provenance**  boolean | Fetch the provenance file, but don’t perform verification.  **Choices:**   - `false` ← (default) - `true` |
| **repo_password**  aliases: password, chart_repo_password  string | Chart repository password where to locate the requested chart.  Required if `repo_username` is specified. |
| **repo_url**  aliases: url, chart_repo_url  string | chart repository url where to locate the requested chart. |
| **repo_username**  aliases: username, chart_repo_username  string | Chart repository username where to locate the requested chart.  Required if `repo_password` is specified. |
| **skip_tls_certs_check**  boolean | Whether or not to check tls certificate for the chart download.  Requires helm >= 3.3.0.  **Choices:**   - `false` ← (default) - `true` |
| **untar_chart**  boolean | if set to true, will untar the chart after downloading it.  **Choices:**   - `false` ← (default) - `true` |
| **verify_chart**  boolean | Verify the package before using it.  **Choices:**   - `false` ← (default) - `true` |
| **verify_chart_keyring**  path | location of public keys used for verification. |

## [Examples](helm_pull_module.md#id4)

```yaml+jinja
- name: Download chart using chart url
  kubernetes.core.helm_pull:
    chart_ref: https://github.com/grafana/helm-charts/releases/download/grafana-5.6.0/grafana-5.6.0.tgz
    destination: /path/to/chart

- name: Download Chart using chart_name and repo_url
  kubernetes.core.helm_pull:
    chart_ref: redis
    repo_url: https://charts.bitnami.com/bitnami
    untar_chart: yes
    destination: /path/to/chart

- name: Download Chart (skip tls certificate check)
  kubernetes.core.helm_pull:
    chart_ref: redis
    repo_url: https://charts.bitnami.com/bitnami
    untar_chart: yes
    destination: /path/to/chart
    skip_tls_certs_check: yes

- name: Download Chart using chart registry credentials
  kubernetes.core.helm_pull:
    chart_ref: redis
    repo_url: https://charts.bitnami.com/bitnami
    untar_chart: yes
    destination: /path/to/chart
    username: myuser
    password: mypassword123
```

## [Return Values](helm_pull_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **command**  string | Full `helm pull` command built by this module, in case you want to re-run the command outside the module or debug a problem.  **Returned:** always  **Sample:** `"helm pull --repo test ..."` |
| **rc**  integer | Helm pull command return code  **Returned:** always  **Sample:** `1` |
| **stderr**  string | Full `helm pull` command stderr, in case you want to display it or examine the event log  **Returned:** always  **Sample:** `""` |
| **stdout**  string | Full `helm pull` command stdout, in case you want to display it or examine the event log  **Returned:** always  **Sample:** `""` |

### Authors

- Aubin Bikouo (@abikouo)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/kubernetes.core/issues)
- [Repository (Sources)](https://github.com/ansible-collections/kubernetes.core)
