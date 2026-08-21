---
collection: kernel
version: "6.8"
title: "ABI stable symbols"
source_url: https://www.kernel.org/doc/html/v6.8/admin-guide/abi-stable.html
fetched_at: 2026-08-21T03:54:37+00:00
---
# ABI stable symbols

Documents the interfaces that the developer has defined to be stable.

Userspace programs are free to use these interfaces with no
restrictions, and backward compatibility for them will be guaranteed
for at least 2 years.

Most interfaces (like syscalls) are expected to never change and always
be available.

## Symbols under /dev/fw

|  |
| --- |
| **/dev/fw[0-9]+** |

Defined on file [firewire-cdev](abi-stable.md#abi-file-stable-firewire-cdev)

The character device files /dev/fw\* are the interface between
firewire-core and IEEE 1394 device drivers implemented in
userspace. The ioctl(2)- and read(2)-based ABI is defined and
documented in <linux/firewire-cdev.h>.

This ABI offers most of the features which firewire-core also
exposes to kernelspace IEEE 1394 drivers.

Each /dev/fw\* is associated with one IEEE 1394 node, which can
be remote or local nodes. Operations on a /dev/fw\* file have
different scope:

> - The 1394 node which is associated with the file:
>
>   > - Asynchronous request transmission
>   > - Get the Configuration ROM
>   > - Query node ID
>   > - Query maximum speed of the path between this node
>   >   and local node
> - The 1394 bus (i.e. "card") to which the node is attached to:
>
>   > - Isochronous stream transmission and reception
>   > - Asynchronous stream transmission and reception
>   > - Asynchronous broadcast request transmission
>   > - PHY packet transmission and reception
>   > - Allocate, reallocate, deallocate isochronous
>   >   resources (channels, bandwidth) at the bus's IRM
>   > - Query node IDs of local node, root node, IRM, bus
>   >   manager
>   > - Query cycle time
>   > - Bus reset initiation, bus reset event reception
> - All 1394 buses:
>
>   > - Allocation of IEEE 1212 address ranges on the local
>   >   link layers, reception of inbound requests to such
>   >   an address range, asynchronous response transmission
>   >   to inbound requests
>   > - Addition of descriptors or directories to the local
>   >   nodes' Configuration ROM

Due to the different scope of operations and in order to let
userland implement different access permission models, some
operations are restricted to /dev/fw\* files that are associated
with a local node:

> - Addition of descriptors or directories to the local
>   nodes' Configuration ROM
> - PHY packet transmission and reception

A /dev/fw\* file remains associated with one particular node
during its entire life time. Bus topology changes, and hence
node ID changes, are tracked by firewire-core. ABI users do not
need to be aware of topology.

The following file operations are supported:

open(2)
:   Currently the only useful flags are O_RDWR.

ioctl(2)
:   Initiate various actions. Some take immediate effect, others
    are performed asynchronously while or after the ioctl returns.
    See the inline documentation in <linux/firewire-cdev.h> for
    descriptions of all ioctls.

poll(2), select(2), epoll_wait(2) etc.
:   Watch for events to become available to be read.

read(2)
:   Receive various events. There are solicited events like
    outbound asynchronous transaction completion or isochronous
    buffer completion, and unsolicited events such as bus resets,
    request reception, or PHY packet reception. Always use a read
    buffer which is large enough to receive the largest event that
    could ever arrive. See <linux/firewire-cdev.h> for descriptions
    of all event types and for which ioctls affect reception of
    events.

mmap(2)
:   Allocate a DMA buffer for isochronous reception or transmission
    and map it into the process address space. The arguments should
    be used as follows: addr = NULL, length = the desired buffer
    size, i.e. number of packets times size of largest packet,
    prot = at least PROT_READ for reception and at least PROT_WRITE
    for transmission, flags = MAP_SHARED, fd = the handle to the
    /dev/fw\*, offset = 0.

Isochronous reception works in packet-per-buffer fashion except
for multichannel reception which works in buffer-fill mode.

munmap(2)
:   Unmap the isochronous I/O buffer from the process address space.

close(2)
:   Besides stopping and freeing I/O contexts that were associated
    with the file descriptor, back out any changes to the local
    nodes' Configuration ROM. Deallocate isochronous channels and
    bandwidth at the IRM that were marked for kernel-assisted
    re- and deallocation.

Users:
libraw1394;
libdc1394;
libhinawa;
tools like linux-firewire-utils, fwhack, ...

## Symbols under /sys/accessibility

|  |
| --- |
| **/sys/accessibility/speakup/<synth-name>/** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

In /sys/accessibility/speakup is a directory corresponding to
the synthesizer driver currently in use (E.G) soft for the
soft driver. This directory contains files which control the
speech synthesizer itself,
as opposed to controlling the speakup
screen reader. The parameters in this directory have the same
names and functions across all
supported synthesizers. The range
of values for freq, pitch, rate, and vol is the same for all
supported synthesizers, with the given range being internally
mapped by the driver to more or less fit the range of values
supported for a given parameter by the individual synthesizer.
Below is a description of values and parameters for soft
synthesizer, which is currently the most commonly used.

|  |
| --- |
| **/sys/accessibility/speakup/<synth-name>/caps_start** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

This is the string that is sent to the synthesizer to cause it
to start speaking uppercase letters. For the soft synthesizer
and most others, this causes the pitch of the voice to rise
above the currently set pitch.

|  |
| --- |
| **/sys/accessibility/speakup/<synth-name>/caps_stop** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

This is the string sent to the synthesizer to cause it to stop
speaking uppercase letters. In the case of the soft synthesizer
and most others, this returns the pitch of the voice
down to the
currently set pitch.

|  |
| --- |
| **/sys/accessibility/speakup/<synth-name>/delay_time** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

TODO:

|  |
| --- |
| **/sys/accessibility/speakup/<synth-name>/direct** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

Controls if punctuation is spoken by speakup, or by the
synthesizer.

For example, speakup speaks ">" as "greater", while
the espeak synthesizer used by the soft driver speaks "greater
than". Zero lets speakup speak the punctuation. One lets the
synthesizer itself speak punctuation.

|  |
| --- |
| **/sys/accessibility/speakup/<synth-name>/flush_time** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

Gets or sets the timeout to wait for the synthesizer flush to
complete. This can be used when the cable gets faulty and flush
notifications are getting lost.

|  |
| --- |
| **/sys/accessibility/speakup/<synth-name>/freq** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

Gets or sets the frequency of the speech synthesizer. Range is
0-9.

|  |
| --- |
| **/sys/accessibility/speakup/<synth-name>/full_time** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

TODO:

|  |
| --- |
| **/sys/accessibility/speakup/<synth-name>/inflection** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

Gets or sets the inflection of the synthesizer, i.e. the pitch
range. The range is 0-9.

|  |
| --- |
| **/sys/accessibility/speakup/<synth-name>/jiffy_delta** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

This controls how many jiffys the kernel gives to the
synthesizer. Setting this too high can make a system unstable,
or even crash it.

|  |
| --- |
| **/sys/accessibility/speakup/<synth-name>/pitch** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

Gets or sets the pitch of the synthesizer. The range is 0-9.

|  |
| --- |
| **/sys/accessibility/speakup/<synth-name>/punct** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

Gets or sets the amount of punctuation spoken by the
synthesizer. The range for the soft driver seems to be 0-2.
TODO: How is this related to speakup's punc_level, or
reading_punc.

|  |
| --- |
| **/sys/accessibility/speakup/<synth-name>/rate** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

Gets or sets the rate of the synthesizer. Range is from zero
slowest, to nine fastest.

|  |
| --- |
| **/sys/accessibility/speakup/<synth-name>/tone** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

Gets or sets the tone of the speech synthesizer. The range for
the soft driver seems to be 0-2. This seems to make no
difference if using espeak and the espeakup connector.
TODO: does espeakup support different tonalities?

|  |
| --- |
| **/sys/accessibility/speakup/<synth-name>/trigger_time** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

TODO:

|  |
| --- |
| **/sys/accessibility/speakup/<synth-name>/voice** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

Gets or sets the voice used by the synthesizer if the
synthesizer can speak in more than one voice. The range for the
soft driver is 0-7. Note that while espeak supports multiple
voices, this parameter will not set the voice when the espeakup
connector is used between speakup and espeak.

|  |
| --- |
| **/sys/accessibility/speakup/<synth-name>/vol** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

Gets or sets the volume of the speech synthesizer. Range is 0-9,
with zero being the softest, and nine being the loudest.

|  |
| --- |
| **/sys/accessibility/speakup/attrib_bleep** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

Beeps the PC speaker when there is an attribute change such as
foreground or background color when using speakup review
commands. One = on, zero = off.

|  |
| --- |
| **/sys/accessibility/speakup/bell_pos** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

This works much like a typewriter bell. If for example 72 is
echoed to bell_pos, it will beep the PC speaker when typing on
a line past character 72.

|  |
| --- |
| **/sys/accessibility/speakup/bleep_time** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

This controls the duration of the PC speaker beeps speakup
produces.
TODO: What are the units? Jiffies?

|  |
| --- |
| **/sys/accessibility/speakup/bleeps** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

This controls whether one hears beeps through the PC speaker
when using speakup's review commands.
TODO: what values does it accept?

|  |
| --- |
| **/sys/accessibility/speakup/cur_phonetic** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

This allows speakup to speak letters phoneticaly when arrowing through
a word letter by letter. This doesn't affect the spelling when typing
the characters. When cur_phonetic=1, speakup will speak characters
phoneticaly when arrowing over a letter. When cur_phonetic=0, speakup
will speak letters as normally.

|  |
| --- |
| **/sys/accessibility/speakup/cursor_time** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

This controls cursor delay when using arrow keys. When a
connection is very slow, with the default setting, when moving
with the arrows, or backspacing etc. speakup says the incorrect
characters. Set this to a higher value to adjust for the delay
and better synchronisation between cursor position and speech.

|  |
| --- |
| **/sys/accessibility/speakup/delimiters** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

Delimit a word from speakup.
TODO: add more info

|  |
| --- |
| **/sys/accessibility/speakup/ex_num** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

TODO:

|  |
| --- |
| **/sys/accessibility/speakup/i18n/announcements** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

This file contains various general announcements, most of which
cannot be categorized. You will find messages such as "You
killed Speakup", "I'm alive", "leaving help", "parked",
"unparked", and others. You will also find the names of the
screen edges and cursor tracking modes here.

|  |
| --- |
| **/sys/accessibility/speakup/i18n/characters** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

Through this sys entry, Speakup gives you the ability to change
how Speakup pronounces a given character. You could, for
example, change how some punctuation characters are spoken. You
can even change how Speakup will pronounce certain letters. For
further details see '12. Changing the Pronunciation of
Characters' in Speakup User's Guide (file spkguide.txt in
source).

|  |
| --- |
| **/sys/accessibility/speakup/i18n/chartab** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

TODO

|  |
| --- |
| **/sys/accessibility/speakup/i18n/colors** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

When you use the "say attributes" function, Speakup says the
name of the foreground and background colors. These names come
from the i18n/colors file.

|  |
| --- |
| **/sys/accessibility/speakup/i18n/ctl_keys** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

Here, you will find names of control keys. These are used with
Speakup's say_control feature.

|  |
| --- |
| **/sys/accessibility/speakup/i18n/formatted** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

This group of messages contains embedded formatting codes, to
specify the type and width of displayed data. If you change
these, you must preserve all of the formatting codes, and they
must appear in the order used by the default messages.

|  |
| --- |
| **/sys/accessibility/speakup/i18n/function_names** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

Here, you will find a list of names for Speakup functions.
These are used by the help system. For example, suppose that
you have activated help mode, and you pressed
keypad 3. Speakup
says: "keypad 3 is character, say next."
The message "character, say next" names a Speakup function, and
it comes from this function_names file.

|  |
| --- |
| **/sys/accessibility/speakup/i18n/key_names** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

Again, key_names is used by Speakup's help system. In the
previous example, Speakup said that you pressed "keypad 3."
This name came from the key_names file.

|  |
| --- |
| **/sys/accessibility/speakup/i18n/states** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

This file contains names for key states.
Again, these are part of the help system. For instance, if you
had pressed speakup + keypad 3, you would hear:
"speakup keypad 3 is go to bottom edge."

The speakup key is depressed, so the name of the key state is
speakup.

This part of the message comes from the states collection.

|  |
| --- |
| **/sys/accessibility/speakup/key_echo** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

Controls if speakup speaks keys when they are typed. One = on,
zero = off or don't echo keys.

|  |
| --- |
| **/sys/accessibility/speakup/keymap** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

Speakup keymap remaps keys to Speakup functions.
It uses a binary
format. A special program called genmap is needed to compile a
textual keymap into the binary format which is then loaded into
[/sys/accessibility/speakup/keymap](abi-stable.md#abi-sys-accessibility-speakup-keymap).

|  |
| --- |
| **/sys/accessibility/speakup/no_interrupt** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

Controls if typing interrupts output from speakup. With
no_interrupt set to zero, typing on the keyboard will interrupt
speakup if for example
the say screen command is used before the
entire screen is read.

With no_interrupt set to one, if the say
screen command is used, and one then types on the keyboard,
speakup will continue to say the whole screen regardless until
it finishes.

|  |
| --- |
| **/sys/accessibility/speakup/punc_all** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

This is a list of all the punctuation speakup should speak when
punc_level is set to four.

|  |
| --- |
| **/sys/accessibility/speakup/punc_level** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

Controls the level of punctuation spoken as the screen is
displayed, not reviewed. Levels range from zero no punctuation,
to four, all punctuation. One corresponds to punc_some, two
corresponds to punc_most, and three as well as four both
correspond to punc_all. Some hardware synthesizers may have
different levels each corresponding to three and four for
punc_level. Also note that if punc_level is set to zero, and
key_echo is set to one, typed punctuation is still spoken as it
is typed.

|  |
| --- |
| **/sys/accessibility/speakup/punc_most** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

This is a list of all the punctuation speakup should speak when
punc_level is set to two.

|  |
| --- |
| **/sys/accessibility/speakup/punc_some** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

This is a list of all the punctuation speakup should speak when
punc_level is set to one.

|  |
| --- |
| **/sys/accessibility/speakup/reading_punc** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

Almost the same as punc_level, the differences being that
reading_punc controls the level of punctuation when reviewing
the screen with speakup's screen review commands. The other
difference is that reading_punc set to three speaks punc_all,
and reading_punc set to four speaks all punctuation, including
spaces.

|  |
| --- |
| **/sys/accessibility/speakup/repeats** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

A list of characters speakup repeats. Normally, when there are
more than three characters in a row, speakup
just reads three of
those characters. For example, "......" would be read as dot,
dot, dot. If a . is added to the list of characters in repeats,
"......" would be read as dot, dot, dot, times six.

|  |
| --- |
| **/sys/accessibility/speakup/say_control** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

If set to one, speakup speaks shift, alt and control when those
keys are pressed. If say_control is set to zero, shift, ctrl,
and alt are not spoken when they are pressed.

|  |
| --- |
| **/sys/accessibility/speakup/say_word_ctl** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

TODO:

|  |
| --- |
| **/sys/accessibility/speakup/silent** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

TODO:

|  |
| --- |
| **/sys/accessibility/speakup/spell_delay** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

This controls how fast a word is spelled
when speakup's say word
review command is pressed twice quickly to speak the current
word being reviewed. Zero just speaks the letters one after
another, while values one through four
seem to introduce more of
a pause between the spelling of each letter by speakup.

|  |
| --- |
| **/sys/accessibility/speakup/synth** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

Gets or sets the synthesizer driver currently in use. Reading
synth returns the synthesizer driver currently in use. Writing
synth switches to the given synthesizer driver, provided it is
either built into the kernel, or already loaded as a module.

|  |
| --- |
| **/sys/accessibility/speakup/synth_direct** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

Sends whatever is written to synth_direct
directly to the speech synthesizer in use, bypassing speakup.
This could be used to make the synthesizer speak
a string, or to
send control sequences to the synthesizer to change how the
synthesizer behaves.

|  |
| --- |
| **/sys/accessibility/speakup/version** |

Defined on file [sysfs-driver-speakup](abi-stable.md#abi-file-stable-sysfs-driver-speakup)

Reading version returns the version of speakup, and the version
of the synthesizer driver currently in use.

## Symbols under /sys/block

|  |
| --- |
| **/sys/block/<disk>/<partition>/alignment_offset** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

Storage devices may report a physical block size that is
bigger than the logical block size (for instance a drive
with 4KB physical sectors exposing 512-byte logical
blocks to the operating system). This parameter
indicates how many bytes the beginning of the partition
is offset from the disk's natural alignment.

|  |
| --- |
| **/sys/block/<disk>/<partition>/discard_alignment** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

Devices that support discard functionality may
internally allocate space in units that are bigger than
the exported logical block size. The discard_alignment
parameter indicates how many bytes the beginning of the
partition is offset from the internal allocation unit's
natural alignment.

|  |
| --- |
| **/sys/block/<disk>/<partition>/stat** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

The [/sys/block/<disk>/<partition>/stat](abi-stable.md#abi-sys-block-disk-partition-stat) files display the
I/O statistics of partition <partition>. The format is the
same as the format of [/sys/block/<disk>/stat](abi-stable.md#abi-sys-block-disk-stat).

|  |
| --- |
| **/sys/block/<disk>/alignment_offset** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

Storage devices may report a physical block size that is
bigger than the logical block size (for instance a drive
with 4KB physical sectors exposing 512-byte logical
blocks to the operating system). This parameter
indicates how many bytes the beginning of the device is
offset from the disk's natural alignment.

|  |
| --- |
| **/sys/block/<disk>/discard_alignment** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

Devices that support discard functionality may
internally allocate space in units that are bigger than
the exported logical block size. The discard_alignment
parameter indicates how many bytes the beginning of the
device is offset from the internal allocation unit's
natural alignment.

|  |
| --- |
| **/sys/block/<disk>/diskseq** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

The [/sys/block/<disk>/diskseq](abi-stable.md#abi-sys-block-disk-diskseq) files reports the disk
sequence number, which is a monotonically increasing
number assigned to every drive.
Some devices, like the loop device, refresh such number
every time the backing file is changed.
The value type is 64 bit unsigned.

|  |
| --- |
| **/sys/block/<disk>/hidden** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RO] the block device is hidden. it doesn’t produce events, and
can’t be opened from userspace or using blkdev_get\*.
Used for the underlying components of multipath devices.

|  |
| --- |
| **/sys/block/<disk>/inflight** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

Reports the number of I/O requests currently in progress
(pending / in flight) in a device driver. This can be less
than the number of requests queued in the block device queue.
The report contains 2 fields: one for read requests
and one for write requests.
The value type is unsigned int.
Cf. [Block layer statistics in /sys/block/<dev>/stat](../block/stat.md) which contains a single value for
requests in flight.
This is related to [/sys/block/<disk>/queue/nr_requests](abi-stable.md#abi-sys-block-disk-queue-nr-requests)
and for SCSI device also its queue_depth.

|  |
| --- |
| **/sys/block/<disk>/integrity/device_is_integrity_capable** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

Indicates whether a storage device is capable of storing
integrity metadata. Set if the device is T10 PI-capable.

|  |
| --- |
| **/sys/block/<disk>/integrity/format** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

Metadata format for integrity capable block device.
E.g. T10-DIF-TYPE1-CRC.

|  |
| --- |
| **/sys/block/<disk>/integrity/protection_interval_bytes** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

Describes the number of data bytes which are protected
by one integrity tuple. Typically the device's logical
block size.

|  |
| --- |
| **/sys/block/<disk>/integrity/read_verify** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

Indicates whether the block layer should verify the
integrity of read requests serviced by devices that
support sending integrity metadata.

|  |
| --- |
| **/sys/block/<disk>/integrity/tag_size** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

Number of bytes of integrity tag space available per
512 bytes of data.

|  |
| --- |
| **/sys/block/<disk>/integrity/write_generate** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

Indicates whether the block layer should automatically
generate checksums for write requests bound for
devices that support receiving integrity metadata.

|  |
| --- |
| **/sys/block/<disk>/queue/add_random** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RW] This file allows to turn off the disk entropy contribution.
Default value of this file is '1'(on).

|  |
| --- |
| **/sys/block/<disk>/queue/chunk_sectors** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RO] chunk_sectors has different meaning depending on the type
of the disk. For a RAID device (dm-raid), chunk_sectors
indicates the size in 512B sectors of the RAID volume stripe
segment. For a zoned block device, either host-aware or
host-managed, chunk_sectors indicates the size in 512B sectors
of the zones of the device, with the eventual exception of the
last zone of the device which may be smaller.

|  |
| --- |
| **/sys/block/<disk>/queue/crypto/** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

The presence of this subdirectory of /sys/block/<disk>/queue/
indicates that the device supports inline encryption. This
subdirectory contains files which describe the inline encryption
capabilities of the device. For more information about inline
encryption, refer to [Inline Encryption](../block/inline-encryption.md).

|  |
| --- |
| **/sys/block/<disk>/queue/crypto/max_dun_bits** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RO] This file shows the maximum length, in bits, of data unit
numbers accepted by the device in inline encryption requests.

|  |
| --- |
| **/sys/block/<disk>/queue/crypto/modes/<mode>** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RO] For each crypto mode (i.e., encryption/decryption
algorithm) the device supports with inline encryption, a file
will exist at this location. It will contain a hexadecimal
number that is a bitmask of the supported data unit sizes, in
bytes, for that crypto mode.

Currently, the crypto modes that may be supported are:

> - AES-256-XTS
> - AES-128-CBC-ESSIV
> - Adiantum

For example, if a device supports AES-256-XTS inline encryption
with data unit sizes of 512 and 4096 bytes, the file
/sys/block/<disk>/queue/crypto/modes/AES-256-XTS will exist and
will contain "0x1200".

|  |
| --- |
| **/sys/block/<disk>/queue/crypto/num_keyslots** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RO] This file shows the number of keyslots the device has for
use with inline encryption.

|  |
| --- |
| **/sys/block/<disk>/queue/dax** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RO] This file indicates whether the device supports Direct
Access (DAX), used by CPU-addressable storage to bypass the
pagecache. It shows '1' if true, '0' if not.

|  |
| --- |
| **/sys/block/<disk>/queue/discard_granularity** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RO] Devices that support discard functionality may internally
allocate space using units that are bigger than the logical
block size. The discard_granularity parameter indicates the size
of the internal allocation unit in bytes if reported by the
device. Otherwise the discard_granularity will be set to match
the device's physical block size. A discard_granularity of 0
means that the device does not support discard functionality.

|  |
| --- |
| **/sys/block/<disk>/queue/discard_max_bytes** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RW] While discard_max_hw_bytes is the hardware limit for the
device, this setting is the software limit. Some devices exhibit
large latencies when large discards are issued, setting this
value lower will make Linux issue smaller discards and
potentially help reduce latencies induced by large discard
operations.

|  |
| --- |
| **/sys/block/<disk>/queue/discard_max_hw_bytes** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RO] Devices that support discard functionality may have
internal limits on the number of bytes that can be trimmed or
unmapped in a single operation. The discard_max_hw_bytes
parameter is set by the device driver to the maximum number of
bytes that can be discarded in a single operation. Discard
requests issued to the device must not exceed this limit. A
discard_max_hw_bytes value of 0 means that the device does not
support discard functionality.

|  |
| --- |
| **/sys/block/<disk>/queue/discard_zeroes_data** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RO] Will always return 0. Don't rely on any specific behavior
for discards, and don't read this file.

|  |
| --- |
| **/sys/block/<disk>/queue/dma_alignment** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

Reports the alignment that user space addresses must have to be
used for raw block device access with O_DIRECT and other driver
specific passthrough mechanisms.

|  |
| --- |
| **/sys/block/<disk>/queue/fua** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RO] Whether or not the block driver supports the FUA flag for
write requests. FUA stands for Force Unit Access. If the FUA
flag is set that means that write requests must bypass the
volatile cache of the storage device.

|  |
| --- |
| **/sys/block/<disk>/queue/hw_sector_size** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RO] This is the hardware sector size of the device, in bytes.

|  |
| --- |
| **/sys/block/<disk>/queue/independent_access_ranges/** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RO] The presence of this sub-directory of the
/sys/block/xxx/queue/ directory indicates that the device is
capable of executing requests targeting different sector ranges
in parallel. For instance, single LUN multi-actuator hard-disks
will have an independent_access_ranges directory if the device
correctly advertises the sector ranges of its actuators.

The independent_access_ranges directory contains one directory
per access range, with each range described using the sector
(RO) attribute file to indicate the first sector of the range
and the nr_sectors (RO) attribute file to indicate the total
number of sectors in the range starting from the first sector of
the range. For example, a dual-actuator hard-disk will have the
following independent_access_ranges entries.:

```
$ tree /sys/block/<disk>/queue/independent_access_ranges/
/sys/block/<disk>/queue/independent_access_ranges/
|-- 0
|   |-- nr_sectors
|   `-- sector
`-- 1
    |-- nr_sectors
    `-- sector
```

The sector and nr_sectors attributes use 512B sector unit,
regardless of the actual block size of the device. Independent
access ranges do not overlap and include all sectors within the
device capacity. The access ranges are numbered in increasing
order of the range start sector, that is, the sector attribute
of range 0 always has the value 0.

|  |
| --- |
| **/sys/block/<disk>/queue/io_poll** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RW] When read, this file shows whether polling is enabled (1)
or disabled (0). Writing '0' to this file will disable polling
for this device. Writing any non-zero value will enable this
feature.

|  |
| --- |
| **/sys/block/<disk>/queue/io_poll_delay** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RW] This was used to control what kind of polling will be
performed. It is now fixed to -1, which is classic polling.
In this mode, the CPU will repeatedly ask for completions
without giving up any time.
<deprecated>

|  |
| --- |
| **/sys/block/<disk>/queue/io_timeout** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RW] io_timeout is the request timeout in milliseconds. If a
request does not complete in this time then the block driver
timeout handler is invoked. That timeout handler can decide to
retry the request, to fail it or to start a device recovery
strategy.

|  |
| --- |
| **/sys/block/<disk>/queue/iostats** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RW] This file is used to control (on/off) the iostats
accounting of the disk.

|  |
| --- |
| **/sys/block/<disk>/queue/logical_block_size** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RO] This is the smallest unit the storage device can address.
It is typically 512 bytes.

|  |
| --- |
| **/sys/block/<disk>/queue/max_active_zones** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RO] For zoned block devices (zoned attribute indicating
"host-managed" or "host-aware"), the sum of zones belonging to
any of the zone states: EXPLICIT OPEN, IMPLICIT OPEN or CLOSED,
is limited by this value. If this value is 0, there is no limit.

If the host attempts to exceed this limit, the driver should
report this error with BLK_STS_ZONE_ACTIVE_RESOURCE, which user
space may see as the EOVERFLOW errno.

|  |
| --- |
| **/sys/block/<disk>/queue/max_discard_segments** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RO] The maximum number of DMA scatter/gather entries in a
discard request.

|  |
| --- |
| **/sys/block/<disk>/queue/max_hw_sectors_kb** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RO] This is the maximum number of kilobytes supported in a
single data transfer.

|  |
| --- |
| **/sys/block/<disk>/queue/max_integrity_segments** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RO] Maximum number of elements in a DMA scatter/gather list
with integrity data that will be submitted by the block layer
core to the associated block driver.

|  |
| --- |
| **/sys/block/<disk>/queue/max_open_zones** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RO] For zoned block devices (zoned attribute indicating
"host-managed" or "host-aware"), the sum of zones belonging to
any of the zone states: EXPLICIT OPEN or IMPLICIT OPEN, is
limited by this value. If this value is 0, there is no limit.

|  |
| --- |
| **/sys/block/<disk>/queue/max_sectors_kb** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RW] This is the maximum number of kilobytes that the block
layer will allow for a filesystem request. Must be smaller than
or equal to the maximum size allowed by the hardware. Write 0
to use default kernel settings.

|  |
| --- |
| **/sys/block/<disk>/queue/max_segment_size** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RO] Maximum size in bytes of a single element in a DMA
scatter/gather list.

|  |
| --- |
| **/sys/block/<disk>/queue/max_segments** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RO] Maximum number of elements in a DMA scatter/gather list
that is submitted to the associated block driver.

|  |
| --- |
| **/sys/block/<disk>/queue/minimum_io_size** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RO] Storage devices may report a granularity or preferred
minimum I/O size which is the smallest request the device can
perform without incurring a performance penalty. For disk
drives this is often the physical block size. For RAID arrays
it is often the stripe chunk size. A properly aligned multiple
of minimum_io_size is the preferred request size for workloads
where a high number of I/O operations is desired.

|  |
| --- |
| **/sys/block/<disk>/queue/nomerges** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RW] Standard I/O elevator operations include attempts to merge
contiguous I/Os. For known random I/O loads these attempts will
always fail and result in extra cycles being spent in the
kernel. This allows one to turn off this behavior on one of two
ways: When set to 1, complex merge checks are disabled, but the
simple one-shot merges with the previous I/O request are
enabled. When set to 2, all merge tries are disabled. The
default value is 0 - which enables all types of merge tries.

|  |
| --- |
| **/sys/block/<disk>/queue/nr_requests** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RW] This controls how many requests may be allocated in the
block layer for read or write requests. Note that the total
allocated number may be twice this amount, since it applies only
to reads or writes (not the accumulated sum).

To avoid priority inversion through request starvation, a
request queue maintains a separate request pool per each cgroup
when CONFIG_BLK_CGROUP is enabled, and this parameter applies to
each such per-block-cgroup request pool. IOW, if there are N
block cgroups, each request queue may have up to N request
pools, each independently regulated by nr_requests.

|  |
| --- |
| **/sys/block/<disk>/queue/nr_zones** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RO] nr_zones indicates the total number of zones of a zoned
block device ("host-aware" or "host-managed" zone model). For
regular block devices, the value is always 0.

|  |
| --- |
| **/sys/block/<disk>/queue/optimal_io_size** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RO] Storage devices may report an optimal I/O size, which is
the device's preferred unit for sustained I/O. This is rarely
reported for disk drives. For RAID arrays it is usually the
stripe width or the internal track size. A properly aligned
multiple of optimal_io_size is the preferred request size for
workloads where sustained throughput is desired. If no optimal
I/O size is reported this file contains 0.

|  |
| --- |
| **/sys/block/<disk>/queue/physical_block_size** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RO] This is the smallest unit a physical storage device can
write atomically. It is usually the same as the logical block
size but may be bigger. One example is SATA drives with 4KB
sectors that expose a 512-byte logical block size to the
operating system. For stacked block devices the
physical_block_size variable contains the maximum
physical_block_size of the component devices.

|  |
| --- |
| **/sys/block/<disk>/queue/read_ahead_kb** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RW] Maximum number of kilobytes to read-ahead for filesystems
on this block device.

|  |
| --- |
| **/sys/block/<disk>/queue/rotational** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RW] This file is used to stat if the device is of rotational
type or non-rotational type.

|  |
| --- |
| **/sys/block/<disk>/queue/rq_affinity** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RW] If this option is '1', the block layer will migrate request
completions to the cpu "group" that originally submitted the
request. For some workloads this provides a significant
reduction in CPU cycles due to caching effects.

For storage configurations that need to maximize distribution of
completion processing setting this option to '2' forces the
completion to run on the requesting cpu (bypassing the "group"
aggregation logic).

|  |
| --- |
| **/sys/block/<disk>/queue/scheduler** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RW] When read, this file will display the current and available
IO schedulers for this block device. The currently active IO
scheduler will be enclosed in [] brackets. Writing an IO
scheduler name to this file will switch control of this block
device to that new IO scheduler. Note that writing an IO
scheduler name to this file will attempt to load that IO
scheduler module, if it isn't already present in the system.

|  |
| --- |
| **/sys/block/<disk>/queue/stable_writes** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RW] This file will contain '1' if memory must not be modified
while it is being used in a write request to this device. When
this is the case and the kernel is performing writeback of a
page, the kernel will wait for writeback to complete before
allowing the page to be modified again, rather than allowing
immediate modification as is normally the case. This
restriction arises when the device accesses the memory multiple
times where the same data must be seen every time -- for
example, once to calculate a checksum and once to actually write
the data. If no such restriction exists, this file will contain
'0'. This file is writable for testing purposes.

|  |
| --- |
| **/sys/block/<disk>/queue/throttle_sample_time** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RW] This is the time window that blk-throttle samples data, in
millisecond. blk-throttle makes decision based on the
samplings. Lower time means cgroups have more smooth throughput,
but higher CPU overhead. This exists only when
CONFIG_BLK_DEV_THROTTLING_LOW is enabled.

|  |
| --- |
| **/sys/block/<disk>/queue/virt_boundary_mask** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RO] This file shows the I/O segment memory alignment mask for
the block device. I/O requests to this device will be split
between segments wherever either the memory address of the end
of the previous segment or the memory address of the beginning
of the current segment is not aligned to virt_boundary_mask + 1
bytes.

|  |
| --- |
| **/sys/block/<disk>/queue/wbt_lat_usec** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RW] If the device is registered for writeback throttling, then
this file shows the target minimum read latency. If this latency
is exceeded in a given window of time (see wb_window_usec), then
the writeback throttling will start scaling back writes. Writing
a value of '0' to this file disables the feature. Writing a
value of '-1' to this file resets the value to the default
setting.

|  |
| --- |
| **/sys/block/<disk>/queue/write_cache** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RW] When read, this file will display whether the device has
write back caching enabled or not. It will return "write back"
for the former case, and "write through" for the latter. Writing
to this file can change the kernels view of the device, but it
doesn't alter the device state. This means that it might not be
safe to toggle the setting from "write back" to "write through",
since that will also eliminate cache flushes issued by the
kernel.

|  |
| --- |
| **/sys/block/<disk>/queue/write_same_max_bytes** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RO] Some devices support a write same operation in which a
single data block can be written to a range of several
contiguous blocks on storage. This can be used to wipe areas on
disk or to initialize drives in a RAID configuration.
write_same_max_bytes indicates how many bytes can be written in
a single write same command. If write_same_max_bytes is 0, write
same is not supported by the device.

|  |
| --- |
| **/sys/block/<disk>/queue/write_zeroes_max_bytes** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RO] Devices that support write zeroes operation in which a
single request can be issued to zero out the range of contiguous
blocks on storage without having any payload in the request.
This can be used to optimize writing zeroes to the devices.
write_zeroes_max_bytes indicates how many bytes can be written
in a single write zeroes command. If write_zeroes_max_bytes is
0, write zeroes is not supported by the device.

|  |
| --- |
| **/sys/block/<disk>/queue/zone_append_max_bytes** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RO] This is the maximum number of bytes that can be written to
a sequential zone of a zoned block device using a zone append
write operation (REQ_OP_ZONE_APPEND). This value is always 0 for
regular block devices.

|  |
| --- |
| **/sys/block/<disk>/queue/zone_write_granularity** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RO] This indicates the alignment constraint, in bytes, for
write operations in sequential zones of zoned block devices
(devices with a zoned attributed that reports "host-managed" or
"host-aware"). This value is always 0 for regular block devices.

|  |
| --- |
| **/sys/block/<disk>/queue/zoned** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

[RO] zoned indicates if the device is a zoned block device and
the zone model of the device if it is indeed zoned. The
possible values indicated by zoned are "none" for regular block
devices and "host-aware" or "host-managed" for zoned block
devices. The characteristics of host-aware and host-managed
zoned block devices are described in the ZBC (Zoned Block
Commands) and ZAC (Zoned Device ATA Command Set) standards.
These standards also define the "drive-managed" zone model.
However, since drive-managed zoned block devices do not support
zone commands, they will be treated as regular block devices and
zoned will report "none".

|  |
| --- |
| **/sys/block/<disk>/stat** |

Defined on file [sysfs-block](abi-stable.md#abi-file-stable-sysfs-block)

The [/sys/block/<disk>/stat](abi-stable.md#abi-sys-block-disk-stat) files displays the I/O
statistics of disk <disk>. They contain 11 fields:

|  |  |
| --- | --- |
| 1 | reads completed successfully |
| 2 | reads merged |
| 3 | sectors read |
| 4 | time spent reading (ms) |
| 5 | writes completed |
| 6 | writes merged |
| 7 | sectors written |
| 8 | time spent writing (ms) |
| 9 | I/Os currently in progress |
| 10 | time spent doing I/Os (ms) |
| 11 | weighted time spent doing I/Os (ms) |
| 12 | discards completed |
| 13 | discards merged |
| 14 | sectors discarded |
| 15 | time spent discarding (ms) |
| 16 | flush requests completed |
| 17 | time spent flushing (ms) |

For more details refer [I/O statistics fields](iostats.md)

## Symbols under /sys/bus

|  |
| --- |
| **/sys/bus/dsa/devices/dsa<m>/cdev_major** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

The major number that the character device driver assigned to
this device.

|  |
| --- |
| **/sys/bus/dsa/devices/dsa<m>/cmd_status** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

The last executed device administrative command's status/error.
Also last configuration error overloaded.
Writing to it will clear the status.

|  |
| --- |
| **/sys/bus/dsa/devices/dsa<m>/configurable** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

To indicate if this device is configurable or not.

|  |
| --- |
| **/sys/bus/dsa/devices/dsa<m>/engine<m>.<n>** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

The assigned engine under this device.

|  |
| --- |
| **/sys/bus/dsa/devices/dsa<m>/errors** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

The error information for this device.

|  |
| --- |
| **/sys/bus/dsa/devices/dsa<m>/event_log_size** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

The event log size to be configured. Default is 64 entries and
occupies 4k size if the evl entry is 64 bytes. It's visible
only on platforms that support the capability.

|  |
| --- |
| **/sys/bus/dsa/devices/dsa<m>/group<m>.<n>** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

The assigned group under this device.

|  |
| --- |
| **/sys/bus/dsa/devices/dsa<m>/iaa_cap** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

IAA (IAX) capability mask. Exported to user space for application
consumption. This attribute should only be visible on IAA devices
that are version 2 or later.

|  |
| --- |
| **/sys/bus/dsa/devices/dsa<m>/max_batch_size** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

The largest number of work descriptors in a batch.
It's not visible when the device does not support batch.

|  |
| --- |
| **/sys/bus/dsa/devices/dsa<m>/max_engines** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

The maximum number of engines supported by this device.

|  |
| --- |
| **/sys/bus/dsa/devices/dsa<m>/max_groups** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

The maximum number of groups can be created under this device.

|  |
| --- |
| **/sys/bus/dsa/devices/dsa<m>/max_read_buffers** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

The total number of read buffers supported by this device.
The read buffers represent resources within the DSA
implementation, and these resources are allocated by engines to
support operations. See DSA spec v1.2 9.2.4 Total Read Buffers.
It's not visible when the device does not support Read Buffer
allocation control.

|  |
| --- |
| **/sys/bus/dsa/devices/dsa<m>/max_transfer_size** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

The number of bytes to be read from the source address to
perform the operation. The maximum transfer size is dependent on
the workqueue the descriptor was submitted to.

|  |
| --- |
| **/sys/bus/dsa/devices/dsa<m>/max_work_queues** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

The maximum work queue number that this device supports.

|  |
| --- |
| **/sys/bus/dsa/devices/dsa<m>/max_work_queues_size** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

The maximum work queue size supported by this device.

|  |
| --- |
| **/sys/bus/dsa/devices/dsa<m>/numa_node** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

The numa node number for this device.

|  |
| --- |
| **/sys/bus/dsa/devices/dsa<m>/op_cap** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

The operation capability bit mask specify the operation types
supported by the this device.

|  |
| --- |
| **/sys/bus/dsa/devices/dsa<m>/pasid_enabled** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

To indicate if user PASID (process address space identifier) is
enabled or not for this device.

|  |
| --- |
| **/sys/bus/dsa/devices/dsa<m>/read_buffer_limit** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

The maximum number of read buffers that may be in use at
one time by operations that access low bandwidth memory in the
device. See DSA spec v1.2 9.2.8 GENCFG on Global Read Buffer Limit.
It's not visible when the device does not support Read Buffer
allocation control.

|  |
| --- |
| **/sys/bus/dsa/devices/dsa<m>/state** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

The state information of this device. It can be either enabled
or disabled.

|  |
| --- |
| **/sys/bus/dsa/devices/dsa<m>/version** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

The hardware version number.

|  |
| --- |
| **/sys/bus/dsa/devices/dsa<m>/wq<m>.<n>** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

The assigned work queue under this device.

|  |
| --- |
| **/sys/bus/dsa/devices/engine<m>.<n>/group_id** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

The group that this engine belongs to.

|  |
| --- |
| **/sys/bus/dsa/devices/group<m>.<n>/batch_progress_limit** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

Allows control of the number of batch descriptors that can be
concurrently processed by an engine in the group as a fraction
of the Maximum Batch Descriptors in Progress value specified in
the ENGCAP register. The acceptable values are 0 (default),
1 (1/2 of max value), 2 (1/4 of the max value), and 3 (1/8 of
the max value). It's visible only on platforms that support
the capability.

|  |
| --- |
| **/sys/bus/dsa/devices/group<m>.<n>/desc_progress_limit** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

Allows control of the number of work descriptors that can be
concurrently processed by an engine in the group as a fraction
of the Maximum Work Descriptors in Progress value specified in
the ENGCAP register. The acceptable values are 0 (default),
1 (1/2 of max value), 2 (1/4 of the max value), and 3 (1/8 of
the max value). It's visible only on platforms that support
the capability.

|  |
| --- |
| **/sys/bus/dsa/devices/group<m>.<n>/read_buffers_allowed** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

Indicates max number of read buffers that may be in use at one time
by all engines in the group. See DSA spec v1.2 9.2.18 GRPCFG Read
Buffers Allowed.
It's not visible when the device does not support Read Buffer
allocation control.

|  |
| --- |
| **/sys/bus/dsa/devices/group<m>.<n>/read_buffers_reserved** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

Indicates the number of Read Buffers reserved for the use of
engines in the group. See DSA spec v1.2 9.2.18 GRPCFG Read Buffers
Reserved.
It's not visible when the device does not support Read Buffer
allocation control.

|  |
| --- |
| **/sys/bus/dsa/devices/group<m>.<n>/use_read_buffer_limit** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

Enable the use of global read buffer limit for the group. See DSA
spec v1.2 9.2.18 GRPCFG Use Global Read Buffer Limit.
It's not visible when the device does not support Read Buffer
allocation control.

|  |
| --- |
| **/sys/bus/dsa/devices/wq<m>.<n>/ats_disable** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

Indicate whether ATS disable is turned on for the workqueue.
0 indicates ATS is on, and 1 indicates ATS is off for the workqueue.

|  |
| --- |
| **/sys/bus/dsa/devices/wq<m>.<n>/block_on_fault** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

To indicate block on fault is allowed or not for the work queue
to support on demand paging.

|  |
| --- |
| **/sys/bus/dsa/devices/wq<m>.<n>/cdev_minor** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

The minor number assigned to this work queue by the character
device driver.

|  |
| --- |
| **/sys/bus/dsa/devices/wq<m>.<n>/driver_name** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

Name of driver to be bounded to the wq.

|  |
| --- |
| **/sys/bus/dsa/devices/wq<m>.<n>/dsa<x>\!wq<m>.<n>/file<y>/cr_fault_failures** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

Show the number of Completion Record (CR) faults failures that this
application has caused. The failure counter is incremented when the
driver cannot fault in the address for the CR. Typically this is caused
by a bad address programmed in the submitted descriptor or a malicious
submitter is using bad CR address on purpose.

|  |
| --- |
| **/sys/bus/dsa/devices/wq<m>.<n>/dsa<x>\!wq<m>.<n>/file<y>/cr_faults** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

Show the number of Completion Record (CR) faults this application
has caused.

|  |
| --- |
| **/sys/bus/dsa/devices/wq<m>.<n>/dsa<x>\!wq<m>.<n>/file<y>/pid** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

Show the process id of the application that opened the file. This is
helpful information for a monitor daemon that wants to kill the
application that opened the file.

|  |
| --- |
| **/sys/bus/dsa/devices/wq<m>.<n>/enqcmds_retries** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

Indicate the number of retires for an enqcmds submission on a sharedwq.
A max value to set attribute is capped at 64.

|  |
| --- |
| **/sys/bus/dsa/devices/wq<m>.<n>/group_id** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

The group id that this work queue belongs to.

|  |
| --- |
| **/sys/bus/dsa/devices/wq<m>.<n>/max_batch_size** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

The max batch size for this workqueue. Cannot exceed device
max batch size. Configurable parameter.
It's not visible when the device does not support batch.

|  |
| --- |
| **/sys/bus/dsa/devices/wq<m>.<n>/max_transfer_size** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

The max transfer sized for this workqueue. Cannot exceed device
max transfer size. Configurable parameter.

|  |
| --- |
| **/sys/bus/dsa/devices/wq<m>.<n>/mode** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

The work queue mode type for this work queue.

|  |
| --- |
| **/sys/bus/dsa/devices/wq<m>.<n>/occupancy** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

Show the current number of entries in this WQ if WQ Occupancy
Support bit WQ capabilities is 1.

|  |
| --- |
| **/sys/bus/dsa/devices/wq<m>.<n>/op_config** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

Shows the operation capability bits displayed in bitmap format
presented by %\*pb [`printk()`](../core-api/printk-basics.md#c.printk "printk") output format specifier.
The attribute can be configured when the WQ is disabled in
order to configure the WQ to accept specific bits that
correlates to the operations allowed. It's visible only
on platforms that support the capability.

|  |
| --- |
| **/sys/bus/dsa/devices/wq<m>.<n>/priority** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

The priority value of this work queue, it is a value relative to
other work queue in the same group to control quality of service
for dispatching work from multiple workqueues in the same group.

|  |
| --- |
| **/sys/bus/dsa/devices/wq<m>.<n>/prs_disable** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

Controls whether PRS disable is turned on for the workqueue.
0 indicates PRS is on, and 1 indicates PRS is off for the
workqueue. This option overrides block_on_fault attribute
if set. It's visible only on platforms that support the
capability.

|  |
| --- |
| **/sys/bus/dsa/devices/wq<m>.<n>/size** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

The work queue size for this work queue.

|  |
| --- |
| **/sys/bus/dsa/devices/wq<m>.<n>/state** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

The current state of the work queue.

|  |
| --- |
| **/sys/bus/dsa/devices/wq<m>.<n>/threshold** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

The number of entries in this work queue that may be filled
via a limited portal.

|  |
| --- |
| **/sys/bus/dsa/devices/wq<m>.<n>/type** |

Defined on file [sysfs-driver-dma-idxd](abi-stable.md#abi-file-stable-sysfs-driver-dma-idxd)

The type of this work queue, it can be "kernel" type for work
queue usages in the kernel space or "user" type for work queue
usages by applications in user space.

|  |
| --- |
| **/sys/bus/firewire/devices/\*/** |

Defined on file [sysfs-bus-firewire](abi-stable.md#abi-file-stable-sysfs-bus-firewire)

Attributes common to IEEE 1394 node devices and unit devices.
Read-only. Mutable during the node device's lifetime.
Immutable during the unit device's lifetime.
See IEEE 1212 for semantic definitions.

These attributes are only created if the root directory of an
IEEE 1394 node or the unit directory of an IEEE 1394 unit
actually contains according entries.

hardware_version
:   Hexadecimal string representation of an u24.

hardware_version_name
:   Contents of a respective textual descriptor leaf.

model
:   Hexadecimal string representation of an u24.

model_name
:   Contents of a respective textual descriptor leaf.

specifier_id
:   Hexadecimal string representation of an u24.
    Mandatory in unit directories according to IEEE 1212.

vendor
:   Hexadecimal string representation of an u24.
    Mandatory in the root directory according to IEEE 1212.

vendor_name
:   Contents of a respective textual descriptor leaf.

version
:   Hexadecimal string representation of an u24.
    Mandatory in unit directories according to IEEE 1212.

|  |
| --- |
| **/sys/bus/firewire/devices/fw[0-9]+/** |

Defined on file [sysfs-bus-firewire](abi-stable.md#abi-file-stable-sysfs-bus-firewire)

IEEE 1394 node device attributes.
Read-only. Mutable during the node device's lifetime.
See IEEE 1212 for semantic definitions.

config_rom
:   Contents of the Configuration ROM register.
    Binary attribute; an array of host-endian u32.

guid
:   The node's EUI-64 in the bus information block of
    Configuration ROM.
    Hexadecimal string representation of an u64.

|  |
| --- |
| **/sys/bus/firewire/devices/fw[0-9]+/is_local** |

Defined on file [sysfs-bus-firewire](abi-stable.md#abi-file-stable-sysfs-bus-firewire)

IEEE 1394 node device attribute.
Read-only and immutable.
Values: 1: The sysfs entry represents a local node (a controller card).

> 0: The sysfs entry represents a remote node.

|  |
| --- |
| **/sys/bus/firewire/devices/fw[0-9]+/units** |

Defined on file [sysfs-bus-firewire](abi-stable.md#abi-file-stable-sysfs-bus-firewire)

IEEE 1394 node device attribute.
Read-only. Mutable during the node device's lifetime.
See IEEE 1212 for semantic definitions.

units
:   Summary of all units present in an IEEE 1394 node.
    Contains space-separated tuples of specifier_id and
    version of each unit present in the node. Specifier_id
    and version are hexadecimal string representations of
    u24 of the respective unit directory entries.
    Specifier_id and version within each tuple are separated
    by a colon.

Users:
udev rules to set ownership and access permissions or ACLs of
/dev/fw[0-9]+ character device files

|  |
| --- |
| **/sys/bus/firewire/devices/fw[0-9]+[.][0-9]+/** |

Defined on file [sysfs-bus-firewire](abi-stable.md#abi-file-stable-sysfs-bus-firewire)

IEEE 1394 unit device attributes.
Read-only. Immutable during the unit device's lifetime.
See IEEE 1212 for semantic definitions.

modalias
:   Same as MODALIAS in the uevent at device creation.

rom_index
:   Offset of the unit directory within the parent device's
    (node device's) Configuration ROM, in quadlets.
    Decimal string representation.

|  |
| --- |
| **/sys/bus/firewire/drivers/sbp2/fw\*/host\*/target\*/\*:\*:\*:\*/ieee1394_id** |

Defined on file [sysfs-bus-firewire](abi-stable.md#abi-file-stable-sysfs-bus-firewire)

SCSI target port identifier and logical unit identifier of a
logical unit of an SBP-2 target. The identifiers are specified
in SAM-2...SAM-4 annex A. They are persistent and world-wide
unique properties the SBP-2 attached target.

Read-only attribute, immutable during the target's lifetime.
Format, as exposed by firewire-sbp2 since 2.6.22, May 2007:
Colon-separated hexadecimal string representations of

> u64 EUI-64 : u24 directory_ID : u16 LUN

without 0x prefixes, without whitespace. The former sbp2 driver
(removed in 2.6.37 after being superseded by firewire-sbp2) used
a somewhat shorter format which was not as close to SAM.

Users:
udev rules to create /dev/disk/by-id/ symlinks

|  |
| --- |
| **/sys/bus/fsl-mc/autorescan** |

Defined on file [sysfs-bus-fsl-mc](abi-stable.md#abi-file-stable-sysfs-bus-fsl-mc)

Writing a zero value to this attribute will
disable the DPRC IRQs on which automatic rescan
of the fsl-mc bus is performed. A non-zero value
will enable the DPRC IRQs.

Users:
Userspace drivers and management tools

|  |
| --- |
| **/sys/bus/fsl-mc/rescan** |

Defined on file [sysfs-bus-fsl-mc](abi-stable.md#abi-file-stable-sysfs-bus-fsl-mc)

Writing a non-zero value to this attribute will
force a rescan of fsl-mc bus in the system and
synchronize the objects under fsl-mc bus and the
Management Complex firmware.

Users:
Userspace drivers and management tools

|  |
| --- |
| **/sys/bus/mhi/devices/.../oem_pk_hash** |

Defined on file [sysfs-bus-mhi](abi-stable.md#abi-file-stable-sysfs-bus-mhi)

The file holds the OEM PK Hash value of the endpoint device
obtained using a BHI (Boot Host Interface) register read after
at least one attempt to power up the device has been done. If
read without having the device power on at least once, the file
will read all 0's.

Users:
Any userspace application or clients interested in device info.

|  |
| --- |
| **/sys/bus/mhi/devices/.../serialnumber** |

Defined on file [sysfs-bus-mhi](abi-stable.md#abi-file-stable-sysfs-bus-mhi)

The file holds the serial number of the client device obtained
using a BHI (Boot Host Interface) register read after at least
one attempt to power up the device has been done. If read
without having the device power on at least once, the file will
read all 0's.

Users:
Any userspace application or clients interested in device info.

|  |
| --- |
| **/sys/bus/mhi/devices/.../soc_reset** |

Defined on file [sysfs-bus-mhi](abi-stable.md#abi-file-stable-sysfs-bus-mhi)

Initiates a SoC reset on the MHI controller. A SoC reset is
a reset of last resort, and will require a complete re-init.
This can be useful as a method of recovery if the device is
non-responsive, or as a means of loading new firmware as a
system administration task.

|  |
| --- |
| **/sys/bus/nvmem/devices/.../nvmem** |

Defined on file [sysfs-bus-nvmem](abi-stable.md#abi-file-stable-sysfs-bus-nvmem)

This file allows user to read/write the raw NVMEM contents.
Permissions for write to this file depends on the nvmem
provider configuration.
Note: This file is only present if CONFIG_NVMEM_SYSFS
is enabled

ex:

```
hexdump /sys/bus/nvmem/devices/qfprom0/nvmem

0000000 0000 0000 0000 0000 0000 0000 0000 0000
*
00000a0 db10 2240 0000 e000 0c00 0c00 0000 0c00
0000000 0000 0000 0000 0000 0000 0000 0000 0000
...
*
0001000
```

|  |
| --- |
| **/sys/bus/pci/drivers/qla2xxx/.../devices/\*** |

Defined on file [sysfs-driver-qla2xxx](abi-stable.md#abi-file-stable-sysfs-driver-qla2xxx)

qla2xxx-udev.sh currently looks for uevent CHANGE events to
signal a firmware-dump has been generated by the driver and is
ready for retrieval.

Users:
qla2xxx-udev.sh. Proposed changes should be mailed to
[linux-driver@qlogic.com](mailto:linux-driver%40qlogic.com)

|  |
| --- |
| **/sys/bus/platform/drivers/aspeed-vuart/\*/lpc_address** |

Defined on file [sysfs-driver-aspeed-vuart](abi-stable.md#abi-file-stable-sysfs-driver-aspeed-vuart)

Configures which IO port the host side of the UART
will appear on the host <-> BMC LPC bus.

Users:
OpenBMC. Proposed changes should be mailed to
[openbmc@lists.ozlabs.org](mailto:openbmc%40lists.ozlabs.org)

|  |
| --- |
| **/sys/bus/platform/drivers/aspeed-vuart/\*/sirq** |

Defined on file [sysfs-driver-aspeed-vuart](abi-stable.md#abi-file-stable-sysfs-driver-aspeed-vuart)

Configures which interrupt number the host side of
the UART will appear on the host <-> BMC LPC bus.

Users:
OpenBMC. Proposed changes should be mailed to
[openbmc@lists.ozlabs.org](mailto:openbmc%40lists.ozlabs.org)

|  |
| --- |
| **/sys/bus/platform/drivers/aspeed-vuart/\*/sirq_polarity** |

Defined on file [sysfs-driver-aspeed-vuart](abi-stable.md#abi-file-stable-sysfs-driver-aspeed-vuart)

Configures the polarity of the serial interrupt to the
host via the BMC LPC bus.
Set to 0 for active-low or 1 for active-high.

Users:
OpenBMC. Proposed changes should be mailed to
[openbmc@lists.ozlabs.org](mailto:openbmc%40lists.ozlabs.org)

|  |
| --- |
| **/sys/bus/usb/device/.../avoid_reset_quirk** |

Defined on file [sysfs-bus-usb](abi-stable.md#abi-file-stable-sysfs-bus-usb)

Writing 1 to this file tells the kernel that this
device will morph into another mode when it is reset.
Drivers will not use reset for error handling for
such devices.

Users:

usb_modeswitch

|  |
| --- |
| **/sys/bus/usb/device/.../power/active_duration** |

Defined on file [sysfs-bus-usb](abi-stable.md#abi-file-stable-sysfs-bus-usb)

If CONFIG_PM is enabled, then this file is present. When read,
it returns the total time (in msec) that the USB device has been
active, i.e. not in a suspended state. This file is read-only.

Tools can use this file and the connected_duration file to
compute the percentage of time that a device has been active.
For example:

```
echo $((100 * `cat active_duration` / `cat connected_duration`))
```

will give an integer percentage. Note that this does not
account for counter wrap.

Users:

PowerTOP <[powertop@lists.01.org](mailto:powertop%40lists.01.org)>
<https://01.org/powertop/>

|  |
| --- |
| **/sys/bus/usb/device/.../power/connected_duration** |

Defined on file [sysfs-bus-usb](abi-stable.md#abi-file-stable-sysfs-bus-usb)

If CONFIG_PM is enabled, then this file is present. When read,
it returns the total time (in msec) that the USB device has been
connected to the machine. This file is read-only.

Users:

PowerTOP <[powertop@lists.01.org](mailto:powertop%40lists.01.org)>
<https://01.org/powertop/>

|  |
| --- |
| **/sys/bus/usb/devices/.../bConfigurationValue** |

Defined on file [sysfs-bus-usb](abi-stable.md#abi-file-stable-sysfs-bus-usb)

bConfigurationValue of the *active* configuration for the
device. Writing 0 or -1 to bConfigurationValue will reset the
active configuration (unconfigure the device). Writing
another value will change the active configuration.

Note that some devices, in violation of the USB spec, have a
configuration with a value equal to 0. Writing 0 to
bConfigurationValue for these devices will install that
configuration, rather then unconfigure the device.

Writing -1 will always unconfigure the device.

Users:

libusb

|  |
| --- |
| **/sys/bus/usb/devices/.../busnum** |

Defined on file [sysfs-bus-usb](abi-stable.md#abi-file-stable-sysfs-bus-usb)

Bus-number of the USB-bus the device is connected to.

Users:

libusb

|  |
| --- |
| **/sys/bus/usb/devices/.../descriptors** |

Defined on file [sysfs-bus-usb](abi-stable.md#abi-file-stable-sysfs-bus-usb)

Binary file containing cached descriptors of the device. The
binary data consists of the device descriptor followed by the
descriptors for each configuration of the device.
Note that the wTotalLength of the config descriptors can not
be trusted, as the device may have a smaller config descriptor
than it advertises. The bLength field of each (sub) descriptor
can be trusted, and can be used to seek forward one (sub)
descriptor at a time until the next config descriptor is found.
All descriptors read from this file are in bus-endian format

Users:

libusb

|  |
| --- |
| **/sys/bus/usb/devices/.../devnum** |

Defined on file [sysfs-bus-usb](abi-stable.md#abi-file-stable-sysfs-bus-usb)

Device address on the USB bus.

Users:

libusb

|  |
| --- |
| **/sys/bus/usb/devices/.../power/autosuspend** |

Defined on file [sysfs-bus-usb](abi-stable.md#abi-file-stable-sysfs-bus-usb)

Each USB device directory will contain a file named
power/autosuspend. This file holds the time (in seconds)
the device must be idle before it will be autosuspended.
0 means the device will be autosuspended as soon as
possible. Negative values will prevent the device from
being autosuspended at all, and writing a negative value
will resume the device if it is already suspended.

The autosuspend delay for newly-created devices is set to
the value of the usbcore.autosuspend module parameter.

|  |
| --- |
| **/sys/bus/usb/devices/.../power/persist** |

Defined on file [sysfs-bus-usb](abi-stable.md#abi-file-stable-sysfs-bus-usb)

USB device directories can contain a file named power/persist.
The file holds a boolean value (0 or 1) indicating whether or
not the "USB-Persist" facility is enabled for the device. For
hubs this facility is always enabled and their device
directories will not contain this file.

For more information, see [USB device persistence during system suspend](../driver-api/usb/persist.md).

|  |
| --- |
| **/sys/bus/usb/devices/.../speed** |

Defined on file [sysfs-bus-usb](abi-stable.md#abi-file-stable-sysfs-bus-usb)

Speed the device is connected with to the usb-host in
Mbit / second. IE one of 1.5 / 12 / 480 / 5000.

Users:

libusb

|  |
| --- |
| **/sys/bus/usb/devices/<busnum>-<port[.port]>...:<config num>-<interface num>/supports_autosuspend** |

Defined on file [sysfs-bus-usb](abi-stable.md#abi-file-stable-sysfs-bus-usb)

When read, this file returns 1 if the interface driver
for this interface supports autosuspend. It also
returns 1 if no driver has claimed this interface, as an
unclaimed interface will not stop the device from being
autosuspended if all other interface drivers are idle.
The file returns 0 if autosuspend support has not been
added to the driver.

Users:

USB PM tool
git://git.moblin.org/users/sarah/usb-pm-tool/

|  |
| --- |
| **/sys/bus/usb/drivers/usbtmc/\*/interface_capabilities** |
| **/sys/bus/usb/drivers/usbtmc/\*/device_capabilities** |

Defined on file [sysfs-driver-usb-usbtmc](abi-stable.md#abi-file-stable-sysfs-driver-usb-usbtmc)

These files show the various USB TMC capabilities as described
by the device itself. The full description of the bitfields
can be found in the USB TMC documents from the USB-IF entitled
"Universal Serial Bus Test and Measurement Class Specification
(USBTMC) Revision 1.0" section 4.2.1.8.

The files are read only.

|  |
| --- |
| **/sys/bus/usb/drivers/usbtmc/\*/usb488_interface_capabilities** |
| **/sys/bus/usb/drivers/usbtmc/\*/usb488_device_capabilities** |

Defined on file [sysfs-driver-usb-usbtmc](abi-stable.md#abi-file-stable-sysfs-driver-usb-usbtmc)

These files show the various USB TMC capabilities as described
by the device itself. The full description of the bitfields
can be found in the USB TMC documents from the USB-IF entitled
"Universal Serial Bus Test and Measurement Class, Subclass
USB488 Specification (USBTMC-USB488) Revision 1.0" section
4.2.2.

The files are read only.

|  |
| --- |
| **/sys/bus/vmbus/devices/<UUID>/channel_vp_mapping** |

Defined on file [sysfs-bus-vmbus](abi-stable.md#abi-file-stable-sysfs-bus-vmbus)

The mapping of which primary/sub channels are bound to which
Virtual Processors.
Format: <channel's child_relid:the bound cpu's number>

Users:
tools/hv/lsvmbus

|  |
| --- |
| **/sys/bus/vmbus/devices/<UUID>/channels/<N>** |

Defined on file [sysfs-bus-vmbus](abi-stable.md#abi-file-stable-sysfs-bus-vmbus)

Directory for per-channel information
NN is the VMBUS relid associated with the channel.

|  |
| --- |
| **/sys/bus/vmbus/devices/<UUID>/channels/<N>/cpu** |

Defined on file [sysfs-bus-vmbus](abi-stable.md#abi-file-stable-sysfs-bus-vmbus)

VCPU (sub)channel is affinitized to

Users:
tools/hv/lsvmbus and other debugging tools

|  |
| --- |
| **/sys/bus/vmbus/devices/<UUID>/channels/<N>/events** |

Defined on file [sysfs-bus-vmbus](abi-stable.md#abi-file-stable-sysfs-bus-vmbus)

Number of times we have signaled the host

Users:
Debugging tools

|  |
| --- |
| **/sys/bus/vmbus/devices/<UUID>/channels/<N>/in_mask** |

Defined on file [sysfs-bus-vmbus](abi-stable.md#abi-file-stable-sysfs-bus-vmbus)

Host to guest channel interrupt mask

Users:
Debugging tools

|  |
| --- |
| **/sys/bus/vmbus/devices/<UUID>/channels/<N>/interrupts** |

Defined on file [sysfs-bus-vmbus](abi-stable.md#abi-file-stable-sysfs-bus-vmbus)

Number of times we have taken an interrupt (incoming)

Users:
Debugging tools

|  |
| --- |
| **/sys/bus/vmbus/devices/<UUID>/channels/<N>/intr_in_full** |

Defined on file [sysfs-bus-vmbus](abi-stable.md#abi-file-stable-sysfs-bus-vmbus)

Number of guest to host interrupts caused by the inbound ring
buffer transitioning from full to not full while a packet is
waiting for buffer space to become available

Users:
Debugging tools

|  |
| --- |
| **/sys/bus/vmbus/devices/<UUID>/channels/<N>/intr_out_empty** |

Defined on file [sysfs-bus-vmbus](abi-stable.md#abi-file-stable-sysfs-bus-vmbus)

Number of guest to host interrupts caused by the outbound ring
buffer transitioning from empty to not empty

Users:
Debugging tools

|  |
| --- |
| **/sys/bus/vmbus/devices/<UUID>/channels/<N>/latency** |

Defined on file [sysfs-bus-vmbus](abi-stable.md#abi-file-stable-sysfs-bus-vmbus)

Channel signaling latency. This file is available only for
performance critical channels (storage, network, etc.) that use
the monitor page mechanism.

Users:
Debugging tools

|  |
| --- |
| **/sys/bus/vmbus/devices/<UUID>/channels/<N>/monitor_id** |

Defined on file [sysfs-bus-vmbus](abi-stable.md#abi-file-stable-sysfs-bus-vmbus)

Monitor bit associated with channel. This file is available only
for performance critical channels (storage, network, etc.) that
use the monitor page mechanism.

Users:
Debugging tools and userspace drivers

|  |
| --- |
| **/sys/bus/vmbus/devices/<UUID>/channels/<N>/out_full_first** |

Defined on file [sysfs-bus-vmbus](abi-stable.md#abi-file-stable-sysfs-bus-vmbus)

Number of write operations that were the first to encounter an
outbound ring buffer full condition

Users:
Debugging tools

|  |
| --- |
| **/sys/bus/vmbus/devices/<UUID>/channels/<N>/out_full_total** |

Defined on file [sysfs-bus-vmbus](abi-stable.md#abi-file-stable-sysfs-bus-vmbus)

Total number of write operations that encountered an outbound
ring buffer full condition

Users:
Debugging tools

|  |
| --- |
| **/sys/bus/vmbus/devices/<UUID>/channels/<N>/out_mask** |

Defined on file [sysfs-bus-vmbus](abi-stable.md#abi-file-stable-sysfs-bus-vmbus)

Guest to host channel interrupt mask

Users:
Debugging tools

|  |
| --- |
| **/sys/bus/vmbus/devices/<UUID>/channels/<N>/pending** |

Defined on file [sysfs-bus-vmbus](abi-stable.md#abi-file-stable-sysfs-bus-vmbus)

Channel interrupt pending state. This file is available only for
performance critical channels (storage, network, etc.) that use
the monitor page mechanism.

Users:
Debugging tools

|  |
| --- |
| **/sys/bus/vmbus/devices/<UUID>/channels/<N>/read_avail** |

Defined on file [sysfs-bus-vmbus](abi-stable.md#abi-file-stable-sysfs-bus-vmbus)

Bytes available to read

Users:
Debugging tools

|  |
| --- |
| **/sys/bus/vmbus/devices/<UUID>/channels/<N>/ring** |

Defined on file [sysfs-bus-vmbus](abi-stable.md#abi-file-stable-sysfs-bus-vmbus)

Binary file created by uio_hv_generic for ring buffer

Users:
Userspace drivers

|  |
| --- |
| **/sys/bus/vmbus/devices/<UUID>/channels/<N>/subchannel_id** |

Defined on file [sysfs-bus-vmbus](abi-stable.md#abi-file-stable-sysfs-bus-vmbus)

Subchannel ID associated with VMBUS channel

Users:
Debugging tools and userspace drivers

|  |
| --- |
| **/sys/bus/vmbus/devices/<UUID>/channels/<N>/write_avail** |

Defined on file [sysfs-bus-vmbus](abi-stable.md#abi-file-stable-sysfs-bus-vmbus)

Bytes available to write

Users:
Debugging tools

|  |
| --- |
| **/sys/bus/vmbus/devices/<UUID>/class_id** |

Defined on file [sysfs-bus-vmbus](abi-stable.md#abi-file-stable-sysfs-bus-vmbus)

The VMBus interface type GUID of the device

Users:
tools/hv/lsvmbus

|  |
| --- |
| **/sys/bus/vmbus/devices/<UUID>/device** |

Defined on file [sysfs-bus-vmbus](abi-stable.md#abi-file-stable-sysfs-bus-vmbus)

The 16 bit device ID of the device

Users:
tools/hv/lsvmbus and user level RDMA libraries

|  |
| --- |
| **/sys/bus/vmbus/devices/<UUID>/device_id** |

Defined on file [sysfs-bus-vmbus](abi-stable.md#abi-file-stable-sysfs-bus-vmbus)

The VMBus interface instance GUID of the device

Users:
tools/hv/lsvmbus

|  |
| --- |
| **/sys/bus/vmbus/devices/<UUID>/id** |

Defined on file [sysfs-bus-vmbus](abi-stable.md#abi-file-stable-sysfs-bus-vmbus)

The VMBus child_relid of the device's primary channel

Users:
tools/hv/lsvmbus

|  |
| --- |
| **/sys/bus/vmbus/devices/<UUID>/numa_node** |

Defined on file [sysfs-bus-vmbus](abi-stable.md#abi-file-stable-sysfs-bus-vmbus)

This NUMA node to which the VMBUS device is
attached, or -1 if the node is unknown.

|  |
| --- |
| **/sys/bus/vmbus/devices/<UUID>/vendor** |

Defined on file [sysfs-bus-vmbus](abi-stable.md#abi-file-stable-sysfs-bus-vmbus)

The 16 bit vendor ID of the device

Users:
tools/hv/lsvmbus and user level RDMA libraries

|  |
| --- |
| **/sys/bus/vmbus/hibernation** |

Defined on file [sysfs-bus-vmbus](abi-stable.md#abi-file-stable-sysfs-bus-vmbus)

Whether the host supports hibernation for the VM.

Users:
Daemon that sets up swap partition/file for hibernation.

|  |
| --- |
| **/sys/bus/w1/devices/.../eeprom** |

Defined on file [sysfs-driver-w1_ds28e04](abi-stable.md#abi-file-stable-sysfs-driver-w1-ds28e04)

read/write the contents of the EEPROM memory of the DS28E04-100
see [Kernel driver w1_ds28e04](../w1/slaves/w1_ds28e04.md) for detailed information

Users:
any user space application which wants to communicate with DS28E04-100

|  |
| --- |
| **/sys/bus/w1/devices/.../offset** |

Defined on file [sysfs-driver-w1_ds2438](abi-stable.md#abi-file-stable-sysfs-driver-w1-ds2438)

write the contents to the offset register of the DS2438
see [Kernel driver w1_ds2438](../w1/slaves/w1_ds2438.md) for detailed information

Users:
any user space application which wants to communicate with DS2438

|  |
| --- |
| **/sys/bus/w1/devices/.../page1** |

Defined on file [sysfs-driver-w1_ds2438](abi-stable.md#abi-file-stable-sysfs-driver-w1-ds2438)

read the contents of the page1 of the DS2438
see [Kernel driver w1_ds2438](../w1/slaves/w1_ds2438.md) for detailed information

Users:
any user space application which wants to communicate with DS2438

|  |
| --- |
| **/sys/bus/w1/devices/.../pio** |

Defined on file [sysfs-driver-w1_ds28e04](abi-stable.md#abi-file-stable-sysfs-driver-w1-ds28e04)

read/write the contents of the two PIO's of the DS28E04-100
see [Kernel driver w1_ds28e04](../w1/slaves/w1_ds28e04.md) for detailed information

Users:
any user space application which wants to communicate with DS28E04-100

|  |
| --- |
| **/sys/bus/w1/devices/.../w1_master_timeout_us** |

Defined on file [sysfs-bus-w1](abi-stable.md#abi-file-stable-sysfs-bus-w1)

Bus scanning interval, microseconds component.
Some of 1-Wire devices commonly associated with physical access
control systems are attached/generate presence for as short as
100 ms - hence the tens-to-hundreds milliseconds scan intervals
are required.

see [Introduction to the 1-wire (w1) subsystem](../w1/w1-generic.md) for detailed information.

Users:
any user space application which wants to know bus scanning
interval

|  |
| --- |
| **/sys/bus/w1/devices/.../w1_seq** |

Defined on file [sysfs-driver-w1_ds28ea00](abi-stable.md#abi-file-stable-sysfs-driver-w1-ds28ea00)

Support for the DS28EA00 chain sequence function
see [Kernel driver w1_therm](../w1/slaves/w1_therm.md) for detailed information

Users:
any user space application which wants to communicate with DS28EA00

|  |
| --- |
| **/sys/bus/wmi/devices/05901221-D566-11D1-B2F0-00A0C9062910[-X]/bmof** |

Defined on file [sysfs-platform-wmi-bmof](abi-stable.md#abi-file-stable-sysfs-platform-wmi-bmof)

Binary MOF metadata used to describe the details of available ACPI WMI interfaces.

See [WMI embedded Binary MOF driver](../wmi/devices/wmi-bmof.md) for details.

|  |
| --- |
| **/sys/bus/xen-backend/devices/\*/devtype** |

Defined on file [sysfs-bus-xen-backend](abi-stable.md#abi-file-stable-sysfs-bus-xen-backend)

The type of the device. e.g., one of: 'vbd' (block),
'vif' (network), or 'vfb' (framebuffer).

|  |
| --- |
| **/sys/bus/xen-backend/devices/\*/nodename** |

Defined on file [sysfs-bus-xen-backend](abi-stable.md#abi-file-stable-sysfs-bus-xen-backend)

XenStore node (under /local/domain/NNN/) for this
backend device.

|  |
| --- |
| **/sys/bus/xen-backend/devices/\*/state** |

Defined on file [sysfs-bus-xen-backend](abi-stable.md#abi-file-stable-sysfs-bus-xen-backend)

The state of the device. One of: 'Unknown',
'Initialising', 'Initialised', 'Connected', 'Closing',
'Closed', 'Reconfiguring', 'Reconfigured'.

|  |
| --- |
| **/sys/bus/xen-backend/devices/vbd-\*/mode** |

Defined on file [sysfs-bus-xen-backend](abi-stable.md#abi-file-stable-sysfs-bus-xen-backend)

Whether the block device is read-only ('r') or
read-write ('w').

|  |
| --- |
| **/sys/bus/xen-backend/devices/vbd-\*/physical_device** |

Defined on file [sysfs-bus-xen-backend](abi-stable.md#abi-file-stable-sysfs-bus-xen-backend)

The major:minor number (in hexadecimal) of the
physical device providing the storage for this backend
block device.

|  |
| --- |
| **/sys/bus/xen-backend/devices/vbd-\*/statistics/f_req** |

Defined on file [sysfs-bus-xen-backend](abi-stable.md#abi-file-stable-sysfs-bus-xen-backend)

Number of flush requests from the frontend.

|  |
| --- |
| **/sys/bus/xen-backend/devices/vbd-\*/statistics/oo_req** |

Defined on file [sysfs-bus-xen-backend](abi-stable.md#abi-file-stable-sysfs-bus-xen-backend)

Number of requests delayed because the backend was too
busy processing previous requests.

|  |
| --- |
| **/sys/bus/xen-backend/devices/vbd-\*/statistics/rd_req** |

Defined on file [sysfs-bus-xen-backend](abi-stable.md#abi-file-stable-sysfs-bus-xen-backend)

Number of read requests from the frontend.

|  |
| --- |
| **/sys/bus/xen-backend/devices/vbd-\*/statistics/rd_sect** |

Defined on file [sysfs-bus-xen-backend](abi-stable.md#abi-file-stable-sysfs-bus-xen-backend)

Number of sectors read by the frontend.

|  |
| --- |
| **/sys/bus/xen-backend/devices/vbd-\*/statistics/wr_req** |

Defined on file [sysfs-bus-xen-backend](abi-stable.md#abi-file-stable-sysfs-bus-xen-backend)

Number of write requests from the frontend.

|  |
| --- |
| **/sys/bus/xen-backend/devices/vbd-\*/statistics/wr_sect** |

Defined on file [sysfs-bus-xen-backend](abi-stable.md#abi-file-stable-sysfs-bus-xen-backend)

Number of sectors written by the frontend.

## Symbols under /sys/class

|  |
| --- |
| **/sys/class/backlight/<backlight>/actual_brightness** |

Defined on file [sysfs-class-backlight](abi-stable.md#abi-file-stable-sysfs-class-backlight)

Show the actual brightness by querying the hardware.

Users:
HAL

|  |
| --- |
| **/sys/class/backlight/<backlight>/bl_power** |

Defined on file [sysfs-class-backlight](abi-stable.md#abi-file-stable-sysfs-class-backlight)

Control BACKLIGHT power, values are FB_BLANK_\* from fb.h

> - FB_BLANK_UNBLANK (0) : power on.
> - FB_BLANK_POWERDOWN (4) : power off

Users:
HAL

|  |
| --- |
| **/sys/class/backlight/<backlight>/brightness** |

Defined on file [sysfs-class-backlight](abi-stable.md#abi-file-stable-sysfs-class-backlight)

Control the brightness for this <backlight>. Values
are between 0 and max_brightness. This file will also
show the brightness level stored in the driver, which
may not be the actual brightness (see actual_brightness).

Users:
HAL

|  |
| --- |
| **/sys/class/backlight/<backlight>/max_brightness** |

Defined on file [sysfs-class-backlight](abi-stable.md#abi-file-stable-sysfs-class-backlight)

Maximum brightness for <backlight>.

Users:
HAL

|  |
| --- |
| **/sys/class/backlight/<backlight>/type** |

Defined on file [sysfs-class-backlight](abi-stable.md#abi-file-stable-sysfs-class-backlight)

The type of interface controlled by <backlight>.
"firmware": The driver uses a standard firmware interface
"platform": The driver uses a platform-specific interface
"raw": The driver controls hardware registers directly

In the general case, when multiple backlight
interfaces are available for a single device, firmware
control should be preferred to platform control should
be preferred to raw control. Using a firmware
interface reduces the probability of confusion with
the hardware and the OS independently updating the
backlight state. Platform interfaces are mostly a
holdover from pre-standardisation of firmware
interfaces.

|  |
| --- |
| **/sys/class/infiniband/<device-name>/hw_counters/lifespan** |
| **/sys/class/infiniband/<device-name>/ports/<port-num>/hw_counters/lifespan** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

The optional "hw_counters" subdirectory can be under either the
parent device or the port subdirectories or both. If present,
there are a list of counters provided by the hardware. They may
match some of the counters in the counters directory, but they
often include many other counters. In addition to the various
counters, there will be a file named "lifespan" that configures
how frequently the core should update the counters when they are
being accessed (counters are not updated if they are not being
accessed). The lifespan is in milliseconds and defaults to 10
unless set to something else by the driver. Users may echo a
value between 0-10000 to the lifespan file to set the length
of time between updates in milliseconds.

|  |
| --- |
| **/sys/class/infiniband/<device>/fw_ver** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

(RO) Display firmware version

|  |
| --- |
| **/sys/class/infiniband/<device>/node_desc** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

(RW) Update the node description with information such as the
node's hostname, so that IB network management software can tie
its view to the real world.

|  |
| --- |
| **/sys/class/infiniband/<device>/node_type** |
| **/sys/class/infiniband/<device>/node_guid** |
| **/sys/class/infiniband/<device>/sys_image_guid** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

|  |  |
| --- | --- |
| node_type: | (RO) Node type (CA, RNIC, usNIC, usNIC UDP, switch or router) |
| node_guid: | (RO) Node GUID |
| sys_image_guid: | (RO) System image GUID |

|  |
| --- |
| **/sys/class/infiniband/<device>/ports/<port-num>/counters/symbol_error** |
| **/sys/class/infiniband/<device>/ports/<port-num>/counters/port_rcv_errors** |
| **/sys/class/infiniband/<device>/ports/<port-num>/counters/port_rcv_remote_physical_errors** |
| **/sys/class/infiniband/<device>/ports/<port-num>/counters/port_rcv_switch_relay_errors** |
| **/sys/class/infiniband/<device>/ports/<port-num>/counters/link_error_recovery** |
| **/sys/class/infiniband/<device>/ports/<port-num>/counters/port_xmit_constraint_errors** |
| **/sys/class/infiniband/<device>/ports/<port-num>/counters/port_rcv_contraint_errors** |
| **/sys/class/infiniband/<device>/ports/<port-num>/counters/local_link_integrity_errors** |
| **/sys/class/infiniband/<device>/ports/<port-num>/counters/excessive_buffer_overrun_errors** |
| **/sys/class/infiniband/<device>/ports/<port-num>/counters/port_xmit_data** |
| **/sys/class/infiniband/<device>/ports/<port-num>/counters/port_rcv_data** |
| **/sys/class/infiniband/<device>/ports/<port-num>/counters/port_xmit_packets** |
| **/sys/class/infiniband/<device>/ports/<port-num>/counters/port_rcv_packets** |
| **/sys/class/infiniband/<device>/ports/<port-num>/counters/unicast_rcv_packets** |
| **/sys/class/infiniband/<device>/ports/<port-num>/counters/unicast_xmit_packets** |
| **/sys/class/infiniband/<device>/ports/<port-num>/counters/multicast_rcv_packets** |
| **/sys/class/infiniband/<device>/ports/<port-num>/counters/multicast_xmit_packets** |
| **/sys/class/infiniband/<device>/ports/<port-num>/counters/link_downed** |
| **/sys/class/infiniband/<device>/ports/<port-num>/counters/port_xmit_discards** |
| **/sys/class/infiniband/<device>/ports/<port-num>/counters/VL15_dropped** |
| **/sys/class/infiniband/<device>/ports/<port-num>/counters/port_xmit_wait** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

**Errors info**:

symbol_error: (RO) Total number of minor link errors detected on
one or more physical lanes.

port_rcv_errors : (RO) Total number of packets containing an
error that were received on the port.

port_rcv_remote_physical_errors : (RO) Total number of packets
marked with the EBP delimiter received on the port.

port_rcv_switch_relay_errors : (RO) Total number of packets
received on the port that were discarded because they could not
be forwarded by the switch relay.

link_error_recovery: (RO) Total number of times the Port
Training state machine has successfully completed the link error
recovery process.

port_xmit_constraint_errors: (RO) Total number of packets not
transmitted from the switch physical port due to outbound raw
filtering or failing outbound partition or IP version check.

port_rcv_constraint_errors: (RO) Total number of packets
received on the switch physical port that are discarded due to
inbound raw filtering or failing inbound partition or IP version
check.

local_link_integrity_errors: (RO) The number of times that the
count of local physical errors exceeded the threshold specified
by LocalPhyErrors

excessive_buffer_overrun_errors: (RO) This counter, indicates an
input buffer overrun. It indicates possible misconfiguration of
a port, either by the Subnet Manager (SM) or by user
intervention. It can also indicate hardware issues or extremely
poor link signal integrity

**Data info**:

port_xmit_data: (RO) Total number of data octets, divided by 4
(lanes), transmitted on all VLs. This is 64 bit counter

port_rcv_data: (RO) Total number of data octets, divided by 4
(lanes), received on all VLs. This is 64 bit counter.

port_xmit_packets: (RO) Total number of packets transmitted on
all VLs from this port. This may include packets with errors.
This is 64 bit counter.

port_rcv_packets: (RO) Total number of packets (this may include
packets containing Errors. This is 64 bit counter.

link_downed: (RO) Total number of times the Port Training state
machine has failed the link error recovery process and downed
the link.

unicast_rcv_packets: (RO) Total number of unicast packets,
including unicast packets containing errors.

unicast_xmit_packets: (RO) Total number of unicast packets
transmitted on all VLs from the port. This may include unicast
packets with errors.

multicast_rcv_packets: (RO) Total number of multicast packets,
including multicast packets containing errors.

multicast_xmit_packets: (RO) Total number of multicast packets
transmitted on all VLs from the port. This may include multicast
packets with errors.

**Misc info**:

port_xmit_discards: (RO) Total number of outbound packets
discarded by the port because the port is down or congested.

VL15_dropped: (RO) Number of incoming VL15 packets dropped due
to resource limitations (e.g., lack of buffers) of the port.

port_xmit_wait: (RO) The number of ticks during which the port
had data to transmit but no data was sent during the entire tick
(either because of insufficient credits or because of lack of
arbitration).

Each of these files contains the corresponding value from the
port's Performance Management PortCounters attribute, as
described in the InfiniBand Architecture Specification.

|  |
| --- |
| **/sys/class/infiniband/<device>/ports/<port-num>/lid** |
| **/sys/class/infiniband/<device>/ports/<port-num>/rate** |
| **/sys/class/infiniband/<device>/ports/<port-num>/lid_mask_count** |
| **/sys/class/infiniband/<device>/ports/<port-num>/sm_sl** |
| **/sys/class/infiniband/<device>/ports/<port-num>/sm_lid** |
| **/sys/class/infiniband/<device>/ports/<port-num>/state** |
| **/sys/class/infiniband/<device>/ports/<port-num>/phys_state** |
| **/sys/class/infiniband/<device>/ports/<port-num>/cap_mask** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

|  |  |
| --- | --- |
| lid: | (RO) Port LID |
| rate: | (RO) Port data rate (active width \* active speed) |
| lid_mask_count: | (RO) Port LID mask count |
| sm_sl: | (RO) Subnet manager SL for port's subnet |
| sm_lid: | (RO) Subnet manager LID for port's subnet |
| state: | (RO) Port state (DOWN, INIT, ARMED, ACTIVE or ACTIVE_DEFER) |
| phys_state: | (RO) Port physical state (Sleep, Polling, LinkUp, etc) |
| cap_mask: | (RO) Port capability mask. 2 bits here are settable- IsCommunicationManagementSupported (set when CM module is loaded) and IsSM (set via open of issmN file). |

|  |
| --- |
| **/sys/class/infiniband/<device>/ports/<port-num>/link_layer** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

(RO) Link layer type information (Infiniband or Ethernet type)

|  |
| --- |
| **/sys/class/infiniband/<hca>/ports/<port-number>/gid_attrs/ndevs/<gid-index>** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

The net-device's name associated with the GID resides
at index <gid-index>.

|  |
| --- |
| **/sys/class/infiniband/<hca>/ports/<port-number>/gid_attrs/types/<gid-index>** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

The RoCE type of the associated GID resides at index <gid-index>.
This could either be "IB/RoCE v1" for IB and RoCE v1 based GIDs
or "RoCE v2" for RoCE v2 based GIDs.

|  |
| --- |
| **/sys/class/infiniband/bnxt_reX/hw_rev** |
| **/sys/class/infiniband/bnxt_reX/hca_type** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

|  |  |  |
| --- | --- | --- |
| hw_rev: | (RO) | Hardware revision number |
| hca_type: | (RO) | Host channel adapter type |

|  |
| --- |
| **/sys/class/infiniband/cxgb4_X/hw_rev** |
| **/sys/class/infiniband/cxgb4_X/hca_type** |
| **/sys/class/infiniband/cxgb4_X/board_id** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

|  |  |
| --- | --- |
| hw_rev: | (RO) Hardware revision number |
| hca_type: | (RO) Driver short name. Should normally match the name in its bus driver structure (e.g. pci_driver::name) |
| board_id: | (RO) Manufacturing board id. (Vendor + device information) |

sysfs interface for Intel IB driver qib

|  |
| --- |
| **/sys/class/infiniband/hfi1_X/hw_rev** |
| **/sys/class/infiniband/hfi1_X/board_id** |
| **/sys/class/infiniband/hfi1_X/nctxts** |
| **/sys/class/infiniband/hfi1_X/serial** |
| **/sys/class/infiniband/hfi1_X/chip_reset** |
| **/sys/class/infiniband/hfi1_X/boardversion** |
| **/sys/class/infiniband/hfi1_X/nfreectxts** |
| **/sys/class/infiniband/hfi1_X/tempsense** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

|  |  |
| --- | --- |
| hw_rev: | (RO) Hardware revision number |
| board_id: | (RO) Manufacturing board id |
| nctxts: | (RO) Total contexts available. |
| serial: | (RO) Board serial number |
| chip_reset: | (WO) Write "reset" to this file to reset the chip if possible. Only allowed if no user contexts are open that use chip resources. |
| boardversion: | (RO) Human readable board info |
| nfreectxts: | (RO) The number of free user ports (contexts) available. |
| tempsense: | (RO) Thermal sense information |

|  |
| --- |
| **/sys/class/infiniband/hfi1_X/ports/<N>/CCMgtA/cc_settings_bin** |
| **/sys/class/infiniband/hfi1_X/ports/<N>/CCMgtA/cc_table_bin** |
| **/sys/class/infiniband/hfi1_X/ports/<N>/CCMgtA/cc_prescan** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

Per-port congestion control.

|  |  |
| --- | --- |
| cc_table_bin | (RO) CCA tables used by PSM2 Congestion control table size followed by table entries. Binary attribute. |
| cc_settings_bin | (RO) Congestion settings: port control, control map and an array of 16 entries for the congestion entries - increase, timer, event log trigger threshold and the minimum injection rate delay. Binary attribute. |
| cc_prescan | (RW) enable prescanning for faster BECN response. Write "on" to enable and "off" to disable. |

|  |
| --- |
| **/sys/class/infiniband/hfi1_X/ports/<N>/sc2vl/[0-31]** |
| **/sys/class/infiniband/hfi1_X/ports/<N>/sl2sc/[0-31]** |
| **/sys/class/infiniband/hfi1_X/ports/<N>/vl2mtu/[0-15]** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

|  |  |
| --- | --- |
| sc2vl/: | (RO) 32 files (0 - 31) used to translate sl->vl |
| sl2sc/: | (RO) 32 files (0 - 31) used to translate sl->sc |
| vl2mtu/: | (RO) 16 files (0 - 15) used to determine MTU for vl |

|  |
| --- |
| **/sys/class/infiniband/hfi1_X/sdma_<N>/cpu_list** |
| **/sys/class/infiniband/hfi1_X/sdma_<N>/vl** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

sdma<N>/ contains one directory per sdma engine (0 - 15)

|  |  |
| --- | --- |
| cpu_list: | (RW) List of cpus for user-process to sdma engine assignment. |
| vl: | (RO) Displays the virtual lane (vl) the sdma engine maps to. |

This interface gives the user control on the affinity settings
for the device. As an example, to set an sdma engine irq
affinity and thread affinity of a user processes to use the
sdma engine, which is "near" in terms of NUMA configuration, or
physical cpu location, the user will do:

```
echo "3" > /proc/irq/<N>/smp_affinity_list
echo "4-7" > /sys/devices/.../sdma3/cpu_list
cat /sys/devices/.../sdma3/vl
0
echo "8" > /proc/irq/<M>/smp_affinity_list
echo "9-12" > /sys/devices/.../sdma4/cpu_list
cat /sys/devices/.../sdma4/vl
1
```

to make sure that when a process runs on cpus 4,5,6, or 7, and
uses vl=0, then sdma engine 3 is selected by the driver, and
also the interrupt of the sdma engine 3 is steered to cpu 3.
Similarly, when a process runs on cpus 9,10,11, or 12 and sets
vl=1, then engine 4 will be selected and the irq of the sdma
engine 4 is steered to cpu 8. This assumes that in the above N
is the irq number of "sdma3", and M is irq number of "sdma4" in
the /proc/interrupts file.

sysfs interface for QLogic qedr NIC Driver

|  |
| --- |
| **/sys/class/infiniband/mlx4_X/hw_rev** |
| **/sys/class/infiniband/mlx4_X/hca_type** |
| **/sys/class/infiniband/mlx4_X/board_id** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

|  |  |
| --- | --- |
| hw_rev: | (RO) Hardware revision number |
| hca_type: | (RO) Host channel adapter type |
| board_id: | (RO) Manufacturing board ID |

|  |
| --- |
| **/sys/class/infiniband/mlx4_X/iov/<pci-slot-num>/ports/<m>/smi_enabled** |
| **/sys/class/infiniband/mlx4_X/iov/<pci-slot-num>/ports/<m>/enable_smi_admin** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

Enabling QP0 on VFs for selected VF/port. By default, no VFs are
enabled for QP0 operation.

|  |  |  |
| --- | --- | --- |
| smi_enabled: | (RO) | Indicates whether smi is currently enabled for the indicated VF/port |
| enable_smi_admin: | (RW) | Used by the admin to request that smi capability be enabled or disabled for the indicated VF/port. 0 = disable, 1 = enable. |

The requested enablement will occur at the next reset of the VF
(e.g. driver restart on the VM which owns the VF).

sysfs interface for Chelsio T4/T5 RDMA driver (cxgb4)

|  |
| --- |
| **/sys/class/infiniband/mlx4_X/iov/ports/<port-num>/gids/<n>** |
| **/sys/class/infiniband/mlx4_X/iov/ports/<port-num>/admin_guids/<n>** |
| **/sys/class/infiniband/mlx4_X/iov/ports/<port-num>/pkeys/<n>** |
| **/sys/class/infiniband/mlx4_X/iov/ports/<port-num>/mcgs/** |
| **/sys/class/infiniband/mlx4_X/iov/ports/<pci-slot-num>/ports/<m>/gid_idx/0** |
| **/sys/class/infiniband/mlx4_X/iov/ports/<pci-slot-num>/ports/<m>/pkey_idx/<n>** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

The sysfs iov directory is used to manage and examine the port
P_Key and guid paravirtualization. This directory is added only
for the master -- slaves do not have it.

Under iov/ports, the administrator may examine the gid and P_Key
tables as they are present in the device (and as are seen in the
"network view" presented to the SM).

The "pkeys" and "gids" subdirectories contain one file for each
entry in the port's P_Key or GID table respectively. For
example, ports/1/pkeys/10 contains the value at index 10 in port
1's P_Key table.

|  |  |
| --- | --- |
| gids/<n>: | (RO) The physical port gids n = 0..127 |
| admin_guids/<n>: | (RW) Allows examining or changing the administrative state of a given GUID n = 0..127 |
| pkeys/<n>: | (RO) Displays the contents of the physical key table n = 0..126 |
| mcgs/: | (RO) Multicast group table |
| <m>/gid_idx/0: | (RO) Display the GID mapping m = 1..2 |
| <m>/pkey_idx/<n>: | (RW) Writable except for RoCE pkeys. m = 1..2, n = 0..126  Under the iov/<pci slot number> directories, the admin may map the index numbers in the physical tables (as under iov/ports) to the paravirtualized index numbers that guests see.  For example, if the administrator, for port 1 on guest 2 maps physical pkey index 10 to virtual index 1, then that guest, whenever it uses its pkey index 1, will actually be using the real pkey index 10. |

|  |
| --- |
| **/sys/class/infiniband/mlx5_X/hw_rev** |
| **/sys/class/infiniband/mlx5_X/hca_type** |
| **/sys/class/infiniband/mlx5_X/reg_pages** |
| **/sys/class/infiniband/mlx5_X/fw_pages** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

[to be documented]

sysfs interface for Cisco VIC (usNIC) Verbs Driver

|  |
| --- |
| **/sys/class/infiniband/mthcaX/hw_rev** |
| **/sys/class/infiniband/mthcaX/hca_type** |
| **/sys/class/infiniband/mthcaX/board_id** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

|  |  |
| --- | --- |
| hw_rev: | (RO) Hardware revision number |
| hca_type: | (RO) Host Channel Adapter type: MT23108, MT25208 (MT23108 compat mode), MT25208 or MT25204 |
| board_id: | (RO) Manufacturing board ID |

sysfs interface for Mellanox ConnectX HCA IB driver (mlx4)

|  |
| --- |
| **/sys/class/infiniband/ocrdmaX/hca_type** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

hca_type: (RO) Display FW version

sysfs interface for Intel Omni-Path driver (HFI1)

|  |
| --- |
| **/sys/class/infiniband/ocrdmaX/hw_rev** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

hw_rev: (RO) Hardware revision number

|  |
| --- |
| **/sys/class/infiniband/qedrX/hw_rev** |
| **/sys/class/infiniband/qedrX/hca_type** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

|  |  |  |
| --- | --- | --- |
| hw_rev: | (RO) | Hardware revision number |
| hca_type: | (RO) | Display HCA type |

sysfs interface for VMware Paravirtual RDMA driver

|  |
| --- |
| **/sys/class/infiniband/qibX/ports/<N>/CCMgtA/cc_settings_bin** |
| **/sys/class/infiniband/qibX/ports/<N>/CCMgtA/cc_table_bin** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

Per-port congestion control. Both are binary attributes.

|  |  |
| --- | --- |
| cc_table_bin | (RO) Congestion control table size followed by table entries. |
| cc_settings_bin | (RO) Congestion settings: port control, control map and an array of 16 entries for the congestion entries - increase, timer, event log trigger threshold and the minimum injection rate delay. |

|  |
| --- |
| **/sys/class/infiniband/qibX/ports/<N>/diag_counters/rc_resends** |
| **/sys/class/infiniband/qibX/ports/<N>/diag_counters/seq_naks** |
| **/sys/class/infiniband/qibX/ports/<N>/diag_counters/rdma_seq** |
| **/sys/class/infiniband/qibX/ports/<N>/diag_counters/rnr_naks** |
| **/sys/class/infiniband/qibX/ports/<N>/diag_counters/other_naks** |
| **/sys/class/infiniband/qibX/ports/<N>/diag_counters/rc_timeouts** |
| **/sys/class/infiniband/qibX/ports/<N>/diag_counters/look_pkts** |
| **/sys/class/infiniband/qibX/ports/<N>/diag_counters/pkt_drops** |
| **/sys/class/infiniband/qibX/ports/<N>/diag_counters/dma_wait** |
| **/sys/class/infiniband/qibX/ports/<N>/diag_counters/unaligned** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

[to be documented]

sysfs interface for Mellanox Connect-IB HCA driver mlx5

|  |
| --- |
| **/sys/class/infiniband/qibX/ports/<N>/linkstate/loopback** |
| **/sys/class/infiniband/qibX/ports/<N>/linkstate/led_override** |
| **/sys/class/infiniband/qibX/ports/<N>/linkstate/hrtbt_enable** |
| **/sys/class/infiniband/qibX/ports/<N>/linkstate/status** |
| **/sys/class/infiniband/qibX/ports/<N>/linkstate/status_str** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

[to be documented]

|  |  |
| --- | --- |
| loopback: | (WO) |
| led_override: | (WO) |
| hrtbt_enable: | (RW) |
| status: | (RO) |
| status_str: | (RO) Displays information about the link state, possible cable/switch problems, and hardware errors. Possible states are- "Initted", "Present", "IB_link_up", "IB_configured" or "Fatal_Hardware_Error". |

|  |
| --- |
| **/sys/class/infiniband/qibX/ports/<N>/sl2vl/[0-15]** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

(RO) The directory contains 16 files numbered 0-15 that specify
the Service Level (SL). Listing the SL files returns the Virtual
Lane (VL) as programmed by the SL.

|  |
| --- |
| **/sys/class/infiniband/qibX/version** |
| **/sys/class/infiniband/qibX/hw_rev** |
| **/sys/class/infiniband/qibX/hca_type** |
| **/sys/class/infiniband/qibX/board_id** |
| **/sys/class/infiniband/qibX/boardversion** |
| **/sys/class/infiniband/qibX/nctxts** |
| **/sys/class/infiniband/qibX/localbus_info** |
| **/sys/class/infiniband/qibX/tempsense** |
| **/sys/class/infiniband/qibX/serial** |
| **/sys/class/infiniband/qibX/nfreectxts** |
| **/sys/class/infiniband/qibX/chip_reset** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

|  |  |
| --- | --- |
| version: | (RO) Display version information of installed software and drivers. |
| hw_rev: | (RO) Hardware revision number |
| hca_type: | (RO) Host channel adapter type |
| board_id: | (RO) Manufacturing board id |
| boardversion: | (RO) Current version of the chip architecture |
| nctxts: | (RO) Return the number of user ports (contexts) available |
| localbus_info: | (RO) Human readable localbus info |
| tempsense: | (RO) Display temp sense registers in decimal |
| serial: | (RO) Serial number of the HCA |
| nfreectxts: | (RO) The number of free user ports (contexts) available. |
| chip_reset: | (WO) Reset the chip if possible by writing "reset" to this file. Only allowed if no user contexts are open that use chip resources. |

|  |
| --- |
| **/sys/class/infiniband/usnic_X/board_id** |
| **/sys/class/infiniband/usnic_X/config** |
| **/sys/class/infiniband/usnic_X/qp_per_vf** |
| **/sys/class/infiniband/usnic_X/max_vf** |
| **/sys/class/infiniband/usnic_X/cq_per_vf** |
| **/sys/class/infiniband/usnic_X/iface** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

|  |  |
| --- | --- |
| board_id: | (RO) Manufacturing board id |
| config: | (RO) Report the configuration for this PF |
| qp_per_vf: | (RO) Queue pairs per virtual function. |
| max_vf: | (RO) Max virtual functions |
| cq_per_vf: | (RO) Completion queue per virtual function |
| iface: | (RO) Shows which network interface this usNIC entry is associated to (visible with ifconfig). |

|  |
| --- |
| **/sys/class/infiniband/usnic_X/qpn/summary** |
| **/sys/class/infiniband/usnic_X/qpn/context** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

[to be documented]

sysfs interface for Emulex RoCE HCA Driver

|  |
| --- |
| **/sys/class/infiniband/vmw_pvrdmaX/hw_rev** |
| **/sys/class/infiniband/vmw_pvrdmaX/hca_type** |
| **/sys/class/infiniband/vmw_pvrdmaX/board_id** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

|  |  |  |
| --- | --- | --- |
| hw_rev: | (RO) | Hardware revision number |
| hca_type: | (RO) | Host channel adapter type |
| board_id: | (RO) | Display PVRDMA manufacturing board ID |

sysfs interface for Broadcom NetXtreme-E RoCE driver

|  |
| --- |
| **/sys/class/infiniband_mad/abi_version** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

(RO) Value is incremented if any changes are made that break
userspace ABI compatibility of umad & issm devices.

|  |
| --- |
| **/sys/class/infiniband_mad/umad<N>/ibdev** |
| **/sys/class/infiniband_mad/umad<N>/port** |
| **/sys/class/infiniband_mad/issm<N>/ibdev** |
| **/sys/class/infiniband_mad/issm<N>/port** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

Each port of each InfiniBand device has a "umad" device and an
"issm" device attached. For example, a two-port HCA will have
two umad devices and two issm devices, while a switch will have
one device of each type (for switch port 0).

|  |  |
| --- | --- |
| ibdev: | (RO) Show Infiniband (IB) device name |
| port: | (RO) Display port number |

|  |
| --- |
| **/sys/class/infiniband_srp/srp-<hca>-<port_number>/add_target** |

Defined on file [sysfs-driver-ib_srp](abi-stable.md#abi-file-stable-sysfs-driver-ib-srp)

Interface for making ib_srp connect to a new target.
One can request ib_srp to connect to a new target by writing
a comma-separated list of login parameters to this sysfs
attribute. The supported parameters are:

- id_ext, a 16-digit hexadecimal number specifying the eight
  byte identifier extension in the 16-byte SRP target port
  identifier. The target port identifier is sent by ib_srp
  to the target in the SRP_LOGIN_REQ request.
- ioc_guid, a 16-digit hexadecimal number specifying the eight
  byte I/O controller GUID portion of the 16-byte target port
  identifier.
- dgid, a 32-digit hexadecimal number specifying the
  destination GID.
- pkey, a four-digit hexadecimal number specifying the
  InfiniBand partition key.
- service_id, a 16-digit hexadecimal number specifying the
  InfiniBand service ID used to establish communication with
  the SRP target. How to find out the value of the service ID
  is specified in the documentation of the SRP target.
- max_sect, a decimal number specifying the maximum number of
  512-byte sectors to be transferred via a single SCSI command.
- max_cmd_per_lun, a decimal number specifying the maximum
  number of outstanding commands for a single LUN.
- io_class, a hexadecimal number specifying the SRP I/O class.
  Must be either 0xff00 (rev 10) or 0x0100 (rev 16a). The I/O
  class defines the format of the SRP initiator and target
  port identifiers.
- initiator_ext, a 16-digit hexadecimal number specifying the
  identifier extension portion of the SRP initiator port
  identifier. This data is sent by the initiator to the target
  in the SRP_LOGIN_REQ request.
- cmd_sg_entries, a number in the range 1..255 that specifies
  the maximum number of data buffer descriptors stored in the
  SRP_CMD information unit itself. With allow_ext_sg=0 the
  parameter cmd_sg_entries defines the maximum S/G list length
  for a single SRP_CMD, and commands whose S/G list length
  exceeds this limit after S/G list collapsing will fail.
- allow_ext_sg, whether ib_srp is allowed to include a partial
  memory descriptor list in an SRP_CMD instead of the entire
  list. If a partial memory descriptor list has been included
  in an SRP_CMD the remaining memory descriptors are
  communicated from initiator to target via an additional RDMA
  transfer. Setting allow_ext_sg to 1 increases the maximum
  amount of data that can be transferred between initiator and
  target via a single SCSI command. Since not all SRP target
  implementations support partial memory descriptor lists the
  default value for this option is 0.
- sg_tablesize, a number in the range 1..2048 specifying the
  maximum S/G list length the SCSI layer is allowed to pass to
  ib_srp. Specifying a value that exceeds cmd_sg_entries is
  only safe with partial memory descriptor list support enabled
  (allow_ext_sg=1).
- comp_vector, a number in the range 0..n-1 specifying the
  MSI-X completion vector of the first RDMA channel. Some
  HCA's allocate multiple (n) MSI-X vectors per HCA port. If
  the IRQ affinity masks of these interrupts have been
  configured such that each MSI-X interrupt is handled by a
  different CPU then the comp_vector parameter can be used to
  spread the SRP completion workload over multiple CPU's.
- tl_retry_count, a number in the range 2..7 specifying the
  IB RC retry count.
- queue_size, the maximum number of commands that the
  initiator is allowed to queue per SCSI host. The default
  value for this parameter is 62. The lowest supported value
  is 2.
- max_it_iu_size, a decimal number specifying the maximum
  initiator to target information unit length.

|  |
| --- |
| **/sys/class/infiniband_srp/srp-<hca>-<port_number>/ibdev** |

Defined on file [sysfs-driver-ib_srp](abi-stable.md#abi-file-stable-sysfs-driver-ib-srp)

HCA name (<hca>).

|  |
| --- |
| **/sys/class/infiniband_srp/srp-<hca>-<port_number>/port** |

Defined on file [sysfs-driver-ib_srp](abi-stable.md#abi-file-stable-sysfs-driver-ib-srp)

HCA port number (<port_number>).

|  |
| --- |
| **/sys/class/infiniband_verbs/abi_version** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

(RO) Value is incremented if any changes are made that break
userspace ABI compatibility of uverbs devices.

sysfs interface for Mellanox IB HCA low-level driver (mthca)

|  |
| --- |
| **/sys/class/infiniband_verbs/uverbs<N>/ibdev** |
| **/sys/class/infiniband_verbs/uverbs<N>/abi_version** |

Defined on file [sysfs-class-infiniband](abi-stable.md#abi-file-stable-sysfs-class-infiniband)

|  |  |
| --- | --- |
| ibdev: | (RO) Display Infiniband (IB) device name |
| abi_version: | (RO) Show ABI version of IB device specific interfaces. |

|  |
| --- |
| **/sys/class/rfkill** |

Defined on file [sysfs-class-rfkill](abi-stable.md#abi-file-stable-sysfs-class-rfkill)

The rfkill class subsystem folder.
Each registered rfkill driver is represented by an rfkillX
subfolder (X being an integer >= 0).

|  |
| --- |
| **/sys/class/rfkill/rfkill[0-9]+/hard** |

Defined on file [sysfs-class-rfkill](abi-stable.md#abi-file-stable-sysfs-class-rfkill)

Current hardblock state. This file is read only.
Values: A numeric value.

> 0: inactive
> :   The transmitter is (potentially) active.
>
> 1: active
> :   The transmitter is forced off by something outside of
>     the driver's control.

|  |
| --- |
| **/sys/class/rfkill/rfkill[0-9]+/name** |

Defined on file [sysfs-class-rfkill](abi-stable.md#abi-file-stable-sysfs-class-rfkill)

Name assigned by driver to this key (interface or driver name).
Values: arbitrary string.

|  |
| --- |
| **/sys/class/rfkill/rfkill[0-9]+/persistent** |

Defined on file [sysfs-class-rfkill](abi-stable.md#abi-file-stable-sysfs-class-rfkill)

Whether the soft blocked state is initialised from non-volatile
storage at startup.
Values: A numeric value:

> - 0: false
> - 1: true

|  |
| --- |
| **/sys/class/rfkill/rfkill[0-9]+/soft** |

Defined on file [sysfs-class-rfkill](abi-stable.md#abi-file-stable-sysfs-class-rfkill)

Current softblock state. This file is read and write.
Values: A numeric value.

> 0: inactive
> :   The transmitter is (potentially) active.
>
> 1: active
> :   The transmitter is turned off by software.

|  |
| --- |
| **/sys/class/rfkill/rfkill[0-9]+/state** |

Defined on file [sysfs-class-rfkill](abi-stable.md#abi-file-stable-sysfs-class-rfkill)

Current state of the transmitter.
This file was scheduled to be removed in 2014, but due to its
large number of users it will be sticking around for a bit
longer. Despite it being marked as stable, the newer "hard" and
"soft" interfaces should be preferred, since it is not possible
to express the 'soft and hard block' state of the rfkill driver
through this interface. There will likely be another attempt to
remove it in the future.
Values: A numeric value.

> 0: RFKILL_STATE_SOFT_BLOCKED
> :   transmitter is turned off by software
>
> 1: RFKILL_STATE_UNBLOCKED
> :   transmitter is (potentially) active
>
> 2: RFKILL_STATE_HARD_BLOCKED
> :   transmitter is forced off by something outside of
>     the driver's control.

|  |
| --- |
| **/sys/class/rfkill/rfkill[0-9]+/type** |

Defined on file [sysfs-class-rfkill](abi-stable.md#abi-file-stable-sysfs-class-rfkill)

Driver type string ("wlan", "bluetooth", etc).
Values: See include/linux/rfkill.h.

|  |
| --- |
| **/sys/class/scsi_host/host<n>/allow_ext_sg** |

Defined on file [sysfs-driver-ib_srp](abi-stable.md#abi-file-stable-sysfs-driver-ib-srp)

Whether ib_srp is allowed to include a partial memory
descriptor list in an SRP_CMD when communicating with an SRP
target.

|  |
| --- |
| **/sys/class/scsi_host/host<n>/ch_count** |

Defined on file [sysfs-driver-ib_srp](abi-stable.md#abi-file-stable-sysfs-driver-ib-srp)

Number of RDMA channels used for communication with the SRP
target.

|  |
| --- |
| **/sys/class/scsi_host/host<n>/cmd_sg_entries** |

Defined on file [sysfs-driver-ib_srp](abi-stable.md#abi-file-stable-sysfs-driver-ib-srp)

Maximum number of data buffer descriptors that may be sent to
the target in a single SRP_CMD request.

|  |
| --- |
| **/sys/class/scsi_host/host<n>/comp_vector** |

Defined on file [sysfs-driver-ib_srp](abi-stable.md#abi-file-stable-sysfs-driver-ib-srp)

Completion vector used for the first RDMA channel.

|  |
| --- |
| **/sys/class/scsi_host/host<n>/dgid** |

Defined on file [sysfs-driver-ib_srp](abi-stable.md#abi-file-stable-sysfs-driver-ib-srp)

InfiniBand destination GID used for communication with the SRP
target. Differs from orig_dgid if port redirection has happened.

|  |
| --- |
| **/sys/class/scsi_host/host<n>/id_ext** |

Defined on file [sysfs-driver-ib_srp](abi-stable.md#abi-file-stable-sysfs-driver-ib-srp)

Eight-byte identifier extension portion of the 16-byte target
port identifier.

|  |
| --- |
| **/sys/class/scsi_host/host<n>/ioc_guid** |

Defined on file [sysfs-driver-ib_srp](abi-stable.md#abi-file-stable-sysfs-driver-ib-srp)

Eight-byte I/O controller GUID portion of the 16-byte target
port identifier.

|  |
| --- |
| **/sys/class/scsi_host/host<n>/local_ib_device** |

Defined on file [sysfs-driver-ib_srp](abi-stable.md#abi-file-stable-sysfs-driver-ib-srp)

Name of the InfiniBand HCA used for communicating with the
SRP target.

|  |
| --- |
| **/sys/class/scsi_host/host<n>/local_ib_port** |

Defined on file [sysfs-driver-ib_srp](abi-stable.md#abi-file-stable-sysfs-driver-ib-srp)

Number of the HCA port used for communicating with the
SRP target.

|  |
| --- |
| **/sys/class/scsi_host/host<n>/orig_dgid** |

Defined on file [sysfs-driver-ib_srp](abi-stable.md#abi-file-stable-sysfs-driver-ib-srp)

InfiniBand destination GID specified in the parameters
written to the add_target sysfs attribute.

|  |
| --- |
| **/sys/class/scsi_host/host<n>/pkey** |

Defined on file [sysfs-driver-ib_srp](abi-stable.md#abi-file-stable-sysfs-driver-ib-srp)

A 16-bit number representing the InfiniBand partition key used
for communication with the SRP target.

|  |
| --- |
| **/sys/class/scsi_host/host<n>/req_lim** |

Defined on file [sysfs-driver-ib_srp](abi-stable.md#abi-file-stable-sysfs-driver-ib-srp)

Number of requests ib_srp can send to the target before it has
to wait for more credits. For more information see also the
SRP credit algorithm in the SRP specification.

|  |
| --- |
| **/sys/class/scsi_host/host<n>/service_id** |

Defined on file [sysfs-driver-ib_srp](abi-stable.md#abi-file-stable-sysfs-driver-ib-srp)

InfiniBand service ID used for establishing communication with
the SRP target.

|  |
| --- |
| **/sys/class/scsi_host/host<n>/sgid** |

Defined on file [sysfs-driver-ib_srp](abi-stable.md#abi-file-stable-sysfs-driver-ib-srp)

InfiniBand GID of the source port used for communication with
the SRP target.

|  |
| --- |
| **/sys/class/scsi_host/host<n>/zero_req_lim** |

Defined on file [sysfs-driver-ib_srp](abi-stable.md#abi-file-stable-sysfs-driver-ib-srp)

Number of times the initiator had to wait before sending a
request to the target because it ran out of credits. For more
information see also the SRP credit algorithm in the SRP
specification.

|  |
| --- |
| **/sys/class/srp_remote_ports/port-<h>:<n>/delete** |

Defined on file [sysfs-transport-srp](abi-stable.md#abi-file-stable-sysfs-transport-srp)

Instructs an SRP initiator to disconnect from a target and to
remove all LUNs imported from that target.

|  |
| --- |
| **/sys/class/srp_remote_ports/port-<h>:<n>/dev_loss_tmo** |

Defined on file [sysfs-transport-srp](abi-stable.md#abi-file-stable-sysfs-transport-srp)

Number of seconds the SCSI layer will wait after a transport
layer error has been observed before removing a target port.
Zero means immediate removal. Setting this attribute to "off"
will disable the dev_loss timer.

|  |
| --- |
| **/sys/class/srp_remote_ports/port-<h>:<n>/fast_io_fail_tmo** |

Defined on file [sysfs-transport-srp](abi-stable.md#abi-file-stable-sysfs-transport-srp)

Number of seconds the SCSI layer will wait after a transport
layer error has been observed before failing I/O. Zero means
failing I/O immediately. Setting this attribute to "off" will
disable the fast_io_fail timer.

|  |
| --- |
| **/sys/class/srp_remote_ports/port-<h>:<n>/port_id** |

Defined on file [sysfs-transport-srp](abi-stable.md#abi-file-stable-sysfs-transport-srp)

16-byte local SRP port identifier in hexadecimal format. An
example: 4c:49:4e:55:58:20:56:49:4f:00:00:00:00:00:00:00.

|  |
| --- |
| **/sys/class/srp_remote_ports/port-<h>:<n>/reconnect_delay** |

Defined on file [sysfs-transport-srp](abi-stable.md#abi-file-stable-sysfs-transport-srp)

Number of seconds the SCSI layer will wait after a reconnect
attempt failed before retrying. Setting this attribute to
"off" will disable time-based reconnecting.

|  |
| --- |
| **/sys/class/srp_remote_ports/port-<h>:<n>/roles** |

Defined on file [sysfs-transport-srp](abi-stable.md#abi-file-stable-sysfs-transport-srp)

Role of the remote port. Either "SRP Initiator" or "SRP Target".

|  |
| --- |
| **/sys/class/srp_remote_ports/port-<h>:<n>/state** |

Defined on file [sysfs-transport-srp](abi-stable.md#abi-file-stable-sysfs-transport-srp)

State of the transport layer used for communication with the
remote port. "running" if the transport layer is operational;
"blocked" if a transport layer error has been encountered but
the fast_io_fail_tmo timer has not yet fired; "fail-fast"
after the fast_io_fail_tmo timer has fired and before the
"dev_loss_tmo" timer has fired; "lost" after the
"dev_loss_tmo" timer has fired and before the port is finally
removed.

|  |
| --- |
| **/sys/class/tpm/tpmX/device/** |

Defined on file [sysfs-class-tpm](abi-stable.md#abi-file-stable-sysfs-class-tpm)

The device/ directory under a specific TPM instance exposes
the properties of that TPM chip

|  |
| --- |
| **/sys/class/tpm/tpmX/device/active** |

Defined on file [sysfs-class-tpm](abi-stable.md#abi-file-stable-sysfs-class-tpm)

The "active" property prints a '1' if the TPM chip is accepting
commands. An inactive TPM chip still contains all the state of
an active chip (Storage Root Key, NVRAM, etc), and can be
visible to the OS, but will only accept a restricted set of
commands. See the TPM Main Specification part 2, Structures,
section 17 for more information on which commands are
available.

|  |
| --- |
| **/sys/class/tpm/tpmX/device/cancel** |

Defined on file [sysfs-class-tpm](abi-stable.md#abi-file-stable-sysfs-class-tpm)

The "cancel" property allows you to cancel the currently
pending TPM command. Writing any value to cancel will call the
TPM vendor specific cancel operation.

|  |
| --- |
| **/sys/class/tpm/tpmX/device/caps** |

Defined on file [sysfs-class-tpm](abi-stable.md#abi-file-stable-sysfs-class-tpm)

The "caps" property contains TPM manufacturer and version info.

Example output:

```
Manufacturer: 0x53544d20
TCG version: 1.2
Firmware version: 8.16
```

Manufacturer is a hex dump of the 4 byte manufacturer info
space in a TPM. TCG version shows the TCG TPM spec level that
the chip supports. Firmware version is that of the chip and
is manufacturer specific.

|  |
| --- |
| **/sys/class/tpm/tpmX/device/durations** |

Defined on file [sysfs-class-tpm](abi-stable.md#abi-file-stable-sysfs-class-tpm)

The "durations" property shows the 3 vendor-specific values
used to wait for a short, medium and long TPM command. All
TPM commands are categorized as short, medium or long in
execution time, so that the driver doesn't have to wait
any longer than necessary before starting to poll for a
result.

Example output:

```
3015000 4508000 180995000 [original]
```

Here the short, medium and long durations are displayed in
usecs. "[original]" indicates that the values are displayed
unmodified from when they were queried from the chip.
Durations can be modified in the case where a buggy chip
reports them in msec instead of usec and they need to be
scaled to be displayed in usecs. In this case "[adjusted]"
will be displayed in place of "[original]".

|  |
| --- |
| **/sys/class/tpm/tpmX/device/enabled** |

Defined on file [sysfs-class-tpm](abi-stable.md#abi-file-stable-sysfs-class-tpm)

The "enabled" property prints a '1' if the TPM chip is enabled,
meaning that it should be visible to the OS. This property
may be visible but produce a '0' after some operation that
disables the TPM.

|  |
| --- |
| **/sys/class/tpm/tpmX/device/owned** |

Defined on file [sysfs-class-tpm](abi-stable.md#abi-file-stable-sysfs-class-tpm)

The "owned" property produces a '1' if the TPM_TakeOwnership
ordinal has been executed successfully in the chip. A '0'
indicates that ownership hasn't been taken.

|  |
| --- |
| **/sys/class/tpm/tpmX/device/pcrs** |

Defined on file [sysfs-class-tpm](abi-stable.md#abi-file-stable-sysfs-class-tpm)

The "pcrs" property will dump the current value of all Platform
Configuration Registers in the TPM. Note that since these
values may be constantly changing, the output is only valid
for a snapshot in time.

Example output:

```
PCR-00: 3A 3F 78 0F 11 A4 B4 99 69 FC AA 80 CD 6E 39 57 C3 3B 22 75
PCR-01: 3A 3F 78 0F 11 A4 B4 99 69 FC AA 80 CD 6E 39 57 C3 3B 22 75
PCR-02: 3A 3F 78 0F 11 A4 B4 99 69 FC AA 80 CD 6E 39 57 C3 3B 22 75
PCR-03: 3A 3F 78 0F 11 A4 B4 99 69 FC AA 80 CD 6E 39 57 C3 3B 22 75
PCR-04: 3A 3F 78 0F 11 A4 B4 99 69 FC AA 80 CD 6E 39 57 C3 3B 22 75
...
```

The number of PCRs and hex bytes needed to represent a PCR
value will vary depending on TPM chip version. For TPM 1.1 and
1.2 chips, PCRs represent SHA-1 hashes, which are 20 bytes
long. Use the "caps" property to determine TPM version.

|  |
| --- |
| **/sys/class/tpm/tpmX/device/pubek** |

Defined on file [sysfs-class-tpm](abi-stable.md#abi-file-stable-sysfs-class-tpm)

The "pubek" property will return the TPM's public endorsement
key if possible. If the TPM has had ownership established and
is version 1.2, the pubek will not be available without the
owner's authorization. Since the TPM driver doesn't store any
secrets, it can't authorize its own request for the pubek,
making it unaccessible. The public endorsement key is gener-
ated at TPM manufacture time and exists for the life of the
chip.

Example output:

```
Algorithm: 00 00 00 01
Encscheme: 00 03
Sigscheme: 00 01
Parameters: 00 00 08 00 00 00 00 02 00 00 00 00
Modulus length: 256
Modulus:
B4 76 41 82 C9 20 2C 10 18 40 BC 8B E5 44 4C 6C
3A B2 92 0C A4 9B 2A 83 EB 5C 12 85 04 48 A0 B6
1E E4 81 84 CE B2 F2 45 1C F0 85 99 61 02 4D EB
86 C4 F7 F3 29 60 52 93 6B B2 E5 AB 8B A9 09 E3
D7 0E 7D CA 41 BF 43 07 65 86 3C 8C 13 7A D0 8B
82 5E 96 0B F8 1F 5F 34 06 DA A2 52 C1 A9 D5 26
0F F4 04 4B D9 3F 2D F2 AC 2F 74 64 1F 8B CD 3E
1E 30 38 6C 70 63 69 AB E2 50 DF 49 05 2E E1 8D
6F 78 44 DA 57 43 69 EE 76 6C 38 8A E9 8E A3 F0
A7 1F 3C A8 D0 12 15 3E CA 0E BD FA 24 CD 33 C6
47 AE A4 18 83 8E 22 39 75 93 86 E6 FD 66 48 B6
10 AD 94 14 65 F9 6A 17 78 BD 16 53 84 30 BF 70
E0 DC 65 FD 3C C6 B0 1E BF B9 C1 B5 6C EF B1 3A
F8 28 05 83 62 26 11 DC B4 6B 5A 97 FF 32 26 B6
F7 02 71 CF 15 AE 16 DD D1 C1 8E A8 CF 9B 50 7B
C3 91 FF 44 1E CF 7C 39 FE 17 77 21 20 BD CE 9B
```

Possible values:

```
Algorithm:    TPM_ALG_RSA                     (1)
Encscheme:    TPM_ES_RSAESPKCSv15             (2)
              TPM_ES_RSAESOAEP_SHA1_MGF1      (3)
Sigscheme:    TPM_SS_NONE                     (1)
Parameters, a byte string of 3 u32 values:
      Key Length (bits):      00 00 08 00     (2048)
      Num primes:             00 00 00 02     (2)
      Exponent Size:          00 00 00 00     (0 means the
                                               default exp)
Modulus Length: 256 (bytes)
Modulus:      The 256 byte Endorsement Key modulus
```

|  |
| --- |
| **/sys/class/tpm/tpmX/device/temp_deactivated** |

Defined on file [sysfs-class-tpm](abi-stable.md#abi-file-stable-sysfs-class-tpm)

The "temp_deactivated" property returns a '1' if the chip has
been temporarily deactivated, usually until the next power
cycle. Whether a warm boot (reboot) will clear a TPM chip
from a temp_deactivated state is platform specific.

|  |
| --- |
| **/sys/class/tpm/tpmX/device/timeouts** |

Defined on file [sysfs-class-tpm](abi-stable.md#abi-file-stable-sysfs-class-tpm)

The "timeouts" property shows the 4 vendor-specific values
for the TPM's interface spec timeouts. The use of these
timeouts is defined by the TPM interface spec that the chip
conforms to.

Example output:

```
750000 750000 750000 750000 [original]
```

The four timeout values are shown in usecs, with a trailing
"[original]" or "[adjusted]" depending on whether the values
were scaled by the driver to be reported in usec from msecs.

|  |
| --- |
| **/sys/class/tpm/tpmX/pcr-<H>/<N>** |

Defined on file [sysfs-class-tpm](abi-stable.md#abi-file-stable-sysfs-class-tpm)

produces output in compact hex representation for PCR
number N from hash bank H. N is the numeric value of
the PCR number and H is the crypto string
representation of the hash

Example output:

```
cat /sys/class/tpm/tpm0/pcr-sha256/7
2ED93F199692DC6788EFA6A1FE74514AB9760B2A6CEEAEF6C808C13E4ABB0D42
```

|  |
| --- |
| **/sys/class/tpm/tpmX/tpm_version_major** |

Defined on file [sysfs-class-tpm](abi-stable.md#abi-file-stable-sysfs-class-tpm)

The "tpm_version_major" property shows the TCG spec major version
implemented by the TPM device.

Example output:

```
2
```

|  |
| --- |
| **/sys/class/ubi/** |

Defined on file [sysfs-class-ubi](abi-stable.md#abi-file-stable-sysfs-class-ubi)

The ubi/ class sub-directory belongs to the UBI subsystem and
provides general UBI information, per-UBI device information
and per-UBI volume information.

|  |
| --- |
| **/sys/class/ubi/ubiX/avail_eraseblocks** |

Defined on file [sysfs-class-ubi](abi-stable.md#abi-file-stable-sysfs-class-ubi)

Amount of available logical eraseblock. For example, one may
create a new UBI volume which has this amount of logical
eraseblocks.

|  |
| --- |
| **/sys/class/ubi/ubiX/bad_peb_count** |

Defined on file [sysfs-class-ubi](abi-stable.md#abi-file-stable-sysfs-class-ubi)

Count of bad physical eraseblocks on the underlying MTD device.

|  |
| --- |
| **/sys/class/ubi/ubiX/bgt_enabled** |

Defined on file [sysfs-class-ubi](abi-stable.md#abi-file-stable-sysfs-class-ubi)

Contains ASCII "0n" if the UBI background thread is disabled,
and ASCII "1n" if it is enabled.

|  |
| --- |
| **/sys/class/ubi/ubiX/dev** |

Defined on file [sysfs-class-ubi](abi-stable.md#abi-file-stable-sysfs-class-ubi)

Major and minor numbers of the character device corresponding
to this UBI device (in <major>:<minor> format).

|  |
| --- |
| **/sys/class/ubi/ubiX/eraseblock_size** |

Defined on file [sysfs-class-ubi](abi-stable.md#abi-file-stable-sysfs-class-ubi)

Maximum logical eraseblock size this UBI device may provide. UBI
volumes may have smaller logical eraseblock size because of their
alignment.

|  |
| --- |
| **/sys/class/ubi/ubiX/max_ec** |

Defined on file [sysfs-class-ubi](abi-stable.md#abi-file-stable-sysfs-class-ubi)

Maximum physical eraseblock erase counter value.

|  |
| --- |
| **/sys/class/ubi/ubiX/max_vol_count** |

Defined on file [sysfs-class-ubi](abi-stable.md#abi-file-stable-sysfs-class-ubi)

Maximum number of volumes which this UBI device may have.

|  |
| --- |
| **/sys/class/ubi/ubiX/min_io_size** |

Defined on file [sysfs-class-ubi](abi-stable.md#abi-file-stable-sysfs-class-ubi)

Minimum input/output unit size. All the I/O may only be done
in fractions of the contained number.

|  |
| --- |
| **/sys/class/ubi/ubiX/mtd_num** |

Defined on file [sysfs-class-ubi](abi-stable.md#abi-file-stable-sysfs-class-ubi)

Number of the underlying MTD device.

|  |
| --- |
| **/sys/class/ubi/ubiX/reserved_for_bad** |

Defined on file [sysfs-class-ubi](abi-stable.md#abi-file-stable-sysfs-class-ubi)

Number of physical eraseblocks reserved for bad block handling.

|  |
| --- |
| **/sys/class/ubi/ubiX/ro_mode** |

Defined on file [sysfs-class-ubi](abi-stable.md#abi-file-stable-sysfs-class-ubi)

Contains ASCII "1n" if the read-only flag is set on this
device, and "0n" if it is cleared. UBI devices mark themselves
as read-only when they detect an unrecoverable error.

|  |
| --- |
| **/sys/class/ubi/ubiX/total_eraseblocks** |

Defined on file [sysfs-class-ubi](abi-stable.md#abi-file-stable-sysfs-class-ubi)

Total number of good (not marked as bad) physical eraseblocks on
the underlying MTD device.

|  |
| --- |
| **/sys/class/ubi/ubiX/ubiX_Y/** |

Defined on file [sysfs-class-ubi](abi-stable.md#abi-file-stable-sysfs-class-ubi)

The /sys/class/ubi/ubiX/ubiX_0/, /sys/class/ubi/ubiX/ubiX_1/,
etc directories describe UBI volumes on UBI device X (volumes
0, 1, etc).

|  |
| --- |
| **/sys/class/ubi/ubiX/ubiX_Y/alignment** |

Defined on file [sysfs-class-ubi](abi-stable.md#abi-file-stable-sysfs-class-ubi)

Volume alignment - the value the logical eraseblock size of
this volume has to be aligned on. For example, 2048 means that
logical eraseblock size is multiple of 2048. In other words,
volume logical eraseblock size is UBI device logical eraseblock
size aligned to the alignment value.

|  |
| --- |
| **/sys/class/ubi/ubiX/ubiX_Y/corrupted** |

Defined on file [sysfs-class-ubi](abi-stable.md#abi-file-stable-sysfs-class-ubi)

Contains ASCII "0n" if the UBI volume is OK, and ASCII "1n"
if it is corrupted (e.g., due to an interrupted volume update).

|  |
| --- |
| **/sys/class/ubi/ubiX/ubiX_Y/data_bytes** |

Defined on file [sysfs-class-ubi](abi-stable.md#abi-file-stable-sysfs-class-ubi)

The amount of data this volume contains. This value makes sense
only for static volumes, and for dynamic volume it equivalent
to the total volume size in bytes.

|  |
| --- |
| **/sys/class/ubi/ubiX/ubiX_Y/dev** |

Defined on file [sysfs-class-ubi](abi-stable.md#abi-file-stable-sysfs-class-ubi)

Major and minor numbers of the character device corresponding
to this UBI volume (in <major>:<minor> format).

|  |
| --- |
| **/sys/class/ubi/ubiX/ubiX_Y/name** |

Defined on file [sysfs-class-ubi](abi-stable.md#abi-file-stable-sysfs-class-ubi)

Volume name.

|  |
| --- |
| **/sys/class/ubi/ubiX/ubiX_Y/reserved_ebs** |

Defined on file [sysfs-class-ubi](abi-stable.md#abi-file-stable-sysfs-class-ubi)

Count of physical eraseblock reserved for this volume.
Equivalent to the volume size in logical eraseblocks.

|  |
| --- |
| **/sys/class/ubi/ubiX/ubiX_Y/type** |

Defined on file [sysfs-class-ubi](abi-stable.md#abi-file-stable-sysfs-class-ubi)

Volume type. Contains ASCII "dynamicn" for dynamic volumes and
"staticn" for static volumes.

|  |
| --- |
| **/sys/class/ubi/ubiX/ubiX_Y/upd_marker** |

Defined on file [sysfs-class-ubi](abi-stable.md#abi-file-stable-sysfs-class-ubi)

Contains ASCII "0n" if the update marker is not set for this
volume, and "1n" if it is set. The update marker is set when
volume update starts, and cleaned when it ends. So the presence
of the update marker indicates that the volume is being updated
at the moment of the update was interrupted. The later may be
checked using the "corrupted" sysfs file.

|  |
| --- |
| **/sys/class/ubi/ubiX/ubiX_Y/usable_eb_size** |

Defined on file [sysfs-class-ubi](abi-stable.md#abi-file-stable-sysfs-class-ubi)

Logical eraseblock size of this volume. Equivalent to logical
eraseblock size of the device aligned on the volume alignment
value.

|  |
| --- |
| **/sys/class/ubi/ubiX/volumes_count** |

Defined on file [sysfs-class-ubi](abi-stable.md#abi-file-stable-sysfs-class-ubi)

Count of volumes on this UBI device.

|  |
| --- |
| **/sys/class/ubi/version** |

Defined on file [sysfs-class-ubi](abi-stable.md#abi-file-stable-sysfs-class-ubi)

This file contains version of the latest supported UBI on-media
format. Currently it is 1, and there is no plan to change this.
However, if in the future UBI needs on-flash format changes
which cannot be done in a compatible manner, a new format
version will be added. So this is a mechanism for possible
future backward-compatible (but forward-incompatible)
improvements.

|  |
| --- |
| **/sys/class/ubiX/** |

Defined on file [sysfs-class-ubi](abi-stable.md#abi-file-stable-sysfs-class-ubi)

The /sys/class/ubi0, /sys/class/ubi1, etc directories describe
UBI devices (UBI device 0, 1, etc). They contain general UBI
device information and per UBI volume information (each UBI
device may have many UBI volumes)

|  |
| --- |
| **/sys/class/udc/<udc>/a_alt_hnp_support** |

Defined on file [sysfs-class-udc](abi-stable.md#abi-file-stable-sysfs-class-udc)

Indicates if an OTG A-Host supports HNP at an alternate port.

|  |
| --- |
| **/sys/class/udc/<udc>/a_hnp_support** |

Defined on file [sysfs-class-udc](abi-stable.md#abi-file-stable-sysfs-class-udc)

Indicates if an OTG A-Host supports HNP at this port.

|  |
| --- |
| **/sys/class/udc/<udc>/b_hnp_enable** |

Defined on file [sysfs-class-udc](abi-stable.md#abi-file-stable-sysfs-class-udc)

Indicates if an OTG A-Host enabled HNP support.

|  |
| --- |
| **/sys/class/udc/<udc>/current_speed** |

Defined on file [sysfs-class-udc](abi-stable.md#abi-file-stable-sysfs-class-udc)

Indicates the current negotiated speed at this port.

|  |
| --- |
| **/sys/class/udc/<udc>/function** |

Defined on file [sysfs-class-udc](abi-stable.md#abi-file-stable-sysfs-class-udc)

Prints out name of currently running USB Gadget Driver.

|  |
| --- |
| **/sys/class/udc/<udc>/is_a_peripheral** |

Defined on file [sysfs-class-udc](abi-stable.md#abi-file-stable-sysfs-class-udc)

Indicates that this port is the default Host on an OTG session
but HNP was used to switch roles.

|  |
| --- |
| **/sys/class/udc/<udc>/is_otg** |

Defined on file [sysfs-class-udc](abi-stable.md#abi-file-stable-sysfs-class-udc)

Indicates that this port support OTG.

|  |
| --- |
| **/sys/class/udc/<udc>/maximum_speed** |

Defined on file [sysfs-class-udc](abi-stable.md#abi-file-stable-sysfs-class-udc)

Indicates the maximum USB speed supported by this port.

|  |
| --- |
| **/sys/class/udc/<udc>/soft_connect** |

Defined on file [sysfs-class-udc](abi-stable.md#abi-file-stable-sysfs-class-udc)

Allows users to disconnect data pullup resistors thus causing a
logical disconnection from the USB Host.

|  |
| --- |
| **/sys/class/udc/<udc>/srp** |

Defined on file [sysfs-class-udc](abi-stable.md#abi-file-stable-sysfs-class-udc)

Allows users to manually start Session Request Protocol.

|  |
| --- |
| **/sys/class/udc/<udc>/state** |

Defined on file [sysfs-class-udc](abi-stable.md#abi-file-stable-sysfs-class-udc)

Indicates current state of the USB Device Controller. Valid
states are: 'not-attached', 'attached', 'powered',
'reconnecting', 'unauthenticated', 'default', 'addressed',
'configured', and 'suspended'; however not all USB Device
Controllers support reporting all states.

## Symbols under /sys/devices

|  |
| --- |
| **/sys/devices/\*/dev** |

Defined on file [sysfs-devices](abi-stable.md#abi-file-stable-sysfs-devices)

Major and minor numbers of the character device corresponding
to the device (in <major>:<minor> format).

|  |
| --- |
| **/sys/devices/\*/devspec** |

Defined on file [sysfs-devices](abi-stable.md#abi-file-stable-sysfs-devices)

If CONFIG_OF is enabled, then this file is present. When
read, it returns full name of the device node.

|  |
| --- |
| **/sys/devices/\*/obppath** |

Defined on file [sysfs-devices](abi-stable.md#abi-file-stable-sysfs-devices)

If CONFIG_OF is enabled, then this file is present. When
read, it returns full name of the device node.

|  |
| --- |
| **/sys/devices/\*/of_node** |

Defined on file [sysfs-devices](abi-stable.md#abi-file-stable-sysfs-devices)

Any device associated with a device-tree node will have
an of_path symlink pointing to the corresponding device
node in /sys/firmware/devicetree/

|  |
| --- |
| **/sys/devices/pciXXXX:XX/0000:XX:XX.X/dma/dma<n>chan<n>/quickdata/cap** |

Defined on file [sysfs-driver-dma-ioatdma](abi-stable.md#abi-file-stable-sysfs-driver-dma-ioatdma)

Capabilities the DMA supports.Currently there are DMA_PQ, DMA_PQ_VAL,
DMA_XOR,DMA_XOR_VAL,DMA_INTERRUPT.

|  |
| --- |
| **/sys/devices/pciXXXX:XX/0000:XX:XX.X/dma/dma<n>chan<n>/quickdata/intr_coalesce** |

Defined on file [sysfs-driver-dma-ioatdma](abi-stable.md#abi-file-stable-sysfs-driver-dma-ioatdma)

Tune-able interrupt delay value per channel basis.

|  |
| --- |
| **/sys/devices/pciXXXX:XX/0000:XX:XX.X/dma/dma<n>chan<n>/quickdata/ring_active** |

Defined on file [sysfs-driver-dma-ioatdma](abi-stable.md#abi-file-stable-sysfs-driver-dma-ioatdma)

The number of descriptors active in the ring.

|  |
| --- |
| **/sys/devices/pciXXXX:XX/0000:XX:XX.X/dma/dma<n>chan<n>/quickdata/ring_size** |

Defined on file [sysfs-driver-dma-ioatdma](abi-stable.md#abi-file-stable-sysfs-driver-dma-ioatdma)

Descriptor ring size, total number of descriptors available.

|  |
| --- |
| **/sys/devices/pciXXXX:XX/0000:XX:XX.X/dma/dma<n>chan<n>/quickdata/version** |

Defined on file [sysfs-driver-dma-ioatdma](abi-stable.md#abi-file-stable-sysfs-driver-dma-ioatdma)

Version of ioatdma device.

|  |
| --- |
| **/sys/devices/platform/firmware\:zynqmp-firmware/feature_config_id** |

Defined on file [sysfs-driver-firmware-zynqmp](abi-stable.md#abi-file-stable-sysfs-driver-firmware-zynqmp)

This sysfs interface allows user to configure features at
runtime. The user can enable or disable features running at
firmware as well as the user can configure the parameters of
the features at runtime. The supported features are over
temperature and external watchdog. Here, the external watchdog
is completely different than the /dev/watchdog as the external
watchdog is running on the firmware and it is used to monitor
the health of firmware not APU(Linux). Also, the external
watchdog is interfaced outside of the zynqmp soc.

The supported config ids are for the feature configuration is,
1. PM_FEATURE_OVERTEMP_STATUS = 1, the user can enable or
disable the over temperature feature.
2. PM_FEATURE_OVERTEMP_VALUE = 2, the user can configure the
over temperature limit in Degree Celsius.
3. PM_FEATURE_EXTWDT_STATUS = 3, the user can enable or disable
the external watchdog feature.
4. PM_FEATURE_EXTWDT_VALUE = 4, the user can configure the
external watchdog feature.

Usage:

Select over temperature config ID to enable/disable feature
# echo 1 > /sys/devices/platform/firmware:zynqmp-firmware/feature_config_id

Check over temperature config ID is selected or not
# cat /sys/devices/platform/firmware:zynqmp-firmware/feature_config_id
The expected result is 1.

Select over temperature config ID to configure OT limit
# echo 2 > /sys/devices/platform/firmware:zynqmp-firmware/feature_config_id

Check over temperature config ID is selected or not
# cat /sys/devices/platform/firmware:zynqmp-firmware/feature_config_id
The expected result is 2.

Select external watchdog config ID to enable/disable feature
# echo 3 > /sys/devices/platform/firmware:zynqmp-firmware/feature_config_id

Check external watchdog config ID is selected or not
# cat /sys/devices/platform/firmware:zynqmp-firmware/feature_config_id
The expected result is 3.

Select external watchdog config ID to configure time interval
# echo 4 > /sys/devices/platform/firmware:zynqmp-firmware/feature_config_id

Check external watchdog config ID is selected or not
# cat /sys/devices/platform/firmware:zynqmp-firmware/feature_config_id
The expected result is 4.

Users:
Xilinx

|  |
| --- |
| **/sys/devices/platform/firmware\:zynqmp-firmware/feature_config_value** |

Defined on file [sysfs-driver-firmware-zynqmp](abi-stable.md#abi-file-stable-sysfs-driver-firmware-zynqmp)

This sysfs interface allows to configure features at runtime.
The user can enable or disable features running at firmware.
Also, the user can configure the parameters of the features
at runtime. The supported features are over temperature and
external watchdog. Here, the external watchdog is completely
different than the /dev/watchdog as the external watchdog is
running on the firmware and it is used to monitor the health
of firmware not APU(Linux). Also, the external watchdog is
interfaced outside of the zynqmp soc.

By default the features are disabled in the firmware. The user
can enable features by querying appropriate config id of the
features.

The default limit for the over temperature is 90 Degree Celsius.
The default timer interval for the external watchdog is 570ms.

The supported config ids are for the feature configuration is,
1. PM_FEATURE_OVERTEMP_STATUS = 1, the user can enable or
disable the over temperature feature.
2. PM_FEATURE_OVERTEMP_VALUE = 2, the user can configure the
over temperature limit in Degree Celsius.
3. PM_FEATURE_EXTWDT_STATUS = 3, the user can enable or disable
the external watchdog feature.
4. PM_FEATURE_EXTWDT_VALUE = 4, the user can configure the
external watchdog feature.

Usage:

Enable over temperature feature
# echo 1 > /sys/devices/platform/firmware:zynqmp-firmware/feature_config_id
# echo 1 > /sys/devices/platform/firmware:zynqmp-firmware/feature_config_value

Check whether the over temperature feature is enabled or not
# cat /sys/devices/platform/firmware:zynqmp-firmware/feature_config_value
The expected result is 1.

Disable over temperature feature
# echo 1 > /sys/devices/platform/firmware:zynqmp-firmware/feature_config_id
# echo 0 > /sys/devices/platform/firmware:zynqmp-firmware/feature_config_value

Check whether the over temperature feature is disabled or not
# cat /sys/devices/platform/firmware:zynqmp-firmware/feature_config_value
The expected result is 0.

Configure over temperature limit to 50 Degree Celsius
# echo 2 > /sys/devices/platform/firmware:zynqmp-firmware/feature_config_id
# echo 50 > /sys/devices/platform/firmware:zynqmp-firmware/feature_config_value

Check whether the over temperature limit is configured or not
# cat /sys/devices/platform/firmware:zynqmp-firmware/feature_config_value
The expected result is 50.

Enable external watchdog feature
# echo 3 > /sys/devices/platform/firmware:zynqmp-firmware/feature_config_id
# echo 1 > /sys/devices/platform/firmware:zynqmp-firmware/feature_config_value

Check whether the external watchdog feature is enabled or not
# cat /sys/devices/platform/firmware:zynqmp-firmware/feature_config_value
The expected result is 1.

Disable external watchdog feature
# echo 3 > /sys/devices/platform/firmware:zynqmp-firmware/feature_config_id
# echo 0 > /sys/devices/platform/firmware:zynqmp-firmware/feature_config_value

Check whether the external watchdog feature is disabled or not
# cat /sys/devices/platform/firmware:zynqmp-firmware/feature_config_value
The expected result is 0.

Configure external watchdog timer interval to 500ms
# echo 4 > /sys/devices/platform/firmware:zynqmp-firmware/feature_config_id
# echo 500 > /sys/devices/platform/firmware:zynqmp-firmware/feature_config_value

Check whether the external watchdog timer interval is configured or not
# cat /sys/devices/platform/firmware:zynqmp-firmware/feature_config_value
The expected result is 500.

Users:
Xilinx

|  |
| --- |
| **/sys/devices/platform/firmware\:zynqmp-firmware/ggs\*** |

Defined on file [sysfs-driver-firmware-zynqmp](abi-stable.md#abi-file-stable-sysfs-driver-firmware-zynqmp)

Read/Write PMU global general storage register value,
GLOBAL_GEN_STORAGE{0:3}.
Global general storage register that can be used
by system to pass information between masters.

The register is reset during system or power-on
resets. Three registers are used by the FSBL and
other Xilinx software products: GLOBAL_GEN_STORAGE{4:6}.

Usage:

```
# cat /sys/devices/platform/firmware\:zynqmp-firmware/ggs0
# echo <value> > /sys/devices/platform/firmware\:zynqmp-firmware/ggs0
```

Example:

```
# cat /sys/devices/platform/firmware\:zynqmp-firmware/ggs0
# echo 0x1234ABCD > /sys/devices/platform/firmware\:zynqmp-firmware/ggs0
```

Users:
Xilinx

|  |
| --- |
| **/sys/devices/platform/firmware\:zynqmp-firmware/health_status** |

Defined on file [sysfs-driver-firmware-zynqmp](abi-stable.md#abi-file-stable-sysfs-driver-firmware-zynqmp)

This sysfs interface allows to set the health status. If PMUFW
is compiled with CHECK_HEALTHY_BOOT, it will check the healthy
bit on FPD WDT expiration. If healthy bit is set by a user
application running in Linux, PMUFW will do APU only restart. If
healthy bit is not set during FPD WDT expiration, PMUFW will do
system restart.

Usage:

Set healthy bit:

```
# echo 1 > /sys/devices/platform/firmware\:zynqmp-firmware/health_status
```

Unset healthy bit:

```
# echo 0 > /sys/devices/platform/firmware\:zynqmp-firmware/health_status
```

Users:
Xilinx

|  |
| --- |
| **/sys/devices/platform/firmware\:zynqmp-firmware/pggs\*** |

Defined on file [sysfs-driver-firmware-zynqmp](abi-stable.md#abi-file-stable-sysfs-driver-firmware-zynqmp)

Read/Write PMU persistent global general storage register
value, PERS_GLOB_GEN_STORAGE{0:3}.
Persistent global general storage register that
can be used by system to pass information between
masters.

This register is only reset by the power-on reset
and maintains its value through a system reset.
Four registers are used by the FSBL and other Xilinx
software products: PERS_GLOB_GEN_STORAGE{4:7}.
Register is reset only by a POR reset.

Usage:

```
# cat /sys/devices/platform/firmware\:zynqmp-firmware/pggs0
# echo <value> > /sys/devices/platform/firmware\:zynqmp-firmware/pggs0
```

Example:

```
# cat /sys/devices/platform/firmware\:zynqmp-firmware/pggs0
# echo 0x1234ABCD > /sys/devices/platform/firmware\:zynqmp-firmware/pggs0
```

Users:
Xilinx

|  |
| --- |
| **/sys/devices/platform/firmware\:zynqmp-firmware/shutdown_scope** |

Defined on file [sysfs-driver-firmware-zynqmp](abi-stable.md#abi-file-stable-sysfs-driver-firmware-zynqmp)

This sysfs interface allows to set the shutdown scope for the
next shutdown request. When the next shutdown is performed, the
platform specific portion of PSCI-system_off can use the chosen
shutdown scope.

Following are available shutdown scopes(subtypes):

subsystem:
:   Only the APU along with all of its peripherals
    not used by other processing units will be
    shut down. This may result in the FPD power
    domain being shut down provided that no other
    processing unit uses FPD peripherals or DRAM.

ps_only:
:   The complete PS will be shut down, including the
    RPU, PMU, etc. Only the PL domain (FPGA)
    remains untouched.

system:
:   The complete system/device is shut down.

Usage:

```
# cat /sys/devices/platform/firmware\:zynqmp-firmware/shutdown_scope
# echo <scope> > /sys/devices/platform/firmware\:zynqmp-firmware/shutdown_scope
```

Example:

```
# cat /sys/devices/platform/firmware\:zynqmp-firmware/shutdown_scope
# echo "subsystem" > /sys/devices/platform/firmware\:zynqmp-firmware/shutdown_scope
```

Users:
Xilinx

|  |
| --- |
| **/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/agb_spi_burn_en** |
| **/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/fpga_spi_burn_en** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

These files allow gearboxes and FPGA SPI flash burning.
The attributes are set 1 to enable burning, 0 - to disable.
If the system is in locked-down mode writing these files will
not be allowed.
The purpose of these files to allow line card Gearboxes and FPGA
burning during production flow.

The file is read/write.

|  |
| --- |
| **/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/cpld1_pn** |
| **/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/cpld1_version** |
| **/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/cpld1_version_min** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

These files show with which CPLD major and minor versions
and part number has been burned CPLD device on line card.

The files are read only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/cpld_upgrade_en** |
| **/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/fpga_upgrade_en** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

These files allow CPLD and FPGA burning. Value 1 in file means burning
is enabled, 0 - otherwise.
If the system is in locked-down mode writing these files will
not be allowed.
The purpose of these files to allow line card CPLD and FPGA
upgrade through the JTAG daisy-chain.

The files are read/write.

|  |
| --- |
| **/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/fpga1_pn** |
| **/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/fpga1_version** |
| **/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/fpga1_version_min** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

These files show with which FPGA major and minor versions
and part number has been burned FPGA device on line card.

The files are read only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/max_power** |
| **/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/config** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

These files provide the maximum powered required for line card
feeding and line card configuration Id.

The files are read only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/qsfp_pwr_en** |
| **/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/pwr_en** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

These files allow to power on/off all QSFP ports and whole line card.
The attributes are set 1 for power on, 0 - for power off.

The files are read/write.

|  |
| --- |
| **/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/reset_aux_pwr_or_ref** |
| **/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/reset_dc_dc_pwr_fail** |
| **/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/reset_fpga_not_done** |
| **/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/reset_from_chassis** |
| **/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/reset_line_card** |
| **/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/reset_pwr_off_from_chassis** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

These files show the line reset cause, as following: power
auxiliary outage or power refresh, DC-to-DC power failure, FPGA reset
failed, line card reset failed, power off from chassis.
Value 1 in file means this is reset cause, 0 - otherwise. Only one of
the above causes could be 1 at the same time, representing only last
reset cause.

The files are read only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/vpd_wp** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

This file allow to overwrite line card VPD hardware write
protection mode. When attribute is set 1 - write protection is
disabled, when 0 - enabled.
Default is 0.
If the system is in locked-down mode writing this file will not
be allowed.
The purpose if this file is to allow line card VPD burning
during production flow.

The file is read/write.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/asic2_health** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

This file shows 2-nd ASIC health status. The possible values are:
0 - health failed, 2 - health OK, 3 - ASIC in booting state.

The file is read only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/asic_health** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

This file shows ASIC health status. The possible values are:
0 - health failed, 2 - health OK, 3 - ASIC in booting state.

The files are read only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/asic_pg_fail** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

This file shows ASIC Power Good status.
Value 1 in file means ASIC Power Good failed, 0 - otherwise.

The file is read only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/asic_reset** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/asic2_reset** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

These files allow to each of ASICs by writing 1.

The files are write only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/bios_active_image** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/bios_auth_fail** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/bios_upgrade_fail** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

The files represent BIOS statuses:

bios_active_image: location of current active BIOS image:
0: Top, 1: Bottom.
The reported value should correspond to value expected by OS
in case of BIOS safe mode is 0. This bit is related to Intel
top-swap feature of DualBios on the same flash.

bios_auth_fail: BIOS upgrade is failed because provided BIOS
image is not signed correctly.

bios_upgrade_fail: BIOS upgrade is failed by some other
reason not because authentication. For example due to
physical SPI flash problem.

The files are read only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/clk_brd1_boot_fail** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/clk_brd2_boot_fail** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/clk_brd_fail** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

These files are related to clock boards status in system.
- clk_brd1_boot_fail: warning about 1-st clock board failed to boot from CI.
- clk_brd2_boot_fail: warning about 2-nd clock board failed to boot from CI.
- clk_brd_fail: error about common clock board boot failure.

The files are read only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/clk_brd_prog_en** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

This file enables programming of clock boards.
Default is 0 (programming disabled).
If the system is in locked-down mode writing this file will not be allowed.

The file is read/write.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/comm_chnl_ready** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

This file is used to indicate remote end (for example BMC) that system
host CPU is ready for sending telemetry data to remote end.
For indication the file should be written 1.

The file is write only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/config1** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/config2** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

These files show system static topology identification
like system's static I2C topology, number and type of FPGA
devices within the system and so on.

The files are read only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/config3** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

The file indicates COME module hardware configuration.
The value is pushed by hardware through GPIO pins.
The purpose is to expose some minor BOM changes for the same system SKU.

The file is read only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld1_pn** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld2_pn** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld3_pn** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld4_pn** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld1_version_min** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld2_version_min** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld3_version_min** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld4_version_min** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

These files show with which CPLD part numbers and minor
versions have been burned CPLD devices equipped on a
system.

The files are read only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld1_version** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld2_version** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

These files show with which CPLD versions have been burned
on carrier and switch boards.

The files are read only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld3_version** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

These files show with which CPLD versions have been burned
on LED or Gearbox board.

The files are read only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld4_version** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

These files show with which CPLD versions have been burned
on LED board.

The files are read only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld5_pn** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld5_version** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld5_version_min** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

These files show with which CPLD part numbers, version and minor
versions have been burned the 5-th CPLD device equipped on a
system.

The files are read only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/erot1_ap_reset** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/erot2_ap_reset** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

These files aim to monitor the status of the External Root of Trust (EROT)
processor's RESET output to the Application Processor (AP).
By reading this file, could be determined if the EROT has invalidated or
revoked AP Firmware, at which point it will hold the AP in RESET until a
valid firmware is loaded. This protects the AP from running an
unauthorized firmware. In the normal flow, the AP reset should be released
after the EROT validates the integrity of the FW, and it should be done so
as quickly as possible so that the AP boots before the CPU starts to
communicate to each ASIC.

The files are read only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/erot1_recovery** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/erot2_recovery** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/erot1_reset** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/erot2_reset** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

These files aim to perform External Root of Trust (EROT) recovery
sequence after EROT device failure.
These EROT devices protect ASICs from unauthorized access and in normal
flow their reset should be released with system power – earliest power
up stage, so that EROTs can begin boot and authentication process before
CPU starts to communicate to ASICs.
Issuing a reset to the EROT while asserting the recovery signal will cause
the EROT Application Processor to enter recovery mode so that the EROT FW
can be updated/recovered.
For reset/recovery the related file should be toggled by 1/0.

The files are read/write.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/erot1_wp** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/erot2_wp** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

These files allow access to External Root of Trust (EROT) for reset
and recovery sequence after EROT device failure.
Default is 0 (programming disabled).
If the system is in locked-down mode writing this file will not be allowed.

The files are read/write.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/fan_dir** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

This file shows the system fans direction:
forward direction - relevant bit is set 0;
reversed direction - relevant bit is set 1.

The files are read only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/jtag_cap** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

This file indicates the available method of CPLD/FPGA devices
field update through the JTAG chain:

b00 - field update through LPC bus register memory space.
b01 - Reserved.
b10 - Reserved.
b11 - field update through CPU GPIOs bit-banging.

The file is read only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/jtag_enable** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

These files enable and disable the access to the JTAG domain.
By default access to the JTAG domain is disabled.

The file is read/write.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc1_enable** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc2_enable** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc3_enable** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc4_enable** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc5_enable** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc6_enable** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc7_enable** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc8_enable** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

These files allow line cards enable state control.
Expected behavior:
When lc{n}_enable is written 1, related line card is released
from the reset state, when 0 - is hold in reset state.

The files are read/write.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc1_pwr** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc2_pwr** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc3_pwr** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc4_pwr** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc5_pwr** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc6_pwr** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc7_pwr** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc8_pwr** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

These files switching line cards power on and off.
Expected behavior:
When lc{n}_pwr is written 1, related line card is powered
on, when written 0 - powered off.

The files are read/write.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc1_rst_mask** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc2_rst_mask** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc3_rst_mask** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc4_rst_mask** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc5_rst_mask** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc6_rst_mask** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc7_rst_mask** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc8_rst_mask** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

These files clear line card reset bit enforced by ASIC, when it
sets it due to some abnormal ASIC behavior.
Expected behavior:
When lc{n}_rst_mask is written 1, related line card reset bit
is cleared, when written 0 - no effect.

The files are write only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lid_open** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

1 - indicates that system lid is opened, otherwise 0.

The file is read only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/mac_reset** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

This file allows to reset ASIC MT52132 when attribute is set 0
due to some abnormal ASIC behavior.
Expected behavior:
When mac_reset is written 1, the ASIC MT52132 is released
from the reset state, when 0 - is hold in reset state.

The files are read/write.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/os_started** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

This file, when written 1, indicates to programmable devices
that OS is taking control over it.

The file is read/write.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/pcie_asic_reset_dis** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

This file allows to retain ASIC up during PCIe root complex
reset, when attribute is set 1.

The file is read/write.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/phy_reset** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

This file allows to reset PHY 88E1548 when attribute is set 0
due to some abnormal PHY behavior.
Expected behavior:
When phy_reset is written 1, all PHY 88E1548 are released
from the reset state, when 0 - are hold in reset state.

The files are read/write.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/pm_mgmt_en** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

This file assigns power management control ownership.
When power management control is provided by hardware, hardware
will automatically power off one or more line previously
powered line cards in case system power budget is getting
insufficient. It could be in case when some of power units lost
power good state.
When pm_mgmt_en is written 1, power management control by
software is enabled, 0 - power management control by hardware.
Note that for any setting of pm_mgmt_en attribute hardware will
not allow to power on any new line card in case system power
budget is insufficient.
Same in case software will try to power on several line cards
at once - hardware will power line cards while system has
enough power budget.
Default is 0.

The file is read/write.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/psu1_on** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

These files allow asserting system power cycling, switching
power supply units on and off and system's main power domain
shutdown.
Expected behavior:
When pwr_cycle is written 1: auxiliary power domain will go
down and after short period (about 1 second) up.
When psu1_on or psu2_on is written 1, related unit will be
disconnected from the power source, when written 0 - connected.
If both are written 1 - power supplies main power domain will
go down.
When pwr_down is written 1, system's main power domain will go
down.

The files are write only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/psu3_on** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/psu4_on** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

These files switching power supply units on and off.
Expected behavior:
When psu3_on or psu4_on is written 1, related unit will be
disconnected from the power source, when written 0 - connected.

The files are write only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/pwr_converter_prog_en** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

This file enables programming of power converters.
Default is 0 (programming disabled).
If the system is in locked-down mode writing this file will not be allowed.

The file is read/write.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/qsfp_pwr_good** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

This file shows QSFP ports power status. The value is set to 0
when one of any QSFP ports is plugged. The value is set to 1 when
there are no any QSFP ports are plugged.
The possible values are:
0 - Power good, 1 - Not power good.

The files are read only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_ac_ok_fail** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

This file shows the system reset cause due to AC power failure.
Value 1 in file means this is reset cause, 0 - otherwise.

The file is read only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_ac_pwr_fail** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_platform** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_soc** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_sw_pwr_off** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

These files show the system reset causes, as following: reset
due to AC power failure, reset invoked from software by
assertion reset signal through CPLD. reset caused by signal
asserted by SOC through ACPI register, reset invoked from
software by assertion power off signal through CPLD.

The files are read only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_aux_pwr_or_ref** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_asic_thermal** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_hotswap_or_halt** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_hotswap_or_wd** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_fw_reset** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_long_pb** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_main_pwr_fail** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_short_pb** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_sw_reset** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

These files show the system reset cause, as following: power
auxiliary outage or power refresh, ASIC thermal shutdown, halt,
hotswap, watchdog, firmware reset, long press power button,
short press power button, software reset. Value 1 in file means
this is reset cause, 0 - otherwise. Only one of the above
causes could be 1 at the same time, representing only last
reset cause.

The files are read only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_comex_pwr_fail** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_from_comex** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_system** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_voltmon_upgrade_fail** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

These files show the system reset cause, as following: ComEx
power fail, reset from ComEx, system platform reset, reset
due to voltage monitor devices upgrade failure,
Value 1 in file means this is reset cause, 0 - otherwise.
Only one bit could be 1 at the same time, representing only
the last reset cause.

The files are read only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_comex_thermal** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_comex_wd** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_from_asic** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_reload_bios** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_sff_wd** |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_swb_wd** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

These files show the system reset cause, as following:
COMEX thermal shutdown; wathchdog power off or reset was derived
by one of the next components: COMEX, switch board or by Small Form
Factor mezzanine, reset requested from ASIC, reset caused by BIOS
reload. Value 1 in file means this is reset cause, 0 - otherwise.
Only one of the above causes could be 1 at the same time, representing
only last reset cause.

The files are read only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_long_pwr_pb** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

This file if set 1 indicates that system has been reset by
long press of power button.

The file is read only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_pwr_converter_fail** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

This file shows the system reset cause due to power converter
devices failure.
Value 1 in file means this is reset cause, 0 - otherwise.

The file is read only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_swb_dc_dc_pwr_fail** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

This file shows 1 in case the system reset happened due to the
failure of any DC-DC power converter devices equipped on the
switch board.

The file is read only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/select_iio** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

This file allows iio devices selection.

Attribute select_iio can be written with 0 or with 1. It
selects which one of iio devices can be accessed.

The file is read/write.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/shutdown_unlock** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

This file allows to unlock ASIC after thermal shutdown event.
When system thermal shutdown is enforced by ASIC, ASIC is
getting locked and after system boot it will not be available.
Software can decide to unlock it by setting this attribute to
1 and then perform system power cycle by setting pwr_cycle
attribute to 1 (power cycle of main power domain).
Before setting shutdown_unlock to 1 it is recommended to
validate that system reboot cause is reset_asic_thermal or
reset_thermal_spc_or_pciesw.
In case shutdown_unlock is not set 1, the only way to release
ASIC from locking - is full system power cycle through the
external power distribution unit.
Default is 1.

The file is read/write.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/spi_chnl_select** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

This file allows SPI chip selection for External Root of Trust (EROT)
device Out-of-Band recovery.
File can be written with 0 or with 1. It selects which EROT can be accessed
through SPI device.

The file is read/write.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/ufm_version** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

This file exposes the firmware version of burnable voltage
regulator devices.

The file is read only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/voltreg_update_status** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

This file exposes the configuration update status of burnable
voltage regulator devices. The status values are as following:
0 - OK; 1 - CRC failure; 2 = I2C failure; 3 - in progress.

The file is read only.

|  |
| --- |
| **/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/vpd_wp** |

Defined on file [sysfs-driver-mlxreg-io](abi-stable.md#abi-file-stable-sysfs-driver-mlxreg-io)

This file allows to overwrite system VPD hardware write
protection when attribute is set 1.

The file is read/write.

|  |
| --- |
| **/sys/devices/system/cpu/cpuX/topology/book_id** |

Defined on file [sysfs-devices-system-cpu](abi-stable.md#abi-file-stable-sysfs-devices-system-cpu)

the book ID of cpuX. Typically it is the hardware platform's
identifier (rather than the kernel's). The actual value is
architecture and platform dependent. it's only used on s390.
Values: integer

|  |
| --- |
| **/sys/devices/system/cpu/cpuX/topology/book_siblings** |

Defined on file [sysfs-devices-system-cpu](abi-stable.md#abi-file-stable-sysfs-devices-system-cpu)

internal kernel map of cpuX's hardware threads within the same
book_id. it's only used on s390.
Values: hexadecimal bitmask.

|  |
| --- |
| **/sys/devices/system/cpu/cpuX/topology/book_siblings_list** |

Defined on file [sysfs-devices-system-cpu](abi-stable.md#abi-file-stable-sysfs-devices-system-cpu)

human-readable list of cpuX's hardware threads within the same
book_id.
The format is like 0-3, 8-11, 14,17. it's only used on s390.
Values: decimal list.

|  |
| --- |
| **/sys/devices/system/cpu/cpuX/topology/cluster_cpus** |

Defined on file [sysfs-devices-system-cpu](abi-stable.md#abi-file-stable-sysfs-devices-system-cpu)

internal kernel map of CPUs within the same cluster.
Values: hexadecimal bitmask.

|  |
| --- |
| **/sys/devices/system/cpu/cpuX/topology/cluster_cpus_list** |

Defined on file [sysfs-devices-system-cpu](abi-stable.md#abi-file-stable-sysfs-devices-system-cpu)

human-readable list of CPUs within the same cluster.
The format is like 0-3, 8-11, 14,17.
Values: decimal list.

|  |
| --- |
| **/sys/devices/system/cpu/cpuX/topology/cluster_id** |

Defined on file [sysfs-devices-system-cpu](abi-stable.md#abi-file-stable-sysfs-devices-system-cpu)

the cluster ID of cpuX. Typically it is the hardware platform's
identifier (rather than the kernel's). The actual value is
architecture and platform dependent.
Values: integer

|  |
| --- |
| **/sys/devices/system/cpu/cpuX/topology/core_cpus** |

Defined on file [sysfs-devices-system-cpu](abi-stable.md#abi-file-stable-sysfs-devices-system-cpu)

internal kernel map of CPUs within the same core.
(deprecated name: "thread_siblings")
Values: hexadecimal bitmask.

|  |
| --- |
| **/sys/devices/system/cpu/cpuX/topology/core_cpus_list** |

Defined on file [sysfs-devices-system-cpu](abi-stable.md#abi-file-stable-sysfs-devices-system-cpu)

human-readable list of CPUs within the same core.
The format is like 0-3, 8-11, 14,17.
(deprecated name: "thread_siblings_list").
Values: decimal list.

|  |
| --- |
| **/sys/devices/system/cpu/cpuX/topology/core_id** |

Defined on file [sysfs-devices-system-cpu](abi-stable.md#abi-file-stable-sysfs-devices-system-cpu)

the CPU core ID of cpuX. Typically it is the hardware platform's
identifier (rather than the kernel's). The actual value is
architecture and platform dependent.
Values: integer

|  |
| --- |
| **/sys/devices/system/cpu/cpuX/topology/die_cpus** |

Defined on file [sysfs-devices-system-cpu](abi-stable.md#abi-file-stable-sysfs-devices-system-cpu)

internal kernel map of CPUs within the same die.
Values: hexadecimal bitmask.

|  |
| --- |
| **/sys/devices/system/cpu/cpuX/topology/die_cpus_list** |

Defined on file [sysfs-devices-system-cpu](abi-stable.md#abi-file-stable-sysfs-devices-system-cpu)

human-readable list of CPUs within the same die.
The format is like 0-3, 8-11, 14,17.
Values: decimal list.

|  |
| --- |
| **/sys/devices/system/cpu/cpuX/topology/die_id** |

Defined on file [sysfs-devices-system-cpu](abi-stable.md#abi-file-stable-sysfs-devices-system-cpu)

the CPU die ID of cpuX. Typically it is the hardware platform's
identifier (rather than the kernel's). The actual value is
architecture and platform dependent.
Values: integer

|  |
| --- |
| **/sys/devices/system/cpu/cpuX/topology/drawer_id** |

Defined on file [sysfs-devices-system-cpu](abi-stable.md#abi-file-stable-sysfs-devices-system-cpu)

the drawer ID of cpuX. Typically it is the hardware platform's
identifier (rather than the kernel's). The actual value is
architecture and platform dependent. it's only used on s390.
Values: integer

|  |
| --- |
| **/sys/devices/system/cpu/cpuX/topology/drawer_siblings** |

Defined on file [sysfs-devices-system-cpu](abi-stable.md#abi-file-stable-sysfs-devices-system-cpu)

internal kernel map of cpuX's hardware threads within the same
drawer_id. it's only used on s390.
Values: hexadecimal bitmask.

|  |
| --- |
| **/sys/devices/system/cpu/cpuX/topology/drawer_siblings_list** |

Defined on file [sysfs-devices-system-cpu](abi-stable.md#abi-file-stable-sysfs-devices-system-cpu)

human-readable list of cpuX's hardware threads within the same
drawer_id.
The format is like 0-3, 8-11, 14,17. it's only used on s390.
Values: decimal list.

|  |
| --- |
| **/sys/devices/system/cpu/cpuX/topology/package_cpus** |

Defined on file [sysfs-devices-system-cpu](abi-stable.md#abi-file-stable-sysfs-devices-system-cpu)

internal kernel map of the CPUs sharing the same physical_package_id.
(deprecated name: "core_siblings").
Values: hexadecimal bitmask.

|  |
| --- |
| **/sys/devices/system/cpu/cpuX/topology/package_cpus_list** |

Defined on file [sysfs-devices-system-cpu](abi-stable.md#abi-file-stable-sysfs-devices-system-cpu)

human-readable list of CPUs sharing the same physical_package_id.
The format is like 0-3, 8-11, 14,17.
(deprecated name: "core_siblings_list")
Values: decimal list.

|  |
| --- |
| **/sys/devices/system/cpu/cpuX/topology/physical_package_id** |

Defined on file [sysfs-devices-system-cpu](abi-stable.md#abi-file-stable-sysfs-devices-system-cpu)

physical package id of cpuX. Typically corresponds to a physical
socket number, but the actual value is architecture and platform
dependent.
Values: integer

|  |
| --- |
| **/sys/devices/system/cpu/cpuX/topology/ppin** |

Defined on file [sysfs-devices-system-cpu](abi-stable.md#abi-file-stable-sysfs-devices-system-cpu)

per-socket protected processor inventory number
Values: hexadecimal.

|  |
| --- |
| **/sys/devices/system/cpu/cpu[0-9]+/dscr** |

Defined on file [sysfs-devices-system-cpu](abi-stable.md#abi-file-stable-sysfs-devices-system-cpu)

Default value for the Data Stream Control Register (DSCR) on
a CPU.
This default value is used when the kernel is executing and
for any process that has not set the DSCR itself.
If a process ever sets the DSCR (via direct access to the
SPR) that value will be persisted for that process and used
on any CPU where it executes (overriding the value described
here).
If set by a process it will be inherited by child processes.
Values: 64 bit unsigned integer (bit field)

|  |
| --- |
| **/sys/devices/system/cpu/dscr_default** |

Defined on file [sysfs-devices-system-cpu](abi-stable.md#abi-file-stable-sysfs-devices-system-cpu)

Writes are equivalent to writing to
/sys/devices/system/cpu/cpuN/dscr on all CPUs.
Reads return the last written value or 0.
This value is not a global default: it is a way to set
all per-CPU defaults at the same time.
Values: 64 bit unsigned integer (bit field)

|  |
| --- |
| **/sys/devices/system/node/has_cpu** |

Defined on file [sysfs-devices-node](abi-stable.md#abi-file-stable-sysfs-devices-node)

Nodes that have one or more CPUs.

|  |
| --- |
| **/sys/devices/system/node/has_high_memory** |

Defined on file [sysfs-devices-node](abi-stable.md#abi-file-stable-sysfs-devices-node)

Nodes that have regular or high memory.
Depends on CONFIG_HIGHMEM.

|  |
| --- |
| **/sys/devices/system/node/has_normal_memory** |

Defined on file [sysfs-devices-node](abi-stable.md#abi-file-stable-sysfs-devices-node)

Nodes that have regular memory.

|  |
| --- |
| **/sys/devices/system/node/nodeX** |

Defined on file [sysfs-devices-node](abi-stable.md#abi-file-stable-sysfs-devices-node)

When CONFIG_NUMA is enabled, this is a directory containing
information on node X such as what CPUs are local to the
node. Each file is detailed next.

|  |
| --- |
| **/sys/devices/system/node/nodeX/accessY/** |

Defined on file [sysfs-devices-node](abi-stable.md#abi-file-stable-sysfs-devices-node)

The node's relationship to other nodes for access class "Y".

|  |
| --- |
| **/sys/devices/system/node/nodeX/accessY/initiators/** |

Defined on file [sysfs-devices-node](abi-stable.md#abi-file-stable-sysfs-devices-node)

The directory containing symlinks to memory initiator
nodes that have class "Y" access to this target node's
memory. CPUs and other memory initiators in nodes not in
the list accessing this node's memory may have different
performance.

|  |
| --- |
| **/sys/devices/system/node/nodeX/accessY/initiators/read_bandwidth** |

Defined on file [sysfs-devices-node](abi-stable.md#abi-file-stable-sysfs-devices-node)

This node's read bandwidth in MB/s when accessed from
nodes found in this access class's linked initiators.

|  |
| --- |
| **/sys/devices/system/node/nodeX/accessY/initiators/read_latency** |

Defined on file [sysfs-devices-node](abi-stable.md#abi-file-stable-sysfs-devices-node)

This node's read latency in nanoseconds when accessed
from nodes found in this access class's linked initiators.

|  |
| --- |
| **/sys/devices/system/node/nodeX/accessY/initiators/write_bandwidth** |

Defined on file [sysfs-devices-node](abi-stable.md#abi-file-stable-sysfs-devices-node)

This node's write bandwidth in MB/s when accessed from
found in this access class's linked initiators.

|  |
| --- |
| **/sys/devices/system/node/nodeX/accessY/initiators/write_latency** |

Defined on file [sysfs-devices-node](abi-stable.md#abi-file-stable-sysfs-devices-node)

This node's write latency in nanoseconds when access
from nodes found in this class's linked initiators.

|  |
| --- |
| **/sys/devices/system/node/nodeX/accessY/targets/** |

Defined on file [sysfs-devices-node](abi-stable.md#abi-file-stable-sysfs-devices-node)

The directory containing symlinks to memory targets that
this initiator node has class "Y" access.

|  |
| --- |
| **/sys/devices/system/node/nodeX/compact** |

Defined on file [sysfs-devices-node](abi-stable.md#abi-file-stable-sysfs-devices-node)

When this file is written to, all memory within that node
will be compacted. When it completes, memory will be freed
into blocks which have as many contiguous pages as possible

|  |
| --- |
| **/sys/devices/system/node/nodeX/cpulist** |

Defined on file [sysfs-devices-node](abi-stable.md#abi-file-stable-sysfs-devices-node)

The CPUs associated to the node.

|  |
| --- |
| **/sys/devices/system/node/nodeX/cpumap** |

Defined on file [sysfs-devices-node](abi-stable.md#abi-file-stable-sysfs-devices-node)

The node's cpumap.

|  |
| --- |
| **/sys/devices/system/node/nodeX/distance** |

Defined on file [sysfs-devices-node](abi-stable.md#abi-file-stable-sysfs-devices-node)

Distance between the node and all the other nodes
in the system.

|  |
| --- |
| **/sys/devices/system/node/nodeX/hugepages/hugepages-<size>/** |

Defined on file [sysfs-devices-node](abi-stable.md#abi-file-stable-sysfs-devices-node)

The node's huge page size control/query attributes.
See [HugeTLB Pages](mm/hugetlbpage.md)

|  |
| --- |
| **/sys/devices/system/node/nodeX/meminfo** |

Defined on file [sysfs-devices-node](abi-stable.md#abi-file-stable-sysfs-devices-node)

Provides information about the node's distribution and memory
utilization. Similar to /proc/meminfo, see [The /proc Filesystem](../filesystems/proc.md)

|  |
| --- |
| **/sys/devices/system/node/nodeX/memory_failure/delayed** |

Defined on file [sysfs-devices-node](abi-stable.md#abi-file-stable-sysfs-devices-node)

Of the raw poisoned pages on a NUMA node, how many pages are
delayed by memory error recovery attempt. Delayed poisoned
pages usually will be retried by kernel.

|  |
| --- |
| **/sys/devices/system/node/nodeX/memory_failure/failed** |

Defined on file [sysfs-devices-node](abi-stable.md#abi-file-stable-sysfs-devices-node)

Of the raw poisoned pages on a NUMA node, how many pages are
failed by memory error recovery attempt. This usually means
a key recovery operation failed.

|  |
| --- |
| **/sys/devices/system/node/nodeX/memory_failure/ignored** |

Defined on file [sysfs-devices-node](abi-stable.md#abi-file-stable-sysfs-devices-node)

Of the raw poisoned pages on a NUMA node, how many pages are
ignored by memory error recovery attempt, usually because
support for this type of pages is unavailable, and kernel
gives up the recovery.

|  |
| --- |
| **/sys/devices/system/node/nodeX/memory_failure/recovered** |

Defined on file [sysfs-devices-node](abi-stable.md#abi-file-stable-sysfs-devices-node)

Of the raw poisoned pages on a NUMA node, how many pages are
recovered by memory error recovery attempt.

|  |
| --- |
| **/sys/devices/system/node/nodeX/memory_failure/total** |

Defined on file [sysfs-devices-node](abi-stable.md#abi-file-stable-sysfs-devices-node)

The total number of raw poisoned pages (pages containing
corrupted data due to memory errors) on a NUMA node.

|  |
| --- |
| **/sys/devices/system/node/nodeX/memory_side_cache/indexY/** |

Defined on file [sysfs-devices-node](abi-stable.md#abi-file-stable-sysfs-devices-node)

The directory containing attributes for the memory-side cache
level 'Y'.

|  |
| --- |
| **/sys/devices/system/node/nodeX/memory_side_cache/indexY/indexing** |

Defined on file [sysfs-devices-node](abi-stable.md#abi-file-stable-sysfs-devices-node)

The caches associativity indexing: 0 for direct mapped,
non-zero if indexed.

|  |
| --- |
| **/sys/devices/system/node/nodeX/memory_side_cache/indexY/line_size** |

Defined on file [sysfs-devices-node](abi-stable.md#abi-file-stable-sysfs-devices-node)

The number of bytes accessed from the next cache level on a
cache miss.

|  |
| --- |
| **/sys/devices/system/node/nodeX/memory_side_cache/indexY/size** |

Defined on file [sysfs-devices-node](abi-stable.md#abi-file-stable-sysfs-devices-node)

The size of this memory side cache in bytes.

|  |
| --- |
| **/sys/devices/system/node/nodeX/memory_side_cache/indexY/write_policy** |

Defined on file [sysfs-devices-node](abi-stable.md#abi-file-stable-sysfs-devices-node)

The cache write policy: 0 for write-back, 1 for write-through,
other or unknown.

|  |
| --- |
| **/sys/devices/system/node/nodeX/numastat** |

Defined on file [sysfs-devices-node](abi-stable.md#abi-file-stable-sysfs-devices-node)

The node's hit/miss statistics, in units of pages.
See [Numa policy hit/miss statistics](numastat.md)

|  |
| --- |
| **/sys/devices/system/node/nodeX/vmstat** |

Defined on file [sysfs-devices-node](abi-stable.md#abi-file-stable-sysfs-devices-node)

The node's zoned virtual memory statistics.
This is a superset of numastat.

|  |
| --- |
| **/sys/devices/system/node/nodeX/x86/sgx_total_bytes** |

Defined on file [sysfs-devices-node](abi-stable.md#abi-file-stable-sysfs-devices-node)

The total amount of SGX physical memory in bytes.

|  |
| --- |
| **/sys/devices/system/node/online** |

Defined on file [sysfs-devices-node](abi-stable.md#abi-file-stable-sysfs-devices-node)

Nodes that are online.

|  |
| --- |
| **/sys/devices/system/node/possible** |

Defined on file [sysfs-devices-node](abi-stable.md#abi-file-stable-sysfs-devices-node)

Nodes that could be possibly become online at some point.

|  |
| --- |
| **/sys/devices/system/xen_memory/xen_memory0/info/current_kb** |

Defined on file [sysfs-devices-system-xen_memory](abi-stable.md#abi-file-stable-sysfs-devices-system-xen-memory)

Current size (in KiB) of this domain's memory
reservation.

|  |
| --- |
| **/sys/devices/system/xen_memory/xen_memory0/info/high_kb** |

Defined on file [sysfs-devices-system-xen_memory](abi-stable.md#abi-file-stable-sysfs-devices-system-xen-memory)

Amount (in KiB) of high memory in the balloon.

|  |
| --- |
| **/sys/devices/system/xen_memory/xen_memory0/info/low_kb** |

Defined on file [sysfs-devices-system-xen_memory](abi-stable.md#abi-file-stable-sysfs-devices-system-xen-memory)

Amount (in KiB) of low (or normal) memory in the
balloon.

|  |
| --- |
| **/sys/devices/system/xen_memory/xen_memory0/max_retry_count** |

Defined on file [sysfs-devices-system-xen_memory](abi-stable.md#abi-file-stable-sysfs-devices-system-xen-memory)

The maximum number of times the balloon driver will
attempt to increase the balloon before giving up. See
also 'retry_count' below.
A value of zero means retry forever and is the default one.

|  |
| --- |
| **/sys/devices/system/xen_memory/xen_memory0/max_schedule_delay** |

Defined on file [sysfs-devices-system-xen_memory](abi-stable.md#abi-file-stable-sysfs-devices-system-xen-memory)

The limit that 'schedule_delay' (see below) will be
increased to. The default value is 32 seconds.

|  |
| --- |
| **/sys/devices/system/xen_memory/xen_memory0/retry_count** |

Defined on file [sysfs-devices-system-xen_memory](abi-stable.md#abi-file-stable-sysfs-devices-system-xen-memory)

The current number of times that the balloon driver
has attempted to increase the size of the balloon.
The default value is one. With max_retry_count being
zero (unlimited), this means that the driver will attempt
to retry with a 'schedule_delay' delay.

|  |
| --- |
| **/sys/devices/system/xen_memory/xen_memory0/schedule_delay** |

Defined on file [sysfs-devices-system-xen_memory](abi-stable.md#abi-file-stable-sysfs-devices-system-xen-memory)

The time (in seconds) to wait between attempts to
increase the balloon. Each time the balloon cannot be
increased, 'schedule_delay' is increased (until
'max_schedule_delay' is reached at which point it
will use the max value).

|  |
| --- |
| **/sys/devices/system/xen_memory/xen_memory0/scrub_pages** |

Defined on file [sysfs-devices-system-xen_memory](abi-stable.md#abi-file-stable-sysfs-devices-system-xen-memory)

Control scrubbing pages before returning them to Xen for others domains
use. Can be set with xen_scrub_pages cmdline
parameter. Default value controlled with CONFIG_XEN_SCRUB_PAGES_DEFAULT.

|  |
| --- |
| **/sys/devices/system/xen_memory/xen_memory0/target** |

Defined on file [sysfs-devices-system-xen_memory](abi-stable.md#abi-file-stable-sysfs-devices-system-xen-memory)

The target number of pages to adjust this domain's
memory reservation to.

|  |
| --- |
| **/sys/devices/system/xen_memory/xen_memory0/target_kb** |

Defined on file [sysfs-devices-system-xen_memory](abi-stable.md#abi-file-stable-sysfs-devices-system-xen-memory)

As target above, except the value is in KiB.

## Symbols under /sys/firmware

|  |
| --- |
| **/sys/firmware/acpi/pm_profile** |

Defined on file [sysfs-acpi-pmprofile](abi-stable.md#abi-file-stable-sysfs-acpi-pmprofile)

The ACPI pm_profile sysfs interface exposes the preferred
power management (and performance) profile of the platform
as provided in the ACPI FADT Preferred_PM_Profile field.

The integer value is directly passed as retrieved from the FADT.

Values: For the possible values refer to the Preferred_PM_Profile field
:   definition in Table 5.9 "FADT Format", Section 5.2.9 "Fixed ACPI
    Description Table (FADT)" of the ACPI specification.

    As of ACPI 6.5, the following values are defined:

    |  |  |
    | --- | --- |
    | 0 | Unspecified |
    | 1 | Desktop |
    | 2 | Mobile |
    | 3 | Workstation |
    | 4 | Enterprise Server |
    | 5 | SOHO Server |
    | 6 | Appliance PC |
    | 7 | Performance Server |
    | 8 | Tablet |
    | >8 | Reserved |

|  |
| --- |
| **/sys/firmware/efi/vars** |

Defined on file [sysfs-firmware-efi-vars](abi-stable.md#abi-file-stable-sysfs-firmware-efi-vars)

This directory exposes interfaces for interactive with
EFI variables. For more information on EFI variables,
see 'Variable Services' in the UEFI specification
(section 7.2 in specification version 2.3 Errata D).

In summary, EFI variables are named, and are classified
into separate namespaces through the use of a vendor
GUID. They also have an arbitrary binary value
associated with them.

The efivars module enumerates these variables and
creates a separate directory for each one found. Each
directory has a name of the form "<key>-<vendor guid>"
and contains the following files:

|  |  |
| --- | --- |
| attributes: | A read-only text file enumerating the EFI variable flags. Potential values include:  EFI_VARIABLE_NON_VOLATILE EFI_VARIABLE_BOOTSERVICE_ACCESS EFI_VARIABLE_RUNTIME_ACCESS EFI_VARIABLE_HARDWARE_ERROR_RECORD EFI_VARIABLE_AUTHENTICATED_WRITE_ACCESS  See the EFI documentation for an explanation of each of these variables. |
| data: | A read-only binary file that can be read to attain the value of the EFI variable |
| guid: | The vendor GUID of the variable. This should always match the GUID in the variable's name. |
| raw_var: | A binary file that can be read to obtain a structure that contains everything there is to know about the variable. For structure definition see "struct efi_variable" in the kernel sources.  This file can also be written to in order to update the value of a variable. For this to work however, all fields of the "struct efi_variable" passed must match byte for byte with the structure read out of the file, save for the value portion.  **Note** the efi_variable structure read/written with this file contains a 'long' type that may change widths depending on your underlying architecture. |
| size: | As ASCII representation of the size of the variable's value. |

In addition, two other magic binary files are provided
in the top-level directory and are used for adding and
removing variables:

|  |  |
| --- | --- |
| new_var: | Takes a "struct efi_variable" and instructs the EFI firmware to create a new variable. |
| del_var: | Takes a "struct efi_variable" and instructs the EFI firmware to remove any variable that has a matching vendor GUID and variable key name. |

|  |
| --- |
| **/sys/firmware/opal/dump** |

Defined on file [sysfs-firmware-opal-dump](abi-stable.md#abi-file-stable-sysfs-firmware-opal-dump)

This directory exposes interfaces for interacting with
the FSP and platform dumps through OPAL firmware interface.

This is only for the powerpc/powernv platform.

|  |  |
| --- | --- |
| initiate_dump: | When '1' is written to it, we will initiate a dump. Read this file for supported commands. |
| 0xXX-0xYYYY: | A directory for dump of type 0xXX and id 0xYYYY (in hex). The name of this directory should not be relied upon to be in this format, only that it's unique among all dumps. For determining the type and ID of the dump, use the id and type files. Do not rely on any particular size of dump type or dump id. |

Each dump has the following files:

|  |  |
| --- | --- |
| id: | An ASCII representation of the dump ID in hex (e.g. '0x01') |
| type: | An ASCII representation of the type of dump in the format "0x%x %s" with the ID in hex and a description of the dump type (or 'unknown'). Type '0xffffffff unknown' is used when we could not get the type from firmware. e.g. '0x02 System/Platform Dump' |
| dump: | A binary file containing the dump. The size of the dump is the size of this file. |
| acknowledge: | When 'ack' is written to this, we will acknowledge that we've retrieved the dump to the service processor. It will then remove it, making the dump inaccessible. Reading this file will get a list of supported actions. |

|  |
| --- |
| **/sys/firmware/opal/elog** |

Defined on file [sysfs-firmware-opal-elog](abi-stable.md#abi-file-stable-sysfs-firmware-opal-elog)

This directory exposes error log entries retrieved
through the OPAL firmware interface.

Each error log is identified by a unique ID and will
exist until explicitly acknowledged to firmware.

Each log entry has a directory in [/sys/firmware/opal/elog](abi-stable.md#abi-sys-firmware-opal-elog).

Log entries may be purged by the service processor
before retrieved by firmware or retrieved/acknowledged by
Linux if there is no room for more log entries.

In the event that Linux has retrieved the log entries
but not explicitly acknowledged them to firmware and
the service processor needs more room for log entries,
the only remaining copy of a log message may be in
Linux.

Typically, a user space daemon will monitor for new
entries, read them out and acknowledge them.

The service processor may be able to store more log
entries than firmware can, so after you acknowledge
an event from Linux you may instantly get another one
from the queue that was generated some time in the past.

The raw log format is a binary format. We currently
do not parse this at all in kernel, leaving it up to
user space to solve the problem. In future, we may
do more parsing in kernel and add more files to make
it easier for simple user space processes to extract
more information.

For each log entry (directory), there are the following
files:

|  |  |
| --- | --- |
| id: | An ASCII representation of the ID of the error log, in hex - e.g. "0x01". |
| type: | An ASCII representation of the type id and description of the type of error log. Currently just "0x00 PEL" - platform error log. In the future there may be additional types. |
| raw: | A read-only binary file that can be read to get the raw log entry. These are <16kb, often just hundreds of bytes and "average" 2kb. |
| acknowledge: | Writing 'ack' to this file will acknowledge the error log to firmware (and in turn the service processor, if applicable). Shortly after acknowledging it, the log entry will be removed from sysfs. Reading this file will list the supported operations (currently just acknowledge). |

## Symbols under /sys/fs

|  |
| --- |
| **/sys/fs/o2cb/** |

Defined on file [o2cb](abi-stable.md#abi-file-stable-o2cb)

Ocfs2-tools looks at 'interface-revision' for versioning
information. Each logmask/ file controls a set of debug prints
and can be written into with the strings "allow", "deny", or
"off". Reading the file returns the current state.

Users:
ocfs2-tools. It's sufficient to mail proposed changes to
[ocfs2-devel@lists.linux.dev](mailto:ocfs2-devel%40lists.linux.dev).

|  |
| --- |
| **/sys/fs/orangefs/acache/\*** |

Defined on file [sysfs-fs-orangefs](abi-stable.md#abi-file-stable-sysfs-fs-orangefs)

Attribute cache configurable settings.

|  |
| --- |
| **/sys/fs/orangefs/capcache/\*** |

Defined on file [sysfs-fs-orangefs](abi-stable.md#abi-file-stable-sysfs-fs-orangefs)

Capability cache configurable settings.

|  |
| --- |
| **/sys/fs/orangefs/ccache/\*** |

Defined on file [sysfs-fs-orangefs](abi-stable.md#abi-file-stable-sysfs-fs-orangefs)

Credential cache configurable settings.

|  |
| --- |
| **/sys/fs/orangefs/ncache/\*** |

Defined on file [sysfs-fs-orangefs](abi-stable.md#abi-file-stable-sysfs-fs-orangefs)

Name cache configurable settings.

|  |
| --- |
| **/sys/fs/orangefs/op_timeout_secs** |

Defined on file [sysfs-fs-orangefs](abi-stable.md#abi-file-stable-sysfs-fs-orangefs)

Service operation timeout in seconds.

|  |
| --- |
| **/sys/fs/orangefs/perf_counter_reset** |

Defined on file [sysfs-fs-orangefs](abi-stable.md#abi-file-stable-sysfs-fs-orangefs)

echo a 0 or a 1 into perf_counter_reset to
reset all the counters in
/sys/fs/orangefs/perf_counters
except ones with PINT_PERF_PRESERVE set.

|  |
| --- |
| **/sys/fs/orangefs/perf_counters/\*** |

Defined on file [sysfs-fs-orangefs](abi-stable.md#abi-file-stable-sysfs-fs-orangefs)

Counters and settings for various caches.
Read only.

|  |
| --- |
| **/sys/fs/orangefs/perf_history_size** |

Defined on file [sysfs-fs-orangefs](abi-stable.md#abi-file-stable-sysfs-fs-orangefs)

The perf_counters cache statistics have N, or
perf_history_size, samples. The default is
one.

Every perf_time_interval_secs the (first)
samples are reset.

If N is greater than one, the "current" set
of samples is reset, and the samples from the
other N-1 intervals remain available.

|  |
| --- |
| **/sys/fs/orangefs/perf_time_interval_secs** |

Defined on file [sysfs-fs-orangefs](abi-stable.md#abi-file-stable-sysfs-fs-orangefs)

Length of perf counter intervals in
seconds.

|  |
| --- |
| **/sys/fs/orangefs/slot_timeout_secs** |

Defined on file [sysfs-fs-orangefs](abi-stable.md#abi-file-stable-sysfs-fs-orangefs)

"Slot" timeout in seconds. A "slot"
is an indexed buffer in the shared
memory segment used for communication
between the kernel module and userspace.
Slots are requested and waited for,
the wait times out after slot_timeout_secs.

## Symbols under /sys/hypervisor

|  |
| --- |
| **/sys/hypervisor/compilation/compile_date** |

Defined on file [sysfs-hypervisor-xen](abi-stable.md#abi-file-stable-sysfs-hypervisor-xen)

If running under Xen:
Contains the build time stamp of the Xen hypervisor
Might return "<denied>" in case of special security settings
in the hypervisor.

|  |
| --- |
| **/sys/hypervisor/compilation/compiled_by** |

Defined on file [sysfs-hypervisor-xen](abi-stable.md#abi-file-stable-sysfs-hypervisor-xen)

If running under Xen:
Contains information who built the Xen hypervisor
Might return "<denied>" in case of special security settings
in the hypervisor.

|  |
| --- |
| **/sys/hypervisor/compilation/compiler** |

Defined on file [sysfs-hypervisor-xen](abi-stable.md#abi-file-stable-sysfs-hypervisor-xen)

If running under Xen:
Compiler which was used to build the Xen hypervisor
Might return "<denied>" in case of special security settings
in the hypervisor.

|  |
| --- |
| **/sys/hypervisor/properties/capabilities** |

Defined on file [sysfs-hypervisor-xen](abi-stable.md#abi-file-stable-sysfs-hypervisor-xen)

If running under Xen:
Space separated list of supported guest system types. Each type
is in the format: <class>-<major>.<minor>-<arch>
With:

> |  |  |
> | --- | --- |
> | <class>: | "xen" -- x86: paravirtualized, arm: standard "hvm" -- x86 only: fully virtualized |
> | <major>: | major guest interface version |
> | <minor>: | minor guest interface version |
> | <arch>: | architecture, e.g.: "x86_32": 32 bit x86 guest without PAE "x86_32p": 32 bit x86 guest with PAE "x86_64": 64 bit x86 guest "armv7l": 32 bit arm guest "aarch64": 64 bit arm guest |

|  |
| --- |
| **/sys/hypervisor/properties/changeset** |

Defined on file [sysfs-hypervisor-xen](abi-stable.md#abi-file-stable-sysfs-hypervisor-xen)

If running under Xen:
Changeset of the hypervisor (git commit)
Might return "<denied>" in case of special security settings
in the hypervisor.

|  |
| --- |
| **/sys/hypervisor/properties/features** |

Defined on file [sysfs-hypervisor-xen](abi-stable.md#abi-file-stable-sysfs-hypervisor-xen)

If running under Xen:
Features the Xen hypervisor supports for the guest as defined
in include/xen/interface/features.h printed as a hex value.

|  |
| --- |
| **/sys/hypervisor/properties/pagesize** |

Defined on file [sysfs-hypervisor-xen](abi-stable.md#abi-file-stable-sysfs-hypervisor-xen)

If running under Xen:
Default page size of the hypervisor printed as a hex value.
Might return "0" in case of special security settings
in the hypervisor.

|  |
| --- |
| **/sys/hypervisor/properties/virtual_start** |

Defined on file [sysfs-hypervisor-xen](abi-stable.md#abi-file-stable-sysfs-hypervisor-xen)

If running under Xen:
Virtual address of the hypervisor as a hex value.

|  |
| --- |
| **/sys/hypervisor/start_flags/\*** |

Defined on file [sysfs-hypervisor-xen](abi-stable.md#abi-file-stable-sysfs-hypervisor-xen)

If running under Xen:
All bits in Xen's start-flags are represented as
boolean files, returning '1' if set, '0' otherwise.
This takes the place of the defunct /proc/xen/capabilities,
which would contain "control_d" on dom0, and be empty
otherwise. This flag is now exposed as "initdomain" in
addition to the "privileged" flag; all other possible flags
are accessible as "unknownXX".

|  |
| --- |
| **/sys/hypervisor/type** |

Defined on file [sysfs-hypervisor-xen](abi-stable.md#abi-file-stable-sysfs-hypervisor-xen)

If running under Xen:
Type of hypervisor:
"xen": Xen hypervisor

|  |
| --- |
| **/sys/hypervisor/uuid** |

Defined on file [sysfs-hypervisor-xen](abi-stable.md#abi-file-stable-sysfs-hypervisor-xen)

If running under Xen:
UUID of the guest as known to the Xen hypervisor.

|  |
| --- |
| **/sys/hypervisor/version/extra** |

Defined on file [sysfs-hypervisor-xen](abi-stable.md#abi-file-stable-sysfs-hypervisor-xen)

If running under Xen:
The Xen version is in the format <major>.<minor><extra>
This is the <extra> part of it.
Might return "<denied>" in case of special security settings
in the hypervisor.

|  |
| --- |
| **/sys/hypervisor/version/major** |

Defined on file [sysfs-hypervisor-xen](abi-stable.md#abi-file-stable-sysfs-hypervisor-xen)

If running under Xen:
The Xen version is in the format <major>.<minor><extra>
This is the <major> part of it.

|  |
| --- |
| **/sys/hypervisor/version/minor** |

Defined on file [sysfs-hypervisor-xen](abi-stable.md#abi-file-stable-sysfs-hypervisor-xen)

If running under Xen:
The Xen version is in the format <major>.<minor><extra>
This is the <minor> part of it.

## Symbols under /sys/kernel

|  |
| --- |
| **/sys/kernel/notes** |

Defined on file [sysfs-kernel-notes](abi-stable.md#abi-file-stable-sysfs-kernel-notes)

The [/sys/kernel/notes](abi-stable.md#abi-sys-kernel-notes) file contains the binary representation
of the running vmlinux's .notes section.

## Symbols under /sys/module

|  |
| --- |
| **/sys/module/<MODULENAME>** |

Defined on file [sysfs-module](abi-stable.md#abi-file-stable-sysfs-module)

The name of the module that is in the kernel. This
module name will always show up if the module is loaded as a
dynamic module. If it is built directly into the kernel, it
will only show up if it has a version or at least one
parameter.

Note: The conditions of creation in the built-in case are not
by design and may be removed in the future.

|  |
| --- |
| **/sys/module/<MODULENAME>/parameters** |

Defined on file [sysfs-module](abi-stable.md#abi-file-stable-sysfs-module)

This directory contains individual files that are each
individual parameters of the module that are able to be
changed at runtime. See the individual module
documentation as to the contents of these parameters and
what they accomplish.

Note: The individual parameter names and values are not
considered stable, only the fact that they will be
placed in this location within sysfs. See the
individual driver documentation for details as to the
stability of the different parameters.

|  |
| --- |
| **/sys/module/<MODULENAME>/refcnt** |

Defined on file [sysfs-module](abi-stable.md#abi-file-stable-sysfs-module)

If the module is able to be unloaded from the kernel, this file
will contain the current reference count of the module.

Note: If the module is built into the kernel, or if the
CONFIG_MODULE_UNLOAD kernel configuration value is not enabled,
this file will not be present.

|  |
| --- |
| **/sys/module/<MODULENAME>/srcversion** |

Defined on file [sysfs-module](abi-stable.md#abi-file-stable-sysfs-module)

If the module source has MODULE_VERSION, this file will contain
the checksum of the source code.

|  |
| --- |
| **/sys/module/<MODULENAME>/version** |

Defined on file [sysfs-module](abi-stable.md#abi-file-stable-sysfs-module)

If the module source has MODULE_VERSION, this file will contain
the version of the source code.

## A notification mechanism for thermal related events

|  |
| --- |
| **A notification mechanism for thermal related events** |

Defined on file [thermal-notification](abi-stable.md#abi-file-stable-thermal-notification)

This interface enables notification for thermal related events.
The notification is in the form of a netlink event.

## Audit Login Session ID

|  |
| --- |
| **Audit Login Session ID** |

Defined on file [procfs-audit_loginuid](abi-stable.md#abi-file-stable-procfs-audit-loginuid)

The /proc/$pid/sessionid pseudofile is read to get the
audit login session ID of process $pid as a decimal
unsigned int (%u, u32). It is set automatically,
serially assigned with each new login.

Users:
audit and login applications

## Audit Login UID

|  |
| --- |
| **Audit Login UID** |

Defined on file [procfs-audit_loginuid](abi-stable.md#abi-file-stable-procfs-audit-loginuid)

The /proc/$pid/loginuid pseudofile is written to set and
read to get the audit login UID of process $pid as a
decimal unsigned int (%u, u32). If it is unset,
permissions are not needed to set it. The accessor must
have CAP_AUDIT_CONTROL in the initial user namespace to
write it if it has been set. It cannot be written again
if AUDIT_FEATURE_LOGINUID_IMMUTABLE is enabled. It
cannot be unset if AUDIT_FEATURE_ONLY_UNSET_LOGINUID is
enabled.

Users:
audit and login applications

## The kernel syscall interface

|  |
| --- |
| **The kernel syscall interface** |

Defined on file [syscalls](abi-stable.md#abi-file-stable-syscalls)

This interface matches much of the POSIX interface and is based
on it and other Unix based interfaces. It will only be added to
over time, and not have things removed from it.

Note that this interface is different for every architecture
that Linux supports. Please see the architecture-specific
documentation for details on the syscall numbers that are to be
mapped to each syscall.

## vDSO

|  |
| --- |
| **vDSO** |

Defined on file [vdso](abi-stable.md#abi-file-stable-vdso)

On some architectures, when the kernel loads any userspace program it
maps an ELF DSO into that program's address space. This DSO is called
the vDSO and it often contains useful and highly-optimized alternatives
to real syscalls.

These functions are called just like ordinary C function according to
your platform's ABI. Call them from a sensible context. (For example,
if you set CS on x86 to something strange, the vDSO functions are
within their rights to crash.) In addition, if you pass a bad
pointer to a vDSO function, you might get SIGSEGV instead of -EFAULT.

To find the DSO, parse the auxiliary vector passed to the program's
entry point. The AT_SYSINFO_EHDR entry will point to the vDSO.

The vDSO uses symbol versioning; whenever you request a symbol from the
vDSO, specify the version you are expecting.

Programs that dynamically link to glibc will use the vDSO automatically.
Otherwise, you can use the reference parser in
tools/testing/selftests/vDSO/parse_vdso.c.

Unless otherwise noted, the set of symbols with any given version and the
ABI of those symbols is considered stable. It may vary across architectures,
though.

Note:
:   As of this writing, this ABI documentation as been confirmed for x86_64.
    The maintainers of the other vDSO-using architectures should confirm
    that it is correct for their architecture.

## File stable/firewire-cdev

Has the following ABI:

- [/dev/fw[0-9]+](abi-stable.md#abi-dev-fw-0-9)

## File stable/o2cb

Has the following ABI:

- [/sys/fs/o2cb/](abi-stable.md#abi-sys-fs-o2cb)

## File stable/procfs-audit_loginuid

Has the following ABI:

- [Audit Login UID](abi-stable.md#abi-audit-login-uid)
- [Audit Login Session ID](abi-stable.md#abi-audit-login-session-id)

## File stable/syscalls

Has the following ABI:

- [The kernel syscall interface](abi-stable.md#abi-the-kernel-syscall-interface)

## File stable/sysfs-acpi-pmprofile

Has the following ABI:

- [/sys/firmware/acpi/pm_profile](abi-stable.md#abi-sys-firmware-acpi-pm-profile)

## File stable/sysfs-block

Has the following ABI:

- [/sys/block/<disk>/alignment_offset](abi-stable.md#abi-sys-block-disk-alignment-offset)
- [/sys/block/<disk>/discard_alignment](abi-stable.md#abi-sys-block-disk-discard-alignment)
- [/sys/block/<disk>/diskseq](abi-stable.md#abi-sys-block-disk-diskseq)
- [/sys/block/<disk>/inflight](abi-stable.md#abi-sys-block-disk-inflight)
- [/sys/block/<disk>/integrity/device_is_integrity_capable](abi-stable.md#abi-sys-block-disk-integrity-device-is-integrity-capable)
- [/sys/block/<disk>/integrity/format](abi-stable.md#abi-sys-block-disk-integrity-format)
- [/sys/block/<disk>/integrity/protection_interval_bytes](abi-stable.md#abi-sys-block-disk-integrity-protection-interval-bytes)
- [/sys/block/<disk>/integrity/read_verify](abi-stable.md#abi-sys-block-disk-integrity-read-verify)
- [/sys/block/<disk>/integrity/tag_size](abi-stable.md#abi-sys-block-disk-integrity-tag-size)
- [/sys/block/<disk>/integrity/write_generate](abi-stable.md#abi-sys-block-disk-integrity-write-generate)
- [/sys/block/<disk>/<partition>/alignment_offset](abi-stable.md#abi-sys-block-disk-partition-alignment-offset)
- [/sys/block/<disk>/<partition>/discard_alignment](abi-stable.md#abi-sys-block-disk-partition-discard-alignment)
- [/sys/block/<disk>/<partition>/stat](abi-stable.md#abi-sys-block-disk-partition-stat)
- [/sys/block/<disk>/queue/add_random](abi-stable.md#abi-sys-block-disk-queue-add-random)
- [/sys/block/<disk>/queue/chunk_sectors](abi-stable.md#abi-sys-block-disk-queue-chunk-sectors)
- [/sys/block/<disk>/queue/crypto/](abi-stable.md#abi-sys-block-disk-queue-crypto)
- [/sys/block/<disk>/queue/crypto/max_dun_bits](abi-stable.md#abi-sys-block-disk-queue-crypto-max-dun-bits)
- [/sys/block/<disk>/queue/crypto/modes/<mode>](abi-stable.md#abi-sys-block-disk-queue-crypto-modes-mode)
- [/sys/block/<disk>/queue/crypto/num_keyslots](abi-stable.md#abi-sys-block-disk-queue-crypto-num-keyslots)
- [/sys/block/<disk>/queue/dax](abi-stable.md#abi-sys-block-disk-queue-dax)
- [/sys/block/<disk>/queue/discard_granularity](abi-stable.md#abi-sys-block-disk-queue-discard-granularity)
- [/sys/block/<disk>/queue/discard_max_bytes](abi-stable.md#abi-sys-block-disk-queue-discard-max-bytes)
- [/sys/block/<disk>/queue/discard_max_hw_bytes](abi-stable.md#abi-sys-block-disk-queue-discard-max-hw-bytes)
- [/sys/block/<disk>/queue/discard_zeroes_data](abi-stable.md#abi-sys-block-disk-queue-discard-zeroes-data)
- [/sys/block/<disk>/queue/dma_alignment](abi-stable.md#abi-sys-block-disk-queue-dma-alignment)
- [/sys/block/<disk>/queue/fua](abi-stable.md#abi-sys-block-disk-queue-fua)
- [/sys/block/<disk>/queue/hw_sector_size](abi-stable.md#abi-sys-block-disk-queue-hw-sector-size)
- [/sys/block/<disk>/queue/independent_access_ranges/](abi-stable.md#abi-sys-block-disk-queue-independent-access-ranges)
- [/sys/block/<disk>/queue/io_poll](abi-stable.md#abi-sys-block-disk-queue-io-poll)
- [/sys/block/<disk>/queue/io_poll_delay](abi-stable.md#abi-sys-block-disk-queue-io-poll-delay)
- [/sys/block/<disk>/queue/io_timeout](abi-stable.md#abi-sys-block-disk-queue-io-timeout)
- [/sys/block/<disk>/queue/iostats](abi-stable.md#abi-sys-block-disk-queue-iostats)
- [/sys/block/<disk>/queue/logical_block_size](abi-stable.md#abi-sys-block-disk-queue-logical-block-size)
- [/sys/block/<disk>/queue/max_active_zones](abi-stable.md#abi-sys-block-disk-queue-max-active-zones)
- [/sys/block/<disk>/queue/max_discard_segments](abi-stable.md#abi-sys-block-disk-queue-max-discard-segments)
- [/sys/block/<disk>/queue/max_hw_sectors_kb](abi-stable.md#abi-sys-block-disk-queue-max-hw-sectors-kb)
- [/sys/block/<disk>/queue/max_integrity_segments](abi-stable.md#abi-sys-block-disk-queue-max-integrity-segments)
- [/sys/block/<disk>/queue/max_open_zones](abi-stable.md#abi-sys-block-disk-queue-max-open-zones)
- [/sys/block/<disk>/queue/max_sectors_kb](abi-stable.md#abi-sys-block-disk-queue-max-sectors-kb)
- [/sys/block/<disk>/queue/max_segment_size](abi-stable.md#abi-sys-block-disk-queue-max-segment-size)
- [/sys/block/<disk>/queue/max_segments](abi-stable.md#abi-sys-block-disk-queue-max-segments)
- [/sys/block/<disk>/queue/minimum_io_size](abi-stable.md#abi-sys-block-disk-queue-minimum-io-size)
- [/sys/block/<disk>/queue/nomerges](abi-stable.md#abi-sys-block-disk-queue-nomerges)
- [/sys/block/<disk>/queue/nr_requests](abi-stable.md#abi-sys-block-disk-queue-nr-requests)
- [/sys/block/<disk>/queue/nr_zones](abi-stable.md#abi-sys-block-disk-queue-nr-zones)
- [/sys/block/<disk>/queue/optimal_io_size](abi-stable.md#abi-sys-block-disk-queue-optimal-io-size)
- [/sys/block/<disk>/queue/physical_block_size](abi-stable.md#abi-sys-block-disk-queue-physical-block-size)
- [/sys/block/<disk>/queue/read_ahead_kb](abi-stable.md#abi-sys-block-disk-queue-read-ahead-kb)
- [/sys/block/<disk>/queue/rotational](abi-stable.md#abi-sys-block-disk-queue-rotational)
- [/sys/block/<disk>/queue/rq_affinity](abi-stable.md#abi-sys-block-disk-queue-rq-affinity)
- [/sys/block/<disk>/queue/scheduler](abi-stable.md#abi-sys-block-disk-queue-scheduler)
- [/sys/block/<disk>/queue/stable_writes](abi-stable.md#abi-sys-block-disk-queue-stable-writes)
- [/sys/block/<disk>/queue/throttle_sample_time](abi-stable.md#abi-sys-block-disk-queue-throttle-sample-time)
- [/sys/block/<disk>/queue/virt_boundary_mask](abi-stable.md#abi-sys-block-disk-queue-virt-boundary-mask)
- [/sys/block/<disk>/queue/wbt_lat_usec](abi-stable.md#abi-sys-block-disk-queue-wbt-lat-usec)
- [/sys/block/<disk>/queue/write_cache](abi-stable.md#abi-sys-block-disk-queue-write-cache)
- [/sys/block/<disk>/queue/write_same_max_bytes](abi-stable.md#abi-sys-block-disk-queue-write-same-max-bytes)
- [/sys/block/<disk>/queue/write_zeroes_max_bytes](abi-stable.md#abi-sys-block-disk-queue-write-zeroes-max-bytes)
- [/sys/block/<disk>/queue/zone_append_max_bytes](abi-stable.md#abi-sys-block-disk-queue-zone-append-max-bytes)
- [/sys/block/<disk>/queue/zone_write_granularity](abi-stable.md#abi-sys-block-disk-queue-zone-write-granularity)
- [/sys/block/<disk>/queue/zoned](abi-stable.md#abi-sys-block-disk-queue-zoned)
- [/sys/block/<disk>/hidden](abi-stable.md#abi-sys-block-disk-hidden)
- [/sys/block/<disk>/stat](abi-stable.md#abi-sys-block-disk-stat)

## File stable/sysfs-bus-firewire

Has the following ABI:

- [/sys/bus/firewire/devices/fw[0-9]+/](abi-stable.md#abi-sys-bus-firewire-devices-fw-0-9)
- [/sys/bus/firewire/devices/fw[0-9]+/units](abi-stable.md#abi-sys-bus-firewire-devices-fw-0-9-units)
- [/sys/bus/firewire/devices/fw[0-9]+/is_local](abi-stable.md#abi-sys-bus-firewire-devices-fw-0-9-is-local)
- [/sys/bus/firewire/devices/fw[0-9]+[.][0-9]+/](abi-stable.md#abi-sys-bus-firewire-devices-fw-0-9-0-9)
- [/sys/bus/firewire/devices/\*/](abi-stable.md#abi-sys-bus-firewire-devices)
- [/sys/bus/firewire/drivers/sbp2/fw\*/host\*/target\*/\*:\*:\*:\*/ieee1394_id](abi-stable.md#abi-sys-bus-firewire-drivers-sbp2-fw-host-target-ieee1394-id)

## File stable/sysfs-bus-fsl-mc

Has the following ABI:

- [/sys/bus/fsl-mc/rescan](abi-stable.md#abi-sys-bus-fsl-mc-rescan)
- [/sys/bus/fsl-mc/autorescan](abi-stable.md#abi-sys-bus-fsl-mc-autorescan)

## File stable/sysfs-bus-mhi

Has the following ABI:

- [/sys/bus/mhi/devices/.../serialnumber](abi-stable.md#abi-sys-bus-mhi-devices-serialnumber)
- [/sys/bus/mhi/devices/.../oem_pk_hash](abi-stable.md#abi-sys-bus-mhi-devices-oem-pk-hash)
- [/sys/bus/mhi/devices/.../soc_reset](abi-stable.md#abi-sys-bus-mhi-devices-soc-reset)

## File stable/sysfs-bus-nvmem

Has the following ABI:

- [/sys/bus/nvmem/devices/.../nvmem](abi-stable.md#abi-sys-bus-nvmem-devices-nvmem)

## File stable/sysfs-bus-usb

Has the following ABI:

- [/sys/bus/usb/devices/.../power/persist](abi-stable.md#abi-sys-bus-usb-devices-power-persist)
- [/sys/bus/usb/devices/.../power/autosuspend](abi-stable.md#abi-sys-bus-usb-devices-power-autosuspend)
- [/sys/bus/usb/device/.../power/connected_duration](abi-stable.md#abi-sys-bus-usb-device-power-connected-duration)
- [/sys/bus/usb/device/.../power/active_duration](abi-stable.md#abi-sys-bus-usb-device-power-active-duration)
- [/sys/bus/usb/devices/<busnum>-<port[.port]>...:<config num>-<interface num>/supports_autosuspend](abi-stable.md#abi-sys-bus-usb-devices-busnum-port-port-config-num-interface-num-supports-autosuspend)
- [/sys/bus/usb/device/.../avoid_reset_quirk](abi-stable.md#abi-sys-bus-usb-device-avoid-reset-quirk)
- [/sys/bus/usb/devices/.../devnum](abi-stable.md#abi-sys-bus-usb-devices-devnum)
- [/sys/bus/usb/devices/.../bConfigurationValue](abi-stable.md#abi-sys-bus-usb-devices-bconfigurationvalue)
- [/sys/bus/usb/devices/.../busnum](abi-stable.md#abi-sys-bus-usb-devices-busnum)
- [/sys/bus/usb/devices/.../descriptors](abi-stable.md#abi-sys-bus-usb-devices-descriptors)
- [/sys/bus/usb/devices/.../speed](abi-stable.md#abi-sys-bus-usb-devices-speed)

## File stable/sysfs-bus-vmbus

Has the following ABI:

- [/sys/bus/vmbus/hibernation](abi-stable.md#abi-sys-bus-vmbus-hibernation)
- [/sys/bus/vmbus/devices/<UUID>/id](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-id)
- [/sys/bus/vmbus/devices/<UUID>/class_id](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-class-id)
- [/sys/bus/vmbus/devices/<UUID>/device_id](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-device-id)
- [/sys/bus/vmbus/devices/<UUID>/channel_vp_mapping](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channel-vp-mapping)
- [/sys/bus/vmbus/devices/<UUID>/device](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-device)
- [/sys/bus/vmbus/devices/<UUID>/vendor](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-vendor)
- [/sys/bus/vmbus/devices/<UUID>/numa_node](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-numa-node)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>/cpu](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n-cpu)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>/in_mask](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n-in-mask)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>/latency](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n-latency)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>/out_mask](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n-out-mask)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>/pending](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n-pending)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>/read_avail](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n-read-avail)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>/write_avail](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n-write-avail)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>/events](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n-events)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>/interrupts](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n-interrupts)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>/subchannel_id](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n-subchannel-id)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>/monitor_id](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n-monitor-id)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>/ring](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n-ring)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>/intr_in_full](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n-intr-in-full)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>/intr_out_empty](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n-intr-out-empty)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>/out_full_first](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n-out-full-first)
- [/sys/bus/vmbus/devices/<UUID>/channels/<N>/out_full_total](abi-stable.md#abi-sys-bus-vmbus-devices-uuid-channels-n-out-full-total)

## File stable/sysfs-bus-w1

Has the following ABI:

- [/sys/bus/w1/devices/.../w1_master_timeout_us](abi-stable.md#abi-sys-bus-w1-devices-w1-master-timeout-us)

## File stable/sysfs-bus-xen-backend

Has the following ABI:

- [/sys/bus/xen-backend/devices/\*/devtype](abi-stable.md#abi-sys-bus-xen-backend-devices-devtype)
- [/sys/bus/xen-backend/devices/\*/nodename](abi-stable.md#abi-sys-bus-xen-backend-devices-nodename)
- [/sys/bus/xen-backend/devices/vbd-\*/physical_device](abi-stable.md#abi-sys-bus-xen-backend-devices-vbd-physical-device)
- [/sys/bus/xen-backend/devices/vbd-\*/mode](abi-stable.md#abi-sys-bus-xen-backend-devices-vbd-mode)
- [/sys/bus/xen-backend/devices/vbd-\*/statistics/f_req](abi-stable.md#abi-sys-bus-xen-backend-devices-vbd-statistics-f-req)
- [/sys/bus/xen-backend/devices/vbd-\*/statistics/oo_req](abi-stable.md#abi-sys-bus-xen-backend-devices-vbd-statistics-oo-req)
- [/sys/bus/xen-backend/devices/vbd-\*/statistics/rd_req](abi-stable.md#abi-sys-bus-xen-backend-devices-vbd-statistics-rd-req)
- [/sys/bus/xen-backend/devices/vbd-\*/statistics/rd_sect](abi-stable.md#abi-sys-bus-xen-backend-devices-vbd-statistics-rd-sect)
- [/sys/bus/xen-backend/devices/vbd-\*/statistics/wr_req](abi-stable.md#abi-sys-bus-xen-backend-devices-vbd-statistics-wr-req)
- [/sys/bus/xen-backend/devices/vbd-\*/statistics/wr_sect](abi-stable.md#abi-sys-bus-xen-backend-devices-vbd-statistics-wr-sect)
- [/sys/bus/xen-backend/devices/\*/state](abi-stable.md#abi-sys-bus-xen-backend-devices-state)

## File stable/sysfs-class-backlight

Has the following ABI:

- [/sys/class/backlight/<backlight>/bl_power](abi-stable.md#abi-sys-class-backlight-backlight-bl-power)
- [/sys/class/backlight/<backlight>/brightness](abi-stable.md#abi-sys-class-backlight-backlight-brightness)
- [/sys/class/backlight/<backlight>/actual_brightness](abi-stable.md#abi-sys-class-backlight-backlight-actual-brightness)
- [/sys/class/backlight/<backlight>/max_brightness](abi-stable.md#abi-sys-class-backlight-backlight-max-brightness)
- [/sys/class/backlight/<backlight>/type](abi-stable.md#abi-sys-class-backlight-backlight-type)

## File stable/sysfs-class-infiniband

sysfs interface common for all infiniband devices

Has the following ABI:

- [/sys/class/infiniband/<device>/node_type](abi-stable.md#abi-sys-class-infiniband-device-node-type)
- [/sys/class/infiniband/<device>/node_guid](abi-stable.md#abi-sys-class-infiniband-device-node-type)
- [/sys/class/infiniband/<device>/sys_image_guid](abi-stable.md#abi-sys-class-infiniband-device-node-type)
- [/sys/class/infiniband/<device>/node_desc](abi-stable.md#abi-sys-class-infiniband-device-node-desc)
- [/sys/class/infiniband/<device>/fw_ver](abi-stable.md#abi-sys-class-infiniband-device-fw-ver)
- [/sys/class/infiniband/<device>/ports/<port-num>/lid](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-lid)
- [/sys/class/infiniband/<device>/ports/<port-num>/rate](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-lid)
- [/sys/class/infiniband/<device>/ports/<port-num>/lid_mask_count](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-lid)
- [/sys/class/infiniband/<device>/ports/<port-num>/sm_sl](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-lid)
- [/sys/class/infiniband/<device>/ports/<port-num>/sm_lid](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-lid)
- [/sys/class/infiniband/<device>/ports/<port-num>/state](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-lid)
- [/sys/class/infiniband/<device>/ports/<port-num>/phys_state](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-lid)
- [/sys/class/infiniband/<device>/ports/<port-num>/cap_mask](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-lid)
- [/sys/class/infiniband/<device>/ports/<port-num>/link_layer](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-link-layer)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/symbol_error](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/port_rcv_errors](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/port_rcv_remote_physical_errors](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/port_rcv_switch_relay_errors](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/link_error_recovery](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/port_xmit_constraint_errors](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/port_rcv_contraint_errors](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/local_link_integrity_errors](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/excessive_buffer_overrun_errors](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/port_xmit_data](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/port_rcv_data](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/port_xmit_packets](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/port_rcv_packets](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/unicast_rcv_packets](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/unicast_xmit_packets](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/multicast_rcv_packets](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/multicast_xmit_packets](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/link_downed](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/port_xmit_discards](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/VL15_dropped](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device>/ports/<port-num>/counters/port_xmit_wait](abi-stable.md#abi-sys-class-infiniband-device-ports-port-num-counters-symbol-error)
- [/sys/class/infiniband/<device-name>/hw_counters/lifespan](abi-stable.md#abi-sys-class-infiniband-device-name-hw-counters-lifespan)
- [/sys/class/infiniband/<device-name>/ports/<port-num>/hw_counters/lifespan](abi-stable.md#abi-sys-class-infiniband-device-name-hw-counters-lifespan)
- [/sys/class/infiniband/<hca>/ports/<port-number>/gid_attrs/ndevs/<gid-index>](abi-stable.md#abi-sys-class-infiniband-hca-ports-port-number-gid-attrs-ndevs-gid-index)
- [/sys/class/infiniband/<hca>/ports/<port-number>/gid_attrs/types/<gid-index>](abi-stable.md#abi-sys-class-infiniband-hca-ports-port-number-gid-attrs-types-gid-index)
- [/sys/class/infiniband_mad/umad<N>/ibdev](abi-stable.md#abi-sys-class-infiniband-mad-umad-n-ibdev)
- [/sys/class/infiniband_mad/umad<N>/port](abi-stable.md#abi-sys-class-infiniband-mad-umad-n-ibdev)
- [/sys/class/infiniband_mad/issm<N>/ibdev](abi-stable.md#abi-sys-class-infiniband-mad-umad-n-ibdev)
- [/sys/class/infiniband_mad/issm<N>/port](abi-stable.md#abi-sys-class-infiniband-mad-umad-n-ibdev)
- [/sys/class/infiniband_mad/abi_version](abi-stable.md#abi-sys-class-infiniband-mad-abi-version)
- [/sys/class/infiniband_verbs/uverbs<N>/ibdev](abi-stable.md#abi-sys-class-infiniband-verbs-uverbs-n-ibdev)
- [/sys/class/infiniband_verbs/uverbs<N>/abi_version](abi-stable.md#abi-sys-class-infiniband-verbs-uverbs-n-ibdev)
- [/sys/class/infiniband_verbs/abi_version](abi-stable.md#abi-sys-class-infiniband-verbs-abi-version)
- [/sys/class/infiniband/mthcaX/hw_rev](abi-stable.md#abi-sys-class-infiniband-mthcax-hw-rev)
- [/sys/class/infiniband/mthcaX/hca_type](abi-stable.md#abi-sys-class-infiniband-mthcax-hw-rev)
- [/sys/class/infiniband/mthcaX/board_id](abi-stable.md#abi-sys-class-infiniband-mthcax-hw-rev)
- [/sys/class/infiniband/mlx4_X/hw_rev](abi-stable.md#abi-sys-class-infiniband-mlx4-x-hw-rev)
- [/sys/class/infiniband/mlx4_X/hca_type](abi-stable.md#abi-sys-class-infiniband-mlx4-x-hw-rev)
- [/sys/class/infiniband/mlx4_X/board_id](abi-stable.md#abi-sys-class-infiniband-mlx4-x-hw-rev)
- [/sys/class/infiniband/mlx4_X/iov/ports/<port-num>/gids/<n>](abi-stable.md#abi-sys-class-infiniband-mlx4-x-iov-ports-port-num-gids-n)
- [/sys/class/infiniband/mlx4_X/iov/ports/<port-num>/admin_guids/<n>](abi-stable.md#abi-sys-class-infiniband-mlx4-x-iov-ports-port-num-gids-n)
- [/sys/class/infiniband/mlx4_X/iov/ports/<port-num>/pkeys/<n>](abi-stable.md#abi-sys-class-infiniband-mlx4-x-iov-ports-port-num-gids-n)
- [/sys/class/infiniband/mlx4_X/iov/ports/<port-num>/mcgs/](abi-stable.md#abi-sys-class-infiniband-mlx4-x-iov-ports-port-num-gids-n)
- [/sys/class/infiniband/mlx4_X/iov/ports/<pci-slot-num>/ports/<m>/gid_idx/0](abi-stable.md#abi-sys-class-infiniband-mlx4-x-iov-ports-port-num-gids-n)
- [/sys/class/infiniband/mlx4_X/iov/ports/<pci-slot-num>/ports/<m>/pkey_idx/<n>](abi-stable.md#abi-sys-class-infiniband-mlx4-x-iov-ports-port-num-gids-n)
- [/sys/class/infiniband/mlx4_X/iov/<pci-slot-num>/ports/<m>/smi_enabled](abi-stable.md#abi-sys-class-infiniband-mlx4-x-iov-pci-slot-num-ports-m-smi-enabled)
- [/sys/class/infiniband/mlx4_X/iov/<pci-slot-num>/ports/<m>/enable_smi_admin](abi-stable.md#abi-sys-class-infiniband-mlx4-x-iov-pci-slot-num-ports-m-smi-enabled)
- [/sys/class/infiniband/cxgb4_X/hw_rev](abi-stable.md#abi-sys-class-infiniband-cxgb4-x-hw-rev)
- [/sys/class/infiniband/cxgb4_X/hca_type](abi-stable.md#abi-sys-class-infiniband-cxgb4-x-hw-rev)
- [/sys/class/infiniband/cxgb4_X/board_id](abi-stable.md#abi-sys-class-infiniband-cxgb4-x-hw-rev)
- [/sys/class/infiniband/qibX/version](abi-stable.md#abi-sys-class-infiniband-qibx-version)
- [/sys/class/infiniband/qibX/hw_rev](abi-stable.md#abi-sys-class-infiniband-qibx-version)
- [/sys/class/infiniband/qibX/hca_type](abi-stable.md#abi-sys-class-infiniband-qibx-version)
- [/sys/class/infiniband/qibX/board_id](abi-stable.md#abi-sys-class-infiniband-qibx-version)
- [/sys/class/infiniband/qibX/boardversion](abi-stable.md#abi-sys-class-infiniband-qibx-version)
- [/sys/class/infiniband/qibX/nctxts](abi-stable.md#abi-sys-class-infiniband-qibx-version)
- [/sys/class/infiniband/qibX/localbus_info](abi-stable.md#abi-sys-class-infiniband-qibx-version)
- [/sys/class/infiniband/qibX/tempsense](abi-stable.md#abi-sys-class-infiniband-qibx-version)
- [/sys/class/infiniband/qibX/serial](abi-stable.md#abi-sys-class-infiniband-qibx-version)
- [/sys/class/infiniband/qibX/nfreectxts](abi-stable.md#abi-sys-class-infiniband-qibx-version)
- [/sys/class/infiniband/qibX/chip_reset](abi-stable.md#abi-sys-class-infiniband-qibx-version)
- [/sys/class/infiniband/qibX/ports/<N>/sl2vl/[0-15]](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-sl2vl-0-15)
- [/sys/class/infiniband/qibX/ports/<N>/CCMgtA/cc_settings_bin](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-ccmgta-cc-settings-bin)
- [/sys/class/infiniband/qibX/ports/<N>/CCMgtA/cc_table_bin](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-ccmgta-cc-settings-bin)
- [/sys/class/infiniband/qibX/ports/<N>/linkstate/loopback](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-linkstate-loopback)
- [/sys/class/infiniband/qibX/ports/<N>/linkstate/led_override](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-linkstate-loopback)
- [/sys/class/infiniband/qibX/ports/<N>/linkstate/hrtbt_enable](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-linkstate-loopback)
- [/sys/class/infiniband/qibX/ports/<N>/linkstate/status](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-linkstate-loopback)
- [/sys/class/infiniband/qibX/ports/<N>/linkstate/status_str](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-linkstate-loopback)
- [/sys/class/infiniband/qibX/ports/<N>/diag_counters/rc_resends](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-diag-counters-rc-resends)
- [/sys/class/infiniband/qibX/ports/<N>/diag_counters/seq_naks](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-diag-counters-rc-resends)
- [/sys/class/infiniband/qibX/ports/<N>/diag_counters/rdma_seq](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-diag-counters-rc-resends)
- [/sys/class/infiniband/qibX/ports/<N>/diag_counters/rnr_naks](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-diag-counters-rc-resends)
- [/sys/class/infiniband/qibX/ports/<N>/diag_counters/other_naks](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-diag-counters-rc-resends)
- [/sys/class/infiniband/qibX/ports/<N>/diag_counters/rc_timeouts](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-diag-counters-rc-resends)
- [/sys/class/infiniband/qibX/ports/<N>/diag_counters/look_pkts](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-diag-counters-rc-resends)
- [/sys/class/infiniband/qibX/ports/<N>/diag_counters/pkt_drops](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-diag-counters-rc-resends)
- [/sys/class/infiniband/qibX/ports/<N>/diag_counters/dma_wait](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-diag-counters-rc-resends)
- [/sys/class/infiniband/qibX/ports/<N>/diag_counters/unaligned](abi-stable.md#abi-sys-class-infiniband-qibx-ports-n-diag-counters-rc-resends)
- [/sys/class/infiniband/mlx5_X/hw_rev](abi-stable.md#abi-sys-class-infiniband-mlx5-x-hw-rev)
- [/sys/class/infiniband/mlx5_X/hca_type](abi-stable.md#abi-sys-class-infiniband-mlx5-x-hw-rev)
- [/sys/class/infiniband/mlx5_X/reg_pages](abi-stable.md#abi-sys-class-infiniband-mlx5-x-hw-rev)
- [/sys/class/infiniband/mlx5_X/fw_pages](abi-stable.md#abi-sys-class-infiniband-mlx5-x-hw-rev)
- [/sys/class/infiniband/usnic_X/board_id](abi-stable.md#abi-sys-class-infiniband-usnic-x-board-id)
- [/sys/class/infiniband/usnic_X/config](abi-stable.md#abi-sys-class-infiniband-usnic-x-board-id)
- [/sys/class/infiniband/usnic_X/qp_per_vf](abi-stable.md#abi-sys-class-infiniband-usnic-x-board-id)
- [/sys/class/infiniband/usnic_X/max_vf](abi-stable.md#abi-sys-class-infiniband-usnic-x-board-id)
- [/sys/class/infiniband/usnic_X/cq_per_vf](abi-stable.md#abi-sys-class-infiniband-usnic-x-board-id)
- [/sys/class/infiniband/usnic_X/iface](abi-stable.md#abi-sys-class-infiniband-usnic-x-board-id)
- [/sys/class/infiniband/usnic_X/qpn/summary](abi-stable.md#abi-sys-class-infiniband-usnic-x-qpn-summary)
- [/sys/class/infiniband/usnic_X/qpn/context](abi-stable.md#abi-sys-class-infiniband-usnic-x-qpn-summary)
- [/sys/class/infiniband/ocrdmaX/hw_rev](abi-stable.md#abi-sys-class-infiniband-ocrdmax-hw-rev)
- [/sys/class/infiniband/ocrdmaX/hca_type](abi-stable.md#abi-sys-class-infiniband-ocrdmax-hca-type)
- [/sys/class/infiniband/hfi1_X/hw_rev](abi-stable.md#abi-sys-class-infiniband-hfi1-x-hw-rev)
- [/sys/class/infiniband/hfi1_X/board_id](abi-stable.md#abi-sys-class-infiniband-hfi1-x-hw-rev)
- [/sys/class/infiniband/hfi1_X/nctxts](abi-stable.md#abi-sys-class-infiniband-hfi1-x-hw-rev)
- [/sys/class/infiniband/hfi1_X/serial](abi-stable.md#abi-sys-class-infiniband-hfi1-x-hw-rev)
- [/sys/class/infiniband/hfi1_X/chip_reset](abi-stable.md#abi-sys-class-infiniband-hfi1-x-hw-rev)
- [/sys/class/infiniband/hfi1_X/boardversion](abi-stable.md#abi-sys-class-infiniband-hfi1-x-hw-rev)
- [/sys/class/infiniband/hfi1_X/nfreectxts](abi-stable.md#abi-sys-class-infiniband-hfi1-x-hw-rev)
- [/sys/class/infiniband/hfi1_X/tempsense](abi-stable.md#abi-sys-class-infiniband-hfi1-x-hw-rev)
- [/sys/class/infiniband/hfi1_X/ports/<N>/CCMgtA/cc_settings_bin](abi-stable.md#abi-sys-class-infiniband-hfi1-x-ports-n-ccmgta-cc-settings-bin)
- [/sys/class/infiniband/hfi1_X/ports/<N>/CCMgtA/cc_table_bin](abi-stable.md#abi-sys-class-infiniband-hfi1-x-ports-n-ccmgta-cc-settings-bin)
- [/sys/class/infiniband/hfi1_X/ports/<N>/CCMgtA/cc_prescan](abi-stable.md#abi-sys-class-infiniband-hfi1-x-ports-n-ccmgta-cc-settings-bin)
- [/sys/class/infiniband/hfi1_X/ports/<N>/sc2vl/[0-31]](abi-stable.md#abi-sys-class-infiniband-hfi1-x-ports-n-sc2vl-0-31)
- [/sys/class/infiniband/hfi1_X/ports/<N>/sl2sc/[0-31]](abi-stable.md#abi-sys-class-infiniband-hfi1-x-ports-n-sc2vl-0-31)
- [/sys/class/infiniband/hfi1_X/ports/<N>/vl2mtu/[0-15]](abi-stable.md#abi-sys-class-infiniband-hfi1-x-ports-n-sc2vl-0-31)
- [/sys/class/infiniband/hfi1_X/sdma_<N>/cpu_list](abi-stable.md#abi-sys-class-infiniband-hfi1-x-sdma-n-cpu-list)
- [/sys/class/infiniband/hfi1_X/sdma_<N>/vl](abi-stable.md#abi-sys-class-infiniband-hfi1-x-sdma-n-cpu-list)
- [/sys/class/infiniband/qedrX/hw_rev](abi-stable.md#abi-sys-class-infiniband-qedrx-hw-rev)
- [/sys/class/infiniband/qedrX/hca_type](abi-stable.md#abi-sys-class-infiniband-qedrx-hw-rev)
- [/sys/class/infiniband/vmw_pvrdmaX/hw_rev](abi-stable.md#abi-sys-class-infiniband-vmw-pvrdmax-hw-rev)
- [/sys/class/infiniband/vmw_pvrdmaX/hca_type](abi-stable.md#abi-sys-class-infiniband-vmw-pvrdmax-hw-rev)
- [/sys/class/infiniband/vmw_pvrdmaX/board_id](abi-stable.md#abi-sys-class-infiniband-vmw-pvrdmax-hw-rev)
- [/sys/class/infiniband/bnxt_reX/hw_rev](abi-stable.md#abi-sys-class-infiniband-bnxt-rex-hw-rev)
- [/sys/class/infiniband/bnxt_reX/hca_type](abi-stable.md#abi-sys-class-infiniband-bnxt-rex-hw-rev)

## File stable/sysfs-class-rfkill

rfkill - radio frequency (RF) connector kill switch support

For details to this subsystem look at [rfkill - RF kill switch support](../driver-api/rfkill.md).

For the deprecated `/sys/class/rfkill/*/claim` knobs of this interface look in
[removed/sysfs-class-rfkill](abi-removed.md#abi-file-removed-sysfs-class-rfkill).

Has the following ABI:

- [/sys/class/rfkill](abi-stable.md#abi-sys-class-rfkill)
- [/sys/class/rfkill/rfkill[0-9]+/name](abi-stable.md#abi-sys-class-rfkill-rfkill-0-9-name)
- [/sys/class/rfkill/rfkill[0-9]+/type](abi-stable.md#abi-sys-class-rfkill-rfkill-0-9-type)
- [/sys/class/rfkill/rfkill[0-9]+/persistent](abi-stable.md#abi-sys-class-rfkill-rfkill-0-9-persistent)
- [/sys/class/rfkill/rfkill[0-9]+/state](abi-stable.md#abi-sys-class-rfkill-rfkill-0-9-state)
- [/sys/class/rfkill/rfkill[0-9]+/hard](abi-stable.md#abi-sys-class-rfkill-rfkill-0-9-hard)
- [/sys/class/rfkill/rfkill[0-9]+/soft](abi-stable.md#abi-sys-class-rfkill-rfkill-0-9-soft)

## File stable/sysfs-class-tpm

Has the following ABI:

- [/sys/class/tpm/tpmX/device/](abi-stable.md#abi-sys-class-tpm-tpmx-device)
- [/sys/class/tpm/tpmX/device/active](abi-stable.md#abi-sys-class-tpm-tpmx-device-active)
- [/sys/class/tpm/tpmX/device/cancel](abi-stable.md#abi-sys-class-tpm-tpmx-device-cancel)
- [/sys/class/tpm/tpmX/device/caps](abi-stable.md#abi-sys-class-tpm-tpmx-device-caps)
- [/sys/class/tpm/tpmX/device/durations](abi-stable.md#abi-sys-class-tpm-tpmx-device-durations)
- [/sys/class/tpm/tpmX/device/enabled](abi-stable.md#abi-sys-class-tpm-tpmx-device-enabled)
- [/sys/class/tpm/tpmX/device/owned](abi-stable.md#abi-sys-class-tpm-tpmx-device-owned)
- [/sys/class/tpm/tpmX/device/pcrs](abi-stable.md#abi-sys-class-tpm-tpmx-device-pcrs)
- [/sys/class/tpm/tpmX/device/pubek](abi-stable.md#abi-sys-class-tpm-tpmx-device-pubek)
- [/sys/class/tpm/tpmX/device/temp_deactivated](abi-stable.md#abi-sys-class-tpm-tpmx-device-temp-deactivated)
- [/sys/class/tpm/tpmX/device/timeouts](abi-stable.md#abi-sys-class-tpm-tpmx-device-timeouts)
- [/sys/class/tpm/tpmX/tpm_version_major](abi-stable.md#abi-sys-class-tpm-tpmx-tpm-version-major)
- [/sys/class/tpm/tpmX/pcr-<H>/<N>](abi-stable.md#abi-sys-class-tpm-tpmx-pcr-h-n)

## File stable/sysfs-class-ubi

Has the following ABI:

- [/sys/class/ubi/](abi-stable.md#abi-sys-class-ubi)
- [/sys/class/ubi/version](abi-stable.md#abi-sys-class-ubi-version)
- [/sys/class/ubiX/](abi-stable.md#abi-sys-class-ubix)
- [/sys/class/ubi/ubiX/avail_eraseblocks](abi-stable.md#abi-sys-class-ubi-ubix-avail-eraseblocks)
- [/sys/class/ubi/ubiX/bad_peb_count](abi-stable.md#abi-sys-class-ubi-ubix-bad-peb-count)
- [/sys/class/ubi/ubiX/bgt_enabled](abi-stable.md#abi-sys-class-ubi-ubix-bgt-enabled)
- [/sys/class/ubi/ubiX/dev](abi-stable.md#abi-sys-class-ubi-ubix-dev)
- [/sys/class/ubi/ubiX/eraseblock_size](abi-stable.md#abi-sys-class-ubi-ubix-eraseblock-size)
- [/sys/class/ubi/ubiX/max_ec](abi-stable.md#abi-sys-class-ubi-ubix-max-ec)
- [/sys/class/ubi/ubiX/max_vol_count](abi-stable.md#abi-sys-class-ubi-ubix-max-vol-count)
- [/sys/class/ubi/ubiX/min_io_size](abi-stable.md#abi-sys-class-ubi-ubix-min-io-size)
- [/sys/class/ubi/ubiX/mtd_num](abi-stable.md#abi-sys-class-ubi-ubix-mtd-num)
- [/sys/class/ubi/ubiX/reserved_for_bad](abi-stable.md#abi-sys-class-ubi-ubix-reserved-for-bad)
- [/sys/class/ubi/ubiX/ro_mode](abi-stable.md#abi-sys-class-ubi-ubix-ro-mode)
- [/sys/class/ubi/ubiX/total_eraseblocks](abi-stable.md#abi-sys-class-ubi-ubix-total-eraseblocks)
- [/sys/class/ubi/ubiX/volumes_count](abi-stable.md#abi-sys-class-ubi-ubix-volumes-count)
- [/sys/class/ubi/ubiX/ubiX_Y/](abi-stable.md#abi-sys-class-ubi-ubix-ubix-y)
- [/sys/class/ubi/ubiX/ubiX_Y/alignment](abi-stable.md#abi-sys-class-ubi-ubix-ubix-y-alignment)
- [/sys/class/ubi/ubiX/ubiX_Y/corrupted](abi-stable.md#abi-sys-class-ubi-ubix-ubix-y-corrupted)
- [/sys/class/ubi/ubiX/ubiX_Y/data_bytes](abi-stable.md#abi-sys-class-ubi-ubix-ubix-y-data-bytes)
- [/sys/class/ubi/ubiX/ubiX_Y/dev](abi-stable.md#abi-sys-class-ubi-ubix-ubix-y-dev)
- [/sys/class/ubi/ubiX/ubiX_Y/name](abi-stable.md#abi-sys-class-ubi-ubix-ubix-y-name)
- [/sys/class/ubi/ubiX/ubiX_Y/reserved_ebs](abi-stable.md#abi-sys-class-ubi-ubix-ubix-y-reserved-ebs)
- [/sys/class/ubi/ubiX/ubiX_Y/type](abi-stable.md#abi-sys-class-ubi-ubix-ubix-y-type)
- [/sys/class/ubi/ubiX/ubiX_Y/upd_marker](abi-stable.md#abi-sys-class-ubi-ubix-ubix-y-upd-marker)
- [/sys/class/ubi/ubiX/ubiX_Y/usable_eb_size](abi-stable.md#abi-sys-class-ubi-ubix-ubix-y-usable-eb-size)

## File stable/sysfs-class-udc

Has the following ABI:

- [/sys/class/udc/<udc>/a_alt_hnp_support](abi-stable.md#abi-sys-class-udc-udc-a-alt-hnp-support)
- [/sys/class/udc/<udc>/a_hnp_support](abi-stable.md#abi-sys-class-udc-udc-a-hnp-support)
- [/sys/class/udc/<udc>/b_hnp_enable](abi-stable.md#abi-sys-class-udc-udc-b-hnp-enable)
- [/sys/class/udc/<udc>/current_speed](abi-stable.md#abi-sys-class-udc-udc-current-speed)
- [/sys/class/udc/<udc>/is_a_peripheral](abi-stable.md#abi-sys-class-udc-udc-is-a-peripheral)
- [/sys/class/udc/<udc>/is_otg](abi-stable.md#abi-sys-class-udc-udc-is-otg)
- [/sys/class/udc/<udc>/maximum_speed](abi-stable.md#abi-sys-class-udc-udc-maximum-speed)
- [/sys/class/udc/<udc>/soft_connect](abi-stable.md#abi-sys-class-udc-udc-soft-connect)
- [/sys/class/udc/<udc>/srp](abi-stable.md#abi-sys-class-udc-udc-srp)
- [/sys/class/udc/<udc>/state](abi-stable.md#abi-sys-class-udc-udc-state)
- [/sys/class/udc/<udc>/function](abi-stable.md#abi-sys-class-udc-udc-function)

## File stable/sysfs-devices

Note:
:   This documents additional properties of any device beyond what
    is documented in [Rules on how to access information in sysfs](sysfs-rules.md)

Has the following ABI:

- [/sys/devices/\*/of_node](abi-stable.md#abi-sys-devices-of-node)
- [/sys/devices/\*/devspec](abi-stable.md#abi-sys-devices-devspec)
- [/sys/devices/\*/obppath](abi-stable.md#abi-sys-devices-obppath)
- [/sys/devices/\*/dev](abi-stable.md#abi-sys-devices-dev)

## File stable/sysfs-devices-node

Has the following ABI:

- [/sys/devices/system/node/possible](abi-stable.md#abi-sys-devices-system-node-possible)
- [/sys/devices/system/node/online](abi-stable.md#abi-sys-devices-system-node-online)
- [/sys/devices/system/node/has_normal_memory](abi-stable.md#abi-sys-devices-system-node-has-normal-memory)
- [/sys/devices/system/node/has_cpu](abi-stable.md#abi-sys-devices-system-node-has-cpu)
- [/sys/devices/system/node/has_high_memory](abi-stable.md#abi-sys-devices-system-node-has-high-memory)
- [/sys/devices/system/node/nodeX](abi-stable.md#abi-sys-devices-system-node-nodex)
- [/sys/devices/system/node/nodeX/cpumap](abi-stable.md#abi-sys-devices-system-node-nodex-cpumap)
- [/sys/devices/system/node/nodeX/cpulist](abi-stable.md#abi-sys-devices-system-node-nodex-cpulist)
- [/sys/devices/system/node/nodeX/meminfo](abi-stable.md#abi-sys-devices-system-node-nodex-meminfo)
- [/sys/devices/system/node/nodeX/numastat](abi-stable.md#abi-sys-devices-system-node-nodex-numastat)
- [/sys/devices/system/node/nodeX/distance](abi-stable.md#abi-sys-devices-system-node-nodex-distance)
- [/sys/devices/system/node/nodeX/vmstat](abi-stable.md#abi-sys-devices-system-node-nodex-vmstat)
- [/sys/devices/system/node/nodeX/compact](abi-stable.md#abi-sys-devices-system-node-nodex-compact)
- [/sys/devices/system/node/nodeX/hugepages/hugepages-<size>/](abi-stable.md#abi-sys-devices-system-node-nodex-hugepages-hugepages-size)
- [/sys/devices/system/node/nodeX/accessY/](abi-stable.md#abi-sys-devices-system-node-nodex-accessy)
- [/sys/devices/system/node/nodeX/accessY/initiators/](abi-stable.md#abi-sys-devices-system-node-nodex-accessy-initiators)
- [/sys/devices/system/node/nodeX/accessY/targets/](abi-stable.md#abi-sys-devices-system-node-nodex-accessy-targets)
- [/sys/devices/system/node/nodeX/accessY/initiators/read_bandwidth](abi-stable.md#abi-sys-devices-system-node-nodex-accessy-initiators-read-bandwidth)
- [/sys/devices/system/node/nodeX/accessY/initiators/read_latency](abi-stable.md#abi-sys-devices-system-node-nodex-accessy-initiators-read-latency)
- [/sys/devices/system/node/nodeX/accessY/initiators/write_bandwidth](abi-stable.md#abi-sys-devices-system-node-nodex-accessy-initiators-write-bandwidth)
- [/sys/devices/system/node/nodeX/accessY/initiators/write_latency](abi-stable.md#abi-sys-devices-system-node-nodex-accessy-initiators-write-latency)
- [/sys/devices/system/node/nodeX/memory_side_cache/indexY/](abi-stable.md#abi-sys-devices-system-node-nodex-memory-side-cache-indexy)
- [/sys/devices/system/node/nodeX/memory_side_cache/indexY/indexing](abi-stable.md#abi-sys-devices-system-node-nodex-memory-side-cache-indexy-indexing)
- [/sys/devices/system/node/nodeX/memory_side_cache/indexY/line_size](abi-stable.md#abi-sys-devices-system-node-nodex-memory-side-cache-indexy-line-size)
- [/sys/devices/system/node/nodeX/memory_side_cache/indexY/size](abi-stable.md#abi-sys-devices-system-node-nodex-memory-side-cache-indexy-size)
- [/sys/devices/system/node/nodeX/memory_side_cache/indexY/write_policy](abi-stable.md#abi-sys-devices-system-node-nodex-memory-side-cache-indexy-write-policy)
- [/sys/devices/system/node/nodeX/x86/sgx_total_bytes](abi-stable.md#abi-sys-devices-system-node-nodex-x86-sgx-total-bytes)
- [/sys/devices/system/node/nodeX/memory_failure/total](abi-stable.md#abi-sys-devices-system-node-nodex-memory-failure-total)
- [/sys/devices/system/node/nodeX/memory_failure/ignored](abi-stable.md#abi-sys-devices-system-node-nodex-memory-failure-ignored)
- [/sys/devices/system/node/nodeX/memory_failure/failed](abi-stable.md#abi-sys-devices-system-node-nodex-memory-failure-failed)
- [/sys/devices/system/node/nodeX/memory_failure/delayed](abi-stable.md#abi-sys-devices-system-node-nodex-memory-failure-delayed)
- [/sys/devices/system/node/nodeX/memory_failure/recovered](abi-stable.md#abi-sys-devices-system-node-nodex-memory-failure-recovered)

## File stable/sysfs-devices-system-cpu

Has the following ABI:

- [/sys/devices/system/cpu/dscr_default](abi-stable.md#abi-sys-devices-system-cpu-dscr-default)
- [/sys/devices/system/cpu/cpu[0-9]+/dscr](abi-stable.md#abi-sys-devices-system-cpu-cpu-0-9-dscr)
- [/sys/devices/system/cpu/cpuX/topology/physical_package_id](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-physical-package-id)
- [/sys/devices/system/cpu/cpuX/topology/die_id](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-die-id)
- [/sys/devices/system/cpu/cpuX/topology/core_id](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-core-id)
- [/sys/devices/system/cpu/cpuX/topology/cluster_id](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-cluster-id)
- [/sys/devices/system/cpu/cpuX/topology/book_id](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-book-id)
- [/sys/devices/system/cpu/cpuX/topology/drawer_id](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-drawer-id)
- [/sys/devices/system/cpu/cpuX/topology/core_cpus](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-core-cpus)
- [/sys/devices/system/cpu/cpuX/topology/core_cpus_list](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-core-cpus-list)
- [/sys/devices/system/cpu/cpuX/topology/package_cpus](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-package-cpus)
- [/sys/devices/system/cpu/cpuX/topology/package_cpus_list](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-package-cpus-list)
- [/sys/devices/system/cpu/cpuX/topology/die_cpus](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-die-cpus)
- [/sys/devices/system/cpu/cpuX/topology/ppin](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-ppin)
- [/sys/devices/system/cpu/cpuX/topology/die_cpus_list](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-die-cpus-list)
- [/sys/devices/system/cpu/cpuX/topology/cluster_cpus](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-cluster-cpus)
- [/sys/devices/system/cpu/cpuX/topology/cluster_cpus_list](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-cluster-cpus-list)
- [/sys/devices/system/cpu/cpuX/topology/book_siblings](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-book-siblings)
- [/sys/devices/system/cpu/cpuX/topology/book_siblings_list](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-book-siblings-list)
- [/sys/devices/system/cpu/cpuX/topology/drawer_siblings](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-drawer-siblings)
- [/sys/devices/system/cpu/cpuX/topology/drawer_siblings_list](abi-stable.md#abi-sys-devices-system-cpu-cpux-topology-drawer-siblings-list)

## File stable/sysfs-devices-system-xen_memory

Has the following ABI:

- [/sys/devices/system/xen_memory/xen_memory0/max_retry_count](abi-stable.md#abi-sys-devices-system-xen-memory-xen-memory0-max-retry-count)
- [/sys/devices/system/xen_memory/xen_memory0/max_schedule_delay](abi-stable.md#abi-sys-devices-system-xen-memory-xen-memory0-max-schedule-delay)
- [/sys/devices/system/xen_memory/xen_memory0/retry_count](abi-stable.md#abi-sys-devices-system-xen-memory-xen-memory0-retry-count)
- [/sys/devices/system/xen_memory/xen_memory0/schedule_delay](abi-stable.md#abi-sys-devices-system-xen-memory-xen-memory0-schedule-delay)
- [/sys/devices/system/xen_memory/xen_memory0/target](abi-stable.md#abi-sys-devices-system-xen-memory-xen-memory0-target)
- [/sys/devices/system/xen_memory/xen_memory0/target_kb](abi-stable.md#abi-sys-devices-system-xen-memory-xen-memory0-target-kb)
- [/sys/devices/system/xen_memory/xen_memory0/info/current_kb](abi-stable.md#abi-sys-devices-system-xen-memory-xen-memory0-info-current-kb)
- [/sys/devices/system/xen_memory/xen_memory0/info/high_kb](abi-stable.md#abi-sys-devices-system-xen-memory-xen-memory0-info-high-kb)
- [/sys/devices/system/xen_memory/xen_memory0/info/low_kb](abi-stable.md#abi-sys-devices-system-xen-memory-xen-memory0-info-low-kb)
- [/sys/devices/system/xen_memory/xen_memory0/scrub_pages](abi-stable.md#abi-sys-devices-system-xen-memory-xen-memory0-scrub-pages)

## File stable/sysfs-driver-aspeed-vuart

Has the following ABI:

- [/sys/bus/platform/drivers/aspeed-vuart/\*/lpc_address](abi-stable.md#abi-sys-bus-platform-drivers-aspeed-vuart-lpc-address)
- [/sys/bus/platform/drivers/aspeed-vuart/\*/sirq](abi-stable.md#abi-sys-bus-platform-drivers-aspeed-vuart-sirq)
- [/sys/bus/platform/drivers/aspeed-vuart/\*/sirq_polarity](abi-stable.md#abi-sys-bus-platform-drivers-aspeed-vuart-sirq-polarity)

## File stable/sysfs-driver-dma-idxd

Has the following ABI:

- [/sys/bus/dsa/devices/dsa<m>/version](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-version)
- [/sys/bus/dsa/devices/dsa<m>/cdev_major](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-cdev-major)
- [/sys/bus/dsa/devices/dsa<m>/errors](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-errors)
- [/sys/bus/dsa/devices/dsa<m>/max_batch_size](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-max-batch-size)
- [/sys/bus/dsa/devices/dsa<m>/max_work_queues_size](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-max-work-queues-size)
- [/sys/bus/dsa/devices/dsa<m>/max_engines](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-max-engines)
- [/sys/bus/dsa/devices/dsa<m>/max_groups](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-max-groups)
- [/sys/bus/dsa/devices/dsa<m>/max_read_buffers](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-max-read-buffers)
- [/sys/bus/dsa/devices/dsa<m>/max_transfer_size](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-max-transfer-size)
- [/sys/bus/dsa/devices/dsa<m>/max_work_queues](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-max-work-queues)
- [/sys/bus/dsa/devices/dsa<m>/numa_node](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-numa-node)
- [/sys/bus/dsa/devices/dsa<m>/op_cap](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-op-cap)
- [/sys/bus/dsa/devices/dsa<m>/pasid_enabled](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-pasid-enabled)
- [/sys/bus/dsa/devices/dsa<m>/state](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-state)
- [/sys/bus/dsa/devices/dsa<m>/group<m>.<n>](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-group-m-n)
- [/sys/bus/dsa/devices/dsa<m>/engine<m>.<n>](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-engine-m-n)
- [/sys/bus/dsa/devices/dsa<m>/wq<m>.<n>](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-wq-m-n)
- [/sys/bus/dsa/devices/dsa<m>/configurable](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-configurable)
- [/sys/bus/dsa/devices/dsa<m>/read_buffer_limit](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-read-buffer-limit)
- [/sys/bus/dsa/devices/dsa<m>/cmd_status](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-cmd-status)
- [/sys/bus/dsa/devices/dsa<m>/iaa_cap](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-iaa-cap)
- [/sys/bus/dsa/devices/dsa<m>/event_log_size](abi-stable.md#abi-sys-bus-dsa-devices-dsa-m-event-log-size)
- [/sys/bus/dsa/devices/wq<m>.<n>/block_on_fault](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-block-on-fault)
- [/sys/bus/dsa/devices/wq<m>.<n>/group_id](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-group-id)
- [/sys/bus/dsa/devices/wq<m>.<n>/size](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-size)
- [/sys/bus/dsa/devices/wq<m>.<n>/type](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-type)
- [/sys/bus/dsa/devices/wq<m>.<n>/cdev_minor](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-cdev-minor)
- [/sys/bus/dsa/devices/wq<m>.<n>/mode](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-mode)
- [/sys/bus/dsa/devices/wq<m>.<n>/priority](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-priority)
- [/sys/bus/dsa/devices/wq<m>.<n>/state](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-state)
- [/sys/bus/dsa/devices/wq<m>.<n>/threshold](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-threshold)
- [/sys/bus/dsa/devices/wq<m>.<n>/max_transfer_size](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-max-transfer-size)
- [/sys/bus/dsa/devices/wq<m>.<n>/max_batch_size](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-max-batch-size)
- [/sys/bus/dsa/devices/wq<m>.<n>/ats_disable](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-ats-disable)
- [/sys/bus/dsa/devices/wq<m>.<n>/prs_disable](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-prs-disable)
- [/sys/bus/dsa/devices/wq<m>.<n>/occupancy](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-occupancy)
- [/sys/bus/dsa/devices/wq<m>.<n>/enqcmds_retries](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-enqcmds-retries)
- [/sys/bus/dsa/devices/wq<m>.<n>/op_config](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-op-config)
- [/sys/bus/dsa/devices/wq<m>.<n>/driver_name](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-driver-name)
- [/sys/bus/dsa/devices/engine<m>.<n>/group_id](abi-stable.md#abi-sys-bus-dsa-devices-engine-m-n-group-id)
- [/sys/bus/dsa/devices/group<m>.<n>/use_read_buffer_limit](abi-stable.md#abi-sys-bus-dsa-devices-group-m-n-use-read-buffer-limit)
- [/sys/bus/dsa/devices/group<m>.<n>/read_buffers_allowed](abi-stable.md#abi-sys-bus-dsa-devices-group-m-n-read-buffers-allowed)
- [/sys/bus/dsa/devices/group<m>.<n>/read_buffers_reserved](abi-stable.md#abi-sys-bus-dsa-devices-group-m-n-read-buffers-reserved)
- [/sys/bus/dsa/devices/group<m>.<n>/desc_progress_limit](abi-stable.md#abi-sys-bus-dsa-devices-group-m-n-desc-progress-limit)
- [/sys/bus/dsa/devices/group<m>.<n>/batch_progress_limit](abi-stable.md#abi-sys-bus-dsa-devices-group-m-n-batch-progress-limit)
- [/sys/bus/dsa/devices/wq<m>.<n>/dsa<x>\!wq<m>.<n>/file<y>/cr_faults](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-dsa-x-wq-m-n-file-y-cr-faults)
- [/sys/bus/dsa/devices/wq<m>.<n>/dsa<x>\!wq<m>.<n>/file<y>/cr_fault_failures](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-dsa-x-wq-m-n-file-y-cr-fault-failures)
- [/sys/bus/dsa/devices/wq<m>.<n>/dsa<x>\!wq<m>.<n>/file<y>/pid](abi-stable.md#abi-sys-bus-dsa-devices-wq-m-n-dsa-x-wq-m-n-file-y-pid)

## File stable/sysfs-driver-dma-ioatdma

Has the following ABI:

- [/sys/devices/pciXXXX:XX/0000:XX:XX.X/dma/dma<n>chan<n>/quickdata/cap](abi-stable.md#abi-sys-devices-pcixxxx-xx-0000-xx-xx-x-dma-dma-n-chan-n-quickdata-cap)
- [/sys/devices/pciXXXX:XX/0000:XX:XX.X/dma/dma<n>chan<n>/quickdata/ring_active](abi-stable.md#abi-sys-devices-pcixxxx-xx-0000-xx-xx-x-dma-dma-n-chan-n-quickdata-ring-active)
- [/sys/devices/pciXXXX:XX/0000:XX:XX.X/dma/dma<n>chan<n>/quickdata/ring_size](abi-stable.md#abi-sys-devices-pcixxxx-xx-0000-xx-xx-x-dma-dma-n-chan-n-quickdata-ring-size)
- [/sys/devices/pciXXXX:XX/0000:XX:XX.X/dma/dma<n>chan<n>/quickdata/version](abi-stable.md#abi-sys-devices-pcixxxx-xx-0000-xx-xx-x-dma-dma-n-chan-n-quickdata-version)
- [/sys/devices/pciXXXX:XX/0000:XX:XX.X/dma/dma<n>chan<n>/quickdata/intr_coalesce](abi-stable.md#abi-sys-devices-pcixxxx-xx-0000-xx-xx-x-dma-dma-n-chan-n-quickdata-intr-coalesce)

## File stable/sysfs-driver-firmware-zynqmp

Has the following ABI:

- [/sys/devices/platform/firmware\:zynqmp-firmware/ggs\*](abi-stable.md#abi-sys-devices-platform-firmware-zynqmp-firmware-ggs)
- [/sys/devices/platform/firmware\:zynqmp-firmware/pggs\*](abi-stable.md#abi-sys-devices-platform-firmware-zynqmp-firmware-pggs)
- [/sys/devices/platform/firmware\:zynqmp-firmware/shutdown_scope](abi-stable.md#abi-sys-devices-platform-firmware-zynqmp-firmware-shutdown-scope)
- [/sys/devices/platform/firmware\:zynqmp-firmware/health_status](abi-stable.md#abi-sys-devices-platform-firmware-zynqmp-firmware-health-status)
- [/sys/devices/platform/firmware\:zynqmp-firmware/feature_config_id](abi-stable.md#abi-sys-devices-platform-firmware-zynqmp-firmware-feature-config-id)
- [/sys/devices/platform/firmware\:zynqmp-firmware/feature_config_value](abi-stable.md#abi-sys-devices-platform-firmware-zynqmp-firmware-feature-config-value)

## File stable/sysfs-driver-ib_srp

Has the following ABI:

- [/sys/class/infiniband_srp/srp-<hca>-<port_number>/add_target](abi-stable.md#abi-sys-class-infiniband-srp-srp-hca-port-number-add-target)
- [/sys/class/infiniband_srp/srp-<hca>-<port_number>/ibdev](abi-stable.md#abi-sys-class-infiniband-srp-srp-hca-port-number-ibdev)
- [/sys/class/infiniband_srp/srp-<hca>-<port_number>/port](abi-stable.md#abi-sys-class-infiniband-srp-srp-hca-port-number-port)
- [/sys/class/scsi_host/host<n>/allow_ext_sg](abi-stable.md#abi-sys-class-scsi-host-host-n-allow-ext-sg)
- [/sys/class/scsi_host/host<n>/ch_count](abi-stable.md#abi-sys-class-scsi-host-host-n-ch-count)
- [/sys/class/scsi_host/host<n>/cmd_sg_entries](abi-stable.md#abi-sys-class-scsi-host-host-n-cmd-sg-entries)
- [/sys/class/scsi_host/host<n>/comp_vector](abi-stable.md#abi-sys-class-scsi-host-host-n-comp-vector)
- [/sys/class/scsi_host/host<n>/dgid](abi-stable.md#abi-sys-class-scsi-host-host-n-dgid)
- [/sys/class/scsi_host/host<n>/id_ext](abi-stable.md#abi-sys-class-scsi-host-host-n-id-ext)
- [/sys/class/scsi_host/host<n>/ioc_guid](abi-stable.md#abi-sys-class-scsi-host-host-n-ioc-guid)
- [/sys/class/scsi_host/host<n>/local_ib_device](abi-stable.md#abi-sys-class-scsi-host-host-n-local-ib-device)
- [/sys/class/scsi_host/host<n>/local_ib_port](abi-stable.md#abi-sys-class-scsi-host-host-n-local-ib-port)
- [/sys/class/scsi_host/host<n>/orig_dgid](abi-stable.md#abi-sys-class-scsi-host-host-n-orig-dgid)
- [/sys/class/scsi_host/host<n>/pkey](abi-stable.md#abi-sys-class-scsi-host-host-n-pkey)
- [/sys/class/scsi_host/host<n>/req_lim](abi-stable.md#abi-sys-class-scsi-host-host-n-req-lim)
- [/sys/class/scsi_host/host<n>/service_id](abi-stable.md#abi-sys-class-scsi-host-host-n-service-id)
- [/sys/class/scsi_host/host<n>/sgid](abi-stable.md#abi-sys-class-scsi-host-host-n-sgid)
- [/sys/class/scsi_host/host<n>/zero_req_lim](abi-stable.md#abi-sys-class-scsi-host-host-n-zero-req-lim)

## File stable/sysfs-driver-mlxreg-io

Has the following ABI:

- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/asic_health](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-asic-health)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld1_version](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-cpld1-version)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld2_version](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-cpld1-version)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/fan_dir](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-fan-dir)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld3_version](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-cpld3-version)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/jtag_enable](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-jtag-enable)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/select_iio](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-select-iio)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/psu1_on](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-psu1-on)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_aux_pwr_or_ref](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-ref)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_asic_thermal](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-ref)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_hotswap_or_halt](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-ref)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_hotswap_or_wd](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-ref)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_fw_reset](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-ref)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_long_pb](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-ref)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_main_pwr_fail](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-ref)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_short_pb](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-ref)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_sw_reset](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-ref)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_comex_pwr_fail](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-comex-pwr-fail)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_from_comex](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-comex-pwr-fail)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_system](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-comex-pwr-fail)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_voltmon_upgrade_fail](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-comex-pwr-fail)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld4_version](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-cpld4-version)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_comex_thermal](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-comex-thermal)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_comex_wd](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-comex-thermal)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_from_asic](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-comex-thermal)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_reload_bios](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-comex-thermal)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_sff_wd](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-comex-thermal)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_swb_wd](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-comex-thermal)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/config1](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-config1)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/config2](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-config1)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_ac_pwr_fail](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-ac-pwr-fail)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_platform](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-ac-pwr-fail)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_soc](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-ac-pwr-fail)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_sw_pwr_off](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-ac-pwr-fail)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/pcie_asic_reset_dis](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-pcie-asic-reset-dis)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/vpd_wp](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-vpd-wp)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/voltreg_update_status](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-voltreg-update-status)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/ufm_version](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-ufm-version)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld1_pn](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-cpld1-pn)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld2_pn](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-cpld1-pn)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld3_pn](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-cpld1-pn)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld4_pn](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-cpld1-pn)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld1_version_min](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-cpld1-pn)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld2_version_min](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-cpld1-pn)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld3_version_min](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-cpld1-pn)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld4_version_min](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-cpld1-pn)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/bios_active_image](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-bios-active-image)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/bios_auth_fail](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-bios-active-image)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/bios_upgrade_fail](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-bios-active-image)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc1_enable](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-enable)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc2_enable](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-enable)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc3_enable](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-enable)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc4_enable](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-enable)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc5_enable](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-enable)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc6_enable](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-enable)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc7_enable](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-enable)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc8_enable](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-enable)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc1_pwr](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-pwr)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc2_pwr](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-pwr)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc3_pwr](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-pwr)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc4_pwr](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-pwr)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc5_pwr](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-pwr)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc6_pwr](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-pwr)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc7_pwr](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-pwr)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc8_pwr](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-pwr)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc1_rst_mask](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-rst-mask)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc2_rst_mask](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-rst-mask)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc3_rst_mask](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-rst-mask)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc4_rst_mask](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-rst-mask)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc5_rst_mask](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-rst-mask)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc6_rst_mask](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-rst-mask)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc7_rst_mask](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-rst-mask)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lc8_rst_mask](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lc1-rst-mask)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/os_started](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-os-started)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/pm_mgmt_en](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-pm-mgmt-en)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/psu3_on](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-psu3-on)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/psu4_on](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-psu3-on)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/shutdown_unlock](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-shutdown-unlock)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/cpld1_pn](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-cpld1-pn)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/cpld1_version](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-cpld1-pn)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/cpld1_version_min](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-cpld1-pn)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/fpga1_pn](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-fpga1-pn)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/fpga1_version](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-fpga1-pn)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/fpga1_version_min](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-fpga1-pn)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/vpd_wp](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-vpd-wp)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/reset_aux_pwr_or_ref](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-ref)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/reset_dc_dc_pwr_fail](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-ref)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/reset_fpga_not_done](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-ref)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/reset_from_chassis](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-ref)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/reset_line_card](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-ref)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/reset_pwr_off_from_chassis](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-reset-aux-pwr-or-ref)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/cpld_upgrade_en](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-cpld-upgrade-en)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/fpga_upgrade_en](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-cpld-upgrade-en)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/qsfp_pwr_en](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-qsfp-pwr-en)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/pwr_en](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-qsfp-pwr-en)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/agb_spi_burn_en](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-agb-spi-burn-en)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/fpga_spi_burn_en](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-agb-spi-burn-en)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/max_power](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-max-power)
- [/sys/devices/platform/mlxplat/i2c_mlxcpld.\*/i2c-\*/i2c-\*/i2c-\*/\*-0032/mlxreg-io.\*/hwmon/hwmon\*/config](abi-stable.md#abi-sys-devices-platform-mlxplat-i2c-mlxcpld-i2c-i2c-i2c-0032-mlxreg-io-hwmon-hwmon-max-power)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/phy_reset](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-phy-reset)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/mac_reset](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-mac-reset)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/qsfp_pwr_good](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-qsfp-pwr-good)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/asic2_health](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-asic2-health)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/asic_reset](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-asic-reset)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/asic2_reset](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-asic-reset)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/comm_chnl_ready](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-comm-chnl-ready)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/config3](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-config3)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_pwr_converter_fail](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-pwr-converter-fail)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/erot1_ap_reset](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-erot1-ap-reset)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/erot2_ap_reset](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-erot1-ap-reset)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/erot1_recovery](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-erot1-recovery)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/erot2_recovery](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-erot1-recovery)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/erot1_reset](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-erot1-recovery)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/erot2_reset](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-erot1-recovery)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/erot1_wp](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-erot1-wp)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/erot2_wp](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-erot1-wp)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/spi_chnl_select](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-spi-chnl-select)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/asic_pg_fail](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-asic-pg-fail)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/clk_brd1_boot_fail](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-clk-brd1-boot-fail)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/clk_brd2_boot_fail](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-clk-brd1-boot-fail)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/clk_brd_fail](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-clk-brd1-boot-fail)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/clk_brd_prog_en](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-clk-brd-prog-en)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/pwr_converter_prog_en](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-pwr-converter-prog-en)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_ac_ok_fail](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-ac-ok-fail)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld5_pn](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-cpld5-pn)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld5_version](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-cpld5-pn)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/cpld5_version_min](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-cpld5-pn)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/jtag_cap](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-jtag-cap)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/lid_open](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-lid-open)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_long_pwr_pb](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-long-pwr-pb)
- [/sys/devices/platform/mlxplat/mlxreg-io/hwmon/hwmon\*/reset_swb_dc_dc_pwr_fail](abi-stable.md#abi-sys-devices-platform-mlxplat-mlxreg-io-hwmon-hwmon-reset-swb-dc-dc-pwr-fail)

## File stable/sysfs-driver-qla2xxx

Has the following ABI:

- [/sys/bus/pci/drivers/qla2xxx/.../devices/\*](abi-stable.md#abi-sys-bus-pci-drivers-qla2xxx-devices)

## File stable/sysfs-driver-speakup

Has the following ABI:

- [/sys/accessibility/speakup/attrib_bleep](abi-stable.md#abi-sys-accessibility-speakup-attrib-bleep)
- [/sys/accessibility/speakup/bell_pos](abi-stable.md#abi-sys-accessibility-speakup-bell-pos)
- [/sys/accessibility/speakup/bleeps](abi-stable.md#abi-sys-accessibility-speakup-bleeps)
- [/sys/accessibility/speakup/bleep_time](abi-stable.md#abi-sys-accessibility-speakup-bleep-time)
- [/sys/accessibility/speakup/cursor_time](abi-stable.md#abi-sys-accessibility-speakup-cursor-time)
- [/sys/accessibility/speakup/cur_phonetic](abi-stable.md#abi-sys-accessibility-speakup-cur-phonetic)
- [/sys/accessibility/speakup/delimiters](abi-stable.md#abi-sys-accessibility-speakup-delimiters)
- [/sys/accessibility/speakup/ex_num](abi-stable.md#abi-sys-accessibility-speakup-ex-num)
- [/sys/accessibility/speakup/key_echo](abi-stable.md#abi-sys-accessibility-speakup-key-echo)
- [/sys/accessibility/speakup/keymap](abi-stable.md#abi-sys-accessibility-speakup-keymap)
- [/sys/accessibility/speakup/no_interrupt](abi-stable.md#abi-sys-accessibility-speakup-no-interrupt)
- [/sys/accessibility/speakup/punc_all](abi-stable.md#abi-sys-accessibility-speakup-punc-all)
- [/sys/accessibility/speakup/punc_level](abi-stable.md#abi-sys-accessibility-speakup-punc-level)
- [/sys/accessibility/speakup/punc_most](abi-stable.md#abi-sys-accessibility-speakup-punc-most)
- [/sys/accessibility/speakup/punc_some](abi-stable.md#abi-sys-accessibility-speakup-punc-some)
- [/sys/accessibility/speakup/reading_punc](abi-stable.md#abi-sys-accessibility-speakup-reading-punc)
- [/sys/accessibility/speakup/repeats](abi-stable.md#abi-sys-accessibility-speakup-repeats)
- [/sys/accessibility/speakup/say_control](abi-stable.md#abi-sys-accessibility-speakup-say-control)
- [/sys/accessibility/speakup/say_word_ctl](abi-stable.md#abi-sys-accessibility-speakup-say-word-ctl)
- [/sys/accessibility/speakup/silent](abi-stable.md#abi-sys-accessibility-speakup-silent)
- [/sys/accessibility/speakup/spell_delay](abi-stable.md#abi-sys-accessibility-speakup-spell-delay)
- [/sys/accessibility/speakup/synth](abi-stable.md#abi-sys-accessibility-speakup-synth)
- [/sys/accessibility/speakup/synth_direct](abi-stable.md#abi-sys-accessibility-speakup-synth-direct)
- [/sys/accessibility/speakup/version](abi-stable.md#abi-sys-accessibility-speakup-version)
- [/sys/accessibility/speakup/i18n/announcements](abi-stable.md#abi-sys-accessibility-speakup-i18n-announcements)
- [/sys/accessibility/speakup/i18n/chartab](abi-stable.md#abi-sys-accessibility-speakup-i18n-chartab)
- [/sys/accessibility/speakup/i18n/ctl_keys](abi-stable.md#abi-sys-accessibility-speakup-i18n-ctl-keys)
- [/sys/accessibility/speakup/i18n/function_names](abi-stable.md#abi-sys-accessibility-speakup-i18n-function-names)
- [/sys/accessibility/speakup/i18n/states](abi-stable.md#abi-sys-accessibility-speakup-i18n-states)
- [/sys/accessibility/speakup/i18n/characters](abi-stable.md#abi-sys-accessibility-speakup-i18n-characters)
- [/sys/accessibility/speakup/i18n/colors](abi-stable.md#abi-sys-accessibility-speakup-i18n-colors)
- [/sys/accessibility/speakup/i18n/formatted](abi-stable.md#abi-sys-accessibility-speakup-i18n-formatted)
- [/sys/accessibility/speakup/i18n/key_names](abi-stable.md#abi-sys-accessibility-speakup-i18n-key-names)
- [/sys/accessibility/speakup/<synth-name>/](abi-stable.md#abi-sys-accessibility-speakup-synth-name)
- [/sys/accessibility/speakup/<synth-name>/caps_start](abi-stable.md#abi-sys-accessibility-speakup-synth-name-caps-start)
- [/sys/accessibility/speakup/<synth-name>/caps_stop](abi-stable.md#abi-sys-accessibility-speakup-synth-name-caps-stop)
- [/sys/accessibility/speakup/<synth-name>/delay_time](abi-stable.md#abi-sys-accessibility-speakup-synth-name-delay-time)
- [/sys/accessibility/speakup/<synth-name>/direct](abi-stable.md#abi-sys-accessibility-speakup-synth-name-direct)
- [/sys/accessibility/speakup/<synth-name>/freq](abi-stable.md#abi-sys-accessibility-speakup-synth-name-freq)
- [/sys/accessibility/speakup/<synth-name>/flush_time](abi-stable.md#abi-sys-accessibility-speakup-synth-name-flush-time)
- [/sys/accessibility/speakup/<synth-name>/full_time](abi-stable.md#abi-sys-accessibility-speakup-synth-name-full-time)
- [/sys/accessibility/speakup/<synth-name>/jiffy_delta](abi-stable.md#abi-sys-accessibility-speakup-synth-name-jiffy-delta)
- [/sys/accessibility/speakup/<synth-name>/pitch](abi-stable.md#abi-sys-accessibility-speakup-synth-name-pitch)
- [/sys/accessibility/speakup/<synth-name>/inflection](abi-stable.md#abi-sys-accessibility-speakup-synth-name-inflection)
- [/sys/accessibility/speakup/<synth-name>/punct](abi-stable.md#abi-sys-accessibility-speakup-synth-name-punct)
- [/sys/accessibility/speakup/<synth-name>/rate](abi-stable.md#abi-sys-accessibility-speakup-synth-name-rate)
- [/sys/accessibility/speakup/<synth-name>/tone](abi-stable.md#abi-sys-accessibility-speakup-synth-name-tone)
- [/sys/accessibility/speakup/<synth-name>/trigger_time](abi-stable.md#abi-sys-accessibility-speakup-synth-name-trigger-time)
- [/sys/accessibility/speakup/<synth-name>/voice](abi-stable.md#abi-sys-accessibility-speakup-synth-name-voice)
- [/sys/accessibility/speakup/<synth-name>/vol](abi-stable.md#abi-sys-accessibility-speakup-synth-name-vol)

## File stable/sysfs-driver-usb-usbtmc

Has the following ABI:

- [/sys/bus/usb/drivers/usbtmc/\*/interface_capabilities](abi-stable.md#abi-sys-bus-usb-drivers-usbtmc-interface-capabilities)
- [/sys/bus/usb/drivers/usbtmc/\*/device_capabilities](abi-stable.md#abi-sys-bus-usb-drivers-usbtmc-interface-capabilities)
- [/sys/bus/usb/drivers/usbtmc/\*/usb488_interface_capabilities](abi-stable.md#abi-sys-bus-usb-drivers-usbtmc-usb488-interface-capabilities)
- [/sys/bus/usb/drivers/usbtmc/\*/usb488_device_capabilities](abi-stable.md#abi-sys-bus-usb-drivers-usbtmc-usb488-interface-capabilities)

## File stable/sysfs-driver-w1_ds2438

Has the following ABI:

- [/sys/bus/w1/devices/.../page1](abi-stable.md#abi-sys-bus-w1-devices-page1)
- [/sys/bus/w1/devices/.../offset](abi-stable.md#abi-sys-bus-w1-devices-offset)

## File stable/sysfs-driver-w1_ds28e04

Has the following ABI:

- [/sys/bus/w1/devices/.../pio](abi-stable.md#abi-sys-bus-w1-devices-pio)
- [/sys/bus/w1/devices/.../eeprom](abi-stable.md#abi-sys-bus-w1-devices-eeprom)

## File stable/sysfs-driver-w1_ds28ea00

Has the following ABI:

- [/sys/bus/w1/devices/.../w1_seq](abi-stable.md#abi-sys-bus-w1-devices-w1-seq)

## File stable/sysfs-firmware-efi-vars

Has the following ABI:

- [/sys/firmware/efi/vars](abi-stable.md#abi-sys-firmware-efi-vars)

## File stable/sysfs-firmware-opal-dump

Has the following ABI:

- [/sys/firmware/opal/dump](abi-stable.md#abi-sys-firmware-opal-dump)

## File stable/sysfs-firmware-opal-elog

Has the following ABI:

- [/sys/firmware/opal/elog](abi-stable.md#abi-sys-firmware-opal-elog)

## File stable/sysfs-fs-orangefs

Has the following ABI:

- [/sys/fs/orangefs/perf_counters/\*](abi-stable.md#abi-sys-fs-orangefs-perf-counters)
- [/sys/fs/orangefs/perf_counter_reset](abi-stable.md#abi-sys-fs-orangefs-perf-counter-reset)
- [/sys/fs/orangefs/perf_time_interval_secs](abi-stable.md#abi-sys-fs-orangefs-perf-time-interval-secs)
- [/sys/fs/orangefs/perf_history_size](abi-stable.md#abi-sys-fs-orangefs-perf-history-size)
- [/sys/fs/orangefs/op_timeout_secs](abi-stable.md#abi-sys-fs-orangefs-op-timeout-secs)
- [/sys/fs/orangefs/slot_timeout_secs](abi-stable.md#abi-sys-fs-orangefs-slot-timeout-secs)
- [/sys/fs/orangefs/acache/\*](abi-stable.md#abi-sys-fs-orangefs-acache)
- [/sys/fs/orangefs/ncache/\*](abi-stable.md#abi-sys-fs-orangefs-ncache)
- [/sys/fs/orangefs/capcache/\*](abi-stable.md#abi-sys-fs-orangefs-capcache)
- [/sys/fs/orangefs/ccache/\*](abi-stable.md#abi-sys-fs-orangefs-ccache)

## File stable/sysfs-hypervisor-xen

Has the following ABI:

- [/sys/hypervisor/compilation/compile_date](abi-stable.md#abi-sys-hypervisor-compilation-compile-date)
- [/sys/hypervisor/compilation/compiled_by](abi-stable.md#abi-sys-hypervisor-compilation-compiled-by)
- [/sys/hypervisor/compilation/compiler](abi-stable.md#abi-sys-hypervisor-compilation-compiler)
- [/sys/hypervisor/properties/capabilities](abi-stable.md#abi-sys-hypervisor-properties-capabilities)
- [/sys/hypervisor/properties/changeset](abi-stable.md#abi-sys-hypervisor-properties-changeset)
- [/sys/hypervisor/properties/features](abi-stable.md#abi-sys-hypervisor-properties-features)
- [/sys/hypervisor/properties/pagesize](abi-stable.md#abi-sys-hypervisor-properties-pagesize)
- [/sys/hypervisor/properties/virtual_start](abi-stable.md#abi-sys-hypervisor-properties-virtual-start)
- [/sys/hypervisor/type](abi-stable.md#abi-sys-hypervisor-type)
- [/sys/hypervisor/uuid](abi-stable.md#abi-sys-hypervisor-uuid)
- [/sys/hypervisor/version/extra](abi-stable.md#abi-sys-hypervisor-version-extra)
- [/sys/hypervisor/version/major](abi-stable.md#abi-sys-hypervisor-version-major)
- [/sys/hypervisor/version/minor](abi-stable.md#abi-sys-hypervisor-version-minor)
- [/sys/hypervisor/start_flags/\*](abi-stable.md#abi-sys-hypervisor-start-flags)

## File stable/sysfs-kernel-notes

Has the following ABI:

- [/sys/kernel/notes](abi-stable.md#abi-sys-kernel-notes)

## File stable/sysfs-module

The /sys/module tree consists of the following structure:

Has the following ABI:

- [/sys/module/<MODULENAME>](abi-stable.md#abi-sys-module-modulename)
- [/sys/module/<MODULENAME>/parameters](abi-stable.md#abi-sys-module-modulename-parameters)
- [/sys/module/<MODULENAME>/refcnt](abi-stable.md#abi-sys-module-modulename-refcnt)
- [/sys/module/<MODULENAME>/srcversion](abi-stable.md#abi-sys-module-modulename-srcversion)
- [/sys/module/<MODULENAME>/version](abi-stable.md#abi-sys-module-modulename-version)

## File stable/sysfs-platform-wmi-bmof

Has the following ABI:

- [/sys/bus/wmi/devices/05901221-D566-11D1-B2F0-00A0C9062910[-X]/bmof](abi-stable.md#abi-sys-bus-wmi-devices-05901221-d566-11d1-b2f0-00a0c9062910-x-bmof)

## File stable/sysfs-transport-srp

Has the following ABI:

- [/sys/class/srp_remote_ports/port-<h>:<n>/delete](abi-stable.md#abi-sys-class-srp-remote-ports-port-h-n-delete)
- [/sys/class/srp_remote_ports/port-<h>:<n>/dev_loss_tmo](abi-stable.md#abi-sys-class-srp-remote-ports-port-h-n-dev-loss-tmo)
- [/sys/class/srp_remote_ports/port-<h>:<n>/fast_io_fail_tmo](abi-stable.md#abi-sys-class-srp-remote-ports-port-h-n-fast-io-fail-tmo)
- [/sys/class/srp_remote_ports/port-<h>:<n>/port_id](abi-stable.md#abi-sys-class-srp-remote-ports-port-h-n-port-id)
- [/sys/class/srp_remote_ports/port-<h>:<n>/reconnect_delay](abi-stable.md#abi-sys-class-srp-remote-ports-port-h-n-reconnect-delay)
- [/sys/class/srp_remote_ports/port-<h>:<n>/roles](abi-stable.md#abi-sys-class-srp-remote-ports-port-h-n-roles)
- [/sys/class/srp_remote_ports/port-<h>:<n>/state](abi-stable.md#abi-sys-class-srp-remote-ports-port-h-n-state)

## File stable/thermal-notification

Has the following ABI:

- [A notification mechanism for thermal related events](abi-stable.md#abi-a-notification-mechanism-for-thermal-related-events)

## File stable/vdso

Has the following ABI:

- [vDSO](abi-stable.md#abi-vdso)
