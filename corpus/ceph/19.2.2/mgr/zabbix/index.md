---
collection: ceph
version: "19.2.2"
title: "Zabbix Module"
source_url: https://docs.ceph.com/en/squid/mgr/zabbix/
fetched_at: 2026-07-27T16:40:51+00:00
---
# Zabbix Module

The Zabbix module has not been supported since April 2020 at the latest. The
upstream Ceph community in April 2024 developed procedures for installing
Zabbix 2.

Discussion of the decisions around the lack of support for Zabbix can be found
here: <https://github.com/ceph/ceph-container/issues/1651>

## Installing zabbix-agent 2

*The procedures that explain the installation of Zabbix 2 were developed by John Jasen.*

Follow the instructions in the sections [Ceph MGR Nodes](index.md#mgr-zabbix-2-nodes),
[Ceph Cluster](index.md#mgr-zabbix-2-cluster), and [Zabbix Server](index.md#mgr-zabbix-2-server) to install a Zabbix
server to monitor your Ceph cluster.

### Ceph MGR Nodes

1. Download an appropriate Zabbix release from <https://www.zabbix.com/download>
   or install a package from the Zabbix repositories.
2. Use your package manager to remove any other Zabbix agents.
3. Install `zabbix-agent 2` using the instructions at
   <https://www.zabbix.com/download>.
4. Edit `/etc/zabbix/zabbix-agent2.conf`. Add your Zabbix monitoring servers
   and your localhost to the `Servers` line of `zabbix-agent2.conf`:

   ```
   Server=127.0.0.1,zabbix2.example.com,zabbix1.example.com
   ```
5. Start or restart the `zabbix-agent2` agent:

   ```
   systemctl restart zabbix-agent2
   ```

### Ceph Cluster

1. Enable the `restful` module:

   ```
   ceph mgr module enable restful
   ```
2. Generate a self-signed certificate. This step is optional:

   ```
   restful create-self-signed-cert
   ```
3. Create an API user called `zabbix-monitor`:

   ```
   ceph restful create-key zabbix-monitor
   ```

   The output of this command, an API key, will look something like this:

   ```
   a4bb2019-XXXX-YYYY-ZZZZ-abcdefghij
   ```
4. Save the generated API key. It will be necessary later.
5. Test API access by using `zabbix-get`:

   > **Note:**
   >
   > This step is optional.

   ```
   zabbix_get -s 127.0.0.1 -k ceph.ping["${CEPH.CONNSTRING}","${CEPH.USER}","{CEPH.API.KEY}"
   ```

   Example:

   ```
   zabbix_get -s 127.0.0.1 -k ceph.ping["https://localhost:8003","zabbix-monitor","a4bb2019-XXXX-YYYY-ZZZZ-abcdefghij"]
   ```

   > **Note:**
   >
   > You may need to install `zabbix-get` via your package manager.

### Zabbix Server

1. Create a host for the Ceph monitoring servers.
2. Add the template `Ceph by Zabbix agent 2` to the host.
3. Inform the host of the keys:

   1. Go to “Macros” on the host.
   2. Show “Inherited and host macros”.
   3. Change `${CEPH.API.KEY}` and `${CEPH.USER}` to the values provided
      under `ceph restful create-key`, above. Example:

      ```
      {$CEPH.API.KEY} a4bb2019-XXXX-YYYY-ZZZZ-abcdefghij
      {$CEPH.USER} zabbix-monitor
      ```
4. Update the host. Within a few cycles, data will populate the server.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
