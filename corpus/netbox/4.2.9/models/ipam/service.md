---
collection: netbox
version: "4.2.9"
title: "Services"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/ipam/service.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Services

A service represents a layer seven application available on a device or virtual machine. For example, a service might be created in NetBox to represent an HTTP server running on TCP/8000. Each service may optionally be further bound to one or more specific interfaces assigned to the selected device or virtual machine.

To aid in the efficient creation of services, users may opt to first create a [service template](./servicetemplate.md) from which service definitions can be quickly replicated.

## Fields

### Name

A service or protocol name.

### Protocol

The wire protocol on which the service runs. Choices include UDP, TCP, and SCTP.

### Ports

One or more numeric ports to which the service is bound. Multiple ports can be expressed using commas and/or hyphens. For example, `80,8001-8003` specifies ports 80, 8001, 8002, and 8003.

### IP Addresses

The [IP address(es)](./ipaddress.md) to which this service is bound. If no IP addresses are bound, the service is assumed to be reachable via any assigned IP address.
