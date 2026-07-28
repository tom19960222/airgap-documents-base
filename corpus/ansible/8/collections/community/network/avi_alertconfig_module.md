---
collection: ansible
version: "8"
title: "community.network.avi_alertconfig module – Module for setup of AlertConfig Avi RESTful Object"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/avi_alertconfig_module.html
fetched_at: 2026-07-28T01:54:22+00:00
---
# community.network.avi_alertconfig module – Module for setup of AlertConfig Avi RESTful Object

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
> You need further requirements to be able to use this module,
> see [Requirements](avi_alertconfig_module.md#ansible-collections-community-network-avi-alertconfig-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.avi_alertconfig`.

- [Synopsis](avi_alertconfig_module.md#synopsis)
- [Requirements](avi_alertconfig_module.md#requirements)
- [Parameters](avi_alertconfig_module.md#parameters)
- [Notes](avi_alertconfig_module.md#notes)
- [Examples](avi_alertconfig_module.md#examples)
- [Return Values](avi_alertconfig_module.md#return-values)

## [Synopsis](avi_alertconfig_module.md#id1)

- This module is used to configure AlertConfig object
- more examples at <https://github.com/avinetworks/devops>

Aliases: network.avi.avi_alertconfig

## [Requirements](avi_alertconfig_module.md#id2)

The below requirements are needed on the host that executes this module.

- avisdk

## [Parameters](avi_alertconfig_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **action_group_ref**  string | The alert config will trigger the selected alert action, which can send notifications and execute a controlscript.  It is a reference to an object of type actiongroupconfig. |
| **alert_rule**  string / required | List of filters matching on events or client logs used for triggering alerts. |
| **api_context**  dictionary | Avi API context that includes current session ID and CSRF Token.  This allows user to perform single login and re-use the session. |
| **api_version**  string | Avi API version of to use for Avi API and objects.  **Default:** `"16.4.4"` |
| **autoscale_alert**  boolean | This alert config applies to auto scale alerts.  **Choices:**   - `false` - `true` |
| **avi_api_patch_op**  string | Patch operation to use when using avi_api_update_method as patch.  **Choices:**   - `"add"` - `"replace"` - `"delete"` |
| **avi_api_update_method**  string | Default method for object update is HTTP PUT.  Setting to patch will override that behavior to use HTTP PATCH.  **Choices:**   - `"put"` ← (default) - `"patch"` |
| **avi_credentials**  dictionary | Avi Credentials dictionary which can be used in lieu of enumerating Avi Controller login details. |
| **api_version**  string | Avi controller version  **Default:** `"16.4.4"` |
| **controller**  string | Avi controller IP or SQDN |
| **csrftoken**  string | Avi controller API csrftoken to reuse existing session with session id  **Default:** `""` |
| **password**  string | Avi controller password |
| **port**  string | Avi controller port |
| **session_id**  string | Avi controller API session id to reuse existing session with csrftoken  **Default:** `""` |
| **tenant**  string | Avi controller tenant  **Default:** `"admin"` |
| **tenant_uuid**  string | Avi controller tenant UUID  **Default:** `""` |
| **timeout**  string | Avi controller request timeout  **Default:** `300` |
| **token**  string | Avi controller API token  **Default:** `""` |
| **username**  string | Avi controller username |
| **avi_disable_session_cache_as_fact**  boolean | It disables avi session information to be cached as a fact.  **Choices:**   - `false` ← (default) - `true` |
| **category**  string / required | Determines whether an alert is raised immediately when event occurs (realtime) or after specified number of events occurs within rolling time  window.  Enum options - REALTIME, ROLLINGWINDOW, WATERMARK.  Default value when not specified in API or module is interpreted by Avi Controller as REALTIME. |
| **controller**  string | IP address or hostname of the controller. The default value is the environment variable `AVI_CONTROLLER`. |
| **description**  string | A custom description field. |
| **enabled**  boolean | Enable or disable this alert config from generating new alerts.  Default value when not specified in API or module is interpreted by Avi Controller as True.  **Choices:**   - `false` - `true` |
| **expiry_time**  string | An alert is expired and deleted after the expiry time has elapsed.  The original event triggering the alert remains in the event’s log.  Allowed values are 1-31536000.  Default value when not specified in API or module is interpreted by Avi Controller as 86400. |
| **name**  string / required | Name of the alert configuration. |
| **obj_uuid**  string | Uuid of the resource for which alert was raised. |
| **object_type**  string | The object type to which the alert config is associated with.  Valid object types are - virtual service, pool, service engine.  Enum options - VIRTUALSERVICE, POOL, HEALTHMONITOR, NETWORKPROFILE, APPLICATIONPROFILE, HTTPPOLICYSET, DNSPOLICY, SECURITYPOLICY, IPADDRGROUP,  STRINGGROUP, SSLPROFILE, SSLKEYANDCERTIFICATE, NETWORKSECURITYPOLICY, APPLICATIONPERSISTENCEPROFILE, ANALYTICSPROFILE, VSDATASCRIPTSET, TENANT,  PKIPROFILE, AUTHPROFILE, CLOUD, SERVERAUTOSCALEPOLICY, AUTOSCALELAUNCHCONFIG, MICROSERVICEGROUP, IPAMPROFILE, HARDWARESECURITYMODULEGROUP,  POOLGROUP, PRIORITYLABELS, POOLGROUPDEPLOYMENTPOLICY, GSLBSERVICE, GSLBSERVICERUNTIME, SCHEDULER, GSLBGEODBPROFILE,  GSLBAPPLICATIONPERSISTENCEPROFILE, TRAFFICCLONEPROFILE, VSVIP, WAFPOLICY, WAFPROFILE, ERRORPAGEPROFILE, ERRORPAGEBODY, L4POLICYSET,  GSLBSERVICERUNTIMEBATCH, WAFPOLICYPSMGROUP, PINGACCESSAGENT, SERVICEENGINEPOLICY, NATPOLICY, SSOPOLICY, PROTOCOLPARSER, SERVICEENGINE,  DEBUGSERVICEENGINE, DEBUGCONTROLLER, DEBUGVIRTUALSERVICE, SERVICEENGINEGROUP, SEPROPERTIES, NETWORK, CONTROLLERNODE, CONTROLLERPROPERTIES,  SYSTEMCONFIGURATION, VRFCONTEXT, USER, ALERTCONFIG, ALERTSYSLOGCONFIG, ALERTEMAILCONFIG, ALERTTYPECONFIG, APPLICATION, ROLE, CLOUDPROPERTIES,  SNMPTRAPPROFILE, ACTIONGROUPPROFILE, MICROSERVICE, ALERTPARAMS, ACTIONGROUPCONFIG, CLOUDCONNECTORUSER, GSLB, GSLBDNSUPDATE, GSLBSITEOPS,  GLBMGRWARMSTART, IPAMDNSRECORD, GSLBDNSGSSTATUS, GSLBDNSGEOFILEOPS, GSLBDNSGEOUPDATE, GSLBDNSGEOCLUSTEROPS, GSLBDNSCLEANUP, GSLBSITEOPSRESYNC,  IPAMDNSPROVIDERPROFILE, TCPSTATRUNTIME, UDPSTATRUNTIME, IPSTATRUNTIME, ARPSTATRUNTIME, MBSTATRUNTIME, IPSTKQSTATSRUNTIME, MALLOCSTATRUNTIME,  SHMALLOCSTATRUNTIME, CPUUSAGERUNTIME, L7GLOBALSTATSRUNTIME, L7VIRTUALSERVICESTATSRUNTIME, SEAGENTVNICDBRUNTIME, SEAGENTGRAPHDBRUNTIME,  SEAGENTSTATERUNTIME, INTERFACERUNTIME, ARPTABLERUNTIME, DISPATCHERSTATRUNTIME, DISPATCHERSTATCLEARRUNTIME, DISPATCHERTABLEDUMPRUNTIME,  DISPATCHERREMOTETIMERLISTDUMPRUNTIME, METRICSAGENTMESSAGE, HEALTHMONITORSTATRUNTIME, METRICSENTITYRUNTIME, PERSISTENCEINTERNAL,  HTTPPOLICYSETINTERNAL, DNSPOLICYINTERNAL, CONNECTIONDUMPRUNTIME, SHAREDDBSTATS, SHAREDDBSTATSCLEAR, ICMPSTATRUNTIME, ROUTETABLERUNTIME,  VIRTUALMACHINE, POOLSERVER, SEVSLIST, MEMINFORUNTIME, RTERINGSTATRUNTIME, ALGOSTATRUNTIME, HEALTHMONITORRUNTIME, CPUSTATRUNTIME, SEVM, HOST,  PORTGROUP, CLUSTER, DATACENTER, VCENTER, HTTPPOLICYSETSTATS, DNSPOLICYSTATS, METRICSSESTATS, RATELIMITERSTATRUNTIME, NETWORKSECURITYPOLICYSTATS,  TCPCONNRUNTIME, POOLSTATS, CONNPOOLINTERNAL, CONNPOOLSTATS, VSHASHSHOWRUNTIME, SELOGSTATSRUNTIME, NETWORKSECURITYPOLICYDETAIL, LICENSERUNTIME,  SERVERRUNTIME, METRICSRUNTIMESUMMARY, METRICSRUNTIMEDETAIL, DISPATCHERSEHMPROBETEMPDISABLERUNTIME, POOLDEBUG, VSLOGMGRMAP, SERUMINSERTIONSTATS,  HTTPCACHE, HTTPCACHESTATS, SEDOSSTATRUNTIME, VSDOSSTATRUNTIME, SERVERUPDATEREQ, VSSCALEOUTLIST, SEMEMDISTRUNTIME, TCPCONNRUNTIMEDETAIL,  SEUPGRADESTATUS, SEUPGRADEPREVIEW, SEFAULTINJECTEXHAUSTM, SEFAULTINJECTEXHAUSTMCL, SEFAULTINJECTEXHAUSTMCLSMALL, SEFAULTINJECTEXHAUSTCONN,  SEHEADLESSONLINEREQ, SEUPGRADE, SEUPGRADESTATUSDETAIL, SERESERVEDVS, SERESERVEDVSCLEAR, VSCANDIDATESEHOSTLIST, SEGROUPUPGRADE, REBALANCE,  SEGROUPREBALANCE, SEAUTHSTATSRUNTIME, AUTOSCALESTATE, VIRTUALSERVICEAUTHSTATS, NETWORKSECURITYPOLICYDOS, KEYVALINTERNAL, KEYVALSUMMARYINTERNAL,  SERVERSTATEUPDATEINFO, CLTRACKINTERNAL, CLTRACKSUMMARYINTERNAL, MICROSERVICERUNTIME, SEMICROSERVICE, VIRTUALSERVICEANALYSIS, CLIENTINTERNAL,  CLIENTSUMMARYINTERNAL, MICROSERVICEGROUPRUNTIME, BGPRUNTIME, REQUESTQUEUERUNTIME, MIGRATEALL, MIGRATEALLSTATUSSUMMARY, MIGRATEALLSTATUSDETAIL,  INTERFACESUMMARYRUNTIME, INTERFACELACPRUNTIME, DNSTABLE, GSLBSERVICEDETAIL, GSLBSERVICEINTERNAL, GSLBSERVICEHMONSTAT, SETROLESREQUEST,  TRAFFICCLONERUNTIME, GEOLOCATIONINFO, SEVSHBSTATRUNTIME, GEODBINTERNAL, GSLBSITEINTERNAL, WAFSTATS, USERDEFINEDDATASCRIPTCOUNTERS, LLDPRUNTIME,  VSESSHARINGPOOL, NDTABLERUNTIME, IP6STATRUNTIME, ICMP6STATRUNTIME, SEVSSPLACEMENT, L4POLICYSETSTATS, L4POLICYSETINTERNAL, BGPDEBUGINFO, SHARD,  CPUSTATRUNTIMEDETAIL, SEASSERTSTATRUNTIME, SEFAULTINJECTINFRA, SEAGENTASSERTSTATRUNTIME, SEDATASTORESTATUS, DIFFQUEUESTATUS, IP6ROUTETABLERUNTIME,  SECURITYMGRSTATE, VIRTUALSERVICESESCALEOUTSTATUS, SHARDSERVERSTATUS, SEAGENTSHARDCLIENTRESOURCEMAP, SEAGENTCONSISTENTHASH, SEAGENTVNICDBHISTORY,  SEAGENTSHARDCLIENTAPPMAP, SEAGENTSHARDCLIENTEVENTHISTORY, SENATSTATRUNTIME, SENATFLOWRUNTIME, SERESOURCEPROTO, SECONSUMERPROTO,  SECREATEPENDINGPROTO, PLACEMENTSTATS, SEVIPPROTO, RMVRFPROTO, VCENTERMAP, VIMGRVCENTERRUNTIME, INTERESTEDVMS, INTERESTEDHOSTS,  VCENTERSUPPORTEDCOUNTERS, ENTITYCOUNTERS, TRANSACTIONSTATS, SEVMCREATEPROGRESS, PLACEMENTSTATUS, VISUBFOLDERS, VIDATASTORE, VIHOSTRESOURCES,  CLOUDCONNECTOR, VINETWORKSUBNETVMS, VIDATASTORECONTENTS, VIMGRVCENTERCLOUDRUNTIME, VIVCENTERPORTGROUPS, VIVCENTERDATACENTERS, VIMGRHOSTRUNTIME,  PLACEMENTGLOBALS, APICCONFIGURATION, CIFTABLE, APICTRANSACTION, VIRTUALSERVICESTATEDBCACHESUMMARY, POOLSTATEDBCACHESUMMARY,  SERVERSTATEDBCACHESUMMARY, APICAGENTINTERNAL, APICTRANSACTIONFLAP, APICGRAPHINSTANCES, APICEPGS, APICEPGEPS, APICDEVICEPKGVER, APICTENANTS,  APICVMMDOMAINS, NSXCONFIGURATION, NSXSGTABLE, NSXAGENTINTERNAL, NSXSGINFO, NSXSGIPS, NSXAGENTINTERNALCLI, MAXOBJECTS. |
| **password**  string | Password of Avi user in Avi controller. The default value is the environment variable `AVI_PASSWORD`. |
| **recommendation**  string | Recommendation of alertconfig. |
| **rolling_window**  string | Only if the number of events is reached or exceeded within the time window will an alert be generated.  Allowed values are 1-31536000.  Default value when not specified in API or module is interpreted by Avi Controller as 300. |
| **source**  string / required | Signifies system events or the type of client logsused in this alert configuration.  Enum options - CONN_LOGS, APP_LOGS, EVENT_LOGS, METRICS. |
| **state**  string | The state that should be applied on the entity.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **summary**  string | Summary of reason why alert is generated. |
| **tenant**  string | Name of tenant used for all Avi API calls and context of object.  **Default:** `"admin"` |
| **tenant_ref**  string | It is a reference to an object of type tenant. |
| **tenant_uuid**  string | UUID of tenant used for all Avi API calls and context of object.  **Default:** `""` |
| **threshold**  string | An alert is created only when the number of events meets or exceeds this number within the chosen time frame.  Allowed values are 1-65536.  Default value when not specified in API or module is interpreted by Avi Controller as 1. |
| **throttle**  string | Alerts are suppressed (throttled) for this duration of time since the last alert was raised for this alert config.  Allowed values are 0-31536000.  Default value when not specified in API or module is interpreted by Avi Controller as 600. |
| **url**  string | Avi controller URL of the object. |
| **username**  string | Username used for accessing Avi controller. The default value is the environment variable `AVI_USERNAME`. |
| **uuid**  string | Unique object identifier of the object. |

## [Notes](avi_alertconfig_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage Avi Network devices see <https://www.ansible.com/ansible-avi-networks>.

## [Examples](avi_alertconfig_module.md#id5)

```yaml+jinja
- name: Example to create AlertConfig object
  community.network.avi_alertconfig:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_alertconfig
```

## [Return Values](avi_alertconfig_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **obj**  dictionary | AlertConfig (api/alertconfig) object  **Returned:** success, changed |

### Authors

- Gaurav Rastogi (@grastogi23)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
