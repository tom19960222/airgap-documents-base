---
collection: ansible
version: "8"
title: "Theforeman.Foreman"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/index.html
fetched_at: 2026-07-28T01:03:01+00:00
---
# Theforeman.Foreman

Collection version 3.15.0

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Ansible Modules to manage Foreman and Katello installations

**Authors:**

- @lessfoobar <[59063885+lessfoobar@users.noreply.github.com](mailto:59063885+lessfoobar%40users.noreply.github.com)>
- Adam Růžička <[aruzicka@redhat.com](mailto:aruzicka%40redhat.com)>
- Alan.Wong <[alawong@redhat.com](mailto:alawong%40redhat.com)>
- AlanCoding <[arominge@redhat.com](mailto:arominge%40redhat.com)>
- Andrea Perotti <[aperotti@redhat.com](mailto:aperotti%40redhat.com)>
- Andrew Kofink <[ajkofink@gmail.com](mailto:ajkofink%40gmail.com)>
- Anthony Green <[green@moxielogic.com](mailto:green%40moxielogic.com)>
- Anton <[nesanton@gmail.com](mailto:nesanton%40gmail.com)>
- Baptiste Agasse <[baptiste.agasse@gmail.com](mailto:baptiste.agasse%40gmail.com)>
- Bernhard Hopfenmüller <[hopfenmueller@atix.de](mailto:hopfenmueller%40atix.de)>
- Bernhard Suttner <[sbernhard@users.noreply.github.com](mailto:sbernhard%40users.noreply.github.com)>
- Bryan Kearney <[bkearney@redhat.com](mailto:bkearney%40redhat.com)>
- Chris Forkner <[gen2fish@gmail.com](mailto:gen2fish%40gmail.com)>
- Chris Hindman <[chindman@chindman.remote.csb](mailto:chindman%40chindman.remote.csb)>
- Chris Snell <[chsnell@users.noreply.github.com](mailto:chsnell%40users.noreply.github.com)>
- Christoffer Reijer <[ephracis@gmail.com](mailto:ephracis%40gmail.com)>
- Dave Thomas <[11580510+dthomastx@users.noreply.github.com](mailto:11580510+dthomastx%40users.noreply.github.com)>
- Deric Crago <[deric.crago@gmail.com](mailto:deric.crago%40gmail.com)>
- Eric D. Helms <[ericdhelms@gmail.com](mailto:ericdhelms%40gmail.com)>
- Eric L <[ericzolf@users.noreply.github.com](mailto:ericzolf%40users.noreply.github.com)>
- Ethan <[smithe2413@gmail.com](mailto:smithe2413%40gmail.com)>
- Evgeni Golov <[evgeni@golov.de](mailto:evgeni%40golov.de)>
- Ewoud Kohl van Wijngaarden <[ewoud@kohlvanwijngaarden.nl](mailto:ewoud%40kohlvanwijngaarden.nl)>
- Felix Fontein <[felix@fontein.de](mailto:felix%40fontein.de)>
- Gerald Vogt <[gvde@users.noreply.github.com](mailto:gvde%40users.noreply.github.com)>
- Greg Swift <[gregswift@gmail.com](mailto:gregswift%40gmail.com)>
- Griffin Sullivan <[gsulliva@redhat.com](mailto:gsulliva%40redhat.com)>
- Hideki Saito <[saito@fgrep.org](mailto:saito%40fgrep.org)>
- Ismael Puerto <[ismaelpuerto@users.noreply.github.com](mailto:ismaelpuerto%40users.noreply.github.com)>
- Jameer Pathan <[jpathan@redhat.com](mailto:jpathan%40redhat.com)>
- James Jeffers <[jjeffers@redhat.com](mailto:jjeffers%40redhat.com)>
- James Stuart <[james@stuart.name](mailto:james%40stuart.name)>
- Jeffrey van Pelt <[jeff@vanpelt.one](mailto:jeff%40vanpelt.one)>
- Jeremy Albinet <[jalbinet@scaleway.com](mailto:jalbinet%40scaleway.com)>
- Jeremy Lenz <[jlenz@redhat.com](mailto:jlenz%40redhat.com)>
- Jesper Reenberg <[jesper.reenberg@gmail.com](mailto:jesper.reenberg%40gmail.com)>
- John Berninger <[john.berninger@gmail.com](mailto:john.berninger%40gmail.com)>
- Josh Swanson <[jswanson@redhat.com](mailto:jswanson%40redhat.com)>
- Julien Godin <[julien.godin@camptocamp.com](mailto:julien.godin%40camptocamp.com)>
- Kenny Tordeurs <[ktordeur@redhat.com](mailto:ktordeur%40redhat.com)>
- Kirill Shirinkin <[fodojyko@gmail.com](mailto:fodojyko%40gmail.com)>
- Leos Stejskal <[lstejska@redhat.com](mailto:lstejska%40redhat.com)>
- Lester Cheung <[lcheung@threatmetrix.com](mailto:lcheung%40threatmetrix.com)>
- Lester Claudio <[claudiol@redhat.com](mailto:claudiol%40redhat.com)>
- Lucas Bickel <[hairmare@rabe.ch](mailto:hairmare%40rabe.ch)>
- Lukas Magauer <[Lukas.Magauer@engel.at](mailto:Lukas.Magauer%40engel.at)>
- Lukáš Zapletal <[lzap+git@redhat.com](mailto:lzap+git%40redhat.com)>
- Manisha Singhal <[manisha1595@gmail.com](mailto:manisha1595%40gmail.com)>
- Manuel Bonk <[githubMB@bonkii.com](mailto:githubMB%40bonkii.com)>
- Marcelo Moreira de Mello <[tchello.mello@gmail.com](mailto:tchello.mello%40gmail.com)>
- Marek Czernek <[mczernek@redhat.com](mailto:mczernek%40redhat.com)>
- Mark Hlawatschek <[hlawatschek@atix.de](mailto:hlawatschek%40atix.de)>
- Markus Bucher <[bucher@atix.de](mailto:bucher%40atix.de)>
- Martin Schlossarek <[martin.schlossarek@gmail.com](mailto:martin.schlossarek%40gmail.com)>
- Matthias Dellweg <[2500@gmx.de](mailto:2500%40gmx.de)>
- Miikka Joutsenvirta <[miikka.joutsenvirta@dna.fi](mailto:miikka.joutsenvirta%40dna.fi)>
- Nikhil Jain <[jainnikhil30@gmail.com](mailto:jainnikhil30%40gmail.com)>
- Olivier <[oliverf1ca@yahoo.com](mailto:oliverf1ca%40yahoo.com)>
- Ondrej Prazak <[oprazak@redhat.com](mailto:oprazak%40redhat.com)>
- Ondřej Ezr <[oezr@redhat.com](mailto:oezr%40redhat.com)>
- Ondřej Gajdušek <[ogajduse@redhat.com](mailto:ogajduse%40redhat.com)>
- Patrick C. F. Ernzer <[pcfe@pcfe.net](mailto:pcfe%40pcfe.net)>
- Patrick Creech <[pcreech@redhat.com](mailto:pcreech%40redhat.com)>
- Paul Armstrong <[parmstro@redhat.com](mailto:parmstro%40redhat.com)>
- Paul Belanger <[pabelanger@redhat.com](mailto:pabelanger%40redhat.com)>
- Paul Gration <[pmgration@gmail.com](mailto:pmgration%40gmail.com)>
- Peter Ondrejka <[pondrejk@redhat.com](mailto:pondrejk%40redhat.com)>
- Philipp <[philipp98.joos@gmail.com](mailto:philipp98.joos%40gmail.com)>
- Quirin Pamp <[pamp@atix.de](mailto:pamp%40atix.de)>
- Richard Stempfl <[richielatk@gmail.com](mailto:richielatk%40gmail.com)>
- Richard Waax <[40852459+riwael@users.noreply.github.com](mailto:40852459+riwael%40users.noreply.github.com)>
- Sam <[samcalvert@me.com](mailto:samcalvert%40me.com)>
- Samir Jha <[sjha4@ncsu.edu](mailto:sjha4%40ncsu.edu)>
- Sean O’Keeffe <[seanokeeffe797@gmail.com](mailto:seanokeeffe797%40gmail.com)>
- Sorin Sbarnea <[sorin.sbarnea@gmail.com](mailto:sorin.sbarnea%40gmail.com)>
- Steffen Frömer <[knumskull@users.noreply.github.com](mailto:knumskull%40users.noreply.github.com)>
- Stoned Elipot <[stoned.elipot@gmail.com](mailto:stoned.elipot%40gmail.com)>
- Sven Meeus <[sven.meeus@scarlet.be](mailto:sven.meeus%40scarlet.be)>
- TTherouanne <[thomas@therouanne.com](mailto:thomas%40therouanne.com)>
- Thomas Mueller <[thomas@chaschperli.ch](mailto:thomas%40chaschperli.ch)>
- William Bradford Clark <[wclark@redhat.com](mailto:wclark%40redhat.com)>
- Yifat Makias <[ymakias@redhat.com](mailto:ymakias%40redhat.com)>
- achevalet <[anthony.chevalet@gmail.com](mailto:anthony.chevalet%40gmail.com)>
- alesc <[github@alesc.fr](mailto:github%40alesc.fr)>
- bob <[57952350+TheRedGreek@users.noreply.github.com](mailto:57952350+TheRedGreek%40users.noreply.github.com)>
- calvingsmith <[4283930+calvingsmith@users.noreply.github.com](mailto:4283930+calvingsmith%40users.noreply.github.com)>
- divialth <[65872926+divialth@users.noreply.github.com](mailto:65872926+divialth%40users.noreply.github.com)>
- furhouse <[furhouse@users.noreply.github.com](mailto:furhouse%40users.noreply.github.com)>
- gardar <[gardar@users.noreply.github.com](mailto:gardar%40users.noreply.github.com)>
- igramic <[36156377+igramic@users.noreply.github.com](mailto:36156377+igramic%40users.noreply.github.com)>
- jerrejkw <[43955357+jerrejkw@users.noreply.github.com](mailto:43955357+jerrejkw%40users.noreply.github.com)>
- linuxonfire <[jaimescampositzel@gmail.com](mailto:jaimescampositzel%40gmail.com)>
- marco <[marco.markgraf@transporeon.com](mailto:marco.markgraf%40transporeon.com)>
- metalcated <[mike.gomon@gmail.com](mailto:mike.gomon%40gmail.com)>
- russianguppie <[46544650+russianguppie@users.noreply.github.com](mailto:46544650+russianguppie%40users.noreply.github.com)>
- willtome <[willtome@gmail.com](mailto:willtome%40gmail.com)>
- yuqo2450 <[79540477+yuqo2450@users.noreply.github.com](mailto:79540477+yuqo2450%40users.noreply.github.com)>

**Supported ansible-core versions:**

- 2.9.17 or newer

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)

## [Plugin Index](index.md#id2)

These are the plugins in the theforeman.foreman collection:

### Modules

- [activation_key module](activation_key_module.md#ansible-collections-theforeman-foreman-activation-key-module) – Manage Activation Keys
- [architecture module](architecture_module.md#ansible-collections-theforeman-foreman-architecture-module) – Manage Architectures
- [auth_source_ldap module](auth_source_ldap_module.md#ansible-collections-theforeman-foreman-auth-source-ldap-module) – Manage LDAP Authentication Sources
- [bookmark module](bookmark_module.md#ansible-collections-theforeman-foreman-bookmark-module) – Manage Bookmarks
- [compute_attribute module](compute_attribute_module.md#ansible-collections-theforeman-foreman-compute-attribute-module) – Manage Compute Attributes
- [compute_profile module](compute_profile_module.md#ansible-collections-theforeman-foreman-compute-profile-module) – Manage Compute Profiles
- [compute_resource module](compute_resource_module.md#ansible-collections-theforeman-foreman-compute-resource-module) – Manage Compute Resources
- [config_group module](config_group_module.md#ansible-collections-theforeman-foreman-config-group-module) – Manage (Puppet) Config Groups
- [content_credential module](content_credential_module.md#ansible-collections-theforeman-foreman-content-credential-module) – Manage Content Credentials
- [content_export_info module](content_export_info_module.md#ansible-collections-theforeman-foreman-content-export-info-module) – List content exports
- [content_export_library module](content_export_library_module.md#ansible-collections-theforeman-foreman-content-export-library-module) – Manage library content exports
- [content_export_repository module](content_export_repository_module.md#ansible-collections-theforeman-foreman-content-export-repository-module) – Manage repository content exports
- [content_export_version module](content_export_version_module.md#ansible-collections-theforeman-foreman-content-export-version-module) – Manage content view version content exports
- [content_upload module](content_upload_module.md#ansible-collections-theforeman-foreman-content-upload-module) – Upload content to a repository
- [content_view module](content_view_module.md#ansible-collections-theforeman-foreman-content-view-module) – Manage Content Views
- [content_view_filter module](content_view_filter_module.md#ansible-collections-theforeman-foreman-content-view-filter-module) – Manage Content View Filters
- [content_view_filter_info module](content_view_filter_info_module.md#ansible-collections-theforeman-foreman-content-view-filter-info-module) – Fetch information about a Content View Filter
- [content_view_filter_rule module](content_view_filter_rule_module.md#ansible-collections-theforeman-foreman-content-view-filter-rule-module) – Manage content view filter rules
- [content_view_filter_rule_info module](content_view_filter_rule_info_module.md#ansible-collections-theforeman-foreman-content-view-filter-rule-info-module) – Fetch information about a Content View Filter Rule
- [content_view_info module](content_view_info_module.md#ansible-collections-theforeman-foreman-content-view-info-module) – Fetch information about Content Views
- [content_view_version module](content_view_version_module.md#ansible-collections-theforeman-foreman-content-view-version-module) – Manage Content View Versions
- [content_view_version_info module](content_view_version_info_module.md#ansible-collections-theforeman-foreman-content-view-version-info-module) – Fetch information about Content Views
- [discovery_rule module](discovery_rule_module.md#ansible-collections-theforeman-foreman-discovery-rule-module) – Manage Host Discovery Rules
- [domain module](domain_module.md#ansible-collections-theforeman-foreman-domain-module) – Manage Domains
- [domain_info module](domain_info_module.md#ansible-collections-theforeman-foreman-domain-info-module) – Fetch information about Domains
- [external_usergroup module](external_usergroup_module.md#ansible-collections-theforeman-foreman-external-usergroup-module) – Manage External User Groups
- [global_parameter module](global_parameter_module.md#ansible-collections-theforeman-foreman-global-parameter-module) – Manage Global Parameters
- [hardware_model module](hardware_model_module.md#ansible-collections-theforeman-foreman-hardware-model-module) – Manage Hardware Models
- [host module](host_module.md#ansible-collections-theforeman-foreman-host-module) – Manage Hosts
- [host_collection module](host_collection_module.md#ansible-collections-theforeman-foreman-host-collection-module) – Manage Host Collections
- [host_errata_info module](host_errata_info_module.md#ansible-collections-theforeman-foreman-host-errata-info-module) – Fetch information about Host Errata
- [host_info module](host_info_module.md#ansible-collections-theforeman-foreman-host-info-module) – Fetch information about Hosts
- [host_power module](host_power_module.md#ansible-collections-theforeman-foreman-host-power-module) – Manage Power State of Hosts
- [hostgroup module](hostgroup_module.md#ansible-collections-theforeman-foreman-hostgroup-module) – Manage Hostgroups
- [hostgroup_info module](hostgroup_info_module.md#ansible-collections-theforeman-foreman-hostgroup-info-module) – Get information about hostgroup(s)
- [http_proxy module](http_proxy_module.md#ansible-collections-theforeman-foreman-http-proxy-module) – Manage HTTP Proxies
- [image module](image_module.md#ansible-collections-theforeman-foreman-image-module) – Manage Images
- [installation_medium module](installation_medium_module.md#ansible-collections-theforeman-foreman-installation-medium-module) – Manage Installation Media
- [job_invocation module](job_invocation_module.md#ansible-collections-theforeman-foreman-job-invocation-module) – Invoke Remote Execution Jobs
- [job_template module](job_template_module.md#ansible-collections-theforeman-foreman-job-template-module) – Manage Job Templates
- [lifecycle_environment module](lifecycle_environment_module.md#ansible-collections-theforeman-foreman-lifecycle-environment-module) – Manage Lifecycle Environments
- [location module](location_module.md#ansible-collections-theforeman-foreman-location-module) – Manage Locations
- [operatingsystem module](operatingsystem_module.md#ansible-collections-theforeman-foreman-operatingsystem-module) – Manage Operating Systems
- [organization module](organization_module.md#ansible-collections-theforeman-foreman-organization-module) – Manage Organizations
- [organization_info module](organization_info_module.md#ansible-collections-theforeman-foreman-organization-info-module) – Get information about organization(s)
- [os_default_template module](os_default_template_module.md#ansible-collections-theforeman-foreman-os-default-template-module) – Manage Default Template Associations To Operating Systems
- [partition_table module](partition_table_module.md#ansible-collections-theforeman-foreman-partition-table-module) – Manage Partition Table Templates
- [product module](product_module.md#ansible-collections-theforeman-foreman-product-module) – Manage Products
- [provisioning_template module](provisioning_template_module.md#ansible-collections-theforeman-foreman-provisioning-template-module) – Manage Provisioning Templates
- [puppet_environment module](puppet_environment_module.md#ansible-collections-theforeman-foreman-puppet-environment-module) – Manage Puppet Environments
- [puppetclasses_import module](puppetclasses_import_module.md#ansible-collections-theforeman-foreman-puppetclasses-import-module) – Import Puppet Classes from a Proxy
- [realm module](realm_module.md#ansible-collections-theforeman-foreman-realm-module) – Manage Realms
- [redhat_manifest module](redhat_manifest_module.md#ansible-collections-theforeman-foreman-redhat-manifest-module) – Interact with a Red Hat Satellite Subscription Manifest
- [repository module](repository_module.md#ansible-collections-theforeman-foreman-repository-module) – Manage Repositories
- [repository_info module](repository_info_module.md#ansible-collections-theforeman-foreman-repository-info-module) – Fetch information about Repositories
- [repository_set module](repository_set_module.md#ansible-collections-theforeman-foreman-repository-set-module) – Enable/disable Red Hat Repositories available through subscriptions
- [repository_set_info module](repository_set_info_module.md#ansible-collections-theforeman-foreman-repository-set-info-module) – Fetch information about Red Hat Repositories
- [repository_sync module](repository_sync_module.md#ansible-collections-theforeman-foreman-repository-sync-module) – Sync a Repository or Product
- [resource_info module](resource_info_module.md#ansible-collections-theforeman-foreman-resource-info-module) – Gather information about resources
- [role module](role_module.md#ansible-collections-theforeman-foreman-role-module) – Manage Roles
- [scap_content module](scap_content_module.md#ansible-collections-theforeman-foreman-scap-content-module) – Manage SCAP content
- [scap_tailoring_file module](scap_tailoring_file_module.md#ansible-collections-theforeman-foreman-scap-tailoring-file-module) – Manage SCAP Tailoring Files
- [scc_account module](scc_account_module.md#ansible-collections-theforeman-foreman-scc-account-module) – Manage SUSE Customer Center Accounts
- [scc_product module](scc_product_module.md#ansible-collections-theforeman-foreman-scc-product-module) – Subscribe SUSE Customer Center Account Products
- [setting module](setting_module.md#ansible-collections-theforeman-foreman-setting-module) – Manage Settings
- [setting_info module](setting_info_module.md#ansible-collections-theforeman-foreman-setting-info-module) – Fetch information about Settings
- [smart_class_parameter module](smart_class_parameter_module.md#ansible-collections-theforeman-foreman-smart-class-parameter-module) – Manage Smart Class Parameters
- [smart_class_parameter_override_value module](smart_class_parameter_override_value_module.md#ansible-collections-theforeman-foreman-smart-class-parameter-override-value-module) – Manage Smart Class Parameter Override Values
- [smart_proxy module](smart_proxy_module.md#ansible-collections-theforeman-foreman-smart-proxy-module) – Manage Smart Proxies
- [snapshot module](snapshot_module.md#ansible-collections-theforeman-foreman-snapshot-module) – Manage Snapshots
- [snapshot_info module](snapshot_info_module.md#ansible-collections-theforeman-foreman-snapshot-info-module) – Fetch information about Foreman Snapshots
- [status_info module](status_info_module.md#ansible-collections-theforeman-foreman-status-info-module) – Get status info
- [subnet module](subnet_module.md#ansible-collections-theforeman-foreman-subnet-module) – Manage Subnets
- [subnet_info module](subnet_info_module.md#ansible-collections-theforeman-foreman-subnet-info-module) – Fetch information about Subnets
- [subscription_info module](subscription_info_module.md#ansible-collections-theforeman-foreman-subscription-info-module) – Fetch information about Subscriptions
- [subscription_manifest module](subscription_manifest_module.md#ansible-collections-theforeman-foreman-subscription-manifest-module) – Manage Subscription Manifests
- [sync_plan module](sync_plan_module.md#ansible-collections-theforeman-foreman-sync-plan-module) – Manage Sync Plans
- [templates_import module](templates_import_module.md#ansible-collections-theforeman-foreman-templates-import-module) – Sync Templates from a repository
- [user module](user_module.md#ansible-collections-theforeman-foreman-user-module) – Manage Users
- [usergroup module](usergroup_module.md#ansible-collections-theforeman-foreman-usergroup-module) – Manage User Groups
- [wait_for_task module](wait_for_task_module.md#ansible-collections-theforeman-foreman-wait-for-task-module) – Wait for a task

### Callback Plugins

- [foreman callback](foreman_callback.md#ansible-collections-theforeman-foreman-foreman-callback) – Sends events to Foreman

### Filter Plugins

- [cp_label filter](cp_label_filter.md#ansible-collections-theforeman-foreman-cp-label-filter) – Convert strings to Candlepin labels

### Inventory Plugins

- [foreman inventory](foreman_inventory.md#ansible-collections-theforeman-foreman-foreman-inventory) – Foreman inventory source

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
