---
collection: kernel
version: "6.8"
title: "Surface System Aggregator Module (SSAM)"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/surface_aggregator/index.html
fetched_at: 2026-08-21T03:31:20+00:00
---
# Surface System Aggregator Module (SSAM)

- [Overview](overview.md)
  - [Features and Integration](overview.md#features-and-integration)
  - [Communication](overview.md#communication)
- [Writing Client Drivers](client.md)
  - [Client Driver API Documentation](client-api.md)
  - [Overview](client.md#overview)
  - [Non-SSAM Client Drivers](client.md#non-ssam-client-drivers)
  - [Adding SSAM Devices](client.md#adding-ssam-devices)
  - [SSAM Client Drivers](client.md#ssam-client-drivers)
  - [Making Synchronous Requests](client.md#making-synchronous-requests)
  - [Handling Events](client.md#handling-events)
- [Client Driver Documentation](clients/index.md)
  - [User-Space EC Interface (cdev)](clients/cdev.md)
  - [User-Space DTX (Clipboard Detachment System) Interface](clients/dtx.md)
  - [Surface ACPI Notify](clients/san.md)
- [Surface Serial Hub Protocol](ssh.md)
  - [SSH Packet Protocol: Definitions](ssh.md#ssh-packet-protocol-definitions)
  - [SSH Packet Protocol: Flow Sequence](ssh.md#ssh-packet-protocol-flow-sequence)
  - [Commands: Requests, Responses, and Events](ssh.md#commands-requests-responses-and-events)
  - [Limitations and Observations](ssh.md#limitations-and-observations)
- [Core Driver Internals](internal.md)
  - [Internal API Documentation](internal-api.md)
  - [Overview](internal.md#overview)
  - [Packet Transport Layer](internal.md#packet-transport-layer)
  - [Request Transport Layer](internal.md#request-transport-layer)
  - [Controller Layer](internal.md#controller-layer)
