---
collection: istio
version: "1.24"
title: "Debugging Virtual Machines"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ops/diagnostic-tools/virtual-machines/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Describes tools and techniques to diagnose issues with Virtual Machines."
---
This page describes how to troubleshoot issues with Istio deployed to Virtual Machines.
Before reading this, you should take the steps in [Virtual Machine Installation](../../../setup/install/virtual-machine/index.md).
Additionally, [Virtual Machine Architecture](../../deployment/vm-architecture/index.md) can help you understand how the components interact.

Troubleshooting an Istio Virtual Machine installation is similar to troubleshooting issues with proxies running inside Kubernetes, but there are some key differences to be aware of.

While much of the same information is available on both platforms, accessing this information differs.

## Monitoring health

The Istio sidecar is typically run as a `systemd` unit. To ensure its running properly, you can check that status:

```bash
$ systemctl status istio
```

Additionally, the sidecar health can be programmatically check at its health endpoint:

```bash
$ curl localhost:15021/healthz/ready -I
```

## Logs

Logs for the Istio proxy can be found in a few places.

To access the `systemd` logs, which has details about the initialization of the proxy:

```bash
$ journalctl -f -u istio -n 1000
```

The proxy will redirect `stderr` and `stdout` to `/var/log/istio/istio.err.log` and  `/var/log/istio/istio.log`, respectively.
To view these in a format similar to `kubectl`:

```bash
$ tail /var/log/istio/istio.err.log /var/log/istio/istio.log -Fq -n 100
```

Log levels can be modified by changing the `cluster.env` configuration file. Make sure to restart `istio` if it is already running:

```bash
$ echo "ISTIO_AGENT_FLAGS=\"--log_output_level=dns:debug --proxyLogLevel=debug\"" >> /var/lib/istio/envoy/cluster.env
$ systemctl restart istio
```

## Iptables

To ensure `iptables` rules have been successfully applied:

```bash
$ sudo iptables-save
...
-A ISTIO_OUTPUT -d 127.0.0.1/32 -j RETURN
-A ISTIO_OUTPUT -j ISTIO_REDIRECT
```

## Istioctl

Most `istioctl` commands will function properly with virtual machines. For example, `istioctl proxy-status` can be used to view all connected proxies:

```bash
$ istioctl proxy-status
NAME           CDS        LDS        EDS        RDS      ISTIOD                    VERSION
vm-1.default   SYNCED     SYNCED     SYNCED     SYNCED   istiod-789ffff8-f2fkt     [istio_full_version]
```

However, `istioctl proxy-config` relies on functionality in Kubernetes to connect to a proxy, which will not work for virtual machines.
Instead, a file containing the configuration dump from Envoy can be passed. For example:

```bash
$ curl -s localhost:15000/config_dump | istioctl proxy-config clusters --file -
SERVICE FQDN                            PORT      SUBSET  DIRECTION     TYPE
istiod.istio-system.svc.cluster.local   443       -       outbound      EDS
istiod.istio-system.svc.cluster.local   15010     -       outbound      EDS
istiod.istio-system.svc.cluster.local   15012     -       outbound      EDS
istiod.istio-system.svc.cluster.local   15014     -       outbound      EDS
```

## Automatic registration

When a virtual machine connects to Istiod, a `WorkloadEntry` will automatically be created. This enables
the virtual machine to become a part of a `Service`, similar to an `Endpoint` in Kubernetes.

To check these are created correctly:

```bash
$ kubectl get workloadentries
NAME             AGE   ADDRESS
vm-10.128.0.50   14m   10.128.0.50
```

## Certificates

Virtual machines handle certificates differently than Kubernetes Pods, which use a Kubernetes-provided service account token
to authenticate and renew mTLS certificates. Instead, existing mTLS credentials are used to authenticate with the certificate authority and
renew certificates.

The status of these certificates can be viewed in the same way as in Kubernetes:

```bash
$ curl -s localhost:15000/config_dump | ./istioctl proxy-config secret --file -
RESOURCE NAME     TYPE           STATUS     VALID CERT     SERIAL NUMBER                               NOT AFTER                NOT BEFORE
default           Cert Chain     ACTIVE     true           251932493344649542420616421203546836446     2021-01-29T18:07:21Z     2021-01-28T18:07:21Z
ROOTCA            CA             ACTIVE     true           81663936513052336343895977765039160718      2031-01-26T17:54:44Z     2021-01-28T17:54:44Z
```

Additionally, these are persisted to disk to ensure downtime or restarts do not lose state.

```bash
$ ls /etc/certs
cert-chain.pem  key.pem  root-cert.pem
```
