---
collection: kernel
version: "6.8"
title: "Reliability, Availability and Serviceability features"
source_url: https://www.kernel.org/doc/html/v6.8/RAS/ras.html
fetched_at: 2026-08-21T03:28:51+00:00
---
# Reliability, Availability and Serviceability features

This documents different aspects of the RAS functionality present in the
kernel.

## Error decoding

- x86

Error decoding on AMD systems should be done using the rasdaemon tool:
<https://github.com/mchehab/rasdaemon/>

While the daemon is running, it would automatically log and decode
errors. If not, one can still decode such errors by supplying the
hardware information from the error:

```
$ rasdaemon -p --status <STATUS> --ipid <IPID> --smca
```

Also, the user can pass particular family and model to decode the error
string:

```
$ rasdaemon -p --status <STATUS> --ipid <IPID> --smca --family <CPU Family> --model <CPU Model> --bank <BANK_NUM>
```
