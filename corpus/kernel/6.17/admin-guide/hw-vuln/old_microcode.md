---
collection: kernel
version: "6.17"
title: "Old Microcode"
source_url: https://www.kernel.org/doc/html/v6.17/admin-guide/hw-vuln/old_microcode.html
fetched_at: 2026-09-16T16:47:39+00:00
---
# Old Microcode

The kernel keeps a table of released microcode. Systems that had
microcode older than this at boot will say “Vulnerable”. This means
that the system was vulnerable to some known CPU issue. It could be
security or functional, the kernel does not know or care.

You should update the CPU microcode to mitigate any exposure. This is
usually accomplished by updating the files in
/lib/firmware/intel-ucode/ via normal distribution updates. Intel also
distributes these files in a github repo:

> <https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files.git>

Just like all the other hardware vulnerabilities, exposure is
determined at boot. Runtime microcode updates do not change the status
of this vulnerability.
