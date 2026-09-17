---
collection: kernel
version: "6.17"
title: "Kyber I/O scheduler tunables"
source_url: https://www.kernel.org/doc/html/v6.17/block/kyber-iosched.html
fetched_at: 2026-09-16T16:42:34+00:00
---
# Kyber I/O scheduler tunables

The only two tunables for the Kyber scheduler are the target latencies for
reads and synchronous writes. Kyber will throttle requests in order to meet
these target latencies.

## read_lat_nsec

Target latency for reads (in nanoseconds).

## write_lat_nsec

Target latency for synchronous writes (in nanoseconds).
