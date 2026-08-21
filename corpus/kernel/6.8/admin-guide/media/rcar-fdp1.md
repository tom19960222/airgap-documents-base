---
collection: kernel
version: "6.8"
title: "7.16. Renesas R-Car Fine Display Processor (FDP1) Driver"
source_url: https://www.kernel.org/doc/html/v6.8/admin-guide/media/rcar-fdp1.html
fetched_at: 2026-08-21T03:55:59+00:00
---
# 7.16. Renesas R-Car Fine Display Processor (FDP1) Driver

The R-Car FDP1 driver implements driver-specific controls as follows.

`V4L2_CID_DEINTERLACING_MODE (menu)`
:   The video deinterlacing mode (such as Bob, Weave, ...). The R-Car FDP1
    driver implements the following modes.

|  |  |
| --- | --- |
| `"Progressive" (0)` | The input image video stream is progressive (not interlaced). No deinterlacing is performed. Apart from (optional) format and encoding conversion output frames are identical to the input frames. |
| `"Adaptive 2D/3D" (1)` | Motion adaptive version of 2D and 3D deinterlacing. Use 3D deinterlacing in the presence of fast motion and 2D deinterlacing with diagonal interpolation otherwise. |
| `"Fixed 2D" (2)` | The current field is scaled vertically by averaging adjacent lines to recover missing lines. This method is also known as blending or Line Averaging (LAV). |
| `"Fixed 3D" (3)` | The previous and next fields are averaged to recover lines missing from the current field. This method is also known as Field Averaging (FAV). |
| `"Previous field" (4)` | The current field is weaved with the previous field, i.e. the previous field is used to fill missing lines from the current field. This method is also known as weave deinterlacing. |
| `"Next field" (5)` | The current field is weaved with the next field, i.e. the next field is used to fill missing lines from the current field. This method is also known as weave deinterlacing. |
