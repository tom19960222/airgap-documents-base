---
collection: ansible
version: "6"
title: "Using Kubernetes dynamic inventory plugin"
source_url: https://docs.ansible.com/projects/ansible/6/collections/kubernetes/core/docsite/kubernetes_scenarios/k8s_inventory.html
fetched_at: 2026-07-28T00:25:22+00:00
---
# Using Kubernetes dynamic inventory plugin

- [Kubernetes dynamic inventory plugin](k8s_inventory.md#kubernetes-dynamic-inventory-plugin)

  - [Requirements](k8s_inventory.md#requirements)
- [Using vaulted configuration files](k8s_inventory.md#using-vaulted-configuration-files)

## [Kubernetes dynamic inventory plugin](k8s_inventory.md#id1)

The best way to interact with your Pods is to use the Kubernetes dynamic inventory plugin, which queries Kubernetes APIs using `kubectl` command line available on controller node and tells Ansible what Pods can be managed.

### [Requirements](k8s_inventory.md#id2)

To use the Kubernetes dynamic inventory plugins, you must install [Kubernetes Python client](https://github.com/kubernetes-client/python), [kubectl](https://github.com/kubernetes/kubectl) on your control node (the host running Ansible).

```bash
$ pip install kubernetes
```

Please refer to Kubernetes official documentation for [installing kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) on the given operating systems.

To use this Kubernetes dynamic inventory plugin, you need to enable it first by specifying the following in the `ansible.cfg` file:

```ini
[inventory]
enable_plugins = kubernetes.core.k8s
```

Then, create a file that ends in `.k8s.yml` or `.k8s.yaml` in your working directory.

The `kubernetes.core.k8s` inventory plugin takes in the same authentication information as any other Kubernetes modules.

Here’s an example of a valid inventory file:

```yaml
plugin: kubernetes.core.k8s
```

Executing `ansible-inventory --list -i <filename>.k8s.yml` will create a list of Pods that are ready to be configured using Ansible.

You can also provide the namespace to gather information about specific pods from the given namespace. For example, to gather information about Pods under the `test` namespace you will specify the `namespaces` parameter:

```yaml
plugin: kubernetes.core.k8s
connections:
- namespaces:
    - test
```

## [Using vaulted configuration files](k8s_inventory.md#id3)

Since the inventory configuration file contains Kubernetes related sensitive information in plain text, a security risk, you may want to
encrypt your entire inventory configuration file.

You can encrypt a valid inventory configuration file as follows:

```bash
$ ansible-vault encrypt <filename>.k8s.yml
  New Vault password:
  Confirm New Vault password:
  Encryption successful

$ echo "MySuperSecretPassw0rd!" > /path/to/vault_password_file
```

And you can use this vaulted inventory configuration file using:

```bash
$ ansible-inventory -i <filename>.k8s.yml --list --vault-password-file=/path/to/vault_password_file
```

> **See also:**
>
> [Kubernetes Python client - Issue Tracker](https://github.com/kubernetes-client/python/issues)
> :   The issue tracker for Kubernetes Python client
>
> [Kubectl installation](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
> :   Installation guide for installing Kubectl
>
> [Working with playbooks](../../../../../user_guide/playbooks.md#working-with-playbooks)
> :   An introduction to playbooks
>
> [Using encrypted variables and files](../../../../../user_guide/vault.md#playbooks-vault)
> :   Using Vault in playbooks
