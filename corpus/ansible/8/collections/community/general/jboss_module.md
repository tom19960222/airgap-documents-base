---
collection: ansible
version: "8"
title: "community.general.jboss module – Deploy applications to JBoss"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/jboss_module.html
fetched_at: 2026-07-28T01:46:58+00:00
---
# community.general.jboss module – Deploy applications to JBoss

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.jboss`.

- [Synopsis](jboss_module.md#synopsis)
- [Parameters](jboss_module.md#parameters)
- [Attributes](jboss_module.md#attributes)
- [Notes](jboss_module.md#notes)
- [See Also](jboss_module.md#see-also)
- [Examples](jboss_module.md#examples)

## [Synopsis](jboss_module.md#id1)

- Deploy applications to JBoss standalone using the filesystem.

Aliases: web_infrastructure.jboss

## [Parameters](jboss_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **deploy_path**  path | The location in the filesystem where the deployment scanner listens.  **Default:** `"/var/lib/jbossas/standalone/deployments"` |
| **deployment**  string / required | The name of the deployment. |
| **src**  path | The remote path of the application ear or war to deploy.  Required when `state=present`.  Ignored when `state=absent`. |
| **state**  string | Whether the application should be deployed or undeployed.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Attributes](jboss_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](jboss_module.md#id4)

> **Note:**
>
> - The JBoss standalone deployment-scanner has to be enabled in standalone.xml
> - The module can wait until `deployment` file is deployed/undeployed by deployment-scanner. Duration of waiting time depends on scan-interval parameter from standalone.xml.
> - Ensure no identically named application is deployed through the JBoss CLI

## [See Also](jboss_module.md#id5)

> **See also:**
>
> [WildFly reference](https://docs.wildfly.org)
> :   Complete reference of the WildFly documentation.

## [Examples](jboss_module.md#id6)

```yaml+jinja
- name: Deploy a hello world application to the default deploy_path
  community.general.jboss:
    src: /tmp/hello-1.0-SNAPSHOT.war
    deployment: hello.war
    state: present

- name: Update the hello world application to the non-default deploy_path
  community.general.jboss:
    src: /tmp/hello-1.1-SNAPSHOT.war
    deploy_path: /opt/wildfly/deployment
    deployment: hello.war
    state: present

- name: Undeploy the hello world application from the default deploy_path
  community.general.jboss:
    deployment: hello.war
    state: absent
```

### Authors

- Jeroen Hoekx (@jhoekx)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
