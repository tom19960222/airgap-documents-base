---
collection: kernel
version: "6.17"
title: "VIA82xx mixer"
source_url: https://www.kernel.org/doc/html/v6.17/sound/cards/via82xx-mixer.html
fetched_at: 2026-09-16T16:39:10+00:00
---
# VIA82xx mixer

On many VIA82xx boards, the `Input Source Select` mixer control does not work.
Setting it to `Input2` on such boards will cause recording to hang, or fail
with EIO (input/output error) via OSS emulation. This control should be left
at `Input1` for such cards.
