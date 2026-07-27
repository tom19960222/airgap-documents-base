---
collection: ceph
version: "19.2.2"
title: "Host Management"
source_url: https://docs.ceph.com/en/squid/cephadm/host-management/
fetched_at: 2026-07-27T16:39:01+00:00
---
# Host Management

## Listing Hosts

Run a command of this form to list hosts associated with the cluster:

```
ceph orch host ls [--format yaml] [--host-pattern <name>] [--label <label>] [--host-status <status>] [--detail]
```

In commands of this form, the arguments “host-pattern”, “label”, and
“host-status” are optional and are used for filtering.

- “host-pattern” is a regex that matches against hostnames and returns only
  matching hosts.
- “label” returns only hosts with the specified label.
- “host-status” returns only hosts with the specified status (currently
  “offline” or “maintenance”).
- Any combination of these filtering flags is valid. It is possible to filter
  against name, label and status simultaneously, or to filter against any
  proper subset of name, label and status.

The “detail” parameter provides more host related information for cephadm based
clusters. For example:

```
ceph orch host ls --detail
```

```
HOSTNAME     ADDRESS         LABELS  STATUS  VENDOR/MODEL                           CPU    HDD      SSD  NIC
ceph-master  192.168.122.73  _admin          QEMU (Standard PC (Q35 + ICH9, 2009))  4C/4T  4/1.6TB  -    1
1 hosts in cluster
```

## Adding Hosts

Hosts must have these [Requirements](../install/index.md#cephadm-host-requirements) installed.
Hosts without all the necessary requirements will fail to be added to the cluster.

To add each new host to the cluster, perform two steps:

1. Install the cluster’s public SSH key in the new host’s root user’s `authorized_keys` file:

   ```
   ssh-copy-id -f -i /etc/ceph/ceph.pub root@*<new-host>*
   ```

   For example:

   ```
   ssh-copy-id -f -i /etc/ceph/ceph.pub root@host2
   ssh-copy-id -f -i /etc/ceph/ceph.pub root@host3
   ```
2. Tell Ceph that the new node is part of the cluster:

   ```
   ceph orch host add *<newhost>* [*<ip>*] [*<label1> ...*]
   ```

   For example:

   ```
   ceph orch host add host2 10.10.0.102
   ceph orch host add host3 10.10.0.103
   ```

   It is best to explicitly provide the host IP address. If an address is
   not provided, then the host name will be immediately resolved via
   DNS and the result will be used.

   One or more labels can also be included to immediately label the
   new host. For example, by default the `_admin` label will make
   cephadm maintain a copy of the `ceph.conf` file and a
   `client.admin` keyring file in `/etc/ceph`:

   ```
   ceph orch host add host4 10.10.0.104 --labels _admin
   ```

## Removing Hosts

A host can safely be removed from the cluster after all daemons are removed
from it.

To drain all daemons from a host, run a command of the following form:

```
ceph orch host drain *<host>*
```

The `_no_schedule` and `_no_conf_keyring` labels will be applied to the
host. See [Special host labels](index.md#cephadm-special-host-labels).

If you want to drain daemons but leave managed ceph.conf and keyring
files on the host, you may pass the `--keep-conf-keyring` flag to the
drain command.

```
ceph orch host drain *<host>* --keep-conf-keyring
```

This will apply the `_no_schedule` label to the host but not the
`_no_conf_keyring` label.

All OSDs on the host will be scheduled to be removed. You can check
progress of the OSD removal operation with the following command:

```
ceph orch osd rm status
```

See [Remove an OSD](../services/osd/index.md#cephadm-osd-removal) for more details about OSD removal.

The `orch host drain` command also supports a `--zap-osd-devices`
flag. Setting this flag while draining a host will cause cephadm to zap
the devices of the OSDs it is removing as part of the drain process

```
ceph orch host drain *<host>* --zap-osd-devices
```

Use the following command to determine whether any daemons are still on the
host:

```
ceph orch ps <host>
```

After all daemons have been removed from the host, remove the host from the
cluster by running the following command:

```
ceph orch host rm <host>
```

### Offline host removal

If a host is offline and can not be recovered, it can be removed from the
cluster by running a command of the following form:

```
ceph orch host rm <host> --offline --force
```

> **Warning:**
>
> This can potentially cause data loss. This command forcefully
> purges OSDs from the cluster by calling `osd purge-actual` for each OSD.
> Any service specs that still contain this host should be manually updated.

## Host labels

The orchestrator supports assigning labels to hosts. Labels
are free form and have no particular meaning by itself and each host
can have multiple labels. They can be used to specify placement
of daemons. See [Placement by labels](../services/index.md#orch-placement-by-labels)

Labels can be added when adding a host with the `--labels` flag:

```
ceph orch host add my_hostname --labels=my_label1
ceph orch host add my_hostname --labels=my_label1,my_label2
```

To add a label a existing host, run:

```
ceph orch host label add my_hostname my_label
```

To remove a label, run:

```
ceph orch host label rm my_hostname my_label
```

### Special host labels

The following host labels have a special meaning to cephadm. All start with `_`.

- `_no_schedule`: *Do not schedule or deploy daemons on this host*.

  This label prevents cephadm from deploying daemons on this host. If it is added to
  an existing host that already contains Ceph daemons, it will cause cephadm to move
  those daemons elsewhere (except OSDs, which are not removed automatically).
- `_no_conf_keyring`: *Do not deploy config files or keyrings on this host*.

  This label is effectively the same as `_no_schedule` but instead of working for
  daemons it works for client keyrings and ceph conf files that are being managed
  by cephadm
- `_no_autotune_memory`: *Do not autotune memory on this host*.

  This label will prevent daemon memory from being tuned even when the
  `osd_memory_target_autotune` or similar option is enabled for one or more daemons
  on that host.
- `_admin`: *Distribute client.admin and ceph.conf to this host*.

  By default, an `_admin` label is applied to the first host in the cluster (where
  bootstrap was originally run), and the `client.admin` key is set to be distributed
  to that host via the `ceph orch client-keyring ...` function. Adding this label
  to additional hosts will normally cause cephadm to deploy config and keyring files
  in `/etc/ceph`. Starting from versions 16.2.10 (Pacific) and 17.2.1 (Quincy) in
  addition to the default location `/etc/ceph/` cephadm also stores config and keyring
  files in the `/var/lib/ceph/<fsid>/config` directory.

## Maintenance Mode

Putting a host into “maintenance mode” stops all Ceph daemons on the host. Run
a command of the following form to put a host into maintenance mode or to take
a host out of maintenance mode:

```
ceph orch host maintenance enter <hostname> [--force] [--yes-i-really-mean-it]
ceph orch host maintenance exit <hostname>
```

- Adding the `--force` flag to the `enter` command allows the user to bypass
  warnings (but not alerts).
- Adding the `--yes-i-really-mean-it` flag to the `enter` command bypasses
  all safety checks and makes an attempt to force the host into maintenance
  mode.
- Adding the `--force` and `--offline` flags to the `exit` command cause
  cephadm to mark hosts that are in maintenance mode and offline as no longer
  in maintenance mode. Note that if the host comes online, the Ceph daemons on
  the host will remain in the stopped state. The `--force` and `--offline`
  flags of the `exit` command are meant to be run on hosts that are in
  maintenance mode and that are permanently offline prior to the removal of
  those hosts from cephadm management by running the `ceph orch host rm`
  command.

> **Warning:**
>
> Using the `--yes-i-really-mean-it` flag to force the host to
> enter maintenance mode can cause loss of data availability, breakdown of the
> mon quorum due to too few running monitors, unresponsive mgr module commands
> (such as `ceph orch . . .` commands), and other issues. Use this flag only
> if you’re absolutely certain that you know what you’re doing.

See also [Fully qualified domain names vs bare host names](index.md#cephadm-fqdn)

## Rescanning Host Devices

Some servers and external enclosures may not register device removal or insertion with the
kernel. In these scenarios, you’ll need to perform a device rescan on the appropriate host.
A rescan is typically non-disruptive, and can be performed with the following CLI command:

```
ceph orch host rescan <hostname> [--with-summary]
```

The `with-summary` flag provides a breakdown of the number of HBAs found and scanned, together
with any that failed:

```
ceph orch host rescan rh9-ceph1 --with-summary
```

```
Ok. 2 adapters detected: 2 rescanned, 0 skipped, 0 failed (0.32s)
```

## Creating many hosts at once

Many hosts can be added at once using
`ceph orch apply -i` by submitting a multi-document YAML file:

```yaml
service_type: host
hostname: node-00
addr: 192.168.0.10
labels:
- example1
- example2
---
service_type: host
hostname: node-01
addr: 192.168.0.11
labels:
- grafana
---
service_type: host
hostname: node-02
addr: 192.168.0.12
```

This can be combined with [service specifications](../services/index.md#orchestrator-cli-service-spec)
to create a cluster spec file to deploy a whole cluster in one command. see
`cephadm bootstrap --apply-spec` also to do this during bootstrap. Cluster
SSH Keys must be copied to hosts prior to adding them.

## Setting the initial CRUSH location of host

Hosts can contain a `location` identifier which will instruct cephadm to
create a new CRUSH host bucket located in the specified hierarchy.
You can specify more than one element of the tree when doing so (for
instance if you want to ensure that the rack that a host is being
added to is also added to the default bucket), for example:

```yaml
service_type: host
hostname: node-00
addr: 192.168.0.10
location:
  root: default
  rack: rack1
```

> **Note:**
>
> The `location` attribute will affect only the initial CRUSH location.
> Subsequent changes to the `location` property will be ignored.
> Removing a host will not remove an associated CRUSH bucket unless the
> `--rm-crush-entry` flag is provided to the `orch host rm` command.

See also [Types and Buckets](../../rados/operations/crush-map/index.md#crush-map-default-types).

## Removing a host from the CRUSH map

The `ceph orch host rm` command has support for removing the associated host bucket
from the CRUSH map. This is done by providing the `--rm-crush-entry` flag.

```
ceph orch host rm host1 --rm-crush-entry
```

When this flag is specified, cephadm will attempt to remove the host bucket
from the CRUSH map as part of the host removal process. Note that if
it fails to do so, cephadm will report the failure and the host will remain under
cephadm control.

> **Note:**
>
> Removal from the CRUSH map will fail if there are OSDs deployed on the
> host. If you would like to remove all the host’s OSDs as well, please start
> by using the `ceph orch host drain` command to do so. Once the OSDs
> have been removed, then you may direct cephadm remove the CRUSH bucket
> along with the host using the `--rm-crush-entry` flag.

## OS Tuning Profiles

Cephadm can be used to manage operating system tuning profiles that apply
`sysctl` settings to sets of hosts.

To do so, create a YAML spec file in the following format:

```yaml
profile_name: 23-mon-host-profile
placement:
  hosts:
    - mon-host-01
    - mon-host-02
settings:
  fs.file-max: 1000000
  vm.swappiness: '13'
```

Apply the tuning profile with the following command:

```
ceph orch tuned-profile apply -i <tuned-profile-file-name>
```

This profile is written to a file under `/etc/sysctl.d/` on each host
specified in the `placement` block, then `sysctl --system` is
run on the host.

> **Note:**
>
> The exact filename that the profile is written to within `/etc/sysctl.d/`
> is `<profile-name>-cephadm-tuned-profile.conf`, where `<profile-name>` is
> the `profile_name` setting that you specify in the YAML spec. We suggest
> naming these profiles following the usual `sysctl.d` NN-xxxxx convention. Because
> sysctl settings are applied in lexicographical order (sorted by the filename
> in which the setting is specified), you may want to carefully choose
> the `profile_name` in your spec so that it is applied before or after other
> conf files. Careful selection ensures that values supplied here override or
> do not override those in other `sysctl.d` files as desired.

> **Note:**
>
> These settings are applied only at the host level, and are not specific
> to any particular daemon or container.

> **Note:**
>
> Applying tuning profiles is idempotent when the `--no-overwrite` option is
> passed. Moreover, if the `--no-overwrite` option is passed, existing
> profiles with the same name are not overwritten.

### Viewing Profiles

Run the following command to view all the profiles that cephadm currently manages:

```
ceph orch tuned-profile ls
```

> **Note:**
>
> To make modifications and re-apply a profile, pass `--format yaml` to the
> `tuned-profile ls` command. The `tuned-profile ls --format yaml` command
> presents the profiles in a format that is easy to copy and re-apply.

### Removing Profiles

To remove a previously applied profile, run this command:

```
ceph orch tuned-profile rm <profile-name>
```

When a profile is removed, cephadm cleans up the file previously written to `/etc/sysctl.d`.

### Modifying Profiles

Profiles can be modified by re-applying a YAML spec with the same name as the
profile that you want to modify, but settings within existing profiles can be
adjusted with the following commands.

To add or modify a setting in an existing profile:

```
ceph orch tuned-profile add-setting <profile-name> <setting-name> <value>
```

To remove a setting from an existing profile:

```
ceph orch tuned-profile rm-setting <profile-name> <setting-name>
```

> **Note:**
>
> Modifying the placement requires re-applying a profile with the same name.
> Remember that profiles are tracked by their names, so when a profile with the
> same name as an existing profile is applied, it overwrites the old profile
> unless the `--no-overwrite` flag is passed.

## SSH Configuration

Cephadm uses SSH to connect to remote hosts. SSH uses a key to authenticate
with those hosts in a secure way.

### Default behavior

Cephadm stores an SSH key in the monitor that is used to
connect to remote hosts. When the cluster is bootstrapped, this SSH
key is generated automatically and no additional configuration
is necessary.

A *new* SSH key can be generated with:

```
ceph cephadm generate-key
```

The public portion of the SSH key can be retrieved with:

```
ceph cephadm get-pub-key
```

The currently stored SSH key can be deleted with:

```
ceph cephadm clear-key
```

You can make use of an existing key by directly importing it with:

```
ceph config-key set mgr/cephadm/ssh_identity_key -i <key>
ceph config-key set mgr/cephadm/ssh_identity_pub -i <pub>
```

You will then need to restart the mgr daemon to reload the configuration with:

```
ceph mgr fail
```

### Configuring a different SSH user

Cephadm must be able to log into all the Ceph cluster nodes as an user
that has enough privileges to download container images, start containers
and execute commands without prompting for a password. If you do not want
to use the “root” user (default option in cephadm), you must provide
cephadm the name of the user that is going to be used to perform all the
cephadm operations. Use the command:

```
ceph cephadm set-user <user>
```

Prior to running this the cluster SSH key needs to be added to this users
authorized_keys file and non-root users must have passwordless sudo access.

### Customizing the SSH configuration

Cephadm generates an appropriate `ssh_config` file that is
used for connecting to remote hosts. This configuration looks
something like this:

```
Host *
User root
StrictHostKeyChecking no
UserKnownHostsFile /dev/null
```

There are two ways to customize this configuration for your environment:

1. Import a customized configuration file that will be stored
   by the monitor with:

   ```
   ceph cephadm set-ssh-config -i <ssh_config_file>
   ```

   To remove a customized SSH config and revert back to the default behavior:

   ```
   ceph cephadm clear-ssh-config
   ```
2. You can configure a file location for the SSH configuration file with:

   ```
   ceph config set mgr mgr/cephadm/ssh_config_file <path>
   ```

   We do *not recommend* this approach. The path name must be
   visible to *any* mgr daemon, and cephadm runs all daemons as
   containers. That means that the file must either be placed
   inside a customized container image for your deployment, or
   manually distributed to the mgr data directory
   (`/var/lib/ceph/<cluster-fsid>/mgr.<id>` on the host, visible at
   `/var/lib/ceph/mgr/ceph-<id>` from inside the container).

### Setting up CA signed keys for the cluster

Cephadm also supports using CA signed keys for SSH authentication
across cluster nodes. In this setup, instead of needing a private
key and public key, we instead need a private key and certificate
created by signing that private key with a CA key. For more info
on setting up nodes for authentication using a CA signed key, see
[Deployment with CA signed SSH keys](../install/index.md#cephadm-bootstrap-ca-signed-keys). Once you have your private
key and signed cert, they can be set up for cephadm to use by running:

```
ceph config-key set mgr/cephadm/ssh_identity_key -i <private-key-file>
ceph config-key set mgr/cephadm/ssh_identity_cert -i <signed-cert-file>
```

## Fully qualified domain names vs bare host names

> **Note:**
>
> cephadm demands that the name of the host given via `ceph orch host add`
> equals the output of `hostname` on remote hosts.

Otherwise cephadm can’t be sure that names returned by
`ceph * metadata` match the hosts known to cephadm. This might result
in a [CEPHADM_STRAY_HOST](../operations/index.md#cephadm-stray-host) warning.

When configuring new hosts, there are two **valid** ways to set the
`hostname` of a host:

1. Using the bare host name. In this case:

- `hostname` returns the bare host name.
- `hostname -f` returns the FQDN.

2. Using the fully qualified domain name as the host name. In this case:

- `hostname` returns the FQDN
- `hostname -s` return the bare host name

Note that `man hostname` recommends `hostname` to return the bare
host name:

> The FQDN (Fully Qualified Domain Name) of the system is the
> name that the resolver(3) returns for the host name, for example
> `ursula.example.com`. It is usually the short hostname followed by the DNS
> domain name (the part after the first dot). You can check the FQDN
> using `hostname --fqdn` or the domain name using `dnsdomainname`.
>
> ```
> You cannot change the FQDN with hostname or dnsdomainname.
>
> The recommended method of setting the FQDN is to make the hostname
> be an alias for the fully qualified name using /etc/hosts, DNS, or
> NIS. For example, if the hostname was "ursula", one might have
> a line in /etc/hosts which reads
>
>        127.0.1.1    ursula.example.com ursula
> ```

Which means, `man hostname` recommends `hostname` to return the bare
host name. This in turn means that Ceph will return the bare host names
when executing `ceph * metadata`. This in turn means cephadm also
requires the bare host name when adding a host to the cluster:
`ceph orch host add <bare-name>`.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
