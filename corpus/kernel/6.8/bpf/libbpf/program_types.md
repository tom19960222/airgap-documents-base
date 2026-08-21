---
collection: kernel
version: "6.8"
title: "Program Types and ELF Sections"
source_url: https://www.kernel.org/doc/html/v6.8/bpf/libbpf/program_types.html
fetched_at: 2026-08-21T04:01:04+00:00
---
# Program Types and ELF Sections

The table below lists the program types, their attach types where relevant and the ELF section
names supported by libbpf for them. The ELF section names follow these rules:

- `type` is an exact match, e.g. `SEC("socket")`
- `type+` means it can be either exact `SEC("type")` or well-formed `SEC("type/extras")`
  with a '`/`' separator between `type` and `extras`.

When `extras` are specified, they provide details of how to auto-attach the BPF program. The
format of `extras` depends on the program type, e.g. `SEC("tracepoint/<category>/<name>")`
for tracepoints or `SEC("usdt/<path>:<provider>:<name>")` for USDT probes. The extras are
described in more detail in the footnotes.

| Program Type | Attach Type | ELF Section Name | Sleepable |
| --- | --- | --- | --- |
| `BPF_PROG_TYPE_CGROUP_DEVICE` | `BPF_CGROUP_DEVICE` | `cgroup/dev` |  |
| `BPF_PROG_TYPE_CGROUP_SKB` |  | `cgroup/skb` |  |
| `BPF_CGROUP_INET_EGRESS` | `cgroup_skb/egress` |  |
| `BPF_CGROUP_INET_INGRESS` | `cgroup_skb/ingress` |  |
| `BPF_PROG_TYPE_CGROUP_SOCKOPT` | `BPF_CGROUP_GETSOCKOPT` | `cgroup/getsockopt` |  |
| `BPF_CGROUP_SETSOCKOPT` | `cgroup/setsockopt` |  |
| `BPF_PROG_TYPE_CGROUP_SOCK_ADDR` | `BPF_CGROUP_INET4_BIND` | `cgroup/bind4` |  |
| `BPF_CGROUP_INET4_CONNECT` | `cgroup/connect4` |  |
| `BPF_CGROUP_INET4_GETPEERNAME` | `cgroup/getpeername4` |  |
| `BPF_CGROUP_INET4_GETSOCKNAME` | `cgroup/getsockname4` |  |
| `BPF_CGROUP_INET6_BIND` | `cgroup/bind6` |  |
| `BPF_CGROUP_INET6_CONNECT` | `cgroup/connect6` |  |
| `BPF_CGROUP_INET6_GETPEERNAME` | `cgroup/getpeername6` |  |
| `BPF_CGROUP_INET6_GETSOCKNAME` | `cgroup/getsockname6` |  |
| `BPF_CGROUP_UDP4_RECVMSG` | `cgroup/recvmsg4` |  |
| `BPF_CGROUP_UDP4_SENDMSG` | `cgroup/sendmsg4` |  |
| `BPF_CGROUP_UDP6_RECVMSG` | `cgroup/recvmsg6` |  |
| `BPF_CGROUP_UDP6_SENDMSG` | `cgroup/sendmsg6` |  |
| `BPF_CGROUP_UNIX_CONNECT` | `cgroup/connect_unix` |  |
| `BPF_CGROUP_UNIX_SENDMSG` | `cgroup/sendmsg_unix` |  |
| `BPF_CGROUP_UNIX_RECVMSG` | `cgroup/recvmsg_unix` |  |
| `BPF_CGROUP_UNIX_GETPEERNAME` | `cgroup/getpeername_unix` |  |
| `BPF_CGROUP_UNIX_GETSOCKNAME` | `cgroup/getsockname_unix` |  |
| `BPF_PROG_TYPE_CGROUP_SOCK` | `BPF_CGROUP_INET4_POST_BIND` | `cgroup/post_bind4` |  |
| `BPF_CGROUP_INET6_POST_BIND` | `cgroup/post_bind6` |  |
| `BPF_CGROUP_INET_SOCK_CREATE` | `cgroup/sock_create` |  |
| `cgroup/sock` |  |
| `BPF_CGROUP_INET_SOCK_RELEASE` | `cgroup/sock_release` |  |
| `BPF_PROG_TYPE_CGROUP_SYSCTL` | `BPF_CGROUP_SYSCTL` | `cgroup/sysctl` |  |
| `BPF_PROG_TYPE_EXT` |  | `freplace+` [1](program_types.md#fentry) |  |
| `BPF_PROG_TYPE_FLOW_DISSECTOR` | `BPF_FLOW_DISSECTOR` | `flow_dissector` |  |
| `BPF_PROG_TYPE_KPROBE` |  | `kprobe+` [2](program_types.md#kprobe) |  |
| `kretprobe+` [2](program_types.md#kprobe) |  |
| `ksyscall+` [3](program_types.md#ksyscall) |  |
| `kretsyscall+` [3](program_types.md#ksyscall) |  |
| `uprobe+` [4](program_types.md#uprobe) |  |
| `uprobe.s+` [4](program_types.md#uprobe) | Yes |
| `uretprobe+` [4](program_types.md#uprobe) |  |
| `uretprobe.s+` [4](program_types.md#uprobe) | Yes |
| `usdt+` [5](program_types.md#usdt) |  |
| `BPF_TRACE_KPROBE_MULTI` | `kprobe.multi+` [6](program_types.md#kpmulti) |  |
| `kretprobe.multi+` [6](program_types.md#kpmulti) |  |
| `BPF_PROG_TYPE_LIRC_MODE2` | `BPF_LIRC_MODE2` | `lirc_mode2` |  |
| `BPF_PROG_TYPE_LSM` | `BPF_LSM_CGROUP` | `lsm_cgroup+` |  |
| `BPF_LSM_MAC` | `lsm+` [7](program_types.md#lsm) |  |
| `lsm.s+` [7](program_types.md#lsm) | Yes |
| `BPF_PROG_TYPE_LWT_IN` |  | `lwt_in` |  |
| `BPF_PROG_TYPE_LWT_OUT` |  | `lwt_out` |  |
| `BPF_PROG_TYPE_LWT_SEG6LOCAL` |  | `lwt_seg6local` |  |
| `BPF_PROG_TYPE_LWT_XMIT` |  | `lwt_xmit` |  |
| `BPF_PROG_TYPE_PERF_EVENT` |  | `perf_event` |  |
| `BPF_PROG_TYPE_RAW_TRACEPOINT_WRITABLE` |  | `raw_tp.w+` [8](program_types.md#rawtp) |  |
| `raw_tracepoint.w+` |  |
| `BPF_PROG_TYPE_RAW_TRACEPOINT` |  | `raw_tp+` [8](program_types.md#rawtp) |  |
| `raw_tracepoint+` |  |
| `BPF_PROG_TYPE_SCHED_ACT` |  | `action` |  |
| `BPF_PROG_TYPE_SCHED_CLS` |  | `classifier` |  |
| `tc` |  |
| `BPF_PROG_TYPE_SK_LOOKUP` | `BPF_SK_LOOKUP` | `sk_lookup` |  |
| `BPF_PROG_TYPE_SK_MSG` | `BPF_SK_MSG_VERDICT` | `sk_msg` |  |
| `BPF_PROG_TYPE_SK_REUSEPORT` | `BPF_SK_REUSEPORT_SELECT_OR_MIGRATE` | `sk_reuseport/migrate` |  |
| `BPF_SK_REUSEPORT_SELECT` | `sk_reuseport` |  |
| `BPF_PROG_TYPE_SK_SKB` |  | `sk_skb` |  |
| `BPF_SK_SKB_STREAM_PARSER` | `sk_skb/stream_parser` |  |
| `BPF_SK_SKB_STREAM_VERDICT` | `sk_skb/stream_verdict` |  |
| `BPF_PROG_TYPE_SOCKET_FILTER` |  | `socket` |  |
| `BPF_PROG_TYPE_SOCK_OPS` | `BPF_CGROUP_SOCK_OPS` | `sockops` |  |
| `BPF_PROG_TYPE_STRUCT_OPS` |  | `struct_ops+` |  |
| `BPF_PROG_TYPE_SYSCALL` |  | `syscall` | Yes |
| `BPF_PROG_TYPE_TRACEPOINT` |  | `tp+` [9](program_types.md#tp) |  |
| `tracepoint+` [9](program_types.md#tp) |  |
| `BPF_PROG_TYPE_TRACING` | `BPF_MODIFY_RETURN` | `fmod_ret+` [1](program_types.md#fentry) |  |
| `fmod_ret.s+` [1](program_types.md#fentry) | Yes |
| `BPF_TRACE_FENTRY` | `fentry+` [1](program_types.md#fentry) |  |
| `fentry.s+` [1](program_types.md#fentry) | Yes |
| `BPF_TRACE_FEXIT` | `fexit+` [1](program_types.md#fentry) |  |
| `fexit.s+` [1](program_types.md#fentry) | Yes |
| `BPF_TRACE_ITER` | `iter+` [10](program_types.md#iter) |  |
| `iter.s+` [10](program_types.md#iter) | Yes |
| `BPF_TRACE_RAW_TP` | `tp_btf+` [1](program_types.md#fentry) |  |
| `BPF_PROG_TYPE_XDP` | `BPF_XDP_CPUMAP` | `xdp.frags/cpumap` |  |
| `xdp/cpumap` |  |
| `BPF_XDP_DEVMAP` | `xdp.frags/devmap` |  |
| `xdp/devmap` |  |
| `BPF_XDP` | `xdp.frags` |  |
| `xdp` |  |

Footnotes

1([1](program_types.md#id1),[2](program_types.md#id19),[3](program_types.md#id20),[4](program_types.md#id21),[5](program_types.md#id22),[6](program_types.md#id23),[7](program_types.md#id24),[8](program_types.md#id27))
:   The `fentry` attach format is `fentry[.s]/<function>`.

2([1](program_types.md#id2),[2](program_types.md#id3))
:   The `kprobe` attach format is `kprobe/<function>[+<offset>]`. Valid
    characters for `function` are `a-zA-Z0-9_.` and `offset` must be a valid
    non-negative integer.

3([1](program_types.md#id4),[2](program_types.md#id5))
:   The `ksyscall` attach format is `ksyscall/<syscall>`.

4([1](program_types.md#id6),[2](program_types.md#id7),[3](program_types.md#id8),[4](program_types.md#id9))
:   The `uprobe` attach format is `uprobe[.s]/<path>:<function>[+<offset>]`.

[5](program_types.md#id10)
:   The `usdt` attach format is `usdt/<path>:<provider>:<name>`.

6([1](program_types.md#id11),[2](program_types.md#id12))
:   The `kprobe.multi` attach format is `kprobe.multi/<pattern>` where `pattern`
    supports `*` and `?` wildcards. Valid characters for pattern are
    `a-zA-Z0-9_.*?`.

7([1](program_types.md#id13),[2](program_types.md#id14))
:   The `lsm` attachment format is `lsm[.s]/<hook>`.

8([1](program_types.md#id15),[2](program_types.md#id16))
:   The `raw_tp` attach format is `raw_tracepoint[.w]/<tracepoint>`.

9([1](program_types.md#id17),[2](program_types.md#id18))
:   The `tracepoint` attach format is `tracepoint/<category>/<name>`.

10([1](program_types.md#id25),[2](program_types.md#id26))
:   The `iter` attach format is `iter[.s]/<struct-name>`.
