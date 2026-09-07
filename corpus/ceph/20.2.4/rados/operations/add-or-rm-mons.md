---
collection: ceph
version: "20.2.4"
title: "Adding/Removing Monitors"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/rados/operations/add-or-rm-mons.rst
fetched_at: 2026-08-18T01:32:45Z
---
<a id="adding-and-removing-monitors"></a>

# Adding/Removing Monitors

It is possible to add monitors to a running cluster as long as redundancy is
maintained. To bootstrap a monitor, see [Manual Deployment](../../install/manual-deployment.md) or [Monitor Bootstrap](../../dev/mon-bootstrap.md).

<a id="adding-monitors"></a>

## Adding Monitors

Ceph monitors serve as the single source of truth for the cluster map. It is
possible to run a cluster with only one monitor, but for a production cluster
it is recommended to have at least three monitors provisioned and in quorum.
Ceph monitors use a variation of the [Paxos](https://en.wikipedia.org/wiki/[Paxos](https://en.wikipedia.org/wiki/Paxos_(computer_science))(computer_science)) algorithm to maintain consensus
about maps and about other critical information across the cluster. Due to the
nature of Paxos, Ceph is able to maintain quorum (and thus establish
consensus) only if a majority of the monitors are ``active``.

It is best to run an odd number of monitors. This is because a cluster that is
running an odd number of monitors is more resilient than a cluster running an
even number. For example, in a two-monitor deployment, no failures can be
tolerated if quorum is to be maintained; in a three-monitor deployment, one
failure can be tolerated; in a four-monitor deployment, one failure can be
tolerated; and in a five-monitor deployment, two failures can be tolerated. In
general, a cluster running an odd number of monitors is best because it avoids
what is called the *split brain* phenomenon. In short, Ceph is able to operate
only if a majority of monitors are ``active`` and able to communicate with each
other, (for example: there must be a single monitor, two out of two monitors,
two out of three monitors, three out of five monitors, or the like).

For small or non-critical deployments of multi-node Ceph clusters, it is
recommended to deploy three monitors. For larger clusters or for clusters that
are intended to survive a double failure, it is recommended to deploy five
monitors. Only in rare circumstances is there any justification for deploying
seven or more monitors.

It is possible to run a monitor on the same host that is running an OSD.
However, this approach has disadvantages: for example: `fsync` issues with the
kernel might weaken performance, monitor and OSD daemons might be inactive at
the same time and cause disruption if the node crashes, is rebooted, or is
taken down for maintenance. Because of these risks, it is instead
recommended to run monitors and managers on dedicated hosts.

> **Note:** A *majority* of monitors in your cluster must be able to
> reach each other in order for quorum to be established.

### Deploying your Hardware

Some operators choose to add a new monitor host at the same time that they add
a new monitor. For details on the minimum recommendations for monitor hardware,
see [Hardware Recommendations](../../start/hardware-recommendations.md). Before adding a monitor host to the cluster,
make sure that there is an up-to-date version of Linux installed.

Add the newly installed monitor host to a rack in your cluster, connect the
host to the network, and make sure that the host has network connectivity.

### Installing the Required Software

In manually deployed clusters, it is necessary to install Ceph packages
manually. For details, see [Installing Packages](../../install/install-storage-cluster.md). Configure SSH so that it can
be used by a user that has passwordless authentication and root permissions.

<a id="adding-a-monitor-manual"></a>

### Adding a Monitor (Manual)

The procedure in this section creates a ``ceph-mon`` data directory, retrieves
both the monitor map and the monitor keyring, and adds a ``ceph-mon`` daemon to
the cluster. The procedure might result in a Ceph cluster that contains only
two monitor daemons. To add more monitors until there are enough ``ceph-mon``
daemons to establish quorum, repeat the procedure.

This is a good point at which to define the new monitor's ``id``. Monitors have
often been named with single letters (``a``, ``b``, ``c``, etc.), but you are
free to define the ``id`` however you see fit. In this document, ``{mon-id}``
refers to the ``id`` exclusive of the ``mon.`` prefix: for example, if
``mon.a`` has been chosen as the ``id`` of a monitor, then ``{mon-id}`` is
``a``.                                               ???

1. Create a data directory on the machine that will host the new monitor:

```bash
ssh {new-mon-host}
sudo mkdir /var/lib/ceph/mon/ceph-{mon-id}
```

1. Create a temporary directory ``{tmp}`` that will contain the files needed
   during this procedure. This directory should be different from the data
   directory created in the previous step. Because this is a temporary
   directory, it can be removed after the procedure is complete:

```bash
mkdir {tmp}
```

1. Retrieve the keyring for your monitors (``{tmp}`` is the path to the
   retrieved keyring and ``{key-filename}`` is the name of the file that
   contains the retrieved monitor key):

```bash
ceph auth get mon. -o {tmp}/{key-filename}
```

1. Retrieve the monitor map (``{tmp}`` is the path to the retrieved monitor map
   and ``{map-filename}`` is the name of the file that contains the retrieved
   monitor map):

```bash
ceph mon getmap -o {tmp}/{map-filename}
```

1. Prepare the monitor's data directory, which was created in the first step.
   The following command must specify the path to the monitor map (so that
   information about a quorum of monitors and their ``fsid``\s can be
   retrieved) and specify the path to the monitor keyring:

```bash
sudo ceph-mon -i {mon-id} --mkfs --monmap {tmp}/{map-filename} --keyring {tmp}/{key-filename}
```

1. Start the new monitor. It will automatically join the cluster. To provide
   information to the daemon about which address to bind to, use either the
   ``--public-addr {ip}`` option or the ``--public-network {network}`` option.
   For example:

```bash
ceph-mon -i {mon-id} --public-addr {ip:port}
```

<a id="removing-monitors"></a>

## Removing Monitors

When monitors are removed from a cluster, it is important to remember
that Ceph monitors use Paxos to maintain consensus about the cluster
map. Such consensus is possible only if the number of monitors is sufficient
to establish quorum.

<a id="removing-a-monitor-manual"></a>

### Removing a Monitor (Manual)

The procedure in this section removes a ``ceph-mon`` daemon from the cluster.
The procedure might result in a Ceph cluster that contains a number of monitors
insufficient to maintain quorum, so plan carefully. When replacing an old
monitor with a new monitor, add the new monitor first, wait for quorum to be
established, and then remove the old monitor. This ensures that quorum is not
lost.

1. Stop the monitor:

```bash
service ceph -a stop mon.{mon-id}
```

1. Remove the monitor from the cluster:

```bash
ceph mon remove {mon-id}
```

1. Remove the monitor entry from the ``ceph.conf`` file:

<a id="rados-mon-remove-from-unhealthy"></a>

### Removing Monitors from an Unhealthy Cluster

The procedure in this section removes a ``ceph-mon`` daemon from an unhealthy
cluster (for example, a cluster whose monitors are unable to form a quorum).

1. Stop all ``ceph-mon`` daemons on all monitor hosts:

```bash
ssh {mon-host}
systemctl stop ceph-mon.target
```

   Repeat this step on every monitor host.

1. Identify a surviving monitor and log in to the monitor's host:

```bash
ssh {mon-host}
```

1. Extract a copy of the ``monmap`` file by running a command of the following
   form:

```bash
ceph-mon -i {mon-id} --extract-monmap {map-path}
```

   Here is a more concrete example. In this example, ``hostname`` is the
   ``{mon-id}`` and ``/tmp/monpap`` is the ``{map-path}``:

```bash
ceph-mon -i `hostname` --extract-monmap /tmp/monmap
```

1. Remove the non-surviving or otherwise problematic monitors:

```bash
monmaptool {map-path} --rm {mon-id}
```

   For example, suppose that there are three monitors |---| ``mon.a``, ``mon.b``,
   and ``mon.c`` |---| and that only ``mon.a`` will survive:

```bash
monmaptool /tmp/monmap --rm b
monmaptool /tmp/monmap --rm c
```

1. Inject the surviving map that includes the removed monitors into the
   monmap of the surviving monitor(s):

```bash
ceph-mon -i {mon-id} --inject-monmap {map-path}
```

   Continuing with the above example, inject a map into monitor ``mon.a`` by
   running the following command:

```bash
ceph-mon -i a --inject-monmap /tmp/monmap
```

1. Start only the surviving monitors.

1. Verify that the monitors form a quorum by running the command ``ceph -s``.

1. The data directory of the removed monitors is in ``/var/lib/ceph/mon``:
   either archive this data directory in a safe location or delete this data
   directory. However, do not delete it unless you are confident that the
   remaining monitors are healthy and sufficiently redundant. Make sure that
   there is enough room for the live DB to expand and compact, and make sure
   that there is also room for an archived copy of the DB. The archived copy
   can be compressed.

<a id="changing-a-monitors-ip-address"></a>

## Changing a Monitor's IP Address

> **Important:** Existing monitors are not supposed to change their IP addresses.

Monitors are critical components of a Ceph cluster. The entire system can work
properly only if the monitors maintain quorum, and quorum can be established
only if the monitors have discovered each other by means of their IP addresses.
Ceph has strict requirements on the discovery of monitors.

Although the ``ceph.conf`` file is used by Ceph clients and other Ceph daemons
to discover monitors, the monitor map is used by monitors to discover each
other. This is why it is necessary to obtain the current ``monmap`` at the time
a new monitor is created: as can be seen above in [Adding a Monitor (Manual)](add-or-rm-mons.md#adding-a-monitor-manual),
the ``monmap`` is one of the arguments required by the ``ceph-mon -i {mon-id}
--mkfs`` command. The following sections explain the consistency requirements
for Ceph monitors, and also explain a number of safe ways to change a monitor's
IP address.

### Consistency Requirements

When a monitor discovers other monitors in the cluster, it always refers to the
local copy of the monitor map. Using the monitor map instead of using the
``ceph.conf`` file avoids errors that could break the cluster (for example,
typos or other slight errors in ``ceph.conf`` when a monitor address or port is
specified). Because monitors use monitor maps for discovery and because they
share monitor maps with Ceph clients and other Ceph daemons, the monitor map
provides monitors with a strict guarantee that their consensus is valid.

Strict consistency also applies to updates to the monmap. As with any other
updates on the monitor, changes to the monmap always run through a distributed
consensus algorithm called [Paxos](https://en.wikipedia.org/wiki/[Paxos](https://en.wikipedia.org/wiki/Paxos_(computer_science))(computer_science)). The monitors must agree on each update to
the monmap, such as adding or removing a monitor, to ensure that each monitor
in the quorum has the same version of the monmap. Updates to the monmap are
incremental so that monitors have the latest agreed upon version, and a set of
previous versions, allowing a monitor that has an older version of the monmap
to catch up with the current state of the cluster.

There are additional advantages to using the monitor map rather than
``ceph.conf`` when monitors discover each other. Because ``ceph.conf`` is not
automatically updated and distributed, its use would bring certain risks:
monitors might use an outdated ``ceph.conf`` file, might fail to recognize a
specific monitor, might fall out of quorum, and might develop a situation in
which [Paxos](https://en.wikipedia.org/wiki/[Paxos](https://en.wikipedia.org/wiki/Paxos_(computer_science))(computer_science)) is unable to accurately ascertain the current state of the
system. Because of these risks, any changes to an existing monitor's IP address
must be made with great care.

<a id="operations_add_or_rm_mons_changing_mon_ip"></a>

### Changing a Monitor's IP address (Preferred Method)

If a monitor's IP address is changed only in the ``ceph.conf`` file, there is
no guarantee that the other monitors in the cluster will receive the update.
For this reason, the preferred method to change a monitor's IP address is as
follows: add a new monitor with the desired IP address (as described in [Adding a Monitor (Manual)](add-or-rm-mons.md#adding-a-monitor-manual)), make sure that the new monitor successfully joins the
quorum, remove the monitor that is using the old IP address, and update the
``ceph.conf`` file to ensure that clients and other daemons are made aware of
the new monitor's IP address.

For example, suppose that there are three monitors in place:

```
[mon.a]
    host = host01
    addr = 10.0.0.1:6789
[mon.b]
    host = host02
    addr = 10.0.0.2:6789
[mon.c]
    host = host03
    addr = 10.0.0.3:6789
```

To change ``mon.c`` so that its name is ``host04`` and its IP address is
``10.0.0.4``: (1) follow the steps in [Adding a Monitor (Manual)](add-or-rm-mons.md#adding-a-monitor-manual) to add a new
monitor ``mon.d``, (2) make sure that ``mon.d`` is  running before removing
``mon.c`` or else quorum will be broken, and (3) follow the steps in [Removing a Monitor (Manual)](add-or-rm-mons.md#removing-a-monitor-manual) to remove ``mon.c``. To move all three monitors to new IP
addresses, repeat this process.

### Changing a Monitor's IP address (Advanced Method)

There are cases in which the method outlined in
[operations_add_or_rm_mons_changing_mon_ip](add-or-rm-mons.md#operations_add_or_rm_mons_changing_mon_ip) cannot be used. For example,
it might be necessary to move the cluster's monitors to a different network, to
a different part of the datacenter, or to a different datacenter altogether. It
is still possible to change the monitors' IP addresses, but a different method
must be used.

For such cases, a new monitor map with updated IP addresses for every monitor
in the cluster must be generated and injected on each monitor. Although this
method is not particularly easy, such a major migration is unlikely to be a
routine task. As stated at the beginning of this section, existing monitors are
not supposed to change their IP addresses.

Continue with the monitor configuration in the example from
[operations_add_or_rm_mons_changing_mon_ip](add-or-rm-mons.md#operations_add_or_rm_mons_changing_mon_ip). Suppose that all of the
monitors are to be moved from the ``10.0.0.x`` range to the ``10.1.0.x`` range,
and that these networks are unable to communicate. Carry out the following
procedure:

1. Retrieve the monitor map (``{tmp}`` is the path to the retrieved monitor
   map, and ``{filename}`` is the name of the file that contains the retrieved
   monitor map):

```bash
ceph mon getmap -o {tmp}/{filename}
```

1. Check the contents of the monitor map:

```bash
monmaptool --print {tmp}/{filename}
```

   :

```
monmaptool: monmap file {tmp}/{filename}
epoch 1
fsid 224e376d-c5fe-4504-96bb-ea6332a19e61
last_changed 2012-12-17 02:46:41.591248
created 2012-12-17 02:46:41.591248
0: 10.0.0.1:6789/0 mon.a
1: 10.0.0.2:6789/0 mon.b
2: 10.0.0.3:6789/0 mon.c
```

1. Remove the existing monitors from the monitor map:

```bash
monmaptool --rm a --rm b --rm c {tmp}/{filename}
```

   :

```
monmaptool: monmap file {tmp}/{filename}
monmaptool: removing a
monmaptool: removing b
monmaptool: removing c
monmaptool: writing epoch 1 to {tmp}/{filename} (0 monitors)
```

1. Add the new monitor locations to the monitor map:

```bash
monmaptool --add a 10.1.0.1:6789 --add b 10.1.0.2:6789 --add c 10.1.0.3:6789 {tmp}/{filename}
```

   :

```
monmaptool: monmap file {tmp}/{filename}
monmaptool: writing epoch 1 to {tmp}/{filename} (3 monitors)
```

1. Check the new contents of the monitor map:

```bash
monmaptool --print {tmp}/{filename}
```

   :

```
monmaptool: monmap file {tmp}/{filename}
epoch 1
fsid 224e376d-c5fe-4504-96bb-ea6332a19e61
last_changed 2012-12-17 02:46:41.591248
created 2012-12-17 02:46:41.591248
0: 10.1.0.1:6789/0 mon.a
1: 10.1.0.2:6789/0 mon.b
2: 10.1.0.3:6789/0 mon.c
```

At this point, we assume that the monitors (and stores) have been installed at
the new location. Next, propagate the modified monitor map to the new monitors,
and inject the modified monitor map into each new monitor.

1. Make sure all of your monitors have been stopped. Never inject into a
   monitor while the monitor daemon is running.

1. Inject the monitor map:

```bash
ceph-mon -i {mon-id} --inject-monmap {tmp}/{filename}
```

1. Restart all of the monitors.

Migration to the new location is now complete. The monitors should operate
successfully.

## Using cephadm to change the public network

### Overview

The procedure in this overview section provides only the broad outlines of
using ``cephadm`` to change the public network.

1. Create backups of all keyrings, configuration files, and the current monmap.

1. Stop the cluster and disable ``ceph.target`` to prevent the daemons from
   starting.

1. Move the servers and power them on.

1. Change the network setup as desired.

### Example Procedure

> **Note:** In this procedure, the "old network" has addresses of the form
> ``10.10.10.0/24`` and the "new network" has addresses of the form
> ``192.168.160.0/24``.

1. Enter the shell of the first monitor:

```bash
cephadm shell --name mon.reef1
```

1. Extract the current monmap from ``mon.reef1``:

```bash
ceph-mon -i reef1 --extract-monmap monmap
```

1. Print the content of the monmap:

```bash
monmaptool --print monmap
```

   :

```
monmaptool: monmap file monmap
epoch 5
fsid 2851404a-d09a-11ee-9aaa-fa163e2de51a
last_changed 2024-02-21T09:32:18.292040+0000
created 2024-02-21T09:18:27.136371+0000
min_mon_release 18 (reef)
election_strategy: 1
0: [v2:10.10.10.11:3300/0,v1:10.10.10.11:6789/0] mon.reef1
1: [v2:10.10.10.12:3300/0,v1:10.10.10.12:6789/0] mon.reef2
2: [v2:10.10.10.13:3300/0,v1:10.10.10.13:6789/0] mon.reef3
```

1. Remove monitors with old addresses:

```bash
monmaptool --rm reef1 --rm reef2 --rm reef3 monmap
```

1. Add monitors with new addresses:

```bash
monmaptool --addv reef1 [v2:192.168.160.11:3300/0,v1:192.168.160.11:6789/0] --addv reef2 [v2:192.168.160.12:3300/0,v1:192.168.160.12:6789/0] --addv reef3 [v2:192.168.160.13:3300/0,v1:192.168.160.13:6789/0] monmap
```

1. Verify that the changes to the monmap have been made successfully:

```bash
monmaptool --print monmap
```

   :

```
monmaptool: monmap file monmap
epoch 4
fsid 2851404a-d09a-11ee-9aaa-fa163e2de51a
last_changed 2024-02-21T09:32:18.292040+0000
created 2024-02-21T09:18:27.136371+0000
min_mon_release 18 (reef)
election_strategy: 1
0: [v2:192.168.160.11:3300/0,v1:192.168.160.11:6789/0] mon.reef1
1: [v2:192.168.160.12:3300/0,v1:192.168.160.12:6789/0] mon.reef2
2: [v2:192.168.160.13:3300/0,v1:192.168.160.13:6789/0] mon.reef3
```

1. Inject the new monmap into the Ceph cluster:

```bash
ceph-mon -i reef1 --inject-monmap monmap
```

1. Repeat the steps above for all other monitors in the cluster.

1. Update ``/var/lib/ceph/{FSID}/mon.{MON}/config``.

1. Start the monitors.

1. Update the ceph ``public_network``:

```bash
ceph config set mon public_network 192.168.160.0/24
```

1. Update the configuration files of the managers
   (``/var/lib/ceph/{FSID}/mgr.{mgr}/config``) and start them. Orchestrator
   will now be available, but it will attempt to connect to the old network
   because the host list contains the old addresses.

1. Update the host addresses by running commands of the following form:

```bash
ceph orch host set-addr reef1 192.168.160.11
ceph orch host set-addr reef2 192.168.160.12
ceph orch host set-addr reef3 192.168.160.13
```

1. Wait a few minutes for the orchestrator to connect to each host.

1. Reconfigure the OSDs so that their config files are automatically updated:

```bash
ceph orch reconfig osd
```

*The above procedure was developed by Eugen Block and was successfully tested
in February 2024 on Ceph version 18.2.1 (Reef).*

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
