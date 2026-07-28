---
collection: ansible
version: "6"
title: "Introduction to Ansible for Kubernetes"
source_url: https://docs.ansible.com/projects/ansible/6/collections/kubernetes/core/docsite/kubernetes_scenarios/k8s_intro.html
fetched_at: 2026-07-28T00:25:21+00:00
---
# Introduction to Ansible for Kubernetes

- [Introduction](k8s_intro.md#introduction)
- [Requirements](k8s_intro.md#requirements)
- [Installation](k8s_intro.md#installation)
- [Authenticating with the API](k8s_intro.md#authenticating-with-the-api)
- [Reporting an issue](k8s_intro.md#reporting-an-issue)

## [Introduction](k8s_intro.md#id1)

The [kubernetes.core collection](https://galaxy.ansible.com/kubernetes/core) offers several modules and plugins for orchestrating Kubernetes.

## [Requirements](k8s_intro.md#id2)

To use the modules, you’ll need the following:

- Ansible 2.9.17 or latest installed
- [Kubernetes Python client](https://pypi.org/project/kubernetes/) installed on the host that will execute the modules.

## [Installation](k8s_intro.md#id3)

The Kubernetes modules are part of the Ansible Kubernetes collection.

To install the collection, run the following:

```bash
$ ansible-galaxy collection install kubernetes.core
```

## [Authenticating with the API](k8s_intro.md#id4)

By default the Kubernetes Rest Client will look for `~/.kube/config`, and if found, connect using the active context. You can override the location of the file using the `kubeconfig` parameter, and the context, using the `context` parameter.

Basic authentication is also supported using the `username` and `password` options. You can override the URL using the `host` parameter. Certificate authentication works through the `ssl_ca_cert`, `cert_file`, and `key_file` parameters, and for token authentication, use the `api_key` parameter.

To disable SSL certificate verification, set `verify_ssl` to false.

## [Reporting an issue](k8s_intro.md#id5)

- If you find a bug or have a suggestion regarding modules or plugins, please file issues at [Ansible Kubernetes collection](https://github.com/ansible-collections/kubernetes.core/issues).
- If you find a bug regarding Kubernetes Python client, please file issues at [Kubernetes Client issues](https://github.com/kubernetes-client/python/issues).
- If you find a bug regarding Kubectl binary, please file issues at [Kubectl issue tracker](https://github.com/kubernetes/kubectl/issues)
- If you find a bug regarding Helm binary, please file issues at [Helm issue tracker](https://github.com/helm/helm/issues).
