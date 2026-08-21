---
collection: kernel
version: "6.8"
title: "Module Parameters"
source_url: https://www.kernel.org/doc/html/v6.8/gpu/amdgpu/module-parameters.html
fetched_at: 2026-08-21T03:38:37+00:00
---
# Module Parameters

The amdgpu driver supports the following module parameters:

**vramlimit (int)**

Restrict the total amount of VRAM in MiB for testing. The default is 0 (Use full VRAM).

**vis_vramlimit (int)**

Restrict the amount of CPU visible VRAM in MiB for testing. The default is 0 (Use full CPU visible VRAM).

**gartsize (uint)**

Restrict the size of GART (for kernel use) in Mib (32, 64, etc.) for testing.
The default is -1 (The size depends on asic).

**gttsize (int)**

Restrict the size of GTT domain (for userspace use) in MiB for testing.
The default is -1 (Use 1/2 RAM, minimum value is 3GB).

**moverate (int)**

Set maximum buffer migration rate in MB/s. The default is -1 (8 MB/s).

**audio (int)**

Set HDMI/DPAudio. Only affects non-DC display handling. The default is -1 (Enabled), set 0 to disabled it.

**disp_priority (int)**

Set display Priority (1 = normal, 2 = high). Only affects non-DC display handling. The default is 0 (auto).

**hw_i2c (int)**

To enable hw i2c engine. Only affects non-DC display handling. The default is 0 (Disabled).

**pcie_gen2 (int)**

To disable PCIE Gen2/3 mode (0 = disable, 1 = enable). The default is -1 (auto, enabled).

**msi (int)**

To disable Message Signaled Interrupts (MSI) functionality (1 = enable, 0 = disable). The default is -1 (auto, enabled).

**lockup_timeout (string)**

Set GPU scheduler timeout value in ms.

The format can be [Non-Compute] or [GFX,Compute,SDMA,Video]. That is there can be one or
multiple values specified. 0 and negative values are invalidated. They will be adjusted
to the default timeout.

- With one value specified, the setting will apply to all non-compute jobs.
- With multiple values specified, the first one will be for GFX.
  The second one is for Compute. The third and fourth ones are
  for SDMA and Video.

By default(with no lockup_timeout settings), the timeout for all non-compute(GFX, SDMA and Video)
jobs is 10000. The timeout for compute is 60000.

**dpm (int)**

Override for dynamic power management setting
(0 = disable, 1 = enable)
The default is -1 (auto).

**fw_load_type (int)**

Set different firmware loading type for debugging, if supported.
Set to 0 to force direct loading if supported by the ASIC. Set
to -1 to select the default loading mode for the ASIC, as defined
by the driver. The default is -1 (auto).

**aspm (int)**

To disable ASPM (1 = enable, 0 = disable). The default is -1 (auto, enabled).

**runpm (int)**

Override for runtime power management control for dGPUs. The amdgpu driver can dynamically power down
the dGPUs when they are idle if supported. The default is -1 (auto enable).
Setting the value to 0 disables this functionality.
Setting the value to -2 is auto enabled with power down when displays are attached.

**ip_block_mask (uint)**

Override what IP blocks are enabled on the GPU. Each GPU is a collection of IP blocks (gfx, display, video, etc.).
Use this parameter to disable specific blocks. Note that the IP blocks do not have a fixed index. Some asics may not have
some IPs or may include multiple instances of an IP so the ordering various from asic to asic. See the driver output in
the kernel log for the list of IPs on the asic. The default is 0xffffffff (enable all blocks on a device).

**bapm (int)**

Bidirectional Application Power Management (BAPM) used to dynamically share TDP between CPU and GPU. Set value 0 to disable it.
The default -1 (auto, enabled)

**deep_color (int)**

Set 1 to enable Deep Color support. Only affects non-DC display handling. The default is 0 (disabled).

**vm_size (int)**

Override the size of the GPU's per client virtual address space in GiB. The default is -1 (automatic for each asic).

**vm_fragment_size (int)**

Override VM fragment size in bits (4, 5, etc. 4 = 64K, 9 = 2M). The default is -1 (automatic for each asic).

**vm_block_size (int)**

Override VM page table size in bits (default depending on vm_size and hw setup). The default is -1 (automatic for each asic).

**vm_fault_stop (int)**

Stop on VM fault for debugging (0 = never, 1 = print first, 2 = always). The default is 0 (No stop).

**vm_update_mode (int)**

Override VM update mode. VM updated by using CPU (0 = never, 1 = Graphics only, 2 = Compute only, 3 = Both). The default
is -1 (Only in large BAR(LB) systems Compute VM tables will be updated by CPU, otherwise 0, never).

**exp_hw_support (int)**

Enable experimental hw support (1 = enable). The default is 0 (disabled).

**dc (int)**

Disable/Enable Display Core driver for debugging (1 = enable, 0 = disable). The default is -1 (automatic for each asic).

**sched_jobs (int)**

Override the max number of jobs supported in the sw queue. The default is 32.

**sched_hw_submission (int)**

Override the max number of HW submissions. The default is 2.

**ppfeaturemask (hexint)**

Override power features enabled. See enum PP_FEATURE_MASK in drivers/gpu/drm/amd/include/amd_shared.h.
The default is the current set of stable power features.

**forcelongtraining (uint)**

Force long memory training in resume.
The default is zero, indicates short training in resume.

**pcie_gen_cap (uint)**

Override PCIE gen speed capabilities. See the CAIL flags in drivers/gpu/drm/amd/include/amd_pcie.h.
The default is 0 (automatic for each asic).

**pcie_lane_cap (uint)**

Override PCIE lanes capabilities. See the CAIL flags in drivers/gpu/drm/amd/include/amd_pcie.h.
The default is 0 (automatic for each asic).

**cg_mask (ullong)**

Override Clockgating features enabled on GPU (0 = disable clock gating). See the AMD_CG_SUPPORT flags in
drivers/gpu/drm/amd/include/amd_shared.h. The default is 0xffffffffffffffff (all enabled).

**pg_mask (uint)**

Override Powergating features enabled on GPU (0 = disable power gating). See the AMD_PG_SUPPORT flags in
drivers/gpu/drm/amd/include/amd_shared.h. The default is 0xffffffff (all enabled).

**sdma_phase_quantum (uint)**

Override SDMA context switch phase quantum (x 1K GPU clock cycles, 0 = no change). The default is 32.

**disable_cu (charp)**

Set to disable CUs (It's set like se.sh.cu,...). The default is NULL.

**virtual_display (charp)**

Set to enable virtual display feature. This feature provides a virtual display hardware on headless boards
or in virtualized environments. It will be set like xxxx:xx:xx.x,x;xxxx:xx:xx.x,x. It's the pci address of
the device, plus the number of crtcs to expose. E.g., 0000:26:00.0,4 would enable 4 virtual crtcs on the pci
device at 26:00.0. The default is NULL.

**lbpw (int)**

Override Load Balancing Per Watt (LBPW) support (1 = enable, 0 = disable). The default is -1 (auto, enabled).

**gpu_recovery (int)**

Set to enable GPU recovery mechanism (1 = enable, 0 = disable). The default is -1 (auto, disabled except SRIOV).

**emu_mode (int)**

Set value 1 to enable emulation mode. This is only needed when running on an emulator. The default is 0 (disabled).

**ras_enable (int)**

Enable RAS features on the GPU (0 = disable, 1 = enable, -1 = auto (default))

**ras_mask (uint)**

Mask of RAS features to enable (default 0xffffffff), only valid when ras_enable == 1
See the flags in drivers/gpu/drm/amd/amdgpu/amdgpu_ras.h

**timeout_fatal_disable (bool)**

Disable Watchdog timeout fatal error event

**timeout_period (uint)**

Modify the watchdog timeout max_cycles as (1 << period)

**si_support (int)**

Set SI support driver. This parameter works after set config CONFIG_DRM_AMDGPU_SI. For SI asic, when radeon driver is enabled,
set value 0 to use radeon driver, while set value 1 to use amdgpu driver. The default is using radeon driver when it available,
otherwise using amdgpu driver.

**cik_support (int)**

Set CIK support driver. This parameter works after set config CONFIG_DRM_AMDGPU_CIK. For CIK asic, when radeon driver is enabled,
set value 0 to use radeon driver, while set value 1 to use amdgpu driver. The default is using radeon driver when it available,
otherwise using amdgpu driver.

**smu_memory_pool_size (uint)**

It is used to reserve gtt for smu debug usage, setting value 0 to disable it. The actual size is value \* 256MiB.
E.g. 0x1 = 256Mbyte, 0x2 = 512Mbyte, 0x4 = 1 Gbyte, 0x8 = 2GByte. The default is 0 (disabled).

**async_gfx_ring (int)**

It is used to enable gfx rings that could be configured with different prioritites or equal priorities

**mcbp (int)**

It is used to enable mid command buffer preemption. (0 = disabled, 1 = enabled, -1 auto (default))

**discovery (int)**

Allow driver to discover hardware IP information from IP Discovery table at the top of VRAM.
(-1 = auto (default), 0 = disabled, 1 = enabled, 2 = use ip_discovery table from file)

**mes (int)**

Enable Micro Engine Scheduler. This is a new hw scheduling engine for gfx, sdma, and compute.
(0 = disabled (default), 1 = enabled)

**mes_kiq (int)**

Enable Micro Engine Scheduler KIQ. This is a new engine pipe for kiq.
(0 = disabled (default), 1 = enabled)

**noretry (int)**

Disable XNACK retry in the SQ by default on GFXv9 hardware. On ASICs that
do not support per-process XNACK this also disables retry page faults.
(0 = retry enabled, 1 = retry disabled, -1 auto (default))

**force_asic_type (int)**

A non negative value used to specify the asic type for all supported GPUs.

**use_xgmi_p2p (int)**

Enables/disables XGMI P2P interface (0 = disable, 1 = enable).

**sched_policy (int)**

Set scheduling policy. Default is HWS(hardware scheduling) with over-subscription.
Setting 1 disables over-subscription. Setting 2 disables HWS and statically
assigns queues to HQDs.

**hws_max_conc_proc (int)**

Maximum number of processes that HWS can schedule concurrently. The maximum is the
number of VMIDs assigned to the HWS, which is also the default.

**cwsr_enable (int)**

CWSR(compute wave store and resume) allows the GPU to preempt shader execution in
the middle of a compute wave. Default is 1 to enable this feature. Setting 0
disables it.

**max_num_of_queues_per_device (int)**

Maximum number of queues per device. Valid setting is between 1 and 4096. Default
is 4096.

**send_sigterm (int)**

Send sigterm to HSA process on unhandled exceptions. Default is not to send sigterm
but just print errors on dmesg. Setting 1 enables sending sigterm.

**halt_if_hws_hang (int)**

Halt if HWS hang is detected. Default value, 0, disables the halt on hang.
Setting 1 enables halt on hang.

**hws_gws_support(bool)**

Assume that HWS supports GWS barriers regardless of what firmware version
check says. Default value: false (rely on MEC2 firmware version check).

**queue_preemption_timeout_ms (int)**

queue preemption timeout in ms (1 = Minimum, 9000 = default)

**debug_evictions(bool)**

Enable extra debug messages to help determine the cause of evictions

**no_system_mem_limit(bool)**

Disable system memory limit, to support multiple process shared memory

**no_queue_eviction_on_vm_fault (int)**

If set, process queues will not be evicted on gpuvm fault. This is to keep the wavefront context for debugging (0 = queue eviction, 1 = no queue eviction). The default is 0 (queue eviction).

**mtype_local (int)**

**pcie_p2p (bool)**

Enable PCIe P2P (requires large-BAR). Default value: true (on)

**dcfeaturemask (uint)**

Override display features enabled. See enum DC_FEATURE_MASK in drivers/gpu/drm/amd/include/amd_shared.h.
The default is the current set of stable display features.

**dcdebugmask (uint)**

Override display features enabled. See enum DC_DEBUG_MASK in drivers/gpu/drm/amd/include/amd_shared.h.

**abmlevel (uint)**

Override the default ABM (Adaptive Backlight Management) level used for DC
enabled hardware. Requires DMCU to be supported and loaded.
Valid levels are 0-4. A value of 0 indicates that ABM should be disabled by
default. Values 1-4 control the maximum allowable brightness reduction via
the ABM algorithm, with 1 being the least reduction and 4 being the most
reduction.

Defaults to 0, or disabled. Userspace can still override this level later
after boot.

**damageclips (int)**

Enable or disable damage clips support. If damage clips support is disabled,
we will force full frame updates, irrespective of what user space sends to
us.

Defaults to -1 (where it is enabled unless a PSR-SU display is detected).

**tmz (int)**

Trusted Memory Zone (TMZ) is a method to protect data being written
to or read from memory.

The default value: 0 (off). TODO: change to auto till it is completed.

**reset_method (int)**

GPU reset method (-1 = auto (default), 0 = legacy, 1 = mode0, 2 = mode1, 3 = mode2, 4 = baco)

**bad_page_threshold (int) Bad page threshold is specifies the**

threshold value of faulty pages detected by RAS ECC, which may
result in the GPU entering bad status when the number of total
faulty pages by ECC exceeds the threshold value.

**vcnfw_log (int)**

Enable vcnfw log output for debugging, the default is disabled.

**sg_display (int)**

Disable S/G (scatter/gather) display (i.e., display from system memory).
This option is only relevant on APUs. Set this option to 0 to disable
S/G display if you experience flickering or other issues under memory
pressure and report the issue.

**umsch_mm (int)**

Enable Multi Media User Mode Scheduler. This is a HW scheduling engine for VCN and VPE.
(0 = disabled (default), 1 = enabled)

**smu_pptable_id (int)**

Used to override pptable id. id = 0 use VBIOS pptable.
id > 0 use the soft pptable with specicfied id.

**partition_mode (int)**

Used to override the default SPX mode.

**enforce_isolation (bool)**

enforce process isolation between graphics and compute via using the same reserved vmid.

**seamless (int)**

Seamless boot will keep the image on the screen during the boot process.

**debug_mask (uint)**

Debug options for amdgpu, work as a binary mask with the following options:

- 0x1: Debug VM handling
- 0x2: Enable simulating large-bar capability on non-large bar system. This
  limits the VRAM size reported to ROCm applications to the visible
  size, usually 256MB.
- 0x4: Disable GPU soft recovery, always do a full reset

**agp (int)**

Enable the AGP aperture. This provides an aperture in the GPU's internal
address space for direct access to system memory. Note that these accesses
are non-snooped, so they are only used for access to uncached memory.

**wbrf (int)**

Enable Wifi RFI interference mitigation feature.
Due to electrical and mechanical constraints there may be likely interference of
relatively high-powered harmonics of the (G-)DDR memory clocks with local radio
module frequency bands used by Wifi 6/6e/7. To mitigate the possible RFI interference,
with this feature enabled, PMFW will use either “shadowed P-State” or “P-State” based
on active list of frequencies in-use (to be avoided) as part of initial setting or
P-state transition. However, there may be potential performance impact with this
feature enabled.
(0 = disabled, 1 = enabled, -1 = auto (default setting, will be enabled if supported))

void amdgpu_drv_delayed_reset_work_handler(struct work_struct \*work)
:   work handler for reset

**Parameters**

`struct work_struct *work`
:   work_struct.
