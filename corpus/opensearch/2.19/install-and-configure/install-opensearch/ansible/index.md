---
collection: "opensearch"
version: "2.19"
title: "Ansible playbook"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_install-and-configure/install-opensearch/ansible.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_install-and-configure/install-opensearch/ansible.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/install-and-configure/install-opensearch/ansible/"
canonical_url: "https://docs.opensearch.org/latest/install-and-configure/install-opensearch/ansible/"
canonical_route: "/install-and-configure/install-opensearch/ansible/"
redirect_from: ["/opensearch/install/ansible/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 60
parent: "Installing OpenSearch"
---
# Ansible playbook

You can use an Ansible playbook to install and configure a production-ready OpenSearch cluster along with OpenSearch Dashboards.

The Ansible playbook only supports deployment of OpenSearch and OpenSearch Dashboards to the most popular Linux distributions (CentOS 7, RHEL7, Amazon Linux 2, Ubuntu 20.04) hosts.
{: .note }

## Prerequisites

Make sure you have [Ansible](https://www.ansible.com/) and [Java 8](https://www.java.com/en/download/manual.jsp) installed.

## Configuration

1. Clone the OpenSearch [ansible-playbook](https://github.com/opensearch-project/ansible-playbook) repository:

   ```bash
   git clone https://github.com/opensearch-project/ansible-playbook
   ```

2. Configure the node properties in the `inventories/opensearch/hosts` file:

   ```bash
   ansible_host=<Public IP address> ansible_user=root ip=<Private IP address / 0.0.0.0>
   ```

   where:

   - `ansible_host` is the IP address of the target node that you want the Ansible playbook to install OpenSearch and OpenSearch DashBoards on.
   - `ip` is the IP address that you want OpenSearch and OpenSearch DashBoards to bind to. You can specify the private IP of the target node, or localhost, or 0.0.0.0.

3. You can modify the default configuration values in the `inventories/opensearch/group_vars/all/all.yml` file. For example, you can increase the Java memory heap size:

   ```bash
   xms_value: 8
   xmx_value: 8
   ```

Make sure you have direct SSH access into the root user of the target node.
{: .note }

## Run OpenSearch and OpenSearch Dashboards using Ansible playbook

1. Run the Ansible playbook with root privileges:

   ```bash
   ansible-playbook -i inventories/opensearch/hosts opensearch.yml --extra-vars "admin_password=Test@123 kibanaserver_password=Test@6789 logstash_password=Test@456"
   ```

   You can set the passwords for reserved users (`admin`, `kibanaserver`, and `logstash`) using the `admin_password`, `kibanaserver_password`, and `logstash_password` variables.

2. After the deployment process is complete, you can access OpenSearch and OpenSearch Dashboards with the username `admin` and the password that you set for the `admin_password` variable.

   If you bind `ip` to a private IP or localhost, make sure you're logged into the server that deployed the playbook to access OpenSearch and OpenSearch Dashboards:

   ```bash
   curl https://localhost:9200 -u 'admin:Test@123' --insecure
   ```

   If you bind `ip` to 0.0.0.0, then replace `localhost` with the public IP or the private IP (if it's in the same network).
