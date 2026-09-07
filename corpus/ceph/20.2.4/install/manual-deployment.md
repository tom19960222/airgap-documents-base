---
collection: ceph
version: "20.2.4"
title: "Manual Deployment"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/install/manual-deployment.rst
fetched_at: 2026-08-18T01:32:45Z
---
<a id="manual-deployment"></a>

# Manual Deployment

All Ceph clusters require at least one monitor, and at least as many OSDs as
copies of an object stored on the cluster.  Bootstrapping the initial monitor(s)
is the first step in deploying a Ceph Storage Cluster. Monitor deployment also
sets important criteria for the entire cluster, such as the number of replicas
for pools, the number of placement groups per OSD, the heartbeat intervals,
whether authentication is required, etc. Most of these values are set by
default, so it's useful to know about them when setting up your cluster for
production.

We will set up a cluster with ``mon-node1`` as  the monitor node, and ``osd-node1`` and
``osd-node2`` for OSD nodes.

.. ditaa::

   /------------------\         /----------------\
   |    Admin Node    |         |    mon-node1   |
   |                  +-------->+                |
   |                  |         | cCCC           |
   \---------+--------/         \----------------/
             |
             |                  /----------------\
             |                  |    osd-node1   |
             +----------------->+                |
             |                  | cCCC           |
             |                  \----------------/
             |
             |                  /----------------\
             |                  |    osd-node2   |
             +----------------->|                |
                                | cCCC           |
                                \----------------/

# Monitor Bootstrapping

Bootstrapping a monitor (a Ceph Storage Cluster, in theory) requires
a number of things:

- **Unique Identifier:** The ``fsid`` is a unique identifier for the cluster,
  and stands for File System ID from the days when the Ceph Storage Cluster was
  principally for the Ceph File System. Ceph now supports native interfaces,
  block devices, and object storage gateway interfaces too, so ``fsid`` is a
  bit of a misnomer.

- **Cluster Name:** Ceph clusters have a cluster name, which is a simple string
  without spaces. The default cluster name is ``ceph``, but you may specify
  a different cluster name. Overriding the default cluster name is
  especially useful when you are working with multiple clusters and you need to
  clearly understand which cluster your are working with.

  For example, when you run multiple clusters in a [multisite configuration](../radosgw/bucket_logging.md#multisite),
  the cluster name (e.g., ``us-west``, ``us-east``) identifies the cluster for
  the current CLI session. **Note:** To identify the cluster name on the
  command line interface, specify the Ceph configuration file with the
  cluster name (e.g., ``ceph.conf``, ``us-west.conf``, ``us-east.conf``, etc.).
  Also see CLI usage (``ceph --cluster {cluster-name}``).

- **Monitor Name:** Each monitor instance within a cluster has a unique name.
  In common practice, the Ceph Monitor name is the host name (we recommend one
  Ceph Monitor per host, and no commingling of Ceph OSD Daemons with
  Ceph Monitors). You may retrieve the short hostname with ``hostname -s``.

- **Monitor Map:** Bootstrapping the initial monitor(s) requires you to
  generate a monitor map. The monitor map requires the ``fsid``, the cluster
  name (or uses the default), and at least one host name and its IP address.

- **Monitor Keyring**: Monitors communicate with each other via a
  secret key. You must generate a keyring with a monitor secret and provide
  it when bootstrapping the initial monitor(s).

* **Configure Cephx**: The monmap will use the most secure defaults but
  you may want to relax the choice in ciphers to support legacy clients.

- **Administrator Keyring**: To use the ``ceph`` CLI tools, you must have
  a ``client.admin`` user. So you must generate the admin user and keyring,
  and you must also add the ``client.admin`` user to the monitor keyring.

The foregoing requirements do not imply the creation of a Ceph Configuration
file. However, as a best practice, we recommend creating a Ceph configuration
file and populating it with the ``fsid``, the ``mon initial members`` and the
``mon host`` settings.

You can get and set all of the monitor settings at runtime as well. However,
a Ceph Configuration file may contain only those settings that override the
default values. When you add settings to a Ceph configuration file, these
settings override the default settings. Maintaining those settings in a
Ceph configuration file makes it easier to maintain your cluster.

The procedure is as follows:

1. Log in to the initial monitor node(s):

```bash
ssh {hostname}
```

   For example:

```bash
ssh mon-node1
```

1. Ensure you have a directory for the Ceph configuration file. By default,
   Ceph uses ``/etc/ceph``. When you install ``ceph``, the installer will
   create the ``/etc/ceph`` directory automatically.

```bash
ls /etc/ceph
```

1. Create a Ceph configuration file. By default, Ceph uses
   ``ceph.conf``, where ``ceph`` reflects the cluster name. Add a line
   containing "[global]" to the configuration file.

```bash
sudo vim /etc/ceph/ceph.conf
```

1. Generate a unique ID (i.e., ``fsid``) for your cluster.

```bash
uuidgen
```

1. Add the unique ID to your Ceph configuration file.

```
fsid = {UUID}
```

   For example:

```
fsid = a7f64266-0894-4f1e-a635-d0aeaca0e993
```

1. Add the initial monitor(s) to your Ceph configuration file.

```
mon_initial_members = {hostname}[,{hostname}]
```

   For example:

```
mon_initial_members = mon-node1
```

1. Add the IP address(es) of the initial monitor(s) to your Ceph configuration
   file and save the file.

```
mon_host = {ip-address}[,{ip-address}]
```

   For example

```
mon_host = 192.168.0.1
```

> **Note:** You may use IPv6 addresses instead of IPv4 addresses, but you must set ``ms_bind_ipv6`` to ``true``. See [Network Configuration Reference](../rados/configuration/network-config-ref.md) for details about network configuration.

1. Create a keyring for your cluster and generate a monitor secret key.

```bash
sudo ceph-authtool --create-keyring /tmp/ceph.mon.keyring --gen-key -n mon.
```

> **Note:** The ``mon.`` credential does not require any capabilities. All Monitors share this single key.

1. Generate an administrator keyring, generate a ``client.admin`` user and add
   the user to the keyring.

```bash
sudo ceph-authtool --create-keyring /etc/ceph/ceph.client.admin.keyring --gen-key -n client.admin --cap mon 'allow *' --cap osd 'allow *' --cap mds 'allow *' --cap mgr 'allow *'
```

1. Generate a bootstrap-osd keyring, generate a ``client.bootstrap-osd`` user and add
   the user to the keyring.

```bash
sudo ceph-authtool --create-keyring /var/lib/ceph/bootstrap-osd/ceph.keyring --gen-key -n client.bootstrap-osd --cap mon 'profile bootstrap-osd' --cap mgr 'allow r'
```

1. Add the generated keys to the ``ceph.mon.keyring``.

```bash
sudo ceph-authtool /tmp/ceph.mon.keyring --import-keyring /etc/ceph/ceph.client.admin.keyring
sudo ceph-authtool /tmp/ceph.mon.keyring --import-keyring /var/lib/ceph/bootstrap-osd/ceph.keyring
```

1. Change the owner for ``ceph.mon.keyring``.

```bash
sudo chown ceph:ceph /tmp/ceph.mon.keyring
```

1. Configure CephX for cluster

> **Note:** This step can also be done after cluster creation.

   If you need to support legacy clients authenticating with the cluster, you will want to allow older insecure ciphers:

```bash
AUTH_SETTINGS="--auth-allowed-ciphers=aes,aes256k"
```

   If you also want new keys to use the legacy (and insecure) ``aes`` cipher by default:

```bash
AUTH_SETTINGS="$AUTH_SETTINGS --auth-preferred-cipher=aes"
```

   The service cipher type can also be configured but this should generally not need to be done unless an older version of a service daemon needs to run in the cluster:

```bash
AUTH_SETTINGS="$AUTH_SETTINGS --auth-service-cipher=aes"
```

> **Note:** Clients do not and cannot decrypt the service cipher.

1. Generate a monitor map using the hostname(s), host IP address(es) and the FSID.
   Save it as ``/tmp/monmap``:

```bash
monmaptool --create $AUTH_SETTINGS --add {hostname} {ip-address} --fsid {uuid} /tmp/monmap
```

   For example:

```bash
monmaptool --create $AUTH_SETTINGS --add mon-node1 192.168.0.1 --fsid a7f64266-0894-4f1e-a635-d0aeaca0e993 /tmp/monmap
```

1. Create a default data directory (or directories) on the monitor host(s).

```bash
sudo mkdir /var/lib/ceph/mon/{cluster-name}-{hostname}
```

   For example:

```bash
sudo -u ceph mkdir /var/lib/ceph/mon/ceph-mon-node1
```

   See [Monitor Config Reference - Data](../rados/configuration/mon-config-ref.md#data) for details.

1. Populate the monitor daemon(s) with the monitor map and keyring.

```bash
sudo -u ceph ceph-mon [--cluster {cluster-name}] --mkfs -i {hostname} --monmap /tmp/monmap --keyring /tmp/ceph.mon.keyring
```

   For example:

```bash
sudo -u ceph ceph-mon --mkfs -i mon-node1 --monmap /tmp/monmap --keyring /tmp/ceph.mon.keyring
```

1. Consider minimal settings for a Ceph configuration file. Common settings include
   the following:

```
[global]
fsid = {cluster-id}
mon_initial_members = {hostname}[, {hostname}]
mon_host = {ip-address}[, {ip-address}]
public_network = {network}[, {network}]
cluster_network = {network}[, {network}]
```

   In the foregoing example, the ``[global]`` section of the configuration might
   look like this:

```
[global]
fsid = a7f64266-0894-4f1e-a635-d0aeaca0e993
mon_initial_members = mon-node1
mon_host = 192.168.0.1
public_network = 192.168.0.0/24
```

> **Note:** Your preference as an operator should be to effect configuration changes through the ``ceph config`` API rather than in the ``ceph.conf`` file. See also [configuring-ceph-api](../rados/configuration/ceph-conf.md#configuring-ceph-api).

1. Start the monitor(s) with systemd.

```bash
sudo systemctl start ceph-mon@mon-node1
```

1. Ensure to open firewall ports for ceph-mon.

   Open the ports with firewalld:

```bash
sudo firewall-cmd --zone=public --add-service=ceph-mon
sudo firewall-cmd --zone=public --add-service=ceph-mon --permanent
```

1. Verify that the monitor is running.

```bash
sudo ceph -s
```

   You should see output that the monitor you started is up and running, and
   you should see a health error indicating that placement groups are stuck
   inactive. It should look something like this:

   :

```
cluster:
  id:     a7f64266-0894-4f1e-a635-d0aeaca0e993
  health: HEALTH_OK

services:
  mon: 1 daemons, quorum mon-node1
  mgr: mon-node1(active)
  osd: 0 osds: 0 up, 0 in

data:
  pools:   0 pools, 0 pgs
  objects: 0 objects, 0 bytes
  usage:   0 kB used, 0 kB / 0 kB avail
  pgs:
```

> **Note:** Once you add OSDs and start them, any placement group health errors should disappear. See [Adding OSDs](manual-deployment.md#adding-osds) for details.

> **Warning:** If you have enabled legacy cipher types then the Monitors may raise health warnings. You may mute (see [rados-monitoring-muting-health-checks](../rados/operations/monitoring.md#rados-monitoring-muting-health-checks)) the warnings. See the warning descriptions in [health-checks](../rados/operations/health-checks.md#health-checks) for more information on the different warnings.

# Manager daemon configuration

On each node where you run a ceph-mon daemon, you should also set up a ceph-mgr daemon.

See [mgr-administrator-guide](../mgr/administrator.md#mgr-administrator-guide)

# Adding OSDs

Once you have your initial monitor(s) running, you should add OSDs. Your cluster
cannot reach an ``active + clean`` state until you have enough OSDs to handle the
number of copies of an object (e.g., ``osd_pool_default_size = 2`` requires at
least two OSDs). After bootstrapping your monitor, your cluster has a default
CRUSH map; however, the CRUSH map doesn't have any Ceph OSD Daemons mapped to
a Ceph Node.

## Short Form

Ceph provides the ``ceph-volume`` utility, which can prepare a logical volume, disk, or partition
for use with Ceph. The ``ceph-volume`` utility creates the OSD ID by
incrementing the index. Additionally, ``ceph-volume`` will add the new OSD to the
CRUSH map under the host for you. Execute ``ceph-volume -h`` for CLI details.
The ``ceph-volume`` utility automates the steps of the [Long Form](manual-deployment.md#long-form) below. To
create the first two OSDs with the short form procedure, execute the following for each OSD:

1. Create the OSD. :

```
     copy /var/lib/ceph/bootstrap-osd/ceph.keyring from monitor node (mon-node1) to /var/lib/ceph/bootstrap-osd/ceph.keyring on osd node (osd-node1)
     ssh {osd node}
     sudo ceph-volume lvm create --data {data-path}

For example::

     scp -3 root@mon-node1:/var/lib/ceph/bootstrap-osd/ceph.keyring root@osd-node1:/var/lib/ceph/bootstrap-osd/ceph.keyring

     ssh osd-node1
     sudo ceph-volume lvm create --data /dev/hdd1
```

Alternatively, the creation process can be split in two phases (prepare, and
activate):

1. Prepare the OSD. :

```
     ssh {osd node}
     sudo ceph-volume lvm prepare --data {data-path} {data-path}

For example::

     ssh osd-node1
     sudo ceph-volume lvm prepare --data /dev/hdd1

Once prepared, the ``ID`` and ``FSID`` of the prepared OSD are required for
activation. These can be obtained by listing OSDs in the current server::

 sudo ceph-volume lvm list
```

1. Activate the OSD:

```
     sudo ceph-volume lvm activate {ID} {FSID}

For example::

     sudo ceph-volume lvm activate 0 a7f64266-0894-4f1e-a635-d0aeaca0e993
```

## Long Form

Without the benefit of any helper utilities, create an OSD and add it to the
cluster and CRUSH map with the following procedure. To create the first two
OSDs with the long form procedure, execute the following steps for each OSD.

> **Note:** This procedure does not describe deployment on top of dm-crypt
> making use of the dm-crypt 'lockbox'.

1. Connect to the OSD host and become root. :

```
ssh {node-name}
sudo bash
```

1. Generate a UUID for the OSD. :

```
UUID=$(uuidgen)
```

1. Generate a cephx key for the OSD. :

```
OSD_SECRET=$(ceph-authtool --gen-print-key)
```

1. Create the OSD. Note that an OSD ID can be provided as an
   additional argument to ``ceph osd new`` if you need to reuse a
   previously-destroyed OSD id. We assume that the
   ``client.bootstrap-osd`` key is present on the machine.  You may
   alternatively execute this command as ``client.admin`` on a
   different host where that key is present.:

```
ID=$(echo "{\"cephx_secret\": \"$OSD_SECRET\"}" | \
   ceph osd new $UUID -i - \
   -n client.bootstrap-osd -k /var/lib/ceph/bootstrap-osd/ceph.keyring)
```

   It is also possible to include a ``crush_device_class`` property in the JSON
   to set an initial class other than the default (``ssd`` or ``hdd`` based on
   the auto-detected device type).

1. Create the default directory on your new OSD. :

```
mkdir /var/lib/ceph/osd/ceph-$ID
```

1. If the OSD is for a drive other than the OS drive, prepare it
   for use with Ceph, and mount it to the directory you just created. :

```
mkfs.xfs /dev/{DEV}
mount /dev/{DEV} /var/lib/ceph/osd/ceph-$ID
```

1. Write the secret to the OSD keyring file. :

```
ceph-authtool --create-keyring /var/lib/ceph/osd/ceph-$ID/keyring \
     --name osd.$ID --add-key $OSD_SECRET
```

1. Initialize the OSD data directory. :

```
ceph-osd -i $ID --mkfs --osd-uuid $UUID
```

1. Fix ownership. :

```
chown -R ceph:ceph /var/lib/ceph/osd/ceph-$ID
```

1. After you add an OSD to Ceph, the OSD is in your configuration. However,
   it is not yet running. You must start
   your new OSD before it can begin receiving data.

   For modern systemd distributions:

```
systemctl enable ceph-osd@$ID
systemctl start ceph-osd@$ID
```

   For example:

```
systemctl enable ceph-osd@12
systemctl start ceph-osd@12
```

# Adding MDS

Please see the section on manual deployment in [manual-mds](../cephfs/add-remove-mds.md#manual-mds).

# Manually Installing RADOSGW

For a more involved discussion of the procedure presented here, see [this
thread on the ceph-users mailing list](https://lists.ceph.io/hyperkitty/list/ceph-users@ceph.io/message/LB3YRIKAPOHXYCW7MKLVUJPYWYRQVARU/).

1. Install ``radosgw`` packages on the nodes that will be the RGW nodes.

1. From a monitor or from a node with admin privileges, run a command of the
   following form:

```bash
ceph auth get-or-create client.$(hostname -s) mon 'allow rw' osd 'allow rwx'
```

1. On one of the RGW nodes, do the following:

   a. Create a ``ceph-user``-owned directory. For example:

```bash
install -d -o ceph -g ceph /var/lib/ceph/radosgw/ceph-$(hostname -s)
```

   b. Enter the directory just created and create a ``keyring`` file:

```bash
touch /var/lib/ceph/radosgw/ceph-$(hostname -s)/keyring
```

      Use a command similar to this one to put the key from the earlier ``ceph
      auth get-or-create`` step in the ``keyring`` file. Use your preferred
      editor:

```bash
$EDITOR /var/lib/ceph/radosgw/ceph-$(hostname -s)/keyring
```

   c. Repeat these steps on every RGW node.

1. Start the RADOSGW service by running the following command:

```bash
systemctl start ceph-radosgw@$(hostname -s).service
```

# Summary

Once you have your monitor and two OSDs up and running, you can watch the
placement groups peer by executing the following:

```
ceph -w
```

To view the tree, execute the following:

```
ceph osd tree
```

You should see output that looks something like this:

```
# id    weight  type name       up/down reweight
-1      2       root default
-2      2               host osd-node1
0       1                       osd.0   up      1
-3      1               host osd-node2
1       1                       osd.1   up      1
```

To add (or remove) additional monitors, see [Add/Remove Monitors](../rados/operations/add-or-rm-mons.md).
To add (or remove) additional Ceph OSD Daemons, see [Add/Remove OSDs](../rados/operations/add-or-rm-osds.md).
