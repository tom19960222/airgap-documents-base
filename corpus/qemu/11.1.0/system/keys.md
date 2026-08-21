---
collection: qemu
version: "11.1.0"
title: "Keys in the graphical frontends"
source_url: https://www.qemu.org/docs/master/system/keys.html
fetched_at: 2026-08-21T03:21:26+00:00
---
# Keys in the graphical frontends

During the graphical emulation, you can use special key combinations from
the following table to change modes. By default the modifier is `Ctrl+Alt`
(used in the table below) which can be changed with `-display` suboption
`mod=` where appropriate. For example, `-display sdl,
grab-mod=lshift-lctrl-lalt` changes the modifier key to `Ctrl+Alt+Shift`,
while `-display sdl,grab-mod=rctrl` changes it to the right `Ctrl` key.

Multiplexer Keys

| Key Sequence | Action |
| --- | --- |
| `Ctrl+Alt+f` | Toggle full screen |
| `Ctrl+Alt++` | Enlarge the screen |
| `Ctrl+Alt+-` | Shrink the screen |
| `Ctrl+Alt+0` | Restore the screen’s un-scaled dimensions |
| `Ctrl+Alt+n` | Switch to virtual console ‘n’. Standard console mappings are:   - *1*: Target system display - *2*: Monitor - *3*: Serial port |
| `Ctrl+Alt+g` | Toggle mouse and keyboard grab. |

In the virtual consoles, you can use `Ctrl+Up`, `Ctrl+Down`, `Ctrl+PageUp` and
`Ctrl+PageDown` to move in the back log.
