---
collection: ansible
version: "8"
title: "Index of all Lookup Plugins"
source_url: https://docs.ansible.com/projects/ansible/8/collections/index_lookup.html
fetched_at: 2026-07-28T01:03:10+00:00
---
# Index of all Lookup Plugins

## amazon.aws

- [amazon.aws.aws_account_attribute](amazon/aws/aws_account_attribute_lookup.md#ansible-collections-amazon-aws-aws-account-attribute-lookup) – Look up AWS account attributes
- [amazon.aws.aws_collection_constants](amazon/aws/aws_collection_constants_lookup.md#ansible-collections-amazon-aws-aws-collection-constants-lookup) – expose various collection related constants
- [amazon.aws.aws_service_ip_ranges](amazon/aws/aws_service_ip_ranges_lookup.md#ansible-collections-amazon-aws-aws-service-ip-ranges-lookup) – Look up the IP ranges for services provided in AWS such as EC2 and S3.
- [amazon.aws.secretsmanager_secret](amazon/aws/secretsmanager_secret_lookup.md#ansible-collections-amazon-aws-secretsmanager-secret-lookup) – Look up secrets stored in AWS Secrets Manager
- [amazon.aws.ssm_parameter](amazon/aws/ssm_parameter_lookup.md#ansible-collections-amazon-aws-ssm-parameter-lookup) – gets the value for a SSM parameter or all parameters under a path

## ansible.builtin

- [ansible.builtin.config](ansible/builtin/config_lookup.md#ansible-collections-ansible-builtin-config-lookup) – Lookup current Ansible configuration values
- [ansible.builtin.csvfile](ansible/builtin/csvfile_lookup.md#ansible-collections-ansible-builtin-csvfile-lookup) – read data from a TSV or CSV file
- [ansible.builtin.dict](ansible/builtin/dict_lookup.md#ansible-collections-ansible-builtin-dict-lookup) – returns key/value pair items from dictionaries
- [ansible.builtin.env](ansible/builtin/env_lookup.md#ansible-collections-ansible-builtin-env-lookup) – Read the value of environment variables
- [ansible.builtin.file](ansible/builtin/file_lookup.md#ansible-collections-ansible-builtin-file-lookup) – read file contents
- [ansible.builtin.fileglob](ansible/builtin/fileglob_lookup.md#ansible-collections-ansible-builtin-fileglob-lookup) – list files matching a pattern
- [ansible.builtin.first_found](ansible/builtin/first_found_lookup.md#ansible-collections-ansible-builtin-first-found-lookup) – return first file found from list
- [ansible.builtin.indexed_items](ansible/builtin/indexed_items_lookup.md#ansible-collections-ansible-builtin-indexed-items-lookup) – rewrites lists to return ‘indexed items’
- [ansible.builtin.ini](ansible/builtin/ini_lookup.md#ansible-collections-ansible-builtin-ini-lookup) – read data from an ini file
- [ansible.builtin.inventory_hostnames](ansible/builtin/inventory_hostnames_lookup.md#ansible-collections-ansible-builtin-inventory-hostnames-lookup) – list of inventory hosts matching a host pattern
- [ansible.builtin.items](ansible/builtin/items_lookup.md#ansible-collections-ansible-builtin-items-lookup) – list of items
- [ansible.builtin.lines](ansible/builtin/lines_lookup.md#ansible-collections-ansible-builtin-lines-lookup) – read lines from command
- [ansible.builtin.list](ansible/builtin/list_lookup.md#ansible-collections-ansible-builtin-list-lookup) – simply returns what it is given.
- [ansible.builtin.nested](ansible/builtin/nested_lookup.md#ansible-collections-ansible-builtin-nested-lookup) – composes a list with nested elements of other lists
- [ansible.builtin.password](ansible/builtin/password_lookup.md#ansible-collections-ansible-builtin-password-lookup) – retrieve or generate a random password, stored in a file
- [ansible.builtin.pipe](ansible/builtin/pipe_lookup.md#ansible-collections-ansible-builtin-pipe-lookup) – read output from a command
- [ansible.builtin.random_choice](ansible/builtin/random_choice_lookup.md#ansible-collections-ansible-builtin-random-choice-lookup) – return random element from list
- [ansible.builtin.sequence](ansible/builtin/sequence_lookup.md#ansible-collections-ansible-builtin-sequence-lookup) – generate a list based on a number sequence
- [ansible.builtin.subelements](ansible/builtin/subelements_lookup.md#ansible-collections-ansible-builtin-subelements-lookup) – traverse nested key from a list of dictionaries
- [ansible.builtin.template](ansible/builtin/template_lookup.md#ansible-collections-ansible-builtin-template-lookup) – retrieve contents of file after templating with Jinja2
- [ansible.builtin.together](ansible/builtin/together_lookup.md#ansible-collections-ansible-builtin-together-lookup) – merges lists into synchronized list
- [ansible.builtin.unvault](ansible/builtin/unvault_lookup.md#ansible-collections-ansible-builtin-unvault-lookup) – read vaulted file(s) contents
- [ansible.builtin.url](ansible/builtin/url_lookup.md#ansible-collections-ansible-builtin-url-lookup) – return contents from URL
- [ansible.builtin.varnames](ansible/builtin/varnames_lookup.md#ansible-collections-ansible-builtin-varnames-lookup) – Lookup matching variable names
- [ansible.builtin.vars](ansible/builtin/vars_lookup.md#ansible-collections-ansible-builtin-vars-lookup) – Lookup templated value of variables

## ansible.utils

- [ansible.utils.get_path](ansible/utils/get_path_lookup.md#ansible-collections-ansible-utils-get-path-lookup) – Retrieve the value in a variable using a path
- [ansible.utils.index_of](ansible/utils/index_of_lookup.md#ansible-collections-ansible-utils-index-of-lookup) – Find the indices of items in a list matching some criteria
- [ansible.utils.to_paths](ansible/utils/to_paths_lookup.md#ansible-collections-ansible-utils-to-paths-lookup) – Flatten a complex object into a dictionary of paths and values
- [ansible.utils.validate](ansible/utils/validate_lookup.md#ansible-collections-ansible-utils-validate-lookup) – Validate data with provided criteria

## awx.awx

- [awx.awx.controller_api](awx/awx/controller_api_lookup.md#ansible-collections-awx-awx-controller-api-lookup) – Search the API for objects
- [awx.awx.schedule_rrule](awx/awx/schedule_rrule_lookup.md#ansible-collections-awx-awx-schedule-rrule-lookup) – Generate an rrule string which can be used for Schedules
- [awx.awx.schedule_rruleset](awx/awx/schedule_rruleset_lookup.md#ansible-collections-awx-awx-schedule-rruleset-lookup) – Generate an rruleset string

## azure.azcollection

- [azure.azcollection.azure_keyvault_secret](azure/azcollection/azure_keyvault_secret_lookup.md#ansible-collections-azure-azcollection-azure-keyvault-secret-lookup) – Read secret from Azure Key Vault.

## cisco.aci

- [cisco.aci.interface_range](cisco/aci/interface_range_lookup.md#ansible-collections-cisco-aci-interface-range-lookup) – query interfaces from a range or comma separated list of ranges

## cloud.common

- [cloud.common.turbo_demo](cloud/common/turbo_demo_lookup.md#ansible-collections-cloud-common-turbo-demo-lookup) – A demo for lookup plugins on cloud.common

## community.crypto

- [community.crypto.gpg_fingerprint](community/crypto/gpg_fingerprint_lookup.md#ansible-collections-community-crypto-gpg-fingerprint-lookup) – Retrieve a GPG fingerprint from a GPG public or private key file

## community.dns

- [community.dns.lookup](community/dns/lookup_lookup.md#ansible-collections-community-dns-lookup-lookup) – Look up DNS records
- [community.dns.lookup_as_dict](community/dns/lookup_as_dict_lookup.md#ansible-collections-community-dns-lookup-as-dict-lookup) – Look up DNS records as dictionaries

## community.general

- [community.general.bitwarden](community/general/bitwarden_lookup.md#ansible-collections-community-general-bitwarden-lookup) – Retrieve secrets from Bitwarden
- [community.general.bitwarden_secrets_manager](community/general/bitwarden_secrets_manager_lookup.md#ansible-collections-community-general-bitwarden-secrets-manager-lookup) – Retrieve secrets from Bitwarden Secrets Manager
- [community.general.cartesian](community/general/cartesian_lookup.md#ansible-collections-community-general-cartesian-lookup) – returns the cartesian product of lists
- [community.general.chef_databag](community/general/chef_databag_lookup.md#ansible-collections-community-general-chef-databag-lookup) – fetches data from a Chef Databag
- [community.general.collection_version](community/general/collection_version_lookup.md#ansible-collections-community-general-collection-version-lookup) – Retrieves the version of an installed collection
- [community.general.consul_kv](community/general/consul_kv_lookup.md#ansible-collections-community-general-consul-kv-lookup) – Fetch metadata from a Consul key value store.
- [community.general.credstash](community/general/credstash_lookup.md#ansible-collections-community-general-credstash-lookup) – retrieve secrets from Credstash on AWS
- [community.general.cyberarkpassword](community/general/cyberarkpassword_lookup.md#ansible-collections-community-general-cyberarkpassword-lookup) – get secrets from CyberArk AIM
- [community.general.dependent](community/general/dependent_lookup.md#ansible-collections-community-general-dependent-lookup) – Composes a list with nested elements of other lists or dicts which can depend on previous loop variables
- [community.general.dig](community/general/dig_lookup.md#ansible-collections-community-general-dig-lookup) – query DNS using the dnspython library
- [community.general.dnstxt](community/general/dnstxt_lookup.md#ansible-collections-community-general-dnstxt-lookup) – query a domain(s)’s DNS txt fields
- [community.general.dsv](community/general/dsv_lookup.md#ansible-collections-community-general-dsv-lookup) – Get secrets from Thycotic DevOps Secrets Vault
- [community.general.etcd](community/general/etcd_lookup.md#ansible-collections-community-general-etcd-lookup) – get info from an etcd server
- [community.general.etcd3](community/general/etcd3_lookup.md#ansible-collections-community-general-etcd3-lookup) – Get key values from etcd3 server
- [community.general.filetree](community/general/filetree_lookup.md#ansible-collections-community-general-filetree-lookup) – recursively match all files in a directory tree
- [community.general.flattened](community/general/flattened_lookup.md#ansible-collections-community-general-flattened-lookup) – return single list completely flattened
- [community.general.hiera](community/general/hiera_lookup.md#ansible-collections-community-general-hiera-lookup) – get info from hiera data
- [community.general.keyring](community/general/keyring_lookup.md#ansible-collections-community-general-keyring-lookup) – grab secrets from the OS keyring
- [community.general.lastpass](community/general/lastpass_lookup.md#ansible-collections-community-general-lastpass-lookup) – fetch data from LastPass
- [community.general.lmdb_kv](community/general/lmdb_kv_lookup.md#ansible-collections-community-general-lmdb-kv-lookup) – fetch data from LMDB
- [community.general.manifold](community/general/manifold_lookup.md#ansible-collections-community-general-manifold-lookup) – get credentials from Manifold.co
- [community.general.merge_variables](community/general/merge_variables_lookup.md#ansible-collections-community-general-merge-variables-lookup) – merge variables with a certain suffix
- [community.general.onepassword](community/general/onepassword_lookup.md#ansible-collections-community-general-onepassword-lookup) – fetch field values from 1Password
- [community.general.onepassword_raw](community/general/onepassword_raw_lookup.md#ansible-collections-community-general-onepassword-raw-lookup) – fetch an entire item from 1Password
- [community.general.passwordstore](community/general/passwordstore_lookup.md#ansible-collections-community-general-passwordstore-lookup) – manage passwords with passwordstore.org’s pass utility
- [community.general.random_pet](community/general/random_pet_lookup.md#ansible-collections-community-general-random-pet-lookup) – Generates random pet names
- [community.general.random_string](community/general/random_string_lookup.md#ansible-collections-community-general-random-string-lookup) – Generates random string
- [community.general.random_words](community/general/random_words_lookup.md#ansible-collections-community-general-random-words-lookup) – Return a number of random words
- [community.general.redis](community/general/redis_lookup.md#ansible-collections-community-general-redis-lookup) – fetch data from Redis
- [community.general.revbitspss](community/general/revbitspss_lookup.md#ansible-collections-community-general-revbitspss-lookup) – Get secrets from RevBits PAM server
- [community.general.shelvefile](community/general/shelvefile_lookup.md#ansible-collections-community-general-shelvefile-lookup) – read keys from Python shelve file
- [community.general.tss](community/general/tss_lookup.md#ansible-collections-community-general-tss-lookup) – Get secrets from Thycotic Secret Server

## community.google

- [community.google.gcp_storage_file](community/google/gcp_storage_file_lookup.md#ansible-collections-community-google-gcp-storage-file-lookup) – Return GC Storage content

## community.grafana

- [community.grafana.grafana_dashboard](community/grafana/grafana_dashboard_lookup.md#ansible-collections-community-grafana-grafana-dashboard-lookup) – list or search grafana dashboards

## community.hashi_vault

- [community.hashi_vault.hashi_vault](community/hashi_vault/hashi_vault_lookup.md#ansible-collections-community-hashi-vault-hashi-vault-lookup) – Retrieve secrets from HashiCorp’s Vault
- [community.hashi_vault.vault_ansible_settings](community/hashi_vault/vault_ansible_settings_lookup.md#ansible-collections-community-hashi-vault-vault-ansible-settings-lookup) – Returns plugin settings (options)
- [community.hashi_vault.vault_kv1_get](community/hashi_vault/vault_kv1_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv1-get-lookup) – Get a secret from HashiCorp Vault’s KV version 1 secret store
- [community.hashi_vault.vault_kv2_get](community/hashi_vault/vault_kv2_get_lookup.md#ansible-collections-community-hashi-vault-vault-kv2-get-lookup) – Get a secret from HashiCorp Vault’s KV version 2 secret store
- [community.hashi_vault.vault_list](community/hashi_vault/vault_list_lookup.md#ansible-collections-community-hashi-vault-vault-list-lookup) – Perform a list operation against HashiCorp Vault
- [community.hashi_vault.vault_login](community/hashi_vault/vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup) – Perform a login operation against HashiCorp Vault
- [community.hashi_vault.vault_read](community/hashi_vault/vault_read_lookup.md#ansible-collections-community-hashi-vault-vault-read-lookup) – Perform a read operation against HashiCorp Vault
- [community.hashi_vault.vault_token_create](community/hashi_vault/vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup) – Create a HashiCorp Vault token
- [community.hashi_vault.vault_write](community/hashi_vault/vault_write_lookup.md#ansible-collections-community-hashi-vault-vault-write-lookup) – Perform a write operation against HashiCorp Vault

## community.mongodb

- [community.mongodb.mongodb](community/mongodb/mongodb_lookup.md#ansible-collections-community-mongodb-mongodb-lookup) – lookup info from MongoDB

## community.network

- [community.network.avi](community/network/avi_lookup.md#ansible-collections-community-network-avi-lookup) – Look up ``Avi`` objects.

## community.rabbitmq

- [community.rabbitmq.rabbitmq](community/rabbitmq/rabbitmq_lookup.md#ansible-collections-community-rabbitmq-rabbitmq-lookup) – Retrieve messages from an AMQP/AMQPS RabbitMQ queue.

## community.skydive

- [community.skydive.skydive](community/skydive/skydive_lookup.md#ansible-collections-community-skydive-skydive-lookup) – Query Skydive objects

## community.sops

- [community.sops.sops](community/sops/sops_lookup.md#ansible-collections-community-sops-sops-lookup) – Read sops encrypted file contents

## community.windows

- [community.windows.laps_password](community/windows/laps_password_lookup.md#ansible-collections-community-windows-laps-password-lookup) – Retrieves the LAPS password for a server.

## cyberark.conjur

- [cyberark.conjur.conjur_variable](cyberark/conjur/conjur_variable_lookup.md#ansible-collections-cyberark-conjur-conjur-variable-lookup) – Fetch credentials from CyberArk Conjur.

## f5networks.f5_modules

- [f5networks.f5_modules.bigiq_license](f5networks/f5_modules/bigiq_license_lookup.md#ansible-collections-f5networks-f5-modules-bigiq-license-lookup) – Select a random license key from a pool of biqiq available licenses
- [f5networks.f5_modules.license_hopper](f5networks/f5_modules/license_hopper_lookup.md#ansible-collections-f5networks-f5-modules-license-hopper-lookup) – Return random license from list

## infoblox.nios_modules

- [infoblox.nios_modules.nios_lookup](infoblox/nios_modules/nios_lookup_lookup.md#ansible-collections-infoblox-nios-modules-nios-lookup-lookup) – Query Infoblox NIOS objects
- [infoblox.nios_modules.nios_next_ip](infoblox/nios_modules/nios_next_ip_lookup.md#ansible-collections-infoblox-nios-modules-nios-next-ip-lookup) – Return the next available IP address for a network
- [infoblox.nios_modules.nios_next_network](infoblox/nios_modules/nios_next_network_lookup.md#ansible-collections-infoblox-nios-modules-nios-next-network-lookup) – Return the next available network range for a network-container

## kubernetes.core

- [kubernetes.core.k8s](kubernetes/core/k8s_lookup.md#ansible-collections-kubernetes-core-k8s-lookup) – Query the K8s API
- [kubernetes.core.kustomize](kubernetes/core/kustomize_lookup.md#ansible-collections-kubernetes-core-kustomize-lookup) – Build a set of kubernetes resources using a ‘kustomization.yaml’ file.

## netapp_eseries.santricity

- [netapp_eseries.santricity.santricity_host](netapp_eseries/santricity/santricity_host_lookup.md#ansible-collections-netapp-eseries-santricity-santricity-host-lookup) –
- [netapp_eseries.santricity.santricity_host_detail](netapp_eseries/santricity/santricity_host_detail_lookup.md#ansible-collections-netapp-eseries-santricity-santricity-host-detail-lookup) – Expands the host information from santricity_host lookup
- [netapp_eseries.santricity.santricity_lun_mapping](netapp_eseries/santricity/santricity_lun_mapping_lookup.md#ansible-collections-netapp-eseries-santricity-santricity-lun-mapping-lookup) –
- [netapp_eseries.santricity.santricity_storage_pool](netapp_eseries/santricity/santricity_storage_pool_lookup.md#ansible-collections-netapp-eseries-santricity-santricity-storage-pool-lookup) – Storage pool information
- [netapp_eseries.santricity.santricity_volume](netapp_eseries/santricity/santricity_volume_lookup.md#ansible-collections-netapp-eseries-santricity-santricity-volume-lookup) –

## netbox.netbox

- [netbox.netbox.nb_lookup](netbox/netbox/nb_lookup_lookup.md#ansible-collections-netbox-netbox-nb-lookup-lookup) – Queries and returns elements from NetBox

## vmware.vmware_rest

- [vmware.vmware_rest.cluster_moid](vmware/vmware_rest/cluster_moid_lookup.md#ansible-collections-vmware-vmware-rest-cluster-moid-lookup) – Look up MoID for vSphere cluster objects using vCenter REST API
- [vmware.vmware_rest.datacenter_moid](vmware/vmware_rest/datacenter_moid_lookup.md#ansible-collections-vmware-vmware-rest-datacenter-moid-lookup) – Look up MoID for vSphere datacenter objects using vCenter REST API
- [vmware.vmware_rest.datastore_moid](vmware/vmware_rest/datastore_moid_lookup.md#ansible-collections-vmware-vmware-rest-datastore-moid-lookup) – Look up MoID for vSphere datastore objects using vCenter REST API
- [vmware.vmware_rest.folder_moid](vmware/vmware_rest/folder_moid_lookup.md#ansible-collections-vmware-vmware-rest-folder-moid-lookup) – Look up MoID for vSphere folder objects using vCenter REST API
- [vmware.vmware_rest.host_moid](vmware/vmware_rest/host_moid_lookup.md#ansible-collections-vmware-vmware-rest-host-moid-lookup) – Look up MoID for vSphere host objects using vCenter REST API
- [vmware.vmware_rest.network_moid](vmware/vmware_rest/network_moid_lookup.md#ansible-collections-vmware-vmware-rest-network-moid-lookup) – Look up MoID for vSphere network objects using vCenter REST API
- [vmware.vmware_rest.resource_pool_moid](vmware/vmware_rest/resource_pool_moid_lookup.md#ansible-collections-vmware-vmware-rest-resource-pool-moid-lookup) – Look up MoID for vSphere resource pool objects using vCenter REST API
- [vmware.vmware_rest.vm_moid](vmware/vmware_rest/vm_moid_lookup.md#ansible-collections-vmware-vmware-rest-vm-moid-lookup) – Look up MoID for vSphere vm objects using vCenter REST API

## wti.remote

- [wti.remote.cpm_alarm_info](wti/remote/cpm_alarm_info_lookup.md#ansible-collections-wti-remote-cpm-alarm-info-lookup) – Get alarm information from WTI OOB and PDU devices
- [wti.remote.cpm_config_backup](wti/remote/cpm_config_backup_lookup.md#ansible-collections-wti-remote-cpm-config-backup-lookup) – Get parameters from WTI OOB and PDU devices
- [wti.remote.cpm_config_restore](wti/remote/cpm_config_restore_lookup.md#ansible-collections-wti-remote-cpm-config-restore-lookup) – Send operational parameters to WTI OOB and PDU devices
- [wti.remote.cpm_current_info](wti/remote/cpm_current_info_lookup.md#ansible-collections-wti-remote-cpm-current-info-lookup) – Get the Current Information of a WTI device
- [wti.remote.cpm_firmware_info](wti/remote/cpm_firmware_info_lookup.md#ansible-collections-wti-remote-cpm-firmware-info-lookup) – Get firmware information from WTI OOB and PDU devices
- [wti.remote.cpm_firmware_update](wti/remote/cpm_firmware_update_lookup.md#ansible-collections-wti-remote-cpm-firmware-update-lookup) – Set Serial port parameters in WTI OOB and PDU devices
- [wti.remote.cpm_hostname_config](wti/remote/cpm_hostname_config_lookup.md#ansible-collections-wti-remote-cpm-hostname-config-lookup) – Set Hostname (Site ID), Location, Asset Tag parameters in WTI OOB and PDU devices.
- [wti.remote.cpm_hostname_info](wti/remote/cpm_hostname_info_lookup.md#ansible-collections-wti-remote-cpm-hostname-info-lookup) – Get Hostname (Site ID), Location, Asset Tag parameters in WTI OOB and PDU devices
- [wti.remote.cpm_interface_config](wti/remote/cpm_interface_config_lookup.md#ansible-collections-wti-remote-cpm-interface-config-lookup) – Set network interface parameters in WTI OOB and PDU devices
- [wti.remote.cpm_interface_info](wti/remote/cpm_interface_info_lookup.md#ansible-collections-wti-remote-cpm-interface-info-lookup) – Get network interface parameters from WTI OOB and PDU devices
- [wti.remote.cpm_iptables_config](wti/remote/cpm_iptables_config_lookup.md#ansible-collections-wti-remote-cpm-iptables-config-lookup) – Set network IPTables parameters in WTI OOB and PDU devices
- [wti.remote.cpm_iptables_info](wti/remote/cpm_iptables_info_lookup.md#ansible-collections-wti-remote-cpm-iptables-info-lookup) – Get network IPTABLES parameters from WTI OOB and PDU devices
- [wti.remote.cpm_metering](wti/remote/cpm_metering_lookup.md#ansible-collections-wti-remote-cpm-metering-lookup) – Get Power and Current data from WTI OOB/Combo and PDU devices
- [wti.remote.cpm_plugconfig](wti/remote/cpm_plugconfig_lookup.md#ansible-collections-wti-remote-cpm-plugconfig-lookup) – Get and Set Plug Parameters on WTI OOB and PDU power devices
- [wti.remote.cpm_plugcontrol](wti/remote/cpm_plugcontrol_lookup.md#ansible-collections-wti-remote-cpm-plugcontrol-lookup) – Get and Set Plug actions on WTI OOB and PDU power devices
- [wti.remote.cpm_power_info](wti/remote/cpm_power_info_lookup.md#ansible-collections-wti-remote-cpm-power-info-lookup) – Get the Power Information of a WTI device
- [wti.remote.cpm_serial_port_action_info](wti/remote/cpm_serial_port_action_info_lookup.md#ansible-collections-wti-remote-cpm-serial-port-action-info-lookup) – Get Serial port connection status in WTI OOB and PDU devices
- [wti.remote.cpm_serial_port_action_set](wti/remote/cpm_serial_port_action_set_lookup.md#ansible-collections-wti-remote-cpm-serial-port-action-set-lookup) – Set Serial port connection/disconnection commands in WTI OOB and PDU devices
- [wti.remote.cpm_serial_port_config](wti/remote/cpm_serial_port_config_lookup.md#ansible-collections-wti-remote-cpm-serial-port-config-lookup) – Set Serial port parameters in WTI OOB and PDU devices
- [wti.remote.cpm_serial_port_info](wti/remote/cpm_serial_port_info_lookup.md#ansible-collections-wti-remote-cpm-serial-port-info-lookup) – Get Serial port parameters in WTI OOB and PDU devices
- [wti.remote.cpm_snmp_config](wti/remote/cpm_snmp_config_lookup.md#ansible-collections-wti-remote-cpm-snmp-config-lookup) – Set network IPTables parameters in WTI OOB and PDU devices
- [wti.remote.cpm_snmp_info](wti/remote/cpm_snmp_info_lookup.md#ansible-collections-wti-remote-cpm-snmp-info-lookup) – Get network SNMP parameters from WTI OOB and PDU devices
- [wti.remote.cpm_status](wti/remote/cpm_status_lookup.md#ansible-collections-wti-remote-cpm-status-lookup) – Get status and parameters from WTI OOB and PDU devices.
- [wti.remote.cpm_status_info](wti/remote/cpm_status_info_lookup.md#ansible-collections-wti-remote-cpm-status-info-lookup) – Get general status information from WTI OOB and PDU devices
- [wti.remote.cpm_syslog_client_config](wti/remote/cpm_syslog_client_config_lookup.md#ansible-collections-wti-remote-cpm-syslog-client-config-lookup) – Set network SYSLOG Client parameters in WTI OOB and PDU devices
- [wti.remote.cpm_syslog_client_info](wti/remote/cpm_syslog_client_info_lookup.md#ansible-collections-wti-remote-cpm-syslog-client-info-lookup) – Get network SYSLOG Client parameters from WTI OOB and PDU devices
- [wti.remote.cpm_syslog_server_config](wti/remote/cpm_syslog_server_config_lookup.md#ansible-collections-wti-remote-cpm-syslog-server-config-lookup) – Set network SYSLOG Server parameters in WTI OOB and PDU devices
- [wti.remote.cpm_syslog_server_info](wti/remote/cpm_syslog_server_info_lookup.md#ansible-collections-wti-remote-cpm-syslog-server-info-lookup) – Get network SYSLOG Server parameters from WTI OOB and PDU devices
- [wti.remote.cpm_temp_info](wti/remote/cpm_temp_info_lookup.md#ansible-collections-wti-remote-cpm-temp-info-lookup) – Get temperature information from WTI OOB and PDU devices
- [wti.remote.cpm_time_config](wti/remote/cpm_time_config_lookup.md#ansible-collections-wti-remote-cpm-time-config-lookup) – Set Time/Date parameters in WTI OOB and PDU devices.
- [wti.remote.cpm_time_info](wti/remote/cpm_time_info_lookup.md#ansible-collections-wti-remote-cpm-time-info-lookup) – Get Time/Date parameters in WTI OOB and PDU devices
- [wti.remote.cpm_user](wti/remote/cpm_user_lookup.md#ansible-collections-wti-remote-cpm-user-lookup) – Get various status and parameters from WTI OOB and PDU devices
