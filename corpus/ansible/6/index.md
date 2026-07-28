---
collection: ansible
version: "6"
title: "Ansible Documentation"
source_url: https://docs.ansible.com/projects/ansible/6/index.html
fetched_at: 2026-07-27T16:40:13+00:00
---
# Ansible Documentation

## About Ansible

Ansible is an IT automation tool. It can configure systems, deploy software, and orchestrate more advanced IT tasks such as continuous deployments or zero downtime rolling updates.

Ansible’s main goals are simplicity and ease-of-use. It also has a strong focus on security and reliability, featuring a minimum of moving parts, usage of OpenSSH for transport (with other transports and pull modes as alternatives), and a language that is designed around auditability by humans–even those not familiar with the program.

We believe simplicity is relevant to all sizes of environments, so we design for busy users of all types: developers, sysadmins, release engineers, IT managers, and everyone in between. Ansible is appropriate for managing all environments, from small setups with a handful of instances to enterprise environments with many thousands of instances.

You can learn more at [AnsibleFest](https://www.ansible.com/ansiblefest), the annual event for all Ansible contributors, users, and customers hosted by Red Hat. AnsibleFest is the place to connect with others, learn new skills, and find a new friend to automate with.

Ansible manages machines in an agent-less manner. There is never a question of how to upgrade remote daemons or the problem of not being able to manage systems because daemons are uninstalled. Also, security exposure is greatly reduced because Ansible uses OpenSSH — the open source connectivity tool for remote login with the SSH (Secure Shell) protocol.

Ansible is decentralized–it relies on your existing OS credentials to control access to remote machines. And if needed, Ansible can easily connect with Kerberos, LDAP, and other centralized authentication management systems.

This documentation covers the version of Ansible noted in the upper left corner of this page. We maintain multiple versions of Ansible and the Ansible documentation, so please be sure you are using the documentation version that covers the version of Ansible you are using. For recent features, we note the version of Ansible where the feature was added.

Ansible releases a new major release approximately twice a year. The core application evolves somewhat conservatively, valuing simplicity in language design and setup. Contributors develop and change modules and plugins hosted in collections since version 2.10 much more quickly.

Ansible getting started

- [Getting started with Ansible](getting_started/index.md)
  - [Building an inventory](getting_started/get_started_inventory.md)
  - [Creating a playbook](getting_started/get_started_playbook.md)

Installation, Upgrade & Configuration

- [Installation Guide](installation_guide/index.md)
  - [Installing Ansible](installation_guide/intro_installation.md)
  - [Installing Ansible on specific operating systems](installation_guide/installation_distros.md)
  - [Configuring Ansible](installation_guide/intro_configuration.md)
- [Ansible Porting Guides](porting_guides/porting_guides.md)
  - [Ansible 6 Porting Guide](porting_guides/porting_guide_6.md)
  - [Ansible 5 Porting Guide](porting_guides/porting_guide_5.md)
  - [Ansible 4 Porting Guide](porting_guides/porting_guide_4.md)
  - [Ansible 3 Porting Guide](porting_guides/porting_guide_3.md)
  - [Ansible 2.10 Porting Guide](porting_guides/porting_guide_2.10.md)
  - [Ansible 2.9 Porting Guide](porting_guides/porting_guide_2.9.md)
  - [Ansible 2.8 Porting Guide](porting_guides/porting_guide_2.8.md)
  - [Ansible 2.7 Porting Guide](porting_guides/porting_guide_2.7.md)
  - [Ansible 2.6 Porting Guide](porting_guides/porting_guide_2.6.md)
  - [Ansible 2.5 Porting Guide](porting_guides/porting_guide_2.5.md)
  - [Ansible 2.4 Porting Guide](porting_guides/porting_guide_2.4.md)
  - [Ansible 2.3 Porting Guide](porting_guides/porting_guide_2.3.md)
  - [Ansible 2.0 Porting Guide](porting_guides/porting_guide_2.0.md)

Using Ansible

- [User Guide](user_guide/index.md)
  - [Writing tasks, plays, and playbooks](user_guide/index.md#writing-tasks-plays-and-playbooks)
  - [Working with inventory](user_guide/index.md#working-with-inventory)
  - [Interacting with data](user_guide/index.md#interacting-with-data)
  - [Executing playbooks](user_guide/index.md#executing-playbooks)
  - [Advanced features and reference](user_guide/index.md#advanced-features-and-reference)
  - [Table of contents](user_guide/index.md#table-of-contents)

Contributing to Ansible

- [Ansible Community Guide](community/index.md)
  - [Getting started](community/getting_started.md)
  - [Contributor path](community/contributor_path.md)
- [Ansible Collections Contributor Guide](community/contributions_collections.md)
  - [The Ansible Collections Development Cycle](community/collection_development_process.md)
  - [Requesting changes to a collection](community/reporting_collections.md)
  - [Creating your first collection pull request](community/create_pr_quick_start.md)
  - [Testing Collection Contributions](community/collection_contributors/test_index.md)
  - [Review checklist for collection PRs](community/collection_contributors/collection_reviewing.md)
  - [Guidelines for collection maintainers](community/maintainers.md)
  - [Contributing to Ansible-maintained Collections](community/contributing_maintained_collections.md)
  - [Ansible Community Steering Committee](community/steering/steering_index.md)
  - [Contributing to the Ansible Documentation](community/documentation_contributions.md)
  - [Other Tools and Programs](community/other_tools_and_programs.md)
  - [Popular editors](community/other_tools_and_programs.md#popular-editors)
  - [Development tools](community/other_tools_and_programs.md#development-tools)
  - [Tools for validating playbooks](community/other_tools_and_programs.md#tools-for-validating-playbooks)
  - [Other tools](community/other_tools_and_programs.md#other-tools)
  - [Working with the Ansible collection repositories](community/contributions_collections.md#working-with-the-ansible-collection-repositories)
- [ansible-core Contributors Guide](community/contributions.md)
  - [Reporting bugs and requesting features](community/reporting_bugs_and_features.md)
  - [Contributing to the Ansible Documentation](community/documentation_contributions.md)
  - [The Ansible Development Cycle](community/development_process.md)
  - [Other Tools and Programs](community/other_tools_and_programs.md)
  - [Popular editors](community/other_tools_and_programs.md#popular-editors)
  - [Development tools](community/other_tools_and_programs.md#development-tools)
  - [Tools for validating playbooks](community/other_tools_and_programs.md#tools-for-validating-playbooks)
  - [Other tools](community/other_tools_and_programs.md#other-tools)
  - [Working with the Ansible repo](community/contributions.md#working-with-the-ansible-repo)
- [Advanced Contributor Guide](community/advanced_index.md)
  - [Committers Guidelines](community/committer_guidelines.md)
  - [Release Manager Guidelines](community/release_managers.md)
  - [GitHub Admins](community/github_admins.md)
- [Ansible documentation style guide](dev_guide/style_guide/index.md)
  - [Linguistic guidelines](dev_guide/style_guide/index.md#linguistic-guidelines)
  - [reStructuredText guidelines](dev_guide/style_guide/index.md#restructuredtext-guidelines)
  - [Accessibility guidelines](dev_guide/style_guide/index.md#accessibility-guidelines)
  - [More resources](dev_guide/style_guide/index.md#more-resources)

Extending Ansible

- [Developer Guide](dev_guide/index.md)
  - [Adding modules and plugins locally](dev_guide/developing_locally.md)
  - [Should you develop a module?](dev_guide/developing_modules.md)
  - [Developing modules](dev_guide/developing_modules_general.md)
  - [Contributing your module to an existing Ansible collection](dev_guide/developing_modules_checklist.md)
  - [Conventions, tips, and pitfalls](dev_guide/developing_modules_best_practices.md)
  - [Ansible and Python 3](dev_guide/developing_python_3.md)
  - [Debugging modules](dev_guide/debugging.md)
  - [Module format and documentation](dev_guide/developing_modules_documenting.md)
  - [Windows module development walkthrough](dev_guide/developing_modules_general_windows.md)
  - [Developing Cisco ACI modules](dev_guide/developing_modules_general_aci.md)
  - [Guidelines for Ansible Amazon AWS module development](dev_guide/platforms/aws_guidelines.md)
  - [OpenStack Ansible Modules](dev_guide/platforms/openstack_guidelines.md)
  - [oVirt Ansible Modules](dev_guide/platforms/ovirt_dev_guide.md)
  - [Guidelines for VMware module development](dev_guide/platforms/vmware_guidelines.md)
  - [Guidelines for VMware REST module development](dev_guide/platforms/vmware_rest_guidelines.md)
  - [Creating a new collection](dev_guide/developing_modules_in_groups.md)
  - [Testing Ansible](dev_guide/testing.md)
  - [The lifecycle of an Ansible module or plugin](dev_guide/module_lifecycle.md)
  - [Developing plugins](dev_guide/developing_plugins.md)
  - [Developing dynamic inventory](dev_guide/developing_inventory.md)
  - [Developing `ansible-core`](dev_guide/developing_core.md)
  - [Ansible module architecture](dev_guide/developing_program_flow_modules.md)
  - [Python API](dev_guide/developing_api.md)
  - [Rebasing a pull request](dev_guide/developing_rebasing.md)
  - [Using and developing module utilities](dev_guide/developing_module_utilities.md)
  - [Developing collections](dev_guide/developing_collections.md)
  - [Migrating Roles to Roles in Collections on Galaxy](dev_guide/migrating_roles.md)
  - [Collection Galaxy metadata structure](dev_guide/collections_galaxy_meta.md)
  - [Ansible architecture](dev_guide/overview_architecture.md)

Common Ansible Scenarios

- [Legacy Public Cloud Guides](scenario_guides/cloud_guides.md)
- [Network Technology Guides](scenario_guides/network_guides.md)
- [Virtualization and Containerization Guides](scenario_guides/virt_guides.md)

Network Automation

- [Network Getting Started](network/getting_started/index.md)
  - [Basic Concepts](network/getting_started/basic_concepts.md)
  - [How Network Automation is Different](network/getting_started/network_differences.md)
  - [Run Your First Command and Playbook](network/getting_started/first_playbook.md)
  - [Build Your Inventory](network/getting_started/first_inventory.md)
  - [Use Ansible network roles](network/getting_started/network_roles.md)
  - [Beyond the basics](network/getting_started/intermediate_concepts.md)
  - [Working with network connection options](network/getting_started/network_connection_options.md)
  - [Resources and next steps](network/getting_started/network_resources.md)
- [Network Advanced Topics](network/user_guide/index.md)
  - [Network Resource Modules](network/user_guide/network_resource_modules.md)
  - [Ansible Network Examples](network/user_guide/network_best_practices_2.5.md)
  - [Parsing semi-structured text with Ansible](network/user_guide/cli_parsing.md)
  - [Validate data against set criteria with Ansible](network/user_guide/validate.md)
  - [Network Debug and Troubleshooting Guide](network/user_guide/network_debug_troubleshooting.md)
  - [Working with command output and prompts in network modules](network/user_guide/network_working_with_command_output.md)
  - [Ansible Network FAQ](network/user_guide/faq.md)
  - [Platform Options](network/user_guide/platform_index.md)
- [Network Developer Guide](network/dev_guide/index.md)
  - [Developing network resource modules](network/dev_guide/developing_resource_modules_network.md)
  - [Developing network plugins](network/dev_guide/developing_plugins_network.md)
  - [Documenting new network platforms](network/dev_guide/documenting_modules_network.md)

Ansible Galaxy

- [Galaxy User Guide](galaxy/user_guide.md)
  - [Finding collections on Galaxy](galaxy/user_guide.md#finding-collections-on-galaxy)
  - [Installing collections](galaxy/user_guide.md#installing-collections)
  - [Finding roles on Galaxy](galaxy/user_guide.md#finding-roles-on-galaxy)
  - [Installing roles from Galaxy](galaxy/user_guide.md#installing-roles-from-galaxy)
- [Galaxy Developer Guide](galaxy/dev_guide.md)
  - [Creating collections for Galaxy](galaxy/dev_guide.md#creating-collections-for-galaxy)
  - [Creating roles for Galaxy](galaxy/dev_guide.md#creating-roles-for-galaxy)

Reference & Appendices

- [Collection Index](collections/index.md)
- [Indexes of all modules and plugins](collections/all_plugins.md)
- [Playbook Keywords](reference_appendices/playbooks_keywords.md)
- [Return Values](reference_appendices/common_return_values.md)
- [Ansible Configuration Settings](reference_appendices/config.md)
- [Controlling how Ansible behaves: precedence rules](reference_appendices/general_precedence.md)
- [YAML Syntax](reference_appendices/YAMLSyntax.md)
- [Python 3 Support](reference_appendices/python_3_support.md)
- [Interpreter Discovery](reference_appendices/interpreter_discovery.md)
- [Releases and maintenance](reference_appendices/release_and_maintenance.md)
- [Testing Strategies](reference_appendices/test_strategies.md)
- [Sanity Tests](dev_guide/testing/sanity/index.md)
- [Frequently Asked Questions](reference_appendices/faq.md)
- [Glossary](reference_appendices/glossary.md)
- [Ansible Reference: Module Utilities](reference_appendices/module_utils.md)
- [Special Variables](reference_appendices/special_variables.md)
- [Red Hat Ansible Automation Platform](reference_appendices/tower.md)
- [Ansible Automation Hub](reference_appendices/automationhub.md)
- [Logging Ansible output](reference_appendices/logging.md)

Roadmaps

- [Ansible Roadmap](roadmap/ansible_roadmap_index.md)
  - [Ansible project 6.0](roadmap/COLLECTIONS_6.md)
  - [Ansible project 5.0](roadmap/COLLECTIONS_5.md)
  - [Ansible project 4.0](roadmap/COLLECTIONS_4.md)
  - [Ansible project 3.0](roadmap/COLLECTIONS_3_0.md)
  - [Ansible project 2.10](roadmap/COLLECTIONS_2_10.md)
  - [Older Roadmaps](roadmap/old_roadmap_index.md)
- [ansible-core Roadmaps](roadmap/ansible_core_roadmap_index.md)
  - [Ansible-core 2.13](roadmap/ROADMAP_2_13.md)
  - [Ansible-core 2.12](roadmap/ROADMAP_2_12.md)
  - [Ansible-core 2.11](roadmap/ROADMAP_2_11.md)
  - [Ansible-base 2.10](roadmap/ROADMAP_2_10.md)
