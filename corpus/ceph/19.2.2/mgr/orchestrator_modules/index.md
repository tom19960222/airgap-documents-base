---
collection: ceph
version: "19.2.2"
title: "ceph-mgr orchestrator modules"
source_url: https://docs.ceph.com/en/squid/mgr/orchestrator_modules/
fetched_at: 2026-07-27T16:40:48+00:00
---
# ceph-mgr orchestrator modules

> **Warning:**
>
> This is developer documentation, describing Ceph internals that
> are only relevant to people writing ceph-mgr orchestrator modules.

In this context, *orchestrator* refers to some external service that
provides the ability to discover devices and create Ceph services. This
includes external projects such as Rook.

An *orchestrator module* is a ceph-mgr module ([ceph-mgr module developer’s guide](../modules/index.md#mgr-module-dev))
which implements common management operations using a particular
orchestrator.

Orchestrator modules subclass the `Orchestrator` class: this class is
an interface, it only provides method definitions to be implemented
by subclasses. The purpose of defining this common interface
for different orchestrators is to enable common UI code, such as
the dashboard, to work with various different backends.

digraph G {
subgraph cluster_1 {
volumes [label="mgr/volumes"]
rook [label="mgr/rook"]
dashboard [label="mgr/dashboard"]
orchestrator_cli [label="mgr/orchestrator"]
orchestrator [label="Orchestrator Interface"]
cephadm [label="mgr/cephadm"]
label = "ceph-mgr";
}
volumes -> orchestrator
dashboard -> orchestrator
orchestrator_cli -> orchestrator
orchestrator -> rook -> rook_io
orchestrator -> cephadm
rook_io [label="Rook"]
rankdir="TB";
}

Behind all the abstraction, the purpose of orchestrator modules is simple:
enable Ceph to do things like discover available hardware, create and
destroy OSDs, and run MDS and RGW services.

A tutorial is not included here: for full and concrete examples, see
the existing implemented orchestrator modules in the Ceph source tree.

## Glossary

Stateful service
:   a daemon that uses local storage, such as OSD or mon.

Stateless service
:   a daemon that doesn’t use any local storage, such
    as an MDS, RGW, nfs-ganesha, iSCSI gateway.

Label
:   arbitrary string tags that may be applied by administrators
    to hosts. Typically administrators use labels to indicate
    which hosts should run which kinds of service. Labels are
    advisory (from human input) and do not guarantee that hosts
    have particular physical capabilities.

Drive group
:   collection of block devices with common/shared OSD
    formatting (typically one or more SSDs acting as
    journals/dbs for a group of HDDs).

Placement
:   choice of which host is used to run a service.

## Key Concepts

The underlying orchestrator remains the source of truth for information
about whether a service is running, what is running where, which
hosts are available, etc. Orchestrator modules should avoid taking
any internal copies of this information, and read it directly from
the orchestrator backend as much as possible.

Bootstrapping hosts and adding them to the underlying orchestration
system is outside the scope of Ceph’s orchestrator interface. Ceph
can only work on hosts when the orchestrator is already aware of them.

Where possible, placement of stateless services should be left up to the
orchestrator.

## Completions and batching

All methods that read or modify the state of the system can potentially
be long running. Therefore the module needs to schedule those operations.

Each orchestrator module implements its own underlying mechanisms
for completions. This might involve running the underlying operations
in threads, or batching the operations up before later executing
in one go in the background. If implementing such a batching pattern, the
module would do no work on any operation until it appeared in a list
of completions passed into *process*.

## Error Handling

The main goal of error handling within orchestrator modules is to provide debug information to
assist users when dealing with deployment errors.

*class* orchestrator.OrchestratorError(*msg*, *errno=-22*, *event_kind_subject=None*)
:   General orchestrator specific error.

    Used for deployment, configuration or user errors.

    It’s not intended for programming errors or orchestrator internal errors.

*class* orchestrator.NoOrchestrator(*msg='No orchestrator configured (try `ceph orch set backend`)'*)
:   No orchestrator in configured.

*class* orchestrator.OrchestratorValidationError(*msg*, *errno=-22*, *event_kind_subject=None*)
:   Raised when an orchestrator doesn’t support a specific feature.

In detail, orchestrators need to explicitly deal with different kinds of errors:

1. No orchestrator configured

   See [`NoOrchestrator`](index.md#orchestrator.NoOrchestrator "orchestrator.NoOrchestrator").
2. An orchestrator doesn’t implement a specific method.

   For example, an Orchestrator doesn’t support `add_host`.

   In this case, a `NotImplementedError` is raised.
3. Missing features within implemented methods.

   E.g. optional parameters to a command that are not supported by the
   backend (e.g. the hosts field in `Orchestrator.apply_mons()` command with the rook backend).

   See [`OrchestratorValidationError`](index.md#orchestrator.OrchestratorValidationError "orchestrator.OrchestratorValidationError").
4. Input validation errors

   The `orchestrator` module and other calling modules are supposed to
   provide meaningful error messages.

   See [`OrchestratorValidationError`](index.md#orchestrator.OrchestratorValidationError "orchestrator.OrchestratorValidationError").
5. Errors when actually executing commands

   The resulting Completion should contain an error string that assists in understanding the
   problem. In addition, `Completion.is_errored()` is set to `True`
6. Invalid configuration in the orchestrator modules

   This can be tackled similar to 5.

All other errors are unexpected orchestrator issues and thus should raise an exception that are then
logged into the mgr log file. If there is a completion object at that point,
`Completion.result()` may contain an error message.

## Excluded functionality

- Ceph’s orchestrator interface is not a general purpose framework for
  managing linux servers -- it is deliberately constrained to manage
  the Ceph cluster’s services only.
- Multipathed storage is not handled (multipathing is unnecessary for
  Ceph clusters). Each drive is assumed to be visible only on
  a single host.

## Host management

Orchestrator.add_host(*host_spec*)
:   Add a host to the orchestrator inventory.

    Parameters:
    :   **host** -- hostname

    Return type:
    :   `OrchResult`[`str`]

Orchestrator.remove_host(*host*, *force*, *offline*, *rm_crush_entry*)
:   Remove a host from the orchestrator inventory.

    Parameters:
    :   **host** (`str`) -- hostname

    Return type:
    :   `OrchResult`[`str`]

Orchestrator.get_hosts()
:   Report the hosts in the cluster.

    Return type:
    :   `OrchResult`[`List`[[`HostSpec`](index.md#orchestrator.HostSpec "ceph.deployment.hostspec.HostSpec")]]

    Returns:
    :   list of HostSpec

Orchestrator.update_host_addr(*host*, *addr*)
:   Update a host’s address

    Parameters:
    :   - **host** (`str`) -- hostname
        - **addr** (`str`) -- address (dns name or IP)

    Return type:
    :   `OrchResult`[`str`]

Orchestrator.add_host_label(*host*, *label*)
:   Add a host label

    Return type:
    :   `OrchResult`[`str`]

Orchestrator.remove_host_label(*host*, *label*, *force=False*)
:   Remove a host label

    Return type:
    :   `OrchResult`[`str`]

*class* orchestrator.HostSpec(*hostname*, *addr=None*, *labels=None*, *status=None*, *location=None*, *oob=None*)
:   Information about hosts. Like e.g. `kubectl get nodes`

## Devices

Orchestrator.get_inventory(*host_filter=None*, *refresh=False*)
:   Returns something that was created by ceph-volume inventory.

    Return type:
    :   `OrchResult`[`List`[`InventoryHost`]]

    Returns:
    :   list of InventoryHost

*class* orchestrator.InventoryFilter(*labels=None*, *hosts=None*)
:   When fetching inventory, use this filter to avoid unnecessarily
    scanning the whole estate.

    Typical use:

    > filter by host when presenting UI workflow for configuring
    > a particular server.
    > filter by label when not all of estate is Ceph servers,
    > and we want to only learn about the Ceph servers.
    > filter by label when we are interested particularly
    > in e.g. OSD servers.

*class* ceph.deployment.inventory.Devices(*devices*)
:   A container for Device instances with reporting

*class* ceph.deployment.inventory.Device(*path*, *sys_api=None*, *available=None*, *rejected_reasons=None*, *lvs=None*, *device_id=None*, *lsm_data=None*, *created=None*, *ceph_device=None*, *crush_device_class=None*, *being_replaced=None*)

## Placement

A [Daemon Placement](../../cephadm/services/index.md#orchestrator-cli-placement-spec) defines the placement of
daemons of a specific service.

In general, stateless services do not require any specific placement
rules as they can run anywhere that sufficient system resources
are available. However, some orchestrators may not include the
functionality to choose a location in this way. Optionally, you can
specify a location when creating a stateless service.

*class* ceph.deployment.service_spec.PlacementSpec(*label=None*, *hosts=None*, *count=None*, *count_per_host=None*, *host_pattern=None*)
:   For APIs that need to specify a host subset

    *classmethod* from_string(*arg*)
    :   A single integer is parsed as a count:

        ```
        >>> PlacementSpec.from_string('3')
        PlacementSpec(count=3)
        ```

        A list of names is parsed as host specifications:

        ```
        >>> PlacementSpec.from_string('host1 host2')
        PlacementSpec(hosts=[HostPlacementSpec(hostname='host1', network='', name=''), HostPlacementSpec(hostname='host2', network='', name='')])
        ```

        You can also prefix the hosts with a count as follows:

        ```
        >>> PlacementSpec.from_string('2 host1 host2')
        PlacementSpec(count=2, hosts=[HostPlacementSpec(hostname='host1', network='', name=''), HostPlacementSpec(hostname='host2', network='', name='')])
        ```

        You can specify labels using label:<label>

        ```
        >>> PlacementSpec.from_string('label:mon')
        PlacementSpec(label='mon')
        ```

        Labels also support a count:

        ```
        >>> PlacementSpec.from_string('3 label:mon')
        PlacementSpec(count=3, label='mon')
        ```

        You can specify a regex to match with regex:<regex>

        ```
        >>> PlacementSpec.from_string('regex:Foo[0-9]|Bar[0-9]')
        PlacementSpec(host_pattern=HostPattern(pattern='Foo[0-9]|Bar[0-9]', pattern_type=PatternType.regex))
        ```

        fnmatch is the default for a single string if “regex:” is not provided:

        ```
        >>> PlacementSpec.from_string('data[1-3]')
        PlacementSpec(host_pattern=HostPattern(pattern='data[1-3]', pattern_type=PatternType.fnmatch))
        ```

        ```
        >>> PlacementSpec.from_string(None)
        PlacementSpec()
        ```

        Return type:
        :   [`PlacementSpec`](index.md#ceph.deployment.service_spec.PlacementSpec "ceph.deployment.service_spec.PlacementSpec")

    host_pattern*: HostPattern*
    :   fnmatch patterns to select hosts. Can also be a single host.

    pretty_str()
    :   ```
        >>> 
        ... ps = PlacementSpec(...)  # For all placement specs:
        ... PlacementSpec.from_string(ps.pretty_str()) == ps
        ```

        Return type:
        :   `str`

## Services

*class* orchestrator.ServiceDescription(*spec*, *container_image_id=None*, *container_image_name=None*, *service_url=None*, *last_refresh=None*, *created=None*, *deleted=None*, *size=0*, *running=0*, *events=None*, *virtual_ip=None*, *ports=[]*)
:   For responding to queries about the status of a particular service,
    stateful or stateless.

    This is not about health or performance monitoring of services: it’s
    about letting the orchestrator tell Ceph whether and where a
    service is scheduled in the cluster. When an orchestrator tells
    Ceph “it’s running on host123”, that’s not a promise that the process
    is literally up this second, it’s a description of where the orchestrator
    has decided the service should run.

*class* ceph.deployment.service_spec.ServiceSpec(*service_type*, *service_id=None*, *placement=None*, *count=None*, *config=None*, *unmanaged=False*, *preview_only=False*, *networks=None*, *targets=None*, *extra_container_args=None*, *extra_entrypoint_args=None*, *custom_configs=None*)
:   Details of service creation.

    Request to the orchestrator for a cluster of daemons
    such as MDS, RGW, iscsi gateway, nvmeof gateway, MONs, MGRs, Prometheus

    This structure is supposed to be enough information to
    start the services.

    *classmethod* from_json(*cls*, *json_spec*)
    :   Initialize ‘ServiceSpec’ object data from a json structure

        There are two valid styles for service specs:

        the “old” style:

        ```yaml
        service_type: nfs
        service_id: foo
        pool: mypool
        namespace: myns
        ```

        and the “new” style:

        ```yaml
        service_type: nfs
        service_id: foo
        config:
          some_option: the_value
        networks: [10.10.0.0/16]
        spec:
          pool: mypool
          namespace: myns
        ```

        In <https://tracker.ceph.com/issues/45321> we decided that we’d like to
        prefer the new style as it is more readable and provides a better
        understanding of what fields are special for a give service type.

        Note, we’ll need to stay compatible with both versions for the
        the next two major releases (octopus, pacific).

        Parameters:
        :   **json_spec** (`Dict`) -- A valid dict with ServiceSpec

        Return type:
        :   `TypeVar`(`ServiceSpecT`, bound= [`ServiceSpec`](../../cephadm/services/index.md#ceph.deployment.service_spec.ServiceSpec "ceph.deployment.service_spec.ServiceSpec"))

    networks*: List[str]*
    :   A list of network identities instructing the daemons to only bind
        on the particular networks in that list. In case the cluster is distributed
        across multiple networks, you can add multiple networks. See
        [Networks and Ports](../../cephadm/services/monitoring/index.md#cephadm-monitoring-networks-ports),
        [Specifying Networks](../../cephadm/services/rgw/index.md#cephadm-rgw-networks) and [Specifying Networks](../../cephadm/services/mgr/index.md#cephadm-mgr-networks).

    placement*: [PlacementSpec](index.md#ceph.deployment.service_spec.PlacementSpec "ceph.deployment.service_spec.PlacementSpec")*
    :   See [Daemon Placement](../../cephadm/services/index.md#orchestrator-cli-placement-spec).

    service_id
    :   The name of the service. Required for `iscsi`, `nvmeof`, `mds`, `nfs`, `osd`,
        `rgw`, `container`, `ingress`

    service_type
    :   The type of the service. Needs to be either a Ceph
        service (`mon`, `crash`, `mds`, `mgr`, `osd` or
        `rbd-mirror`), a gateway (`nfs` or `rgw`), part of the
        monitoring stack (`alertmanager`, `grafana`, `node-exporter` or
        `prometheus`) or (`container`) for custom containers.

    unmanaged
    :   If set to `true`, the orchestrator will not deploy nor remove
        any daemon associated with this service. Placement and all other properties
        will be ignored. This is useful, if you do not want this service to be
        managed temporarily. For cephadm, See [Disabling automatic deployment of daemons](../../cephadm/services/index.md#cephadm-spec-unmanaged)

Orchestrator.describe_service(*service_type=None*, *service_name=None*, *refresh=False*)
:   Describe a service (of any kind) that is already configured in
    the orchestrator. For example, when viewing an OSD in the dashboard
    we might like to also display information about the orchestrator’s
    view of the service (like the kubernetes pod ID).

    When viewing a CephFS filesystem in the dashboard, we would use this
    to display the pods being currently run for MDS daemons.

    Return type:
    :   `OrchResult`[`List`[[`ServiceDescription`](index.md#orchestrator.ServiceDescription "orchestrator._interface.ServiceDescription")]]

    Returns:
    :   list of ServiceDescription objects.

Orchestrator.service_action(*action*, *service_name*)
:   Perform an action (start/stop/reload) on a service (i.e., all daemons
    providing the logical service).

    Parameters:
    :   - **action** (`str`) -- one of “start”, “stop”, “restart”, “redeploy”, “reconfig”
        - **service_name** (`str`) -- service_type + ‘.’ + service_id
          (e.g. “mon”, “mgr”, “mds.mycephfs”, “rgw.realm.zone”, …)

    Return type:
    :   OrchResult

Orchestrator.remove_service(*service_name*, *force=False*)
:   Remove a service (a collection of daemons).

    Return type:
    :   `OrchResult`[`str`]

    Returns:
    :   None

## Daemons

Orchestrator.list_daemons(*service_name=None*, *daemon_type=None*, *daemon_id=None*, *host=None*, *refresh=False*)
:   Describe a daemon (of any kind) that is already configured in
    the orchestrator.

    Return type:
    :   `OrchResult`[`List`[[`DaemonDescription`](index.md#orchestrator.DaemonDescription "orchestrator._interface.DaemonDescription")]]

    Returns:
    :   list of DaemonDescription objects.

Orchestrator.remove_daemons(*names*)
:   Remove specific daemon(s).

    Return type:
    :   `OrchResult`[`List`[`str`]]

    Returns:
    :   None

Orchestrator.daemon_action(*action*, *daemon_name*, *image=None*)
:   Perform an action (start/stop/reload) on a daemon.

    Parameters:
    :   - **action** (`str`) -- one of “start”, “stop”, “restart”, “redeploy”, “reconfig”
        - **daemon_name** (`str`) -- name of daemon
        - **image** (`Optional`[`str`]) -- Container image when redeploying that daemon

    Return type:
    :   OrchResult

*class* orchestrator.DaemonDescription(*daemon_type=None*, *daemon_id=None*, *hostname=None*, *container_id=None*, *container_image_id=None*, *container_image_name=None*, *container_image_digests=None*, *version=None*, *status=None*, *status_desc=None*, *last_refresh=None*, *created=None*, *started=None*, *last_configured=None*, *osdspec_affinity=None*, *last_deployed=None*, *events=None*, *is_active=False*, *memory_usage=None*, *memory_request=None*, *memory_limit=None*, *cpu_percentage=None*, *service_name=None*, *ports=None*, *ip=None*, *deployed_by=None*, *systemd_unit=None*, *rank=None*, *rank_generation=None*, *extra_container_args=None*, *extra_entrypoint_args=None*)
:   For responding to queries about the status of a particular daemon,
    stateful or stateless.

    This is not about health or performance monitoring of daemons: it’s
    about letting the orchestrator tell Ceph whether and where a
    daemon is scheduled in the cluster. When an orchestrator tells
    Ceph “it’s running on host123”, that’s not a promise that the process
    is literally up this second, it’s a description of where the orchestrator
    has decided the daemon should run.

*class* orchestrator.DaemonDescriptionStatus(*value*)
:   An enumeration.

## OSD management

Orchestrator.create_osds(*drive_group*)
:   Create one or more OSDs within a single Drive Group.

    The principal argument here is the drive_group member
    of OsdSpec: other fields are advisory/extensible for any
    finer-grained OSD feature enablement (choice of backing store,
    compression/encryption, etc).

    Return type:
    :   `OrchResult`[`str`]

Orchestrator.blink_device_light(*ident_fault*, *on*, *locations*)
:   Instructs the orchestrator to enable or disable either the ident or the fault LED.

    Parameters:
    :   - **ident_fault** (`str`) -- either `"ident"` or `"fault"`
        - **on** (`bool`) -- `True` = on.
        - **locations** (`List`[[`DeviceLightLoc`](index.md#orchestrator.DeviceLightLoc "orchestrator._interface.DeviceLightLoc")]) -- See [`orchestrator.DeviceLightLoc`](index.md#orchestrator.DeviceLightLoc "orchestrator.DeviceLightLoc")

    Return type:
    :   `OrchResult`[`List`[`str`]]

*class* orchestrator.DeviceLightLoc(*host*, *dev*, *path*)
:   Describes a specific device on a specific host. Used for enabling or disabling LEDs
    on devices.

    hostname as in [`orchestrator.Orchestrator.get_hosts()`](index.md#orchestrator.Orchestrator.get_hosts "orchestrator.Orchestrator.get_hosts")

    device_id: e.g. `ABC1234DEF567-1R1234_ABC8DE0Q`.
    :   See `ceph osd metadata | jq '.[].device_ids'`

### OSD Replacement

See [Replacing an OSD](../../rados/operations/add-or-rm-osds/index.md#rados-replacing-an-osd) for the underlying process.

Replacing OSDs is fundamentally a two-staged process, as users need to
physically replace drives. The orchestrator therefore exposes this two-staged process.

Phase one is a call to [`Orchestrator.remove_daemons()`](index.md#orchestrator.Orchestrator.remove_daemons "orchestrator.Orchestrator.remove_daemons") with `destroy=True` in order to mark
the OSD as destroyed.

Phase two is a call to [`Orchestrator.create_osds()`](index.md#orchestrator.Orchestrator.create_osds "orchestrator.Orchestrator.create_osds") with a Drive Group with

[`DriveGroupSpec.osd_id_claims`](../../cephadm/services/osd/index.md#ceph.deployment.drive_group.DriveGroupSpec.osd_id_claims "ceph.deployment.drive_group.DriveGroupSpec.osd_id_claims") set to the destroyed OSD ids.

## Services

Orchestrator.add_daemon(*spec*)
:   Create daemons daemon(s) for unmanaged services

    Return type:
    :   `OrchResult`[`List`[`str`]]

Orchestrator.apply_mon(*spec*)
:   Update mon cluster

    Return type:
    :   `OrchResult`[`str`]

Orchestrator.apply_mgr(*spec*)
:   Update mgr cluster

    Return type:
    :   `OrchResult`[`str`]

Orchestrator.apply_mds(*spec*)
:   Update MDS cluster

    Return type:
    :   `OrchResult`[`str`]

Orchestrator.apply_rbd_mirror(*spec*)
:   Update rbd-mirror cluster

    Return type:
    :   `OrchResult`[`str`]

*class* ceph.deployment.service_spec.RGWSpec(*service_type='rgw'*, *service_id=None*, *placement=None*, *rgw_realm=None*, *rgw_zonegroup=None*, *rgw_zone=None*, *rgw_frontend_port=None*, *rgw_frontend_ssl_certificate=None*, *rgw_frontend_type=None*, *rgw_frontend_extra_args=None*, *unmanaged=False*, *ssl=False*, *preview_only=False*, *config=None*, *networks=None*, *subcluster=None*, *extra_container_args=None*, *extra_entrypoint_args=None*, *custom_configs=None*, *rgw_realm_token=None*, *update_endpoints=False*, *zone_endpoints=None*, *zonegroup_hostnames=None*, *rgw_user_counters_cache=False*, *rgw_user_counters_cache_size=None*, *rgw_bucket_counters_cache=False*, *rgw_bucket_counters_cache_size=None*, *disable_multisite_sync_traffic=None*)
:   Settings to configure a (multisite) Ceph RGW

    ```yaml
    service_type: rgw
    service_id: myrealm.myzone
    spec:
        rgw_realm: myrealm
        rgw_zonegroup: myzonegroup
        rgw_zone: myzone
        ssl: true
        rgw_frontend_port: 1234
        rgw_frontend_type: beast
        rgw_frontend_ssl_certificate: ...
    ```

    See also: [Service Specification](../../cephadm/services/index.md#orchestrator-cli-service-spec)

Orchestrator.apply_rgw(*spec*)
:   Update RGW cluster

    Return type:
    :   `OrchResult`[`str`]

*class* ceph.deployment.service_spec.NFSServiceSpec(*service_type='nfs'*, *service_id=None*, *placement=None*, *unmanaged=False*, *preview_only=False*, *config=None*, *networks=None*, *port=None*, *virtual_ip=None*, *enable_nlm=False*, *enable_haproxy_protocol=False*, *extra_container_args=None*, *extra_entrypoint_args=None*, *idmap_conf=None*, *custom_configs=None*)

Orchestrator.apply_nfs(*spec*)
:   Update NFS cluster

    Return type:
    :   `OrchResult`[`str`]

## Upgrades

Orchestrator.upgrade_available()
:   Report on what versions are available to upgrade to

    Return type:
    :   `OrchResult`

    Returns:
    :   List of strings

Orchestrator.upgrade_start(*image*, *version*, *daemon_types*, *hosts*, *services*, *limit*)
:   Return type:
    :   `OrchResult`[`str`]

Orchestrator.upgrade_status()
:   If an upgrade is currently underway, report on where
    we are in the process, or if some error has occurred.

    Return type:
    :   `OrchResult`[[`UpgradeStatusSpec`](index.md#orchestrator.UpgradeStatusSpec "orchestrator._interface.UpgradeStatusSpec")]

    Returns:
    :   UpgradeStatusSpec instance

*class* orchestrator.UpgradeStatusSpec

## Utility

Orchestrator.available()
:   Report whether we can talk to the orchestrator. This is the
    place to give the user a meaningful message if the orchestrator
    isn’t running or can’t be contacted.

    This method may be called frequently (e.g. every page load
    to conditionally display a warning banner), so make sure it’s
    not too expensive. It’s okay to give a slightly stale status
    (e.g. based on a periodic background ping of the orchestrator)
    if that’s necessary to make this method fast.

    > **Note:**
    >
    > True doesn’t mean that the desired functionality
    > is actually available in the orchestrator. I.e. this
    > won’t work as expected:
    >
    > ```
    > >>> 
    > ... if OrchestratorClientMixin().available()[0]:  # wrong.
    > ...     OrchestratorClientMixin().get_hosts()
    > ```

    Returns:
    :   boolean representing whether the module is available/usable

    Returns:
    :   string describing any error

    Return type:
    :   `Tuple`[`bool`, `str`, `Dict`[`str`, `Any`]]

    Returns:
    :   dict containing any module specific information

Orchestrator.get_feature_set()
:   Describes which methods this orchestrator implements

    > **Note:**
    >
    > True doesn’t mean that the desired functionality
    > is actually possible in the orchestrator. I.e. this
    > won’t work as expected:
    >
    > ```
    > >>> 
    > ... api = OrchestratorClientMixin()
    > ... if api.get_feature_set()['get_hosts']['available']:  # wrong.
    > ...     api.get_hosts()
    > ```
    >
    > It’s better to ask for forgiveness instead:
    >
    > ```
    > >>> 
    > ... try:
    > ...     OrchestratorClientMixin().get_hosts()
    > ... except (OrchestratorError, NotImplementedError):
    > ...     ...
    > ```

    Return type:
    :   `Dict`[`str`, `dict`]

    Returns:
    :   Dict of API method names to `{'available': True or False}`

## Client Modules

*class* orchestrator.OrchestratorClientMixin
:   A module that inherents from OrchestratorClientMixin can directly call
    all `Orchestrator` methods without manually calling remote.

    Every interface method from `Orchestrator` is converted into a stub method that internally
    calls `OrchestratorClientMixin._oremote()`

    ```
    >>> class MyModule(OrchestratorClientMixin):
    ...    def func(self):
    ...        completion = self.add_host('somehost')  # calls `_oremote()`
    ...        self.log.debug(completion.result)
    ```

    > **Note:**
    >
    > Orchestrator implementations should not inherit from OrchestratorClientMixin.
    > Reason is, that OrchestratorClientMixin magically redirects all methods to the
    > “real” implementation of the orchestrator.

    ```
    >>> import mgr_module
    >>> 
    ... class MyImplementation(mgr_module.MgrModule, Orchestrator):
    ...     def __init__(self, ...):
    ...         self.orch_client = OrchestratorClientMixin()
    ...         self.orch_client.set_mgr(self.mgr))
    ```

    add_daemon(*spec*)
    :   Create daemons daemon(s) for unmanaged services

        Return type:
        :   `OrchResult`[`List`[`str`]]

    add_host(*host_spec*)
    :   Add a host to the orchestrator inventory.

        Parameters:
        :   **host** -- hostname

        Return type:
        :   `OrchResult`[`str`]

    add_host_label(*host*, *label*)
    :   Add a host label

        Return type:
        :   `OrchResult`[`str`]

    apply(*specs*, *no_overwrite=False*, *continue_on_error=False*)
    :   Applies any spec

        Return type:
        :   `List`[`str`]

    apply_alertmanager(*spec*)
    :   Update an existing AlertManager daemon(s)

        Return type:
        :   `OrchResult`[`str`]

    apply_ceph_exporter(*spec*)
    :   Update existing a ceph exporter daemon(s)

        Return type:
        :   `OrchResult`[`str`]

    apply_crash(*spec*)
    :   Update existing a crash daemon(s)

        Return type:
        :   `OrchResult`[`str`]

    apply_drivegroups(*specs*)
    :   Update OSD cluster

        Return type:
        :   `OrchResult`[`List`[`str`]]

    apply_grafana(*spec*)
    :   Update existing a grafana service

        Return type:
        :   `OrchResult`[`str`]

    apply_ingress(*spec*)
    :   Update ingress daemons

        Return type:
        :   `OrchResult`[`str`]

    apply_iscsi(*spec*)
    :   Update iscsi cluster

        Return type:
        :   `OrchResult`[`str`]

    apply_loki(*spec*)
    :   Update existing a Loki daemon(s)

        Return type:
        :   `OrchResult`[`str`]

    apply_mds(*spec*)
    :   Update MDS cluster

        Return type:
        :   `OrchResult`[`str`]

    apply_mgr(*spec*)
    :   Update mgr cluster

        Return type:
        :   `OrchResult`[`str`]

    apply_mon(*spec*)
    :   Update mon cluster

        Return type:
        :   `OrchResult`[`str`]

    apply_nfs(*spec*)
    :   Update NFS cluster

        Return type:
        :   `OrchResult`[`str`]

    apply_node_exporter(*spec*)
    :   Update existing a Node-Exporter daemon(s)

        Return type:
        :   `OrchResult`[`str`]

    apply_nvmeof(*spec*)
    :   Update nvmeof cluster

        Return type:
        :   `OrchResult`[`str`]

    apply_prometheus(*spec*)
    :   Update prometheus cluster

        Return type:
        :   `OrchResult`[`str`]

    apply_promtail(*spec*)
    :   Update existing a Promtail daemon(s)

        Return type:
        :   `OrchResult`[`str`]

    apply_rbd_mirror(*spec*)
    :   Update rbd-mirror cluster

        Return type:
        :   `OrchResult`[`str`]

    apply_rgw(*spec*)
    :   Update RGW cluster

        Return type:
        :   `OrchResult`[`str`]

    apply_smb(*spec*)
    :   Update a smb gateway service

        Return type:
        :   `OrchResult`[`str`]

    apply_snmp_gateway(*spec*)
    :   Update an existing snmp gateway service

        Return type:
        :   `OrchResult`[`str`]

    apply_tuned_profiles(*specs*, *no_overwrite*)
    :   Add or update an existing tuned profile

        Return type:
        :   `OrchResult`[`str`]

    available()
    :   Report whether we can talk to the orchestrator. This is the
        place to give the user a meaningful message if the orchestrator
        isn’t running or can’t be contacted.

        This method may be called frequently (e.g. every page load
        to conditionally display a warning banner), so make sure it’s
        not too expensive. It’s okay to give a slightly stale status
        (e.g. based on a periodic background ping of the orchestrator)
        if that’s necessary to make this method fast.

        > **Note:**
        >
        > True doesn’t mean that the desired functionality
        > is actually available in the orchestrator. I.e. this
        > won’t work as expected:
        >
        > ```
        > >>> 
        > ... if OrchestratorClientMixin().available()[0]:  # wrong.
        > ...     OrchestratorClientMixin().get_hosts()
        > ```

        Returns:
        :   boolean representing whether the module is available/usable

        Returns:
        :   string describing any error

        Return type:
        :   `Tuple`[`bool`, `str`, `Dict`[`str`, `Any`]]

        Returns:
        :   dict containing any module specific information

    blink_device_light(*ident_fault*, *on*, *locations*)
    :   Instructs the orchestrator to enable or disable either the ident or the fault LED.

        Parameters:
        :   - **ident_fault** (`str`) -- either `"ident"` or `"fault"`
            - **on** (`bool`) -- `True` = on.
            - **locations** (`List`[[`DeviceLightLoc`](index.md#orchestrator.DeviceLightLoc "orchestrator._interface.DeviceLightLoc")]) -- See [`orchestrator.DeviceLightLoc`](index.md#orchestrator.DeviceLightLoc "orchestrator.DeviceLightLoc")

        Return type:
        :   `OrchResult`[`List`[`str`]]

    cancel_completions()
    :   Cancels ongoing completions. Unstuck the mgr.

        Return type:
        :   `None`

    create_osds(*drive_group*)
    :   Create one or more OSDs within a single Drive Group.

        The principal argument here is the drive_group member
        of OsdSpec: other fields are advisory/extensible for any
        finer-grained OSD feature enablement (choice of backing store,
        compression/encryption, etc).

        Return type:
        :   `OrchResult`[`str`]

    daemon_action(*action*, *daemon_name*, *image=None*)
    :   Perform an action (start/stop/reload) on a daemon.

        Parameters:
        :   - **action** (`str`) -- one of “start”, “stop”, “restart”, “redeploy”, “reconfig”
            - **daemon_name** (`str`) -- name of daemon
            - **image** (`Optional`[`str`]) -- Container image when redeploying that daemon

        Return type:
        :   OrchResult

    describe_service(*service_type=None*, *service_name=None*, *refresh=False*)
    :   Describe a service (of any kind) that is already configured in
        the orchestrator. For example, when viewing an OSD in the dashboard
        we might like to also display information about the orchestrator’s
        view of the service (like the kubernetes pod ID).

        When viewing a CephFS filesystem in the dashboard, we would use this
        to display the pods being currently run for MDS daemons.

        Return type:
        :   `OrchResult`[`List`[[`ServiceDescription`](index.md#orchestrator.ServiceDescription "orchestrator._interface.ServiceDescription")]]

        Returns:
        :   list of ServiceDescription objects.

    drain_host(*hostname*, *force=False*, *keep_conf_keyring=False*, *zap_osd_devices=False*)
    :   drain all daemons from a host

        Parameters:
        :   **hostname** (`str`) -- hostname

        Return type:
        :   `OrchResult`[`str`]

    enter_host_maintenance(*hostname*, *force=False*, *yes_i_really_mean_it=False*)
    :   Place a host in maintenance, stopping daemons and disabling it’s systemd target

        Return type:
        :   `OrchResult`

    exit_host_maintenance(*hostname*)
    :   Return a host from maintenance, restarting the clusters systemd target

        Return type:
        :   `OrchResult`

    get_alertmanager_access_info()
    :   get alertmanager access information

        Return type:
        :   `OrchResult`[`Dict`[`str`, `str`]]

    get_facts(*hostname=None*)
    :   Return hosts metadata(gather_facts).

        Return type:
        :   `OrchResult`[`List`[`Dict`[`str`, `Any`]]]

    get_feature_set()
    :   Describes which methods this orchestrator implements

        > **Note:**
        >
        > True doesn’t mean that the desired functionality
        > is actually possible in the orchestrator. I.e. this
        > won’t work as expected:
        >
        > ```
        > >>> 
        > ... api = OrchestratorClientMixin()
        > ... if api.get_feature_set()['get_hosts']['available']:  # wrong.
        > ...     api.get_hosts()
        > ```
        >
        > It’s better to ask for forgiveness instead:
        >
        > ```
        > >>> 
        > ... try:
        > ...     OrchestratorClientMixin().get_hosts()
        > ... except (OrchestratorError, NotImplementedError):
        > ...     ...
        > ```

        Return type:
        :   `Dict`[`str`, `dict`]

        Returns:
        :   Dict of API method names to `{'available': True or False}`

    get_hosts()
    :   Report the hosts in the cluster.

        Return type:
        :   `OrchResult`[`List`[[`HostSpec`](index.md#orchestrator.HostSpec "ceph.deployment.hostspec.HostSpec")]]

        Returns:
        :   list of HostSpec

    get_inventory(*host_filter=None*, *refresh=False*)
    :   Returns something that was created by ceph-volume inventory.

        Return type:
        :   `OrchResult`[`List`[`InventoryHost`]]

        Returns:
        :   list of InventoryHost

    get_prometheus_access_info()
    :   get prometheus access information

        Return type:
        :   `OrchResult`[`Dict`[`str`, `str`]]

    hardware_light(*light_type*, *action*, *hostname*, *device=None*)
    :   Light a chassis or device ident LED.

        Parameters:
        :   - **light_type** (`str`) -- led type (chassis or device).
            - **action** (`str`) -- set or get status led.
            - **hostname** (`str`) -- the name of the host.
            - **device** (`Optional`[`str`]) -- the device id (when light_type = ‘device’)

        Return type:
        :   `OrchResult`[`Dict`[`str`, `Any`]]

    hardware_powercycle(*hostname*, *yes_i_really_mean_it=False*)
    :   Reboot a host.

        Parameters:
        :   **hostname** (`str`) -- the name of the host being rebooted.

        Return type:
        :   `OrchResult`[`str`]

    hardware_shutdown(*hostname*, *force=False*, *yes_i_really_mean_it=False*)
    :   Shutdown a host.

        Parameters:
        :   **hostname** (`str`) -- the name of the host to shutdown.

        Return type:
        :   `OrchResult`[`str`]

    hardware_status(*hostname=None*, *category='summary'*)
    :   Display hardware status.

        Parameters:
        :   - **category** (`Optional`[`str`]) -- category
            - **hostname** (`Optional`[`str`]) -- hostname

        Return type:
        :   `OrchResult`[`str`]

    host_ok_to_stop(*hostname*)
    :   Check if the specified host can be safely stopped without reducing availability

        Parameters:
        :   **host** -- hostname

        Return type:
        :   `OrchResult`

    list_daemons(*service_name=None*, *daemon_type=None*, *daemon_id=None*, *host=None*, *refresh=False*)
    :   Describe a daemon (of any kind) that is already configured in
        the orchestrator.

        Return type:
        :   `OrchResult`[`List`[[`DaemonDescription`](index.md#orchestrator.DaemonDescription "orchestrator._interface.DaemonDescription")]]

        Returns:
        :   list of DaemonDescription objects.

    node_proxy_common(*category*, *hostname=None*)
    :   Return node-proxy generic report

        Parameters:
        :   **hostname** (`Optional`[`str`]) -- hostname

        Return type:
        :   `OrchResult`[`Dict`[`str`, `Any`]]

    node_proxy_criticals(*hostname=None*)
    :   Return node-proxy criticals report

        Parameters:
        :   **hostname** (`Optional`[`str`]) -- hostname

        Return type:
        :   `OrchResult`[`Dict`[`str`, `Any`]]

    node_proxy_firmwares(*hostname=None*)
    :   Return node-proxy firmwares report

        Parameters:
        :   **hostname** (`Optional`[`str`]) -- hostname

        Return type:
        :   `OrchResult`[`Dict`[`str`, `Any`]]

    node_proxy_fullreport(*hostname=None*)
    :   Return node-proxy full report

        Parameters:
        :   **hostname** (`Optional`[`str`]) -- hostname

        Return type:
        :   `OrchResult`[`Dict`[`str`, `Any`]]

    node_proxy_summary(*hostname=None*)
    :   Return node-proxy summary

        Parameters:
        :   **hostname** (`Optional`[`str`]) -- hostname

        Return type:
        :   `OrchResult`[`Dict`[`str`, `Any`]]

    plan(*spec*)
    :   Plan (Dry-run, Preview) a List of Specs.

        Return type:
        :   `OrchResult`[`List`]

    preview_osdspecs(*osdspec_name='osd'*, *osdspecs=None*)
    :   Get a preview for OSD deployments

        Return type:
        :   `OrchResult`[`str`]

    remove_daemons(*names*)
    :   Remove specific daemon(s).

        Return type:
        :   `OrchResult`[`List`[`str`]]

        Returns:
        :   None

    remove_host(*host*, *force*, *offline*, *rm_crush_entry*)
    :   Remove a host from the orchestrator inventory.

        Parameters:
        :   **host** (`str`) -- hostname

        Return type:
        :   `OrchResult`[`str`]

    remove_host_label(*host*, *label*, *force=False*)
    :   Remove a host label

        Return type:
        :   `OrchResult`[`str`]

    remove_osds(*osd_ids*, *replace=False*, *replace_block=False*, *replace_db=False*, *replace_wal=False*, *force=False*, *zap=False*, *no_destroy=False*)
    :   Parameters:
        :   - **osd_ids** (`List`[`str`]) -- list of OSD IDs
            - **replace** (`bool`) -- marks the OSD as being destroyed. See [OSD Replacement](index.md#orchestrator-osd-replace)
            - **replace_block** (`bool`) -- marks the corresponding block device as being replaced.
            - **replace_db** (`bool`) -- marks the corresponding db device as being replaced.
            - **replace_wal** (`bool`) -- marks the corresponding wal device as being replaced.
            - **force** (`bool`) -- Forces the OSD removal process without waiting for the data to be drained first.
            - **zap** (`bool`) -- Zap/Erase all devices associated with the OSDs (DESTROYS DATA)
            - **no_destroy** (`bool`) -- Do not destroy associated VGs/LVs with the OSD.

        > **Note:**
        >
        > this can only remove OSDs that were successfully
        > created (i.e. got an OSD ID).

        Return type:
        :   `OrchResult`[`str`]

    remove_osds_status()
    :   Returns a status of the ongoing OSD removal operations.

        Return type:
        :   `OrchResult`

    remove_prometheus_target(*url*)
    :   remove prometheus target for multi-cluster

        Return type:
        :   `OrchResult`[`str`]

    remove_service(*service_name*, *force=False*)
    :   Remove a service (a collection of daemons).

        Return type:
        :   `OrchResult`[`str`]

        Returns:
        :   None

    replace_device(*hostname*, *device*, *clear=False*, *yes_i_really_mean_it=False*)
    :   Perform all required operations in order to replace a device.

        Return type:
        :   `OrchResult`

    rescan_host(*hostname*)
    :   Use cephadm to issue a disk rescan on each HBA

        Some HBAs and external enclosures don’t automatically register
        device insertion with the kernel, so for these scenarios we need
        to manually rescan

        Parameters:
        :   **hostname** (`str`) -- (str) host name

        Return type:
        :   `OrchResult`

    rm_tuned_profile(*profile_name*)
    :   Remove a tuned profile

        Return type:
        :   `OrchResult`[`str`]

    service_action(*action*, *service_name*)
    :   Perform an action (start/stop/reload) on a service (i.e., all daemons
        providing the logical service).

        Parameters:
        :   - **action** (`str`) -- one of “start”, “stop”, “restart”, “redeploy”, “reconfig”
            - **service_name** (`str`) -- service_type + ‘.’ + service_id
              (e.g. “mon”, “mgr”, “mds.mycephfs”, “rgw.realm.zone”, …)

        Return type:
        :   OrchResult

    service_discovery_dump_cert()
    :   Returns service discovery server root certificate

        Return type:
        :   `OrchResult`

        Returns:
        :   service discovery root certificate

    set_alertmanager_access_info(*user*, *password*)
    :   set alertmanager access information

        Return type:
        :   `OrchResult`[`str`]

    set_custom_prometheus_alerts(*alerts_file*)
    :   set prometheus custom alerts files and schedule reconfig of prometheus

        Return type:
        :   `OrchResult`[`str`]

    set_mgr(*mgr*)
    :   Useable in the Dashboard that uses a global `mgr`

        Return type:
        :   `None`

    set_prometheus_access_info(*user*, *password*)
    :   set prometheus access information

        Return type:
        :   `OrchResult`[`str`]

    set_prometheus_target(*url*)
    :   set prometheus target for multi-cluster

        Return type:
        :   `OrchResult`[`str`]

    set_unmanaged(*service_name*, *value*)
    :   Set unmanaged parameter to True/False for a given service

        Return type:
        :   `OrchResult`[`str`]

        Returns:
        :   None

    stop_remove_osds(*osd_ids*)
    :   TODO

        Return type:
        :   `OrchResult`

    tuned_profile_add_setting(*profile_name*, *setting*, *value*)
    :   Change/Add a specific setting for a tuned profile

        Return type:
        :   `OrchResult`[`str`]

    tuned_profile_ls()
    :   See current tuned profiles

        Return type:
        :   `OrchResult`[`List`[`TunedProfileSpec`]]

    tuned_profile_rm_setting(*profile_name*, *setting*)
    :   Remove a specific setting for a tuned profile

        Return type:
        :   `OrchResult`[`str`]

    update_host_addr(*host*, *addr*)
    :   Update a host’s address

        Parameters:
        :   - **host** (`str`) -- hostname
            - **addr** (`str`) -- address (dns name or IP)

        Return type:
        :   `OrchResult`[`str`]

    upgrade_available()
    :   Report on what versions are available to upgrade to

        Return type:
        :   `OrchResult`

        Returns:
        :   List of strings

    upgrade_status()
    :   If an upgrade is currently underway, report on where
        we are in the process, or if some error has occurred.

        Return type:
        :   `OrchResult`[[`UpgradeStatusSpec`](index.md#orchestrator.UpgradeStatusSpec "orchestrator._interface.UpgradeStatusSpec")]

        Returns:
        :   UpgradeStatusSpec instance

    zap_device(*host*, *path*)
    :   Zap/Erase a device (DESTROYS DATA)

        Return type:
        :   `OrchResult`[`str`]

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
