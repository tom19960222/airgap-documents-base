---
collection: ansible
version: "8"
title: "Contributing to Ansible-maintained Collections"
source_url: https://docs.ansible.com/projects/ansible/8/community/contributing_maintained_collections.html
fetched_at: 2026-07-28T00:58:58+00:00
---
# Contributing to Ansible-maintained Collections

The Ansible team welcomes community contributions to the collections maintained by Red Hat Ansible Engineering. This section describes how you can open issues and create PRs with the required testing before your PR can be merged.

- [Ansible-maintained collections](contributing_maintained_collections.md#ansible-maintained-collections)
- [Deciding where your contribution belongs](contributing_maintained_collections.md#deciding-where-your-contribution-belongs)
- [Requirements to merge your PR](contributing_maintained_collections.md#requirements-to-merge-your-pr)

## [Ansible-maintained collections](contributing_maintained_collections.md#id1)

The following table shows:

- **Ansible-maintained collection** - Click the link to the collection on Galaxy, then click the `repo` button in Galaxy to find the GitHub repository for this collection.
- **Related community collection** - Collection that holds community-created content (modules, roles, and so on) that may also be of interest to a user of the Ansible-maintained collection. You can, for example, add new modules to the community collection as a technical preview before the content is moved to the Ansible-maintained collection.
- **Sponsor** - Working group that manages the collections. You can join the meetings to discuss important proposed changes and enhancements to the collections.
- **Test requirements** - Testing required for any new or changed content for the Ansible-maintained collection.
- **Developer details** - Describes whether the Ansible-maintained collection accepts direct community issues and PRs for existing collection content, as well as more specific developer guidelines based on the collection type.

| Collection details | | | Test requirements: Ansible collections | | | | Developer details | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ansible collection | Related community collection | Sponsor | Sanity | Unit | Integration | CI Platform | Open to PRs\* | Guidelines |
| [amazon.aws](https://galaxy.ansible.com/amazon/aws) | [community.aws](https://galaxy.ansible.com/community/aws) | [AWS](https://github.com/ansible/community/tree/main/group-aws) | ✓\*\* | \*\* | ✓ | Zuul | ✓ | [AWS guide](https://docs.ansible.com/ansible/devel/collections/amazon/aws/docsite/dev_guidelines.html) |
| [ansible.netcommon\*\*\*](https://galaxy.ansible.com/ansible/netcommon) | [community.network](https://galaxy.ansible.com/community/network) | [Network](https://github.com/ansible/community/wiki/Network) | ✓ | ✓ | ✓ | Zuul | ✓ | [Network guide](https://docs.ansible.com/ansible/devel/network/dev_guide/index.html) |
| [ansible.posix](https://galaxy.ansible.com/ansible/posix) | [community.general](https://galaxy.ansible.com/community/general) | Linux | ✓ |  |  | Zuul | ✓ | [Developer guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html) |
| [ansible.windows](https://galaxy.ansible.com/ansible/windows) | [community.windows](https://galaxy.ansible.com/community/windows) | [Windows](https://github.com/ansible/community/wiki/Windows) | ✓ | ✓\*\*\*\* | ✓ | Azure Pipelines and Zuul | ✓ | [Windows guide](https://docs.ansible.com/ansible/devel/dev_guide/developing_modules_general_windows.html#developing-modules-general-windows) |
| [arista.eos](https://galaxy.ansible.com/arista/eos) | [community.network](https://galaxy.ansible.com/community/network) | [Network](https://github.com/ansible/community/wiki/Network) | ✓ | ✓ | ✓ | Zuul | ✓ | [Network guide](https://docs.ansible.com/ansible/devel/network/dev_guide/index.html) |
| [cisco.asa](https://galaxy.ansible.com/cisco/asa) | [community.asa](https://github.com/ansible-collections/community.asa) | [Security](https://github.com/ansible/community/wiki/Security-Automation) | ✓ | ✓ | ✓ | Zuul | ✓ | [Developer guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html) |
| [cisco.ios](https://galaxy.ansible.com/cisco/ios) | [community.network](https://galaxy.ansible.com/community/network) | [Network](https://github.com/ansible/community/wiki/Network) | ✓ | ✓ | ✓ | Zuul | ✓ | [Network guide](https://docs.ansible.com/ansible/devel/network/dev_guide/index.html) |
| [cisco.iosxr](https://galaxy.ansible.com/cisco/iosxr) | [community.network](https://galaxy.ansible.com/community/network) | [Network](https://github.com/ansible/community/wiki/Network) | ✓ | ✓ | ✓ | Zuul | ✓ | [Network guide](https://docs.ansible.com/ansible/devel/network/dev_guide/index.html) |
| [cisco.nxos](https://galaxy.ansible.com/cisco/nxos) | [community.network](https://galaxy.ansible.com/community/network) | [Network](https://github.com/ansible/community/wiki/Network) | ✓ | ✓ | ✓ | Zuul | ✓ | [Network guide](https://docs.ansible.com/ansible/devel/network/dev_guide/index.html) |
| [ibm.qradar](https://galaxy.ansible.com/ibm/qradar) | [community.qradar](https://github.com/ansible-collections/community.qradar) | [Security](https://github.com/ansible/community/wiki/Security-Automation) | ✓ |  | ✓ | Zuul | ✓ | [Developer guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html) |
| [junipernetworks.junos](https://galaxy.ansible.com/junipernetworks/junos) | [community.network](https://galaxy.ansible.com/community/network) | [Network](https://github.com/ansible/community/wiki/Network) | ✓ | ✓ | ✓ | Zuul | ✓ | [Network guide](https://docs.ansible.com/ansible/devel/network/dev_guide/index.html) |
| [kubernetes.core](https://galaxy.ansible.com/kubernetes/core) | [kubernetes.core](https://galaxy.ansible.com/kubernetes/core) | [Kubernetes](https://github.com/ansible/community/wiki/Kubernetes) | ✓ | ✓ | ✓ | GitHub Actions | ✓ |  |
| [redhat.openshift](https://cloud.redhat.com/ansible/automation-hub/redhat/openshift) | [community.okd](https://galaxy.ansible.com/community/okd) | [Kubernetes](https://github.com/ansible/community/wiki/Kubernetes) | ✓ | ✓ | ✓ | GitHub Actions | ✓ |  |
| [openvswitch.openvswitch](https://galaxy.ansible.com/openvswitch/openvswitch) | [community.network](https://galaxy.ansible.com/community/network) | [Network](https://github.com/ansible/community/wiki/Network) | ✓ | ✓ | ✓ | Zuul | ✓ | [Network guide](https://docs.ansible.com/ansible/devel/network/dev_guide/index.html) |
| [splunk.es](https://github.com/ansible-collections/splunk.es) | [community.es](https://github.com/ansible-collections/community.es) | [Security](https://github.com/ansible/community/wiki/Security-Automation) | ✓ |  | ✓ | Zuul | ✓ | [Developer guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html) |
| [vyos.vyos](https://galaxy.ansible.com/vyos/vyos) | [community.network](https://galaxy.ansible.com/community/network) | [Network](https://github.com/ansible/community/wiki/Network) | ✓ | ✓ | ✓ | Zuul | ✓ | [Network guide](https://docs.ansible.com/ansible/devel/network/dev_guide/index.html) |
| [vmware.vmware_rest](https://galaxy.ansible.com/vmware/vmware_rest) | [vmware.vmware_rest](https://galaxy.ansible.com/vmware/vmware_rest) | [VMware](https://github.com/ansible/community/wiki/VMware) | ✓ | ✓ | ✓ | Zuul | ✓ | [VMware REST guide](https://docs.ansible.com/ansible/devel/collections/vmware/vmware_rest/docsite/dev_guide.html) |

> **Note:**
>
> \* A ✓ under **Open to PRs** means the collection welcomes GitHub issues and PRs for any changes to existing collection content (plugins, roles, and so on).
>
> \*\* Integration tests are required and unit tests are welcomed but not required for the AWS collections. An exception to this is made in cases where integration tests are logistically not feasible due to external requirements. An example of this is AWS Direct Connect, as this service can not be functionally tested without the establishment of network peering connections. Unit tests are therefore required for modules that interact with AWS Direct Connect. Exceptions to `amazon.aws` must be approved by Red Hat, and exceptions to `community.aws` must be approved by the AWS community.
>
> \*\*\* `ansible.netcommon` contains all foundational components for enabling many network and security [platform](../network/user_guide/platform_index.md#platform-options) collections. It contains all connection and filter plugins required, and installs as a dependency when you install the platform collection.
>
> \*\*\*\* Unit tests for Windows PowerShell modules are an exception to testing, but unit tests are valid and required for the remainder of the collection, including Ansible-side plugins.

## [Deciding where your contribution belongs](contributing_maintained_collections.md#id2)

We welcome contributions to Ansible-maintained collections. Because these collections are part of a downstream supported Red Hat product, the criteria for contribution, testing, and release may be higher than other community collections. The related community collections (such as `community.general` and `community.network`) have less-stringent requirements and are a great place for new functionality that may become part of the Ansible-maintained collection in a future release.

The following scenarios use the `arista.eos` to help explain when to contribute to the Ansible-maintained collection, and when to propose your change or idea to the related community collection:

1. You want to fix a problem in the `arista.eos` Ansible-maintained collection. Create the PR directly in the [arista.eos collection GitHub repository](https://github.com/ansible-collections/arista.eos). Apply all the [merge requirements](contributing_maintained_collections.md#ansible-collection-merge-requirements).
2. You want to add a new Ansible module for Arista. Your options are one of the following:

   > - Propose a new module in the `arista.eos` collection (requires approval from Arista and Red Hat).
   > - Propose a new collection in the `arista` namespace (requires approval from Arista and Red Hat).
   > - Propose a new module in the `community.network` collection (requires network community approval).
   > - Place your new module in a collection in your own namespace (no approvals required).

Most new content should go into either a related community collection or your own collection first so that is well established in the community before you can propose adding it to the `arista` namespace, where inclusion and maintenance criteria are much higher.

## [Requirements to merge your PR](contributing_maintained_collections.md#id3)

Your PR must meet the following requirements before it can merge into an Ansible-maintained collection:

1. The PR is in the intended scope of the collection. Communicate with the appropriate Ansible sponsor listed in the [Ansible-maintained collection table](contributing_maintained_collections.md#ansible-collection-table) for help.
2. For network and security domains, the PR follows the [resource module development principles](../network/dev_guide/developing_resource_modules_network.md#developing-resource-modules).
3. Passes [sanity tests and tox](../network/dev_guide/developing_resource_modules_network.md#tox-resource-modules).
4. Passes unit, and integration tests, as listed in the [Ansible-maintained collection table](contributing_maintained_collections.md#ansible-collection-table) and described in [Resource module integration tests](../network/dev_guide/developing_resource_modules_network.md#id3).
5. Follows Ansible guidelines. See [Should you develop a module?](../dev_guide/developing_modules.md#developing-modules) and [Developing collections](../dev_guide/developing_collections.md#developing-collections).
6. Addresses all review comments.
7. Includes an appropriate [changelog](development_process.md#community-changelogs).
