---
collection: kernel
version: "6.8"
title: "libbpf"
source_url: https://www.kernel.org/doc/html/v6.8/bpf/libbpf/index.html
fetched_at: 2026-08-21T03:53:59+00:00
---
# libbpf

If you are looking to develop BPF applications using the libbpf library, this
directory contains important documentation that you should read.

To get started, it is recommended to begin with the [libbpf Overview](libbpf_overview.md) document, which provides a high-level understanding of the
libbpf APIs and their usage. This will give you a solid foundation to start
exploring and utilizing the various features of libbpf to develop your BPF
applications.

- [libbpf Overview](libbpf_overview.md)
- [API Documentation](https://libbpf.readthedocs.io/en/latest/api.html)
- [Program Types and ELF Sections](program_types.md)
- [API naming convention](libbpf_naming_convention.md)
- [API documentation convention](libbpf_naming_convention.md#api-documentation-convention)
- [Building libbpf](libbpf_build.md)

All general BPF questions, including kernel functionality, libbpf APIs and their
application, should be sent to [bpf@vger.kernel.org](mailto:bpf%40vger.kernel.org) mailing list. You can
[subscribe](http://vger.kernel.org/vger-lists.html#bpf) to the mailing list
search its [archive](https://lore.kernel.org/bpf/). Please search the archive
before asking new questions. It may be that this was already addressed or
answered before.
