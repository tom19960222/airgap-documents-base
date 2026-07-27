---
collection: ceph
version: "19.2.2"
title: "Diskprediction Module"
source_url: https://docs.ceph.com/en/squid/mgr/diskprediction/
fetched_at: 2026-07-27T16:40:50+00:00
---
# Diskprediction Module

The `diskprediction` module leverages Ceph device health checks to collect
disk health metrics and uses the internal predictor module to produce disk
failure predictions and returns them back to Ceph. It requires no external
server for data analysis and the outputting of results. Its internal
predictor’s accuracy is around 70%.

## Enabling

Run the following command to enable the `diskprediction_local` module in the
Ceph environment:

```
ceph mgr module enable diskprediction_local
```

Run the following command to enable the local predictor:

```
ceph config set global device_failure_prediction_mode local
```

Run the following command to disable prediction:

```
ceph config set global device_failure_prediction_mode none
```

`diskprediction_local` requires at least six datasets of device health
metrics to make prediction of the devices’ life expectancy. And these health
metrics are collected only if health monitoring is [enabled](../../rados/operations/devices/index.md#enabling-monitoring).

Run the following command to retrieve the life expectancy of a given device:

```
ceph device predict-life-expectancy <device id>
```

## Configuration

The module performs the prediction on a daily basis by default. Adjust this
interval by running a command of the following form:

```
ceph config set mgr mgr/diskprediction_local/predict_interval <interval-in-seconds>
```

## Debugging

To debug the DiskPrediction module mapping to Ceph logging level,
use the following command.

```
[mgr]

    debug mgr = 20
```

With logging set to `debug` for the Manager, the module will print logging
messages with the prefix `mgr[diskprediction]`. This facilitates filtering.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
