---
collection: kernel
version: "6.8"
title: "CPUFreq - CPU frequency and voltage scaling code in the Linux(TM) kernel"
source_url: https://www.kernel.org/doc/html/v6.8/cpu-freq/index.html
fetched_at: 2026-08-21T03:33:02+00:00
---
English

- [Chinese (Simplified)](../translations/zh_CN/cpu-freq/index.md)
- [Chinese (Traditional)](../translations/zh_TW/cpu-freq/index.md)

# CPUFreq - CPU frequency and voltage scaling code in the Linux(TM) kernel

Author: Dominik Brodowski <[linux@brodo.de](mailto:linux%40brodo.de)>

> Clock scaling allows you to change the clock speed of the CPUs on the
> fly. This is a nice method to save battery power, because the lower
> the clock speed, the less power the CPU consumes.

- [General description of the CPUFreq core and CPUFreq notifiers](core.md)
- [How to Implement a new CPUFreq Processor Driver](cpu-drivers.md)
- [General Description of sysfs CPUFreq Stats](cpufreq-stats.md)

## Mailing List

There is a CPU frequency general list where you can report bugs,
problems or submit patches. To post a message, send an email to
[linux-pm@vger.kernel.org](mailto:linux-pm%40vger.kernel.org).

## Links

the FTP archives:
\* <ftp://ftp.linux.org.uk/pub/linux/cpufreq/>

the CPUFreq Mailing list:
\* <http://vger.kernel.org/vger-lists.html#linux-pm>

Clock and voltage scaling for the SA-1100:
\* <http://www.lartmaker.nl/projects/scaling>
