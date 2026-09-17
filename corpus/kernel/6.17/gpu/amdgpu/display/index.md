---
collection: kernel
version: "6.17"
title: "drm/amd/display - Display Core (DC)"
source_url: https://www.kernel.org/doc/html/v6.17/gpu/amdgpu/display/index.html
fetched_at: 2026-09-16T16:39:21+00:00
---
# drm/amd/display - Display Core (DC)

AMD display engine is partially shared with other operating systems; for this
reason, our Display Core Driver is divided into two pieces:

1. **Display Core (DC)** contains the OS-agnostic components. Things like
   hardware programming and resource management are handled here.
2. **Display Manager (DM)** contains the OS-dependent components. Hooks to the
   amdgpu base driver and DRM are implemented here. For example, you can check
   display/amdgpu_dm/ folder.

## DC Code validation

Maintaining the same code base across multiple OSes requires a lot of
synchronization effort between repositories and exhaustive validation. In the
DC case, we maintain a tree to centralize code from different parts. The shared
repository has integration tests with our Internal Linux CI farm, and we run a
comprehensive set of IGT tests in various AMD GPUs/APUs (mostly recent dGPUs
and APUs). Our CI also checks ARM64/32, PPC64/32, and x86_64/32 compilation
with DCN enabled and disabled.

When we upstream a new feature or some patches, we pack them in a patchset with
the prefix **DC Patches for <DATE>**, which is created based on the latest
[amd-staging-drm-next](https://gitlab.freedesktop.org/agd5f/linux). All of
those patches are under a DC version tested as follows:

- Ensure that every patch compiles and the entire series pass our set of IGT
  test in different hardware.
- Prepare a branch with those patches for our validation team. If there is an
  error, a developer will debug as fast as possible; usually, a simple bisect
  in the series is enough to point to a bad change, and two possible actions
  emerge: fix the issue or drop the patch. If it is not an easy fix, the bad
  patch is dropped.
- Finally, developers wait a few days for community feedback before we merge
  the series.

It is good to stress that the test phase is something that we take extremely
seriously, and we never merge anything that fails our validation. Follows an
overview of our test set:

1. Manual test
   :   - Multiple Hotplugs with DP and HDMI.
       - Stress test with multiple display configuration changes via the user interface.
       - Validate VRR behaviour.
       - Check PSR.
       - Validate MPO when playing video.
       - Test more than two displays connected at the same time.
       - Check suspend/resume.
       - Validate FPO.
       - Check MST.
2. Automated test
   :   - IGT tests in a farm with GPUs and APUs that support DCN and DCE.
       - Compilation validation with the latest GCC and Clang from LTS distro.
       - Cross-compilation for PowerPC 64/32, ARM 64/32, and x86 32.

In terms of test setup for CI and manual tests, we usually use:

1. The latest Ubuntu LTS.
2. In terms of userspace, we only use fully updated open-source components
   provided by the distribution official package manager.
3. Regarding IGT, we use the latest code from the upstream.
4. Most of the manual tests are conducted in the GNome but we also use KDE.

Notice that someone from our test team will always reply to the cover letter
with the test report.

## DC Information

The display pipe is responsible for “scanning out” a rendered frame from the
GPU memory (also called VRAM, FrameBuffer, etc.) to a display. In other words,
it would:

1. Read frame information from memory;
2. Perform required transformation;
3. Send pixel data to sink devices.

If you want to learn more about our driver details, take a look at the below
table of content:

- [AMDgpu Display Manager](display-manager.md)
  - [Lifecycle](display-manager.md#lifecycle)
  - [Interrupts](display-manager.md#interrupts)
  - [Atomic Implementation](display-manager.md#atomic-implementation)
  - [Color Management Properties](display-manager.md#color-management-properties)
    - [DC Color Capabilities between DCN generations](display-manager.md#dc-color-capabilities-between-dcn-generations)
  - [Blend Mode Properties](display-manager.md#blend-mode-properties)
    - [Blend configuration flow](display-manager.md#blend-configuration-flow)
- [Display Core Next (DCN)](dcn-overview.md)
  - [Front End and Back End](dcn-overview.md#front-end-and-back-end)
  - [Data Flow](dcn-overview.md#data-flow)
  - [AMD Hardware Pipeline](dcn-overview.md#amd-hardware-pipeline)
  - [Global Sync](dcn-overview.md#global-sync)
- [DCN Blocks](dcn-blocks.md)
  - [DCHUBBUB](dcn-blocks.md#dchubbub)
  - [HUBP](dcn-blocks.md#hubp)
  - [DPP](dcn-blocks.md#dpp)
  - [MPC](dcn-blocks.md#mpc)
  - [OPP](dcn-blocks.md#opp)
  - [DIO](dcn-blocks.md#dio)
- [DC Programming Model](programming-model-dcn.md)
  - [Overview](programming-model-dcn.md#overview)
  - [Display Driver Architecture Overview](programming-model-dcn.md#display-driver-architecture-overview)
    - [Basic Objects](programming-model-dcn.md#basic-objects)
    - [Basic Operations](programming-model-dcn.md#basic-operations)
- [Multiplane Overlay (MPO)](mpo-overview.md)
  - [Plane Restrictions](mpo-overview.md#plane-restrictions)
  - [Cursor Restrictions](mpo-overview.md#cursor-restrictions)
  - [Use Cases](mpo-overview.md#use-cases)
    - [Picture-in-Picture (PIP) playback - Underlay strategy](mpo-overview.md#picture-in-picture-pip-playback-underlay-strategy)
    - [Multiple Display MPO](mpo-overview.md#multiple-display-mpo)
      - [Limitations](mpo-overview.md#limitations)
- [Display Core Debug tools](dc-debug.md)
  - [Narrow down display issues](dc-debug.md#narrow-down-display-issues)
    - [DC dmesg important messages](dc-debug.md#dc-dmesg-important-messages)
    - [Avoid loading display core](dc-debug.md#avoid-loading-display-core)
    - [Display flickering](dc-debug.md#display-flickering)
    - [Display artifacts](dc-debug.md#display-artifacts)
  - [Disabling/Enabling specific features](dc-debug.md#disabling-enabling-specific-features)
  - [DC Visual Confirmation](dc-debug.md#dc-visual-confirmation)
    - [Multiple Planes Debug](dc-debug.md#multiple-planes-debug)
    - [Pipe Split Debug](dc-debug.md#pipe-split-debug)
  - [DTN Debug](dc-debug.md#dtn-debug)
  - [Collect Firmware information](dc-debug.md#collect-firmware-information)
  - [DMUB Firmware Debug](dc-debug.md#dmub-firmware-debug)
    - [Trace Groups](dc-debug.md#trace-groups)
- [AMDGPU - Display Contributions](display-contributing.md)
  - [Gitlab issues](display-contributing.md#gitlab-issues)
  - [IGT](display-contributing.md#igt)
  - [Compilation](display-contributing.md#compilation)
    - [Fix compilation warnings](display-contributing.md#fix-compilation-warnings)
    - [Fix compilation issues when using um architecture](display-contributing.md#fix-compilation-issues-when-using-um-architecture)
  - [Code Refactor](display-contributing.md#code-refactor)
    - [Add prefix to DC functions to improve the debug with ftrace](display-contributing.md#add-prefix-to-dc-functions-to-improve-the-debug-with-ftrace)
    - [Reduce code duplication](display-contributing.md#reduce-code-duplication)
    - [Make atomic_commit_[check|tail] more readable](display-contributing.md#make-atomic-commit-check-tail-more-readable)
  - [Documentation](display-contributing.md#documentation)
    - [Expand kernel-doc](display-contributing.md#expand-kernel-doc)
  - [Beyond AMDGPU](display-contributing.md#beyond-amdgpu)
    - [Enable underlay](display-contributing.md#enable-underlay)
    - [Adaptive Backlight Modulation (ABM)](display-contributing.md#adaptive-backlight-modulation-abm)
    - [HDR & Color management & VRR](display-contributing.md#hdr-color-management-vrr)
- [DC Glossary](dc-glossary.md)
