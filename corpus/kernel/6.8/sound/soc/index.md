---
collection: kernel
version: "6.8"
title: "ALSA SoC Layer"
source_url: https://www.kernel.org/doc/html/v6.8/sound/soc/index.html
fetched_at: 2026-08-21T03:47:39+00:00
---
# ALSA SoC Layer

The documentation is spilt into the following sections:-

- [ALSA SoC Layer Overview](overview.md)
  - [ASoC Design](overview.md#asoc-design)
- [ASoC Codec Class Driver](codec.md)
  - [ASoC Codec driver breakdown](codec.md#asoc-codec-driver-breakdown)
- [ASoC Digital Audio Interface (DAI)](dai.md)
  - [AC97](dai.md#ac97)
  - [I2S](dai.md#i2s)
  - [PCM](dai.md#pcm)
- [Dynamic Audio Power Management for Portable Devices](dapm.md)
  - [Description](dapm.md#description)
  - [DAPM Widgets](dapm.md#dapm-widgets)
  - [Codec/DSP Widget Interconnections](dapm.md#codec-dsp-widget-interconnections)
  - [Endpoint Widgets](dapm.md#endpoint-widgets)
  - [DAPM Widget Events](dapm.md#dapm-widget-events)
- [ASoC Platform Driver](platform.md)
  - [Audio DMA](platform.md#audio-dma)
  - [SoC DAI Drivers](platform.md#soc-dai-drivers)
  - [SoC DSP Drivers](platform.md#soc-dsp-drivers)
- [ASoC Machine Driver](machine.md)
  - [probe()/remove()](machine.md#probe-remove)
  - [suspend()/resume()](machine.md#suspend-resume)
  - [Machine DAI Configuration](machine.md#machine-dai-configuration)
  - [Machine Power Map](machine.md#machine-power-map)
  - [Machine Controls](machine.md#machine-controls)
- [Audio Pops and Clicks](pops-clicks.md)
  - [Minimising Playback Pops and Clicks](pops-clicks.md#minimising-playback-pops-and-clicks)
  - [Minimising Capture Pops and Clicks](pops-clicks.md#minimising-capture-pops-and-clicks)
  - [Zipper Noise](pops-clicks.md#zipper-noise)
- [Audio Clocking](clocking.md)
  - [Master Clock](clocking.md#master-clock)
  - [DAI Clocks](clocking.md#dai-clocks)
- [ASoC jack detection](jack.md)
  - [The jack - struct snd_soc_jack](jack.md#the-jack-struct-snd-soc-jack)
  - [snd_soc_jack_pin](jack.md#snd-soc-jack-pin)
  - [Jack detection methods](jack.md#jack-detection-methods)
  - [Machine drivers](jack.md#machine-drivers)
- [Dynamic PCM](dpcm.md)
  - [Description](dpcm.md#description)
  - [DPCM machine driver](dpcm.md#dpcm-machine-driver)
  - [Writing a DPCM DSP driver](dpcm.md#writing-a-dpcm-dsp-driver)
  - [Hostless PCM streams](dpcm.md#hostless-pcm-streams)
- [Creating codec to codec dai link for ALSA dapm](codec-to-codec.md)
