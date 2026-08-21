---
collection: kernel
version: "6.8"
title: "2.13.3. V4L2_META_FMT_RK_ISP1_PARAMS ('rk1p'), V4L2_META_FMT_RK_ISP1_STAT_3A ('rk1s')"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/metafmt-rkisp1.html
fetched_at: 2026-08-21T03:40:16+00:00
---
# 2.13.3. V4L2_META_FMT_RK_ISP1_PARAMS ('rk1p'), V4L2_META_FMT_RK_ISP1_STAT_3A ('rk1s')

## 2.13.3.1. Configuration parameters

The configuration parameters are passed to the
[rkisp1_params](../../../admin-guide/media/rkisp1.md#rkisp1-params) metadata output video node, using
the [`v4l2_meta_format`](dev-meta.md#c.v4l2_meta_format "v4l2_meta_format") interface. The buffer contains
a single instance of the C structure [`rkisp1_params_cfg`](metafmt-rkisp1.md#c.rkisp1_params_cfg "rkisp1_params_cfg") defined in
`rkisp1-config.h`. So the structure can be obtained from the buffer by:

```c
struct rkisp1_params_cfg *params = (struct rkisp1_params_cfg*) buffer;
```

## 2.13.3.2. 3A and histogram statistics

The ISP1 device collects different statistics over an input Bayer frame.
Those statistics are obtained from the [rkisp1_stats](../../../admin-guide/media/rkisp1.md#rkisp1-stats)
metadata capture video node,
using the [`v4l2_meta_format`](dev-meta.md#c.v4l2_meta_format "v4l2_meta_format") interface. The buffer contains a single
instance of the C structure [`rkisp1_stat_buffer`](metafmt-rkisp1.md#c.rkisp1_stat_buffer "rkisp1_stat_buffer") defined in
`rkisp1-config.h`. So the structure can be obtained from the buffer by:

```c
struct rkisp1_stat_buffer *stats = (struct rkisp1_stat_buffer*) buffer;
```

The statistics collected are Exposure, AWB (Auto-white balance), Histogram and
AF (Auto-focus). See [`rkisp1_stat_buffer`](metafmt-rkisp1.md#c.rkisp1_stat_buffer "rkisp1_stat_buffer") for details of the statistics.

The 3A statistics and configuration parameters described here are usually
consumed and produced by dedicated user space libraries that comprise the
important tuning tools using software control loop.

## 2.13.3.3. rkisp1 uAPI data types

enum rkisp1_cif_isp_version
:   ISP variants

**Constants**

`RKISP1_V10`
:   used at least in rk3288 and rk3399

`RKISP1_V11`
:   declared in the original vendor code, but not used

`RKISP1_V12`
:   used at least in rk3326 and px30

`RKISP1_V13`
:   used at least in rk1808

enum rkisp1_cif_isp_exp_ctrl_autostop
:   stop modes

**Constants**

`RKISP1_CIF_ISP_EXP_CTRL_AUTOSTOP_0`
:   continuous measurement

`RKISP1_CIF_ISP_EXP_CTRL_AUTOSTOP_1`
:   stop measuring after a complete frame

enum rkisp1_cif_isp_exp_meas_mode
:   Exposure measure mode

**Constants**

`RKISP1_CIF_ISP_EXP_MEASURING_MODE_0`
:   Y = 16 + 0.25R + 0.5G + 0.1094B

`RKISP1_CIF_ISP_EXP_MEASURING_MODE_1`
:   Y = (R + G + B) x (85/256)

struct rkisp1_cif_isp_window
:   measurement window.

**Definition**:

```
struct rkisp1_cif_isp_window {
    __u16 h_offs;
    __u16 v_offs;
    __u16 h_size;
    __u16 v_size;
};
```

**Members**

`h_offs`
:   the horizontal offset of the window from the left of the frame in pixels.

`v_offs`
:   the vertical offset of the window from the top of the frame in pixels.

`h_size`
:   the horizontal size of the window in pixels

`v_size`
:   the vertical size of the window in pixels.

**Description**

Measurements are calculated per window inside the frame.
This struct represents a window for a measurement.

struct rkisp1_cif_isp_bls_fixed_val
:   BLS fixed subtraction values

**Definition**:

```
struct rkisp1_cif_isp_bls_fixed_val {
    __s16 r;
    __s16 gr;
    __s16 gb;
    __s16 b;
};
```

**Members**

`r`
:   Fixed (signed!) subtraction value for Bayer pattern R

`gr`
:   Fixed (signed!) subtraction value for Bayer pattern Gr

`gb`
:   Fixed (signed!) subtraction value for Bayer pattern Gb

`b`
:   Fixed (signed!) subtraction value for Bayer pattern B

**Description**

The values will be subtracted from the sensor
values. Therefore a negative value means addition instead of subtraction!

struct rkisp1_cif_isp_bls_config
:   Configuration used by black level subtraction

**Definition**:

```
struct rkisp1_cif_isp_bls_config {
    __u8 enable_auto;
    __u8 en_windows;
    struct rkisp1_cif_isp_window bls_window1;
    struct rkisp1_cif_isp_window bls_window2;
    __u8 bls_samples;
    struct rkisp1_cif_isp_bls_fixed_val fixed_val;
};
```

**Members**

`enable_auto`
:   Automatic mode activated means that the measured values
    are subtracted. Otherwise the fixed subtraction
    values will be subtracted.

`en_windows`
:   enabled window

`bls_window1`
:   Measurement window 1 size

`bls_window2`
:   Measurement window 2 size

`bls_samples`
:   Set amount of measured pixels for each Bayer position
    (A, B,C and D) to 2^bls_samples.

`fixed_val`
:   Fixed subtraction values

struct rkisp1_cif_isp_dpcc_methods_config
:   DPCC methods set configuration

**Definition**:

```
struct rkisp1_cif_isp_dpcc_methods_config {
    __u32 method;
    __u32 line_thresh;
    __u32 line_mad_fac;
    __u32 pg_fac;
    __u32 rnd_thresh;
    __u32 rg_fac;
};
```

**Members**

`method`
:   Method enable bits (RKISP1_CIF_ISP_DPCC_METHODS_SET_\*)

`line_thresh`
:   Line threshold (RKISP1_CIF_ISP_DPCC_LINE_THRESH_\*)

`line_mad_fac`
:   Line Mean Absolute Difference factor (RKISP1_CIF_ISP_DPCC_LINE_MAD_FAC_\*)

`pg_fac`
:   Peak gradient factor (RKISP1_CIF_ISP_DPCC_PG_FAC_\*)

`rnd_thresh`
:   Rank Neighbor Difference threshold (RKISP1_CIF_ISP_DPCC_RND_THRESH_\*)

`rg_fac`
:   Rank gradient factor (RKISP1_CIF_ISP_DPCC_RG_FAC_\*)

**Description**

This structure stores the configuration of one set of methods for the DPCC
algorithm. Multiple methods can be selected in each set (independently for
the Green and Red/Blue components) through the **method** field, the result is
the logical AND of all enabled methods. The remaining fields set thresholds
and factors for each method.

struct rkisp1_cif_isp_dpcc_config
:   Configuration used by DPCC

**Definition**:

```
struct rkisp1_cif_isp_dpcc_config {
    __u32 mode;
    __u32 output_mode;
    __u32 set_use;
    struct rkisp1_cif_isp_dpcc_methods_config methods[RKISP1_CIF_ISP_DPCC_METHODS_MAX];
    __u32 ro_limits;
    __u32 rnd_offs;
};
```

**Members**

`mode`
:   DPCC mode (RKISP1_CIF_ISP_DPCC_MODE_\*)

`output_mode`
:   Interpolation output mode (RKISP1_CIF_ISP_DPCC_OUTPUT_MODE_\*)

`set_use`
:   Methods sets selection (RKISP1_CIF_ISP_DPCC_SET_USE_\*)

`methods`
:   Methods sets configuration

`ro_limits`
:   Rank order limits (RKISP1_CIF_ISP_DPCC_RO_LIMITS_\*)

`rnd_offs`
:   Differential rank offsets for rank neighbor difference (RKISP1_CIF_ISP_DPCC_RND_OFFS_\*)

**Description**

Configuration used by Defect Pixel Cluster Correction. Three sets of methods
can be configured and selected through the **set_use** field. The result is the
logical OR of all enabled sets.

struct rkisp1_cif_isp_gamma_corr_curve
:   gamma curve point definition y-axis (output).

**Definition**:

```
struct rkisp1_cif_isp_gamma_corr_curve {
    __u16 gamma_y[RKISP1_CIF_ISP_DEGAMMA_CURVE_SIZE];
};
```

**Members**

`gamma_y`
:   the values for the y-axis of gamma curve points. Each value is 12 bit.

**Description**

The reset values define a linear curve which has the same effect as bypass. Reset values are:
gamma_y[0] = 0x0000, gamma_y[1] = 0x0100, ... gamma_y[15] = 0x0f00, gamma_y[16] = 0xfff

struct rkisp1_cif_isp_gamma_curve_x_axis_pnts
:   De-Gamma Curve definition x increments (sampling points). gamma_dx0 is for the lower samples (1-8), gamma_dx1 is for the higher samples (9-16). The reset values for both fields is 0x44444444. This means that each sample is 4 units away from the previous one on the x-axis.

**Definition**:

```
struct rkisp1_cif_isp_gamma_curve_x_axis_pnts {
    __u32 gamma_dx0;
    __u32 gamma_dx1;
};
```

**Members**

`gamma_dx0`
:   gamma curve sample points definitions. Bits 0:2 for sample 1. Bit 3 unused.
    Bits 4:6 for sample 2. bit 7 unused ... Bits 28:30 for sample 8. Bit 31 unused

`gamma_dx1`
:   gamma curve sample points definitions. Bits 0:2 for sample 9. Bit 3 unused.
    Bits 4:6 for sample 10. bit 7 unused ... Bits 28:30 for sample 16. Bit 31 unused

struct rkisp1_cif_isp_sdg_config
:   Configuration used by sensor degamma

**Definition**:

```
struct rkisp1_cif_isp_sdg_config {
    struct rkisp1_cif_isp_gamma_corr_curve curve_r;
    struct rkisp1_cif_isp_gamma_corr_curve curve_g;
    struct rkisp1_cif_isp_gamma_corr_curve curve_b;
    struct rkisp1_cif_isp_gamma_curve_x_axis_pnts xa_pnts;
};
```

**Members**

`curve_r`
:   gamma curve point definition axis for red

`curve_g`
:   gamma curve point definition axis for green

`curve_b`
:   gamma curve point definition axis for blue

`xa_pnts`
:   x axis increments

struct rkisp1_cif_isp_lsc_config
:   Configuration used by Lens shading correction

**Definition**:

```
struct rkisp1_cif_isp_lsc_config {
    __u16 r_data_tbl[RKISP1_CIF_ISP_LSC_SAMPLES_MAX][RKISP1_CIF_ISP_LSC_SAMPLES_MAX];
    __u16 gr_data_tbl[RKISP1_CIF_ISP_LSC_SAMPLES_MAX][RKISP1_CIF_ISP_LSC_SAMPLES_MAX];
    __u16 gb_data_tbl[RKISP1_CIF_ISP_LSC_SAMPLES_MAX][RKISP1_CIF_ISP_LSC_SAMPLES_MAX];
    __u16 b_data_tbl[RKISP1_CIF_ISP_LSC_SAMPLES_MAX][RKISP1_CIF_ISP_LSC_SAMPLES_MAX];
    __u16 x_grad_tbl[RKISP1_CIF_ISP_LSC_SECTORS_TBL_SIZE];
    __u16 y_grad_tbl[RKISP1_CIF_ISP_LSC_SECTORS_TBL_SIZE];
    __u16 x_size_tbl[RKISP1_CIF_ISP_LSC_SECTORS_TBL_SIZE];
    __u16 y_size_tbl[RKISP1_CIF_ISP_LSC_SECTORS_TBL_SIZE];
    __u16 config_width;
    __u16 config_height;
};
```

**Members**

`r_data_tbl`
:   sample table red

`gr_data_tbl`
:   sample table green (red)

`gb_data_tbl`
:   sample table green (blue)

`b_data_tbl`
:   sample table blue

`x_grad_tbl`
:   gradient table x

`y_grad_tbl`
:   gradient table y

`x_size_tbl`
:   size table x

`y_size_tbl`
:   size table y

`config_width`
:   not used at the moment

`config_height`
:   not used at the moment

struct rkisp1_cif_isp_ie_config
:   Configuration used by image effects

**Definition**:

```
struct rkisp1_cif_isp_ie_config {
    __u16 effect;
    __u16 color_sel;
    __u16 eff_mat_1;
    __u16 eff_mat_2;
    __u16 eff_mat_3;
    __u16 eff_mat_4;
    __u16 eff_mat_5;
    __u16 eff_tint;
};
```

**Members**

`effect`
:   values from 'enum v4l2_colorfx'. Possible values are: V4L2_COLORFX_SEPIA,
    V4L2_COLORFX_SET_CBCR, V4L2_COLORFX_AQUA, V4L2_COLORFX_EMBOSS,
    V4L2_COLORFX_SKETCH, V4L2_COLORFX_BW, V4L2_COLORFX_NEGATIVE

`color_sel`
:   bits 0:2 - colors bitmask (001 - blue, 010 - green, 100 - red).
    bits 8:15 - Threshold value of the RGB colors for the color selection effect.

`eff_mat_1`
:   3x3 Matrix Coefficients for Emboss Effect 1

`eff_mat_2`
:   3x3 Matrix Coefficients for Emboss Effect 2

`eff_mat_3`
:   3x3 Matrix Coefficients for Emboss 3/Sketch 1

`eff_mat_4`
:   3x3 Matrix Coefficients for Sketch Effect 2

`eff_mat_5`
:   3x3 Matrix Coefficients for Sketch Effect 3

`eff_tint`
:   Chrominance increment values of tint (used for sepia effect)

struct rkisp1_cif_isp_cproc_config
:   Configuration used by Color Processing

**Definition**:

```
struct rkisp1_cif_isp_cproc_config {
    __u8 c_out_range;
    __u8 y_in_range;
    __u8 y_out_range;
    __u8 contrast;
    __u8 brightness;
    __u8 sat;
    __u8 hue;
};
```

**Members**

`c_out_range`
:   Chrominance pixel clipping range at output.
    (0 for limit, 1 for full)

`y_in_range`
:   Luminance pixel clipping range at output.

`y_out_range`
:   Luminance pixel clipping range at output.

`contrast`
:   00~ff, 0.0~1.992

`brightness`
:   80~7F, -128~+127

`sat`
:   saturation, 00~FF, 0.0~1.992

`hue`
:   80~7F, -90~+87.188

struct rkisp1_cif_isp_awb_meas_config
:   Configuration for the AWB statistics

**Definition**:

```
struct rkisp1_cif_isp_awb_meas_config {
    struct rkisp1_cif_isp_window awb_wnd;
    __u32 awb_mode;
    __u8 max_y;
    __u8 min_y;
    __u8 max_csum;
    __u8 min_c;
    __u8 frames;
    __u8 awb_ref_cr;
    __u8 awb_ref_cb;
    __u8 enable_ymax_cmp;
};
```

**Members**

`awb_wnd`
:   white balance measurement window (in pixels)

`awb_mode`
:   the awb meas mode. From enum rkisp1_cif_isp_awb_mode_type.

`max_y`
:   only pixels values < max_y contribute to awb measurement, set to 0
    to disable this feature

`min_y`
:   only pixels values > min_y contribute to awb measurement

`max_csum`
:   Chrominance sum maximum value, only consider pixels with Cb+Cr,
    smaller than threshold for awb measurements

`min_c`
:   Chrominance minimum value, only consider pixels with Cb/Cr
    each greater than threshold value for awb measurements

`frames`
:   number of frames - 1 used for mean value calculation
    (ucFrames=0 means 1 Frame)

`awb_ref_cr`
:   reference Cr value for AWB regulation, target for AWB

`awb_ref_cb`
:   reference Cb value for AWB regulation, target for AWB

`enable_ymax_cmp`
:   enable Y_MAX compare (Not valid in RGB measurement mode.)

struct rkisp1_cif_isp_awb_gain_config
:   Configuration used by auto white balance gain

**Definition**:

```
struct rkisp1_cif_isp_awb_gain_config {
    __u16 gain_red;
    __u16 gain_green_r;
    __u16 gain_blue;
    __u16 gain_green_b;
};
```

**Members**

`gain_red`
:   gain value for red component.

`gain_green_r`
:   gain value for green component in red line.

`gain_blue`
:   gain value for blue component.

`gain_green_b`
:   gain value for green component in blue line.

**Description**

All fields in this struct are 10 bit, where:
0x100h = 1, unsigned integer value, range 0 to 4 with 8 bit fractional part.

out_data_x = ( AWB_GAIN_X \* in_data + 128) >> 8

struct rkisp1_cif_isp_flt_config
:   Configuration used by ISP filtering

**Definition**:

```
struct rkisp1_cif_isp_flt_config {
    __u32 mode;
    __u8 grn_stage1;
    __u8 chr_h_mode;
    __u8 chr_v_mode;
    __u32 thresh_bl0;
    __u32 thresh_bl1;
    __u32 thresh_sh0;
    __u32 thresh_sh1;
    __u32 lum_weight;
    __u32 fac_sh1;
    __u32 fac_sh0;
    __u32 fac_mid;
    __u32 fac_bl0;
    __u32 fac_bl1;
};
```

**Members**

`mode`
:   ISP_FILT_MODE register fields (from enum rkisp1_cif_isp_flt_mode)

`grn_stage1`
:   Green filter stage 1 select (range 0x0...0x8)

`chr_h_mode`
:   Chroma filter horizontal mode

`chr_v_mode`
:   Chroma filter vertical mode

`thresh_bl0`
:   If thresh_bl1 < sum_grad < thresh_bl0 then fac_bl0 is selected (blurring th)

`thresh_bl1`
:   If sum_grad < thresh_bl1 then fac_bl1 is selected (blurring th)

`thresh_sh0`
:   If thresh_sh0 < sum_grad < thresh_sh1 then thresh_sh0 is selected (sharpening th)

`thresh_sh1`
:   If thresh_sh1 < sum_grad then thresh_sh1 is selected (sharpening th)

`lum_weight`
:   Parameters for luminance weight function.

`fac_sh1`
:   filter factor for sharp1 level

`fac_sh0`
:   filter factor for sharp0 level

`fac_mid`
:   filter factor for mid level and for static filter mode

`fac_bl0`
:   filter factor for blur 0 level

`fac_bl1`
:   filter factor for blur 1 level (max blur)

**Description**

All 4 threshold fields (thresh_\*) are 10 bits.
All 6 factor fields (fac_\*) are 6 bits.

struct rkisp1_cif_isp_bdm_config
:   Configuration used by Bayer DeMosaic

**Definition**:

```
struct rkisp1_cif_isp_bdm_config {
    __u8 demosaic_th;
};
```

**Members**

`demosaic_th`
:   threshold for bayer demosaicing texture detection

struct rkisp1_cif_isp_ctk_config
:   Configuration used by Cross Talk correction

**Definition**:

```
struct rkisp1_cif_isp_ctk_config {
    __u16 coeff[3][3];
    __u16 ct_offset[3];
};
```

**Members**

`coeff`
:   color correction matrix. Values are 11-bit signed fixed-point numbers with 4 bit integer
    and 7 bit fractional part, ranging from -8 (0x400) to +7.992 (0x3FF). 0 is
    represented by 0x000 and a coefficient value of 1 as 0x080.

`ct_offset`
:   Red, Green, Blue offsets for the crosstalk correction matrix

struct rkisp1_cif_isp_goc_config
:   Configuration used by Gamma Out correction

**Definition**:

```
struct rkisp1_cif_isp_goc_config {
    __u32 mode;
    __u16 gamma_y[RKISP1_CIF_ISP_GAMMA_OUT_MAX_SAMPLES];
};
```

**Members**

`mode`
:   goc mode (from enum rkisp1_cif_isp_goc_mode)

`gamma_y`
:   gamma out curve y-axis for all color components

**Description**

The number of entries of **gamma_y** depends on the hardware revision
as is reported by the hw_revision field of the struct media_device_info
that is returned by ioctl MEDIA_IOC_DEVICE_INFO.

Versions <= V11 have RKISP1_CIF_ISP_GAMMA_OUT_MAX_SAMPLES_V10
entries, versions >= V12 have RKISP1_CIF_ISP_GAMMA_OUT_MAX_SAMPLES_V12
entries. RKISP1_CIF_ISP_GAMMA_OUT_MAX_SAMPLES is equal to the maximum
of the two.

struct rkisp1_cif_isp_hst_config
:   Configuration for Histogram statistics

**Definition**:

```
struct rkisp1_cif_isp_hst_config {
    __u32 mode;
    __u8 histogram_predivider;
    struct rkisp1_cif_isp_window meas_window;
    __u8 hist_weight[RKISP1_CIF_ISP_HISTOGRAM_WEIGHT_GRIDS_SIZE];
};
```

**Members**

`mode`
:   histogram mode (from enum rkisp1_cif_isp_histogram_mode)

`histogram_predivider`
:   process every stepsize pixel, all other pixels are
    skipped

`meas_window`
:   coordinates of the measure window

`hist_weight`
:   weighting factor for sub-windows

**Description**

The number of entries of **hist_weight** depends on the hardware revision
as is reported by the hw_revision field of the struct media_device_info
that is returned by ioctl MEDIA_IOC_DEVICE_INFO.

Versions <= V11 have RKISP1_CIF_ISP_HISTOGRAM_WEIGHT_GRIDS_SIZE_V10
entries, versions >= V12 have RKISP1_CIF_ISP_HISTOGRAM_WEIGHT_GRIDS_SIZE_V12
entries. RKISP1_CIF_ISP_HISTOGRAM_WEIGHT_GRIDS_SIZE is equal to the maximum
of the two.

struct rkisp1_cif_isp_aec_config
:   Configuration for Auto Exposure statistics

**Definition**:

```
struct rkisp1_cif_isp_aec_config {
    __u32 mode;
    __u32 autostop;
    struct rkisp1_cif_isp_window meas_window;
};
```

**Members**

`mode`
:   Exposure measure mode (from [`enum rkisp1_cif_isp_exp_meas_mode`](metafmt-rkisp1.md#c.rkisp1_cif_isp_exp_meas_mode "rkisp1_cif_isp_exp_meas_mode"))

`autostop`
:   stop mode (from [`enum rkisp1_cif_isp_exp_ctrl_autostop`](metafmt-rkisp1.md#c.rkisp1_cif_isp_exp_ctrl_autostop "rkisp1_cif_isp_exp_ctrl_autostop"))

`meas_window`
:   coordinates of the measure window

struct rkisp1_cif_isp_afc_config
:   Configuration for the Auto Focus statistics

**Definition**:

```
struct rkisp1_cif_isp_afc_config {
    __u8 num_afm_win;
    struct rkisp1_cif_isp_window afm_win[RKISP1_CIF_ISP_AFM_MAX_WINDOWS];
    __u32 thres;
    __u32 var_shift;
};
```

**Members**

`num_afm_win`
:   max RKISP1_CIF_ISP_AFM_MAX_WINDOWS

`afm_win`
:   coordinates of the meas window

`thres`
:   threshold used for minimizing the influence of noise

`var_shift`
:   the number of bits for the shift operation at the end of the
    calculation chain.

enum rkisp1_cif_isp_dpf_gain_usage
:   dpf gain usage

**Constants**

`RKISP1_CIF_ISP_DPF_GAIN_USAGE_DISABLED`
:   don't use any gains in preprocessing stage

`RKISP1_CIF_ISP_DPF_GAIN_USAGE_NF_GAINS`
:   use only the noise function gains from
    registers DPF_NF_GAIN_R, ...

`RKISP1_CIF_ISP_DPF_GAIN_USAGE_LSC_GAINS`
:   use only the gains from LSC module

`RKISP1_CIF_ISP_DPF_GAIN_USAGE_NF_LSC_GAINS`
:   use the noise function gains and the
    gains from LSC module

`RKISP1_CIF_ISP_DPF_GAIN_USAGE_AWB_GAINS`
:   use only the gains from AWB module

`RKISP1_CIF_ISP_DPF_GAIN_USAGE_AWB_LSC_GAINS`
:   use the gains from AWB and LSC module

`RKISP1_CIF_ISP_DPF_GAIN_USAGE_MAX`
:   upper border (only for an internal evaluation)

enum rkisp1_cif_isp_dpf_rb_filtersize
:   Red and blue filter sizes

**Constants**

`RKISP1_CIF_ISP_DPF_RB_FILTERSIZE_13x9`
:   red and blue filter kernel size 13x9
    (means 7x5 active pixel)

`RKISP1_CIF_ISP_DPF_RB_FILTERSIZE_9x9`
:   red and blue filter kernel size 9x9
    (means 5x5 active pixel)

enum rkisp1_cif_isp_dpf_nll_scale_mode
:   dpf noise level scale mode

**Constants**

`RKISP1_CIF_ISP_NLL_SCALE_LINEAR`
:   use a linear scaling

`RKISP1_CIF_ISP_NLL_SCALE_LOGARITHMIC`
:   use a logarithmic scaling

struct rkisp1_cif_isp_dpf_nll
:   Noise level lookup

**Definition**:

```
struct rkisp1_cif_isp_dpf_nll {
    __u16 coeff[RKISP1_CIF_ISP_DPF_MAX_NLF_COEFFS];
    __u32 scale_mode;
};
```

**Members**

`coeff`
:   Noise level Lookup coefficient

`scale_mode`
:   dpf noise level scale mode (from [`enum rkisp1_cif_isp_dpf_nll_scale_mode`](metafmt-rkisp1.md#c.rkisp1_cif_isp_dpf_nll_scale_mode "rkisp1_cif_isp_dpf_nll_scale_mode"))

struct rkisp1_cif_isp_dpf_rb_flt
:   Red blue filter config

**Definition**:

```
struct rkisp1_cif_isp_dpf_rb_flt {
    __u32 fltsize;
    __u8 spatial_coeff[RKISP1_CIF_ISP_DPF_MAX_SPATIAL_COEFFS];
    __u8 r_enable;
    __u8 b_enable;
};
```

**Members**

`fltsize`
:   The filter size for the red and blue pixels
    (from [`enum rkisp1_cif_isp_dpf_rb_filtersize`](metafmt-rkisp1.md#c.rkisp1_cif_isp_dpf_rb_filtersize "rkisp1_cif_isp_dpf_rb_filtersize"))

`spatial_coeff`
:   Spatial weights

`r_enable`
:   enable filter processing for red pixels

`b_enable`
:   enable filter processing for blue pixels

struct rkisp1_cif_isp_dpf_g_flt
:   Green filter Configuration

**Definition**:

```
struct rkisp1_cif_isp_dpf_g_flt {
    __u8 spatial_coeff[RKISP1_CIF_ISP_DPF_MAX_SPATIAL_COEFFS];
    __u8 gr_enable;
    __u8 gb_enable;
};
```

**Members**

`spatial_coeff`
:   Spatial weights

`gr_enable`
:   enable filter processing for green pixels in green/red lines

`gb_enable`
:   enable filter processing for green pixels in green/blue lines

struct rkisp1_cif_isp_dpf_gain
:   Noise function Configuration

**Definition**:

```
struct rkisp1_cif_isp_dpf_gain {
    __u32 mode;
    __u16 nf_r_gain;
    __u16 nf_b_gain;
    __u16 nf_gr_gain;
    __u16 nf_gb_gain;
};
```

**Members**

`mode`
:   dpf gain usage (from [`enum rkisp1_cif_isp_dpf_gain_usage`](metafmt-rkisp1.md#c.rkisp1_cif_isp_dpf_gain_usage "rkisp1_cif_isp_dpf_gain_usage"))

`nf_r_gain`
:   Noise function Gain that replaces the AWB gain for red pixels

`nf_b_gain`
:   Noise function Gain that replaces the AWB gain for blue pixels

`nf_gr_gain`
:   Noise function Gain that replaces the AWB gain
    for green pixels in a red line

`nf_gb_gain`
:   Noise function Gain that replaces the AWB gain
    for green pixels in a blue line

struct rkisp1_cif_isp_dpf_config
:   Configuration used by De-noising pre-filter

**Definition**:

```
struct rkisp1_cif_isp_dpf_config {
    struct rkisp1_cif_isp_dpf_gain gain;
    struct rkisp1_cif_isp_dpf_g_flt g_flt;
    struct rkisp1_cif_isp_dpf_rb_flt rb_flt;
    struct rkisp1_cif_isp_dpf_nll nll;
};
```

**Members**

`gain`
:   noise function gain

`g_flt`
:   green filter config

`rb_flt`
:   red blue filter config

`nll`
:   noise level lookup

struct rkisp1_cif_isp_dpf_strength_config
:   strength of the filter

**Definition**:

```
struct rkisp1_cif_isp_dpf_strength_config {
    __u8 r;
    __u8 g;
    __u8 b;
};
```

**Members**

`r`
:   filter strength of the RED filter

`g`
:   filter strength of the GREEN filter

`b`
:   filter strength of the BLUE filter

struct rkisp1_cif_isp_isp_other_cfg
:   Parameters for some blocks in rockchip isp1

**Definition**:

```
struct rkisp1_cif_isp_isp_other_cfg {
    struct rkisp1_cif_isp_dpcc_config dpcc_config;
    struct rkisp1_cif_isp_bls_config bls_config;
    struct rkisp1_cif_isp_sdg_config sdg_config;
    struct rkisp1_cif_isp_lsc_config lsc_config;
    struct rkisp1_cif_isp_awb_gain_config awb_gain_config;
    struct rkisp1_cif_isp_flt_config flt_config;
    struct rkisp1_cif_isp_bdm_config bdm_config;
    struct rkisp1_cif_isp_ctk_config ctk_config;
    struct rkisp1_cif_isp_goc_config goc_config;
    struct rkisp1_cif_isp_dpf_config dpf_config;
    struct rkisp1_cif_isp_dpf_strength_config dpf_strength_config;
    struct rkisp1_cif_isp_cproc_config cproc_config;
    struct rkisp1_cif_isp_ie_config ie_config;
};
```

**Members**

`dpcc_config`
:   Defect Pixel Cluster Correction config

`bls_config`
:   black level subtraction config

`sdg_config`
:   sensor degamma config

`lsc_config`
:   Lens Shade config

`awb_gain_config`
:   Auto White balance gain config

`flt_config`
:   filter config

`bdm_config`
:   demosaic config

`ctk_config`
:   cross talk config

`goc_config`
:   gamma out config

`dpf_config`
:   De-noising pre-filter config

`dpf_strength_config`
:   dpf strength config

`cproc_config`
:   color process config

`ie_config`
:   image effects config

struct rkisp1_cif_isp_isp_meas_cfg
:   Rockchip ISP1 Measure Parameters

**Definition**:

```
struct rkisp1_cif_isp_isp_meas_cfg {
    struct rkisp1_cif_isp_awb_meas_config awb_meas_config;
    struct rkisp1_cif_isp_hst_config hst_config;
    struct rkisp1_cif_isp_aec_config aec_config;
    struct rkisp1_cif_isp_afc_config afc_config;
};
```

**Members**

`awb_meas_config`
:   auto white balance config

`hst_config`
:   histogram config

`aec_config`
:   auto exposure config

`afc_config`
:   auto focus config

struct rkisp1_params_cfg
:   Rockchip ISP1 Input Parameters Meta Data

**Definition**:

```
struct rkisp1_params_cfg {
    __u32 module_en_update;
    __u32 module_ens;
    __u32 module_cfg_update;
    struct rkisp1_cif_isp_isp_meas_cfg meas;
    struct rkisp1_cif_isp_isp_other_cfg others;
};
```

**Members**

`module_en_update`
:   mask the enable bits of which module should be updated

`module_ens`
:   mask the enable value of each module, only update the module
    which correspond bit was set in module_en_update

`module_cfg_update`
:   mask the config bits of which module should be updated

`meas`
:   measurement config

`others`
:   other config

struct rkisp1_cif_isp_awb_meas
:   AWB measured values

**Definition**:

```
struct rkisp1_cif_isp_awb_meas {
    __u32 cnt;
    __u8 mean_y_or_g;
    __u8 mean_cb_or_b;
    __u8 mean_cr_or_r;
};
```

**Members**

`cnt`
:   White pixel count, number of "white pixels" found during last
    measurement

`mean_y_or_g`
:   Mean value of Y within window and frames,
    Green if RGB is selected.

`mean_cb_or_b`
:   Mean value of Cb within window and frames,
    Blue if RGB is selected.

`mean_cr_or_r`
:   Mean value of Cr within window and frames,
    Red if RGB is selected.

struct rkisp1_cif_isp_awb_stat
:   statistics automatic white balance data

**Definition**:

```
struct rkisp1_cif_isp_awb_stat {
    struct rkisp1_cif_isp_awb_meas awb_mean[RKISP1_CIF_ISP_AWB_MAX_GRID];
};
```

**Members**

`awb_mean`
:   Mean measured data

struct rkisp1_cif_isp_bls_meas_val
:   BLS measured values

**Definition**:

```
struct rkisp1_cif_isp_bls_meas_val {
    __u16 meas_r;
    __u16 meas_gr;
    __u16 meas_gb;
    __u16 meas_b;
};
```

**Members**

`meas_r`
:   Mean measured value for Bayer pattern R

`meas_gr`
:   Mean measured value for Bayer pattern Gr

`meas_gb`
:   Mean measured value for Bayer pattern Gb

`meas_b`
:   Mean measured value for Bayer pattern B

struct rkisp1_cif_isp_ae_stat
:   statistics auto exposure data

**Definition**:

```
struct rkisp1_cif_isp_ae_stat {
    __u8 exp_mean[RKISP1_CIF_ISP_AE_MEAN_MAX];
    struct rkisp1_cif_isp_bls_meas_val bls_val;
};
```

**Members**

`exp_mean`
:   Mean luminance value of block xx

`bls_val`
:   BLS measured values

**Description**

The number of entries of **exp_mean** depends on the hardware revision
as is reported by the hw_revision field of the struct media_device_info
that is returned by ioctl MEDIA_IOC_DEVICE_INFO.

Versions <= V11 have RKISP1_CIF_ISP_AE_MEAN_MAX_V10 entries,
versions >= V12 have RKISP1_CIF_ISP_AE_MEAN_MAX_V12 entries.
RKISP1_CIF_ISP_AE_MEAN_MAX is equal to the maximum of the two.

Image is divided into 5x5 blocks on V10 and 9x9 blocks on V12.

struct rkisp1_cif_isp_af_meas_val
:   AF measured values

**Definition**:

```
struct rkisp1_cif_isp_af_meas_val {
    __u32 sum;
    __u32 lum;
};
```

**Members**

`sum`
:   sharpness value

`lum`
:   luminance value

struct rkisp1_cif_isp_af_stat
:   statistics auto focus data

**Definition**:

```
struct rkisp1_cif_isp_af_stat {
    struct rkisp1_cif_isp_af_meas_val window[RKISP1_CIF_ISP_AFM_MAX_WINDOWS];
};
```

**Members**

`window`
:   AF measured value of window x

**Description**

The module measures the sharpness in 3 windows of selectable size via
register settings(ISP_AFM_\*_A/B/C)

struct rkisp1_cif_isp_hist_stat
:   statistics histogram data

**Definition**:

```
struct rkisp1_cif_isp_hist_stat {
    __u32 hist_bins[RKISP1_CIF_ISP_HIST_BIN_N_MAX];
};
```

**Members**

`hist_bins`
:   measured bin counters. Each bin is a 20 bits unsigned fixed point
    type. Bits 0-4 are the fractional part and bits 5-19 are the
    integer part.

**Description**

The window of the measurements area is divided to 5x5 sub-windows for
V10/V11 and to 9x9 sub-windows for V12. The histogram is then computed for
each sub-window independently and the final result is a weighted average of
the histogram measurements on all sub-windows. The window of the
measurements area and the weight of each sub-window are configurable using
struct **rkisp1_cif_isp_hst_config**.

The histogram contains 16 bins in V10/V11 and 32 bins in V12/V13.

The number of entries of **hist_bins** depends on the hardware revision
as is reported by the hw_revision field of the struct media_device_info
that is returned by ioctl MEDIA_IOC_DEVICE_INFO.

Versions <= V11 have RKISP1_CIF_ISP_HIST_BIN_N_MAX_V10 entries,
versions >= V12 have RKISP1_CIF_ISP_HIST_BIN_N_MAX_V12 entries.
RKISP1_CIF_ISP_HIST_BIN_N_MAX is equal to the maximum of the two.

struct rkisp1_cif_isp_stat
:   Rockchip ISP1 Statistics Data

**Definition**:

```
struct rkisp1_cif_isp_stat {
    struct rkisp1_cif_isp_awb_stat awb;
    struct rkisp1_cif_isp_ae_stat ae;
    struct rkisp1_cif_isp_af_stat af;
    struct rkisp1_cif_isp_hist_stat hist;
};
```

**Members**

`awb`
:   statistics data for automatic white balance

`ae`
:   statistics data for auto exposure

`af`
:   statistics data for auto focus

`hist`
:   statistics histogram data

struct rkisp1_stat_buffer
:   Rockchip ISP1 Statistics Meta Data

**Definition**:

```
struct rkisp1_stat_buffer {
    __u32 meas_type;
    __u32 frame_id;
    struct rkisp1_cif_isp_stat params;
};
```

**Members**

`meas_type`
:   measurement types (RKISP1_CIF_ISP_STAT_\* definitions)

`frame_id`
:   frame ID for sync

`params`
:   statistics data
