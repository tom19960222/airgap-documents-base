---
collection: ansible
version: "8"
title: "Creating K8S object"
source_url: https://docs.ansible.com/projects/ansible/8/collections/kubernetes/core/docsite/kubernetes_scenarios/scenario_k8s_object.html
fetched_at: 2026-07-28T03:01:07+00:00
---
# Creating K8S object

- [Introduction](scenario_k8s_object.md#introduction)
- [Scenario Requirements](scenario_k8s_object.md#scenario-requirements)
- [Assumptions](scenario_k8s_object.md#assumptions)
- [Caveats](scenario_k8s_object.md#caveats)
- [Example Description](scenario_k8s_object.md#example-description)

  - [What to expect](scenario_k8s_object.md#what-to-expect)
  - [Troubleshooting](scenario_k8s_object.md#troubleshooting)

## [Introduction](scenario_k8s_object.md#id1)

This guide will show you how to utilize Ansible to create Kubernetes objects such as Pods, Deployments, and Secrets.

## [Scenario Requirements](scenario_k8s_object.md#id2)

- Software

  > - Ansible 2.9.17 or later must be installed
  > - The Python module `kubernetes` must be installed on the Ansible controller (or Target host if not executing against localhost)
  > - Kubernetes Cluster
  > - Kubectl binary installed on the Ansible controller
- Access / Credentials

  > - Kubeconfig configured with the given Kubernetes cluster

## [Assumptions](scenario_k8s_object.md#id3)

- User has required level of authorization to create, delete and update resources on the given Kubernetes cluster.

## [Caveats](scenario_k8s_object.md#id4)

- community.kubernetes 2.0.0 has been renamed to [kubernetes.core](https://github.com/ansible-collections/kubernetes.core)

## [Example Description](scenario_k8s_object.md#id5)

In this use case / example, we will create a Pod in the given Kubernetes Cluster. The following Ansible playbook showcases the basic parameters that are needed for this.

```yaml
---
- hosts: localhost
  collections:
    - kubernetes.core
  tasks:
    - name: Create a pod
      kubernetes.core.k8s:
        state: present
        definition:
          apiVersion: v1
          kind: Pod
          metadata:
            name: "utilitypod-1"
            namespace: default
            labels:
              app: galaxy
          spec:
            containers:
              - name: utilitypod
                image: busybox
```

Since Ansible utilizes the Kubernetes API to perform actions, in this use case we will be connecting directly to the Kubernetes cluster.

To begin, there are a few bits of information we will need. Here you are using Kubeconfig which is pre-configured in your machine. The Kubeconfig is generally located at `~/.kube/config`. It is highly recommended to store sensitive information such as password, user certificates in a more secure fashion using [ansible-vault](../../../../../cli/ansible-vault.md#ansible-vault) or using [Ansible Tower credentials](https://docs.ansible.com/ansible-tower/latest/html/userguide/credentials.html).

Now you need to supply the information about the Pod which will be created. Using `definition` parameter of the `kubernetes.core.k8s` module, you specify [PodTemplate](https://kubernetes.io/docs/concepts/workloads/pods/#pod-templates). This PodTemplate is identical to what you provide to the `kubectl` command.

### [What to expect](scenario_k8s_object.md#id6)

- You will see a bit of JSON output after this playbook completes. This output shows various parameters that are returned from the module and from cluster about the newly created Pod.

```json
{
    "changed": true,
    "method": "create",
    "result": {
        "apiVersion": "v1",
        "kind": "Pod",
        "metadata": {
            "creationTimestamp": "2020-10-03T15:36:25Z",
            "labels": {
                "app": "galaxy"
            },
            "name": "utilitypod-1",
            "namespace": "default",
            "resourceVersion": "4511073",
            "selfLink": "/api/v1/namespaces/default/pods/utilitypod-1",
            "uid": "c7dec819-09df-4efd-9d78-67cf010b4f4e"
        },
        "spec": {
            "containers": [{
                "image": "busybox",
                "imagePullPolicy": "Always",
                "name": "utilitypod",
                "resources": {},
                "terminationMessagePath": "/dev/termination-log",
                "terminationMessagePolicy": "File",
                "volumeMounts": [{
                    "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                    "name": "default-token-6j842",
                    "readOnly": true
                }]
            }],
            "dnsPolicy": "ClusterFirst",
            "enableServiceLinks": true,
            "priority": 0,
            "restartPolicy": "Always",
            "schedulerName": "default-scheduler",
            "securityContext": {},
            "serviceAccount": "default",
            "serviceAccountName": "default",
            "terminationGracePeriodSeconds": 30,
            "tolerations": [{
                    "effect": "NoExecute",
                    "key": "node.kubernetes.io/not-ready",
                    "operator": "Exists",
                    "tolerationSeconds": 300
                },
                {
                    "effect": "NoExecute",
                    "key": "node.kubernetes.io/unreachable",
                    "operator": "Exists",
                    "tolerationSeconds": 300
                }
            ],
            "volumes": [{
                "name": "default-token-6j842",
                "secret": {
                    "defaultMode": 420,
                    "secretName": "default-token-6j842"
                }
            }]
        },
        "status": {
            "phase": "Pending",
            "qosClass": "BestEffort"
        }
    }
}
```

- In the above example, ‘changed’ is `True` which notifies that the Pod creation started on the given cluster. This can take some time depending on your environment.

### [Troubleshooting](scenario_k8s_object.md#id7)

Things to inspect

- Check if the values provided for username and password are correct
- Check if the Kubeconfig is populated with correct values

> **See also:**
>
> [Kubernetes Python client](https://github.com/kubernetes-client/python)
> :   The GitHub Page of Kubernetes Python client
>
> [Kubernetes Python client - Issue Tracker](https://github.com/kubernetes-client/python/issues)
> :   The issue tracker for Kubernetes Python client
>
> [Kubectl installation](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
> :   Installation guide for installing Kubectl
>
> [Working with playbooks](../../../../../playbook_guide/playbooks.md#working-with-playbooks)
> :   An introduction to playbooks
>
> [Using encrypted variables and files](../../../../../vault_guide/vault_using_encrypted_content.md#playbooks-vault)
> :   Using Vault in playbooks
