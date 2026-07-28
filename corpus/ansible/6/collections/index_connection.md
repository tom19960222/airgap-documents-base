---
collection: ansible
version: "6"
title: "Index of all Connection Plugins"
source_url: https://docs.ansible.com/projects/ansible/6/collections/index_connection.html
fetched_at: 2026-07-27T16:42:14+00:00
---
# Index of all Connection Plugins

## ansible.builtin

- [ansible.builtin.local](ansible/builtin/local_connection.md#ansible-collections-ansible-builtin-local-connection) – execute on controller
- [ansible.builtin.paramiko_ssh](ansible/builtin/paramiko_ssh_connection.md#ansible-collections-ansible-builtin-paramiko-ssh-connection) – Run tasks via python ssh (paramiko)
- [ansible.builtin.psrp](ansible/builtin/psrp_connection.md#ansible-collections-ansible-builtin-psrp-connection) – Run tasks over Microsoft PowerShell Remoting Protocol
- [ansible.builtin.ssh](ansible/builtin/ssh_connection.md#ansible-collections-ansible-builtin-ssh-connection) – connect via SSH client binary
- [ansible.builtin.winrm](ansible/builtin/winrm_connection.md#ansible-collections-ansible-builtin-winrm-connection) – Run tasks over Microsoft’s WinRM

## ansible.netcommon

- [ansible.netcommon.grpc](ansible/netcommon/grpc_connection.md#ansible-collections-ansible-netcommon-grpc-connection) – Provides a persistent connection using the gRPC protocol
- [ansible.netcommon.httpapi](ansible/netcommon/httpapi_connection.md#ansible-collections-ansible-netcommon-httpapi-connection) – Use httpapi to run command on network appliances
- [ansible.netcommon.libssh](ansible/netcommon/libssh_connection.md#ansible-collections-ansible-netcommon-libssh-connection) – Run tasks using libssh for ssh connection
- [ansible.netcommon.napalm](ansible/netcommon/napalm_connection.md#ansible-collections-ansible-netcommon-napalm-connection) – Provides persistent connection using NAPALM
- [ansible.netcommon.netconf](ansible/netcommon/netconf_connection.md#ansible-collections-ansible-netcommon-netconf-connection) – Provides a persistent connection using the netconf protocol
- [ansible.netcommon.network_cli](ansible/netcommon/network_cli_connection.md#ansible-collections-ansible-netcommon-network-cli-connection) – Use network_cli to run command on network appliances
- [ansible.netcommon.persistent](ansible/netcommon/persistent_connection.md#ansible-collections-ansible-netcommon-persistent-connection) – Use a persistent unix socket for connection

## community.aws

- [community.aws.aws_ssm](community/aws/aws_ssm_connection.md#ansible-collections-community-aws-aws-ssm-connection) – execute via AWS Systems Manager

## community.docker

- [community.docker.docker](community/docker/docker_connection.md#ansible-collections-community-docker-docker-connection) – Run tasks in docker containers
- [community.docker.docker_api](community/docker/docker_api_connection.md#ansible-collections-community-docker-docker-api-connection) – Run tasks in docker containers
- [community.docker.nsenter](community/docker/nsenter_connection.md#ansible-collections-community-docker-nsenter-connection) – execute on host running controller container

## community.general

- [community.general.chroot](community/general/chroot_connection.md#ansible-collections-community-general-chroot-connection) – Interact with local chroot
- [community.general.funcd](community/general/funcd_connection.md#ansible-collections-community-general-funcd-connection) – Use funcd to connect to target
- [community.general.iocage](community/general/iocage_connection.md#ansible-collections-community-general-iocage-connection) – Run tasks in iocage jails
- [community.general.jail](community/general/jail_connection.md#ansible-collections-community-general-jail-connection) – Run tasks in jails
- [community.general.lxc](community/general/lxc_connection.md#ansible-collections-community-general-lxc-connection) – Run tasks in lxc containers via lxc python library
- [community.general.lxd](community/general/lxd_connection.md#ansible-collections-community-general-lxd-connection) – Run tasks in lxc containers via lxc CLI
- [community.general.qubes](community/general/qubes_connection.md#ansible-collections-community-general-qubes-connection) – Interact with an existing QubesOS AppVM
- [community.general.saltstack](community/general/saltstack_connection.md#ansible-collections-community-general-saltstack-connection) – Allow ansible to piggyback on salt minions
- [community.general.zone](community/general/zone_connection.md#ansible-collections-community-general-zone-connection) – Run tasks in a zone instance

## community.libvirt

- [community.libvirt.libvirt_lxc](community/libvirt/libvirt_lxc_connection.md#ansible-collections-community-libvirt-libvirt-lxc-connection) – Run tasks in lxc containers via libvirt
- [community.libvirt.libvirt_qemu](community/libvirt/libvirt_qemu_connection.md#ansible-collections-community-libvirt-libvirt-qemu-connection) – Run tasks on libvirt/qemu virtual machines

## community.okd

- [community.okd.oc](community/okd/oc_connection.md#ansible-collections-community-okd-oc-connection) – Execute tasks in pods running on OpenShift.

## community.vmware

- [community.vmware.vmware_tools](community/vmware/vmware_tools_connection.md#ansible-collections-community-vmware-vmware-tools-connection) – Execute tasks inside a VM via VMware Tools

## containers.podman

- [containers.podman.buildah](containers/podman/buildah_connection.md#ansible-collections-containers-podman-buildah-connection) – Interact with an existing buildah container
- [containers.podman.podman](containers/podman/podman_connection.md#ansible-collections-containers-podman-podman-connection) – Interact with an existing podman container

## kubernetes.core

- [kubernetes.core.kubectl](kubernetes/core/kubectl_connection.md#ansible-collections-kubernetes-core-kubectl-connection) – Execute tasks in pods running on Kubernetes.
