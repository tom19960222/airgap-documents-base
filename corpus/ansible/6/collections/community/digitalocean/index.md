---
collection: ansible
version: "6"
title: "Community.Digitalocean"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/digitalocean/index.html
fetched_at: 2026-07-27T16:41:42+00:00
---
# Community.Digitalocean

Collection version 1.22.0

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

DigitalOcean Ansible Collection.

**Authors:**

- Ansible (<https://github.com/ansible>)
- BondAnthony (<https://github.com/BondAnthony>)
- Akasurde (<https://github.com/Akasurde>)
- pmarques (<https://github.com/pmarques>)
- geerlingguy (<https://www.jeffgeerling.com/>)
- Andres Hermosilla (<https://github.com/rezen>)
- Luis (<https://github.com/lalvarezguillen>)
- grzs (<https://github.com/grzs>)
- Lucas Basquerotto (<https://github.com/lucasbasquerotto>)
- Tadej Borovšak (<https://github.com/tadeboro>)
- Mark Mercado (<https://github.com/mamercad>)
- Mike Pontillo (<https://github.com/mpontillo>)
- Felix Fontein (<https://github.com/felixfontein>)
- Andrew Starr-Bochicchio (<https://github.com/andrewsomething>)
- Sam Pinkus (<https://github.com/sgpinkus>)
- Luis (<https://github.com/lalvarezguillen>)
- John R Barker (<https://github.com/gundalow>)
- Andrew Klychkov (<https://github.com/Andersson007>)
- Tyler Auerbeck (<https://github.com/tylerauerbeck>)
- Angel Aviel Domaoan (<https://github.com/tenshiAMD>)
- Max Truxa (<https://github.com/maxtruxa>)
- Franco Posa (<https://github.com/francoposa>)
- magicrobotmonkey (<https://github.com/magicrobotmonkey>)
- radioactive73 (<https://github.com/radioactive73>)
- danxg87 (<https://github.com/danxg87>)
- Sviatoslav Sydorenko (<https://github.com/webknjaz>)
- Vitaly Khabarov (<https://github.com/vitkhab>)
- Onur Güzel (<https://github.com/onurguzel>)
- Shuaib Munshi (<https://github.com/shuaibmunshi>)
- Corey Wright (<https://github.com/coreywright>)

**Supported ansible-core versions:**

- 2.9.10 or newer

[Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)

## [Plugin Index](index.md#id2)

These are the plugins in the community.digitalocean collection:

### Modules

- [digital_ocean module](digital_ocean_module.md#ansible-collections-community-digitalocean-digital-ocean-module) – Create/delete a droplet/SSH_key in DigitalOcean
- [digital_ocean_account_info module](digital_ocean_account_info_module.md#ansible-collections-community-digitalocean-digital-ocean-account-info-module) – Gather information about DigitalOcean User account
- [digital_ocean_balance_info module](digital_ocean_balance_info_module.md#ansible-collections-community-digitalocean-digital-ocean-balance-info-module) – Display DigitalOcean customer balance
- [digital_ocean_block_storage module](digital_ocean_block_storage_module.md#ansible-collections-community-digitalocean-digital-ocean-block-storage-module) – Create/destroy or attach/detach Block Storage volumes in DigitalOcean
- [digital_ocean_cdn_endpoints module](digital_ocean_cdn_endpoints_module.md#ansible-collections-community-digitalocean-digital-ocean-cdn-endpoints-module) – Create, update, and delete DigitalOcean CDN Endpoints
- [digital_ocean_cdn_endpoints_info module](digital_ocean_cdn_endpoints_info_module.md#ansible-collections-community-digitalocean-digital-ocean-cdn-endpoints-info-module) – Display DigitalOcean CDN Endpoints
- [digital_ocean_certificate module](digital_ocean_certificate_module.md#ansible-collections-community-digitalocean-digital-ocean-certificate-module) – Manage certificates in DigitalOcean
- [digital_ocean_certificate_info module](digital_ocean_certificate_info_module.md#ansible-collections-community-digitalocean-digital-ocean-certificate-info-module) – Gather information about DigitalOcean certificates
- [digital_ocean_database module](digital_ocean_database_module.md#ansible-collections-community-digitalocean-digital-ocean-database-module) – Create and delete a DigitalOcean database
- [digital_ocean_database_info module](digital_ocean_database_info_module.md#ansible-collections-community-digitalocean-digital-ocean-database-info-module) – Gather information about DigitalOcean databases
- [digital_ocean_domain module](digital_ocean_domain_module.md#ansible-collections-community-digitalocean-digital-ocean-domain-module) – Create/delete a DNS domain in DigitalOcean
- [digital_ocean_domain_info module](digital_ocean_domain_info_module.md#ansible-collections-community-digitalocean-digital-ocean-domain-info-module) – Gather information about DigitalOcean Domains
- [digital_ocean_domain_record module](digital_ocean_domain_record_module.md#ansible-collections-community-digitalocean-digital-ocean-domain-record-module) – Manage DigitalOcean domain records
- [digital_ocean_domain_record_info module](digital_ocean_domain_record_info_module.md#ansible-collections-community-digitalocean-digital-ocean-domain-record-info-module) – Gather information about DigitalOcean domain records
- [digital_ocean_droplet module](digital_ocean_droplet_module.md#ansible-collections-community-digitalocean-digital-ocean-droplet-module) – Create and delete a DigitalOcean droplet
- [digital_ocean_droplet_info module](digital_ocean_droplet_info_module.md#ansible-collections-community-digitalocean-digital-ocean-droplet-info-module) – Gather information about DigitalOcean Droplets
- [digital_ocean_firewall module](digital_ocean_firewall_module.md#ansible-collections-community-digitalocean-digital-ocean-firewall-module) – Manage cloud firewalls within DigitalOcean
- [digital_ocean_firewall_info module](digital_ocean_firewall_info_module.md#ansible-collections-community-digitalocean-digital-ocean-firewall-info-module) – Gather information about DigitalOcean firewalls
- [digital_ocean_floating_ip module](digital_ocean_floating_ip_module.md#ansible-collections-community-digitalocean-digital-ocean-floating-ip-module) – Manage DigitalOcean Floating IPs
- [digital_ocean_floating_ip_info module](digital_ocean_floating_ip_info_module.md#ansible-collections-community-digitalocean-digital-ocean-floating-ip-info-module) – DigitalOcean Floating IPs information
- [digital_ocean_image_info module](digital_ocean_image_info_module.md#ansible-collections-community-digitalocean-digital-ocean-image-info-module) – Gather information about DigitalOcean images
- [digital_ocean_kubernetes module](digital_ocean_kubernetes_module.md#ansible-collections-community-digitalocean-digital-ocean-kubernetes-module) – Create and delete a DigitalOcean Kubernetes cluster
- [digital_ocean_kubernetes_info module](digital_ocean_kubernetes_info_module.md#ansible-collections-community-digitalocean-digital-ocean-kubernetes-info-module) – Returns information about an existing DigitalOcean Kubernetes cluster
- [digital_ocean_load_balancer module](digital_ocean_load_balancer_module.md#ansible-collections-community-digitalocean-digital-ocean-load-balancer-module) – Manage DigitalOcean Load Balancers
- [digital_ocean_load_balancer_info module](digital_ocean_load_balancer_info_module.md#ansible-collections-community-digitalocean-digital-ocean-load-balancer-info-module) – Gather information about DigitalOcean load balancers
- [digital_ocean_monitoring_alerts module](digital_ocean_monitoring_alerts_module.md#ansible-collections-community-digitalocean-digital-ocean-monitoring-alerts-module) – Programmatically retrieve metrics as well as configure alert policies based on these metrics
- [digital_ocean_monitoring_alerts_info module](digital_ocean_monitoring_alerts_info_module.md#ansible-collections-community-digitalocean-digital-ocean-monitoring-alerts-info-module) – Programmatically retrieve metrics as well as configure alert policies based on these metrics
- [digital_ocean_project module](digital_ocean_project_module.md#ansible-collections-community-digitalocean-digital-ocean-project-module) – Manage a DigitalOcean project
- [digital_ocean_project_info module](digital_ocean_project_info_module.md#ansible-collections-community-digitalocean-digital-ocean-project-info-module) – Gather information about DigitalOcean Projects
- [digital_ocean_region_info module](digital_ocean_region_info_module.md#ansible-collections-community-digitalocean-digital-ocean-region-info-module) – Gather information about DigitalOcean regions
- [digital_ocean_size_info module](digital_ocean_size_info_module.md#ansible-collections-community-digitalocean-digital-ocean-size-info-module) – Gather information about DigitalOcean Droplet sizes
- [digital_ocean_snapshot module](digital_ocean_snapshot_module.md#ansible-collections-community-digitalocean-digital-ocean-snapshot-module) – Create and delete DigitalOcean snapshots
- [digital_ocean_snapshot_info module](digital_ocean_snapshot_info_module.md#ansible-collections-community-digitalocean-digital-ocean-snapshot-info-module) – Gather information about DigitalOcean Snapshot
- [digital_ocean_spaces module](digital_ocean_spaces_module.md#ansible-collections-community-digitalocean-digital-ocean-spaces-module) – Create and remove DigitalOcean Spaces.
- [digital_ocean_spaces_info module](digital_ocean_spaces_info_module.md#ansible-collections-community-digitalocean-digital-ocean-spaces-info-module) – List DigitalOcean Spaces.
- [digital_ocean_sshkey module](digital_ocean_sshkey_module.md#ansible-collections-community-digitalocean-digital-ocean-sshkey-module) – Manage DigitalOcean SSH keys
- [digital_ocean_sshkey_info module](digital_ocean_sshkey_info_module.md#ansible-collections-community-digitalocean-digital-ocean-sshkey-info-module) – Gather information about DigitalOcean SSH keys
- [digital_ocean_tag module](digital_ocean_tag_module.md#ansible-collections-community-digitalocean-digital-ocean-tag-module) – Create and remove tag(s) to DigitalOcean resource.
- [digital_ocean_tag_info module](digital_ocean_tag_info_module.md#ansible-collections-community-digitalocean-digital-ocean-tag-info-module) – Gather information about DigitalOcean tags
- [digital_ocean_volume_info module](digital_ocean_volume_info_module.md#ansible-collections-community-digitalocean-digital-ocean-volume-info-module) – Gather information about DigitalOcean volumes
- [digital_ocean_vpc module](digital_ocean_vpc_module.md#ansible-collections-community-digitalocean-digital-ocean-vpc-module) – Create and delete DigitalOcean VPCs
- [digital_ocean_vpc_info module](digital_ocean_vpc_info_module.md#ansible-collections-community-digitalocean-digital-ocean-vpc-info-module) – Gather information about DigitalOcean VPCs

### Inventory Plugins

- [digitalocean inventory](digitalocean_inventory.md#ansible-collections-community-digitalocean-digitalocean-inventory) – DigitalOcean Inventory Plugin

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
