---
collection: ansible
version: "6"
title: "Index of all Inventory Plugins"
source_url: https://docs.ansible.com/projects/ansible/6/collections/index_inventory.html
fetched_at: 2026-07-27T16:42:15+00:00
---
# Index of all Inventory Plugins

## amazon.aws

- [amazon.aws.aws_ec2](amazon/aws/aws_ec2_inventory.md#ansible-collections-amazon-aws-aws-ec2-inventory) – EC2 inventory source
- [amazon.aws.aws_rds](amazon/aws/aws_rds_inventory.md#ansible-collections-amazon-aws-aws-rds-inventory) – rds instance source

## ansible.builtin

- [ansible.builtin.advanced_host_list](ansible/builtin/advanced_host_list_inventory.md#ansible-collections-ansible-builtin-advanced-host-list-inventory) – Parses a ‘host list’ with ranges
- [ansible.builtin.auto](ansible/builtin/auto_inventory.md#ansible-collections-ansible-builtin-auto-inventory) – Loads and executes an inventory plugin specified in a YAML config
- [ansible.builtin.constructed](ansible/builtin/constructed_inventory.md#ansible-collections-ansible-builtin-constructed-inventory) – Uses Jinja2 to construct vars and groups based on existing inventory.
- [ansible.builtin.generator](ansible/builtin/generator_inventory.md#ansible-collections-ansible-builtin-generator-inventory) – Uses Jinja2 to construct hosts and groups from patterns
- [ansible.builtin.host_list](ansible/builtin/host_list_inventory.md#ansible-collections-ansible-builtin-host-list-inventory) – Parses a ‘host list’ string
- [ansible.builtin.ini](ansible/builtin/ini_inventory.md#ansible-collections-ansible-builtin-ini-inventory) – Uses an Ansible INI file as inventory source.
- [ansible.builtin.script](ansible/builtin/script_inventory.md#ansible-collections-ansible-builtin-script-inventory) – Executes an inventory script that returns JSON
- [ansible.builtin.toml](ansible/builtin/toml_inventory.md#ansible-collections-ansible-builtin-toml-inventory) – Uses a specific TOML file as an inventory source.
- [ansible.builtin.yaml](ansible/builtin/yaml_inventory.md#ansible-collections-ansible-builtin-yaml-inventory) – Uses a specific YAML file as an inventory source.

## awx.awx

- [awx.awx.controller](awx/awx/controller_inventory.md#ansible-collections-awx-awx-controller-inventory) – Ansible dynamic inventory plugin for the Automation Platform Controller.

## azure.azcollection

- [azure.azcollection.azure_rm](azure/azcollection/azure_rm_inventory.md#ansible-collections-azure-azcollection-azure-rm-inventory) – Azure Resource Manager inventory plugin

## cloudscale_ch.cloud

- [cloudscale_ch.cloud.inventory](cloudscale_ch/cloud/inventory_inventory.md#ansible-collections-cloudscale-ch-cloud-inventory-inventory) – cloudscale.ch inventory source

## community.digitalocean

- [community.digitalocean.digitalocean](community/digitalocean/digitalocean_inventory.md#ansible-collections-community-digitalocean-digitalocean-inventory) – DigitalOcean Inventory Plugin

## community.dns

- [community.dns.hetzner_dns_records](community/dns/hetzner_dns_records_inventory.md#ansible-collections-community-dns-hetzner-dns-records-inventory) – Create inventory from Hetzner DNS records
- [community.dns.hosttech_dns_records](community/dns/hosttech_dns_records_inventory.md#ansible-collections-community-dns-hosttech-dns-records-inventory) – Create inventory from Hosttech DNS records

## community.docker

- [community.docker.docker_containers](community/docker/docker_containers_inventory.md#ansible-collections-community-docker-docker-containers-inventory) – Ansible dynamic inventory plugin for Docker containers.
- [community.docker.docker_machine](community/docker/docker_machine_inventory.md#ansible-collections-community-docker-docker-machine-inventory) – Docker Machine inventory source
- [community.docker.docker_swarm](community/docker/docker_swarm_inventory.md#ansible-collections-community-docker-docker-swarm-inventory) – Ansible dynamic inventory plugin for Docker swarm nodes.

## community.general

- [community.general.cobbler](community/general/cobbler_inventory.md#ansible-collections-community-general-cobbler-inventory) – Cobbler inventory source
- [community.general.gitlab_runners](community/general/gitlab_runners_inventory.md#ansible-collections-community-general-gitlab-runners-inventory) – Ansible dynamic inventory plugin for GitLab runners.
- [community.general.icinga2](community/general/icinga2_inventory.md#ansible-collections-community-general-icinga2-inventory) – Icinga2 inventory source
- [community.general.linode](community/general/linode_inventory.md#ansible-collections-community-general-linode-inventory) – Ansible dynamic inventory plugin for Linode.
- [community.general.lxd](community/general/lxd_inventory.md#ansible-collections-community-general-lxd-inventory) – Returns Ansible inventory from lxd host
- [community.general.nmap](community/general/nmap_inventory.md#ansible-collections-community-general-nmap-inventory) – Uses nmap to find hosts to target
- [community.general.online](community/general/online_inventory.md#ansible-collections-community-general-online-inventory) – Scaleway (previously Online SAS or Online.net) inventory source
- [community.general.opennebula](community/general/opennebula_inventory.md#ansible-collections-community-general-opennebula-inventory) – OpenNebula inventory source
- [community.general.proxmox](community/general/proxmox_inventory.md#ansible-collections-community-general-proxmox-inventory) – Proxmox inventory source
- [community.general.scaleway](community/general/scaleway_inventory.md#ansible-collections-community-general-scaleway-inventory) – Scaleway inventory source
- [community.general.stackpath_compute](community/general/stackpath_compute_inventory.md#ansible-collections-community-general-stackpath-compute-inventory) – StackPath Edge Computing inventory source
- [community.general.virtualbox](community/general/virtualbox_inventory.md#ansible-collections-community-general-virtualbox-inventory) – virtualbox inventory source
- [community.general.xen_orchestra](community/general/xen_orchestra_inventory.md#ansible-collections-community-general-xen-orchestra-inventory) – Xen Orchestra inventory source

## community.hrobot

- [community.hrobot.robot](community/hrobot/robot_inventory.md#ansible-collections-community-hrobot-robot-inventory) – Hetzner Robot inventory source

## community.libvirt

- [community.libvirt.libvirt](community/libvirt/libvirt_inventory.md#ansible-collections-community-libvirt-libvirt-inventory) – Libvirt inventory source

## community.okd

- [community.okd.openshift](community/okd/openshift_inventory.md#ansible-collections-community-okd-openshift-inventory) – OpenShift inventory source

## community.vmware

- [community.vmware.vmware_host_inventory](community/vmware/vmware_host_inventory_inventory.md#ansible-collections-community-vmware-vmware-host-inventory-inventory) – VMware ESXi hostsystem inventory source
- [community.vmware.vmware_vm_inventory](community/vmware/vmware_vm_inventory_inventory.md#ansible-collections-community-vmware-vmware-vm-inventory-inventory) – VMware Guest inventory source

## community.zabbix

- [community.zabbix.zabbix_inventory](community/zabbix/zabbix_inventory_inventory.md#ansible-collections-community-zabbix-zabbix-inventory-inventory) – Zabbix Inventory Plugin

## google.cloud

- [google.cloud.gcp_compute](google/cloud/gcp_compute_inventory.md#ansible-collections-google-cloud-gcp-compute-inventory) – Google Cloud Compute Engine inventory source

## hetzner.hcloud

- [hetzner.hcloud.hcloud](hetzner/hcloud/hcloud_inventory.md#ansible-collections-hetzner-hcloud-hcloud-inventory) – Ansible dynamic inventory plugin for the Hetzner Cloud.

## infoblox.nios_modules

- [infoblox.nios_modules.nios_inventory](infoblox/nios_modules/nios_inventory_inventory.md#ansible-collections-infoblox-nios-modules-nios-inventory-inventory) – Infoblox inventory plugin

## kubernetes.core

- [kubernetes.core.k8s](kubernetes/core/k8s_inventory.md#ansible-collections-kubernetes-core-k8s-inventory) – Kubernetes (K8s) inventory source

## netbox.netbox

- [netbox.netbox.nb_inventory](netbox/netbox/nb_inventory_inventory.md#ansible-collections-netbox-netbox-nb-inventory-inventory) – NetBox inventory source

## ngine_io.cloudstack

- [ngine_io.cloudstack.instance](ngine_io/cloudstack/instance_inventory.md#ansible-collections-ngine-io-cloudstack-instance-inventory) – Apache CloudStack instance inventory source

## ngine_io.vultr

- [ngine_io.vultr.vultr](ngine_io/vultr/vultr_inventory.md#ansible-collections-ngine-io-vultr-vultr-inventory) – Vultr inventory source

## openstack.cloud

- [openstack.cloud.openstack](openstack/cloud/openstack_inventory.md#ansible-collections-openstack-cloud-openstack-inventory) – OpenStack inventory source

## ovirt.ovirt

- [ovirt.ovirt.ovirt](ovirt/ovirt/ovirt_inventory.md#ansible-collections-ovirt-ovirt-ovirt-inventory) – oVirt inventory source

## servicenow.servicenow

- [servicenow.servicenow.now](servicenow/servicenow/now_inventory.md#ansible-collections-servicenow-servicenow-now-inventory) – ServiceNow Inventory Plugin

## t_systems_mms.icinga_director

- [t_systems_mms.icinga_director.icinga_director_inventory](t_systems_mms/icinga_director/icinga_director_inventory_inventory.md#ansible-collections-t-systems-mms-icinga-director-icinga-director-inventory-inventory) – Returns Ansible inventory from Icinga

## theforeman.foreman

- [theforeman.foreman.foreman](theforeman/foreman/foreman_inventory.md#ansible-collections-theforeman-foreman-foreman-inventory) – Foreman inventory source
