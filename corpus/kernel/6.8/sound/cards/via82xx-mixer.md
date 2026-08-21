---
collection: kernel
version: "6.8"
title: "VIA82xx mixer"
source_url: https://www.kernel.org/doc/html/v6.8/sound/cards/via82xx-mixer.html
fetched_at: 2026-08-21T03:47:54+00:00
---
# VIA82xx mixer

On many VIA82xx boards, the `Input Source Select` mixer control does not work.
Setting it to `Input2` on such boards will cause recording to hang, or fail
with EIO (input/output error) via OSS emulation. This control should be left
at `Input1` for such cards.
