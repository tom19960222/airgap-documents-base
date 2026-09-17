---
collection: k8s-dns
version: "1.23.1"
title: "sidecar"
source_url: https://github.com/kubernetes/dns/blob/fd33e8663c6f83c771cdad6178614b882ae4fba0/docs/sidecar/README.md
fetched_at: 2024-05-13T08:19:40-07:00
---
# sidecar

`sidecar` is a daemon that exports metrics and performs healthcheck on DNS
systems.

## Running

`sidecar` is configured through command line flags, defaults of which
can be found by executing it with `--help`. Important flags to configure:

| Flag | Description |
| ---- | ---- |
| `--dnsmasq-{addr,port}` | endpoint of dnsmasq DNS service |
| `--prometheus-{addr,port}` | endpoint used to export metrics |
| `--probe` label,server,domain name,interval | probe DNS server with domain name every `interval` seconds, reporting its health under `healthcheck/`label. |
