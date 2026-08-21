---
collection: rook
version: "1.17.2"
title: "Specification"
source_url: https://rook.io/docs/rook/v1.17/CRDs/specification/
fetched_at: 2026-08-21T02:34:38+00:00
---
# Specification

Packages:

- [ceph.rook.io/v1](index.md#ceph.rook.io%2fv1)

## ceph.rook.io/v1

Package v1 is the v1 version of the API.

Resource Types:

- [CephBlockPool](index.md#ceph.rook.io/v1.CephBlockPool)
- [CephBucketNotification](index.md#ceph.rook.io/v1.CephBucketNotification)
- [CephBucketTopic](index.md#ceph.rook.io/v1.CephBucketTopic)
- [CephCOSIDriver](index.md#ceph.rook.io/v1.CephCOSIDriver)
- [CephClient](index.md#ceph.rook.io/v1.CephClient)
- [CephCluster](index.md#ceph.rook.io/v1.CephCluster)
- [CephFilesystem](index.md#ceph.rook.io/v1.CephFilesystem)
- [CephFilesystemMirror](index.md#ceph.rook.io/v1.CephFilesystemMirror)
- [CephFilesystemSubVolumeGroup](index.md#ceph.rook.io/v1.CephFilesystemSubVolumeGroup)
- [CephNFS](index.md#ceph.rook.io/v1.CephNFS)
- [CephObjectRealm](index.md#ceph.rook.io/v1.CephObjectRealm)
- [CephObjectStore](index.md#ceph.rook.io/v1.CephObjectStore)
- [CephObjectStoreUser](index.md#ceph.rook.io/v1.CephObjectStoreUser)
- [CephObjectZone](index.md#ceph.rook.io/v1.CephObjectZone)
- [CephObjectZoneGroup](index.md#ceph.rook.io/v1.CephObjectZoneGroup)
- [CephRBDMirror](index.md#ceph.rook.io/v1.CephRBDMirror)

### CephBlockPool

CephBlockPool represents a Ceph Storage Pool

| Field | Description |
| --- | --- |
| `apiVersion`  string | `ceph.rook.io/v1` |
| `kind`  string | `CephBlockPool` |
| `metadata`   *[Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#objectmeta-v1-meta)* | Refer to the Kubernetes API documentation for the fields of the `metadata` field. |
| `spec`   *[NamedBlockPoolSpec](index.md#ceph.rook.io/v1.NamedBlockPoolSpec)* | |  |  | | --- | --- | | `name`   *string* | *(Optional)* The desired name of the pool if different from the CephBlockPool CR name. | | `PoolSpec`   *[PoolSpec](index.md#ceph.rook.io/v1.PoolSpec)* | (Members of `PoolSpec` are embedded into this type.)  The core pool configuration | |
| `status`   *[CephBlockPoolStatus](index.md#ceph.rook.io/v1.CephBlockPoolStatus)* |  |

### CephBucketNotification

CephBucketNotification represents a Bucket Notifications

| Field | Description |
| --- | --- |
| `apiVersion`  string | `ceph.rook.io/v1` |
| `kind`  string | `CephBucketNotification` |
| `metadata`   *[Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#objectmeta-v1-meta)* | Refer to the Kubernetes API documentation for the fields of the `metadata` field. |
| `spec`   *[BucketNotificationSpec](index.md#ceph.rook.io/v1.BucketNotificationSpec)* | |  |  | | --- | --- | | `topic`   *string* | The name of the topic associated with this notification | | `events`   *[[]BucketNotificationEvent](index.md#ceph.rook.io/v1.BucketNotificationEvent)* | *(Optional)* List of events that should trigger the notification | | `filter`   *[NotificationFilterSpec](index.md#ceph.rook.io/v1.NotificationFilterSpec)* | *(Optional)* Spec of notification filter | |
| `status`   *[Status](index.md#ceph.rook.io/v1.Status)* | *(Optional)* |

### CephBucketTopic

CephBucketTopic represents a Ceph Object Topic for Bucket Notifications

| Field | Description |
| --- | --- |
| `apiVersion`  string | `ceph.rook.io/v1` |
| `kind`  string | `CephBucketTopic` |
| `metadata`   *[Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#objectmeta-v1-meta)* | Refer to the Kubernetes API documentation for the fields of the `metadata` field. |
| `spec`   *[BucketTopicSpec](index.md#ceph.rook.io/v1.BucketTopicSpec)* | |  |  | | --- | --- | | `objectStoreName`   *string* | The name of the object store on which to define the topic | | `objectStoreNamespace`   *string* | The namespace of the object store on which to define the topic | | `opaqueData`   *string* | *(Optional)* Data which is sent in each event | | `persistent`   *bool* | *(Optional)* Indication whether notifications to this endpoint are persistent or not | | `endpoint`   *[TopicEndpointSpec](index.md#ceph.rook.io/v1.TopicEndpointSpec)* | Contains the endpoint spec of the topic | |
| `status`   *[BucketTopicStatus](index.md#ceph.rook.io/v1.BucketTopicStatus)* | *(Optional)* |

### CephCOSIDriver

CephCOSIDriver represents the CRD for the Ceph COSI Driver Deployment

| Field | Description |
| --- | --- |
| `apiVersion`  string | `ceph.rook.io/v1` |
| `kind`  string | `CephCOSIDriver` |
| `metadata`   *[Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#objectmeta-v1-meta)* | Refer to the Kubernetes API documentation for the fields of the `metadata` field. |
| `spec`   *[CephCOSIDriverSpec](index.md#ceph.rook.io/v1.CephCOSIDriverSpec)* | Spec represents the specification of a Ceph COSI Driver      |  |  | | --- | --- | | `image`   *string* | *(Optional)* Image is the container image to run the Ceph COSI driver | | `objectProvisionerImage`   *string* | *(Optional)* ObjectProvisionerImage is the container image to run the COSI driver sidecar | | `deploymentStrategy`   *[COSIDeploymentStrategy](index.md#ceph.rook.io/v1.COSIDeploymentStrategy)* | *(Optional)* DeploymentStrategy is the strategy to use to deploy the COSI driver. | | `placement`   *[Placement](index.md#ceph.rook.io/v1.Placement)* | *(Optional)* Placement is the placement strategy to use for the COSI driver | | `resources`   *[Kubernetes core/v1.ResourceRequirements](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#resourcerequirements-v1-core)* | *(Optional)* Resources is the resource requirements for the COSI driver | |

### CephClient

CephClient represents a Ceph Client

| Field | Description |
| --- | --- |
| `apiVersion`  string | `ceph.rook.io/v1` |
| `kind`  string | `CephClient` |
| `metadata`   *[Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#objectmeta-v1-meta)* | Refer to the Kubernetes API documentation for the fields of the `metadata` field. |
| `spec`   *[ClientSpec](index.md#ceph.rook.io/v1.ClientSpec)* | Spec represents the specification of a Ceph Client      |  |  | | --- | --- | | `name`   *string* | *(Optional)* | | `secretName`   *string* | *(Optional)* SecretName is the name of the secret created for this ceph client. If not specified, the default name is “rook-ceph-client-” as a prefix to the CR name. | | `removeSecret`   *bool* | *(Optional)* RemoveSecret indicates whether the current secret for this ceph client should be removed or not. If true, the K8s secret will be deleted, but the cephx keyring will remain until the CR is deleted. | | `caps`   *map[string]string* |  | |
| `status`   *[CephClientStatus](index.md#ceph.rook.io/v1.CephClientStatus)* | *(Optional)* Status represents the status of a Ceph Client |

### CephCluster

CephCluster is a Ceph storage cluster

| Field | Description |
| --- | --- |
| `apiVersion`  string | `ceph.rook.io/v1` |
| `kind`  string | `CephCluster` |
| `metadata`   *[Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#objectmeta-v1-meta)* | Refer to the Kubernetes API documentation for the fields of the `metadata` field. |
| `spec`   *[ClusterSpec](index.md#ceph.rook.io/v1.ClusterSpec)* | |  |  | | --- | --- | | `cephVersion`   *[CephVersionSpec](index.md#ceph.rook.io/v1.CephVersionSpec)* | *(Optional)* The version information that instructs Rook to orchestrate a particular version of Ceph. | | `storage`   *[StorageScopeSpec](index.md#ceph.rook.io/v1.StorageScopeSpec)* | *(Optional)* A spec for available storage in the cluster and how it should be used | | `annotations`   *[AnnotationsSpec](index.md#ceph.rook.io/v1.AnnotationsSpec)* | *(Optional)* The annotations-related configuration to add/set on each Pod related object. | | `labels`   *[LabelsSpec](index.md#ceph.rook.io/v1.LabelsSpec)* | *(Optional)* The labels-related configuration to add/set on each Pod related object. | | `placement`   *[PlacementSpec](index.md#ceph.rook.io/v1.PlacementSpec)* | *(Optional)* The placement-related configuration to pass to kubernetes (affinity, node selector, tolerations). | | `network`   *[NetworkSpec](index.md#ceph.rook.io/v1.NetworkSpec)* | *(Optional)* Network related configuration | | `resources`   *[ResourceSpec](index.md#ceph.rook.io/v1.ResourceSpec)* | *(Optional)* Resources set resource requests and limits | | `priorityClassNames`   *[PriorityClassNamesSpec](index.md#ceph.rook.io/v1.PriorityClassNamesSpec)* | *(Optional)* PriorityClassNames sets priority classes on components | | `dataDirHostPath`   *string* | *(Optional)* The path on the host where config and data can be persisted | | `skipUpgradeChecks`   *bool* | *(Optional)* SkipUpgradeChecks defines if an upgrade should be forced even if one of the check fails | | `continueUpgradeAfterChecksEvenIfNotHealthy`   *bool* | *(Optional)* ContinueUpgradeAfterChecksEvenIfNotHealthy defines if an upgrade should continue even if PGs are not clean | | `waitTimeoutForHealthyOSDInMinutes`   *time.Duration* | *(Optional)* WaitTimeoutForHealthyOSDInMinutes defines the time the operator would wait before an OSD can be stopped for upgrade or restart. If the timeout exceeds and OSD is not ok to stop, then the operator would skip upgrade for the current OSD and proceed with the next one if `continueUpgradeAfterChecksEvenIfNotHealthy` is `false`. If `continueUpgradeAfterChecksEvenIfNotHealthy` is `true`, then operator would continue with the upgrade of an OSD even if its not ok to stop after the timeout. This timeout won’t be applied if `skipUpgradeChecks` is `true`. The default wait timeout is 10 minutes. | | `upgradeOSDRequiresHealthyPGs`   *bool* | *(Optional)* UpgradeOSDRequiresHealthyPGs defines if OSD upgrade requires PGs are clean. If set to `true` OSD upgrade process won’t start until PGs are healthy. This configuration will be ignored if `skipUpgradeChecks` is `true`. Default is false. | | `disruptionManagement`   *[DisruptionManagementSpec](index.md#ceph.rook.io/v1.DisruptionManagementSpec)* | *(Optional)* A spec for configuring disruption management. | | `mon`   *[MonSpec](index.md#ceph.rook.io/v1.MonSpec)* | *(Optional)* A spec for mon related options | | `crashCollector`   *[CrashCollectorSpec](index.md#ceph.rook.io/v1.CrashCollectorSpec)* | *(Optional)* A spec for the crash controller | | `dashboard`   *[DashboardSpec](index.md#ceph.rook.io/v1.DashboardSpec)* | *(Optional)* Dashboard settings | | `monitoring`   *[MonitoringSpec](index.md#ceph.rook.io/v1.MonitoringSpec)* | *(Optional)* Prometheus based Monitoring settings | | `external`   *[ExternalSpec](index.md#ceph.rook.io/v1.ExternalSpec)* | *(Optional)* Whether the Ceph Cluster is running external to this Kubernetes cluster mon, mgr, osd, mds, and discover daemons will not be created for external clusters. | | `mgr`   *[MgrSpec](index.md#ceph.rook.io/v1.MgrSpec)* | *(Optional)* A spec for mgr related options | | `removeOSDsIfOutAndSafeToRemove`   *bool* | *(Optional)* Remove the OSD that is out and safe to remove only if this option is true | | `cleanupPolicy`   *[CleanupPolicySpec](index.md#ceph.rook.io/v1.CleanupPolicySpec)* | *(Optional)* Indicates user intent when deleting a cluster; blocks orchestration and should not be set if cluster deletion is not imminent. | | `healthCheck`   *[CephClusterHealthCheckSpec](index.md#ceph.rook.io/v1.CephClusterHealthCheckSpec)* | *(Optional)* Internal daemon healthchecks and liveness probe | | `security`   *[SecuritySpec](index.md#ceph.rook.io/v1.SecuritySpec)* | *(Optional)* Security represents security settings | | `logCollector`   *[LogCollectorSpec](index.md#ceph.rook.io/v1.LogCollectorSpec)* | *(Optional)* Logging represents loggings settings | | `csi`   *[CSIDriverSpec](index.md#ceph.rook.io/v1.CSIDriverSpec)* | *(Optional)* CSI Driver Options applied per cluster. | | `cephConfig`   *map[string]map[string]string* | *(Optional)* Ceph Config options | | `cephConfigFromSecret`   *map[string]map[string]k8s.io/api/core/v1.SecretKeySelector* | *(Optional)* CephConfigFromSecret works exactly like CephConfig but takes config value from Secret Key reference. | |
| `status`   *[ClusterStatus](index.md#ceph.rook.io/v1.ClusterStatus)* | *(Optional)* |

### CephFilesystem

CephFilesystem represents a Ceph Filesystem

| Field | Description |
| --- | --- |
| `apiVersion`  string | `ceph.rook.io/v1` |
| `kind`  string | `CephFilesystem` |
| `metadata`   *[Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#objectmeta-v1-meta)* | Refer to the Kubernetes API documentation for the fields of the `metadata` field. |
| `spec`   *[FilesystemSpec](index.md#ceph.rook.io/v1.FilesystemSpec)* | |  |  | | --- | --- | | `metadataPool`   *[NamedPoolSpec](index.md#ceph.rook.io/v1.NamedPoolSpec)* | The metadata pool settings | | `dataPools`   *[[]NamedPoolSpec](index.md#ceph.rook.io/v1.NamedPoolSpec)* | The data pool settings, with optional predefined pool name. | | `preservePoolNames`   *bool* | *(Optional)* Preserve pool names as specified | | `preservePoolsOnDelete`   *bool* | *(Optional)* Preserve pools on filesystem deletion | | `preserveFilesystemOnDelete`   *bool* | *(Optional)* Preserve the fs in the cluster on CephFilesystem CR deletion. Setting this to true automatically implies PreservePoolsOnDelete is true. | | `metadataServer`   *[MetadataServerSpec](index.md#ceph.rook.io/v1.MetadataServerSpec)* | The mds pod info | | `mirroring`   *[FSMirroringSpec](index.md#ceph.rook.io/v1.FSMirroringSpec)* | *(Optional)* The mirroring settings | | `statusCheck`   *[MirrorHealthCheckSpec](index.md#ceph.rook.io/v1.MirrorHealthCheckSpec)* | The mirroring statusCheck | |
| `status`   *[CephFilesystemStatus](index.md#ceph.rook.io/v1.CephFilesystemStatus)* |  |

### CephFilesystemMirror

CephFilesystemMirror is the Ceph Filesystem Mirror object definition

| Field | Description |
| --- | --- |
| `apiVersion`  string | `ceph.rook.io/v1` |
| `kind`  string | `CephFilesystemMirror` |
| `metadata`   *[Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#objectmeta-v1-meta)* | Refer to the Kubernetes API documentation for the fields of the `metadata` field. |
| `spec`   *[FilesystemMirroringSpec](index.md#ceph.rook.io/v1.FilesystemMirroringSpec)* | |  |  | | --- | --- | | `placement`   *[Placement](index.md#ceph.rook.io/v1.Placement)* | *(Optional)* The affinity to place the rgw pods (default is to place on any available node) | | `annotations`   *[Annotations](index.md#ceph.rook.io/v1.Annotations)* | *(Optional)* The annotations-related configuration to add/set on each Pod related object. | | `labels`   *[Labels](index.md#ceph.rook.io/v1.Labels)* | *(Optional)* The labels-related configuration to add/set on each Pod related object. | | `resources`   *[Kubernetes core/v1.ResourceRequirements](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#resourcerequirements-v1-core)* | *(Optional)* The resource requirements for the cephfs-mirror pods | | `priorityClassName`   *string* | *(Optional)* PriorityClassName sets priority class on the cephfs-mirror pods | |
| `status`   *[Status](index.md#ceph.rook.io/v1.Status)* | *(Optional)* |

### CephFilesystemSubVolumeGroup

CephFilesystemSubVolumeGroup represents a Ceph Filesystem SubVolumeGroup

| Field | Description |
| --- | --- |
| `apiVersion`  string | `ceph.rook.io/v1` |
| `kind`  string | `CephFilesystemSubVolumeGroup` |
| `metadata`   *[Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#objectmeta-v1-meta)* | Refer to the Kubernetes API documentation for the fields of the `metadata` field. |
| `spec`   *[CephFilesystemSubVolumeGroupSpec](index.md#ceph.rook.io/v1.CephFilesystemSubVolumeGroupSpec)* | Spec represents the specification of a Ceph Filesystem SubVolumeGroup      |  |  | | --- | --- | | `name`   *string* | *(Optional)* The name of the subvolume group. If not set, the default is the name of the subvolumeGroup CR. | | `filesystemName`   *string* | FilesystemName is the name of Ceph Filesystem SubVolumeGroup volume name. Typically it’s the name of the CephFilesystem CR. If not coming from the CephFilesystem CR, it can be retrieved from the list of Ceph Filesystem volumes with `ceph fs volume ls`. To learn more about Ceph Filesystem abstractions see <https://docs.ceph.com/en/latest/cephfs/fs-volumes/#fs-volumes-and-subvolumes> | | `pinning`   *[CephFilesystemSubVolumeGroupSpecPinning](index.md#ceph.rook.io/v1.CephFilesystemSubVolumeGroupSpecPinning)* | *(Optional)* Pinning configuration of CephFilesystemSubVolumeGroup, reference <https://docs.ceph.com/en/latest/cephfs/fs-volumes/#pinning-subvolumes-and-subvolume-groups> only one out of (export, distributed, random) can be set at a time | | `quota`   *k8s.io/apimachinery/pkg/api/resource.Quantity* | *(Optional)* Quota size of the Ceph Filesystem subvolume group. | | `dataPoolName`   *string* | *(Optional)* The data pool name for the Ceph Filesystem subvolume group layout, if the default CephFS pool is not desired. | |
| `status`   *[CephFilesystemSubVolumeGroupStatus](index.md#ceph.rook.io/v1.CephFilesystemSubVolumeGroupStatus)* | *(Optional)* Status represents the status of a CephFilesystem SubvolumeGroup |

### CephNFS

CephNFS represents a Ceph NFS

| Field | Description |
| --- | --- |
| `apiVersion`  string | `ceph.rook.io/v1` |
| `kind`  string | `CephNFS` |
| `metadata`   *[Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#objectmeta-v1-meta)* | Refer to the Kubernetes API documentation for the fields of the `metadata` field. |
| `spec`   *[NFSGaneshaSpec](index.md#ceph.rook.io/v1.NFSGaneshaSpec)* | |  |  | | --- | --- | | `rados`   *[GaneshaRADOSSpec](index.md#ceph.rook.io/v1.GaneshaRADOSSpec)* | *(Optional)* RADOS is the Ganesha RADOS specification | | `server`   *[GaneshaServerSpec](index.md#ceph.rook.io/v1.GaneshaServerSpec)* | Server is the Ganesha Server specification | | `security`   *[NFSSecuritySpec](index.md#ceph.rook.io/v1.NFSSecuritySpec)* | *(Optional)* Security allows specifying security configurations for the NFS cluster | |
| `status`   *[Status](index.md#ceph.rook.io/v1.Status)* | *(Optional)* |

### CephObjectRealm

CephObjectRealm represents a Ceph Object Store Gateway Realm

| Field | Description |
| --- | --- |
| `apiVersion`  string | `ceph.rook.io/v1` |
| `kind`  string | `CephObjectRealm` |
| `metadata`   *[Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#objectmeta-v1-meta)* | Refer to the Kubernetes API documentation for the fields of the `metadata` field. |
| `spec`   *[ObjectRealmSpec](index.md#ceph.rook.io/v1.ObjectRealmSpec)* | *(Optional)*      |  |  | | --- | --- | | `pull`   *[PullSpec](index.md#ceph.rook.io/v1.PullSpec)* |  | | `defaultRealm`   *bool* | *(Optional)* Set this realm as the default in Ceph. Only one realm should be default. | |
| `status`   *[Status](index.md#ceph.rook.io/v1.Status)* | *(Optional)* |

### CephObjectStore

CephObjectStore represents a Ceph Object Store Gateway

| Field | Description |
| --- | --- |
| `apiVersion`  string | `ceph.rook.io/v1` |
| `kind`  string | `CephObjectStore` |
| `metadata`   *[Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#objectmeta-v1-meta)* | Refer to the Kubernetes API documentation for the fields of the `metadata` field. |
| `spec`   *[ObjectStoreSpec](index.md#ceph.rook.io/v1.ObjectStoreSpec)* | |  |  | | --- | --- | | `metadataPool`   *[PoolSpec](index.md#ceph.rook.io/v1.PoolSpec)* | *(Optional)* The metadata pool settings | | `dataPool`   *[PoolSpec](index.md#ceph.rook.io/v1.PoolSpec)* | *(Optional)* The data pool settings | | `sharedPools`   *[ObjectSharedPoolsSpec](index.md#ceph.rook.io/v1.ObjectSharedPoolsSpec)* | *(Optional)* The pool information when configuring RADOS namespaces in existing pools. | | `preservePoolsOnDelete`   *bool* | *(Optional)* Preserve pools on object store deletion | | `gateway`   *[GatewaySpec](index.md#ceph.rook.io/v1.GatewaySpec)* | *(Optional)* The rgw pod info | | `protocols`   *[ProtocolSpec](index.md#ceph.rook.io/v1.ProtocolSpec)* | *(Optional)* The protocol specification | | `auth`   *[AuthSpec](index.md#ceph.rook.io/v1.AuthSpec)* | *(Optional)* The authentication configuration | | `zone`   *[ZoneSpec](index.md#ceph.rook.io/v1.ZoneSpec)* | *(Optional)* The multisite info | | `healthCheck`   *[ObjectHealthCheckSpec](index.md#ceph.rook.io/v1.ObjectHealthCheckSpec)* | *(Optional)* The RGW health probes | | `security`   *[ObjectStoreSecuritySpec](index.md#ceph.rook.io/v1.ObjectStoreSecuritySpec)* | *(Optional)* Security represents security settings | | `allowUsersInNamespaces`   *[]string* | *(Optional)* The list of allowed namespaces in addition to the object store namespace where ceph object store users may be created. Specify “\*” to allow all namespaces, otherwise list individual namespaces that are to be allowed. This is useful for applications that need object store credentials to be created in their own namespace, where neither OBCs nor COSI is being used to create buckets. The default is empty. | | `hosting`   *[ObjectStoreHostingSpec](index.md#ceph.rook.io/v1.ObjectStoreHostingSpec)* | *(Optional)* Hosting settings for the object store. A common use case for hosting configuration is to inform Rook of endpoints that support DNS wildcards, which in turn allows virtual host-style bucket addressing. | | `defaultRealm`   *bool* | *(Optional)* Set this realm as the default in Ceph. Only one realm should be default. Do not set this true on more than one CephObjectStore. This may not be set when zone is also specified; in this case, the realm referenced by the zone’s zonegroup should configure defaulting behavior. | |
| `status`   *[ObjectStoreStatus](index.md#ceph.rook.io/v1.ObjectStoreStatus)* |  |

### CephObjectStoreUser

CephObjectStoreUser represents a Ceph Object Store Gateway User

| Field | Description |
| --- | --- |
| `apiVersion`  string | `ceph.rook.io/v1` |
| `kind`  string | `CephObjectStoreUser` |
| `metadata`   *[Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#objectmeta-v1-meta)* | Refer to the Kubernetes API documentation for the fields of the `metadata` field. |
| `spec`   *[ObjectStoreUserSpec](index.md#ceph.rook.io/v1.ObjectStoreUserSpec)* | |  |  | | --- | --- | | `store`   *string* | *(Optional)* The store the user will be created in | | `displayName`   *string* | *(Optional)* The display name for the ceph user. | | `capabilities`   *[ObjectUserCapSpec](index.md#ceph.rook.io/v1.ObjectUserCapSpec)* | *(Optional)* | | `quotas`   *[ObjectUserQuotaSpec](index.md#ceph.rook.io/v1.ObjectUserQuotaSpec)* | *(Optional)* | | `keys`   *[[]ObjectUserKey](index.md#ceph.rook.io/v1.ObjectUserKey)* | *(Optional)* Allows specifying credentials for the user. If not provided, the operator will generate them. | | `clusterNamespace`   *string* | *(Optional)* The namespace where the parent CephCluster and CephObjectStore are found | |
| `status`   *[ObjectStoreUserStatus](index.md#ceph.rook.io/v1.ObjectStoreUserStatus)* | *(Optional)* |

### CephObjectZone

CephObjectZone represents a Ceph Object Store Gateway Zone

| Field | Description |
| --- | --- |
| `apiVersion`  string | `ceph.rook.io/v1` |
| `kind`  string | `CephObjectZone` |
| `metadata`   *[Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#objectmeta-v1-meta)* | Refer to the Kubernetes API documentation for the fields of the `metadata` field. |
| `spec`   *[ObjectZoneSpec](index.md#ceph.rook.io/v1.ObjectZoneSpec)* | |  |  | | --- | --- | | `zoneGroup`   *string* | The name of the zone group the zone is a member of. | | `metadataPool`   *[PoolSpec](index.md#ceph.rook.io/v1.PoolSpec)* | *(Optional)* The metadata pool settings | | `dataPool`   *[PoolSpec](index.md#ceph.rook.io/v1.PoolSpec)* | *(Optional)* The data pool settings | | `sharedPools`   *[ObjectSharedPoolsSpec](index.md#ceph.rook.io/v1.ObjectSharedPoolsSpec)* | *(Optional)* The pool information when configuring RADOS namespaces in existing pools. | | `customEndpoints`   *[]string* | *(Optional)* If this zone cannot be accessed from other peer Ceph clusters via the ClusterIP Service endpoint created by Rook, you must set this to the externally reachable endpoint(s). You may include the port in the definition. For example: “[https://my-object-store.my-domain.net:443”](https://my-object-store.my-domain.net:443"). In many cases, you should set this to the endpoint of the ingress resource that makes the CephObjectStore associated with this CephObjectStoreZone reachable to peer clusters. The list can have one or more endpoints pointing to different RGW servers in the zone.  If a CephObjectStore endpoint is omitted from this list, that object store’s gateways will not receive multisite replication data (see CephObjectStore.spec.gateway.disableMultisiteSyncTraffic). | | `preservePoolsOnDelete`   *bool* | *(Optional)* Preserve pools on object zone deletion | |
| `status`   *[Status](index.md#ceph.rook.io/v1.Status)* | *(Optional)* |

### CephObjectZoneGroup

CephObjectZoneGroup represents a Ceph Object Store Gateway Zone Group

| Field | Description |
| --- | --- |
| `apiVersion`  string | `ceph.rook.io/v1` |
| `kind`  string | `CephObjectZoneGroup` |
| `metadata`   *[Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#objectmeta-v1-meta)* | Refer to the Kubernetes API documentation for the fields of the `metadata` field. |
| `spec`   *[ObjectZoneGroupSpec](index.md#ceph.rook.io/v1.ObjectZoneGroupSpec)* | |  |  | | --- | --- | | `realm`   *string* | The name of the realm the zone group is a member of. | |
| `status`   *[Status](index.md#ceph.rook.io/v1.Status)* | *(Optional)* |

### CephRBDMirror

CephRBDMirror represents a Ceph RBD Mirror

| Field | Description |
| --- | --- |
| `apiVersion`  string | `ceph.rook.io/v1` |
| `kind`  string | `CephRBDMirror` |
| `metadata`   *[Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#objectmeta-v1-meta)* | Refer to the Kubernetes API documentation for the fields of the `metadata` field. |
| `spec`   *[RBDMirroringSpec](index.md#ceph.rook.io/v1.RBDMirroringSpec)* | |  |  | | --- | --- | | `count`   *int* | Count represents the number of rbd mirror instance to run | | `peers`   *[MirroringPeerSpec](index.md#ceph.rook.io/v1.MirroringPeerSpec)* | *(Optional)* Peers represents the peers spec | | `placement`   *[Placement](index.md#ceph.rook.io/v1.Placement)* | *(Optional)* The affinity to place the rgw pods (default is to place on any available node) | | `annotations`   *[Annotations](index.md#ceph.rook.io/v1.Annotations)* | *(Optional)* The annotations-related configuration to add/set on each Pod related object. | | `labels`   *[Labels](index.md#ceph.rook.io/v1.Labels)* | *(Optional)* The labels-related configuration to add/set on each Pod related object. | | `resources`   *[Kubernetes core/v1.ResourceRequirements](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#resourcerequirements-v1-core)* | *(Optional)* The resource requirements for the rbd mirror pods | | `priorityClassName`   *string* | *(Optional)* PriorityClassName sets priority class on the rbd mirror pods | |
| `status`   *[Status](index.md#ceph.rook.io/v1.Status)* | *(Optional)* |

### AMQPEndpointSpec

(*Appears on:*[TopicEndpointSpec](index.md#ceph.rook.io/v1.TopicEndpointSpec))

AMQPEndpointSpec represent the spec of an AMQP endpoint of a Bucket Topic

| Field | Description |
| --- | --- |
| `uri`   *string* | The URI of the AMQP endpoint to push notification to |
| `exchange`   *string* | Name of the exchange that is used to route messages based on topics |
| `disableVerifySSL`   *bool* | *(Optional)* Indicate whether the server certificate is validated by the client or not |
| `ackLevel`   *string* | *(Optional)* The ack level required for this topic (none/broker/routeable) |

### AdditionalVolumeMount

AdditionalVolumeMount represents the source from where additional files in pod containers should come from and what subdirectory they are made available in.

| Field | Description |
| --- | --- |
| `subPath`   *string* | SubPath defines the sub-path (subdirectory) of the directory root where the volumeSource will be mounted. All files/keys in the volume source’s volume will be mounted to the subdirectory. This is not the same as the Kubernetes `subPath` volume mount option. Each subPath definition must be unique and must not contain ‘:’. |
| `volumeSource`   *[ConfigFileVolumeSource](index.md#ceph.rook.io/v1.ConfigFileVolumeSource)* | VolumeSource accepts a pared down version of the standard Kubernetes VolumeSource for the additional file(s) like what is normally used to configure Volumes for a Pod. Fore example, a ConfigMap, Secret, or HostPath. Each VolumeSource adds one or more additional files to the container `<directory-root>/<subPath>` directory. Be aware that some files may need to have a specific file mode like 0600 due to application requirements. For example, CA or TLS certificates. |

### AdditionalVolumeMounts (`[]github.com/rook/rook/pkg/apis/ceph.rook.io/v1.AdditionalVolumeMount` alias)

(*Appears on:*[GatewaySpec](index.md#ceph.rook.io/v1.GatewaySpec), [SSSDSidecar](index.md#ceph.rook.io/v1.SSSDSidecar))

### AddressRangesSpec

(*Appears on:*[NetworkSpec](index.md#ceph.rook.io/v1.NetworkSpec))

| Field | Description |
| --- | --- |
| `public`   *[CIDRList](index.md#ceph.rook.io/v1.CIDRList)* | *(Optional)* Public defines a list of CIDRs to use for Ceph public network communication. |
| `cluster`   *[CIDRList](index.md#ceph.rook.io/v1.CIDRList)* | *(Optional)* Cluster defines a list of CIDRs to use for Ceph cluster network communication. |

### Annotations (`map[string]string` alias)

(*Appears on:*[FilesystemMirroringSpec](index.md#ceph.rook.io/v1.FilesystemMirroringSpec), [GaneshaServerSpec](index.md#ceph.rook.io/v1.GaneshaServerSpec), [GatewaySpec](index.md#ceph.rook.io/v1.GatewaySpec), [MetadataServerSpec](index.md#ceph.rook.io/v1.MetadataServerSpec), [RBDMirroringSpec](index.md#ceph.rook.io/v1.RBDMirroringSpec), [RGWServiceSpec](index.md#ceph.rook.io/v1.RGWServiceSpec))

Annotations are annotations

### AnnotationsSpec (`map[github.com/rook/rook/pkg/apis/ceph.rook.io/v1.KeyType]github.com/rook/rook/pkg/apis/ceph.rook.io/v1.Annotations` alias)

(*Appears on:*[ClusterSpec](index.md#ceph.rook.io/v1.ClusterSpec))

AnnotationsSpec is the main spec annotation for all daemons

### AuthSpec

(*Appears on:*[ObjectStoreSpec](index.md#ceph.rook.io/v1.ObjectStoreSpec))

AuthSpec represents the authentication protocol configuration of a Ceph Object Store Gateway

| Field | Description |
| --- | --- |
| `keystone`   *[KeystoneSpec](index.md#ceph.rook.io/v1.KeystoneSpec)* | *(Optional)* The spec for Keystone |

### BucketNotificationEvent (`string` alias)

(*Appears on:*[BucketNotificationSpec](index.md#ceph.rook.io/v1.BucketNotificationSpec))

BucketNotificationSpec represent the event type of the bucket notification

### BucketNotificationSpec

(*Appears on:*[CephBucketNotification](index.md#ceph.rook.io/v1.CephBucketNotification))

BucketNotificationSpec represent the spec of a Bucket Notification

| Field | Description |
| --- | --- |
| `topic`   *string* | The name of the topic associated with this notification |
| `events`   *[[]BucketNotificationEvent](index.md#ceph.rook.io/v1.BucketNotificationEvent)* | *(Optional)* List of events that should trigger the notification |
| `filter`   *[NotificationFilterSpec](index.md#ceph.rook.io/v1.NotificationFilterSpec)* | *(Optional)* Spec of notification filter |

### BucketTopicSpec

(*Appears on:*[CephBucketTopic](index.md#ceph.rook.io/v1.CephBucketTopic))

BucketTopicSpec represent the spec of a Bucket Topic

| Field | Description |
| --- | --- |
| `objectStoreName`   *string* | The name of the object store on which to define the topic |
| `objectStoreNamespace`   *string* | The namespace of the object store on which to define the topic |
| `opaqueData`   *string* | *(Optional)* Data which is sent in each event |
| `persistent`   *bool* | *(Optional)* Indication whether notifications to this endpoint are persistent or not |
| `endpoint`   *[TopicEndpointSpec](index.md#ceph.rook.io/v1.TopicEndpointSpec)* | Contains the endpoint spec of the topic |

### BucketTopicStatus

(*Appears on:*[CephBucketTopic](index.md#ceph.rook.io/v1.CephBucketTopic))

BucketTopicStatus represents the Status of a CephBucketTopic

| Field | Description |
| --- | --- |
| `phase`   *string* | *(Optional)* |
| `ARN`   *string* | *(Optional)* The ARN of the topic generated by the RGW |
| `observedGeneration`   *int64* | *(Optional)* ObservedGeneration is the latest generation observed by the controller. |
| `secrets`   *[[]SecretReference](index.md#ceph.rook.io/v1.SecretReference)* | *(Optional)* |

### CIDR (`string` alias)

An IPv4 or IPv6 network CIDR.

This naive kubebuilder regex provides immediate feedback for some typos and for a common problem case where the range spec is forgotten (e.g., /24). Rook does in-depth validation in code.

### COSIDeploymentStrategy (`string` alias)

(*Appears on:*[CephCOSIDriverSpec](index.md#ceph.rook.io/v1.CephCOSIDriverSpec))

COSIDeploymentStrategy represents the strategy to use to deploy the Ceph COSI driver

| Value | Description |
| --- | --- |
| "Always" | Always means the Ceph COSI driver will be deployed even if the object store is not present |
| "Auto" | Auto means the Ceph COSI driver will be deployed automatically if object store is present |
| "Never" | Never means the Ceph COSI driver will never deployed |

### CSICephFSSpec

(*Appears on:*[CSIDriverSpec](index.md#ceph.rook.io/v1.CSIDriverSpec))

CSICephFSSpec defines the settings for CephFS CSI driver.

| Field | Description |
| --- | --- |
| `kernelMountOptions`   *string* | *(Optional)* KernelMountOptions defines the mount options for kernel mounter. |
| `fuseMountOptions`   *string* | *(Optional)* FuseMountOptions defines the mount options for ceph fuse mounter. |

### CSIDriverSpec

(*Appears on:*[ClusterSpec](index.md#ceph.rook.io/v1.ClusterSpec))

CSIDriverSpec defines CSI Driver settings applied per cluster.

| Field | Description |
| --- | --- |
| `readAffinity`   *[ReadAffinitySpec](index.md#ceph.rook.io/v1.ReadAffinitySpec)* | *(Optional)* ReadAffinity defines the read affinity settings for CSI driver. |
| `cephfs`   *[CSICephFSSpec](index.md#ceph.rook.io/v1.CSICephFSSpec)* | *(Optional)* CephFS defines CSI Driver settings for CephFS driver. |
| `skipUserCreation`   *bool* | *(Optional)* SkipUserCreation determines whether CSI users and their associated secrets should be skipped. If set to true, the user must manually manage these secrets. |

### Capacity

(*Appears on:*[CephStatus](index.md#ceph.rook.io/v1.CephStatus))

Capacity is the capacity information of a Ceph Cluster

| Field | Description |
| --- | --- |
| `bytesTotal`   *uint64* |  |
| `bytesUsed`   *uint64* |  |
| `bytesAvailable`   *uint64* |  |
| `lastUpdated`   *string* |  |

### CephBlockPoolRadosNamespace

CephBlockPoolRadosNamespace represents a Ceph BlockPool Rados Namespace

| Field | Description |
| --- | --- |
| `metadata`   *[Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#objectmeta-v1-meta)* | Refer to the Kubernetes API documentation for the fields of the `metadata` field. |
| `spec`   *[CephBlockPoolRadosNamespaceSpec](index.md#ceph.rook.io/v1.CephBlockPoolRadosNamespaceSpec)* | Spec represents the specification of a Ceph BlockPool Rados Namespace      |  |  | | --- | --- | | `name`   *string* | *(Optional)* The name of the CephBlockPoolRadosNamespaceSpec namespace. If not set, the default is the name of the CR. | | `blockPoolName`   *string* | BlockPoolName is the name of Ceph BlockPool. Typically it’s the name of the CephBlockPool CR. | | `mirroring`   *[RadosNamespaceMirroring](index.md#ceph.rook.io/v1.RadosNamespaceMirroring)* | *(Optional)* Mirroring configuration of CephBlockPoolRadosNamespace | |
| `status`   *[CephBlockPoolRadosNamespaceStatus](index.md#ceph.rook.io/v1.CephBlockPoolRadosNamespaceStatus)* | *(Optional)* Status represents the status of a CephBlockPool Rados Namespace |

### CephBlockPoolRadosNamespaceSpec

(*Appears on:*[CephBlockPoolRadosNamespace](index.md#ceph.rook.io/v1.CephBlockPoolRadosNamespace))

CephBlockPoolRadosNamespaceSpec represents the specification of a CephBlockPool Rados Namespace

| Field | Description |
| --- | --- |
| `name`   *string* | *(Optional)* The name of the CephBlockPoolRadosNamespaceSpec namespace. If not set, the default is the name of the CR. |
| `blockPoolName`   *string* | BlockPoolName is the name of Ceph BlockPool. Typically it’s the name of the CephBlockPool CR. |
| `mirroring`   *[RadosNamespaceMirroring](index.md#ceph.rook.io/v1.RadosNamespaceMirroring)* | *(Optional)* Mirroring configuration of CephBlockPoolRadosNamespace |

### CephBlockPoolRadosNamespaceStatus

(*Appears on:*[CephBlockPoolRadosNamespace](index.md#ceph.rook.io/v1.CephBlockPoolRadosNamespace))

CephBlockPoolRadosNamespaceStatus represents the Status of Ceph BlockPool Rados Namespace

| Field | Description |
| --- | --- |
| `phase`   *[ConditionType](index.md#ceph.rook.io/v1.ConditionType)* | *(Optional)* |
| `info`   *map[string]string* | *(Optional)* |
| `mirroringStatus`   *[MirroringStatusSpec](index.md#ceph.rook.io/v1.MirroringStatusSpec)* | *(Optional)* |
| `mirroringInfo`   *[MirroringInfoSpec](index.md#ceph.rook.io/v1.MirroringInfoSpec)* | *(Optional)* |
| `snapshotScheduleStatus`   *[SnapshotScheduleStatusSpec](index.md#ceph.rook.io/v1.SnapshotScheduleStatusSpec)* | *(Optional)* |
| `conditions`   *[[]Condition](index.md#ceph.rook.io/v1.Condition)* |  |

### CephBlockPoolStatus

(*Appears on:*[CephBlockPool](index.md#ceph.rook.io/v1.CephBlockPool))

CephBlockPoolStatus represents the mirroring status of Ceph Storage Pool

| Field | Description |
| --- | --- |
| `phase`   *[ConditionType](index.md#ceph.rook.io/v1.ConditionType)* | *(Optional)* |
| `mirroringStatus`   *[MirroringStatusSpec](index.md#ceph.rook.io/v1.MirroringStatusSpec)* | *(Optional)* |
| `mirroringInfo`   *[MirroringInfoSpec](index.md#ceph.rook.io/v1.MirroringInfoSpec)* | *(Optional)* |
| `poolID`   *int* | optional |
| `snapshotScheduleStatus`   *[SnapshotScheduleStatusSpec](index.md#ceph.rook.io/v1.SnapshotScheduleStatusSpec)* | *(Optional)* |
| `info`   *map[string]string* | *(Optional)* |
| `observedGeneration`   *int64* | *(Optional)* ObservedGeneration is the latest generation observed by the controller. |
| `conditions`   *[[]Condition](index.md#ceph.rook.io/v1.Condition)* |  |

### CephCOSIDriverSpec

(*Appears on:*[CephCOSIDriver](index.md#ceph.rook.io/v1.CephCOSIDriver))

CephCOSIDriverSpec represents the specification of a Ceph COSI Driver

| Field | Description |
| --- | --- |
| `image`   *string* | *(Optional)* Image is the container image to run the Ceph COSI driver |
| `objectProvisionerImage`   *string* | *(Optional)* ObjectProvisionerImage is the container image to run the COSI driver sidecar |
| `deploymentStrategy`   *[COSIDeploymentStrategy](index.md#ceph.rook.io/v1.COSIDeploymentStrategy)* | *(Optional)* DeploymentStrategy is the strategy to use to deploy the COSI driver. |
| `placement`   *[Placement](index.md#ceph.rook.io/v1.Placement)* | *(Optional)* Placement is the placement strategy to use for the COSI driver |
| `resources`   *[Kubernetes core/v1.ResourceRequirements](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#resourcerequirements-v1-core)* | *(Optional)* Resources is the resource requirements for the COSI driver |

### CephClientStatus

(*Appears on:*[CephClient](index.md#ceph.rook.io/v1.CephClient))

CephClientStatus represents the Status of Ceph Client

| Field | Description |
| --- | --- |
| `phase`   *[ConditionType](index.md#ceph.rook.io/v1.ConditionType)* | *(Optional)* |
| `info`   *map[string]string* | *(Optional)* |
| `observedGeneration`   *int64* | *(Optional)* ObservedGeneration is the latest generation observed by the controller. |

### CephClusterHealthCheckSpec

(*Appears on:*[ClusterSpec](index.md#ceph.rook.io/v1.ClusterSpec))

CephClusterHealthCheckSpec represent the healthcheck for Ceph daemons

| Field | Description |
| --- | --- |
| `daemonHealth`   *[DaemonHealthSpec](index.md#ceph.rook.io/v1.DaemonHealthSpec)* | *(Optional)* DaemonHealth is the health check for a given daemon |
| `livenessProbe`   *[map[github.com/rook/rook/pkg/apis/ceph.rook.io/v1.KeyType]\*github.com/rook/rook/pkg/apis/ceph.rook.io/v1.ProbeSpec](index.md#ceph.rook.io/v1.*github.com/rook/rook/pkg/apis/ceph.rook.io/v1.ProbeSpec)* | *(Optional)* LivenessProbe allows changing the livenessProbe configuration for a given daemon |
| `startupProbe`   *[map[github.com/rook/rook/pkg/apis/ceph.rook.io/v1.KeyType]\*github.com/rook/rook/pkg/apis/ceph.rook.io/v1.ProbeSpec](index.md#ceph.rook.io/v1.*github.com/rook/rook/pkg/apis/ceph.rook.io/v1.ProbeSpec)* | *(Optional)* StartupProbe allows changing the startupProbe configuration for a given daemon |

### CephDaemonsVersions

(*Appears on:*[CephStatus](index.md#ceph.rook.io/v1.CephStatus))

CephDaemonsVersions show the current ceph version for different ceph daemons

| Field | Description |
| --- | --- |
| `mon`   *map[string]int* | *(Optional)* Mon shows Mon Ceph version |
| `mgr`   *map[string]int* | *(Optional)* Mgr shows Mgr Ceph version |
| `osd`   *map[string]int* | *(Optional)* Osd shows Osd Ceph version |
| `rgw`   *map[string]int* | *(Optional)* Rgw shows Rgw Ceph version |
| `mds`   *map[string]int* | *(Optional)* Mds shows Mds Ceph version |
| `rbd-mirror`   *map[string]int* | *(Optional)* RbdMirror shows RbdMirror Ceph version |
| `cephfs-mirror`   *map[string]int* | *(Optional)* CephFSMirror shows CephFSMirror Ceph version |
| `overall`   *map[string]int* | *(Optional)* Overall shows overall Ceph version |

### CephExporterSpec

(*Appears on:*[MonitoringSpec](index.md#ceph.rook.io/v1.MonitoringSpec))

| Field | Description |
| --- | --- |
| `perfCountersPrioLimit`   *int64* | Only performance counters greater than or equal to this option are fetched |
| `statsPeriodSeconds`   *int64* | Time to wait before sending requests again to exporter server (seconds) |
| `hostNetwork`   *bool* | *(Optional)* Whether host networking is enabled for CephExporter. If not set, the network settings from CephCluster.spec.networking will be applied. |

### CephFilesystemStatus

(*Appears on:*[CephFilesystem](index.md#ceph.rook.io/v1.CephFilesystem))

CephFilesystemStatus represents the status of a Ceph Filesystem

| Field | Description |
| --- | --- |
| `phase`   *[ConditionType](index.md#ceph.rook.io/v1.ConditionType)* | *(Optional)* |
| `snapshotScheduleStatus`   *[FilesystemSnapshotScheduleStatusSpec](index.md#ceph.rook.io/v1.FilesystemSnapshotScheduleStatusSpec)* | *(Optional)* |
| `info`   *map[string]string* | *(Optional)* Use only info and put mirroringStatus in it? |
| `mirroringStatus`   *[FilesystemMirroringInfoSpec](index.md#ceph.rook.io/v1.FilesystemMirroringInfoSpec)* | *(Optional)* MirroringStatus is the filesystem mirroring status |
| `conditions`   *[[]Condition](index.md#ceph.rook.io/v1.Condition)* |  |
| `observedGeneration`   *int64* | *(Optional)* ObservedGeneration is the latest generation observed by the controller. |

### CephFilesystemSubVolumeGroupSpec

(*Appears on:*[CephFilesystemSubVolumeGroup](index.md#ceph.rook.io/v1.CephFilesystemSubVolumeGroup))

CephFilesystemSubVolumeGroupSpec represents the specification of a Ceph Filesystem SubVolumeGroup

| Field | Description |
| --- | --- |
| `name`   *string* | *(Optional)* The name of the subvolume group. If not set, the default is the name of the subvolumeGroup CR. |
| `filesystemName`   *string* | FilesystemName is the name of Ceph Filesystem SubVolumeGroup volume name. Typically it’s the name of the CephFilesystem CR. If not coming from the CephFilesystem CR, it can be retrieved from the list of Ceph Filesystem volumes with `ceph fs volume ls`. To learn more about Ceph Filesystem abstractions see <https://docs.ceph.com/en/latest/cephfs/fs-volumes/#fs-volumes-and-subvolumes> |
| `pinning`   *[CephFilesystemSubVolumeGroupSpecPinning](index.md#ceph.rook.io/v1.CephFilesystemSubVolumeGroupSpecPinning)* | *(Optional)* Pinning configuration of CephFilesystemSubVolumeGroup, reference <https://docs.ceph.com/en/latest/cephfs/fs-volumes/#pinning-subvolumes-and-subvolume-groups> only one out of (export, distributed, random) can be set at a time |
| `quota`   *k8s.io/apimachinery/pkg/api/resource.Quantity* | *(Optional)* Quota size of the Ceph Filesystem subvolume group. |
| `dataPoolName`   *string* | *(Optional)* The data pool name for the Ceph Filesystem subvolume group layout, if the default CephFS pool is not desired. |

### CephFilesystemSubVolumeGroupSpecPinning

(*Appears on:*[CephFilesystemSubVolumeGroupSpec](index.md#ceph.rook.io/v1.CephFilesystemSubVolumeGroupSpec))

CephFilesystemSubVolumeGroupSpecPinning represents the pinning configuration of SubVolumeGroup

| Field | Description |
| --- | --- |
| `export`   *int* | *(Optional)* |
| `distributed`   *int* | *(Optional)* |
| `random,`   *float64* | *(Optional)* |

### CephFilesystemSubVolumeGroupStatus

(*Appears on:*[CephFilesystemSubVolumeGroup](index.md#ceph.rook.io/v1.CephFilesystemSubVolumeGroup))

CephFilesystemSubVolumeGroupStatus represents the Status of Ceph Filesystem SubVolumeGroup

| Field | Description |
| --- | --- |
| `phase`   *[ConditionType](index.md#ceph.rook.io/v1.ConditionType)* | *(Optional)* |
| `info`   *map[string]string* | *(Optional)* |
| `observedGeneration`   *int64* | *(Optional)* ObservedGeneration is the latest generation observed by the controller. |

### CephHealthMessage

(*Appears on:*[CephStatus](index.md#ceph.rook.io/v1.CephStatus))

CephHealthMessage represents the health message of a Ceph Cluster

| Field | Description |
| --- | --- |
| `severity`   *string* |  |
| `message`   *string* |  |

### CephNetworkType (`string` alias)

CephNetworkType should be “public” or “cluster”. Allow any string so that over-specified legacy clusters do not break on CRD update.

| Value | Description |
| --- | --- |
| "cluster" |  |
| "public" |  |

### CephStatus

(*Appears on:*[ClusterStatus](index.md#ceph.rook.io/v1.ClusterStatus))

CephStatus is the details health of a Ceph Cluster

| Field | Description |
| --- | --- |
| `health`   *string* |  |
| `details`   *[map[string]github.com/rook/rook/pkg/apis/ceph.rook.io/v1.CephHealthMessage](index.md#ceph.rook.io/v1.CephHealthMessage)* |  |
| `lastChecked`   *string* |  |
| `lastChanged`   *string* |  |
| `previousHealth`   *string* |  |
| `capacity`   *[Capacity](index.md#ceph.rook.io/v1.Capacity)* |  |
| `versions`   *[CephDaemonsVersions](index.md#ceph.rook.io/v1.CephDaemonsVersions)* | *(Optional)* |
| `fsid`   *string* |  |

### CephStorage

(*Appears on:*[ClusterStatus](index.md#ceph.rook.io/v1.ClusterStatus))

CephStorage represents flavors of Ceph Cluster Storage

| Field | Description |
| --- | --- |
| `deviceClasses`   *[[]DeviceClasses](index.md#ceph.rook.io/v1.DeviceClasses)* |  |
| `osd`   *[OSDStatus](index.md#ceph.rook.io/v1.OSDStatus)* |  |
| `deprecatedOSDs`   *map[string][]int* |  |

### CephVersionSpec

(*Appears on:*[ClusterSpec](index.md#ceph.rook.io/v1.ClusterSpec))

CephVersionSpec represents the settings for the Ceph version that Rook is orchestrating.

| Field | Description |
| --- | --- |
| `image`   *string* | *(Optional)* Image is the container image used to launch the ceph daemons, such as quay.io/ceph/ceph: The full list of images can be found at <https://quay.io/repository/ceph/ceph?tab=tags> |
| `allowUnsupported`   *bool* | *(Optional)* Whether to allow unsupported versions (do not set to true in production) |
| `imagePullPolicy`   *[Kubernetes core/v1.PullPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#pullpolicy-v1-core)* | *(Optional)* ImagePullPolicy describes a policy for if/when to pull a container image One of Always, Never, IfNotPresent. |

### CleanupConfirmationProperty (`string` alias)

(*Appears on:*[CleanupPolicySpec](index.md#ceph.rook.io/v1.CleanupPolicySpec))

CleanupConfirmationProperty represents the cleanup confirmation

| Value | Description |
| --- | --- |
| "yes-really-destroy-data" | DeleteDataDirOnHostsConfirmation represents the validation to destroy dataDirHostPath |

### CleanupPolicySpec

(*Appears on:*[ClusterSpec](index.md#ceph.rook.io/v1.ClusterSpec))

CleanupPolicySpec represents a Ceph Cluster cleanup policy

| Field | Description |
| --- | --- |
| `confirmation`   *[CleanupConfirmationProperty](index.md#ceph.rook.io/v1.CleanupConfirmationProperty)* | *(Optional)* Confirmation represents the cleanup confirmation |
| `sanitizeDisks`   *[SanitizeDisksSpec](index.md#ceph.rook.io/v1.SanitizeDisksSpec)* | *(Optional)* SanitizeDisks represents way we sanitize disks |
| `allowUninstallWithVolumes`   *bool* | *(Optional)* AllowUninstallWithVolumes defines whether we can proceed with the uninstall if they are RBD images still present |
| `wipeDevicesFromOtherClusters`   *bool* | *(Optional)* WipeDevicesFromOtherClusters wipes the OSD disks belonging to other clusters. This is useful in scenarios where ceph cluster was reinstalled but OSD disk still contains the metadata from previous ceph cluster. |

### ClientSpec

(*Appears on:*[CephClient](index.md#ceph.rook.io/v1.CephClient))

ClientSpec represents the specification of a Ceph Client

| Field | Description |
| --- | --- |
| `name`   *string* | *(Optional)* |
| `secretName`   *string* | *(Optional)* SecretName is the name of the secret created for this ceph client. If not specified, the default name is “rook-ceph-client-” as a prefix to the CR name. |
| `removeSecret`   *bool* | *(Optional)* RemoveSecret indicates whether the current secret for this ceph client should be removed or not. If true, the K8s secret will be deleted, but the cephx keyring will remain until the CR is deleted. |
| `caps`   *map[string]string* |  |

### ClusterSpec

(*Appears on:*[CephCluster](index.md#ceph.rook.io/v1.CephCluster))

ClusterSpec represents the specification of Ceph Cluster

| Field | Description |
| --- | --- |
| `cephVersion`   *[CephVersionSpec](index.md#ceph.rook.io/v1.CephVersionSpec)* | *(Optional)* The version information that instructs Rook to orchestrate a particular version of Ceph. |
| `storage`   *[StorageScopeSpec](index.md#ceph.rook.io/v1.StorageScopeSpec)* | *(Optional)* A spec for available storage in the cluster and how it should be used |
| `annotations`   *[AnnotationsSpec](index.md#ceph.rook.io/v1.AnnotationsSpec)* | *(Optional)* The annotations-related configuration to add/set on each Pod related object. |
| `labels`   *[LabelsSpec](index.md#ceph.rook.io/v1.LabelsSpec)* | *(Optional)* The labels-related configuration to add/set on each Pod related object. |
| `placement`   *[PlacementSpec](index.md#ceph.rook.io/v1.PlacementSpec)* | *(Optional)* The placement-related configuration to pass to kubernetes (affinity, node selector, tolerations). |
| `network`   *[NetworkSpec](index.md#ceph.rook.io/v1.NetworkSpec)* | *(Optional)* Network related configuration |
| `resources`   *[ResourceSpec](index.md#ceph.rook.io/v1.ResourceSpec)* | *(Optional)* Resources set resource requests and limits |
| `priorityClassNames`   *[PriorityClassNamesSpec](index.md#ceph.rook.io/v1.PriorityClassNamesSpec)* | *(Optional)* PriorityClassNames sets priority classes on components |
| `dataDirHostPath`   *string* | *(Optional)* The path on the host where config and data can be persisted |
| `skipUpgradeChecks`   *bool* | *(Optional)* SkipUpgradeChecks defines if an upgrade should be forced even if one of the check fails |
| `continueUpgradeAfterChecksEvenIfNotHealthy`   *bool* | *(Optional)* ContinueUpgradeAfterChecksEvenIfNotHealthy defines if an upgrade should continue even if PGs are not clean |
| `waitTimeoutForHealthyOSDInMinutes`   *time.Duration* | *(Optional)* WaitTimeoutForHealthyOSDInMinutes defines the time the operator would wait before an OSD can be stopped for upgrade or restart. If the timeout exceeds and OSD is not ok to stop, then the operator would skip upgrade for the current OSD and proceed with the next one if `continueUpgradeAfterChecksEvenIfNotHealthy` is `false`. If `continueUpgradeAfterChecksEvenIfNotHealthy` is `true`, then operator would continue with the upgrade of an OSD even if its not ok to stop after the timeout. This timeout won’t be applied if `skipUpgradeChecks` is `true`. The default wait timeout is 10 minutes. |
| `upgradeOSDRequiresHealthyPGs`   *bool* | *(Optional)* UpgradeOSDRequiresHealthyPGs defines if OSD upgrade requires PGs are clean. If set to `true` OSD upgrade process won’t start until PGs are healthy. This configuration will be ignored if `skipUpgradeChecks` is `true`. Default is false. |
| `disruptionManagement`   *[DisruptionManagementSpec](index.md#ceph.rook.io/v1.DisruptionManagementSpec)* | *(Optional)* A spec for configuring disruption management. |
| `mon`   *[MonSpec](index.md#ceph.rook.io/v1.MonSpec)* | *(Optional)* A spec for mon related options |
| `crashCollector`   *[CrashCollectorSpec](index.md#ceph.rook.io/v1.CrashCollectorSpec)* | *(Optional)* A spec for the crash controller |
| `dashboard`   *[DashboardSpec](index.md#ceph.rook.io/v1.DashboardSpec)* | *(Optional)* Dashboard settings |
| `monitoring`   *[MonitoringSpec](index.md#ceph.rook.io/v1.MonitoringSpec)* | *(Optional)* Prometheus based Monitoring settings |
| `external`   *[ExternalSpec](index.md#ceph.rook.io/v1.ExternalSpec)* | *(Optional)* Whether the Ceph Cluster is running external to this Kubernetes cluster mon, mgr, osd, mds, and discover daemons will not be created for external clusters. |
| `mgr`   *[MgrSpec](index.md#ceph.rook.io/v1.MgrSpec)* | *(Optional)* A spec for mgr related options |
| `removeOSDsIfOutAndSafeToRemove`   *bool* | *(Optional)* Remove the OSD that is out and safe to remove only if this option is true |
| `cleanupPolicy`   *[CleanupPolicySpec](index.md#ceph.rook.io/v1.CleanupPolicySpec)* | *(Optional)* Indicates user intent when deleting a cluster; blocks orchestration and should not be set if cluster deletion is not imminent. |
| `healthCheck`   *[CephClusterHealthCheckSpec](index.md#ceph.rook.io/v1.CephClusterHealthCheckSpec)* | *(Optional)* Internal daemon healthchecks and liveness probe |
| `security`   *[SecuritySpec](index.md#ceph.rook.io/v1.SecuritySpec)* | *(Optional)* Security represents security settings |
| `logCollector`   *[LogCollectorSpec](index.md#ceph.rook.io/v1.LogCollectorSpec)* | *(Optional)* Logging represents loggings settings |
| `csi`   *[CSIDriverSpec](index.md#ceph.rook.io/v1.CSIDriverSpec)* | *(Optional)* CSI Driver Options applied per cluster. |
| `cephConfig`   *map[string]map[string]string* | *(Optional)* Ceph Config options |
| `cephConfigFromSecret`   *map[string]map[string]k8s.io/api/core/v1.SecretKeySelector* | *(Optional)* CephConfigFromSecret works exactly like CephConfig but takes config value from Secret Key reference. |

### ClusterState (`string` alias)

(*Appears on:*[ClusterStatus](index.md#ceph.rook.io/v1.ClusterStatus))

ClusterState represents the state of a Ceph Cluster

| Value | Description |
| --- | --- |
| "Connected" | ClusterStateConnected represents the Connected state of a Ceph Cluster |
| "Connecting" | ClusterStateConnecting represents the Connecting state of a Ceph Cluster |
| "Created" | ClusterStateCreated represents the Created state of a Ceph Cluster |
| "Creating" | ClusterStateCreating represents the Creating state of a Ceph Cluster |
| "Error" | ClusterStateError represents the Error state of a Ceph Cluster |
| "Updating" | ClusterStateUpdating represents the Updating state of a Ceph Cluster |

### ClusterStatus

(*Appears on:*[CephCluster](index.md#ceph.rook.io/v1.CephCluster))

ClusterStatus represents the status of a Ceph cluster

| Field | Description |
| --- | --- |
| `state`   *[ClusterState](index.md#ceph.rook.io/v1.ClusterState)* |  |
| `phase`   *[ConditionType](index.md#ceph.rook.io/v1.ConditionType)* |  |
| `message`   *string* |  |
| `conditions`   *[[]Condition](index.md#ceph.rook.io/v1.Condition)* |  |
| `ceph`   *[CephStatus](index.md#ceph.rook.io/v1.CephStatus)* |  |
| `storage`   *[CephStorage](index.md#ceph.rook.io/v1.CephStorage)* |  |
| `version`   *[ClusterVersion](index.md#ceph.rook.io/v1.ClusterVersion)* |  |
| `observedGeneration`   *int64* | *(Optional)* ObservedGeneration is the latest generation observed by the controller. |

### ClusterVersion

(*Appears on:*[ClusterStatus](index.md#ceph.rook.io/v1.ClusterStatus))

ClusterVersion represents the version of a Ceph Cluster

| Field | Description |
| --- | --- |
| `image`   *string* |  |
| `version`   *string* |  |

### CompressionSpec

(*Appears on:*[ConnectionsSpec](index.md#ceph.rook.io/v1.ConnectionsSpec))

| Field | Description |
| --- | --- |
| `enabled`   *bool* | *(Optional)* Whether to compress the data in transit across the wire. The default is not set. |

### Condition

(*Appears on:*[CephBlockPoolRadosNamespaceStatus](index.md#ceph.rook.io/v1.CephBlockPoolRadosNamespaceStatus), [CephBlockPoolStatus](index.md#ceph.rook.io/v1.CephBlockPoolStatus), [CephFilesystemStatus](index.md#ceph.rook.io/v1.CephFilesystemStatus), [ClusterStatus](index.md#ceph.rook.io/v1.ClusterStatus), [ObjectStoreStatus](index.md#ceph.rook.io/v1.ObjectStoreStatus), [Status](index.md#ceph.rook.io/v1.Status))

Condition represents a status condition on any Rook-Ceph Custom Resource.

| Field | Description |
| --- | --- |
| `type`   *[ConditionType](index.md#ceph.rook.io/v1.ConditionType)* |  |
| `status`   *[Kubernetes core/v1.ConditionStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#conditionstatus-v1-core)* |  |
| `reason`   *[ConditionReason](index.md#ceph.rook.io/v1.ConditionReason)* |  |
| `message`   *string* |  |
| `lastHeartbeatTime`   *[Kubernetes meta/v1.Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#time-v1-meta)* |  |
| `lastTransitionTime`   *[Kubernetes meta/v1.Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#time-v1-meta)* |  |

### ConditionReason (`string` alias)

(*Appears on:*[Condition](index.md#ceph.rook.io/v1.Condition))

ConditionReason is a reason for a condition

| Value | Description |
| --- | --- |
| "ClusterConnected" | ClusterConnectedReason is cluster connected reason |
| "ClusterConnecting" | ClusterConnectingReason is cluster connecting reason |
| "ClusterCreated" | ClusterCreatedReason is cluster created reason |
| "ClusterDeleting" | ClusterDeletingReason is cluster deleting reason |
| "ClusterProgressing" | ClusterProgressingReason is cluster progressing reason |
| "Deleting" | DeletingReason represents when Rook has detected a resource object should be deleted. |
| "ObjectHasDependents" | ObjectHasDependentsReason represents when a resource object has dependents that are blocking deletion. |
| "ObjectHasNoDependents" | ObjectHasNoDependentsReason represents when a resource object has no dependents that are blocking deletion. |
| "PoolEmpty" | PoolEmptyReason represents when a pool does not contain images or snapshots that are blocking deletion. |
| "PoolNotEmpty" | PoolNotEmptyReason represents when a pool contains images or snapshots that are blocking deletion. |
| "RadosNamespaceEmpty" | RadosNamespaceEmptyReason represents when a rados namespace does not contain images or snapshots that are blocking deletion. |
| "RadosNamespaceNotEmpty" | RadosNamespaceNotEmptyReason represents when a rados namespace contains images or snapshots that are blocking deletion. |
| "ReconcileFailed" | ReconcileFailed represents when a resource reconciliation failed. |
| "ReconcileRequeuing" | ReconcileRequeuing represents when a resource reconciliation requeue. |
| "ReconcileStarted" | ReconcileStarted represents when a resource reconciliation started. |
| "ReconcileSucceeded" | ReconcileSucceeded represents when a resource reconciliation was successful. |

### ConditionType (`string` alias)

(*Appears on:*[CephBlockPoolRadosNamespaceStatus](index.md#ceph.rook.io/v1.CephBlockPoolRadosNamespaceStatus), [CephBlockPoolStatus](index.md#ceph.rook.io/v1.CephBlockPoolStatus), [CephClientStatus](index.md#ceph.rook.io/v1.CephClientStatus), [CephFilesystemStatus](index.md#ceph.rook.io/v1.CephFilesystemStatus), [CephFilesystemSubVolumeGroupStatus](index.md#ceph.rook.io/v1.CephFilesystemSubVolumeGroupStatus), [ClusterStatus](index.md#ceph.rook.io/v1.ClusterStatus), [Condition](index.md#ceph.rook.io/v1.Condition), [ObjectStoreStatus](index.md#ceph.rook.io/v1.ObjectStoreStatus))

ConditionType represent a resource’s status

| Value | Description |
| --- | --- |
| "Connected" | ConditionConnected represents Connected state of an object |
| "Connecting" | ConditionConnecting represents Connecting state of an object |
| "Deleting" | ConditionDeleting represents Deleting state of an object |
| "DeletionIsBlocked" | ConditionDeletionIsBlocked represents when deletion of the object is blocked. |
| "Failure" | ConditionFailure represents Failure state of an object |
| "PoolDeletionIsBlocked" | ConditionPoolDeletionIsBlocked represents when deletion of the object is blocked. |
| "Progressing" | ConditionProgressing represents Progressing state of an object |
| "RadosNamespaceDeletionIsBlocked" | ConditionRadosNSDeletionIsBlocked represents when deletion of the object is blocked. |
| "Ready" | ConditionReady represents Ready state of an object |

### ConfigFileVolumeSource

(*Appears on:*[AdditionalVolumeMount](index.md#ceph.rook.io/v1.AdditionalVolumeMount), [KerberosConfigFiles](index.md#ceph.rook.io/v1.KerberosConfigFiles), [KerberosKeytabFile](index.md#ceph.rook.io/v1.KerberosKeytabFile), [SSSDSidecarConfigFile](index.md#ceph.rook.io/v1.SSSDSidecarConfigFile))

Represents the source of a volume to mount. Only one of its members may be specified. This is a subset of the full Kubernetes API’s VolumeSource that is reduced to what is most likely to be useful for mounting config files/dirs into Rook pods.

| Field | Description |
| --- | --- |
| `hostPath`   *[Kubernetes core/v1.HostPathVolumeSource](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#hostpathvolumesource-v1-core)* | *(Optional)* hostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: <https://kubernetes.io/docs/concepts/storage/volumes#hostpath>   --- |
| `emptyDir`   *[Kubernetes core/v1.EmptyDirVolumeSource](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#emptydirvolumesource-v1-core)* | *(Optional)* emptyDir represents a temporary directory that shares a pod’s lifetime. More info: <https://kubernetes.io/docs/concepts/storage/volumes#emptydir> |
| `secret`   *[Kubernetes core/v1.SecretVolumeSource](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#secretvolumesource-v1-core)* | *(Optional)* secret represents a secret that should populate this volume. More info: <https://kubernetes.io/docs/concepts/storage/volumes#secret> |
| `persistentVolumeClaim`   *[Kubernetes core/v1.PersistentVolumeClaimVolumeSource](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#persistentvolumeclaimvolumesource-v1-core)* | *(Optional)* persistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims> |
| `configMap`   *[Kubernetes core/v1.ConfigMapVolumeSource](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#configmapvolumesource-v1-core)* | *(Optional)* configMap represents a configMap that should populate this volume |
| `projected`   *[Kubernetes core/v1.ProjectedVolumeSource](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#projectedvolumesource-v1-core)* | projected items for all in one resources secrets, configmaps, and downward API |

### ConnectionsSpec

(*Appears on:*[NetworkSpec](index.md#ceph.rook.io/v1.NetworkSpec))

| Field | Description |
| --- | --- |
| `encryption`   *[EncryptionSpec](index.md#ceph.rook.io/v1.EncryptionSpec)* | *(Optional)* Encryption settings for the network connections. |
| `compression`   *[CompressionSpec](index.md#ceph.rook.io/v1.CompressionSpec)* | *(Optional)* Compression settings for the network connections. |
| `requireMsgr2`   *bool* | *(Optional)* Whether to require msgr2 (port 3300) even if compression or encryption are not enabled. If true, the msgr1 port (6789) will be disabled. Requires a kernel that supports msgr2 (kernel 5.11 or CentOS 8.4 or newer). |

### CrashCollectorSpec

(*Appears on:*[ClusterSpec](index.md#ceph.rook.io/v1.ClusterSpec))

CrashCollectorSpec represents options to configure the crash controller

| Field | Description |
| --- | --- |
| `disable`   *bool* | *(Optional)* Disable determines whether we should enable the crash collector |
| `daysToRetain`   *uint* | *(Optional)* DaysToRetain represents the number of days to retain crash until they get pruned |

### DaemonHealthSpec

(*Appears on:*[CephClusterHealthCheckSpec](index.md#ceph.rook.io/v1.CephClusterHealthCheckSpec))

DaemonHealthSpec is a daemon health check

| Field | Description |
| --- | --- |
| `status`   *[HealthCheckSpec](index.md#ceph.rook.io/v1.HealthCheckSpec)* | *(Optional)* Status represents the health check settings for the Ceph health |
| `mon`   *[HealthCheckSpec](index.md#ceph.rook.io/v1.HealthCheckSpec)* | *(Optional)* Monitor represents the health check settings for the Ceph monitor |
| `osd`   *[HealthCheckSpec](index.md#ceph.rook.io/v1.HealthCheckSpec)* | *(Optional)* ObjectStorageDaemon represents the health check settings for the Ceph OSDs |

### DashboardSpec

(*Appears on:*[ClusterSpec](index.md#ceph.rook.io/v1.ClusterSpec))

DashboardSpec represents the settings for the Ceph dashboard

| Field | Description |
| --- | --- |
| `enabled`   *bool* | *(Optional)* Enabled determines whether to enable the dashboard |
| `urlPrefix`   *string* | *(Optional)* URLPrefix is a prefix for all URLs to use the dashboard with a reverse proxy |
| `port`   *int* | *(Optional)* Port is the dashboard webserver port |
| `ssl`   *bool* | *(Optional)* SSL determines whether SSL should be used |
| `prometheusEndpoint`   *string* | *(Optional)* Endpoint for the Prometheus host |
| `prometheusEndpointSSLVerify`   *bool* | *(Optional)* Whether to verify the ssl endpoint for prometheus. Set to false for a self-signed cert. |

### Device

(*Appears on:*[Selection](index.md#ceph.rook.io/v1.Selection))

Device represents a disk to use in the cluster

| Field | Description |
| --- | --- |
| `name`   *string* | *(Optional)* |
| `fullpath`   *string* | *(Optional)* |
| `config`   *map[string]string* | *(Optional)* |

### DeviceClasses

(*Appears on:*[CephStorage](index.md#ceph.rook.io/v1.CephStorage))

DeviceClasses represents device classes of a Ceph Cluster

| Field | Description |
| --- | --- |
| `name`   *string* |  |

### DisruptionManagementSpec

(*Appears on:*[ClusterSpec](index.md#ceph.rook.io/v1.ClusterSpec))

DisruptionManagementSpec configures management of daemon disruptions

| Field | Description |
| --- | --- |
| `managePodBudgets`   *bool* | *(Optional)* This enables management of poddisruptionbudgets |
| `osdMaintenanceTimeout`   *time.Duration* | *(Optional)* OSDMaintenanceTimeout sets how many additional minutes the DOWN/OUT interval is for drained failure domains it only works if managePodBudgets is true. the default is 30 minutes |
| `pgHealthCheckTimeout`   *time.Duration* | *(Optional)* DEPRECATED: PGHealthCheckTimeout is no longer implemented |
| `pgHealthyRegex`   *string* | *(Optional)* PgHealthyRegex is the regular expression that is used to determine which PG states should be considered healthy. The default is `^(active\+clean|active\+clean\+scrubbing|active\+clean\+scrubbing\+deep)$` |
| `manageMachineDisruptionBudgets`   *bool* | *(Optional)* Deprecated. This enables management of machinedisruptionbudgets. |
| `machineDisruptionBudgetNamespace`   *string* | *(Optional)* Deprecated. Namespace to look for MDBs by the machineDisruptionBudgetController |

### EncryptionSpec

(*Appears on:*[ConnectionsSpec](index.md#ceph.rook.io/v1.ConnectionsSpec))

| Field | Description |
| --- | --- |
| `enabled`   *bool* | *(Optional)* Whether to encrypt the data in transit across the wire to prevent eavesdropping the data on the network. The default is not set. Even if encryption is not enabled, clients still establish a strong initial authentication for the connection and data integrity is still validated with a crc check. When encryption is enabled, all communication between clients and Ceph daemons, or between Ceph daemons will be encrypted. |

### EndpointAddress

(*Appears on:*[GatewaySpec](index.md#ceph.rook.io/v1.GatewaySpec))

EndpointAddress is a tuple that describes a single IP address or host name. This is a subset of Kubernetes’s v1.EndpointAddress.

| Field | Description |
| --- | --- |
| `ip`   *string* | *(Optional)* The IP of this endpoint. As a legacy behavior, this supports being given a DNS-addressable hostname as well. |
| `hostname`   *string* | *(Optional)* The DNS-addressable Hostname of this endpoint. This field will be preferred over IP if both are given. |

### ErasureCodedSpec

(*Appears on:*[PoolSpec](index.md#ceph.rook.io/v1.PoolSpec))

ErasureCodedSpec represents the spec for erasure code in a pool

| Field | Description |
| --- | --- |
| `codingChunks`   *uint* | Number of coding chunks per object in an erasure coded storage pool (required for erasure-coded pool type). This is the number of OSDs that can be lost simultaneously before data cannot be recovered. |
| `dataChunks`   *uint* | Number of data chunks per object in an erasure coded storage pool (required for erasure-coded pool type). The number of chunks required to recover an object when any single OSD is lost is the same as dataChunks so be aware that the larger the number of data chunks, the higher the cost of recovery. |
| `algorithm`   *string* | *(Optional)* The algorithm for erasure coding. If absent, defaults to the plugin specified in osd_pool_default_erasure_code_profile. |

### ExternalSpec

(*Appears on:*[ClusterSpec](index.md#ceph.rook.io/v1.ClusterSpec))

ExternalSpec represents the options supported by an external cluster

| Field | Description |
| --- | --- |
| `enable`   *bool* | *(Optional)* Enable determines whether external mode is enabled or not |

### FSMirroringSpec

(*Appears on:*[FilesystemSpec](index.md#ceph.rook.io/v1.FilesystemSpec))

FSMirroringSpec represents the setting for a mirrored filesystem

| Field | Description |
| --- | --- |
| `enabled`   *bool* | *(Optional)* Enabled whether this filesystem is mirrored or not |
| `peers`   *[MirroringPeerSpec](index.md#ceph.rook.io/v1.MirroringPeerSpec)* | *(Optional)* Peers represents the peers spec |
| `snapshotSchedules`   *[[]SnapshotScheduleSpec](index.md#ceph.rook.io/v1.SnapshotScheduleSpec)* | *(Optional)* SnapshotSchedules is the scheduling of snapshot for mirrored filesystems |
| `snapshotRetention`   *[[]SnapshotScheduleRetentionSpec](index.md#ceph.rook.io/v1.SnapshotScheduleRetentionSpec)* | *(Optional)* Retention is the retention policy for a snapshot schedule One path has exactly one retention policy. A policy can however contain multiple count-time period pairs in order to specify complex retention policies |

### FilesystemMirrorInfoPeerSpec

(*Appears on:*[FilesystemsSpec](index.md#ceph.rook.io/v1.FilesystemsSpec))

FilesystemMirrorInfoPeerSpec is the specification of a filesystem peer mirror

| Field | Description |
| --- | --- |
| `uuid`   *string* | *(Optional)* UUID is the peer unique identifier |
| `remote`   *[PeerRemoteSpec](index.md#ceph.rook.io/v1.PeerRemoteSpec)* | *(Optional)* Remote are the remote cluster information |
| `stats`   *[PeerStatSpec](index.md#ceph.rook.io/v1.PeerStatSpec)* | *(Optional)* Stats are the stat a peer mirror |

### FilesystemMirroringInfo

(*Appears on:*[FilesystemMirroringInfoSpec](index.md#ceph.rook.io/v1.FilesystemMirroringInfoSpec))

FilesystemMirrorInfoSpec is the filesystem mirror status of a given filesystem

| Field | Description |
| --- | --- |
| `daemon_id`   *int* | *(Optional)* DaemonID is the cephfs-mirror name |
| `filesystems`   *[[]FilesystemsSpec](index.md#ceph.rook.io/v1.FilesystemsSpec)* | *(Optional)* Filesystems is the list of filesystems managed by a given cephfs-mirror daemon |

### FilesystemMirroringInfoSpec

(*Appears on:*[CephFilesystemStatus](index.md#ceph.rook.io/v1.CephFilesystemStatus))

FilesystemMirroringInfo is the status of the pool mirroring

| Field | Description |
| --- | --- |
| `daemonsStatus`   *[[]FilesystemMirroringInfo](index.md#ceph.rook.io/v1.FilesystemMirroringInfo)* | *(Optional)* PoolMirroringStatus is the mirroring status of a filesystem |
| `lastChecked`   *string* | *(Optional)* LastChecked is the last time time the status was checked |
| `lastChanged`   *string* | *(Optional)* LastChanged is the last time time the status last changed |
| `details`   *string* | *(Optional)* Details contains potential status errors |

### FilesystemMirroringSpec

(*Appears on:*[CephFilesystemMirror](index.md#ceph.rook.io/v1.CephFilesystemMirror))

FilesystemMirroringSpec is the filesystem mirroring specification

| Field | Description |
| --- | --- |
| `placement`   *[Placement](index.md#ceph.rook.io/v1.Placement)* | *(Optional)* The affinity to place the rgw pods (default is to place on any available node) |
| `annotations`   *[Annotations](index.md#ceph.rook.io/v1.Annotations)* | *(Optional)* The annotations-related configuration to add/set on each Pod related object. |
| `labels`   *[Labels](index.md#ceph.rook.io/v1.Labels)* | *(Optional)* The labels-related configuration to add/set on each Pod related object. |
| `resources`   *[Kubernetes core/v1.ResourceRequirements](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#resourcerequirements-v1-core)* | *(Optional)* The resource requirements for the cephfs-mirror pods |
| `priorityClassName`   *string* | *(Optional)* PriorityClassName sets priority class on the cephfs-mirror pods |

### FilesystemSnapshotScheduleStatusRetention

(*Appears on:*[FilesystemSnapshotSchedulesSpec](index.md#ceph.rook.io/v1.FilesystemSnapshotSchedulesSpec))

FilesystemSnapshotScheduleStatusRetention is the retention specification for a filesystem snapshot schedule

| Field | Description |
| --- | --- |
| `start`   *string* | *(Optional)* Start is when the snapshot schedule starts |
| `created`   *string* | *(Optional)* Created is when the snapshot schedule was created |
| `first`   *string* | *(Optional)* First is when the first snapshot schedule was taken |
| `last`   *string* | *(Optional)* Last is when the last snapshot schedule was taken |
| `last_pruned`   *string* | *(Optional)* LastPruned is when the last snapshot schedule was pruned |
| `created_count`   *int* | *(Optional)* CreatedCount is total amount of snapshots |
| `pruned_count`   *int* | *(Optional)* PrunedCount is total amount of pruned snapshots |
| `active`   *bool* | *(Optional)* Active is whether the scheduled is active or not |

### FilesystemSnapshotScheduleStatusSpec

(*Appears on:*[CephFilesystemStatus](index.md#ceph.rook.io/v1.CephFilesystemStatus))

FilesystemSnapshotScheduleStatusSpec is the status of the snapshot schedule

| Field | Description |
| --- | --- |
| `snapshotSchedules`   *[[]FilesystemSnapshotSchedulesSpec](index.md#ceph.rook.io/v1.FilesystemSnapshotSchedulesSpec)* | *(Optional)* SnapshotSchedules is the list of snapshots scheduled |
| `lastChecked`   *string* | *(Optional)* LastChecked is the last time time the status was checked |
| `lastChanged`   *string* | *(Optional)* LastChanged is the last time time the status last changed |
| `details`   *string* | *(Optional)* Details contains potential status errors |

### FilesystemSnapshotSchedulesSpec

(*Appears on:*[FilesystemSnapshotScheduleStatusSpec](index.md#ceph.rook.io/v1.FilesystemSnapshotScheduleStatusSpec))

FilesystemSnapshotSchedulesSpec is the list of snapshot scheduled for images in a pool

| Field | Description |
| --- | --- |
| `fs`   *string* | *(Optional)* Fs is the name of the Ceph Filesystem |
| `subvol`   *string* | *(Optional)* Subvol is the name of the sub volume |
| `path`   *string* | *(Optional)* Path is the path on the filesystem |
| `rel_path`   *string* | *(Optional)* |
| `schedule`   *string* | *(Optional)* |
| `retention`   *[FilesystemSnapshotScheduleStatusRetention](index.md#ceph.rook.io/v1.FilesystemSnapshotScheduleStatusRetention)* | *(Optional)* |

### FilesystemSpec

(*Appears on:*[CephFilesystem](index.md#ceph.rook.io/v1.CephFilesystem))

FilesystemSpec represents the spec of a file system

| Field | Description |
| --- | --- |
| `metadataPool`   *[NamedPoolSpec](index.md#ceph.rook.io/v1.NamedPoolSpec)* | The metadata pool settings |
| `dataPools`   *[[]NamedPoolSpec](index.md#ceph.rook.io/v1.NamedPoolSpec)* | The data pool settings, with optional predefined pool name. |
| `preservePoolNames`   *bool* | *(Optional)* Preserve pool names as specified |
| `preservePoolsOnDelete`   *bool* | *(Optional)* Preserve pools on filesystem deletion |
| `preserveFilesystemOnDelete`   *bool* | *(Optional)* Preserve the fs in the cluster on CephFilesystem CR deletion. Setting this to true automatically implies PreservePoolsOnDelete is true. |
| `metadataServer`   *[MetadataServerSpec](index.md#ceph.rook.io/v1.MetadataServerSpec)* | The mds pod info |
| `mirroring`   *[FSMirroringSpec](index.md#ceph.rook.io/v1.FSMirroringSpec)* | *(Optional)* The mirroring settings |
| `statusCheck`   *[MirrorHealthCheckSpec](index.md#ceph.rook.io/v1.MirrorHealthCheckSpec)* | The mirroring statusCheck |

### FilesystemsSpec

(*Appears on:*[FilesystemMirroringInfo](index.md#ceph.rook.io/v1.FilesystemMirroringInfo))

FilesystemsSpec is spec for the mirrored filesystem

| Field | Description |
| --- | --- |
| `filesystem_id`   *int* | *(Optional)* FilesystemID is the filesystem identifier |
| `name`   *string* | *(Optional)* Name is name of the filesystem |
| `directory_count`   *int* | *(Optional)* DirectoryCount is the number of directories in the filesystem |
| `peers`   *[[]FilesystemMirrorInfoPeerSpec](index.md#ceph.rook.io/v1.FilesystemMirrorInfoPeerSpec)* | *(Optional)* Peers represents the mirroring peers |

### GaneshaRADOSSpec

(*Appears on:*[NFSGaneshaSpec](index.md#ceph.rook.io/v1.NFSGaneshaSpec))

GaneshaRADOSSpec represents the specification of a Ganesha RADOS object

| Field | Description |
| --- | --- |
| `pool`   *string* | *(Optional)* The Ceph pool used store the shared configuration for NFS-Ganesha daemons. This setting is deprecated, as it is internally required to be “.nfs”. |
| `namespace`   *string* | *(Optional)* The namespace inside the Ceph pool (set by ‘pool’) where shared NFS-Ganesha config is stored. This setting is deprecated as it is internally set to the name of the CephNFS. |

### GaneshaServerSpec

(*Appears on:*[NFSGaneshaSpec](index.md#ceph.rook.io/v1.NFSGaneshaSpec))

GaneshaServerSpec represents the specification of a Ganesha Server

| Field | Description |
| --- | --- |
| `active`   *int* | The number of active Ganesha servers |
| `placement`   *[Placement](index.md#ceph.rook.io/v1.Placement)* | *(Optional)* The affinity to place the ganesha pods |
| `annotations`   *[Annotations](index.md#ceph.rook.io/v1.Annotations)* | *(Optional)* The annotations-related configuration to add/set on each Pod related object. |
| `labels`   *[Labels](index.md#ceph.rook.io/v1.Labels)* | *(Optional)* The labels-related configuration to add/set on each Pod related object. |
| `resources`   *[Kubernetes core/v1.ResourceRequirements](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#resourcerequirements-v1-core)* | *(Optional)* Resources set resource requests and limits |
| `priorityClassName`   *string* | *(Optional)* PriorityClassName sets the priority class on the pods |
| `logLevel`   *string* | *(Optional)* LogLevel set logging level |
| `hostNetwork`   *bool* | *(Optional)* Whether host networking is enabled for the Ganesha server. If not set, the network settings from the cluster CR will be applied. |
| `livenessProbe`   *[ProbeSpec](index.md#ceph.rook.io/v1.ProbeSpec)* | *(Optional)* A liveness-probe to verify that Ganesha server has valid run-time state. If LivenessProbe.Disabled is false and LivenessProbe.Probe is nil uses default probe. |

### GatewaySpec

(*Appears on:*[ObjectStoreSpec](index.md#ceph.rook.io/v1.ObjectStoreSpec))

GatewaySpec represents the specification of Ceph Object Store Gateway

| Field | Description |
| --- | --- |
| `port`   *int32* | *(Optional)* The port the rgw service will be listening on (http) |
| `securePort`   *int32* | *(Optional)* The port the rgw service will be listening on (https) |
| `instances`   *int32* | *(Optional)* The number of pods in the rgw replicaset. |
| `sslCertificateRef`   *string* | *(Optional)* The name of the secret that stores the ssl certificate for secure rgw connections |
| `caBundleRef`   *string* | *(Optional)* The name of the secret that stores custom ca-bundle with root and intermediate certificates. |
| `placement`   *[Placement](index.md#ceph.rook.io/v1.Placement)* | *(Optional)* The affinity to place the rgw pods (default is to place on any available node) |
| `disableMultisiteSyncTraffic`   *bool* | *(Optional)* DisableMultisiteSyncTraffic, when true, prevents this object store’s gateways from transmitting multisite replication data. Note that this value does not affect whether gateways receive multisite replication traffic: see ObjectZone.spec.customEndpoints for that. If false or unset, this object store’s gateways will be able to transmit multisite replication data. |
| `annotations`   *[Annotations](index.md#ceph.rook.io/v1.Annotations)* | *(Optional)* The annotations-related configuration to add/set on each Pod related object. |
| `labels`   *[Labels](index.md#ceph.rook.io/v1.Labels)* | *(Optional)* The labels-related configuration to add/set on each Pod related object. |
| `resources`   *[Kubernetes core/v1.ResourceRequirements](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#resourcerequirements-v1-core)* | *(Optional)* The resource requirements for the rgw pods |
| `priorityClassName`   *string* | *(Optional)* PriorityClassName sets priority classes on the rgw pods |
| `externalRgwEndpoints`   *[[]EndpointAddress](index.md#ceph.rook.io/v1.EndpointAddress)* | *(Optional)* ExternalRgwEndpoints points to external RGW endpoint(s). Multiple endpoints can be given, but for stability of ObjectBucketClaims, we highly recommend that users give only a single external RGW endpoint that is a load balancer that sends requests to the multiple RGWs. |
| `service`   *[RGWServiceSpec](index.md#ceph.rook.io/v1.RGWServiceSpec)* | *(Optional)* The configuration related to add/set on each rgw service. |
| `opsLogSidecar`   *[OpsLogSidecar](index.md#ceph.rook.io/v1.OpsLogSidecar)* | *(Optional)* Enable enhanced operation Logs for S3 in a sidecar named ops-log |
| `hostNetwork`   *bool* | *(Optional)* Whether host networking is enabled for the rgw daemon. If not set, the network settings from the cluster CR will be applied. |
| `dashboardEnabled`   *bool* | *(Optional)* Whether rgw dashboard is enabled for the rgw daemon. If not set, the rgw dashboard will be enabled. |
| `additionalVolumeMounts`   *[AdditionalVolumeMounts](index.md#ceph.rook.io/v1.AdditionalVolumeMounts)* | AdditionalVolumeMounts allows additional volumes to be mounted to the RGW pod. The root directory for each additional volume mount is `/var/rgw`. Example: for an additional mount at subPath `ldap`, mounted from a secret that has key `bindpass.secret`, the file would reside at `/var/rgw/ldap/bindpass.secret`. |
| `rgwConfig`   *map[string]string* | *(Optional)* RgwConfig sets Ceph RGW config values for the gateway clients that serve this object store. Values are modified at runtime without RGW restart. This feature is intended for advanced users. It allows breaking configurations to be easily applied. Use with caution. |
| `rgwConfigFromSecret`   *[map[string]k8s.io/api/core/v1.SecretKeySelector](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#secretkeyselector-v1-core)* | *(Optional)* RgwConfigFromSecret works exactly like RgwConfig but takes config value from Secret Key reference. Values are modified at runtime without RGW restart. This feature is intended for advanced users. It allows breaking configurations to be easily applied. Use with caution. |
| `rgwCommandFlags`   *map[string]string* | *(Optional)* RgwCommandFlags sets Ceph RGW config values for the gateway clients that serve this object store. Values are modified at RGW startup, resulting in RGW pod restarts. This feature is intended for advanced users. It allows breaking configurations to be easily applied. Use with caution. |
| `readAffinity`   *[RgwReadAffinity](index.md#ceph.rook.io/v1.RgwReadAffinity)* | *(Optional)* ReadAffinity defines the RGW read affinity policy to optimize the read requests for the RGW clients Note: Only supported from Ceph Tentacle (v20) |

### HTTPEndpointSpec

(*Appears on:*[TopicEndpointSpec](index.md#ceph.rook.io/v1.TopicEndpointSpec))

HTTPEndpointSpec represent the spec of an HTTP endpoint of a Bucket Topic

| Field | Description |
| --- | --- |
| `uri`   *string* | The URI of the HTTP endpoint to push notification to |
| `disableVerifySSL`   *bool* | *(Optional)* Indicate whether the server certificate is validated by the client or not |
| `sendCloudEvents`   *bool* | *(Optional)* Send the notifications with the CloudEvents header: <https://github.com/cloudevents/spec/blob/main/cloudevents/adapters/aws-s3.md> |

### HealthCheckSpec

(*Appears on:*[DaemonHealthSpec](index.md#ceph.rook.io/v1.DaemonHealthSpec), [MirrorHealthCheckSpec](index.md#ceph.rook.io/v1.MirrorHealthCheckSpec))

HealthCheckSpec represents the health check of an object store bucket

| Field | Description |
| --- | --- |
| `disabled`   *bool* | *(Optional)* |
| `interval`   *[Kubernetes meta/v1.Duration](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration)* | *(Optional)* Interval is the internal in second or minute for the health check to run like 60s for 60 seconds |
| `timeout`   *string* | *(Optional)* |

### HybridStorageSpec

(*Appears on:*[ReplicatedSpec](index.md#ceph.rook.io/v1.ReplicatedSpec))

HybridStorageSpec represents the settings for hybrid storage pool

| Field | Description |
| --- | --- |
| `primaryDeviceClass`   *string* | PrimaryDeviceClass represents high performance tier (for example SSD or NVME) for Primary OSD |
| `secondaryDeviceClass`   *string* | SecondaryDeviceClass represents low performance tier (for example HDDs) for remaining OSDs |

### IPFamilyType (`string` alias)

(*Appears on:*[NetworkSpec](index.md#ceph.rook.io/v1.NetworkSpec))

IPFamilyType represents the single stack Ipv4 or Ipv6 protocol.

| Value | Description |
| --- | --- |
| "IPv4" | IPv4 internet protocol version |
| "IPv6" | IPv6 internet protocol version |

### ImplicitTenantSetting (`string` alias)

(*Appears on:*[KeystoneSpec](index.md#ceph.rook.io/v1.KeystoneSpec))

| Value | Description |
| --- | --- |
| "" |  |
| "false" |  |
| "s3" |  |
| "swift" |  |
| "true" |  |

### KafkaEndpointSpec

(*Appears on:*[TopicEndpointSpec](index.md#ceph.rook.io/v1.TopicEndpointSpec))

KafkaEndpointSpec represent the spec of a Kafka endpoint of a Bucket Topic

| Field | Description |
| --- | --- |
| `uri`   *string* | The URI of the Kafka endpoint to push notification to |
| `useSSL`   *bool* | *(Optional)* Indicate whether to use SSL when communicating with the broker |
| `disableVerifySSL`   *bool* | *(Optional)* Indicate whether the server certificate is validated by the client or not |
| `ackLevel`   *string* | *(Optional)* The ack level required for this topic (none/broker) |
| `mechanism`   *string* | *(Optional)* The authentication mechanism for this topic (PLAIN/SCRAM-SHA-512/SCRAM-SHA-256/GSSAPI/OAUTHBEARER) |
| `userSecretRef`   *[Kubernetes core/v1.SecretKeySelector](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#secretkeyselector-v1-core)* | *(Optional)* The kafka user name to use for authentication |
| `passwordSecretRef`   *[Kubernetes core/v1.SecretKeySelector](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#secretkeyselector-v1-core)* | *(Optional)* The kafka password to use for authentication |

### KerberosConfigFiles

(*Appears on:*[KerberosSpec](index.md#ceph.rook.io/v1.KerberosSpec))

KerberosConfigFiles represents the source(s) from which Kerberos configuration should come.

| Field | Description |
| --- | --- |
| `volumeSource`   *[ConfigFileVolumeSource](index.md#ceph.rook.io/v1.ConfigFileVolumeSource)* | VolumeSource accepts a pared down version of the standard Kubernetes VolumeSource for Kerberos configuration files like what is normally used to configure Volumes for a Pod. For example, a ConfigMap, Secret, or HostPath. The volume may contain multiple files, all of which will be loaded. |

### KerberosKeytabFile

(*Appears on:*[KerberosSpec](index.md#ceph.rook.io/v1.KerberosSpec))

KerberosKeytabFile represents the source(s) from which the Kerberos keytab file should come.

| Field | Description |
| --- | --- |
| `volumeSource`   *[ConfigFileVolumeSource](index.md#ceph.rook.io/v1.ConfigFileVolumeSource)* | VolumeSource accepts a pared down version of the standard Kubernetes VolumeSource for the Kerberos keytab file like what is normally used to configure Volumes for a Pod. For example, a Secret or HostPath. There are two requirements for the source’s content: 1. The config file must be mountable via `subPath: krb5.keytab`. For example, in a Secret, the data item must be named `krb5.keytab`, or `items` must be defined to select the key and give it path `krb5.keytab`. A HostPath directory must have the `krb5.keytab` file. 2. The volume or config file must have mode 0600. |

### KerberosSpec

(*Appears on:*[NFSSecuritySpec](index.md#ceph.rook.io/v1.NFSSecuritySpec))

KerberosSpec represents configuration for Kerberos.

| Field | Description |
| --- | --- |
| `principalName`   *string* | *(Optional)* PrincipalName corresponds directly to NFS-Ganesha’s NFS_KRB5:PrincipalName config. In practice, this is the service prefix of the principal name. The default is “nfs”. This value is combined with (a) the namespace and name of the CephNFS (with a hyphen between) and (b) the Realm configured in the user-provided krb5.conf to determine the full principal name: /-@. e.g., nfs/rook-ceph-my-nfs@example.net. See <https://github.com/nfs-ganesha/nfs-ganesha/wiki/RPCSEC_GSS> for more detail. |
| `domainName`   *string* | *(Optional)* DomainName should be set to the Kerberos Realm. |
| `configFiles`   *[KerberosConfigFiles](index.md#ceph.rook.io/v1.KerberosConfigFiles)* | *(Optional)* ConfigFiles defines where the Kerberos configuration should be sourced from. Config files will be placed into the `/etc/krb5.conf.rook/` directory.  If this is left empty, Rook will not add any files. This allows you to manage the files yourself however you wish. For example, you may build them into your custom Ceph container image or use the Vault agent injector to securely add the files via annotations on the CephNFS spec (passed to the NFS server pods).  Rook configures Kerberos to log to stderr. We suggest removing logging sections from config files to avoid consuming unnecessary disk space from logging to files. |
| `keytabFile`   *[KerberosKeytabFile](index.md#ceph.rook.io/v1.KerberosKeytabFile)* | *(Optional)* KeytabFile defines where the Kerberos keytab should be sourced from. The keytab file will be placed into `/etc/krb5.keytab`. If this is left empty, Rook will not add the file. This allows you to manage the `krb5.keytab` file yourself however you wish. For example, you may build it into your custom Ceph container image or use the Vault agent injector to securely add the file via annotations on the CephNFS spec (passed to the NFS server pods). |

### KeyManagementServiceSpec

(*Appears on:*[ObjectStoreSecuritySpec](index.md#ceph.rook.io/v1.ObjectStoreSecuritySpec), [SecuritySpec](index.md#ceph.rook.io/v1.SecuritySpec))

KeyManagementServiceSpec represent various details of the KMS server

| Field | Description |
| --- | --- |
| `connectionDetails`   *map[string]string* | *(Optional)* ConnectionDetails contains the KMS connection details (address, port etc) |
| `tokenSecretName`   *string* | *(Optional)* TokenSecretName is the kubernetes secret containing the KMS token |

### KeyRotationSpec

(*Appears on:*[SecuritySpec](index.md#ceph.rook.io/v1.SecuritySpec))

KeyRotationSpec represents the settings for Key Rotation.

| Field | Description |
| --- | --- |
| `enabled`   *bool* | *(Optional)* Enabled represents whether the key rotation is enabled. |
| `schedule`   *string* | *(Optional)* Schedule represents the cron schedule for key rotation. |

### KeyType (`string` alias)

KeyType type safety

| Value | Description |
| --- | --- |
| "exporter" |  |
| "cleanup" |  |
| "clusterMetadata" |  |
| "cmdreporter" |  |
| "crashcollector" |  |
| "dashboard" |  |
| "mds" |  |
| "mgr" |  |
| "mon" |  |
| "arbiter" |  |
| "monitoring" |  |
| "osd" |  |
| "prepareosd" |  |
| "rgw" |  |
| "keyrotation" |  |

### KeystoneSpec

(*Appears on:*[AuthSpec](index.md#ceph.rook.io/v1.AuthSpec))

KeystoneSpec represents the Keystone authentication configuration of a Ceph Object Store Gateway

| Field | Description |
| --- | --- |
| `url`   *string* | The URL for the Keystone server. |
| `serviceUserSecretName`   *string* | The name of the secret containing the credentials for the service user account used by RGW. It has to be in the same namespace as the object store resource. |
| `acceptedRoles`   *[]string* | The roles requires to serve requests. |
| `implicitTenants`   *[ImplicitTenantSetting](index.md#ceph.rook.io/v1.ImplicitTenantSetting)* | *(Optional)* Create new users in their own tenants of the same name. Possible values are true, false, swift and s3. The latter have the effect of splitting the identity space such that only the indicated protocol will use implicit tenants. |
| `tokenCacheSize`   *int* | *(Optional)* The maximum number of entries in each Keystone token cache. |
| `revocationInterval`   *int* | *(Optional)* The number of seconds between token revocation checks. |

### Labels (`map[string]string` alias)

(*Appears on:*[FilesystemMirroringSpec](index.md#ceph.rook.io/v1.FilesystemMirroringSpec), [GaneshaServerSpec](index.md#ceph.rook.io/v1.GaneshaServerSpec), [GatewaySpec](index.md#ceph.rook.io/v1.GatewaySpec), [MetadataServerSpec](index.md#ceph.rook.io/v1.MetadataServerSpec), [RBDMirroringSpec](index.md#ceph.rook.io/v1.RBDMirroringSpec))

Labels are label for a given daemons

### LabelsSpec (`map[github.com/rook/rook/pkg/apis/ceph.rook.io/v1.KeyType]github.com/rook/rook/pkg/apis/ceph.rook.io/v1.Labels` alias)

(*Appears on:*[ClusterSpec](index.md#ceph.rook.io/v1.ClusterSpec))

LabelsSpec is the main spec label for all daemons

### LogCollectorSpec

(*Appears on:*[ClusterSpec](index.md#ceph.rook.io/v1.ClusterSpec))

LogCollectorSpec is the logging spec

| Field | Description |
| --- | --- |
| `enabled`   *bool* | *(Optional)* Enabled represents whether the log collector is enabled |
| `periodicity`   *string* | *(Optional)* Periodicity is the periodicity of the log rotation. |
| `maxLogSize`   *k8s.io/apimachinery/pkg/api/resource.Quantity* | *(Optional)* MaxLogSize is the maximum size of the log per ceph daemons. Must be at least 1M. |

### MetadataServerSpec

(*Appears on:*[FilesystemSpec](index.md#ceph.rook.io/v1.FilesystemSpec))

MetadataServerSpec represents the specification of a Ceph Metadata Server

| Field | Description |
| --- | --- |
| `activeCount`   *int32* | The number of metadata servers that are active. The remaining servers in the cluster will be in standby mode. |
| `activeStandby`   *bool* | *(Optional)* Whether each active MDS instance will have an active standby with a warm metadata cache for faster failover. If false, standbys will still be available, but will not have a warm metadata cache. |
| `placement`   *[Placement](index.md#ceph.rook.io/v1.Placement)* | *(Optional)* The affinity to place the mds pods (default is to place on all available node) with a daemonset |
| `annotations`   *[Annotations](index.md#ceph.rook.io/v1.Annotations)* | *(Optional)* The annotations-related configuration to add/set on each Pod related object. |
| `labels`   *[Labels](index.md#ceph.rook.io/v1.Labels)* | *(Optional)* The labels-related configuration to add/set on each Pod related object. |
| `resources`   *[Kubernetes core/v1.ResourceRequirements](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#resourcerequirements-v1-core)* | *(Optional)* The resource requirements for the mds pods |
| `priorityClassName`   *string* | *(Optional)* PriorityClassName sets priority classes on components |
| `livenessProbe`   *[ProbeSpec](index.md#ceph.rook.io/v1.ProbeSpec)* | *(Optional)* |
| `startupProbe`   *[ProbeSpec](index.md#ceph.rook.io/v1.ProbeSpec)* | *(Optional)* |

### MgrSpec

(*Appears on:*[ClusterSpec](index.md#ceph.rook.io/v1.ClusterSpec))

MgrSpec represents options to configure a ceph mgr

| Field | Description |
| --- | --- |
| `count`   *int* | *(Optional)* Count is the number of manager daemons to run |
| `allowMultiplePerNode`   *bool* | *(Optional)* AllowMultiplePerNode allows to run multiple managers on the same node (not recommended) |
| `modules`   *[[]Module](index.md#ceph.rook.io/v1.Module)* | *(Optional)* Modules is the list of ceph manager modules to enable/disable |

### Migration

(*Appears on:*[StorageScopeSpec](index.md#ceph.rook.io/v1.StorageScopeSpec))

Migration handles the OSD migration

| Field | Description |
| --- | --- |
| `confirmation`   *string* | *(Optional)* A user confirmation to migrate the OSDs. It destroys each OSD one at a time, cleans up the backing disk and prepares OSD with same ID on that disk |

### MigrationStatus

(*Appears on:*[OSDStatus](index.md#ceph.rook.io/v1.OSDStatus))

MigrationStatus status represents the current status of any OSD migration.

| Field | Description |
| --- | --- |
| `pending`   *int* |  |

### MirrorHealthCheckSpec

(*Appears on:*[FilesystemSpec](index.md#ceph.rook.io/v1.FilesystemSpec), [PoolSpec](index.md#ceph.rook.io/v1.PoolSpec))

MirrorHealthCheckSpec represents the health specification of a Ceph Storage Pool mirror

| Field | Description |
| --- | --- |
| `mirror`   *[HealthCheckSpec](index.md#ceph.rook.io/v1.HealthCheckSpec)* | *(Optional)* |

### MirroringInfo

(*Appears on:*[MirroringInfoSpec](index.md#ceph.rook.io/v1.MirroringInfoSpec))

MirroringInfo is the mirroring info of a given pool/radosnamespace

| Field | Description |
| --- | --- |
| `mode`   *string* | *(Optional)* Mode is the mirroring mode |
| `site_name`   *string* | *(Optional)* SiteName is the current site name |
| `peers`   *[[]PeersSpec](index.md#ceph.rook.io/v1.PeersSpec)* | *(Optional)* Peers are the list of peer sites connected to that cluster |

### MirroringInfoSpec

(*Appears on:*[CephBlockPoolRadosNamespaceStatus](index.md#ceph.rook.io/v1.CephBlockPoolRadosNamespaceStatus), [CephBlockPoolStatus](index.md#ceph.rook.io/v1.CephBlockPoolStatus))

MirroringInfoSpec is the status of the pool/radosnamespace mirroring

| Field | Description |
| --- | --- |
| `MirroringInfo`   *[MirroringInfo](index.md#ceph.rook.io/v1.MirroringInfo)* | (Members of `MirroringInfo` are embedded into this type.) *(Optional)* |
| `lastChecked`   *string* | *(Optional)* |
| `lastChanged`   *string* | *(Optional)* |
| `details`   *string* | *(Optional)* |

### MirroringPeerSpec

(*Appears on:*[FSMirroringSpec](index.md#ceph.rook.io/v1.FSMirroringSpec), [MirroringSpec](index.md#ceph.rook.io/v1.MirroringSpec), [RBDMirroringSpec](index.md#ceph.rook.io/v1.RBDMirroringSpec))

MirroringPeerSpec represents the specification of a mirror peer

| Field | Description |
| --- | --- |
| `secretNames`   *[]string* | *(Optional)* SecretNames represents the Kubernetes Secret names to add rbd-mirror or cephfs-mirror peers |

### MirroringSpec

(*Appears on:*[PoolSpec](index.md#ceph.rook.io/v1.PoolSpec))

MirroringSpec represents the setting for a mirrored pool

| Field | Description |
| --- | --- |
| `enabled`   *bool* | *(Optional)* Enabled whether this pool is mirrored or not |
| `mode`   *string* | *(Optional)* Mode is the mirroring mode: pool, image or init-only. |
| `snapshotSchedules`   *[[]SnapshotScheduleSpec](index.md#ceph.rook.io/v1.SnapshotScheduleSpec)* | *(Optional)* SnapshotSchedules is the scheduling of snapshot for mirrored images/pools |
| `peers`   *[MirroringPeerSpec](index.md#ceph.rook.io/v1.MirroringPeerSpec)* | *(Optional)* Peers represents the peers spec |

### MirroringStatus

(*Appears on:*[MirroringStatusSpec](index.md#ceph.rook.io/v1.MirroringStatusSpec))

MirroringStatus is the pool/radosNamespace mirror status

| Field | Description |
| --- | --- |
| `summary`   *[MirroringStatusSummarySpec](index.md#ceph.rook.io/v1.MirroringStatusSummarySpec)* | *(Optional)* Summary is the mirroring status summary |

### MirroringStatusSpec

(*Appears on:*[CephBlockPoolRadosNamespaceStatus](index.md#ceph.rook.io/v1.CephBlockPoolRadosNamespaceStatus), [CephBlockPoolStatus](index.md#ceph.rook.io/v1.CephBlockPoolStatus))

MirroringStatusSpec is the status of the pool/radosNamespace mirroring

| Field | Description |
| --- | --- |
| `MirroringStatus`   *[MirroringStatus](index.md#ceph.rook.io/v1.MirroringStatus)* | (Members of `MirroringStatus` are embedded into this type.) *(Optional)* MirroringStatus is the mirroring status of a pool/radosNamespace |
| `lastChecked`   *string* | *(Optional)* LastChecked is the last time time the status was checked |
| `lastChanged`   *string* | *(Optional)* LastChanged is the last time time the status last changed |
| `details`   *string* | *(Optional)* Details contains potential status errors |

### MirroringStatusSummarySpec

(*Appears on:*[MirroringStatus](index.md#ceph.rook.io/v1.MirroringStatus))

MirroringStatusSummarySpec is the summary output of the command

| Field | Description |
| --- | --- |
| `health`   *string* | *(Optional)* Health is the mirroring health |
| `daemon_health`   *string* | *(Optional)* DaemonHealth is the health of the mirroring daemon |
| `image_health`   *string* | *(Optional)* ImageHealth is the health of the mirrored image |
| `states`   *[StatesSpec](index.md#ceph.rook.io/v1.StatesSpec)* | *(Optional)* States is the various state for all mirrored images |
| `image_states`   *[StatesSpec](index.md#ceph.rook.io/v1.StatesSpec)* | *(Optional)* ImageStates is the various state for all mirrored images |
| `group_health`   *string* | *(Optional)* GroupHealth is the health of the mirrored image group |
| `group_states`   *[StatesSpec](index.md#ceph.rook.io/v1.StatesSpec)* | *(Optional)* GroupStates is the various state for all mirrored image groups |

### Module

(*Appears on:*[MgrSpec](index.md#ceph.rook.io/v1.MgrSpec))

Module represents mgr modules that the user wants to enable or disable

| Field | Description |
| --- | --- |
| `name`   *string* | *(Optional)* Name is the name of the ceph manager module |
| `enabled`   *bool* | *(Optional)* Enabled determines whether a module should be enabled or not |
| `settings`   *[ModuleSettings](index.md#ceph.rook.io/v1.ModuleSettings)* | Settings to further configure the module |

### ModuleSettings

(*Appears on:*[Module](index.md#ceph.rook.io/v1.Module))

| Field | Description |
| --- | --- |
| `balancerMode`   *string* | BalancerMode sets the `balancer` module with different modes like `upmap`, `crush-compact` etc |

### MonSpec

(*Appears on:*[ClusterSpec](index.md#ceph.rook.io/v1.ClusterSpec))

MonSpec represents the specification of the monitor

| Field | Description |
| --- | --- |
| `count`   *int* | *(Optional)* Count is the number of Ceph monitors |
| `allowMultiplePerNode`   *bool* | *(Optional)* AllowMultiplePerNode determines if we can run multiple monitors on the same node (not recommended) |
| `failureDomainLabel`   *string* | *(Optional)* |
| `zones`   *[[]MonZoneSpec](index.md#ceph.rook.io/v1.MonZoneSpec)* | *(Optional)* Zones are specified when we want to provide zonal awareness to mons |
| `stretchCluster`   *[StretchClusterSpec](index.md#ceph.rook.io/v1.StretchClusterSpec)* | *(Optional)* StretchCluster is the stretch cluster specification |
| `volumeClaimTemplate`   *[VolumeClaimTemplate](index.md#ceph.rook.io/v1.VolumeClaimTemplate)* | *(Optional)* VolumeClaimTemplate is the PVC definition |
| `externalMonIDs`   *[]string* | *(Optional)* ExternalMonIDs - optional list of monitor IDs which are deployed externally and not managed by Rook. If set, Rook will not remove mons with given IDs from quorum. This parameter is used only for local Rook cluster running in normal mode and will be ignored if external or stretched mode is used. leading |

### MonZoneSpec

(*Appears on:*[MonSpec](index.md#ceph.rook.io/v1.MonSpec), [StretchClusterSpec](index.md#ceph.rook.io/v1.StretchClusterSpec))

MonZoneSpec represents the specification of a zone in a Ceph Cluster

| Field | Description |
| --- | --- |
| `name`   *string* | *(Optional)* Name is the name of the zone |
| `arbiter`   *bool* | *(Optional)* Arbiter determines if the zone contains the arbiter used for stretch cluster mode |
| `volumeClaimTemplate`   *[VolumeClaimTemplate](index.md#ceph.rook.io/v1.VolumeClaimTemplate)* | *(Optional)* VolumeClaimTemplate is the PVC template |

### MonitoringSpec

(*Appears on:*[ClusterSpec](index.md#ceph.rook.io/v1.ClusterSpec))

MonitoringSpec represents the settings for Prometheus based Ceph monitoring

| Field | Description |
| --- | --- |
| `enabled`   *bool* | *(Optional)* Enabled determines whether to create the prometheus rules for the ceph cluster. If true, the prometheus types must exist or the creation will fail. Default is false. |
| `metricsDisabled`   *bool* | *(Optional)* Whether to disable the metrics reported by Ceph. If false, the prometheus mgr module and Ceph exporter are enabled. If true, the prometheus mgr module and Ceph exporter are both disabled. Default is false. |
| `externalMgrEndpoints`   *[[]Kubernetes core/v1.EndpointAddress](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#endpointaddress-v1-core)* | *(Optional)* ExternalMgrEndpoints points to an existing Ceph prometheus exporter endpoint |
| `externalMgrPrometheusPort`   *uint16* | *(Optional)* ExternalMgrPrometheusPort Prometheus exporter port |
| `port`   *int* | *(Optional)* Port is the prometheus server port |
| `interval`   *[Kubernetes meta/v1.Duration](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration)* | *(Optional)* Interval determines prometheus scrape interval |
| `exporter`   *[CephExporterSpec](index.md#ceph.rook.io/v1.CephExporterSpec)* | *(Optional)* Ceph exporter configuration |

### MultiClusterServiceSpec

(*Appears on:*[NetworkSpec](index.md#ceph.rook.io/v1.NetworkSpec))

| Field | Description |
| --- | --- |
| `enabled`   *bool* | *(Optional)* Enable multiClusterService to export the mon and OSD services to peer cluster. Ensure that peer clusters are connected using an MCS API compatible application, like Globalnet Submariner. |
| `clusterID`   *string* | ClusterID uniquely identifies a cluster. It is used as a prefix to nslookup exported services. For example: ...svc.clusterset.local |

### NFSGaneshaSpec

(*Appears on:*[CephNFS](index.md#ceph.rook.io/v1.CephNFS))

NFSGaneshaSpec represents the spec of an nfs ganesha server

| Field | Description |
| --- | --- |
| `rados`   *[GaneshaRADOSSpec](index.md#ceph.rook.io/v1.GaneshaRADOSSpec)* | *(Optional)* RADOS is the Ganesha RADOS specification |
| `server`   *[GaneshaServerSpec](index.md#ceph.rook.io/v1.GaneshaServerSpec)* | Server is the Ganesha Server specification |
| `security`   *[NFSSecuritySpec](index.md#ceph.rook.io/v1.NFSSecuritySpec)* | *(Optional)* Security allows specifying security configurations for the NFS cluster |

### NFSSecuritySpec

(*Appears on:*[NFSGaneshaSpec](index.md#ceph.rook.io/v1.NFSGaneshaSpec))

NFSSecuritySpec represents security configurations for an NFS server pod

| Field | Description |
| --- | --- |
| `sssd`   *[SSSDSpec](index.md#ceph.rook.io/v1.SSSDSpec)* | *(Optional)* SSSD enables integration with System Security Services Daemon (SSSD). SSSD can be used to provide user ID mapping from a number of sources. See <https://sssd.io> for more information about the SSSD project. |
| `kerberos`   *[KerberosSpec](index.md#ceph.rook.io/v1.KerberosSpec)* | *(Optional)* Kerberos configures NFS-Ganesha to secure NFS client connections with Kerberos. |

### NamedBlockPoolSpec

(*Appears on:*[CephBlockPool](index.md#ceph.rook.io/v1.CephBlockPool))

NamedBlockPoolSpec allows a block pool to be created with a non-default name. This is more specific than the NamedPoolSpec so we get schema validation on the allowed pool names that can be specified.

| Field | Description |
| --- | --- |
| `name`   *string* | *(Optional)* The desired name of the pool if different from the CephBlockPool CR name. |
| `PoolSpec`   *[PoolSpec](index.md#ceph.rook.io/v1.PoolSpec)* | (Members of `PoolSpec` are embedded into this type.)  The core pool configuration |

### NamedPoolSpec

(*Appears on:*[FilesystemSpec](index.md#ceph.rook.io/v1.FilesystemSpec))

NamedPoolSpec represents the named ceph pool spec

| Field | Description |
| --- | --- |
| `name`   *string* | Name of the pool |
| `PoolSpec`   *[PoolSpec](index.md#ceph.rook.io/v1.PoolSpec)* | (Members of `PoolSpec` are embedded into this type.)  PoolSpec represents the spec of ceph pool |

### NetworkProviderType (`string` alias)

(*Appears on:*[NetworkSpec](index.md#ceph.rook.io/v1.NetworkSpec))

NetworkProviderType defines valid network providers for Rook.

| Value | Description |
| --- | --- |
| "" |  |
| "host" |  |
| "multus" |  |

### NetworkSpec

(*Appears on:*[ClusterSpec](index.md#ceph.rook.io/v1.ClusterSpec))

NetworkSpec for Ceph includes backward compatibility code

| Field | Description |
| --- | --- |
| `provider`   *[NetworkProviderType](index.md#ceph.rook.io/v1.NetworkProviderType)* | *(Optional)* Provider is what provides network connectivity to the cluster e.g. “host” or “multus”. If the Provider is updated from being empty to “host” on a running cluster, then the operator will automatically fail over all the mons to apply the “host” network settings. |
| `selectors`   *map[github.com/rook/rook/pkg/apis/ceph.rook.io/v1.CephNetworkType]string* | *(Optional)* Selectors define NetworkAttachmentDefinitions to be used for Ceph public and/or cluster networks when the “multus” network provider is used. This config section is not used for other network providers.  Valid keys are “public” and “cluster”. Refer to Ceph networking documentation for more: <https://docs.ceph.com/en/latest/rados/configuration/network-config-ref/>  Refer to Multus network annotation documentation for help selecting values: <https://github.com/k8snetworkplumbingwg/multus-cni/blob/master/docs/how-to-use.md#run-pod-with-network-annotation>  Rook will make a best-effort attempt to automatically detect CIDR address ranges for given network attachment definitions. Rook’s methods are robust but may be imprecise for sufficiently complicated networks. Rook’s auto-detection process obtains a new IP address lease for each CephCluster reconcile. If Rook fails to detect, incorrectly detects, only partially detects, or if underlying networks do not support reusing old IP addresses, it is best to use the ‘addressRanges’ config section to specify CIDR ranges for the Ceph cluster.  As a contrived example, one can use a theoretical Kubernetes-wide network for Ceph client traffic and a theoretical Rook-only network for Ceph replication traffic as shown: selectors: public: “default/cluster-fast-net” cluster: “rook-ceph/ceph-backend-net” |
| `addressRanges`   *[AddressRangesSpec](index.md#ceph.rook.io/v1.AddressRangesSpec)* | *(Optional)* AddressRanges specify a list of CIDRs that Rook will apply to Ceph’s ‘public_network’ and/or ‘cluster_network’ configurations. This config section may be used for the “host” or “multus” network providers. |
| `connections`   *[ConnectionsSpec](index.md#ceph.rook.io/v1.ConnectionsSpec)* | *(Optional)* Settings for network connections such as compression and encryption across the wire. |
| `hostNetwork`   *bool* | *(Optional)* HostNetwork to enable host network. If host networking is enabled or disabled on a running cluster, then the operator will automatically fail over all the mons to apply the new network settings. |
| `ipFamily`   *[IPFamilyType](index.md#ceph.rook.io/v1.IPFamilyType)* | *(Optional)* IPFamily is the single stack IPv6 or IPv4 protocol |
| `dualStack`   *bool* | *(Optional)* DualStack determines whether Ceph daemons should listen on both IPv4 and IPv6 |
| `multiClusterService`   *[MultiClusterServiceSpec](index.md#ceph.rook.io/v1.MultiClusterServiceSpec)* | *(Optional)* Enable multiClusterService to export the Services between peer clusters |

### Node

(*Appears on:*[StorageScopeSpec](index.md#ceph.rook.io/v1.StorageScopeSpec))

Node is a storage nodes

| Field | Description |
| --- | --- |
| `name`   *string* | *(Optional)* |
| `resources`   *[Kubernetes core/v1.ResourceRequirements](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#resourcerequirements-v1-core)* | *(Optional)* |
| `config`   *map[string]string* | *(Optional)* |
| `Selection`   *[Selection](index.md#ceph.rook.io/v1.Selection)* | (Members of `Selection` are embedded into this type.) |

### NodesByName (`[]github.com/rook/rook/pkg/apis/ceph.rook.io/v1.Node` alias)

NodesByName implements an interface to sort nodes by name

### NotificationFilterRule

(*Appears on:*[NotificationFilterSpec](index.md#ceph.rook.io/v1.NotificationFilterSpec))

NotificationFilterRule represent a single rule in the Notification Filter spec

| Field | Description |
| --- | --- |
| `name`   *string* | Name of the metadata or tag |
| `value`   *string* | Value to filter on |

### NotificationFilterSpec

(*Appears on:*[BucketNotificationSpec](index.md#ceph.rook.io/v1.BucketNotificationSpec))

NotificationFilterSpec represent the spec of a Bucket Notification filter

| Field | Description |
| --- | --- |
| `keyFilters`   *[[]NotificationKeyFilterRule](index.md#ceph.rook.io/v1.NotificationKeyFilterRule)* | *(Optional)* Filters based on the object’s key |
| `metadataFilters`   *[[]NotificationFilterRule](index.md#ceph.rook.io/v1.NotificationFilterRule)* | *(Optional)* Filters based on the object’s metadata |
| `tagFilters`   *[[]NotificationFilterRule](index.md#ceph.rook.io/v1.NotificationFilterRule)* | *(Optional)* Filters based on the object’s tags |

### NotificationKeyFilterRule

(*Appears on:*[NotificationFilterSpec](index.md#ceph.rook.io/v1.NotificationFilterSpec))

NotificationKeyFilterRule represent a single key rule in the Notification Filter spec

| Field | Description |
| --- | --- |
| `name`   *string* | Name of the filter - prefix/suffix/regex |
| `value`   *string* | Value to filter on |

### OSDStatus

(*Appears on:*[CephStorage](index.md#ceph.rook.io/v1.CephStorage))

OSDStatus represents OSD status of the ceph Cluster

| Field | Description |
| --- | --- |
| `storeType`   *map[string]int* | StoreType is a mapping between the OSD backend stores and number of OSDs using these stores |
| `migrationStatus`   *[MigrationStatus](index.md#ceph.rook.io/v1.MigrationStatus)* |  |

### OSDStore

(*Appears on:*[StorageScopeSpec](index.md#ceph.rook.io/v1.StorageScopeSpec))

OSDStore is the backend storage type used for creating the OSDs

| Field | Description |
| --- | --- |
| `type`   *string* | *(Optional)* Type of backend storage to be used while creating OSDs. If empty, then bluestore will be used |
| `updateStore`   *string* | *(Optional)* UpdateStore updates the backend store for existing OSDs. It destroys each OSD one at a time, cleans up the backing disk and prepares same OSD on that disk |

### ObjectEndpointSpec

(*Appears on:*[ObjectStoreHostingSpec](index.md#ceph.rook.io/v1.ObjectStoreHostingSpec))

ObjectEndpointSpec represents an object store endpoint

| Field | Description |
| --- | --- |
| `dnsName`   *string* | DnsName is the DNS name (in RFC-1123 format) of the endpoint. If the DNS name corresponds to an endpoint with DNS wildcard support, do not include the wildcard itself in the list of hostnames. E.g., use “mystore.example.com” instead of “\*.mystore.example.com”. |
| `port`   *int32* | Port is the port on which S3 connections can be made for this endpoint. |
| `useTls`   *bool* | UseTls defines whether the endpoint uses TLS (HTTPS) or not (HTTP). |

### ObjectEndpoints

(*Appears on:*[ObjectStoreStatus](index.md#ceph.rook.io/v1.ObjectStoreStatus))

| Field | Description |
| --- | --- |
| `insecure`   *[]string* | *(Optional)* |
| `secure`   *[]string* | *(Optional)* |

### ObjectHealthCheckSpec

(*Appears on:*[ObjectStoreSpec](index.md#ceph.rook.io/v1.ObjectStoreSpec))

ObjectHealthCheckSpec represents the health check of an object store

| Field | Description |
| --- | --- |
| `readinessProbe`   *[ProbeSpec](index.md#ceph.rook.io/v1.ProbeSpec)* | *(Optional)* |
| `startupProbe`   *[ProbeSpec](index.md#ceph.rook.io/v1.ProbeSpec)* | *(Optional)* |

### ObjectRealmSpec

(*Appears on:*[CephObjectRealm](index.md#ceph.rook.io/v1.CephObjectRealm))

ObjectRealmSpec represent the spec of an ObjectRealm

| Field | Description |
| --- | --- |
| `pull`   *[PullSpec](index.md#ceph.rook.io/v1.PullSpec)* |  |
| `defaultRealm`   *bool* | *(Optional)* Set this realm as the default in Ceph. Only one realm should be default. |

### ObjectSharedPoolsSpec

(*Appears on:*[ObjectStoreSpec](index.md#ceph.rook.io/v1.ObjectStoreSpec), [ObjectZoneSpec](index.md#ceph.rook.io/v1.ObjectZoneSpec))

ObjectSharedPoolsSpec represents object store pool info when configuring RADOS namespaces in existing pools.

| Field | Description |
| --- | --- |
| `metadataPoolName`   *string* | *(Optional)* The metadata pool used for creating RADOS namespaces in the object store |
| `dataPoolName`   *string* | *(Optional)* The data pool used for creating RADOS namespaces in the object store |
| `preserveRadosNamespaceDataOnDelete`   *bool* | *(Optional)* Whether the RADOS namespaces should be preserved on deletion of the object store |
| `poolPlacements`   *[[]PoolPlacementSpec](index.md#ceph.rook.io/v1.PoolPlacementSpec)* | *(Optional)* PoolPlacements control which Pools are associated with a particular RGW bucket. Once PoolPlacements are defined, RGW client will be able to associate pool with ObjectStore bucket by providing “” during s3 bucket creation or “X-Storage-Policy” header during swift container creation. See: <https://docs.ceph.com/en/latest/radosgw/placement/#placement-targets> PoolPlacement with name: “default” will be used as a default pool if no option is provided during bucket creation. If default placement is not provided, spec.sharedPools.dataPoolName and spec.sharedPools.MetadataPoolName will be used as default pools. If spec.sharedPools are also empty, then RGW pools (spec.dataPool and spec.metadataPool) will be used as defaults. |

### ObjectStoreAPI (`string` alias)

(*Appears on:*[ProtocolSpec](index.md#ceph.rook.io/v1.ProtocolSpec))

### ObjectStoreHostingSpec

(*Appears on:*[ObjectStoreSpec](index.md#ceph.rook.io/v1.ObjectStoreSpec))

ObjectStoreHostingSpec represents the hosting settings for the object store

| Field | Description |
| --- | --- |
| `advertiseEndpoint`   *[ObjectEndpointSpec](index.md#ceph.rook.io/v1.ObjectEndpointSpec)* | *(Optional)* AdvertiseEndpoint is the default endpoint Rook will return for resources dependent on this object store. This endpoint will be returned to CephObjectStoreUsers, Object Bucket Claims, and COSI Buckets/Accesses. By default, Rook returns the endpoint for the object store’s Kubernetes service using HTTPS with `gateway.securePort` if it is defined (otherwise, HTTP with `gateway.port`). |
| `dnsNames`   *[]string* | *(Optional)* A list of DNS host names on which object store gateways will accept client S3 connections. When specified, object store gateways will reject client S3 connections to hostnames that are not present in this list, so include all endpoints. The object store’s advertiseEndpoint and Kubernetes service endpoint, plus CephObjectZone `customEndpoints` are automatically added to the list but may be set here again if desired. Each DNS name must be valid according RFC-1123. If the DNS name corresponds to an endpoint with DNS wildcard support, do not include the wildcard itself in the list of hostnames. E.g., use “mystore.example.com” instead of “\*.mystore.example.com”. |

### ObjectStoreSecuritySpec

(*Appears on:*[ObjectStoreSpec](index.md#ceph.rook.io/v1.ObjectStoreSpec))

ObjectStoreSecuritySpec is spec to define security features like encryption

| Field | Description |
| --- | --- |
| `SecuritySpec`   *[SecuritySpec](index.md#ceph.rook.io/v1.SecuritySpec)* | *(Optional)* |
| `s3`   *[KeyManagementServiceSpec](index.md#ceph.rook.io/v1.KeyManagementServiceSpec)* | *(Optional)* The settings for supporting AWS-SSE:S3 with RGW |

### ObjectStoreSpec

(*Appears on:*[CephObjectStore](index.md#ceph.rook.io/v1.CephObjectStore))

ObjectStoreSpec represent the spec of a pool

| Field | Description |
| --- | --- |
| `metadataPool`   *[PoolSpec](index.md#ceph.rook.io/v1.PoolSpec)* | *(Optional)* The metadata pool settings |
| `dataPool`   *[PoolSpec](index.md#ceph.rook.io/v1.PoolSpec)* | *(Optional)* The data pool settings |
| `sharedPools`   *[ObjectSharedPoolsSpec](index.md#ceph.rook.io/v1.ObjectSharedPoolsSpec)* | *(Optional)* The pool information when configuring RADOS namespaces in existing pools. |
| `preservePoolsOnDelete`   *bool* | *(Optional)* Preserve pools on object store deletion |
| `gateway`   *[GatewaySpec](index.md#ceph.rook.io/v1.GatewaySpec)* | *(Optional)* The rgw pod info |
| `protocols`   *[ProtocolSpec](index.md#ceph.rook.io/v1.ProtocolSpec)* | *(Optional)* The protocol specification |
| `auth`   *[AuthSpec](index.md#ceph.rook.io/v1.AuthSpec)* | *(Optional)* The authentication configuration |
| `zone`   *[ZoneSpec](index.md#ceph.rook.io/v1.ZoneSpec)* | *(Optional)* The multisite info |
| `healthCheck`   *[ObjectHealthCheckSpec](index.md#ceph.rook.io/v1.ObjectHealthCheckSpec)* | *(Optional)* The RGW health probes |
| `security`   *[ObjectStoreSecuritySpec](index.md#ceph.rook.io/v1.ObjectStoreSecuritySpec)* | *(Optional)* Security represents security settings |
| `allowUsersInNamespaces`   *[]string* | *(Optional)* The list of allowed namespaces in addition to the object store namespace where ceph object store users may be created. Specify “\*” to allow all namespaces, otherwise list individual namespaces that are to be allowed. This is useful for applications that need object store credentials to be created in their own namespace, where neither OBCs nor COSI is being used to create buckets. The default is empty. |
| `hosting`   *[ObjectStoreHostingSpec](index.md#ceph.rook.io/v1.ObjectStoreHostingSpec)* | *(Optional)* Hosting settings for the object store. A common use case for hosting configuration is to inform Rook of endpoints that support DNS wildcards, which in turn allows virtual host-style bucket addressing. |
| `defaultRealm`   *bool* | *(Optional)* Set this realm as the default in Ceph. Only one realm should be default. Do not set this true on more than one CephObjectStore. This may not be set when zone is also specified; in this case, the realm referenced by the zone’s zonegroup should configure defaulting behavior. |

### ObjectStoreStatus

(*Appears on:*[CephObjectStore](index.md#ceph.rook.io/v1.CephObjectStore))

ObjectStoreStatus represents the status of a Ceph Object Store resource

| Field | Description |
| --- | --- |
| `phase`   *[ConditionType](index.md#ceph.rook.io/v1.ConditionType)* | *(Optional)* |
| `message`   *string* | *(Optional)* |
| `endpoints`   *[ObjectEndpoints](index.md#ceph.rook.io/v1.ObjectEndpoints)* | *(Optional)* |
| `info`   *map[string]string* | *(Optional)* |
| `conditions`   *[[]Condition](index.md#ceph.rook.io/v1.Condition)* |  |
| `observedGeneration`   *int64* | *(Optional)* ObservedGeneration is the latest generation observed by the controller. |

### ObjectStoreUserSpec

(*Appears on:*[CephObjectStoreUser](index.md#ceph.rook.io/v1.CephObjectStoreUser))

ObjectStoreUserSpec represent the spec of an Objectstoreuser

| Field | Description |
| --- | --- |
| `store`   *string* | *(Optional)* The store the user will be created in |
| `displayName`   *string* | *(Optional)* The display name for the ceph user. |
| `capabilities`   *[ObjectUserCapSpec](index.md#ceph.rook.io/v1.ObjectUserCapSpec)* | *(Optional)* |
| `quotas`   *[ObjectUserQuotaSpec](index.md#ceph.rook.io/v1.ObjectUserQuotaSpec)* | *(Optional)* |
| `keys`   *[[]ObjectUserKey](index.md#ceph.rook.io/v1.ObjectUserKey)* | *(Optional)* Allows specifying credentials for the user. If not provided, the operator will generate them. |
| `clusterNamespace`   *string* | *(Optional)* The namespace where the parent CephCluster and CephObjectStore are found |

### ObjectStoreUserStatus

(*Appears on:*[CephObjectStoreUser](index.md#ceph.rook.io/v1.CephObjectStoreUser))

ObjectStoreUserStatus represents the status Ceph Object Store Gateway User

| Field | Description |
| --- | --- |
| `phase`   *string* | *(Optional)* |
| `info`   *map[string]string* | *(Optional)* |
| `observedGeneration`   *int64* | *(Optional)* ObservedGeneration is the latest generation observed by the controller. |
| `keys`   *[[]SecretReference](index.md#ceph.rook.io/v1.SecretReference)* | *(Optional)* |

### ObjectUserCapSpec

(*Appears on:*[ObjectStoreUserSpec](index.md#ceph.rook.io/v1.ObjectStoreUserSpec))

Additional admin-level capabilities for the Ceph object store user

| Field | Description |
| --- | --- |
| `user`   *string* | *(Optional)* Admin capabilities to read/write Ceph object store users. Documented in <https://docs.ceph.com/en/latest/radosgw/admin/?#add-remove-admin-capabilities> |
| `users`   *string* | *(Optional)* Admin capabilities to read/write Ceph object store users. Documented in <https://docs.ceph.com/en/latest/radosgw/admin/?#add-remove-admin-capabilities> |
| `bucket`   *string* | *(Optional)* Admin capabilities to read/write Ceph object store buckets. Documented in <https://docs.ceph.com/en/latest/radosgw/admin/?#add-remove-admin-capabilities> |
| `buckets`   *string* | *(Optional)* Admin capabilities to read/write Ceph object store buckets. Documented in <https://docs.ceph.com/en/latest/radosgw/admin/?#add-remove-admin-capabilities> |
| `metadata`   *string* | *(Optional)* Admin capabilities to read/write Ceph object store metadata. Documented in <https://docs.ceph.com/en/latest/radosgw/admin/?#add-remove-admin-capabilities> |
| `usage`   *string* | *(Optional)* Admin capabilities to read/write Ceph object store usage. Documented in <https://docs.ceph.com/en/latest/radosgw/admin/?#add-remove-admin-capabilities> |
| `zone`   *string* | *(Optional)* Admin capabilities to read/write Ceph object store zones. Documented in <https://docs.ceph.com/en/latest/radosgw/admin/?#add-remove-admin-capabilities> |
| `roles`   *string* | *(Optional)* Admin capabilities to read/write roles for user. Documented in <https://docs.ceph.com/en/latest/radosgw/admin/?#add-remove-admin-capabilities> |
| `info`   *string* | *(Optional)* Admin capabilities to read/write information about the user. Documented in <https://docs.ceph.com/en/latest/radosgw/admin/?#add-remove-admin-capabilities> |
| `amz-cache`   *string* | *(Optional)* Add capabilities for user to send request to RGW Cache API header. Documented in <https://docs.ceph.com/en/latest/radosgw/rgw-cache/#cache-api> |
| `bilog`   *string* | *(Optional)* Add capabilities for user to change bucket index logging. Documented in <https://docs.ceph.com/en/latest/radosgw/admin/?#add-remove-admin-capabilities> |
| `mdlog`   *string* | *(Optional)* Add capabilities for user to change metadata logging. Documented in <https://docs.ceph.com/en/latest/radosgw/admin/?#add-remove-admin-capabilities> |
| `datalog`   *string* | *(Optional)* Add capabilities for user to change data logging. Documented in <https://docs.ceph.com/en/latest/radosgw/admin/?#add-remove-admin-capabilities> |
| `user-policy`   *string* | *(Optional)* Add capabilities for user to change user policies. Documented in <https://docs.ceph.com/en/latest/radosgw/admin/?#add-remove-admin-capabilities> |
| `oidc-provider`   *string* | *(Optional)* Add capabilities for user to change oidc provider. Documented in <https://docs.ceph.com/en/latest/radosgw/admin/?#add-remove-admin-capabilities> |
| `ratelimit`   *string* | *(Optional)* Add capabilities for user to set rate limiter for user and bucket. Documented in <https://docs.ceph.com/en/latest/radosgw/admin/?#add-remove-admin-capabilities> |

### ObjectUserKey

(*Appears on:*[ObjectStoreUserSpec](index.md#ceph.rook.io/v1.ObjectStoreUserSpec))

ObjectUserKey defines a set of rgw user access credentials to be retrieved from secret resources.

| Field | Description |
| --- | --- |
| `accessKeyRef`   *[Kubernetes core/v1.SecretKeySelector](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#secretkeyselector-v1-core)* | Secret key selector for the access_key (commonly referred to as AWS_ACCESS_KEY_ID). |
| `secretKeyRef`   *[Kubernetes core/v1.SecretKeySelector](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#secretkeyselector-v1-core)* | Secret key selector for the secret_key (commonly referred to as AWS_SECRET_ACCESS_KEY). |

### ObjectUserQuotaSpec

(*Appears on:*[ObjectStoreUserSpec](index.md#ceph.rook.io/v1.ObjectStoreUserSpec))

ObjectUserQuotaSpec can be used to set quotas for the object store user to limit their usage. See the [Ceph docs](https://docs.ceph.com/en/latest/radosgw/admin/?#quota-management) for more

| Field | Description |
| --- | --- |
| `maxBuckets`   *int* | *(Optional)* Maximum bucket limit for the ceph user |
| `maxSize`   *k8s.io/apimachinery/pkg/api/resource.Quantity* | *(Optional)* Maximum size limit of all objects across all the user’s buckets See <https://pkg.go.dev/k8s.io/apimachinery/pkg/api/resource#Quantity> for more info. |
| `maxObjects`   *int64* | *(Optional)* Maximum number of objects across all the user’s buckets |

### ObjectZoneGroupSpec

(*Appears on:*[CephObjectZoneGroup](index.md#ceph.rook.io/v1.CephObjectZoneGroup))

ObjectZoneGroupSpec represent the spec of an ObjectZoneGroup

| Field | Description |
| --- | --- |
| `realm`   *string* | The name of the realm the zone group is a member of. |

### ObjectZoneSpec

(*Appears on:*[CephObjectZone](index.md#ceph.rook.io/v1.CephObjectZone))

ObjectZoneSpec represent the spec of an ObjectZone

| Field | Description |
| --- | --- |
| `zoneGroup`   *string* | The name of the zone group the zone is a member of. |
| `metadataPool`   *[PoolSpec](index.md#ceph.rook.io/v1.PoolSpec)* | *(Optional)* The metadata pool settings |
| `dataPool`   *[PoolSpec](index.md#ceph.rook.io/v1.PoolSpec)* | *(Optional)* The data pool settings |
| `sharedPools`   *[ObjectSharedPoolsSpec](index.md#ceph.rook.io/v1.ObjectSharedPoolsSpec)* | *(Optional)* The pool information when configuring RADOS namespaces in existing pools. |
| `customEndpoints`   *[]string* | *(Optional)* If this zone cannot be accessed from other peer Ceph clusters via the ClusterIP Service endpoint created by Rook, you must set this to the externally reachable endpoint(s). You may include the port in the definition. For example: “[https://my-object-store.my-domain.net:443”](https://my-object-store.my-domain.net:443"). In many cases, you should set this to the endpoint of the ingress resource that makes the CephObjectStore associated with this CephObjectStoreZone reachable to peer clusters. The list can have one or more endpoints pointing to different RGW servers in the zone.  If a CephObjectStore endpoint is omitted from this list, that object store’s gateways will not receive multisite replication data (see CephObjectStore.spec.gateway.disableMultisiteSyncTraffic). |
| `preservePoolsOnDelete`   *bool* | *(Optional)* Preserve pools on object zone deletion |

### OpsLogSidecar

(*Appears on:*[GatewaySpec](index.md#ceph.rook.io/v1.GatewaySpec))

RGWLoggingSpec is intended to extend the s3/swift logging for client operations

| Field | Description |
| --- | --- |
| `resources`   *[Kubernetes core/v1.ResourceRequirements](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#resourcerequirements-v1-core)* | *(Optional)* Resources represents the way to specify resource requirements for the ops-log sidecar |

### PeerRemoteSpec

(*Appears on:*[FilesystemMirrorInfoPeerSpec](index.md#ceph.rook.io/v1.FilesystemMirrorInfoPeerSpec))

| Field | Description |
| --- | --- |
| `client_name`   *string* | *(Optional)* ClientName is cephx name |
| `cluster_name`   *string* | *(Optional)* ClusterName is the name of the cluster |
| `fs_name`   *string* | *(Optional)* FsName is the filesystem name |

### PeerStatSpec

(*Appears on:*[FilesystemMirrorInfoPeerSpec](index.md#ceph.rook.io/v1.FilesystemMirrorInfoPeerSpec))

PeerStatSpec are the mirror stat with a given peer

| Field | Description |
| --- | --- |
| `failure_count`   *int* | *(Optional)* FailureCount is the number of mirroring failure |
| `recovery_count`   *int* | *(Optional)* RecoveryCount is the number of recovery attempted after failures |

### PeersSpec

(*Appears on:*[MirroringInfo](index.md#ceph.rook.io/v1.MirroringInfo))

PeersSpec contains peer details

| Field | Description |
| --- | --- |
| `uuid`   *string* | *(Optional)* UUID is the peer UUID |
| `direction`   *string* | *(Optional)* Direction is the peer mirroring direction |
| `site_name`   *string* | *(Optional)* SiteName is the current site name |
| `mirror_uuid`   *string* | *(Optional)* MirrorUUID is the mirror UUID |
| `client_name`   *string* | *(Optional)* ClientName is the CephX user used to connect to the peer |

### Placement

(*Appears on:*[CephCOSIDriverSpec](index.md#ceph.rook.io/v1.CephCOSIDriverSpec), [FilesystemMirroringSpec](index.md#ceph.rook.io/v1.FilesystemMirroringSpec), [GaneshaServerSpec](index.md#ceph.rook.io/v1.GaneshaServerSpec), [GatewaySpec](index.md#ceph.rook.io/v1.GatewaySpec), [MetadataServerSpec](index.md#ceph.rook.io/v1.MetadataServerSpec), [RBDMirroringSpec](index.md#ceph.rook.io/v1.RBDMirroringSpec), [StorageClassDeviceSet](index.md#ceph.rook.io/v1.StorageClassDeviceSet))

Placement is the placement for an object

| Field | Description |
| --- | --- |
| `nodeAffinity`   *[Kubernetes core/v1.NodeAffinity](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#nodeaffinity-v1-core)* | *(Optional)* NodeAffinity is a group of node affinity scheduling rules |
| `podAffinity`   *[Kubernetes core/v1.PodAffinity](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#podaffinity-v1-core)* | *(Optional)* PodAffinity is a group of inter pod affinity scheduling rules |
| `podAntiAffinity`   *[Kubernetes core/v1.PodAntiAffinity](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#podantiaffinity-v1-core)* | *(Optional)* PodAntiAffinity is a group of inter pod anti affinity scheduling rules |
| `tolerations`   *[[]Kubernetes core/v1.Toleration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#toleration-v1-core)* | *(Optional)* The pod this Toleration is attached to tolerates any taint that matches the triple  using the matching operator |
| `topologySpreadConstraints`   *[[]Kubernetes core/v1.TopologySpreadConstraint](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#topologyspreadconstraint-v1-core)* | *(Optional)* TopologySpreadConstraints specifies how to spread matching pods among the given topology |

### PlacementSpec (`map[github.com/rook/rook/pkg/apis/ceph.rook.io/v1.KeyType]github.com/rook/rook/pkg/apis/ceph.rook.io/v1.Placement` alias)

(*Appears on:*[ClusterSpec](index.md#ceph.rook.io/v1.ClusterSpec))

PlacementSpec is the placement for core ceph daemons part of the CephCluster CRD

### PlacementStorageClassSpec

(*Appears on:*[PoolPlacementSpec](index.md#ceph.rook.io/v1.PoolPlacementSpec))

| Field | Description |
| --- | --- |
| `name`   *string* | Name is the StorageClass name. Ceph allows arbitrary name for StorageClasses, however most clients/libs insist on AWS names so it is recommended to use one of the valid x-amz-storage-class values for better compatibility: REDUCED_REDUNDANCY | STANDARD_IA | ONEZONE_IA | INTELLIGENT_TIERING | GLACIER | DEEP_ARCHIVE | OUTPOSTS | GLACIER_IR | SNOW | EXPRESS_ONEZONE See AWS docs: <https://aws.amazon.com/de/s3/storage-classes/> |
| `dataPoolName`   *string* | DataPoolName is the data pool used to store ObjectStore objects data. |

### PoolPlacementSpec

(*Appears on:*[ObjectSharedPoolsSpec](index.md#ceph.rook.io/v1.ObjectSharedPoolsSpec))

| Field | Description |
| --- | --- |
| `name`   *string* | Pool placement name. Name can be arbitrary. Placement with name “default” will be used as default. |
| `default`   *bool* | *(Optional)* Sets given placement as default. Only one placement in the list can be marked as default. Default is false. |
| `metadataPoolName`   *string* | The metadata pool used to store ObjectStore bucket index. |
| `dataPoolName`   *string* | The data pool used to store ObjectStore objects data. |
| `dataNonECPoolName`   *string* | *(Optional)* The data pool used to store ObjectStore data that cannot use erasure coding (ex: multi-part uploads). If dataPoolName is not erasure coded, then there is no need for dataNonECPoolName. |
| `storageClasses`   *[[]PlacementStorageClassSpec](index.md#ceph.rook.io/v1.PlacementStorageClassSpec)* | *(Optional)* StorageClasses can be selected by user to override dataPoolName during object creation. Each placement has default STANDARD StorageClass pointing to dataPoolName. This list allows defining additional StorageClasses on top of default STANDARD storage class. |

### PoolSpec

(*Appears on:*[NamedBlockPoolSpec](index.md#ceph.rook.io/v1.NamedBlockPoolSpec), [NamedPoolSpec](index.md#ceph.rook.io/v1.NamedPoolSpec), [ObjectStoreSpec](index.md#ceph.rook.io/v1.ObjectStoreSpec), [ObjectZoneSpec](index.md#ceph.rook.io/v1.ObjectZoneSpec))

PoolSpec represents the spec of ceph pool

| Field | Description |
| --- | --- |
| `failureDomain`   *string* | *(Optional)* The failure domain: osd/host/(region or zone if available) - technically also any type in the crush map |
| `crushRoot`   *string* | *(Optional)* The root of the crush hierarchy utilized by the pool |
| `deviceClass`   *string* | *(Optional)* The device class the OSD should set to for use in the pool |
| `enableCrushUpdates`   *bool* | *(Optional)* Allow rook operator to change the pool CRUSH tunables once the pool is created |
| `compressionMode`   *string* | *(Optional)* DEPRECATED: use Parameters instead, e.g., Parameters[“compression_mode”] = “force” The inline compression mode in Bluestore OSD to set to (options are: none, passive, aggressive, force) Do NOT set a default value for kubebuilder as this will override the Parameters |
| `replicated`   *[ReplicatedSpec](index.md#ceph.rook.io/v1.ReplicatedSpec)* | *(Optional)* The replication settings |
| `erasureCoded`   *[ErasureCodedSpec](index.md#ceph.rook.io/v1.ErasureCodedSpec)* | *(Optional)* The erasure code settings |
| `parameters`   *map[string]string* | *(Optional)* Parameters is a list of properties to enable on a given pool |
| `enableRBDStats`   *bool* | EnableRBDStats is used to enable gathering of statistics for all RBD images in the pool |
| `mirroring`   *[MirroringSpec](index.md#ceph.rook.io/v1.MirroringSpec)* | The mirroring settings |
| `statusCheck`   *[MirrorHealthCheckSpec](index.md#ceph.rook.io/v1.MirrorHealthCheckSpec)* | The mirroring statusCheck |
| `quotas`   *[QuotaSpec](index.md#ceph.rook.io/v1.QuotaSpec)* | *(Optional)* The quota settings |
| `application`   *string* | *(Optional)* The application name to set on the pool. Only expected to be set for rgw pools. |

### PriorityClassNamesSpec (`map[github.com/rook/rook/pkg/apis/ceph.rook.io/v1.KeyType]string` alias)

(*Appears on:*[ClusterSpec](index.md#ceph.rook.io/v1.ClusterSpec))

PriorityClassNamesSpec is a map of priority class names to be assigned to components

### ProbeSpec

(*Appears on:*[GaneshaServerSpec](index.md#ceph.rook.io/v1.GaneshaServerSpec), [MetadataServerSpec](index.md#ceph.rook.io/v1.MetadataServerSpec), [ObjectHealthCheckSpec](index.md#ceph.rook.io/v1.ObjectHealthCheckSpec))

ProbeSpec is a wrapper around Probe so it can be enabled or disabled for a Ceph daemon

| Field | Description |
| --- | --- |
| `disabled`   *bool* | *(Optional)* Disabled determines whether probe is disable or not |
| `probe`   *[Kubernetes core/v1.Probe](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#probe-v1-core)* | *(Optional)* Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic. |

### ProtocolSpec

(*Appears on:*[ObjectStoreSpec](index.md#ceph.rook.io/v1.ObjectStoreSpec))

ProtocolSpec represents a Ceph Object Store protocol specification

| Field | Description |
| --- | --- |
| `enableAPIs`   *[[]ObjectStoreAPI](index.md#ceph.rook.io/v1.ObjectStoreAPI)* | *(Optional)* Represents RGW ‘rgw_enable_apis’ config option. See: <https://docs.ceph.com/en/reef/radosgw/config-ref/#confval-rgw_enable_apis> If no value provided then all APIs will be enabled: s3, s3website, swift, swift_auth, admin, sts, iam, notifications If enabled APIs are set, all remaining APIs will be disabled. This option overrides S3.Enabled value. |
| `s3`   *[S3Spec](index.md#ceph.rook.io/v1.S3Spec)* | *(Optional)* The spec for S3 |
| `swift`   *[SwiftSpec](index.md#ceph.rook.io/v1.SwiftSpec)* | *(Optional)* The spec for Swift |

### PullSpec

(*Appears on:*[ObjectRealmSpec](index.md#ceph.rook.io/v1.ObjectRealmSpec))

PullSpec represents the pulling specification of a Ceph Object Storage Gateway Realm

| Field | Description |
| --- | --- |
| `endpoint`   *string* |  |

### QuotaSpec

(*Appears on:*[PoolSpec](index.md#ceph.rook.io/v1.PoolSpec))

QuotaSpec represents the spec for quotas in a pool

| Field | Description |
| --- | --- |
| `maxBytes`   *uint64* | *(Optional)* MaxBytes represents the quota in bytes Deprecated in favor of MaxSize |
| `maxSize`   *string* | *(Optional)* MaxSize represents the quota in bytes as a string |
| `maxObjects`   *uint64* | *(Optional)* MaxObjects represents the quota in objects |

### RBDMirroringSpec

(*Appears on:*[CephRBDMirror](index.md#ceph.rook.io/v1.CephRBDMirror))

RBDMirroringSpec represents the specification of an RBD mirror daemon

| Field | Description |
| --- | --- |
| `count`   *int* | Count represents the number of rbd mirror instance to run |
| `peers`   *[MirroringPeerSpec](index.md#ceph.rook.io/v1.MirroringPeerSpec)* | *(Optional)* Peers represents the peers spec |
| `placement`   *[Placement](index.md#ceph.rook.io/v1.Placement)* | *(Optional)* The affinity to place the rgw pods (default is to place on any available node) |
| `annotations`   *[Annotations](index.md#ceph.rook.io/v1.Annotations)* | *(Optional)* The annotations-related configuration to add/set on each Pod related object. |
| `labels`   *[Labels](index.md#ceph.rook.io/v1.Labels)* | *(Optional)* The labels-related configuration to add/set on each Pod related object. |
| `resources`   *[Kubernetes core/v1.ResourceRequirements](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#resourcerequirements-v1-core)* | *(Optional)* The resource requirements for the rbd mirror pods |
| `priorityClassName`   *string* | *(Optional)* PriorityClassName sets priority class on the rbd mirror pods |

### RGWServiceSpec

(*Appears on:*[GatewaySpec](index.md#ceph.rook.io/v1.GatewaySpec))

RGWServiceSpec represent the spec for RGW service

| Field | Description |
| --- | --- |
| `annotations`   *[Annotations](index.md#ceph.rook.io/v1.Annotations)* | The annotations-related configuration to add/set on each rgw service. nullable optional |

### RadosNamespaceMirroring

(*Appears on:*[CephBlockPoolRadosNamespaceSpec](index.md#ceph.rook.io/v1.CephBlockPoolRadosNamespaceSpec))

RadosNamespaceMirroring represents the mirroring configuration of CephBlockPoolRadosNamespace

| Field | Description |
| --- | --- |
| `remoteNamespace`   *string* | *(Optional)* RemoteNamespace is the name of the CephBlockPoolRadosNamespace on the secondary cluster CephBlockPool |
| `mode`   *[RadosNamespaceMirroringMode](index.md#ceph.rook.io/v1.RadosNamespaceMirroringMode)* | Mode is the mirroring mode; either pool or image. |
| `snapshotSchedules`   *[[]SnapshotScheduleSpec](index.md#ceph.rook.io/v1.SnapshotScheduleSpec)* | *(Optional)* SnapshotSchedules is the scheduling of snapshot for mirrored images |

### RadosNamespaceMirroringMode (`string` alias)

(*Appears on:*[RadosNamespaceMirroring](index.md#ceph.rook.io/v1.RadosNamespaceMirroring))

RadosNamespaceMirroringMode represents the mode of the RadosNamespace

| Value | Description |
| --- | --- |
| "image" | RadosNamespaceMirroringModeImage represents the image mode |
| "pool" | RadosNamespaceMirroringModePool represents the pool mode |

### ReadAffinitySpec

(*Appears on:*[CSIDriverSpec](index.md#ceph.rook.io/v1.CSIDriverSpec))

ReadAffinitySpec defines the read affinity settings for CSI driver.

| Field | Description |
| --- | --- |
| `enabled`   *bool* | *(Optional)* Enables read affinity for CSI driver. |
| `crushLocationLabels`   *[]string* | *(Optional)* CrushLocationLabels defines which node labels to use as CRUSH location. This should correspond to the values set in the CRUSH map. |

### ReplicatedSpec

(*Appears on:*[PoolSpec](index.md#ceph.rook.io/v1.PoolSpec))

ReplicatedSpec represents the spec for replication in a pool

| Field | Description |
| --- | --- |
| `size`   *uint* | Size - Number of copies per object in a replicated storage pool, including the object itself (required for replicated pool type) |
| `targetSizeRatio`   *float64* | *(Optional)* TargetSizeRatio gives a hint (%) to Ceph in terms of expected consumption of the total cluster capacity |
| `requireSafeReplicaSize`   *bool* | *(Optional)* RequireSafeReplicaSize if false allows you to set replica 1 |
| `replicasPerFailureDomain`   *uint* | *(Optional)* ReplicasPerFailureDomain the number of replica in the specified failure domain |
| `subFailureDomain`   *string* | *(Optional)* SubFailureDomain the name of the sub-failure domain |
| `hybridStorage`   *[HybridStorageSpec](index.md#ceph.rook.io/v1.HybridStorageSpec)* | *(Optional)* HybridStorage represents hybrid storage tier settings |

### ResourceSpec (`map[string]k8s.io/api/core/v1.ResourceRequirements` alias)

(*Appears on:*[ClusterSpec](index.md#ceph.rook.io/v1.ClusterSpec))

ResourceSpec is a collection of ResourceRequirements that describes the compute resource requirements

### RgwReadAffinity

(*Appears on:*[GatewaySpec](index.md#ceph.rook.io/v1.GatewaySpec))

| Field | Description |
| --- | --- |
| `type`   *string* | Type defines the RGW ReadAffinity type localize: read from the nearest OSD based on crush location of the RGW client balance: picks a random OSD from the PG’s active set default: read from the primary OSD |

### S3Spec

(*Appears on:*[ProtocolSpec](index.md#ceph.rook.io/v1.ProtocolSpec))

S3Spec represents Ceph Object Store specification for the S3 API

| Field | Description |
| --- | --- |
| `enabled`   *bool* | *(Optional)* Deprecated: use protocol.enableAPIs instead. Whether to enable S3. This defaults to true (even if protocols.s3 is not present in the CRD). This maintains backwards compatibility – by default S3 is enabled. |
| `authUseKeystone`   *bool* | *(Optional)* Whether to use Keystone for authentication. This option maps directly to the rgw_s3_auth_use_keystone option. Enabling it allows generating S3 credentials via an OpenStack API call, see the docs. If not given, the defaults of the corresponding RGW option apply. |

### SSSDSidecar

(*Appears on:*[SSSDSpec](index.md#ceph.rook.io/v1.SSSDSpec))

SSSDSidecar represents configuration when SSSD is run in a sidecar.

| Field | Description |
| --- | --- |
| `image`   *string* | Image defines the container image that should be used for the SSSD sidecar. |
| `sssdConfigFile`   *[SSSDSidecarConfigFile](index.md#ceph.rook.io/v1.SSSDSidecarConfigFile)* | *(Optional)* SSSDConfigFile defines where the SSSD configuration should be sourced from. The config file will be placed into `/etc/sssd/sssd.conf`. If this is left empty, Rook will not add the file. This allows you to manage the `sssd.conf` file yourself however you wish. For example, you may build it into your custom Ceph container image or use the Vault agent injector to securely add the file via annotations on the CephNFS spec (passed to the NFS server pods). |
| `additionalFiles`   *[AdditionalVolumeMounts](index.md#ceph.rook.io/v1.AdditionalVolumeMounts)* | *(Optional)* AdditionalFiles defines any number of additional files that should be mounted into the SSSD sidecar with a directory root of `/etc/sssd/rook-additional/`. These files may be referenced by the sssd.conf config file. |
| `resources`   *[Kubernetes core/v1.ResourceRequirements](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#resourcerequirements-v1-core)* | *(Optional)* Resources allow specifying resource requests/limits on the SSSD sidecar container. |
| `debugLevel`   *int* | *(Optional)* DebugLevel sets the debug level for SSSD. If unset or set to 0, Rook does nothing. Otherwise, this may be a value between 1 and 10. See SSSD docs for more info: <https://sssd.io/troubleshooting/basics.html#sssd-debug-logs> |

### SSSDSidecarConfigFile

(*Appears on:*[SSSDSidecar](index.md#ceph.rook.io/v1.SSSDSidecar))

SSSDSidecarConfigFile represents the source(s) from which the SSSD configuration should come.

| Field | Description |
| --- | --- |
| `volumeSource`   *[ConfigFileVolumeSource](index.md#ceph.rook.io/v1.ConfigFileVolumeSource)* | VolumeSource accepts a pared down version of the standard Kubernetes VolumeSource for the SSSD configuration file like what is normally used to configure Volumes for a Pod. For example, a ConfigMap, Secret, or HostPath. There are two requirements for the source’s content: 1. The config file must be mountable via `subPath: sssd.conf`. For example, in a ConfigMap, the data item must be named `sssd.conf`, or `items` must be defined to select the key and give it path `sssd.conf`. A HostPath directory must have the `sssd.conf` file. 2. The volume or config file must have mode 0600. |

### SSSDSpec

(*Appears on:*[NFSSecuritySpec](index.md#ceph.rook.io/v1.NFSSecuritySpec))

SSSDSpec represents configuration for System Security Services Daemon (SSSD).

| Field | Description |
| --- | --- |
| `sidecar`   *[SSSDSidecar](index.md#ceph.rook.io/v1.SSSDSidecar)* | *(Optional)* Sidecar tells Rook to run SSSD in a sidecar alongside the NFS-Ganesha server in each NFS pod. |

### SanitizeDataSourceProperty (`string` alias)

(*Appears on:*[SanitizeDisksSpec](index.md#ceph.rook.io/v1.SanitizeDisksSpec))

SanitizeDataSourceProperty represents a sanitizing data source

| Value | Description |
| --- | --- |
| "random" | SanitizeDataSourceRandom uses `shred’s default entropy source |
| "zero" | SanitizeDataSourceZero uses /dev/zero as sanitize source |

### SanitizeDisksSpec

(*Appears on:*[CleanupPolicySpec](index.md#ceph.rook.io/v1.CleanupPolicySpec))

SanitizeDisksSpec represents a disk sanitizing specification

| Field | Description |
| --- | --- |
| `method`   *[SanitizeMethodProperty](index.md#ceph.rook.io/v1.SanitizeMethodProperty)* | *(Optional)* Method is the method we use to sanitize disks |
| `dataSource`   *[SanitizeDataSourceProperty](index.md#ceph.rook.io/v1.SanitizeDataSourceProperty)* | *(Optional)* DataSource is the data source to use to sanitize the disk with |
| `iteration`   *int32* | *(Optional)* Iteration is the number of pass to apply the sanitizing |

### SanitizeMethodProperty (`string` alias)

(*Appears on:*[SanitizeDisksSpec](index.md#ceph.rook.io/v1.SanitizeDisksSpec))

SanitizeMethodProperty represents a disk sanitizing method

| Value | Description |
| --- | --- |
| "complete" | SanitizeMethodComplete will sanitize everything on the disk |
| "quick" | SanitizeMethodQuick will sanitize metadata only on the disk |

### SecretReference

(*Appears on:*[BucketTopicStatus](index.md#ceph.rook.io/v1.BucketTopicStatus), [ObjectStoreUserStatus](index.md#ceph.rook.io/v1.ObjectStoreUserStatus))

| Field | Description |
| --- | --- |
| `,secretReference`   *[Kubernetes core/v1.SecretReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#secretreference-v1-core)* |  |
| `uid`   *k8s.io/apimachinery/pkg/types.UID* |  |
| `resourceVersion`   *string* |  |

### SecuritySpec

(*Appears on:*[ClusterSpec](index.md#ceph.rook.io/v1.ClusterSpec), [ObjectStoreSecuritySpec](index.md#ceph.rook.io/v1.ObjectStoreSecuritySpec))

SecuritySpec is security spec to include various security items such as kms

| Field | Description |
| --- | --- |
| `kms`   *[KeyManagementServiceSpec](index.md#ceph.rook.io/v1.KeyManagementServiceSpec)* | *(Optional)* KeyManagementService is the main Key Management option |
| `keyRotation`   *[KeyRotationSpec](index.md#ceph.rook.io/v1.KeyRotationSpec)* | *(Optional)* KeyRotation defines options for Key Rotation. |

### Selection

(*Appears on:*[Node](index.md#ceph.rook.io/v1.Node), [StorageScopeSpec](index.md#ceph.rook.io/v1.StorageScopeSpec))

| Field | Description |
| --- | --- |
| `useAllDevices`   *bool* | *(Optional)* Whether to consume all the storage devices found on a machine |
| `deviceFilter`   *string* | *(Optional)* A regular expression to allow more fine-grained selection of devices on nodes across the cluster |
| `devicePathFilter`   *string* | *(Optional)* A regular expression to allow more fine-grained selection of devices with path names |
| `devices`   *[[]Device](index.md#ceph.rook.io/v1.Device)* | *(Optional)* List of devices to use as storage devices |
| `volumeClaimTemplates`   *[[]VolumeClaimTemplate](index.md#ceph.rook.io/v1.VolumeClaimTemplate)* | *(Optional)* PersistentVolumeClaims to use as storage |

### SnapshotSchedule

(*Appears on:*[SnapshotSchedulesSpec](index.md#ceph.rook.io/v1.SnapshotSchedulesSpec))

SnapshotSchedule is a schedule

| Field | Description |
| --- | --- |
| `interval`   *string* | *(Optional)* Interval is the interval in which snapshots will be taken |
| `start_time`   *string* | *(Optional)* StartTime is the snapshot starting time |

### SnapshotScheduleRetentionSpec

(*Appears on:*[FSMirroringSpec](index.md#ceph.rook.io/v1.FSMirroringSpec))

SnapshotScheduleRetentionSpec is a retention policy

| Field | Description |
| --- | --- |
| `path`   *string* | *(Optional)* Path is the path to snapshot |
| `duration`   *string* | *(Optional)* Duration represents the retention duration for a snapshot |

### SnapshotScheduleSpec

(*Appears on:*[FSMirroringSpec](index.md#ceph.rook.io/v1.FSMirroringSpec), [MirroringSpec](index.md#ceph.rook.io/v1.MirroringSpec), [RadosNamespaceMirroring](index.md#ceph.rook.io/v1.RadosNamespaceMirroring))

SnapshotScheduleSpec represents the snapshot scheduling settings of a mirrored pool

| Field | Description |
| --- | --- |
| `path`   *string* | *(Optional)* Path is the path to snapshot, only valid for CephFS |
| `interval`   *string* | *(Optional)* Interval represent the periodicity of the snapshot. |
| `startTime`   *string* | *(Optional)* StartTime indicates when to start the snapshot |

### SnapshotScheduleStatusSpec

(*Appears on:*[CephBlockPoolRadosNamespaceStatus](index.md#ceph.rook.io/v1.CephBlockPoolRadosNamespaceStatus), [CephBlockPoolStatus](index.md#ceph.rook.io/v1.CephBlockPoolStatus))

SnapshotScheduleStatusSpec is the status of the snapshot schedule

| Field | Description |
| --- | --- |
| `snapshotSchedules`   *[[]SnapshotSchedulesSpec](index.md#ceph.rook.io/v1.SnapshotSchedulesSpec)* | *(Optional)* SnapshotSchedules is the list of snapshots scheduled |
| `lastChecked`   *string* | *(Optional)* LastChecked is the last time time the status was checked |
| `lastChanged`   *string* | *(Optional)* LastChanged is the last time time the status last changed |
| `details`   *string* | *(Optional)* Details contains potential status errors |

### SnapshotSchedulesSpec

(*Appears on:*[SnapshotScheduleStatusSpec](index.md#ceph.rook.io/v1.SnapshotScheduleStatusSpec))

SnapshotSchedulesSpec is the list of snapshot scheduled for images in a pool

| Field | Description |
| --- | --- |
| `pool`   *string* | *(Optional)* Pool is the pool name |
| `namespace`   *string* | *(Optional)* Namespace is the RADOS namespace the image is part of |
| `image`   *string* | *(Optional)* Image is the mirrored image |
| `items`   *[[]SnapshotSchedule](index.md#ceph.rook.io/v1.SnapshotSchedule)* | *(Optional)* Items is the list schedules times for a given snapshot |

### StatesSpec

(*Appears on:*[MirroringStatusSummarySpec](index.md#ceph.rook.io/v1.MirroringStatusSummarySpec))

StatesSpec are rbd images mirroring state

| Field | Description |
| --- | --- |
| `starting_replay`   *int* | *(Optional)* StartingReplay is when the replay of the mirroring journal starts |
| `replaying`   *int* | *(Optional)* Replaying is when the replay of the mirroring journal is on-going |
| `syncing`   *int* | *(Optional)* Syncing is when the image is syncing |
| `stopping_replay`   *int* | *(Optional)* StopReplaying is when the replay of the mirroring journal stops |
| `stopped`   *int* | *(Optional)* Stopped is when the mirroring state is stopped |
| `unknown`   *int* | *(Optional)* Unknown is when the mirroring state is unknown |
| `error`   *int* | *(Optional)* Error is when the mirroring state is errored |

### Status

(*Appears on:*[CephBucketNotification](index.md#ceph.rook.io/v1.CephBucketNotification), [CephFilesystemMirror](index.md#ceph.rook.io/v1.CephFilesystemMirror), [CephNFS](index.md#ceph.rook.io/v1.CephNFS), [CephObjectRealm](index.md#ceph.rook.io/v1.CephObjectRealm), [CephObjectZone](index.md#ceph.rook.io/v1.CephObjectZone), [CephObjectZoneGroup](index.md#ceph.rook.io/v1.CephObjectZoneGroup), [CephRBDMirror](index.md#ceph.rook.io/v1.CephRBDMirror))

Status represents the status of an object

| Field | Description |
| --- | --- |
| `phase`   *string* | *(Optional)* |
| `observedGeneration`   *int64* | *(Optional)* ObservedGeneration is the latest generation observed by the controller. |
| `conditions`   *[[]Condition](index.md#ceph.rook.io/v1.Condition)* |  |

### StorageClassDeviceSet

(*Appears on:*[StorageScopeSpec](index.md#ceph.rook.io/v1.StorageScopeSpec))

StorageClassDeviceSet is a storage class device set

| Field | Description |
| --- | --- |
| `name`   *string* | Name is a unique identifier for the set |
| `count`   *int* | Count is the number of devices in this set |
| `resources`   *[Kubernetes core/v1.ResourceRequirements](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#resourcerequirements-v1-core)* | *(Optional)* |
| `placement`   *[Placement](index.md#ceph.rook.io/v1.Placement)* | *(Optional)* |
| `preparePlacement`   *[Placement](index.md#ceph.rook.io/v1.Placement)* | *(Optional)* |
| `config`   *map[string]string* | *(Optional)* Provider-specific device configuration |
| `volumeClaimTemplates`   *[[]VolumeClaimTemplate](index.md#ceph.rook.io/v1.VolumeClaimTemplate)* | VolumeClaimTemplates is a list of PVC templates for the underlying storage devices |
| `portable`   *bool* | *(Optional)* Portable represents OSD portability across the hosts |
| `tuneDeviceClass`   *bool* | *(Optional)* TuneSlowDeviceClass Tune the OSD when running on a slow Device Class |
| `tuneFastDeviceClass`   *bool* | *(Optional)* TuneFastDeviceClass Tune the OSD when running on a fast Device Class |
| `schedulerName`   *string* | *(Optional)* Scheduler name for OSD pod placement |
| `encrypted`   *bool* | *(Optional)* Whether to encrypt the deviceSet |

### StorageScopeSpec

(*Appears on:*[ClusterSpec](index.md#ceph.rook.io/v1.ClusterSpec))

| Field | Description |
| --- | --- |
| `nodes`   *[[]Node](index.md#ceph.rook.io/v1.Node)* | *(Optional)* |
| `useAllNodes`   *bool* | *(Optional)* |
| `scheduleAlways`   *bool* | *(Optional)* Whether to always schedule OSDs on a node even if the node is not currently scheduleable or ready |
| `onlyApplyOSDPlacement`   *bool* | *(Optional)* |
| `config`   *map[string]string* | *(Optional)* |
| `Selection`   *[Selection](index.md#ceph.rook.io/v1.Selection)* | (Members of `Selection` are embedded into this type.) |
| `storageClassDeviceSets`   *[[]StorageClassDeviceSet](index.md#ceph.rook.io/v1.StorageClassDeviceSet)* | *(Optional)* |
| `migration`   *[Migration](index.md#ceph.rook.io/v1.Migration)* | *(Optional)* Migration handles the OSD migration |
| `store`   *[OSDStore](index.md#ceph.rook.io/v1.OSDStore)* | *(Optional)* |
| `flappingRestartIntervalHours`   *int* | *(Optional)* FlappingRestartIntervalHours defines the time for which the OSD pods, that failed with zero exit code, will sleep before restarting. This is needed for OSD flapping where OSD daemons are marked down more than 5 times in 600 seconds by Ceph. Preventing the OSD pods to restart immediately in such scenarios will prevent Rook from marking OSD as `up` and thus peering of the PGs mapped to the OSD. User needs to manually restart the OSD pod if they manage to fix the underlying OSD flapping issue before the restart interval. The sleep will be disabled if this interval is set to 0. |
| `fullRatio`   *float64* | *(Optional)* FullRatio is the ratio at which the cluster is considered full and ceph will stop accepting writes. Default is 0.95. |
| `nearFullRatio`   *float64* | *(Optional)* NearFullRatio is the ratio at which the cluster is considered nearly full and will raise a ceph health warning. Default is 0.85. |
| `backfillFullRatio`   *float64* | *(Optional)* BackfillFullRatio is the ratio at which the cluster is too full for backfill. Backfill will be disabled if above this threshold. Default is 0.90. |
| `allowDeviceClassUpdate`   *bool* | *(Optional)* Whether to allow updating the device class after the OSD is initially provisioned |
| `allowOsdCrushWeightUpdate`   *bool* | *(Optional)* Whether Rook will resize the OSD CRUSH weight when the OSD PVC size is increased. This allows cluster data to be rebalanced to make most effective use of new OSD space. The default is false since data rebalancing can cause temporary cluster slowdown. |

### StoreType (`string` alias)

| Value | Description |
| --- | --- |
| "bluestore" | StoreTypeBlueStore is the bluestore backend storage for OSDs |
| "bluestore-rdr" | StoreTypeBlueStoreRDR is the bluestore-rdr backed storage for OSDs |

### StretchClusterSpec

(*Appears on:*[MonSpec](index.md#ceph.rook.io/v1.MonSpec))

StretchClusterSpec represents the specification of a stretched Ceph Cluster

| Field | Description |
| --- | --- |
| `failureDomainLabel`   *string* | *(Optional)* FailureDomainLabel the failure domain name (e,g: zone) |
| `subFailureDomain`   *string* | *(Optional)* SubFailureDomain is the failure domain within a zone |
| `zones`   *[[]MonZoneSpec](index.md#ceph.rook.io/v1.MonZoneSpec)* | *(Optional)* Zones is the list of zones |

### SwiftSpec

(*Appears on:*[ProtocolSpec](index.md#ceph.rook.io/v1.ProtocolSpec))

SwiftSpec represents Ceph Object Store specification for the Swift API

| Field | Description |
| --- | --- |
| `accountInUrl`   *bool* | *(Optional)* Whether or not the Swift account name should be included in the Swift API URL. If set to false (the default), then the Swift API will listen on a URL formed like <http://host:port/>/v1. If set to true, the Swift API URL will be <http://host:port/>/v1/AUTH_. You must set this option to true (and update the Keystone service catalog) if you want radosgw to support publicly-readable containers and temporary URLs. |
| `urlPrefix`   *string* | *(Optional)* The URL prefix for the Swift API, to distinguish it from the S3 API endpoint. The default is swift, which makes the Swift API available at the URL <http://host:port/swift/v1> (or <http://host:port/swift/v1/AUTH_%(tenant_id)s> if rgw swift account in url is enabled). |
| `versioningEnabled`   *bool* | *(Optional)* Enables the Object Versioning of OpenStack Object Storage API. This allows clients to put the X-Versions-Location attribute on containers that should be versioned. |

### TopicEndpointSpec

(*Appears on:*[BucketTopicSpec](index.md#ceph.rook.io/v1.BucketTopicSpec))

TopicEndpointSpec contains exactly one of the endpoint specs of a Bucket Topic

| Field | Description |
| --- | --- |
| `http`   *[HTTPEndpointSpec](index.md#ceph.rook.io/v1.HTTPEndpointSpec)* | *(Optional)* Spec of HTTP endpoint |
| `amqp`   *[AMQPEndpointSpec](index.md#ceph.rook.io/v1.AMQPEndpointSpec)* | *(Optional)* Spec of AMQP endpoint |
| `kafka`   *[KafkaEndpointSpec](index.md#ceph.rook.io/v1.KafkaEndpointSpec)* | *(Optional)* Spec of Kafka endpoint |

### VolumeClaimTemplate

(*Appears on:*[MonSpec](index.md#ceph.rook.io/v1.MonSpec), [MonZoneSpec](index.md#ceph.rook.io/v1.MonZoneSpec), [Selection](index.md#ceph.rook.io/v1.Selection), [StorageClassDeviceSet](index.md#ceph.rook.io/v1.StorageClassDeviceSet))

VolumeClaimTemplate is a simplified version of K8s corev1’s PVC. It has no type meta or status.

| Field | Description |
| --- | --- |
| `metadata`   *[Kubernetes meta/v1.ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#objectmeta-v1-meta)* | *(Optional)* Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> Refer to the Kubernetes API documentation for the fields of the `metadata` field. |
| `spec`   *[Kubernetes core/v1.PersistentVolumeClaimSpec](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#persistentvolumeclaimspec-v1-core)* | *(Optional)* spec defines the desired characteristics of a volume requested by a pod author. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims>      |  |  | | --- | --- | | `accessModes`   *[[]Kubernetes core/v1.PersistentVolumeAccessMode](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#persistentvolumeaccessmode-v1-core)* | *(Optional)* accessModes contains the desired access modes the volume should have. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1> | | `selector`   *[Kubernetes meta/v1.LabelSelector](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#labelselector-v1-meta)* | *(Optional)* selector is a label query over volumes to consider for binding. | | `resources`   *[Kubernetes core/v1.VolumeResourceRequirements](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#volumeresourcerequirements-v1-core)* | *(Optional)* resources represents the minimum resources the volume should have. If RecoverVolumeExpansionFailure feature is enabled users are allowed to specify resource requirements that are lower than previous value but must still be higher than capacity recorded in the status field of the claim. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources> | | `volumeName`   *string* | *(Optional)* volumeName is the binding reference to the PersistentVolume backing this claim. | | `storageClassName`   *string* | *(Optional)* storageClassName is the name of the StorageClass required by the claim. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1> | | `volumeMode`   *[Kubernetes core/v1.PersistentVolumeMode](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#persistentvolumemode-v1-core)* | *(Optional)* volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec. | | `dataSource`   *[Kubernetes core/v1.TypedLocalObjectReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#typedlocalobjectreference-v1-core)* | *(Optional)* dataSource field can be used to specify either: \* An existing VolumeSnapshot object (snapshot.storage.k8s.io/VolumeSnapshot) \* An existing PVC (PersistentVolumeClaim) If the provisioner or an external controller can support the specified data source, it will create a new volume based on the contents of the specified data source. When the AnyVolumeDataSource feature gate is enabled, dataSource contents will be copied to dataSourceRef, and dataSourceRef contents will be copied to dataSource when dataSourceRef.namespace is not specified. If the namespace is specified, then dataSourceRef will not be copied to dataSource. | | `dataSourceRef`   *[Kubernetes core/v1.TypedObjectReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#typedobjectreference-v1-core)* | *(Optional)* dataSourceRef specifies the object from which to populate the volume with data, if a non-empty volume is desired. This may be any object from a non-empty API group (non core object) or a PersistentVolumeClaim object. When this field is specified, volume binding will only succeed if the type of the specified object matches some installed volume populator or dynamic provisioner. This field will replace the functionality of the dataSource field and as such if both fields are non-empty, they must have the same value. For backwards compatibility, when namespace isn’t specified in dataSourceRef, both fields (dataSource and dataSourceRef) will be set to the same value automatically if one of them is empty and the other is non-empty. When namespace is specified in dataSourceRef, dataSource isn’t set to the same value and must be empty. There are three important differences between dataSource and dataSourceRef: \* While dataSource only allows two specific types of objects, dataSourceRef allows any non-core object, as well as PersistentVolumeClaim objects. \* While dataSource ignores disallowed values (dropping them), dataSourceRef preserves all values, and generates an error if a disallowed value is specified. \* While dataSource only allows local objects, dataSourceRef allows objects in any namespaces. (Beta) Using this field requires the AnyVolumeDataSource feature gate to be enabled. (Alpha) Using the namespace field of dataSourceRef requires the CrossNamespaceVolumeDataSource feature gate to be enabled. | | `volumeAttributesClassName`   *string* | *(Optional)* volumeAttributesClassName may be used to set the VolumeAttributesClass used by this claim. If specified, the CSI driver will create or update the volume with the attributes defined in the corresponding VolumeAttributesClass. This has a different purpose than storageClassName, it can be changed after the claim is created. An empty string value means that no VolumeAttributesClass will be applied to the claim but it’s not allowed to reset this field to empty string once it is set. If unspecified and the PersistentVolumeClaim is unbound, the default VolumeAttributesClass will be set by the persistentvolume controller if it exists. If the resource referred to by volumeAttributesClass does not exist, this PersistentVolumeClaim will be set to a Pending state, as reflected by the modifyVolumeStatus field, until such as a resource exists. More info: <https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/> (Beta) Using this field requires the VolumeAttributesClass feature gate to be enabled (off by default). | |

### ZoneSpec

(*Appears on:*[ObjectStoreSpec](index.md#ceph.rook.io/v1.ObjectStoreSpec))

ZoneSpec represents a Ceph Object Store Gateway Zone specification

| Field | Description |
| --- | --- |
| `name`   *string* | CephObjectStoreZone name this CephObjectStore is part of |

---

*Generated with `gen-crd-api-reference-docs`.*
