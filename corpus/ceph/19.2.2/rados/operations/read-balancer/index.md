---
collection: ceph
version: "19.2.2"
title: "Operating the Read (Primary) Balancer"
source_url: https://docs.ceph.com/en/squid/rados/operations/read-balancer/
fetched_at: 2026-07-27T16:39:42+00:00
---
# Operating the Read (Primary) Balancer

You might be wondering: How can I improve performance in my Ceph cluster?
One important data point you can check is the `read_balance_score` on each
of your replicated pools.

This metric, available via `ceph osd pool ls detail` (see [Pools](../pools/index.md#rados-pools)
for more details) indicates read performance, or how balanced the primaries are
for each replicated pool. In most cases, if a `read_balance_score` is above 1
(for instance, 1.5), this means that your pool has unbalanced primaries and that
you may want to try improving your read performance with the read balancer.

## Online Optimization

### Enabling

To enable automatic read balancing, you must turn on the *balancer module*
(enabled by default in new clusters) and set the mode to `read` or `upmap-read`:

```
ceph balancer on
ceph balancer mode <read|upmap-read>
```

Both `read` and `upmap-read` mode make use of `pg-upmap-primary`. In order
to use `pg-upmap-primary`, the cluster cannot have any pre-Reef clients.

If you want to use a different balancer or if you want to make your
own custom `pg-upmap-primary` entries, you might want to turn off the balancer in
order to avoid conflict:

```
ceph balancer off
```

To allow use of the new feature on an existing cluster, you must restrict the
cluster to supporting only Reef (and newer) clients. To do so, run the
following command:

```
ceph osd set-require-min-compat-client reef
```

This command will fail if any pre-Reef clients or daemons are connected to
the monitors. To see which client versions are in use, run the following
command:

```
ceph features
```

### Balancer Module

The balancer module for `ceph-mgr` will automatically balance the number of
primary PGs per OSD if set to `read` or `upmap-read` mode. See [Balancer Module](../balancer/index.md#balancer)
for more information.

## Offline Optimization

Primaries are updated with an offline optimizer that is built into the
[osdmaptool -- ceph osd cluster map manipulation tool](../../../man/8/osdmaptool/index.md#osdmaptool).

1. Grab the latest copy of your osdmap:

   ```
   ceph osd getmap -o om
   ```
2. Run the optimizer:

   ```
   osdmaptool om --read out.txt --read-pool <pool name> [--vstart]
   ```

   It is highly recommended that you run the capacity balancer before running the
   balancer to ensure optimal results. See [Using pg-upmap](../upmap/index.md#upmap) for details on how to balance
   capacity in a cluster.
3. Apply the changes:

   ```
   source out.txt
   ```

   In the above example, the proposed changes are written to the output file
   `out.txt`. The commands in this procedure are normal Ceph CLI commands
   that can be run in order to apply the changes to the cluster.

   If you are working in a vstart cluster, you may pass the `--vstart` parameter
   as shown above so the CLI commands are formatted with the ./bin/ prefix.

   Note that any time the number of pgs changes (for instance, if the pg autoscaler [[Autoscaling placement groups](../placement-groups/index.md#pg-autoscaler)]
   kicks in), you should consider rechecking the scores and rerunning the balancer if needed.

To see some details about what the tool is doing, you can pass
`--debug-osd 10` to `osdmaptool`. To see even more details, pass
`--debug-osd 20` to `osdmaptool`.

## Troubleshooting

### Removing pg-upmap-primary mappings

For scenarios where you need to manually remove `pg-upmap-primary` mappings, Ceph provides the following
developer-level commands. These commands should be used with caution, as they directly modify
primary PG mappings and can impact read performance (this excludes any data movement).

> **Note:**
>
> Users affected by [#66867](https://tracker.ceph.com/issues/66867) or [#61948](https://tracker.ceph.com/issues/61948)
> may find these commands useful when dealing with unexpected `pg-upmap-primary` behavior.

To remove a specific `pg-upmap-primary` mapping, use:

```
ceph osd rm-pg-upmap-primary <pgid>
```

If you need to clear **all** `pg-upmap-primary` mappings in your cluster, you may use:

```
ceph osd rm-pg-upmap-primary-all
```

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
