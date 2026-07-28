---
collection: ansible
version: "6"
title: "Working with playbooks"
source_url: https://docs.ansible.com/projects/ansible/6/user_guide/playbooks.html
fetched_at: 2026-07-27T16:40:16+00:00
---
# Working with playbooks

Playbooks record and execute Ansible’s configuration, deployment, and orchestration functions. They can describe a policy you want your remote systems to enforce, or a set of steps in a general IT process.

If Ansible modules are the tools in your workshop, playbooks are your instruction manuals, and your inventory of hosts are your raw material.

At a basic level, playbooks can be used to manage configurations of and deployments to remote machines. At a more advanced level, they can sequence multi-tier rollouts involving rolling updates, and can delegate actions to other hosts, interacting with monitoring servers and load balancers along the way.

Playbooks are designed to be human-readable and are developed in a basic text language. There are multiple ways to organize playbooks and the files they include, and we’ll offer up some suggestions on that and making the most out of Ansible.

You should look at [Example Playbooks](https://github.com/ansible/ansible-examples) while reading along with the playbook documentation. These illustrate best practices as well as how to put many of the various concepts together.

- [Templating (Jinja2)](playbooks_templating.md)
  - [Using filters to manipulate data](playbooks_filters.md)
  - [Tests](playbooks_tests.md)
  - [Lookups](playbooks_lookups.md)
  - [Python3 in templates](playbooks_python_version.md)
  - [Get the current time](playbooks_templating.md#get-the-current-time)
- [Advanced playbooks features](playbooks_special_topics.md)
- [Playbook Example: Continuous Delivery and Rolling Upgrades](guide_rolling_upgrade.md)
  - [What is continuous delivery?](guide_rolling_upgrade.md#what-is-continuous-delivery)
  - [Site deployment](guide_rolling_upgrade.md#site-deployment)
  - [Reusable content: roles](guide_rolling_upgrade.md#reusable-content-roles)
  - [Configuration: group variables](guide_rolling_upgrade.md#configuration-group-variables)
  - [The rolling upgrade](guide_rolling_upgrade.md#the-rolling-upgrade)
  - [Managing other load balancers](guide_rolling_upgrade.md#managing-other-load-balancers)
  - [Continuous delivery end-to-end](guide_rolling_upgrade.md#continuous-delivery-end-to-end)
