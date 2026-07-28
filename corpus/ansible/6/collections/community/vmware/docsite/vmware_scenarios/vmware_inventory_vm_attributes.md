---
collection: ansible
version: "6"
title: "Using Virtual machine attributes in VMware dynamic inventory plugin"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/docsite/vmware_scenarios/vmware_inventory_vm_attributes.html
fetched_at: 2026-07-28T00:25:14+00:00
---
# Using Virtual machine attributes in VMware dynamic inventory plugin

- [Virtual machine attributes](vmware_inventory_vm_attributes.md#virtual-machine-attributes)

  - [capability](vmware_inventory_vm_attributes.md#capability)

    - [snapshotOperationsSupported (bool)](vmware_inventory_vm_attributes.md#snapshotoperationssupported-bool)
    - [multipleSnapshotsSupported (bool)](vmware_inventory_vm_attributes.md#multiplesnapshotssupported-bool)
    - [snapshotConfigSupported (bool)](vmware_inventory_vm_attributes.md#snapshotconfigsupported-bool)
    - [poweredOffSnapshotsSupported (bool)](vmware_inventory_vm_attributes.md#poweredoffsnapshotssupported-bool)
    - [memorySnapshotsSupported (bool)](vmware_inventory_vm_attributes.md#memorysnapshotssupported-bool)
    - [revertToSnapshotSupported (bool)](vmware_inventory_vm_attributes.md#reverttosnapshotsupported-bool)
    - [quiescedSnapshotsSupported (bool)](vmware_inventory_vm_attributes.md#quiescedsnapshotssupported-bool)
    - [disableSnapshotsSupported (bool)](vmware_inventory_vm_attributes.md#disablesnapshotssupported-bool)
    - [lockSnapshotsSupported (bool)](vmware_inventory_vm_attributes.md#locksnapshotssupported-bool)
    - [consolePreferencesSupported (bool)](vmware_inventory_vm_attributes.md#consolepreferencessupported-bool)
    - [cpuFeatureMaskSupported (bool)](vmware_inventory_vm_attributes.md#cpufeaturemasksupported-bool)
    - [s1AcpiManagementSupported (bool)](vmware_inventory_vm_attributes.md#s1acpimanagementsupported-bool)
    - [settingScreenResolutionSupported (bool)](vmware_inventory_vm_attributes.md#settingscreenresolutionsupported-bool)
    - [toolsAutoUpdateSupported (bool)](vmware_inventory_vm_attributes.md#toolsautoupdatesupported-bool)
    - [vmNpivWwnSupported (bool)](vmware_inventory_vm_attributes.md#vmnpivwwnsupported-bool)
    - [npivWwnOnNonRdmVmSupported (bool)](vmware_inventory_vm_attributes.md#npivwwnonnonrdmvmsupported-bool)
    - [vmNpivWwnDisableSupported (bool)](vmware_inventory_vm_attributes.md#vmnpivwwndisablesupported-bool)
    - [vmNpivWwnUpdateSupported (bool)](vmware_inventory_vm_attributes.md#vmnpivwwnupdatesupported-bool)
    - [swapPlacementSupported (bool)](vmware_inventory_vm_attributes.md#swapplacementsupported-bool)
    - [toolsSyncTimeSupported (bool)](vmware_inventory_vm_attributes.md#toolssynctimesupported-bool)
    - [virtualMmuUsageSupported (bool)](vmware_inventory_vm_attributes.md#virtualmmuusagesupported-bool)
    - [diskSharesSupported (bool)](vmware_inventory_vm_attributes.md#disksharessupported-bool)
    - [bootOptionsSupported (bool)](vmware_inventory_vm_attributes.md#bootoptionssupported-bool)
    - [bootRetryOptionsSupported (bool)](vmware_inventory_vm_attributes.md#bootretryoptionssupported-bool)
    - [settingVideoRamSizeSupported (bool)](vmware_inventory_vm_attributes.md#settingvideoramsizesupported-bool)
    - [settingDisplayTopologySupported (bool)](vmware_inventory_vm_attributes.md#settingdisplaytopologysupported-bool)
    - [recordReplaySupported (bool)](vmware_inventory_vm_attributes.md#recordreplaysupported-bool)
    - [changeTrackingSupported (bool)](vmware_inventory_vm_attributes.md#changetrackingsupported-bool)
    - [multipleCoresPerSocketSupported (bool)](vmware_inventory_vm_attributes.md#multiplecorespersocketsupported-bool)
    - [hostBasedReplicationSupported (bool)](vmware_inventory_vm_attributes.md#hostbasedreplicationsupported-bool)
    - [guestAutoLockSupported (bool)](vmware_inventory_vm_attributes.md#guestautolocksupported-bool)
    - [memoryReservationLockSupported (bool)](vmware_inventory_vm_attributes.md#memoryreservationlocksupported-bool)
    - [featureRequirementSupported (bool)](vmware_inventory_vm_attributes.md#featurerequirementsupported-bool)
    - [poweredOnMonitorTypeChangeSupported (bool)](vmware_inventory_vm_attributes.md#poweredonmonitortypechangesupported-bool)
    - [seSparseDiskSupported (bool)](vmware_inventory_vm_attributes.md#sesparsedisksupported-bool)
    - [nestedHVSupported (bool)](vmware_inventory_vm_attributes.md#nestedhvsupported-bool)
    - [vPMCSupported (bool)](vmware_inventory_vm_attributes.md#vpmcsupported-bool)
  - [config](vmware_inventory_vm_attributes.md#config)

    - [changeVersion (str)](vmware_inventory_vm_attributes.md#changeversion-str)
    - [modified (datetime)](vmware_inventory_vm_attributes.md#modified-datetime)
    - [name (str)](vmware_inventory_vm_attributes.md#name-str)
    - [guestFullName (str)](vmware_inventory_vm_attributes.md#guestfullname-str)
    - [version (str)](vmware_inventory_vm_attributes.md#version-str)
    - [uuid (str)](vmware_inventory_vm_attributes.md#uuid-str)
    - [instanceUuid (str, optional)](vmware_inventory_vm_attributes.md#instanceuuid-str-optional)
    - [npivNodeWorldWideName (long, optional)](vmware_inventory_vm_attributes.md#npivnodeworldwidename-long-optional)
    - [npivPortWorldWideName (long, optional)](vmware_inventory_vm_attributes.md#npivportworldwidename-long-optional)
    - [npivWorldWideNameType (str, optional)](vmware_inventory_vm_attributes.md#npivworldwidenametype-str-optional)
    - [npivDesiredNodeWwns (short, optional)](vmware_inventory_vm_attributes.md#npivdesirednodewwns-short-optional)
    - [npivDesiredPortWwns (short, optional)](vmware_inventory_vm_attributes.md#npivdesiredportwwns-short-optional)
    - [npivTemporaryDisabled (bool, optional)](vmware_inventory_vm_attributes.md#npivtemporarydisabled-bool-optional)
    - [npivOnNonRdmDisks (bool, optional)](vmware_inventory_vm_attributes.md#npivonnonrdmdisks-bool-optional)
    - [locationId (str, optional)](vmware_inventory_vm_attributes.md#locationid-str-optional)
    - [template (bool)](vmware_inventory_vm_attributes.md#template-bool)
    - [guestId (str)](vmware_inventory_vm_attributes.md#guestid-str)
    - [alternateGuestName (str)](vmware_inventory_vm_attributes.md#alternateguestname-str)
    - [annotation (str, optional)](vmware_inventory_vm_attributes.md#annotation-str-optional)
    - [files (vim.vm.FileInfo)](vmware_inventory_vm_attributes.md#files-vim-vm-fileinfo)
    - [tools (vim.vm.ToolsConfigInfo, optional)](vmware_inventory_vm_attributes.md#tools-vim-vm-toolsconfiginfo-optional)
    - [flags (vim.vm.FlagInfo)](vmware_inventory_vm_attributes.md#flags-vim-vm-flaginfo)
    - [consolePreferences (vim.vm.ConsolePreferences, optional)](vmware_inventory_vm_attributes.md#consolepreferences-vim-vm-consolepreferences-optional)
    - [defaultPowerOps (vim.vm.DefaultPowerOpInfo)](vmware_inventory_vm_attributes.md#defaultpowerops-vim-vm-defaultpoweropinfo)
    - [hardware (vim.vm.VirtualHardware)](vmware_inventory_vm_attributes.md#hardware-vim-vm-virtualhardware)
    - [cpuAllocation (vim.ResourceAllocationInfo, optional)](vmware_inventory_vm_attributes.md#cpuallocation-vim-resourceallocationinfo-optional)
    - [memoryAllocation (vim.ResourceAllocationInfo, optional)](vmware_inventory_vm_attributes.md#memoryallocation-vim-resourceallocationinfo-optional)
    - [latencySensitivity (vim.LatencySensitivity, optional)](vmware_inventory_vm_attributes.md#latencysensitivity-vim-latencysensitivity-optional)
    - [memoryHotAddEnabled (bool, optional)](vmware_inventory_vm_attributes.md#memoryhotaddenabled-bool-optional)
    - [cpuHotAddEnabled (bool, optional)](vmware_inventory_vm_attributes.md#cpuhotaddenabled-bool-optional)
    - [cpuHotRemoveEnabled (bool, optional)](vmware_inventory_vm_attributes.md#cpuhotremoveenabled-bool-optional)
    - [hotPlugMemoryLimit (long, optional)](vmware_inventory_vm_attributes.md#hotplugmemorylimit-long-optional)
    - [hotPlugMemoryIncrementSize (long, optional)](vmware_inventory_vm_attributes.md#hotplugmemoryincrementsize-long-optional)
    - [cpuAffinity (vim.vm.AffinityInfo, optional)](vmware_inventory_vm_attributes.md#cpuaffinity-vim-vm-affinityinfo-optional)
    - [memoryAffinity (vim.vm.AffinityInfo, optional)](vmware_inventory_vm_attributes.md#memoryaffinity-vim-vm-affinityinfo-optional)
    - [networkShaper (vim.vm.NetworkShaperInfo, optional)](vmware_inventory_vm_attributes.md#networkshaper-vim-vm-networkshaperinfo-optional)
    - [extraConfig (vim.option.OptionValue, optional)](vmware_inventory_vm_attributes.md#extraconfig-vim-option-optionvalue-optional)
    - [cpuFeatureMask (vim.host.CpuIdInfo, optional)](vmware_inventory_vm_attributes.md#cpufeaturemask-vim-host-cpuidinfo-optional)
    - [datastoreUrl (vim.vm.ConfigInfo.DatastoreUrlPair, optional)](vmware_inventory_vm_attributes.md#datastoreurl-vim-vm-configinfo-datastoreurlpair-optional)
    - [swapPlacement (str, optional)](vmware_inventory_vm_attributes.md#swapplacement-str-optional)
    - [bootOptions (vim.vm.BootOptions, optional)](vmware_inventory_vm_attributes.md#bootoptions-vim-vm-bootoptions-optional)
    - [ftInfo (vim.vm.FaultToleranceConfigInfo, optional)](vmware_inventory_vm_attributes.md#ftinfo-vim-vm-faulttoleranceconfiginfo-optional)
    - [vAppConfig (vim.vApp.VmConfigInfo, optional)](vmware_inventory_vm_attributes.md#vappconfig-vim-vapp-vmconfiginfo-optional)
    - [vAssertsEnabled (bool, optional)](vmware_inventory_vm_attributes.md#vassertsenabled-bool-optional)
    - [changeTrackingEnabled (bool, optional)](vmware_inventory_vm_attributes.md#changetrackingenabled-bool-optional)
    - [firmware (str, optional)](vmware_inventory_vm_attributes.md#firmware-str-optional)
    - [maxMksConnections (int, optional)](vmware_inventory_vm_attributes.md#maxmksconnections-int-optional)
    - [guestAutoLockEnabled (bool, optional)](vmware_inventory_vm_attributes.md#guestautolockenabled-bool-optional)
    - [managedBy (vim.ext.ManagedByInfo, optional)](vmware_inventory_vm_attributes.md#managedby-vim-ext-managedbyinfo-optional)
    - [memoryReservationLockedToMax (bool, optional)](vmware_inventory_vm_attributes.md#memoryreservationlockedtomax-bool-optional)
    - [initialOverhead (vim.vm.ConfigInfo.OverheadInfo), optional)](vmware_inventory_vm_attributes.md#initialoverhead-vim-vm-configinfo-overheadinfo-optional)
    - [nestedHVEnabled (bool, optional)](vmware_inventory_vm_attributes.md#nestedhvenabled-bool-optional)
    - [vPMCEnabled (bool, optional)](vmware_inventory_vm_attributes.md#vpmcenabled-bool-optional)
    - [scheduledHardwareUpgradeInfo (vim.vm.ScheduledHardwareUpgradeInfo, optional)](vmware_inventory_vm_attributes.md#scheduledhardwareupgradeinfo-vim-vm-scheduledhardwareupgradeinfo-optional)
    - [vFlashCacheReservation (long, optional)](vmware_inventory_vm_attributes.md#vflashcachereservation-long-optional)
  - [layout](vmware_inventory_vm_attributes.md#layout)

    - [configFile (str, optional)](vmware_inventory_vm_attributes.md#configfile-str-optional)
    - [logFile (str, optional)](vmware_inventory_vm_attributes.md#logfile-str-optional)
    - [disk (vim.vm.FileLayout.DiskLayout, optional)](vmware_inventory_vm_attributes.md#disk-vim-vm-filelayout-disklayout-optional)
    - [snapshot (vim.vm.FileLayout.SnapshotLayout, optional)](vmware_inventory_vm_attributes.md#snapshot-vim-vm-filelayout-snapshotlayout-optional)
    - [swapFile (str, optional)](vmware_inventory_vm_attributes.md#swapfile-str-optional)
  - [layoutEx](vmware_inventory_vm_attributes.md#layoutex)

    - [file (vim.vm.FileLayoutEx.FileInfo, optional)](vmware_inventory_vm_attributes.md#file-vim-vm-filelayoutex-fileinfo-optional)
    - [disk (vim.vm.FileLayoutEx.DiskLayout, optional)](vmware_inventory_vm_attributes.md#disk-vim-vm-filelayoutex-disklayout-optional)
    - [snapshot (vim.vm.FileLayoutEx.SnapshotLayout, optional)](vmware_inventory_vm_attributes.md#snapshot-vim-vm-filelayoutex-snapshotlayout-optional)
    - [timestamp (datetime)](vmware_inventory_vm_attributes.md#timestamp-datetime)
  - [storage (vim.vm.StorageInfo)](vmware_inventory_vm_attributes.md#storage-vim-vm-storageinfo)

    - [perDatastoreUsage (vim.vm.StorageInfo.UsageOnDatastore, optional)](vmware_inventory_vm_attributes.md#perdatastoreusage-vim-vm-storageinfo-usageondatastore-optional)
    - [timestamp (datetime)](vmware_inventory_vm_attributes.md#id1)
  - [environmentBrowser (vim.EnvironmentBrowser)](vmware_inventory_vm_attributes.md#environmentbrowser-vim-environmentbrowser)

    - [datastoreBrowser (vim.host.DatastoreBrowser)](vmware_inventory_vm_attributes.md#datastorebrowser-vim-host-datastorebrowser)
  - [resourcePool (vim.ResourcePool)](vmware_inventory_vm_attributes.md#resourcepool-vim-resourcepool)

    - [summary (vim.ResourcePool.Summary)](vmware_inventory_vm_attributes.md#summary-vim-resourcepool-summary)
    - [runtime (vim.ResourcePool.RuntimeInfo)](vmware_inventory_vm_attributes.md#runtime-vim-resourcepool-runtimeinfo)
    - [owner (vim.ComputeResource)](vmware_inventory_vm_attributes.md#owner-vim-computeresource)
    - [resourcePool (vim.ResourcePool)](vmware_inventory_vm_attributes.md#id2)
    - [vm (vim.VirtualMachine)](vmware_inventory_vm_attributes.md#vm-vim-virtualmachine)
    - [config (vim.ResourceConfigSpec)](vmware_inventory_vm_attributes.md#config-vim-resourceconfigspec)
    - [childConfiguration (vim.ResourceConfigSpec)](vmware_inventory_vm_attributes.md#childconfiguration-vim-resourceconfigspec)
  - [parentVApp (vim.ManagedEntity)](vmware_inventory_vm_attributes.md#parentvapp-vim-managedentity)

    - [parent (vim.ManagedEntity)](vmware_inventory_vm_attributes.md#parent-vim-managedentity)
    - [customValue (vim.CustomFieldsManager.Value)](vmware_inventory_vm_attributes.md#customvalue-vim-customfieldsmanager-value)
    - [overallStatus (vim.ManagedEntity.Status)](vmware_inventory_vm_attributes.md#overallstatus-vim-managedentity-status)
    - [configStatus (vim.ManagedEntity.Status)](vmware_inventory_vm_attributes.md#configstatus-vim-managedentity-status)
    - [configIssue (vim.event.Event)](vmware_inventory_vm_attributes.md#configissue-vim-event-event)
    - [effectiveRole (int)](vmware_inventory_vm_attributes.md#effectiverole-int)
    - [permission (vim.AuthorizationManager.Permission)](vmware_inventory_vm_attributes.md#permission-vim-authorizationmanager-permission)
    - [name (str)](vmware_inventory_vm_attributes.md#id3)
    - [disabledMethod (str)](vmware_inventory_vm_attributes.md#disabledmethod-str)
    - [recentTask (vim.Task)](vmware_inventory_vm_attributes.md#recenttask-vim-task)
    - [declaredAlarmState (vim.alarm.AlarmState)](vmware_inventory_vm_attributes.md#declaredalarmstate-vim-alarm-alarmstate)
    - [triggeredAlarmState (vim.alarm.AlarmState)](vmware_inventory_vm_attributes.md#triggeredalarmstate-vim-alarm-alarmstate)
    - [alarmActionsEnabled (bool)](vmware_inventory_vm_attributes.md#alarmactionsenabled-bool)
    - [tag (vim.Tag)](vmware_inventory_vm_attributes.md#tag-vim-tag)
  - [resourceConfig (vim.ResourceConfigSpec)](vmware_inventory_vm_attributes.md#resourceconfig-vim-resourceconfigspec)

    - [entity (vim.ManagedEntity, optional)](vmware_inventory_vm_attributes.md#entity-vim-managedentity-optional)
    - [changeVersion (str, optional)](vmware_inventory_vm_attributes.md#changeversion-str-optional)
    - [lastModified (datetime, optional)](vmware_inventory_vm_attributes.md#lastmodified-datetime-optional)
    - [cpuAllocation (vim.ResourceAllocationInfo)](vmware_inventory_vm_attributes.md#cpuallocation-vim-resourceallocationinfo)
    - [memoryAllocation (vim.ResourceAllocationInfo)](vmware_inventory_vm_attributes.md#memoryallocation-vim-resourceallocationinfo)
  - [runtime (vim.vm.RuntimeInfo)](vmware_inventory_vm_attributes.md#runtime-vim-vm-runtimeinfo)

    - [device (vim.vm.DeviceRuntimeInfo, optional)](vmware_inventory_vm_attributes.md#device-vim-vm-deviceruntimeinfo-optional)
    - [host (vim.HostSystem, optional)](vmware_inventory_vm_attributes.md#host-vim-hostsystem-optional)
    - [connectionState (vim.VirtualMachine.ConnectionState)](vmware_inventory_vm_attributes.md#connectionstate-vim-virtualmachine-connectionstate)
    - [powerState (vim.VirtualMachine.PowerState)](vmware_inventory_vm_attributes.md#powerstate-vim-virtualmachine-powerstate)
    - [faultToleranceState (vim.VirtualMachine.FaultToleranceState)](vmware_inventory_vm_attributes.md#faulttolerancestate-vim-virtualmachine-faulttolerancestate)
    - [dasVmProtection (vim.vm.RuntimeInfo.DasProtectionState, optional)](vmware_inventory_vm_attributes.md#dasvmprotection-vim-vm-runtimeinfo-dasprotectionstate-optional)
    - [toolsInstallerMounted (bool)](vmware_inventory_vm_attributes.md#toolsinstallermounted-bool)
    - [suspendTime (datetime, optional)](vmware_inventory_vm_attributes.md#suspendtime-datetime-optional)
    - [bootTime (datetime, optional)](vmware_inventory_vm_attributes.md#boottime-datetime-optional)
    - [suspendInterval (long, optional)](vmware_inventory_vm_attributes.md#suspendinterval-long-optional)
    - [question (vim.vm.QuestionInfo, optional)](vmware_inventory_vm_attributes.md#question-vim-vm-questioninfo-optional)
    - [memoryOverhead (long, optional)](vmware_inventory_vm_attributes.md#memoryoverhead-long-optional)
    - [maxCpuUsage (int, optional)](vmware_inventory_vm_attributes.md#maxcpuusage-int-optional)
    - [maxMemoryUsage (int, optional)](vmware_inventory_vm_attributes.md#maxmemoryusage-int-optional)
    - [numMksConnections (int)](vmware_inventory_vm_attributes.md#nummksconnections-int)
    - [recordReplayState (vim.VirtualMachine.RecordReplayState)](vmware_inventory_vm_attributes.md#recordreplaystate-vim-virtualmachine-recordreplaystate)
    - [cleanPowerOff (bool, optional)](vmware_inventory_vm_attributes.md#cleanpoweroff-bool-optional)
    - [needSecondaryReason (str, optional)](vmware_inventory_vm_attributes.md#needsecondaryreason-str-optional)
    - [onlineStandby (bool)](vmware_inventory_vm_attributes.md#onlinestandby-bool)
    - [minRequiredEVCModeKey (str, optional)](vmware_inventory_vm_attributes.md#minrequiredevcmodekey-str-optional)
    - [consolidationNeeded (bool)](vmware_inventory_vm_attributes.md#consolidationneeded-bool)
    - [offlineFeatureRequirement (vim.vm.FeatureRequirement, optional)](vmware_inventory_vm_attributes.md#offlinefeaturerequirement-vim-vm-featurerequirement-optional)
    - [featureRequirement (vim.vm.FeatureRequirement, optional)](vmware_inventory_vm_attributes.md#featurerequirement-vim-vm-featurerequirement-optional)
    - [featureMask (vim.host.FeatureMask, optional)](vmware_inventory_vm_attributes.md#featuremask-vim-host-featuremask-optional)
    - [vFlashCacheAllocation (long, optional)](vmware_inventory_vm_attributes.md#vflashcacheallocation-long-optional)
  - [guest (vim.vm.GuestInfo)](vmware_inventory_vm_attributes.md#guest-vim-vm-guestinfo)

    - [toolsStatus (vim.vm.GuestInfo.ToolsStatus, optional)](vmware_inventory_vm_attributes.md#toolsstatus-vim-vm-guestinfo-toolsstatus-optional)
    - [toolsVersionStatus (str, optional)](vmware_inventory_vm_attributes.md#toolsversionstatus-str-optional)
    - [toolsVersionStatus2 (str, optional)](vmware_inventory_vm_attributes.md#toolsversionstatus2-str-optional)
    - [toolsRunningStatus (str, optional)](vmware_inventory_vm_attributes.md#toolsrunningstatus-str-optional)
    - [toolsVersion (str, optional)](vmware_inventory_vm_attributes.md#toolsversion-str-optional)
    - [guestId (str, optional)](vmware_inventory_vm_attributes.md#guestid-str-optional)
    - [guestFamily (str, optional)](vmware_inventory_vm_attributes.md#guestfamily-str-optional)
    - [guestFullName (str, optional)](vmware_inventory_vm_attributes.md#guestfullname-str-optional)
    - [hostName (str, optional)](vmware_inventory_vm_attributes.md#hostname-str-optional)
    - [ipAddress (str, optional)](vmware_inventory_vm_attributes.md#ipaddress-str-optional)
    - [net (vim.vm.GuestInfo.NicInfo, optional)](vmware_inventory_vm_attributes.md#net-vim-vm-guestinfo-nicinfo-optional)
    - [ipStack (vim.vm.GuestInfo.StackInfo, optional)](vmware_inventory_vm_attributes.md#ipstack-vim-vm-guestinfo-stackinfo-optional)
    - [disk (vim.vm.GuestInfo.DiskInfo, optional)](vmware_inventory_vm_attributes.md#disk-vim-vm-guestinfo-diskinfo-optional)
    - [screen (vim.vm.GuestInfo.ScreenInfo, optional)](vmware_inventory_vm_attributes.md#screen-vim-vm-guestinfo-screeninfo-optional)
    - [guestState (str)](vmware_inventory_vm_attributes.md#gueststate-str)
    - [appHeartbeatStatus (str, optional)](vmware_inventory_vm_attributes.md#appheartbeatstatus-str-optional)
    - [appState (str, optional)](vmware_inventory_vm_attributes.md#appstate-str-optional)
    - [guestOperationsReady (bool, optional)](vmware_inventory_vm_attributes.md#guestoperationsready-bool-optional)
    - [interactiveGuestOperationsReady (bool, optional)](vmware_inventory_vm_attributes.md#interactiveguestoperationsready-bool-optional)
    - [generationInfo (vim.vm.GuestInfo.NamespaceGenerationInfo, privilege: VirtualMachine.Namespace.EventNotify, optional)](vmware_inventory_vm_attributes.md#generationinfo-vim-vm-guestinfo-namespacegenerationinfo-privilege-virtualmachine-namespace-eventnotify-optional)
  - [summary (vim.vm.Summary)](vmware_inventory_vm_attributes.md#summary-vim-vm-summary)

    - [vm (vim.VirtualMachine, optional)](vmware_inventory_vm_attributes.md#vm-vim-virtualmachine-optional)
    - [runtime (vim.vm.RuntimeInfo)](vmware_inventory_vm_attributes.md#id4)
    - [guest (vim.vm.Summary.GuestSummary, optional)](vmware_inventory_vm_attributes.md#guest-vim-vm-summary-guestsummary-optional)
    - [config (vim.vm.Summary.ConfigSummary)](vmware_inventory_vm_attributes.md#config-vim-vm-summary-configsummary)
    - [storage (vim.vm.Summary.StorageSummary, optional)](vmware_inventory_vm_attributes.md#storage-vim-vm-summary-storagesummary-optional)
    - [quickStats (vim.vm.Summary.QuickStats)](vmware_inventory_vm_attributes.md#quickstats-vim-vm-summary-quickstats)
    - [overallStatus (vim.ManagedEntity.Status)](vmware_inventory_vm_attributes.md#id5)
    - [customValue (vim.CustomFieldsManager.Value, optional)](vmware_inventory_vm_attributes.md#customvalue-vim-customfieldsmanager-value-optional)
  - [datastore (vim.Datastore)](vmware_inventory_vm_attributes.md#datastore-vim-datastore)

    - [info (vim.Datastore.Info)](vmware_inventory_vm_attributes.md#info-vim-datastore-info)
    - [summary (vim.Datastore.Summary)](vmware_inventory_vm_attributes.md#summary-vim-datastore-summary)
    - [host (vim.Datastore.HostMount)](vmware_inventory_vm_attributes.md#host-vim-datastore-hostmount)
    - [vm (vim.VirtualMachine)](vmware_inventory_vm_attributes.md#id6)
    - [browser (vim.host.DatastoreBrowser)](vmware_inventory_vm_attributes.md#browser-vim-host-datastorebrowser)
    - [capability (vim.Datastore.Capability)](vmware_inventory_vm_attributes.md#capability-vim-datastore-capability)
    - [iormConfiguration (vim.StorageResourceManager.IORMConfigInfo)](vmware_inventory_vm_attributes.md#iormconfiguration-vim-storageresourcemanager-iormconfiginfo)
  - [network (vim.Network)](vmware_inventory_vm_attributes.md#network-vim-network)

    - [name (str)](vmware_inventory_vm_attributes.md#id7)
    - [summary (vim.Network.Summary)](vmware_inventory_vm_attributes.md#summary-vim-network-summary)
    - [host (vim.HostSystem)](vmware_inventory_vm_attributes.md#host-vim-hostsystem)
    - [vm (vim.VirtualMachine)](vmware_inventory_vm_attributes.md#id8)
  - [snapshot (vim.vm.SnapshotInfo)](vmware_inventory_vm_attributes.md#snapshot-vim-vm-snapshotinfo)

    - [currentSnapshot (vim.vm.Snapshot, optional)](vmware_inventory_vm_attributes.md#currentsnapshot-vim-vm-snapshot-optional)
    - [rootSnapshotList (vim.vm.SnapshotTree)](vmware_inventory_vm_attributes.md#rootsnapshotlist-vim-vm-snapshottree)
  - [rootSnapshot (vim.vm.Snapshot)](vmware_inventory_vm_attributes.md#rootsnapshot-vim-vm-snapshot)

    - [config (vim.vm.ConfigInfo)](vmware_inventory_vm_attributes.md#config-vim-vm-configinfo)
    - [childSnapshot (vim.vm.Snapshot)](vmware_inventory_vm_attributes.md#childsnapshot-vim-vm-snapshot)
  - [guestHeartbeatStatus (vim.ManagedEntity.Status)](vmware_inventory_vm_attributes.md#guestheartbeatstatus-vim-managedentity-status)

## [Virtual machine attributes](vmware_inventory_vm_attributes.md#id9)

You can use virtual machine properties which can be used to populate `hostvars` for the given
virtual machine in a VMware dynamic inventory plugin.

### [capability](vmware_inventory_vm_attributes.md#id10)

This section describes settings for the runtime capabilities of the virtual machine.

#### [snapshotOperationsSupported (bool)](vmware_inventory_vm_attributes.md#id11)

> Indicates whether or not a virtual machine supports snapshot operations.

#### [multipleSnapshotsSupported (bool)](vmware_inventory_vm_attributes.md#id12)

> Indicates whether or not a virtual machine supports multiple snapshots.
> This value is not set when the virtual machine is unavailable, for instance, when it is being created or deleted.

#### [snapshotConfigSupported (bool)](vmware_inventory_vm_attributes.md#id13)

> Indicates whether or not a virtual machine supports snapshot config.

#### [poweredOffSnapshotsSupported (bool)](vmware_inventory_vm_attributes.md#id14)

> Indicates whether or not a virtual machine supports snapshot operations in `poweredOff` state.

#### [memorySnapshotsSupported (bool)](vmware_inventory_vm_attributes.md#id15)

> Indicates whether or not a virtual machine supports memory snapshots.

#### [revertToSnapshotSupported (bool)](vmware_inventory_vm_attributes.md#id16)

> Indicates whether or not a virtual machine supports reverting to a snapshot.

#### [quiescedSnapshotsSupported (bool)](vmware_inventory_vm_attributes.md#id17)

> Indicates whether or not a virtual machine supports quiesced snapshots.

#### [disableSnapshotsSupported (bool)](vmware_inventory_vm_attributes.md#id18)

> Indicates whether or not snapshots can be disabled.

#### [lockSnapshotsSupported (bool)](vmware_inventory_vm_attributes.md#id19)

> Indicates whether or not the snapshot tree can be locked.

#### [consolePreferencesSupported (bool)](vmware_inventory_vm_attributes.md#id20)

> Indicates whether console preferences can be set for the virtual machine.

#### [cpuFeatureMaskSupported (bool)](vmware_inventory_vm_attributes.md#id21)

> Indicates whether CPU feature requirements masks can be set for the virtual machine.

#### [s1AcpiManagementSupported (bool)](vmware_inventory_vm_attributes.md#id22)

> Indicates whether or not a virtual machine supports ACPI S1 settings management.

#### [settingScreenResolutionSupported (bool)](vmware_inventory_vm_attributes.md#id23)

> Indicates whether or not the virtual machine supports setting the screen resolution of the console window.

#### [toolsAutoUpdateSupported (bool)](vmware_inventory_vm_attributes.md#id24)

> Supports tools auto-update.

#### [vmNpivWwnSupported (bool)](vmware_inventory_vm_attributes.md#id25)

> Supports virtual machine NPIV WWN.

#### [npivWwnOnNonRdmVmSupported (bool)](vmware_inventory_vm_attributes.md#id26)

> Supports assigning NPIV WWN to virtual machines that do not have RDM disks.

#### [vmNpivWwnDisableSupported (bool)](vmware_inventory_vm_attributes.md#id27)

> Indicates whether the NPIV disabling operation is supported on the virtual machine.

#### [vmNpivWwnUpdateSupported (bool)](vmware_inventory_vm_attributes.md#id28)

> Indicates whether the update of NPIV WWNs are supported on the virtual machine.

#### [swapPlacementSupported (bool)](vmware_inventory_vm_attributes.md#id29)

> Flag indicating whether the virtual machine has a configurable (swapfile placement policy).

#### [toolsSyncTimeSupported (bool)](vmware_inventory_vm_attributes.md#id30)

> Indicates whether asking tools to sync time with the host is supported.

#### [virtualMmuUsageSupported (bool)](vmware_inventory_vm_attributes.md#id31)

> Indicates whether or not the use of nested page table hardware support can be explicitly set.

#### [diskSharesSupported (bool)](vmware_inventory_vm_attributes.md#id32)

> Indicates whether resource settings for disks can be applied to the virtual machine.

#### [bootOptionsSupported (bool)](vmware_inventory_vm_attributes.md#id33)

> Indicates whether boot options can be configured for the virtual machine.

#### [bootRetryOptionsSupported (bool)](vmware_inventory_vm_attributes.md#id34)

> Indicates whether automatic boot retry can be configured for the virtual machine.

#### [settingVideoRamSizeSupported (bool)](vmware_inventory_vm_attributes.md#id35)

> Flag indicating whether the video RAM size of the virtual machine can be configured.

#### [settingDisplayTopologySupported (bool)](vmware_inventory_vm_attributes.md#id36)

> Indicates whether or not the virtual machine supports setting the display topology of the console window.

#### [recordReplaySupported (bool)](vmware_inventory_vm_attributes.md#id37)

> Indicates whether record and replay functionality is supported on the virtual machine.

#### [changeTrackingSupported (bool)](vmware_inventory_vm_attributes.md#id38)

> Indicates that change tracking is supported for virtual disks of the virtual machine.
> However, even if change tracking is supported, it might not be available for all disks of the virtual machine.
> For example, passthru raw disk mappings or disks backed by any Ver1BackingInfo cannot be tracked.

#### [multipleCoresPerSocketSupported (bool)](vmware_inventory_vm_attributes.md#id39)

> Indicates whether multiple virtual cores per socket is supported on the virtual machine.

#### [hostBasedReplicationSupported (bool)](vmware_inventory_vm_attributes.md#id40)

> Indicates that host based replication is supported on the virtual machine.
> However, even if host based replication is supported, it might not be available for all disk types.
> For example, passthru raw disk mappings can not be replicated.

#### [guestAutoLockSupported (bool)](vmware_inventory_vm_attributes.md#id41)

> Indicates whether or not guest autolock is supported on the virtual machine.

#### [memoryReservationLockSupported (bool)](vmware_inventory_vm_attributes.md#id42)

> Indicates whether [memoryReservationLockedToMax (bool, optional)](https://docs.ansible.com/ansible/5/scenario_guides/vmware_scenarios/vmware_inventory_vm_attributes.html#memory-reservation-locked-to-max "(in Ansible v5)") may be set to true for the virtual machine.

#### [featureRequirementSupported (bool)](vmware_inventory_vm_attributes.md#id43)

> Indicates whether the featureRequirement feature is supported.

#### [poweredOnMonitorTypeChangeSupported (bool)](vmware_inventory_vm_attributes.md#id44)

> Indicates whether a monitor type change is supported while the virtual machine is in the `poweredOn` state.

#### [seSparseDiskSupported (bool)](vmware_inventory_vm_attributes.md#id45)

> Indicates whether the virtual machine supports the Flex-SE (space-efficent, sparse) format for virtual disks.

#### [nestedHVSupported (bool)](vmware_inventory_vm_attributes.md#id46)

> Indicates whether the virtual machine supports nested hardware-assisted virtualization.

#### [vPMCSupported (bool)](vmware_inventory_vm_attributes.md#id47)

> Indicates whether the virtual machine supports virtualized CPU performance counters.

### [config](vmware_inventory_vm_attributes.md#id48)

This section describes the configuration settings of the virtual machine, including the name and UUID.
This property is set when a virtual machine is created or when the `reconfigVM` method is called.
The virtual machine configuration is not guaranteed to be available.
For example, the configuration information would be unavailable if the server is unable to access the virtual machine files on disk, and is often also unavailable during the initial phases of virtual machine creation.

#### [changeVersion (str)](vmware_inventory_vm_attributes.md#id49)

> The changeVersion is a unique identifier for a given version of the configuration.
> Each change to the configuration updates this value. This is typically implemented as an ever increasing count or a time-stamp.
> However, a client should always treat this as an opaque string.

#### [modified (datetime)](vmware_inventory_vm_attributes.md#id50)

> Last time a virtual machine’s configuration was modified.

#### [name (str)](vmware_inventory_vm_attributes.md#id51)

> Display name of the virtual machine. Any / (slash), (backslash), character used in this name element is escaped. Similarly, any % (percent) character used in this name element is escaped, unless it is used to start an escape sequence. A slash is escaped as %2F or %2f. A backslash is escaped as %5C or %5c, and a percent is escaped as %25.

#### [guestFullName (str)](vmware_inventory_vm_attributes.md#id52)

> This is the full name of the guest operating system for the virtual machine. For example: Windows 2000 Professional. See [alternateGuestName (str)](https://docs.ansible.com/ansible/5/scenario_guides/vmware_scenarios/vmware_inventory_vm_attributes.html#alternate-guest-name "(in Ansible v5)").

#### [version (str)](vmware_inventory_vm_attributes.md#id53)

> The version string for the virtual machine.

#### [uuid (str)](vmware_inventory_vm_attributes.md#id54)

> 128-bit SMBIOS UUID of a virtual machine represented as a hexadecimal string in “12345678-abcd-1234-cdef-123456789abc” format.

#### [instanceUuid (str, optional)](vmware_inventory_vm_attributes.md#id55)

> VirtualCenter-specific 128-bit UUID of a virtual machine, represented as a hexademical string. This identifier is used by VirtualCenter to uniquely identify all virtual machine instances, including those that may share the same SMBIOS UUID.

#### [npivNodeWorldWideName (long, optional)](vmware_inventory_vm_attributes.md#id56)

> A 64-bit node WWN (World Wide Name).

#### [npivPortWorldWideName (long, optional)](vmware_inventory_vm_attributes.md#id57)

> A 64-bit port WWN (World Wide Name).

#### [npivWorldWideNameType (str, optional)](vmware_inventory_vm_attributes.md#id58)

> The source that provides/generates the assigned WWNs.

#### [npivDesiredNodeWwns (short, optional)](vmware_inventory_vm_attributes.md#id59)

> The NPIV node WWNs to be extended from the original list of WWN numbers.

#### [npivDesiredPortWwns (short, optional)](vmware_inventory_vm_attributes.md#id60)

> The NPIV port WWNs to be extended from the original list of WWN numbers.

#### [npivTemporaryDisabled (bool, optional)](vmware_inventory_vm_attributes.md#id61)

> This property is used to enable or disable the NPIV capability on a desired virtual machine on a temporary basis.

#### [npivOnNonRdmDisks (bool, optional)](vmware_inventory_vm_attributes.md#id62)

> This property is used to check whether the NPIV can be enabled on the Virtual machine with non-rdm disks in the configuration, so this is potentially not enabling npiv on vmfs disks.
> Also this property is used to check whether RDM is required to generate WWNs for a virtual machine.

#### [locationId (str, optional)](vmware_inventory_vm_attributes.md#id63)

> Hash incorporating the virtual machine’s config file location and the UUID of the host assigned to run the virtual machine.

#### [template (bool)](vmware_inventory_vm_attributes.md#id64)

> Flag indicating whether or not a virtual machine is a template.

#### [guestId (str)](vmware_inventory_vm_attributes.md#id65)

> Guest operating system configured on a virtual machine.

#### [alternateGuestName (str)](vmware_inventory_vm_attributes.md#id66)

> Used as display name for the operating system if guestId isotherorother-64. See [guestFullName (str)](https://docs.ansible.com/ansible/5/scenario_guides/vmware_scenarios/vmware_inventory_vm_attributes.html#guest-full-name "(in Ansible v5)").

#### [annotation (str, optional)](vmware_inventory_vm_attributes.md#id67)

> Description for the virtual machine.

#### [files (vim.vm.FileInfo)](vmware_inventory_vm_attributes.md#id68)

> Information about the files associated with a virtual machine.
> This information does not include files for specific virtual disks or snapshots.

#### [tools (vim.vm.ToolsConfigInfo, optional)](vmware_inventory_vm_attributes.md#id69)

> Configuration of VMware Tools running in the guest operating system.

#### [flags (vim.vm.FlagInfo)](vmware_inventory_vm_attributes.md#id70)

> Additional flags for a virtual machine.

#### [consolePreferences (vim.vm.ConsolePreferences, optional)](vmware_inventory_vm_attributes.md#id71)

> Legacy console viewer preferences when doing power operations.

#### [defaultPowerOps (vim.vm.DefaultPowerOpInfo)](vmware_inventory_vm_attributes.md#id72)

> Configuration of default power operations.

#### [hardware (vim.vm.VirtualHardware)](vmware_inventory_vm_attributes.md#id73)

> Processor, memory, and virtual devices for a virtual machine.

#### [cpuAllocation (vim.ResourceAllocationInfo, optional)](vmware_inventory_vm_attributes.md#id74)

> Resource limits for CPU.

#### [memoryAllocation (vim.ResourceAllocationInfo, optional)](vmware_inventory_vm_attributes.md#id75)

> Resource limits for memory.

#### [latencySensitivity (vim.LatencySensitivity, optional)](vmware_inventory_vm_attributes.md#id76)

> The latency-sensitivity of the virtual machine.

#### [memoryHotAddEnabled (bool, optional)](vmware_inventory_vm_attributes.md#id77)

> Whether memory can be added while the virtual machine is running.

#### [cpuHotAddEnabled (bool, optional)](vmware_inventory_vm_attributes.md#id78)

> Whether virtual processors can be added while the virtual machine is running.

#### [cpuHotRemoveEnabled (bool, optional)](vmware_inventory_vm_attributes.md#id79)

> Whether virtual processors can be removed while the virtual machine is running.

#### [hotPlugMemoryLimit (long, optional)](vmware_inventory_vm_attributes.md#id80)

> The maximum amount of memory, in MB, than can be added to a running virtual machine.

#### [hotPlugMemoryIncrementSize (long, optional)](vmware_inventory_vm_attributes.md#id81)

> Memory, in MB that can be added to a running virtual machine.

#### [cpuAffinity (vim.vm.AffinityInfo, optional)](vmware_inventory_vm_attributes.md#id82)

> Affinity settings for CPU.

#### [memoryAffinity (vim.vm.AffinityInfo, optional)](vmware_inventory_vm_attributes.md#id83)

> Affinity settings for memory.

#### [networkShaper (vim.vm.NetworkShaperInfo, optional)](vmware_inventory_vm_attributes.md#id84)

> Resource limits for network.

#### [extraConfig (vim.option.OptionValue, optional)](vmware_inventory_vm_attributes.md#id85)

> Additional configuration information for the virtual machine.

#### [cpuFeatureMask (vim.host.CpuIdInfo, optional)](vmware_inventory_vm_attributes.md#id86)

> Specifies CPU feature compatibility masks that override the defaults from the `GuestOsDescriptor` of the virtual machine’s guest OS.

#### [datastoreUrl (vim.vm.ConfigInfo.DatastoreUrlPair, optional)](vmware_inventory_vm_attributes.md#id87)

> Enumerates the set of datastores that the virtual machine is stored on, as well as the URL identification for each of these.

#### [swapPlacement (str, optional)](vmware_inventory_vm_attributes.md#id88)

> Virtual machine swapfile placement policy.

#### [bootOptions (vim.vm.BootOptions, optional)](vmware_inventory_vm_attributes.md#id89)

> Configuration options for the boot behavior of the virtual machine.

#### [ftInfo (vim.vm.FaultToleranceConfigInfo, optional)](vmware_inventory_vm_attributes.md#id90)

> Fault tolerance settings for the virtual machine.

#### [vAppConfig (vim.vApp.VmConfigInfo, optional)](vmware_inventory_vm_attributes.md#id91)

> vApp meta-data for the virtual machine.

#### [vAssertsEnabled (bool, optional)](vmware_inventory_vm_attributes.md#id92)

> Indicates whether user-configured virtual asserts will be triggered during virtual machine replay.

#### [changeTrackingEnabled (bool, optional)](vmware_inventory_vm_attributes.md#id93)

> Indicates whether changed block tracking for the virtual machine’s disks is active.

#### [firmware (str, optional)](vmware_inventory_vm_attributes.md#id94)

> Information about firmware type for the virtual machine.

#### [maxMksConnections (int, optional)](vmware_inventory_vm_attributes.md#id95)

> Indicates the maximum number of active remote display connections that the virtual machine will support.

#### [guestAutoLockEnabled (bool, optional)](vmware_inventory_vm_attributes.md#id96)

> Indicates whether the guest operating system will logout any active sessions whenever there are no remote display connections open to the virtual machine.

#### [managedBy (vim.ext.ManagedByInfo, optional)](vmware_inventory_vm_attributes.md#id97)

> Specifies that the virtual machine is managed by a VC Extension.

#### [memoryReservationLockedToMax (bool, optional)](vmware_inventory_vm_attributes.md#id98)

> If set true, memory resource reservation for the virtual machine will always be equal to the virtual machine’s memory size; increases in memory size will be rejected when a corresponding reservation increase is not possible.

#### [initialOverhead (vim.vm.ConfigInfo.OverheadInfo), optional)](vmware_inventory_vm_attributes.md#id99)

> Set of values to be used only to perform admission control when determining if a host has sufficient resources for the virtual machine to power on.

#### [nestedHVEnabled (bool, optional)](vmware_inventory_vm_attributes.md#id100)

> Indicates whether the virtual machine is configured to use nested hardware-assisted virtualization.

#### [vPMCEnabled (bool, optional)](vmware_inventory_vm_attributes.md#id101)

> Indicates whether the virtual machine have virtual CPU performance counters enabled.

#### [scheduledHardwareUpgradeInfo (vim.vm.ScheduledHardwareUpgradeInfo, optional)](vmware_inventory_vm_attributes.md#id102)

> Configuration of scheduled hardware upgrades and result from last attempt to run scheduled hardware upgrade.

#### [vFlashCacheReservation (long, optional)](vmware_inventory_vm_attributes.md#id103)

> Specifies the total vFlash resource reservation for the vFlash caches associated with the virtual machine’s virtual disks, in bytes.

### [layout](vmware_inventory_vm_attributes.md#id104)

Detailed information about the files that comprise the virtual machine.

#### [configFile (str, optional)](vmware_inventory_vm_attributes.md#id105)

> A list of files that makes up the configuration of the virtual machine (excluding the .vmx file, since that file is represented in the FileInfo).
> These are relative paths from the configuration directory.
> A slash is always used as a separator.
> This list will typically include the NVRAM file, but could also include other meta-data files.

#### [logFile (str, optional)](vmware_inventory_vm_attributes.md#id106)

> A list of files stored in the virtual machine’s log directory.
> These are relative paths from the `logDirectory`.
> A slash is always used as a separator.

#### [disk (vim.vm.FileLayout.DiskLayout, optional)](vmware_inventory_vm_attributes.md#id107)

> Files making up each virtual disk.

#### [snapshot (vim.vm.FileLayout.SnapshotLayout, optional)](vmware_inventory_vm_attributes.md#id108)

> Files of each snapshot.

#### [swapFile (str, optional)](vmware_inventory_vm_attributes.md#id109)

> The swapfile specific to the virtual machine, if any. This is a complete datastore path, not a relative path.

### [layoutEx](vmware_inventory_vm_attributes.md#id110)

Detailed information about the files that comprise the virtual machine.

#### [file (vim.vm.FileLayoutEx.FileInfo, optional)](vmware_inventory_vm_attributes.md#id111)

> Information about all the files that constitute the virtual machine including configuration files, disks, swap file, suspend file, log files, core files, memory file and so on.

#### [disk (vim.vm.FileLayoutEx.DiskLayout, optional)](vmware_inventory_vm_attributes.md#id112)

> Layout of each virtual disk attached to the virtual machine.
> For a virtual machine with snaphots, this property gives only those disks that are attached to it at the current point of running.

#### [snapshot (vim.vm.FileLayoutEx.SnapshotLayout, optional)](vmware_inventory_vm_attributes.md#id113)

> Layout of each snapshot of the virtual machine.

#### [timestamp (datetime)](vmware_inventory_vm_attributes.md#id114)

> Time when values in this structure were last updated.

### [storage (vim.vm.StorageInfo)](vmware_inventory_vm_attributes.md#id115)

Storage space used by the virtual machine, split by datastore.

#### [perDatastoreUsage (vim.vm.StorageInfo.UsageOnDatastore, optional)](vmware_inventory_vm_attributes.md#id116)

> Storage space used by the virtual machine on all datastores that it is located on.
> Total storage space committed to the virtual machine across all datastores is simply an aggregate of the property `committed`

#### [timestamp (datetime)](vmware_inventory_vm_attributes.md#id117)

> Time when values in this structure were last updated.

### [environmentBrowser (vim.EnvironmentBrowser)](vmware_inventory_vm_attributes.md#id118)

The current virtual machine’s environment browser object.
This contains information on all the configurations that can be used on the virtual machine.
This is identical to the environment browser on the ComputeResource to which the virtual machine belongs.

#### [datastoreBrowser (vim.host.DatastoreBrowser)](vmware_inventory_vm_attributes.md#id119)

> DatastoreBrowser to browse datastores that are available on this entity.

### [resourcePool (vim.ResourcePool)](vmware_inventory_vm_attributes.md#id120)

The current resource pool that specifies resource allocation for the virtual machine.
This property is set when a virtual machine is created or associated with a different resource pool.
Returns null if the virtual machine is a template or the session has no access to the resource pool.

#### [summary (vim.ResourcePool.Summary)](vmware_inventory_vm_attributes.md#id121)

> Basic information about a resource pool.

#### [runtime (vim.ResourcePool.RuntimeInfo)](vmware_inventory_vm_attributes.md#id122)

> Runtime information about a resource pool.

#### [owner (vim.ComputeResource)](vmware_inventory_vm_attributes.md#id123)

> The ComputeResource to which this set of one or more nested resource pools belong.

#### [resourcePool (vim.ResourcePool)](vmware_inventory_vm_attributes.md#id124)

> The set of child resource pools.

#### [vm (vim.VirtualMachine)](vmware_inventory_vm_attributes.md#id125)

> The set of virtual machines associated with this resource pool.

#### [config (vim.ResourceConfigSpec)](vmware_inventory_vm_attributes.md#id126)

> Configuration of this resource pool.

#### [childConfiguration (vim.ResourceConfigSpec)](vmware_inventory_vm_attributes.md#id127)

> The resource configuration of all direct children (VirtualMachine and ResourcePool) of this resource group.

### [parentVApp (vim.ManagedEntity)](vmware_inventory_vm_attributes.md#id128)

Reference to the parent vApp.

#### [parent (vim.ManagedEntity)](vmware_inventory_vm_attributes.md#id129)

> Parent of this entity.
> This value is null for the root object and for (VirtualMachine) objects that are part of a (VirtualApp).

#### [customValue (vim.CustomFieldsManager.Value)](vmware_inventory_vm_attributes.md#id130)

> Custom field values.

#### [overallStatus (vim.ManagedEntity.Status)](vmware_inventory_vm_attributes.md#id131)

> General health of this managed entity.

#### [configStatus (vim.ManagedEntity.Status)](vmware_inventory_vm_attributes.md#id132)

> The configStatus indicates whether or not the system has detected a configuration issue involving this entity.
> For example, it might have detected a duplicate IP address or MAC address, or a host in a cluster might be out of `compliance.property`.

#### [configIssue (vim.event.Event)](vmware_inventory_vm_attributes.md#id133)

> Current configuration issues that have been detected for this entity.

#### [effectiveRole (int)](vmware_inventory_vm_attributes.md#id134)

> Access rights the current session has to this entity.

#### [permission (vim.AuthorizationManager.Permission)](vmware_inventory_vm_attributes.md#id135)

> List of permissions defined for this entity.

#### [name (str)](vmware_inventory_vm_attributes.md#id136)

> Name of this entity, unique relative to its parent.
> Any / (slash), (backslash), character used in this name element will be escaped.
> Similarly, any % (percent) character used in this name element will be escaped, unless it is used to start an escape sequence.
> A slash is escaped as %2F or %2f. A backslash is escaped as %5C or %5c, and a percent is escaped as %25.

#### [disabledMethod (str)](vmware_inventory_vm_attributes.md#id137)

> List of operations that are disabled, given the current runtime state of the entity.
> For example, a power-on operation always fails if a virtual machine is already powered on.

#### [recentTask (vim.Task)](vmware_inventory_vm_attributes.md#id138)

> The set of recent tasks operating on this managed entity.
> A task in this list could be in one of the four states: pending, running, success or error.

#### [declaredAlarmState (vim.alarm.AlarmState)](vmware_inventory_vm_attributes.md#id139)

> A set of alarm states for alarms that apply to this managed entity.

#### [triggeredAlarmState (vim.alarm.AlarmState)](vmware_inventory_vm_attributes.md#id140)

> A set of alarm states for alarms triggered by this entity or by its descendants.

#### [alarmActionsEnabled (bool)](vmware_inventory_vm_attributes.md#id141)

> Whether alarm actions are enabled for this entity. True if enabled; false otherwise.

#### [tag (vim.Tag)](vmware_inventory_vm_attributes.md#id142)

> The set of tags associated with this managed entity. Experimental. Subject to change.

### [resourceConfig (vim.ResourceConfigSpec)](vmware_inventory_vm_attributes.md#id143)

> The resource configuration for a virtual machine.

#### [entity (vim.ManagedEntity, optional)](vmware_inventory_vm_attributes.md#id144)

> Reference to the entity with this resource specification: either a VirtualMachine or a ResourcePool.

#### [changeVersion (str, optional)](vmware_inventory_vm_attributes.md#id145)

> The changeVersion is a unique identifier for a given version of the configuration. Each change to the configuration will update this value.
> This is typically implemented as an ever increasing count or a time-stamp.

#### [lastModified (datetime, optional)](vmware_inventory_vm_attributes.md#id146)

> Timestamp when the resources were last modified. This is ignored when the object is used to update a configuration.

#### [cpuAllocation (vim.ResourceAllocationInfo)](vmware_inventory_vm_attributes.md#id147)

> Resource allocation for CPU.

#### [memoryAllocation (vim.ResourceAllocationInfo)](vmware_inventory_vm_attributes.md#id148)

> Resource allocation for memory.

### [runtime (vim.vm.RuntimeInfo)](vmware_inventory_vm_attributes.md#id149)

Execution state and history for the virtual machine.

#### [device (vim.vm.DeviceRuntimeInfo, optional)](vmware_inventory_vm_attributes.md#id150)

> Per-device runtime info. This array will be empty if the host software does not provide runtime info for any of the device types currently in use by the virtual machine.

#### [host (vim.HostSystem, optional)](vmware_inventory_vm_attributes.md#id151)

> The host that is responsible for running a virtual machine.
> This property is null if the virtual machine is not running and is not assigned to run on a particular host.

#### [connectionState (vim.VirtualMachine.ConnectionState)](vmware_inventory_vm_attributes.md#id152)

> Indicates whether or not the virtual machine is available for management.

#### [powerState (vim.VirtualMachine.PowerState)](vmware_inventory_vm_attributes.md#id153)

> The current power state of the virtual machine.

#### [faultToleranceState (vim.VirtualMachine.FaultToleranceState)](vmware_inventory_vm_attributes.md#id154)

> The fault tolerance state of the virtual machine.

#### [dasVmProtection (vim.vm.RuntimeInfo.DasProtectionState, optional)](vmware_inventory_vm_attributes.md#id155)

> The vSphere HA protection state for a virtual machine.
> Property is unset if vSphere HA is not enabled.

#### [toolsInstallerMounted (bool)](vmware_inventory_vm_attributes.md#id156)

> Flag to indicate whether or not the VMware Tools installer is mounted as a CD-ROM.

#### [suspendTime (datetime, optional)](vmware_inventory_vm_attributes.md#id157)

> The timestamp when the virtual machine was most recently suspended.
> This property is updated every time the virtual machine is suspended.

#### [bootTime (datetime, optional)](vmware_inventory_vm_attributes.md#id158)

> The timestamp when the virtual machine was most recently powered on.
> This property is updated when the virtual machine is powered on from the poweredOff state, and is cleared when the virtual machine is powered off.
> This property is not updated when a virtual machine is resumed from a suspended state.

#### [suspendInterval (long, optional)](vmware_inventory_vm_attributes.md#id159)

> The total time the virtual machine has been suspended since it was initially powered on.
> This time excludes the current period, if the virtual machine is currently suspended.
> This property is updated when the virtual machine resumes, and is reset to zero when the virtual machine is powered off.

#### [question (vim.vm.QuestionInfo, optional)](vmware_inventory_vm_attributes.md#id160)

> The current question, if any, that is blocking the virtual machine’s execution.

#### [memoryOverhead (long, optional)](vmware_inventory_vm_attributes.md#id161)

> The amount of memory resource (in bytes) that will be used by the virtual machine above its guest memory requirements.
> This value is set if and only if the virtual machine is registered on a host that supports memory resource allocation features.
> For powered off VMs, this is the minimum overhead required to power on the VM on the registered host.
> For powered on VMs, this is the current overhead reservation, a value which is almost always larger than the minimum overhead, and which grows with time.

#### [maxCpuUsage (int, optional)](vmware_inventory_vm_attributes.md#id162)

> Current upper-bound on CPU usage.
> The upper-bound is based on the host the virtual machine is current running on, as well as limits configured on the virtual machine itself or any parent resource pool.
> Valid while the virtual machine is running.

#### [maxMemoryUsage (int, optional)](vmware_inventory_vm_attributes.md#id163)

> Current upper-bound on memory usage.
> The upper-bound is based on memory configuration of the virtual machine, as well as limits configured on the virtual machine itself or any parent resource pool.
> Valid while the virtual machine is running.

#### [numMksConnections (int)](vmware_inventory_vm_attributes.md#id164)

> Number of active MKS connections to the virtual machine.

#### [recordReplayState (vim.VirtualMachine.RecordReplayState)](vmware_inventory_vm_attributes.md#id165)

> Record / replay state of the virtual machine.

#### [cleanPowerOff (bool, optional)](vmware_inventory_vm_attributes.md#id166)

> For a powered off virtual machine, indicates whether the virtual machine’s last shutdown was an orderly power off or not.
> Unset if the virtual machine is running or suspended.

#### [needSecondaryReason (str, optional)](vmware_inventory_vm_attributes.md#id167)

> If set, indicates the reason the virtual machine needs a secondary.

#### [onlineStandby (bool)](vmware_inventory_vm_attributes.md#id168)

> This property indicates whether the guest has gone into one of the s1, s2 or s3 standby modes. False indicates the guest is awake.

#### [minRequiredEVCModeKey (str, optional)](vmware_inventory_vm_attributes.md#id169)

> For a powered-on or suspended virtual machine in a cluster with Enhanced VMotion Compatibility (EVC) enabled, this identifies the least-featured EVC mode (among those for the appropriate CPU vendor) that could admit the virtual machine.
> This property will be unset if the virtual machine is powered off or is not in an EVC cluster.
> This property may be used as a general indicator of the CPU feature baseline currently in use by the virtual machine.
> However, the virtual machine may be suppressing some of the features present in the CPU feature baseline of the indicated mode, either explicitly (in the virtual machine’s configured `cpuFeatureMask`) or implicitly (in the default masks for the `GuestOsDescriptor` appropriate for the virtual machine’s configured guest OS).

#### [consolidationNeeded (bool)](vmware_inventory_vm_attributes.md#id170)

> Whether any disk of the virtual machine requires consolidation.
> This can happen for example when a snapshot is deleted but its associated disk is not committed back to the base disk.

#### [offlineFeatureRequirement (vim.vm.FeatureRequirement, optional)](vmware_inventory_vm_attributes.md#id171)

> These requirements must have equivalent host capabilities `featureCapability` in order to power on.

#### [featureRequirement (vim.vm.FeatureRequirement, optional)](vmware_inventory_vm_attributes.md#id172)

> These requirements must have equivalent host capabilities `featureCapability` in order to power on, resume, or migrate to the host.

#### [featureMask (vim.host.FeatureMask, optional)](vmware_inventory_vm_attributes.md#id173)

> The masks applied to an individual virtual machine as a result of its configuration.

#### [vFlashCacheAllocation (long, optional)](vmware_inventory_vm_attributes.md#id174)

> Specifies the total allocated vFlash resource for the vFlash caches associated with VM’s VMDKs when VM is powered on, in bytes.

### [guest (vim.vm.GuestInfo)](vmware_inventory_vm_attributes.md#id175)

Information about VMware Tools and about the virtual machine from the perspective of VMware Tools.
Information about the guest operating system is available in VirtualCenter.
Guest operating system information reflects the last known state of the virtual machine.
For powered on machines, this is current information.
For powered off machines, this is the last recorded state before the virtual machine was powered off.

#### [toolsStatus (vim.vm.GuestInfo.ToolsStatus, optional)](vmware_inventory_vm_attributes.md#id176)

> Current status of VMware Tools in the guest operating system, if known.

#### [toolsVersionStatus (str, optional)](vmware_inventory_vm_attributes.md#id177)

> Current version status of VMware Tools in the guest operating system, if known.

#### [toolsVersionStatus2 (str, optional)](vmware_inventory_vm_attributes.md#id178)

> Current version status of VMware Tools in the guest operating system, if known.

#### [toolsRunningStatus (str, optional)](vmware_inventory_vm_attributes.md#id179)

> Current running status of VMware Tools in the guest operating system, if known.

#### [toolsVersion (str, optional)](vmware_inventory_vm_attributes.md#id180)

> Current version of VMware Tools, if known.

#### [guestId (str, optional)](vmware_inventory_vm_attributes.md#id181)

> Guest operating system identifier (short name), if known.

#### [guestFamily (str, optional)](vmware_inventory_vm_attributes.md#id182)

> Guest operating system family, if known.

#### [guestFullName (str, optional)](vmware_inventory_vm_attributes.md#id183)

> See [guestFullName (str)](https://docs.ansible.com/ansible/5/scenario_guides/vmware_scenarios/vmware_inventory_vm_attributes.html#guest-full-name "(in Ansible v5)").

#### [hostName (str, optional)](vmware_inventory_vm_attributes.md#id184)

> Hostname of the guest operating system, if known.

#### [ipAddress (str, optional)](vmware_inventory_vm_attributes.md#id185)

> Primary IP address assigned to the guest operating system, if known.

#### [net (vim.vm.GuestInfo.NicInfo, optional)](vmware_inventory_vm_attributes.md#id186)

> Guest information about network adapters, if known.

#### [ipStack (vim.vm.GuestInfo.StackInfo, optional)](vmware_inventory_vm_attributes.md#id187)

> Guest information about IP networking stack, if known.

#### [disk (vim.vm.GuestInfo.DiskInfo, optional)](vmware_inventory_vm_attributes.md#id188)

> Guest information about disks.
> You can obtain Linux guest disk information for the following file system types only: Ext2, Ext3, Ext4, ReiserFS, ZFS, NTFS, VFAT, UFS, PCFS, HFS, and MS-DOS.

#### [screen (vim.vm.GuestInfo.ScreenInfo, optional)](vmware_inventory_vm_attributes.md#id189)

> Guest screen resolution info, if known.

#### [guestState (str)](vmware_inventory_vm_attributes.md#id190)

> Operation mode of guest operating system.

#### [appHeartbeatStatus (str, optional)](vmware_inventory_vm_attributes.md#id191)

> Application heartbeat status.

#### [appState (str, optional)](vmware_inventory_vm_attributes.md#id192)

> Application state.
> If vSphere HA is enabled and the vm is configured for Application Monitoring and this field’s value is `appStateNeedReset` then HA will attempt immediately reset the virtual machine.
> There are some system conditions which may delay the immediate reset.
> The immediate reset will be performed as soon as allowed by vSphere HA and ESX.
> If during these conditions the value is changed to `appStateOk` the reset will be cancelled.

#### [guestOperationsReady (bool, optional)](vmware_inventory_vm_attributes.md#id193)

> Guest Operations availability. If true, the vitrual machine is ready to process guest operations.

#### [interactiveGuestOperationsReady (bool, optional)](vmware_inventory_vm_attributes.md#id194)

> Interactive Guest Operations availability. If true, the virtual machine is ready to process guest operations as the user interacting with the guest desktop.

#### [generationInfo (vim.vm.GuestInfo.NamespaceGenerationInfo, privilege: VirtualMachine.Namespace.EventNotify, optional)](vmware_inventory_vm_attributes.md#id195)

> A list of namespaces and their corresponding generation numbers. Only namespaces with non-zero `maxSizeEventsFromGuest` are guaranteed to be present here.

### [summary (vim.vm.Summary)](vmware_inventory_vm_attributes.md#id196)

> Basic information about the virtual machine.

#### [vm (vim.VirtualMachine, optional)](vmware_inventory_vm_attributes.md#id197)

> Reference to the virtual machine managed object.

#### [runtime (vim.vm.RuntimeInfo)](vmware_inventory_vm_attributes.md#id198)

> Runtime and state information of a running virtual machine.
> Most of this information is also available when a virtual machine is powered off.
> In that case, it contains information from the last run, if available.

#### [guest (vim.vm.Summary.GuestSummary, optional)](vmware_inventory_vm_attributes.md#id199)

> Guest operating system and VMware Tools information.

#### [config (vim.vm.Summary.ConfigSummary)](vmware_inventory_vm_attributes.md#id200)

> Basic configuration information about the virtual machine.
> This information is not available when the virtual machine is unavailable, for instance, when it is being created or deleted.

#### [storage (vim.vm.Summary.StorageSummary, optional)](vmware_inventory_vm_attributes.md#id201)

> Storage information of the virtual machine.

#### [quickStats (vim.vm.Summary.QuickStats)](vmware_inventory_vm_attributes.md#id202)

> A set of statistics that are typically updated with near real-time regularity.

#### [overallStatus (vim.ManagedEntity.Status)](vmware_inventory_vm_attributes.md#id203)

> Overall alarm status on this node.

#### [customValue (vim.CustomFieldsManager.Value, optional)](vmware_inventory_vm_attributes.md#id204)

> Custom field values.

### [datastore (vim.Datastore)](vmware_inventory_vm_attributes.md#id205)

> A collection of references to the subset of datastore objects in the datacenter that is used by the virtual machine.

#### [info (vim.Datastore.Info)](vmware_inventory_vm_attributes.md#id206)

> Specific information about the datastore.

#### [summary (vim.Datastore.Summary)](vmware_inventory_vm_attributes.md#id207)

> Global properties of the datastore.

#### [host (vim.Datastore.HostMount)](vmware_inventory_vm_attributes.md#id208)

> Hosts attached to this datastore.

#### [vm (vim.VirtualMachine)](vmware_inventory_vm_attributes.md#id209)

> Virtual machines stored on this datastore.

#### [browser (vim.host.DatastoreBrowser)](vmware_inventory_vm_attributes.md#id210)

> DatastoreBrowser used to browse this datastore.

#### [capability (vim.Datastore.Capability)](vmware_inventory_vm_attributes.md#id211)

> Capabilities of this datastore.

#### [iormConfiguration (vim.StorageResourceManager.IORMConfigInfo)](vmware_inventory_vm_attributes.md#id212)

> Configuration of storage I/O resource management for the datastore.
> Currently VMware only support storage I/O resource management on VMFS volumes of a datastore.
> This configuration may not be available if the datastore is not accessible from any host, or if the datastore does not have VMFS volume.

### [network (vim.Network)](vmware_inventory_vm_attributes.md#id213)

> A collection of references to the subset of network objects in the datacenter that is used by the virtual machine.

#### [name (str)](vmware_inventory_vm_attributes.md#id214)

> Name of this network.

#### [summary (vim.Network.Summary)](vmware_inventory_vm_attributes.md#id215)

> Properties of a network.

#### [host (vim.HostSystem)](vmware_inventory_vm_attributes.md#id216)

> Hosts attached to this network.

#### [vm (vim.VirtualMachine)](vmware_inventory_vm_attributes.md#id217)

> Virtual machines using this network.

### [snapshot (vim.vm.SnapshotInfo)](vmware_inventory_vm_attributes.md#id218)

Current snapshot and tree.
The property is valid if snapshots have been created for the virtual machine.

#### [currentSnapshot (vim.vm.Snapshot, optional)](vmware_inventory_vm_attributes.md#id219)

> Current snapshot of the virtual machineThis property is set by calling `Snapshot.revert` or `VirtualMachine.createSnapshot`.
> This property will be empty when the working snapshot is at the root of the snapshot tree.

#### [rootSnapshotList (vim.vm.SnapshotTree)](vmware_inventory_vm_attributes.md#id220)

> Data for the entire set of snapshots for one virtual machine.

### [rootSnapshot (vim.vm.Snapshot)](vmware_inventory_vm_attributes.md#id221)

The roots of all snapshot trees for the virtual machine.

#### [config (vim.vm.ConfigInfo)](vmware_inventory_vm_attributes.md#id222)

> Information about the configuration of the virtual machine when this snapshot was taken.
> The datastore paths for the virtual machine disks point to the head of the disk chain that represents the disk at this given snapshot.

#### [childSnapshot (vim.vm.Snapshot)](vmware_inventory_vm_attributes.md#id223)

> All snapshots for which this snapshot is the parent.

### [guestHeartbeatStatus (vim.ManagedEntity.Status)](vmware_inventory_vm_attributes.md#id224)

> The guest heartbeat.

> **See also:**
>
> [pyVmomi](https://github.com/vmware/pyvmomi)
> :   The GitHub Page of pyVmomi
>
> [pyVmomi Issue Tracker](https://github.com/vmware/pyvmomi/issues)
> :   The issue tracker for the pyVmomi project
>
> rst/scenario_guides/guide_vmware.rst
> :   The GitHub Page of vSphere Automation SDK for Python
>
> [vSphere Automation SDK Issue Tracker](https://github.com/vmware/vsphere-automation-sdk-python/issues)
> :   The issue tracker for vSphere Automation SDK for Python
>
> [Working with playbooks](../../../../../user_guide/playbooks.md#working-with-playbooks)
> :   An introduction to playbooks
>
> [Using encrypted variables and files](../../../../../user_guide/vault.md#playbooks-vault)
> :   Using Vault in playbooks
