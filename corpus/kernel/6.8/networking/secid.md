---
collection: kernel
version: "6.8"
title: "LSM/SeLinux secid"
source_url: https://www.kernel.org/doc/html/v6.8/networking/secid.html
fetched_at: 2026-08-21T03:49:45+00:00
---
# LSM/SeLinux secid

flowi structure:

The secid member in the flow structure is used in LSMs (e.g. SELinux) to indicate
the label of the flow. This label of the flow is currently used in selecting
matching labeled xfrm(s).

If this is an outbound flow, the label is derived from the socket, if any, or
the incoming packet this flow is being generated as a response to (e.g. tcp
resets, timewait ack, etc.). It is also conceivable that the label could be
derived from other sources such as process context, device, etc., in special
cases, as may be appropriate.

If this is an inbound flow, the label is derived from the IPSec security
associations, if any, used by the packet.
