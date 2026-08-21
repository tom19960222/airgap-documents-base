---
collection: kernel
version: "6.8"
title: "6.1.1.4. frontend events"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/dvb-frontend-event.html
fetched_at: 2026-08-21T03:39:36+00:00
---
type dvb_frontend_event

# 6.1.1.4. frontend events

```c
struct dvb_frontend_event {
    fe_status_t status;
    struct dvb_frontend_parameters parameters;
};
```
