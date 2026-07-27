---
collection: ceph
version: "19.2.2"
title: "PG Calc"
source_url: https://docs.ceph.com/en/squid/rados/operations/pgcalc/
fetched_at: 2026-07-27T16:39:38+00:00
---
# PG Calc

## Ceph PGs per Pool Calculator

  
Instructions

1. Confirm your understanding of the fields by reading through the Key below.
2. Select a **"Ceph Use Case"** from the drop down menu.
3. Adjust the values in the "Green" shaded fields below.  
   **Tip:** Headers can be clicked to change the value throughout the table.
4. You will see the Suggested PG Count update based on your inputs.
5. Click the **"Add Pool"** button to create a new line for a new pool.
6. Click the  icon to delete the specific Pool.
7. For more details on the logic used and some important details, see the area below the table.
8. Once all values have been adjusted, click the **"Generate Commands"** button to get the pool creation commands.

  
Ceph Use Case Selector:  
Add PoolGenerate Commands
  

Logic behind Suggested PG Count
  

( Target PGs per OSD ) x ( OSD # ) x ( %Data )

( Size )

1. If the value of the above calculation is less than the value of **( OSD# ) / ( Size )**, then the value is updated to the value of **( OSD# ) / ( Size )**. This is to ensure even load / data distribution by allocating at least one Primary or Secondary PG to every OSD for every Pool.
2. The output value is then rounded to the **nearest power of 2**.  
   **Tip:** The nearest power of 2 provides a marginal improvement in efficiency of the [CRUSH](https://web.archive.org/web/20230614135557/http://ceph.com/docs/master/rados/operations/crush-map/ "CRUSH Map Details") algorithm.
3. If the nearest power of 2 is more than **25%** below the original value, the next higher power of 2 is used.

**Objective**

- The objective of this calculation and the target ranges noted in the "Key" section above are to ensure that there are sufficient Placement Groups for even data distribution throughout the cluster, while not going high enough on the PG per OSD ratio to cause problems during Recovery and/or Backfill operations.

**Effects of empty or non-active pools:**

- Empty or otherwise non-active pools should not be considered helpful toward even data distribution throughout the cluster.
- However, the PGs associated with these empty / non-active pools still consume memory and CPU overhead.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
