---
collection: kernel
version: "6.8"
title: "8. Digital TV uAPI header files"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/headers.html
fetched_at: 2026-08-21T03:57:57+00:00
---
# 8. Digital TV uAPI header files

## 8.1. Digital TV uAPI headers

### 8.1.1. frontend.h

```
/* SPDX-License-Identifier: LGPL-2.1+ WITH Linux-syscall-note */
/*
 * frontend.h
 *
 * Copyright (C) 2000 Marcus Metzler <marcus@convergence.de>
 *                  Ralph  Metzler <ralph@convergence.de>
 *                  Holger Waechtler <holger@convergence.de>
 *                  Andre Draszik <ad@convergence.de>
 *                  for convergence integrated media GmbH
 */

#ifndef _DVBFRONTEND_H_
#define _DVBFRONTEND_H_

#include <linux/types.h>

/**
 * enum fe_caps - Frontend capabilities
 *
 * @FE_IS_STUPID:                       There's something wrong at the
 *                                      frontend, and it can't report its
 *                                      capabilities.
 * @FE_CAN_INVERSION_AUTO:              Can auto-detect frequency spectral
 *                                      band inversion
 * @FE_CAN_FEC_1_2:                     Supports FEC 1/2
 * @FE_CAN_FEC_2_3:                     Supports FEC 2/3
 * @FE_CAN_FEC_3_4:                     Supports FEC 3/4
 * @FE_CAN_FEC_4_5:                     Supports FEC 4/5
 * @FE_CAN_FEC_5_6:                     Supports FEC 5/6
 * @FE_CAN_FEC_6_7:                     Supports FEC 6/7
 * @FE_CAN_FEC_7_8:                     Supports FEC 7/8
 * @FE_CAN_FEC_8_9:                     Supports FEC 8/9
 * @FE_CAN_FEC_AUTO:                    Can auto-detect FEC
 * @FE_CAN_QPSK:                        Supports QPSK modulation
 * @FE_CAN_QAM_16:                      Supports 16-QAM modulation
 * @FE_CAN_QAM_32:                      Supports 32-QAM modulation
 * @FE_CAN_QAM_64:                      Supports 64-QAM modulation
 * @FE_CAN_QAM_128:                     Supports 128-QAM modulation
 * @FE_CAN_QAM_256:                     Supports 256-QAM modulation
 * @FE_CAN_QAM_AUTO:                    Can auto-detect QAM modulation
 * @FE_CAN_TRANSMISSION_MODE_AUTO:      Can auto-detect transmission mode
 * @FE_CAN_BANDWIDTH_AUTO:              Can auto-detect bandwidth
 * @FE_CAN_GUARD_INTERVAL_AUTO:         Can auto-detect guard interval
 * @FE_CAN_HIERARCHY_AUTO:              Can auto-detect hierarchy
 * @FE_CAN_8VSB:                        Supports 8-VSB modulation
 * @FE_CAN_16VSB:                       Supporta 16-VSB modulation
 * @FE_HAS_EXTENDED_CAPS:               Unused
 * @FE_CAN_MULTISTREAM:                 Supports multistream filtering
 * @FE_CAN_TURBO_FEC:                   Supports "turbo FEC" modulation
 * @FE_CAN_2G_MODULATION:               Supports "2nd generation" modulation,
 *                                      e. g. DVB-S2, DVB-T2, DVB-C2
 * @FE_NEEDS_BENDING:                   Unused
 * @FE_CAN_RECOVER:                     Can recover from a cable unplug
 *                                      automatically
 * @FE_CAN_MUTE_TS:                     Can stop spurious TS data output
 */
enum fe_caps {
        FE_IS_STUPID                    = 0,
        FE_CAN_INVERSION_AUTO           = 0x1,
        FE_CAN_FEC_1_2                  = 0x2,
        FE_CAN_FEC_2_3                  = 0x4,
        FE_CAN_FEC_3_4                  = 0x8,
        FE_CAN_FEC_4_5                  = 0x10,
        FE_CAN_FEC_5_6                  = 0x20,
        FE_CAN_FEC_6_7                  = 0x40,
        FE_CAN_FEC_7_8                  = 0x80,
        FE_CAN_FEC_8_9                  = 0x100,
        FE_CAN_FEC_AUTO                 = 0x200,
        FE_CAN_QPSK                     = 0x400,
        FE_CAN_QAM_16                   = 0x800,
        FE_CAN_QAM_32                   = 0x1000,
        FE_CAN_QAM_64                   = 0x2000,
        FE_CAN_QAM_128                  = 0x4000,
        FE_CAN_QAM_256                  = 0x8000,
        FE_CAN_QAM_AUTO                 = 0x10000,
        FE_CAN_TRANSMISSION_MODE_AUTO   = 0x20000,
        FE_CAN_BANDWIDTH_AUTO           = 0x40000,
        FE_CAN_GUARD_INTERVAL_AUTO      = 0x80000,
        FE_CAN_HIERARCHY_AUTO           = 0x100000,
        FE_CAN_8VSB                     = 0x200000,
        FE_CAN_16VSB                    = 0x400000,
        FE_HAS_EXTENDED_CAPS            = 0x800000,
        FE_CAN_MULTISTREAM              = 0x4000000,
        FE_CAN_TURBO_FEC                = 0x8000000,
        FE_CAN_2G_MODULATION            = 0x10000000,
        FE_NEEDS_BENDING                = 0x20000000,
        FE_CAN_RECOVER                  = 0x40000000,
        FE_CAN_MUTE_TS                  = 0x80000000
};

/*
 * DEPRECATED: Should be kept just due to backward compatibility.
 */
enum fe_type {
        FE_QPSK,
        FE_QAM,
        FE_OFDM,
        FE_ATSC
};

/**
 * struct dvb_frontend_info - Frontend properties and capabilities
 *
 * @name:                       Name of the frontend
 * @type:                       ****DEPRECATED****.
 *                              Should not be used on modern programs,
 *                              as a frontend may have more than one type.
 *                              In order to get the support types of a given
 *                              frontend, use :c:type:`DTV_ENUM_DELSYS`
 *                              instead.
 * @frequency_min:              Minimal frequency supported by the frontend.
 * @frequency_max:              Minimal frequency supported by the frontend.
 * @frequency_stepsize:         All frequencies are multiple of this value.
 * @frequency_tolerance:        Frequency tolerance.
 * @symbol_rate_min:            Minimal symbol rate, in bauds
 *                              (for Cable/Satellite systems).
 * @symbol_rate_max:            Maximal symbol rate, in bauds
 *                              (for Cable/Satellite systems).
 * @symbol_rate_tolerance:      Maximal symbol rate tolerance, in ppm
 *                              (for Cable/Satellite systems).
 * @notifier_delay:             ****DEPRECATED****. Not used by any driver.
 * @caps:                       Capabilities supported by the frontend,
 *                              as specified in &enum fe_caps.
 *
 * .. note:
 *
 *    #. The frequencies are specified in Hz for Terrestrial and Cable
 *       systems.
 *    #. The frequencies are specified in kHz for Satellite systems.
 */
struct dvb_frontend_info {
        char       name[128];
        enum fe_type type;      /* DEPRECATED. Use DTV_ENUM_DELSYS instead */
        __u32      frequency_min;
        __u32      frequency_max;
        __u32      frequency_stepsize;
        __u32      frequency_tolerance;
        __u32      symbol_rate_min;
        __u32      symbol_rate_max;
        __u32      symbol_rate_tolerance;
        __u32      notifier_delay;              /* DEPRECATED */
        enum fe_caps caps;
};

/**
 * struct dvb_diseqc_master_cmd - DiSEqC master command
 *
 * @msg:
 *      DiSEqC message to be sent. It contains a 3 bytes header with:
 *      framing + address + command, and an optional argument
 *      of up to 3 bytes of data.
 * @msg_len:
 *      Length of the DiSEqC message. Valid values are 3 to 6.
 *
 * Check out the DiSEqC bus spec available on http://www.eutelsat.org/ for
 * the possible messages that can be used.
 */
struct dvb_diseqc_master_cmd {
        __u8 msg[6];
        __u8 msg_len;
};

/**
 * struct dvb_diseqc_slave_reply - DiSEqC received data
 *
 * @msg:
 *      DiSEqC message buffer to store a message received via DiSEqC.
 *      It contains one byte header with: framing and
 *      an optional argument of up to 3 bytes of data.
 * @msg_len:
 *      Length of the DiSEqC message. Valid values are 0 to 4,
 *      where 0 means no message.
 * @timeout:
 *      Return from ioctl after timeout ms with errorcode when
 *      no message was received.
 *
 * Check out the DiSEqC bus spec available on http://www.eutelsat.org/ for
 * the possible messages that can be used.
 */
struct dvb_diseqc_slave_reply {
        __u8 msg[4];
        __u8 msg_len;
        int  timeout;
};

/**
 * enum fe_sec_voltage - DC Voltage used to feed the LNBf
 *
 * @SEC_VOLTAGE_13:     Output 13V to the LNBf
 * @SEC_VOLTAGE_18:     Output 18V to the LNBf
 * @SEC_VOLTAGE_OFF:    Don't feed the LNBf with a DC voltage
 */
enum fe_sec_voltage {
        SEC_VOLTAGE_13,
        SEC_VOLTAGE_18,
        SEC_VOLTAGE_OFF
};

/**
 * enum fe_sec_tone_mode - Type of tone to be send to the LNBf.
 * @SEC_TONE_ON:        Sends a 22kHz tone burst to the antenna.
 * @SEC_TONE_OFF:       Don't send a 22kHz tone to the antenna (except
 *                      if the ``FE_DISEQC_*`` ioctls are called).
 */
enum fe_sec_tone_mode {
        SEC_TONE_ON,
        SEC_TONE_OFF
};

/**
 * enum fe_sec_mini_cmd - Type of mini burst to be sent
 *
 * @SEC_MINI_A:         Sends a mini-DiSEqC 22kHz '0' Tone Burst to select
 *                      satellite-A
 * @SEC_MINI_B:         Sends a mini-DiSEqC 22kHz '1' Data Burst to select
 *                      satellite-B
 */
enum fe_sec_mini_cmd {
        SEC_MINI_A,
        SEC_MINI_B
};

/**
 * enum fe_status - Enumerates the possible frontend status.
 * @FE_NONE:            The frontend doesn't have any kind of lock.
 *                      That's the initial frontend status
 * @FE_HAS_SIGNAL:      Has found something above the noise level.
 * @FE_HAS_CARRIER:     Has found a signal.
 * @FE_HAS_VITERBI:     FEC inner coding (Viterbi, LDPC or other inner code).
 *                      is stable.
 * @FE_HAS_SYNC:        Synchronization bytes was found.
 * @FE_HAS_LOCK:        Digital TV were locked and everything is working.
 * @FE_TIMEDOUT:        Fo lock within the last about 2 seconds.
 * @FE_REINIT:          Frontend was reinitialized, application is recommended
 *                      to reset DiSEqC, tone and parameters.
 */
enum fe_status {
        FE_NONE                 = 0x00,
        FE_HAS_SIGNAL           = 0x01,
        FE_HAS_CARRIER          = 0x02,
        FE_HAS_VITERBI          = 0x04,
        FE_HAS_SYNC             = 0x08,
        FE_HAS_LOCK             = 0x10,
        FE_TIMEDOUT             = 0x20,
        FE_REINIT               = 0x40,
};

/**
 * enum fe_spectral_inversion - Type of inversion band
 *
 * @INVERSION_OFF:      Don't do spectral band inversion.
 * @INVERSION_ON:       Do spectral band inversion.
 * @INVERSION_AUTO:     Autodetect spectral band inversion.
 *
 * This parameter indicates if spectral inversion should be presumed or
 * not. In the automatic setting (``INVERSION_AUTO``) the hardware will try
 * to figure out the correct setting by itself. If the hardware doesn't
 * support, the %dvb_frontend will try to lock at the carrier first with
 * inversion off. If it fails, it will try to enable inversion.
 */
enum fe_spectral_inversion {
        INVERSION_OFF,
        INVERSION_ON,
        INVERSION_AUTO
};

/**
 * enum fe_code_rate - Type of Forward Error Correction (FEC)
 *
 * @FEC_NONE: No Forward Error Correction Code
 * @FEC_1_2:  Forward Error Correction Code 1/2
 * @FEC_2_3:  Forward Error Correction Code 2/3
 * @FEC_3_4:  Forward Error Correction Code 3/4
 * @FEC_4_5:  Forward Error Correction Code 4/5
 * @FEC_5_6:  Forward Error Correction Code 5/6
 * @FEC_6_7:  Forward Error Correction Code 6/7
 * @FEC_7_8:  Forward Error Correction Code 7/8
 * @FEC_8_9:  Forward Error Correction Code 8/9
 * @FEC_AUTO: Autodetect Error Correction Code
 * @FEC_3_5:  Forward Error Correction Code 3/5
 * @FEC_9_10: Forward Error Correction Code 9/10
 * @FEC_2_5:  Forward Error Correction Code 2/5
 * @FEC_1_3:  Forward Error Correction Code 1/3
 * @FEC_1_4:  Forward Error Correction Code 1/4
 * @FEC_5_9:  Forward Error Correction Code 5/9
 * @FEC_7_9:  Forward Error Correction Code 7/9
 * @FEC_8_15:  Forward Error Correction Code 8/15
 * @FEC_11_15: Forward Error Correction Code 11/15
 * @FEC_13_18: Forward Error Correction Code 13/18
 * @FEC_9_20:  Forward Error Correction Code 9/20
 * @FEC_11_20: Forward Error Correction Code 11/20
 * @FEC_23_36: Forward Error Correction Code 23/36
 * @FEC_25_36: Forward Error Correction Code 25/36
 * @FEC_13_45: Forward Error Correction Code 13/45
 * @FEC_26_45: Forward Error Correction Code 26/45
 * @FEC_28_45: Forward Error Correction Code 28/45
 * @FEC_32_45: Forward Error Correction Code 32/45
 * @FEC_77_90: Forward Error Correction Code 77/90
 * @FEC_11_45: Forward Error Correction Code 11/45
 * @FEC_4_15: Forward Error Correction Code 4/15
 * @FEC_14_45: Forward Error Correction Code 14/45
 * @FEC_7_15: Forward Error Correction Code 7/15
 *
 * Please note that not all FEC types are supported by a given standard.
 */
enum fe_code_rate {
        FEC_NONE = 0,
        FEC_1_2,
        FEC_2_3,
        FEC_3_4,
        FEC_4_5,
        FEC_5_6,
        FEC_6_7,
        FEC_7_8,
        FEC_8_9,
        FEC_AUTO,
        FEC_3_5,
        FEC_9_10,
        FEC_2_5,
        FEC_1_3,
        FEC_1_4,
        FEC_5_9,
        FEC_7_9,
        FEC_8_15,
        FEC_11_15,
        FEC_13_18,
        FEC_9_20,
        FEC_11_20,
        FEC_23_36,
        FEC_25_36,
        FEC_13_45,
        FEC_26_45,
        FEC_28_45,
        FEC_32_45,
        FEC_77_90,
        FEC_11_45,
        FEC_4_15,
        FEC_14_45,
        FEC_7_15,
};

/**
 * enum fe_modulation - Type of modulation/constellation
 * @QPSK:       QPSK modulation
 * @QAM_16:     16-QAM modulation
 * @QAM_32:     32-QAM modulation
 * @QAM_64:     64-QAM modulation
 * @QAM_128:    128-QAM modulation
 * @QAM_256:    256-QAM modulation
 * @QAM_AUTO:   Autodetect QAM modulation
 * @VSB_8:      8-VSB modulation
 * @VSB_16:     16-VSB modulation
 * @PSK_8:      8-PSK modulation
 * @APSK_16:    16-APSK modulation
 * @APSK_32:    32-APSK modulation
 * @DQPSK:      DQPSK modulation
 * @QAM_4_NR:   4-QAM-NR modulation
 * @QAM_1024:   1024-QAM modulation
 * @QAM_4096:   4096-QAM modulation
 * @APSK_8_L:   8APSK-L modulation
 * @APSK_16_L:  16APSK-L modulation
 * @APSK_32_L:  32APSK-L modulation
 * @APSK_64:    64APSK modulation
 * @APSK_64_L:  64APSK-L modulation
 *
 * Please note that not all modulations are supported by a given standard.
 *
 */
enum fe_modulation {
        QPSK,
        QAM_16,
        QAM_32,
        QAM_64,
        QAM_128,
        QAM_256,
        QAM_AUTO,
        VSB_8,
        VSB_16,
        PSK_8,
        APSK_16,
        APSK_32,
        DQPSK,
        QAM_4_NR,
        QAM_1024,
        QAM_4096,
        APSK_8_L,
        APSK_16_L,
        APSK_32_L,
        APSK_64,
        APSK_64_L,
};

/**
 * enum fe_transmit_mode - Transmission mode
 *
 * @TRANSMISSION_MODE_AUTO:
 *      Autodetect transmission mode. The hardware will try to find the
 *      correct FFT-size (if capable) to fill in the missing parameters.
 * @TRANSMISSION_MODE_1K:
 *      Transmission mode 1K
 * @TRANSMISSION_MODE_2K:
 *      Transmission mode 2K
 * @TRANSMISSION_MODE_8K:
 *      Transmission mode 8K
 * @TRANSMISSION_MODE_4K:
 *      Transmission mode 4K
 * @TRANSMISSION_MODE_16K:
 *      Transmission mode 16K
 * @TRANSMISSION_MODE_32K:
 *      Transmission mode 32K
 * @TRANSMISSION_MODE_C1:
 *      Single Carrier (C=1) transmission mode (DTMB only)
 * @TRANSMISSION_MODE_C3780:
 *      Multi Carrier (C=3780) transmission mode (DTMB only)
 *
 * Please note that not all transmission modes are supported by a given
 * standard.
 */
enum fe_transmit_mode {
        TRANSMISSION_MODE_2K,
        TRANSMISSION_MODE_8K,
        TRANSMISSION_MODE_AUTO,
        TRANSMISSION_MODE_4K,
        TRANSMISSION_MODE_1K,
        TRANSMISSION_MODE_16K,
        TRANSMISSION_MODE_32K,
        TRANSMISSION_MODE_C1,
        TRANSMISSION_MODE_C3780,
};

/**
 * enum fe_guard_interval - Guard interval
 *
 * @GUARD_INTERVAL_AUTO:        Autodetect the guard interval
 * @GUARD_INTERVAL_1_128:       Guard interval 1/128
 * @GUARD_INTERVAL_1_32:        Guard interval 1/32
 * @GUARD_INTERVAL_1_16:        Guard interval 1/16
 * @GUARD_INTERVAL_1_8:         Guard interval 1/8
 * @GUARD_INTERVAL_1_4:         Guard interval 1/4
 * @GUARD_INTERVAL_19_128:      Guard interval 19/128
 * @GUARD_INTERVAL_19_256:      Guard interval 19/256
 * @GUARD_INTERVAL_PN420:       PN length 420 (1/4)
 * @GUARD_INTERVAL_PN595:       PN length 595 (1/6)
 * @GUARD_INTERVAL_PN945:       PN length 945 (1/9)
 * @GUARD_INTERVAL_1_64:        Guard interval 1/64
 *
 * Please note that not all guard intervals are supported by a given standard.
 */
enum fe_guard_interval {
        GUARD_INTERVAL_1_32,
        GUARD_INTERVAL_1_16,
        GUARD_INTERVAL_1_8,
        GUARD_INTERVAL_1_4,
        GUARD_INTERVAL_AUTO,
        GUARD_INTERVAL_1_128,
        GUARD_INTERVAL_19_128,
        GUARD_INTERVAL_19_256,
        GUARD_INTERVAL_PN420,
        GUARD_INTERVAL_PN595,
        GUARD_INTERVAL_PN945,
        GUARD_INTERVAL_1_64,
};

/**
 * enum fe_hierarchy - Hierarchy
 * @HIERARCHY_NONE:     No hierarchy
 * @HIERARCHY_AUTO:     Autodetect hierarchy (if supported)
 * @HIERARCHY_1:        Hierarchy 1
 * @HIERARCHY_2:        Hierarchy 2
 * @HIERARCHY_4:        Hierarchy 4
 *
 * Please note that not all hierarchy types are supported by a given standard.
 */
enum fe_hierarchy {
        HIERARCHY_NONE,
        HIERARCHY_1,
        HIERARCHY_2,
        HIERARCHY_4,
        HIERARCHY_AUTO
};

/**
 * enum fe_interleaving - Interleaving
 * @INTERLEAVING_NONE:  No interleaving.
 * @INTERLEAVING_AUTO:  Auto-detect interleaving.
 * @INTERLEAVING_240:   Interleaving of 240 symbols.
 * @INTERLEAVING_720:   Interleaving of 720 symbols.
 *
 * Please note that, currently, only DTMB uses it.
 */
enum fe_interleaving {
        INTERLEAVING_NONE,
        INTERLEAVING_AUTO,
        INTERLEAVING_240,
        INTERLEAVING_720,
};

/* DVBv5 property Commands */

#define DTV_UNDEFINED           0
#define DTV_TUNE                1
#define DTV_CLEAR               2
#define DTV_FREQUENCY           3
#define DTV_MODULATION          4
#define DTV_BANDWIDTH_HZ        5
#define DTV_INVERSION           6
#define DTV_DISEQC_MASTER       7
#define DTV_SYMBOL_RATE         8
#define DTV_INNER_FEC           9
#define DTV_VOLTAGE             10
#define DTV_TONE                11
#define DTV_PILOT               12
#define DTV_ROLLOFF             13
#define DTV_DISEQC_SLAVE_REPLY  14

/* Basic enumeration set for querying unlimited capabilities */
#define DTV_FE_CAPABILITY_COUNT 15
#define DTV_FE_CAPABILITY       16
#define DTV_DELIVERY_SYSTEM     17

/* ISDB-T and ISDB-Tsb */
#define DTV_ISDBT_PARTIAL_RECEPTION     18
#define DTV_ISDBT_SOUND_BROADCASTING    19

#define DTV_ISDBT_SB_SUBCHANNEL_ID      20
#define DTV_ISDBT_SB_SEGMENT_IDX        21
#define DTV_ISDBT_SB_SEGMENT_COUNT      22

#define DTV_ISDBT_LAYERA_FEC                    23
#define DTV_ISDBT_LAYERA_MODULATION             24
#define DTV_ISDBT_LAYERA_SEGMENT_COUNT          25
#define DTV_ISDBT_LAYERA_TIME_INTERLEAVING      26

#define DTV_ISDBT_LAYERB_FEC                    27
#define DTV_ISDBT_LAYERB_MODULATION             28
#define DTV_ISDBT_LAYERB_SEGMENT_COUNT          29
#define DTV_ISDBT_LAYERB_TIME_INTERLEAVING      30

#define DTV_ISDBT_LAYERC_FEC                    31
#define DTV_ISDBT_LAYERC_MODULATION             32
#define DTV_ISDBT_LAYERC_SEGMENT_COUNT          33
#define DTV_ISDBT_LAYERC_TIME_INTERLEAVING      34

#define DTV_API_VERSION         35

#define DTV_CODE_RATE_HP        36
#define DTV_CODE_RATE_LP        37
#define DTV_GUARD_INTERVAL      38
#define DTV_TRANSMISSION_MODE   39
#define DTV_HIERARCHY           40

#define DTV_ISDBT_LAYER_ENABLED 41

#define DTV_STREAM_ID           42
#define DTV_ISDBS_TS_ID_LEGACY  DTV_STREAM_ID
#define DTV_DVBT2_PLP_ID_LEGACY 43

#define DTV_ENUM_DELSYS         44

/* ATSC-MH */
#define DTV_ATSCMH_FIC_VER              45
#define DTV_ATSCMH_PARADE_ID            46
#define DTV_ATSCMH_NOG                  47
#define DTV_ATSCMH_TNOG                 48
#define DTV_ATSCMH_SGN                  49
#define DTV_ATSCMH_PRC                  50
#define DTV_ATSCMH_RS_FRAME_MODE        51
#define DTV_ATSCMH_RS_FRAME_ENSEMBLE    52
#define DTV_ATSCMH_RS_CODE_MODE_PRI     53
#define DTV_ATSCMH_RS_CODE_MODE_SEC     54
#define DTV_ATSCMH_SCCC_BLOCK_MODE      55
#define DTV_ATSCMH_SCCC_CODE_MODE_A     56
#define DTV_ATSCMH_SCCC_CODE_MODE_B     57
#define DTV_ATSCMH_SCCC_CODE_MODE_C     58
#define DTV_ATSCMH_SCCC_CODE_MODE_D     59

#define DTV_INTERLEAVING                        60
#define DTV_LNA                                 61

/* Quality parameters */
#define DTV_STAT_SIGNAL_STRENGTH        62
#define DTV_STAT_CNR                    63
#define DTV_STAT_PRE_ERROR_BIT_COUNT    64
#define DTV_STAT_PRE_TOTAL_BIT_COUNT    65
#define DTV_STAT_POST_ERROR_BIT_COUNT   66
#define DTV_STAT_POST_TOTAL_BIT_COUNT   67
#define DTV_STAT_ERROR_BLOCK_COUNT      68
#define DTV_STAT_TOTAL_BLOCK_COUNT      69

/* Physical layer scrambling */
#define DTV_SCRAMBLING_SEQUENCE_INDEX   70

#define DTV_MAX_COMMAND         DTV_SCRAMBLING_SEQUENCE_INDEX

/**
 * enum fe_pilot - Type of pilot tone
 *
 * @PILOT_ON:   Pilot tones enabled
 * @PILOT_OFF:  Pilot tones disabled
 * @PILOT_AUTO: Autodetect pilot tones
 */
enum fe_pilot {
        PILOT_ON,
        PILOT_OFF,
        PILOT_AUTO,
};

/**
 * enum fe_rolloff - Rolloff factor
 * @ROLLOFF_35:         Roloff factor: α=35%
 * @ROLLOFF_20:         Roloff factor: α=20%
 * @ROLLOFF_25:         Roloff factor: α=25%
 * @ROLLOFF_AUTO:       Auto-detect the roloff factor.
 * @ROLLOFF_15:         Rolloff factor: α=15%
 * @ROLLOFF_10:         Rolloff factor: α=10%
 * @ROLLOFF_5:          Rolloff factor: α=5%
 *
 * .. note:
 *
 *    Roloff factor of 35% is implied on DVB-S. On DVB-S2, it is default.
 */
enum fe_rolloff {
        ROLLOFF_35,
        ROLLOFF_20,
        ROLLOFF_25,
        ROLLOFF_AUTO,
        ROLLOFF_15,
        ROLLOFF_10,
        ROLLOFF_5,
};

/**
 * enum fe_delivery_system - Type of the delivery system
 *
 * @SYS_UNDEFINED:
 *      Undefined standard. Generally, indicates an error
 * @SYS_DVBC_ANNEX_A:
 *      Cable TV: DVB-C following ITU-T J.83 Annex A spec
 * @SYS_DVBC_ANNEX_B:
 *      Cable TV: DVB-C following ITU-T J.83 Annex B spec (ClearQAM)
 * @SYS_DVBC_ANNEX_C:
 *      Cable TV: DVB-C following ITU-T J.83 Annex C spec
 * @SYS_DVBC2:
 *      Cable TV: DVB-C2
 * @SYS_ISDBC:
 *      Cable TV: ISDB-C (no drivers yet)
 * @SYS_DVBT:
 *      Terrestrial TV: DVB-T
 * @SYS_DVBT2:
 *      Terrestrial TV: DVB-T2
 * @SYS_ISDBT:
 *      Terrestrial TV: ISDB-T
 * @SYS_ATSC:
 *      Terrestrial TV: ATSC
 * @SYS_ATSCMH:
 *      Terrestrial TV (mobile): ATSC-M/H
 * @SYS_DTMB:
 *      Terrestrial TV: DTMB
 * @SYS_DVBS:
 *      Satellite TV: DVB-S
 * @SYS_DVBS2:
 *      Satellite TV: DVB-S2 and DVB-S2X
 * @SYS_TURBO:
 *      Satellite TV: DVB-S Turbo
 * @SYS_ISDBS:
 *      Satellite TV: ISDB-S
 * @SYS_DAB:
 *      Digital audio: DAB (not fully supported)
 * @SYS_DSS:
 *      Satellite TV: DSS (not fully supported)
 * @SYS_CMMB:
 *      Terrestrial TV (mobile): CMMB (not fully supported)
 * @SYS_DVBH:
 *      Terrestrial TV (mobile): DVB-H (standard deprecated)
 */
enum fe_delivery_system {
        SYS_UNDEFINED,
        SYS_DVBC_ANNEX_A,
        SYS_DVBC_ANNEX_B,
        SYS_DVBT,
        SYS_DSS,
        SYS_DVBS,
        SYS_DVBS2,
        SYS_DVBH,
        SYS_ISDBT,
        SYS_ISDBS,
        SYS_ISDBC,
        SYS_ATSC,
        SYS_ATSCMH,
        SYS_DTMB,
        SYS_CMMB,
        SYS_DAB,
        SYS_DVBT2,
        SYS_TURBO,
        SYS_DVBC_ANNEX_C,
        SYS_DVBC2,
};

/* backward compatibility definitions for delivery systems */
#define SYS_DVBC_ANNEX_AC       SYS_DVBC_ANNEX_A
#define SYS_DMBTH               SYS_DTMB /* DMB-TH is legacy name, use DTMB */

/* ATSC-MH specific parameters */

/**
 * enum atscmh_sccc_block_mode - Type of Series Concatenated Convolutional
 *                               Code Block Mode.
 *
 * @ATSCMH_SCCC_BLK_SEP:
 *      Separate SCCC: the SCCC outer code mode shall be set independently
 *      for each Group Region (A, B, C, D)
 * @ATSCMH_SCCC_BLK_COMB:
 *      Combined SCCC: all four Regions shall have the same SCCC outer
 *      code mode.
 * @ATSCMH_SCCC_BLK_RES:
 *      Reserved. Shouldn't be used.
 */
enum atscmh_sccc_block_mode {
        ATSCMH_SCCC_BLK_SEP      = 0,
        ATSCMH_SCCC_BLK_COMB     = 1,
        ATSCMH_SCCC_BLK_RES      = 2,
};

/**
 * enum atscmh_sccc_code_mode - Type of Series Concatenated Convolutional
 *                              Code Rate.
 *
 * @ATSCMH_SCCC_CODE_HLF:
 *      The outer code rate of a SCCC Block is 1/2 rate.
 * @ATSCMH_SCCC_CODE_QTR:
 *      The outer code rate of a SCCC Block is 1/4 rate.
 * @ATSCMH_SCCC_CODE_RES:
 *      Reserved. Should not be used.
 */
enum atscmh_sccc_code_mode {
        ATSCMH_SCCC_CODE_HLF     = 0,
        ATSCMH_SCCC_CODE_QTR     = 1,
        ATSCMH_SCCC_CODE_RES     = 2,
};

/**
 * enum atscmh_rs_frame_ensemble - Reed Solomon(RS) frame ensemble.
 *
 * @ATSCMH_RSFRAME_ENS_PRI:     Primary Ensemble.
 * @ATSCMH_RSFRAME_ENS_SEC:     Secondary Ensemble.
 */
enum atscmh_rs_frame_ensemble {
        ATSCMH_RSFRAME_ENS_PRI   = 0,
        ATSCMH_RSFRAME_ENS_SEC   = 1,
};

/**
 * enum atscmh_rs_frame_mode - Reed Solomon (RS) frame mode.
 *
 * @ATSCMH_RSFRAME_PRI_ONLY:
 *      Single Frame: There is only a primary RS Frame for all Group
 *      Regions.
 * @ATSCMH_RSFRAME_PRI_SEC:
 *      Dual Frame: There are two separate RS Frames: Primary RS Frame for
 *      Group Region A and B and Secondary RS Frame for Group Region C and
 *      D.
 * @ATSCMH_RSFRAME_RES:
 *      Reserved. Shouldn't be used.
 */
enum atscmh_rs_frame_mode {
        ATSCMH_RSFRAME_PRI_ONLY  = 0,
        ATSCMH_RSFRAME_PRI_SEC   = 1,
        ATSCMH_RSFRAME_RES       = 2,
};

/**
 * enum atscmh_rs_code_mode - ATSC-M/H Reed Solomon modes
 * @ATSCMH_RSCODE_211_187:      Reed Solomon code (211,187).
 * @ATSCMH_RSCODE_223_187:      Reed Solomon code (223,187).
 * @ATSCMH_RSCODE_235_187:      Reed Solomon code (235,187).
 * @ATSCMH_RSCODE_RES:          Reserved. Shouldn't be used.
 */
enum atscmh_rs_code_mode {
        ATSCMH_RSCODE_211_187    = 0,
        ATSCMH_RSCODE_223_187    = 1,
        ATSCMH_RSCODE_235_187    = 2,
        ATSCMH_RSCODE_RES        = 3,
};

#define NO_STREAM_ID_FILTER     (~0U)
#define LNA_AUTO                (~0U)

/**
 * enum fecap_scale_params - scale types for the quality parameters.
 *
 * @FE_SCALE_NOT_AVAILABLE: That QoS measure is not available. That
 *                          could indicate a temporary or a permanent
 *                          condition.
 * @FE_SCALE_DECIBEL: The scale is measured in 0.001 dB steps, typically
 *                    used on signal measures.
 * @FE_SCALE_RELATIVE: The scale is a relative percentual measure,
 *                     ranging from 0 (0%) to 0xffff (100%).
 * @FE_SCALE_COUNTER: The scale counts the occurrence of an event, like
 *                    bit error, block error, lapsed time.
 */
enum fecap_scale_params {
        FE_SCALE_NOT_AVAILABLE = 0,
        FE_SCALE_DECIBEL,
        FE_SCALE_RELATIVE,
        FE_SCALE_COUNTER
};

/**
 * struct dtv_stats - Used for reading a DTV status property
 *
 * @scale:
 *      Filled with enum fecap_scale_params - the scale in usage
 *      for that parameter
 *
 * @svalue:
 *      integer value of the measure, for %FE_SCALE_DECIBEL,
 *      used for dB measures. The unit is 0.001 dB.
 *
 * @uvalue:
 *      unsigned integer value of the measure, used when @scale is
 *      either %FE_SCALE_RELATIVE or %FE_SCALE_COUNTER.
 *
 * For most delivery systems, this will return a single value for each
 * parameter.
 *
 * It should be noticed, however, that new OFDM delivery systems like
 * ISDB can use different modulation types for each group of carriers.
 * On such standards, up to 8 groups of statistics can be provided, one
 * for each carrier group (called "layer" on ISDB).
 *
 * In order to be consistent with other delivery systems, the first
 * value refers to the entire set of carriers ("global").
 *
 * @scale should use the value %FE_SCALE_NOT_AVAILABLE when
 * the value for the entire group of carriers or from one specific layer
 * is not provided by the hardware.
 *
 * @len should be filled with the latest filled status + 1.
 *
 * In other words, for ISDB, those values should be filled like::
 *
 *      u.st.stat.svalue[0] = global statistics;
 *      u.st.stat.scale[0] = FE_SCALE_DECIBEL;
 *      u.st.stat.value[1] = layer A statistics;
 *      u.st.stat.scale[1] = FE_SCALE_NOT_AVAILABLE (if not available);
 *      u.st.stat.svalue[2] = layer B statistics;
 *      u.st.stat.scale[2] = FE_SCALE_DECIBEL;
 *      u.st.stat.svalue[3] = layer C statistics;
 *      u.st.stat.scale[3] = FE_SCALE_DECIBEL;
 *      u.st.len = 4;
 */
struct dtv_stats {
        __u8 scale;     /* enum fecap_scale_params type */
        union {
                __u64 uvalue;   /* for counters and relative scales */
                __s64 svalue;   /* for 0.001 dB measures */
        };
} __attribute__ ((packed));

#define MAX_DTV_STATS   4

/**
 * struct dtv_fe_stats - store Digital TV frontend statistics
 *
 * @len:        length of the statistics - if zero, stats is disabled.
 * @stat:       array with digital TV statistics.
 *
 * On most standards, @len can either be 0 or 1. However, for ISDB, each
 * layer is modulated in separate. So, each layer may have its own set
 * of statistics. If so, stat[0] carries on a global value for the property.
 * Indexes 1 to 3 means layer A to B.
 */
struct dtv_fe_stats {
        __u8 len;
        struct dtv_stats stat[MAX_DTV_STATS];
} __attribute__ ((packed));

/**
 * struct dtv_property - store one of frontend command and its value
 *
 * @cmd:                Digital TV command.
 * @reserved:           Not used.
 * @u:                  Union with the values for the command.
 * @u.data:             A unsigned 32 bits integer with command value.
 * @u.buffer:           Struct to store bigger properties.
 *                      Currently unused.
 * @u.buffer.data:      an unsigned 32-bits array.
 * @u.buffer.len:       number of elements of the buffer.
 * @u.buffer.reserved1: Reserved.
 * @u.buffer.reserved2: Reserved.
 * @u.st:               a &struct dtv_fe_stats array of statistics.
 * @result:             Currently unused.
 *
 */
struct dtv_property {
        __u32 cmd;
        __u32 reserved[3];
        union {
                __u32 data;
                struct dtv_fe_stats st;
                struct {
                        __u8 data[32];
                        __u32 len;
                        __u32 reserved1[3];
                        void *reserved2;
                } buffer;
        } u;
        int result;
} __attribute__ ((packed));

/* num of properties cannot exceed DTV_IOCTL_MAX_MSGS per ioctl */
#define DTV_IOCTL_MAX_MSGS 64

/**
 * struct dtv_properties - a set of command/value pairs.
 *
 * @num:        amount of commands stored at the struct.
 * @props:      a pointer to &struct dtv_property.
 */
struct dtv_properties {
        __u32 num;
        struct dtv_property *props;
};

/*
 * When set, this flag will disable any zigzagging or other "normal" tuning
 * behavior. Additionally, there will be no automatic monitoring of the lock
 * status, and hence no frontend events will be generated. If a frontend device
 * is closed, this flag will be automatically turned off when the device is
 * reopened read-write.
 */
#define FE_TUNE_MODE_ONESHOT 0x01

/* Digital TV Frontend API calls */

#define FE_GET_INFO                _IOR('o', 61, struct dvb_frontend_info)

#define FE_DISEQC_RESET_OVERLOAD   _IO('o', 62)
#define FE_DISEQC_SEND_MASTER_CMD  _IOW('o', 63, struct dvb_diseqc_master_cmd)
#define FE_DISEQC_RECV_SLAVE_REPLY _IOR('o', 64, struct dvb_diseqc_slave_reply)
#define FE_DISEQC_SEND_BURST       _IO('o', 65)  /* fe_sec_mini_cmd_t */

#define FE_SET_TONE                _IO('o', 66)  /* fe_sec_tone_mode_t */
#define FE_SET_VOLTAGE             _IO('o', 67)  /* fe_sec_voltage_t */
#define FE_ENABLE_HIGH_LNB_VOLTAGE _IO('o', 68)  /* int */

#define FE_READ_STATUS             _IOR('o', 69, fe_status_t)
#define FE_READ_BER                _IOR('o', 70, __u32)
#define FE_READ_SIGNAL_STRENGTH    _IOR('o', 71, __u16)
#define FE_READ_SNR                _IOR('o', 72, __u16)
#define FE_READ_UNCORRECTED_BLOCKS _IOR('o', 73, __u32)

#define FE_SET_FRONTEND_TUNE_MODE  _IO('o', 81) /* unsigned int */
#define FE_GET_EVENT               _IOR('o', 78, struct dvb_frontend_event)

#define FE_DISHNETWORK_SEND_LEGACY_CMD _IO('o', 80) /* unsigned int */

#define FE_SET_PROPERTY            _IOW('o', 82, struct dtv_properties)
#define FE_GET_PROPERTY            _IOR('o', 83, struct dtv_properties)

#if defined(__DVB_CORE__) || !defined(__KERNEL__)

/*
 * DEPRECATED: Everything below is deprecated in favor of DVBv5 API
 *
 * The DVBv3 only ioctls, structs and enums should not be used on
 * newer programs, as it doesn't support the second generation of
 * digital TV standards, nor supports newer delivery systems.
 * They also don't support modern frontends with usually support multiple
 * delivery systems.
 *
 * Drivers shouldn't use them.
 *
 * New applications should use DVBv5 delivery system instead
 */

/*
 */

enum fe_bandwidth {
        BANDWIDTH_8_MHZ,
        BANDWIDTH_7_MHZ,
        BANDWIDTH_6_MHZ,
        BANDWIDTH_AUTO,
        BANDWIDTH_5_MHZ,
        BANDWIDTH_10_MHZ,
        BANDWIDTH_1_712_MHZ,
};

/* This is kept for legacy userspace support */
typedef enum fe_sec_voltage fe_sec_voltage_t;
typedef enum fe_caps fe_caps_t;
typedef enum fe_type fe_type_t;
typedef enum fe_sec_tone_mode fe_sec_tone_mode_t;
typedef enum fe_sec_mini_cmd fe_sec_mini_cmd_t;
typedef enum fe_status fe_status_t;
typedef enum fe_spectral_inversion fe_spectral_inversion_t;
typedef enum fe_code_rate fe_code_rate_t;
typedef enum fe_modulation fe_modulation_t;
typedef enum fe_transmit_mode fe_transmit_mode_t;
typedef enum fe_bandwidth fe_bandwidth_t;
typedef enum fe_guard_interval fe_guard_interval_t;
typedef enum fe_hierarchy fe_hierarchy_t;
typedef enum fe_pilot fe_pilot_t;
typedef enum fe_rolloff fe_rolloff_t;
typedef enum fe_delivery_system fe_delivery_system_t;

/* DVBv3 structs */

struct dvb_qpsk_parameters {
        __u32           symbol_rate;  /* symbol rate in Symbols per second */
        fe_code_rate_t  fec_inner;    /* forward error correction (see above) */
};

struct dvb_qam_parameters {
        __u32           symbol_rate; /* symbol rate in Symbols per second */
        fe_code_rate_t  fec_inner;   /* forward error correction (see above) */
        fe_modulation_t modulation;  /* modulation type (see above) */
};

struct dvb_vsb_parameters {
        fe_modulation_t modulation;  /* modulation type (see above) */
};

struct dvb_ofdm_parameters {
        fe_bandwidth_t      bandwidth;
        fe_code_rate_t      code_rate_HP;  /* high priority stream code rate */
        fe_code_rate_t      code_rate_LP;  /* low priority stream code rate */
        fe_modulation_t     constellation; /* modulation type (see above) */
        fe_transmit_mode_t  transmission_mode;
        fe_guard_interval_t guard_interval;
        fe_hierarchy_t      hierarchy_information;
};

struct dvb_frontend_parameters {
        __u32 frequency;  /* (absolute) frequency in Hz for DVB-C/DVB-T/ATSC */
                          /* intermediate frequency in kHz for DVB-S */
        fe_spectral_inversion_t inversion;
        union {
                struct dvb_qpsk_parameters qpsk;        /* DVB-S */
                struct dvb_qam_parameters  qam;         /* DVB-C */
                struct dvb_ofdm_parameters ofdm;        /* DVB-T */
                struct dvb_vsb_parameters vsb;          /* ATSC */
        } u;
};

struct dvb_frontend_event {
        fe_status_t status;
        struct dvb_frontend_parameters parameters;
};

/* DVBv3 API calls */

#define FE_SET_FRONTEND            _IOW('o', 76, struct dvb_frontend_parameters)
#define FE_GET_FRONTEND            _IOR('o', 77, struct dvb_frontend_parameters)

#endif

#endif /*_DVBFRONTEND_H_*/
```

### 8.1.2. dmx.h

```
/* SPDX-License-Identifier: LGPL-2.1+ WITH Linux-syscall-note */
/*
 * dmx.h
 *
 * Copyright (C) 2000 Marcus Metzler <marcus@convergence.de>
 *                  & Ralph  Metzler <ralph@convergence.de>
 *                    for convergence integrated media GmbH
 */

#ifndef _UAPI_DVBDMX_H_
#define _UAPI_DVBDMX_H_

#include <linux/types.h>
#ifndef __KERNEL__
#include <time.h>
#endif

#define DMX_FILTER_SIZE 16

/**
 * enum dmx_output - Output for the demux.
 *
 * @:c:type:DMX_OUT_DECODER <dmx_output>:
 *      Streaming directly to decoder.
 * @:c:type:DMX_OUT_TAP <dmx_output>:
 *      Output going to a memory buffer (to be retrieved via the read command).
 *      Delivers the stream output to the demux device on which the ioctl
 *      is called.
 * @:c:type:DMX_OUT_TS_TAP <dmx_output>:
 *      Output multiplexed into a new TS (to be retrieved by reading from the
 *      logical DVR device). Routes output to the logical DVR device
 *      ``/dev/dvb/adapter?/dvr?``, which delivers a TS multiplexed from all
 *      filters for which @:c:type:DMX_OUT_TS_TAP <dmx_output> was specified.
 * @:c:type:DMX_OUT_TSDEMUX_TAP <dmx_output>:
 *      Like @:c:type:DMX_OUT_TS_TAP <dmx_output> but retrieved from the DMX device.
 */
enum dmx_output {
        DMX_OUT_DECODER,
        DMX_OUT_TAP,
        DMX_OUT_TS_TAP,
        DMX_OUT_TSDEMUX_TAP
};

/**
 * dmx_input - Input from the demux.
 *
 * @:c:type:DMX_IN_FRONTEND <dmx_input>:    Input from a front-end device.
 * @:c:type:DMX_IN_DVR <dmx_input>:         Input from the logical DVR device.
 */
dmx_input {
        DMX_IN_FRONTEND,
        DMX_IN_DVR
};

/**
 * dmx_ts_pes - type of the PES filter.
 *
 * @:c:type:DMX_PES_AUDIO0 <dmx_pes_type>:     first audio PID. Also referred as @DMX_PES_AUDIO.
 * @:c:type:DMX_PES_VIDEO0 <dmx_pes_type>:     first video PID. Also referred as @DMX_PES_VIDEO.
 * @:c:type:DMX_PES_TELETEXT0 <dmx_pes_type>:  first teletext PID. Also referred as @DMX_PES_TELETEXT.
 * @:c:type:DMX_PES_SUBTITLE0 <dmx_pes_type>:  first subtitle PID. Also referred as @DMX_PES_SUBTITLE.
 * @:c:type:DMX_PES_PCR0 <dmx_pes_type>:       first Program Clock Reference PID.
 *                      Also referred as @DMX_PES_PCR.
 *
 * @:c:type:DMX_PES_AUDIO1 <dmx_pes_type>:     second audio PID.
 * @:c:type:DMX_PES_VIDEO1 <dmx_pes_type>:     second video PID.
 * @:c:type:DMX_PES_TELETEXT1 <dmx_pes_type>:  second teletext PID.
 * @:c:type:DMX_PES_SUBTITLE1 <dmx_pes_type>:  second subtitle PID.
 * @:c:type:DMX_PES_PCR1 <dmx_pes_type>:       second Program Clock Reference PID.
 *
 * @:c:type:DMX_PES_AUDIO2 <dmx_pes_type>:     third audio PID.
 * @:c:type:DMX_PES_VIDEO2 <dmx_pes_type>:     third video PID.
 * @:c:type:DMX_PES_TELETEXT2 <dmx_pes_type>:  third teletext PID.
 * @:c:type:DMX_PES_SUBTITLE2 <dmx_pes_type>:  third subtitle PID.
 * @:c:type:DMX_PES_PCR2 <dmx_pes_type>:       third Program Clock Reference PID.
 *
 * @:c:type:DMX_PES_AUDIO3 <dmx_pes_type>:     fourth audio PID.
 * @:c:type:DMX_PES_VIDEO3 <dmx_pes_type>:     fourth video PID.
 * @:c:type:DMX_PES_TELETEXT3 <dmx_pes_type>:  fourth teletext PID.
 * @:c:type:DMX_PES_SUBTITLE3 <dmx_pes_type>:  fourth subtitle PID.
 * @:c:type:DMX_PES_PCR3 <dmx_pes_type>:       fourth Program Clock Reference PID.
 *
 * @:c:type:DMX_PES_OTHER <dmx_pes_type>:      any other PID.
 */

dmx_ts_pes {
        DMX_PES_AUDIO0,
        DMX_PES_VIDEO0,
        DMX_PES_TELETEXT0,
        DMX_PES_SUBTITLE0,
        DMX_PES_PCR0,

        DMX_PES_AUDIO1,
        DMX_PES_VIDEO1,
        DMX_PES_TELETEXT1,
        DMX_PES_SUBTITLE1,
        DMX_PES_PCR1,

        DMX_PES_AUDIO2,
        DMX_PES_VIDEO2,
        DMX_PES_TELETEXT2,
        DMX_PES_SUBTITLE2,
        DMX_PES_PCR2,

        DMX_PES_AUDIO3,
        DMX_PES_VIDEO3,
        DMX_PES_TELETEXT3,
        DMX_PES_SUBTITLE3,
        DMX_PES_PCR3,

        DMX_PES_OTHER
};

#define DMX_PES_AUDIO    DMX_PES_AUDIO0
#define DMX_PES_VIDEO    DMX_PES_VIDEO0
#define DMX_PES_TELETEXT DMX_PES_TELETEXT0
#define DMX_PES_SUBTITLE DMX_PES_SUBTITLE0
#define DMX_PES_PCR      DMX_PES_PCR0

/**
 * struct dmx_filter - Specifies a section header filter.
 *
 * @filter: bit array with bits to be matched at the section header.
 * @mask: bits that are valid at the filter bit array.
 * @mode: mode of match: if bit is zero, it will match if equal (positive
 *        match); if bit is one, it will match if the bit is negated.
 *
 * Note: All arrays in this struct have a size of DMX_FILTER_SIZE (16 bytes).
 */
struct dmx_filter {
        __u8  filter[DMX_FILTER_SIZE];
        __u8  mask[DMX_FILTER_SIZE];
        __u8  mode[DMX_FILTER_SIZE];
};

/**
 * struct dmx_sct_filter_params - Specifies a section filter.
 *
 * @pid: PID to be filtered.
 * @filter: section header filter, as defined by &struct dmx_filter.
 * @timeout: maximum time to filter, in milliseconds.
 * @flags: extra flags for the section filter.
 *
 * Carries the configuration for a MPEG-TS section filter.
 *
 * The @flags can be:
 *
 *      - %DMX_CHECK_CRC - only deliver sections where the CRC check succeeded;
 *      - %DMX_ONESHOT - disable the section filter after one section
 *        has been delivered;
 *      - %DMX_IMMEDIATE_START - Start filter immediately without requiring a
 *        :ref:`DMX_START`.
 */
struct dmx_sct_filter_params {
        __u16             pid;
        struct dmx_filter filter;
        __u32             timeout;
        __u32             flags;
#define DMX_CHECK_CRC       1
#define DMX_ONESHOT         2
#define DMX_IMMEDIATE_START 4
};

/**
 * struct dmx_pes_filter_params - Specifies Packetized Elementary Stream (PES)
 *      filter parameters.
 *
 * @pid:        PID to be filtered.
 * @input:      Demux input, as specified by &enum dmx_input.
 * @output:     Demux output, as specified by &enum dmx_output.
 * @pes_type:   Type of the pes filter, as specified by &enum dmx_pes_type.
 * @flags:      Demux PES flags.
 */
struct dmx_pes_filter_params {
        __u16           pid;
        dmx_input  input;
        enum dmx_output output;
        dmx_ts_pes pes_type;
        __u32           flags;
};

/**
 * struct dmx_stc - Stores System Time Counter (STC) information.
 *
 * @num: input data: number of the STC, from 0 to N.
 * @base: output: divisor for STC to get 90 kHz clock.
 * @stc: output: stc in @base * 90 kHz units.
 */
struct dmx_stc {
        unsigned int num;
        unsigned int base;
        __u64 stc;
};

/**
 * enum dmx_buffer_flags - DMX memory-mapped buffer flags
 *
 * @:c:type:DMX_BUFFER_FLAG_HAD_CRC32_DISCARD <dmx_buffer_flags>:
 *      Indicates that the Kernel discarded one or more frames due to wrong
 *      CRC32 checksum.
 * @:c:type:DMX_BUFFER_FLAG_TEI <dmx_buffer_flags>:
 *      Indicates that the Kernel has detected a Transport Error indicator
 *      (TEI) on a filtered pid.
 * @:c:type:DMX_BUFFER_PKT_COUNTER_MISMATCH <dmx_buffer_flags>:
 *      Indicates that the Kernel has detected a packet counter mismatch
 *      on a filtered pid.
 * @:c:type:DMX_BUFFER_FLAG_DISCONTINUITY_DETECTED <dmx_buffer_flags>:
 *      Indicates that the Kernel has detected one or more frame discontinuity.
 * @:c:type:DMX_BUFFER_FLAG_DISCONTINUITY_INDICATOR <dmx_buffer_flags>:
 *      Received at least one packet with a frame discontinuity indicator.
 */

enum dmx_buffer_flags {
        DMX_BUFFER_FLAG_HAD_CRC32_DISCARD               = 1 << 0,
        DMX_BUFFER_FLAG_TEI                             = 1 << 1,
        DMX_BUFFER_PKT_COUNTER_MISMATCH                 = 1 << 2,
        DMX_BUFFER_FLAG_DISCONTINUITY_DETECTED          = 1 << 3,
        DMX_BUFFER_FLAG_DISCONTINUITY_INDICATOR         = 1 << 4,
};

/**
 * struct dmx_buffer - dmx buffer info
 *
 * @index:      id number of the buffer
 * @bytesused:  number of bytes occupied by data in the buffer (payload);
 * @offset:     for buffers with memory == DMX_MEMORY_MMAP;
 *              offset from the start of the device memory for this plane,
 *              (or a "cookie" that should be passed to mmap() as offset)
 * @length:     size in bytes of the buffer
 * @flags:      bit array of buffer flags as defined by &enum dmx_buffer_flags.
 *              Filled only at &DMX_DQBUF.
 * @count:      monotonic counter for filled buffers. Helps to identify
 *              data stream loses. Filled only at &DMX_DQBUF.
 *
 * Contains data exchanged by application and driver using one of the streaming
 * I/O methods.
 *
 * Please notice that, for &DMX_QBUF, only @index should be filled.
 * On &DMX_DQBUF calls, all fields will be filled by the Kernel.
 */
struct dmx_buffer {
        __u32                   index;
        __u32                   bytesused;
        __u32                   offset;
        __u32                   length;
        __u32                   flags;
        __u32                   count;
};

/**
 * struct dmx_requestbuffers - request dmx buffer information
 *
 * @count:      number of requested buffers,
 * @size:       size in bytes of the requested buffer
 *
 * Contains data used for requesting a dmx buffer.
 * All reserved fields must be set to zero.
 */
struct dmx_requestbuffers {
        __u32                   count;
        __u32                   size;
};

/**
 * struct dmx_exportbuffer - export of dmx buffer as DMABUF file descriptor
 *
 * @index:      id number of the buffer
 * @flags:      flags for newly created file, currently only O_CLOEXEC is
 *              supported, refer to manual of open syscall for more details
 * @fd:         file descriptor associated with DMABUF (set by driver)
 *
 * Contains data used for exporting a dmx buffer as DMABUF file descriptor.
 * The buffer is identified by a 'cookie' returned by DMX_QUERYBUF
 * (identical to the cookie used to mmap() the buffer to userspace). All
 * reserved fields must be set to zero. The field reserved0 is expected to
 * become a structure 'type' allowing an alternative layout of the structure
 * content. Therefore this field should not be used for any other extensions.
 */
struct dmx_exportbuffer {
        __u32           index;
        __u32           flags;
        __s32           fd;
};

#define DMX_START                _IO('o', 41)
#define DMX_STOP                 _IO('o', 42)
#define DMX_SET_FILTER           _IOW('o', 43, struct dmx_sct_filter_params)
#define DMX_SET_PES_FILTER       _IOW('o', 44, struct dmx_pes_filter_params)
#define DMX_SET_BUFFER_SIZE      _IO('o', 45)
#define DMX_GET_PES_PIDS         _IOR('o', 47, __u16[5])
#define DMX_GET_STC              _IOWR('o', 50, struct dmx_stc)
#define DMX_ADD_PID              _IOW('o', 51, __u16)
#define DMX_REMOVE_PID           _IOW('o', 52, __u16)

#if !defined(__KERNEL__)

/* This is needed for legacy userspace support */
typedef enum dmx_output dmx_output_t;
typedef dmx_input dmx_input_t;
typedef dmx_ts_pes dmx_pes_type_t;
typedef struct dmx_filter dmx_filter_t;

#endif

#define DMX_REQBUFS              _IOWR('o', 60, struct dmx_requestbuffers)
#define DMX_QUERYBUF             _IOWR('o', 61, struct dmx_buffer)
#define DMX_EXPBUF               _IOWR('o', 62, struct dmx_exportbuffer)
#define DMX_QBUF                 _IOWR('o', 63, struct dmx_buffer)
#define DMX_DQBUF                _IOWR('o', 64, struct dmx_buffer)

#endif /* _DVBDMX_H_ */
```

### 8.1.3. ca.h

```
/* SPDX-License-Identifier: LGPL-2.1+ WITH Linux-syscall-note */
/*
 * ca.h
 *
 * Copyright (C) 2000 Ralph  Metzler <ralph@convergence.de>
 *                  & Marcus Metzler <marcus@convergence.de>
 *                    for convergence integrated media GmbH
 */

#ifndef _DVBCA_H_
#define _DVBCA_H_

/**
 * struct ca_slot_info - CA slot interface types and info.
 *
 * @num:        slot number.
 * @type:       slot type.
 * @flags:      flags applicable to the slot.
 *
 * This struct stores the CA slot information.
 *
 * @type can be:
 *
 *      - %CA_CI - CI high level interface;
 *      - %CA_CI_LINK - CI link layer level interface;
 *      - %CA_CI_PHYS - CI physical layer level interface;
 *      - %CA_DESCR - built-in descrambler;
 *      - %CA_SC -simple smart card interface.
 *
 * @flags can be:
 *
 *      - %CA_CI_MODULE_PRESENT - module (or card) inserted;
 *      - %CA_CI_MODULE_READY - module is ready for usage.
 */

struct ca_slot_info {
        int num;
        int type;
#define CA_CI            1
#define CA_CI_LINK       2
#define CA_CI_PHYS       4
#define CA_DESCR         8
#define CA_SC          128

        unsigned int flags;
#define CA_CI_MODULE_PRESENT 1
#define CA_CI_MODULE_READY   2
};

/**
 * struct ca_descr_info - descrambler types and info.
 *
 * @num:        number of available descramblers (keys).
 * @type:       type of supported scrambling system.
 *
 * Identifies the number of descramblers and their type.
 *
 * @type can be:
 *
 *      - %CA_ECD - European Common Descrambler (ECD) hardware;
 *      - %CA_NDS - Videoguard (NDS) hardware;
 *      - %CA_DSS - Distributed Sample Scrambling (DSS) hardware.
 */
struct ca_descr_info {
        unsigned int num;
        unsigned int type;
#define CA_ECD           1
#define CA_NDS           2
#define CA_DSS           4
};

/**
 * struct ca_caps - CA slot interface capabilities.
 *
 * @slot_num:   total number of CA card and module slots.
 * @slot_type:  bitmap with all supported types as defined at
 *              &struct ca_slot_info (e. g. %CA_CI, %CA_CI_LINK, etc).
 * @descr_num:  total number of descrambler slots (keys)
 * @descr_type: bitmap with all supported types as defined at
 *              &struct ca_descr_info (e. g. %CA_ECD, %CA_NDS, etc).
 */
struct ca_caps {
        unsigned int slot_num;
        unsigned int slot_type;
        unsigned int descr_num;
        unsigned int descr_type;
};

/**
 * struct ca_msg - a message to/from a CI-CAM
 *
 * @index:      unused
 * @type:       unused
 * @length:     length of the message
 * @msg:        message
 *
 * This struct carries a message to be send/received from a CI CA module.
 */
struct ca_msg {
        unsigned int index;
        unsigned int type;
        unsigned int length;
        unsigned char msg[256];
};

/**
 * struct ca_descr - CA descrambler control words info
 *
 * @index: CA Descrambler slot
 * @parity: control words parity, where 0 means even and 1 means odd
 * @cw: CA Descrambler control words
 */
struct ca_descr {
        unsigned int index;
        unsigned int parity;
        unsigned char cw[8];
};

#define CA_RESET          _IO('o', 128)
#define CA_GET_CAP        _IOR('o', 129, struct ca_caps)
#define CA_GET_SLOT_INFO  _IOR('o', 130, struct ca_slot_info)
#define CA_GET_DESCR_INFO _IOR('o', 131, struct ca_descr_info)
#define CA_GET_MSG        _IOR('o', 132, struct ca_msg)
#define CA_SEND_MSG       _IOW('o', 133, struct ca_msg)
#define CA_SET_DESCR      _IOW('o', 134, struct ca_descr)

#if !defined(__KERNEL__)

/* This is needed for legacy userspace support */
typedef struct ca_slot_info ca_slot_info_t;
typedef struct ca_descr_info  ca_descr_info_t;
typedef struct ca_caps  ca_caps_t;
typedef struct ca_msg ca_msg_t;
typedef struct ca_descr ca_descr_t;

#endif

#endif
```

### 8.1.4. net.h

```
/* SPDX-License-Identifier: LGPL-2.1+ WITH Linux-syscall-note */
/*
 * net.h
 *
 * Copyright (C) 2000 Marcus Metzler <marcus@convergence.de>
 *                  & Ralph  Metzler <ralph@convergence.de>
 *                    for convergence integrated media GmbH
 */

#ifndef _DVBNET_H_
#define _DVBNET_H_

#include <linux/types.h>

/**
 * struct dvb_net_if - describes a DVB network interface
 *
 * @pid: Packet ID (PID) of the MPEG-TS that contains data
 * @if_num: number of the Digital TV interface.
 * @feedtype: Encapsulation type of the feed.
 *
 * A MPEG-TS stream may contain packet IDs with IP packages on it.
 * This struct describes it, and the type of encoding.
 *
 * @feedtype can be:
 *
 *      - %DVB_NET_FEEDTYPE_MPE for MPE encoding
 *      - %DVB_NET_FEEDTYPE_ULE for ULE encoding.
 */
struct dvb_net_if {
        __u16 pid;
        __u16 if_num;
        __u8  feedtype;
#define DVB_NET_FEEDTYPE_MPE 0  /* multi protocol encapsulation */
#define DVB_NET_FEEDTYPE_ULE 1  /* ultra lightweight encapsulation */
};

#define NET_ADD_IF    _IOWR('o', 52, struct dvb_net_if)
#define NET_REMOVE_IF _IO('o', 53)
#define NET_GET_IF    _IOWR('o', 54, struct dvb_net_if)

/* binary compatibility cruft: */
struct __dvb_net_if_old {
        __u16 pid;
        __u16 if_num;
};
#define __NET_ADD_IF_OLD _IOWR('o', 52, struct __dvb_net_if_old)
#define __NET_GET_IF_OLD _IOWR('o', 54, struct __dvb_net_if_old)

#endif /*_DVBNET_H_*/
```
