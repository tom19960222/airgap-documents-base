---
collection: kernel
version: "6.8"
title: "Net DIM - Generic Network Dynamic Interrupt Moderation"
source_url: https://www.kernel.org/doc/html/v6.8/networking/net_dim.html
fetched_at: 2026-08-21T03:38:59+00:00
---
# [Net DIM - Generic Network Dynamic Interrupt Moderation](net_dim.md#id1)

Author
:   Tal Gilboa <[talgi@mellanox.com](mailto:talgi%40mellanox.com)>

Contents

- [Net DIM - Generic Network Dynamic Interrupt Moderation](net_dim.md#net-dim-generic-network-dynamic-interrupt-moderation)

  - [Assumptions](net_dim.md#assumptions)
  - [Introduction](net_dim.md#introduction)
  - [Net DIM Algorithm](net_dim.md#net-dim-algorithm)
  - [Registering a Network Device to DIM](net_dim.md#registering-a-network-device-to-dim)
  - [Example](net_dim.md#example)
  - [Dynamic Interrupt Moderation (DIM) library API](net_dim.md#dynamic-interrupt-moderation-dim-library-api)

## [Assumptions](net_dim.md#id2)

This document assumes the reader has basic knowledge in network drivers
and in general interrupt moderation.

## [Introduction](net_dim.md#id3)

Dynamic Interrupt Moderation (DIM) (in networking) refers to changing the
interrupt moderation configuration of a channel in order to optimize packet
processing. The mechanism includes an algorithm which decides if and how to
change moderation parameters for a channel, usually by performing an analysis on
runtime data sampled from the system. Net DIM is such a mechanism. In each
iteration of the algorithm, it analyses a given sample of the data, compares it
to the previous sample and if required, it can decide to change some of the
interrupt moderation configuration fields. The data sample is composed of data
bandwidth, the number of packets and the number of events. The time between
samples is also measured. Net DIM compares the current and the previous data and
returns an adjusted interrupt moderation configuration object. In some cases,
the algorithm might decide not to change anything. The configuration fields are
the minimum duration (microseconds) allowed between events and the maximum
number of wanted packets per event. The Net DIM algorithm ascribes importance to
increase bandwidth over reducing interrupt rate.

## [Net DIM Algorithm](net_dim.md#id4)

Each iteration of the Net DIM algorithm follows these steps:

1. Calculates new data sample.
2. Compares it to previous sample.
3. Makes a decision - suggests interrupt moderation configuration fields.
4. Applies a schedule work function, which applies suggested configuration.

The first two steps are straightforward, both the new and the previous data are
supplied by the driver registered to Net DIM. The previous data is the new data
supplied to the previous iteration. The comparison step checks the difference
between the new and previous data and decides on the result of the last step.
A step would result as "better" if bandwidth increases and as "worse" if
bandwidth reduces. If there is no change in bandwidth, the packet rate is
compared in a similar fashion - increase == "better" and decrease == "worse".
In case there is no change in the packet rate as well, the interrupt rate is
compared. Here the algorithm tries to optimize for lower interrupt rate so an
increase in the interrupt rate is considered "worse" and a decrease is
considered "better". Step #2 has an optimization for avoiding false results: it
only considers a difference between samples as valid if it is greater than a
certain percentage. Also, since Net DIM does not measure anything by itself, it
assumes the data provided by the driver is valid.

Step #3 decides on the suggested configuration based on the result from step #2
and the internal state of the algorithm. The states reflect the "direction" of
the algorithm: is it going left (reducing moderation), right (increasing
moderation) or standing still. Another optimization is that if a decision
to stay still is made multiple times, the interval between iterations of the
algorithm would increase in order to reduce calculation overhead. Also, after
"parking" on one of the most left or most right decisions, the algorithm may
decide to verify this decision by taking a step in the other direction. This is
done in order to avoid getting stuck in a "deep sleep" scenario. Once a
decision is made, an interrupt moderation configuration is selected from
the predefined profiles.

The last step is to notify the registered driver that it should apply the
suggested configuration. This is done by scheduling a work function, defined by
the Net DIM API and provided by the registered driver.

As you can see, Net DIM itself does not actively interact with the system. It
would have trouble making the correct decisions if the wrong data is supplied to
it and it would be useless if the work function would not apply the suggested
configuration. This does, however, allow the registered driver some room for
manoeuvre as it may provide partial data or ignore the algorithm suggestion
under some conditions.

## [Registering a Network Device to DIM](net_dim.md#id5)

Net DIM API exposes the main function [`net_dim()`](net_dim.md#c.net_dim "net_dim").
This function is the entry point to the Net
DIM algorithm and has to be called every time the driver would like to check if
it should change interrupt moderation parameters. The driver should provide two
data structures: [`struct dim`](net_dim.md#c.dim "dim") and
[`struct dim_sample`](net_dim.md#c.dim_sample "dim_sample"). [`struct dim`](net_dim.md#c.dim "dim")
describes the state of DIM for a specific object (RX queue, TX queue,
other queues, etc.). This includes the current selected profile, previous data
samples, the callback function provided by the driver and more.
[`struct dim_sample`](net_dim.md#c.dim_sample "dim_sample") describes a data sample,
which will be compared to the data sample stored in [`struct dim`](net_dim.md#c.dim "dim")
in order to decide on the algorithm's next
step. The sample should include bytes, packets and interrupts, measured by
the driver.

In order to use Net DIM from a networking driver, the driver needs to call the
main [`net_dim()`](net_dim.md#c.net_dim "net_dim") function. The recommended method is to call [`net_dim()`](net_dim.md#c.net_dim "net_dim") on each
interrupt. Since Net DIM has a built-in moderation and it might decide to skip
iterations under certain conditions, there is no need to moderate the [`net_dim()`](net_dim.md#c.net_dim "net_dim")
calls as well. As mentioned above, the driver needs to provide an object of type
[`struct dim`](net_dim.md#c.dim "dim") to the [`net_dim()`](net_dim.md#c.net_dim "net_dim") function call. It is advised for
each entity using Net DIM to hold a [`struct dim`](net_dim.md#c.dim "dim") as part of its
data structure and use it as the main Net DIM API object.
The [`struct dim_sample`](net_dim.md#c.dim_sample "dim_sample") should hold the latest
bytes, packets and interrupts count. No need to perform any calculations, just
include the raw data.

The [`net_dim()`](net_dim.md#c.net_dim "net_dim") call itself does not return anything. Instead Net DIM relies on
the driver to provide a callback function, which is called when the algorithm
decides to make a change in the interrupt moderation parameters. This callback
will be scheduled and run in a separate thread in order not to add overhead to
the data flow. After the work is done, Net DIM algorithm needs to be set to
the proper state in order to move to the next iteration.

## [Example](net_dim.md#id6)

The following code demonstrates how to register a driver to Net DIM. The actual
usage is not complete but it should make the outline of the usage clear.

```c
#include <linux/dim.h>

/* Callback for net DIM to schedule on a decision to change moderation */
void my_driver_do_dim_work(struct work_struct *work)
{
      /* Get struct dim from struct work_struct */
      struct dim *dim = container_of(work, struct dim,
                                     work);
      /* Do interrupt moderation related stuff */
      ...

      /* Signal net DIM work is done and it should move to next iteration */
      dim->state = DIM_START_MEASURE;
}

/* My driver's interrupt handler */
int my_driver_handle_interrupt(struct my_driver_entity *my_entity, ...)
{
      ...
      /* A struct to hold current measured data */
      struct dim_sample dim_sample;
      ...
      /* Initiate data sample struct with current data */
      dim_update_sample(my_entity->events,
                        my_entity->packets,
                        my_entity->bytes,
                        &dim_sample);
      /* Call net DIM */
      net_dim(&my_entity->dim, dim_sample);
      ...
}

/* My entity's initialization function (my_entity was already allocated) */
int my_driver_init_my_entity(struct my_driver_entity *my_entity, ...)
{
      ...
      /* Initiate struct work_struct with my driver's callback function */
      INIT_WORK(&my_entity->dim.work, my_driver_do_dim_work);
      ...
}
```

## [Dynamic Interrupt Moderation (DIM) library API](net_dim.md#id7)

struct dim_cq_moder
:   Structure for CQ moderation values. Used for communications between DIM and its consumer.

**Definition**:

```
struct dim_cq_moder {
    u16 usec;
    u16 pkts;
    u16 comps;
    u8 cq_period_mode;
};
```

**Members**

`usec`
:   CQ timer suggestion (by DIM)

`pkts`
:   CQ packet counter suggestion (by DIM)

`comps`
:   Completion counter

`cq_period_mode`
:   CQ period count mode (from CQE/EQE)

struct dim_sample
:   Structure for DIM sample data. Used for communications between DIM and its consumer.

**Definition**:

```
struct dim_sample {
    ktime_t time;
    u32 pkt_ctr;
    u32 byte_ctr;
    u16 event_ctr;
    u32 comp_ctr;
};
```

**Members**

`time`
:   Sample timestamp

`pkt_ctr`
:   Number of packets

`byte_ctr`
:   Number of bytes

`event_ctr`
:   Number of events

`comp_ctr`
:   Current completion counter

struct dim_stats
:   Structure for DIM stats. Used for holding current measured rates.

**Definition**:

```
struct dim_stats {
    int ppms;
    int bpms;
    int epms;
    int cpms;
    int cpe_ratio;
};
```

**Members**

`ppms`
:   Packets per msec

`bpms`
:   Bytes per msec

`epms`
:   Events per msec

`cpms`
:   Completions per msec

`cpe_ratio`
:   Ratio of completions to events

struct dim
:   Main structure for dynamic interrupt moderation (DIM). Used for holding all information about a specific DIM instance.

**Definition**:

```
struct dim {
    u8 state;
    struct dim_stats prev_stats;
    struct dim_sample start_sample;
    struct dim_sample measuring_sample;
    struct work_struct work;
    void *priv;
    u8 profile_ix;
    u8 mode;
    u8 tune_state;
    u8 steps_right;
    u8 steps_left;
    u8 tired;
};
```

**Members**

`state`
:   Algorithm state (see below)

`prev_stats`
:   Measured rates from previous iteration (for comparison)

`start_sample`
:   Sampled data at start of current iteration

`measuring_sample`
:   A [`dim_sample`](net_dim.md#c.dim_sample "dim_sample") that is used to update the current events

`work`
:   Work to perform on action required

`priv`
:   A pointer to the struct that points to dim

`profile_ix`
:   Current moderation profile

`mode`
:   CQ period count mode

`tune_state`
:   Algorithm tuning state (see below)

`steps_right`
:   Number of steps taken towards higher moderation

`steps_left`
:   Number of steps taken towards lower moderation

`tired`
:   Parking depth counter

enum dim_cq_period_mode
:   Modes for CQ period count

**Constants**

`DIM_CQ_PERIOD_MODE_START_FROM_EQE`
:   Start counting from EQE

`DIM_CQ_PERIOD_MODE_START_FROM_CQE`
:   Start counting from CQE (implies timer reset)

`DIM_CQ_PERIOD_NUM_MODES`
:   Number of modes

enum dim_state
:   DIM algorithm states

**Constants**

`DIM_START_MEASURE`
:   This is the first iteration (also after applying a new profile)

`DIM_MEASURE_IN_PROGRESS`
:   Algorithm is already in progress - check if
    need to perform an action

`DIM_APPLY_NEW_PROFILE`
:   DIM consumer is currently applying a profile - no need to measure

**Description**

These will determine if the algorithm is in a valid state to start an iteration.

enum dim_tune_state
:   DIM algorithm tune states

**Constants**

`DIM_PARKING_ON_TOP`
:   Algorithm found a local top point - exit on significant difference

`DIM_PARKING_TIRED`
:   Algorithm found a deep top point - don't exit if tired > 0

`DIM_GOING_RIGHT`
:   Algorithm is currently trying higher moderation levels

`DIM_GOING_LEFT`
:   Algorithm is currently trying lower moderation levels

**Description**

These will determine which action the algorithm should perform.

enum dim_stats_state
:   DIM algorithm statistics states

**Constants**

`DIM_STATS_WORSE`
:   Current iteration shows worse performance than before

`DIM_STATS_SAME`
:   Current iteration shows same performance than before

`DIM_STATS_BETTER`
:   Current iteration shows better performance than before

**Description**

These will determine the verdict of current iteration.

enum dim_step_result
:   DIM algorithm step results

**Constants**

`DIM_STEPPED`
:   Performed a regular step

`DIM_TOO_TIRED`
:   Same kind of step was done multiple times - should go to
    tired parking

`DIM_ON_EDGE`
:   Stepped to the most left/right profile

**Description**

These describe the result of a step.

bool dim_on_top(struct [dim](net_dim.md#c.dim_on_top "dim") \*dim)
:   check if current state is a good place to stop (top location)

**Parameters**

`struct dim *dim`
:   DIM context

**Description**

Check if current profile is a good place to park at.
This will result in reducing the DIM checks frequency as we assume we
shouldn't probably change profiles, unless traffic pattern wasn't changed.

void dim_turn(struct [dim](net_dim.md#c.dim_turn "dim") \*dim)
:   change profile altering direction

**Parameters**

`struct dim *dim`
:   DIM context

**Description**

Go left if we were going right and vice-versa.
Do nothing if currently parking.

void dim_park_on_top(struct [dim](net_dim.md#c.dim_park_on_top "dim") \*dim)
:   enter a parking state on a top location

**Parameters**

`struct dim *dim`
:   DIM context

**Description**

Enter parking state.
Clear all movement history.

void dim_park_tired(struct [dim](net_dim.md#c.dim_park_tired "dim") \*dim)
:   enter a tired parking state

**Parameters**

`struct dim *dim`
:   DIM context

**Description**

Enter parking state.
Clear all movement history and cause DIM checks frequency to reduce.

bool dim_calc_stats(struct [dim_sample](net_dim.md#c.dim_sample "dim_sample") \*start, struct [dim_sample](net_dim.md#c.dim_sample "dim_sample") \*end, struct [dim_stats](net_dim.md#c.dim_stats "dim_stats") \*curr_stats)
:   calculate the difference between two samples

**Parameters**

`struct dim_sample *start`
:   start sample

`struct dim_sample *end`
:   end sample

`struct dim_stats *curr_stats`
:   delta between samples

**Description**

Calculate the delta between two samples (in data rates).
Takes into consideration counter wrap-around.
Returned boolean indicates whether curr_stats are reliable.

void dim_update_sample(u16 event_ctr, u64 packets, u64 bytes, struct [dim_sample](net_dim.md#c.dim_sample "dim_sample") \*s)
:   set a sample's fields with given values

**Parameters**

`u16 event_ctr`
:   number of events to set

`u64 packets`
:   number of packets to set

`u64 bytes`
:   number of bytes to set

`struct dim_sample *s`
:   DIM sample

void dim_update_sample_with_comps(u16 event_ctr, u64 packets, u64 bytes, u64 comps, struct [dim_sample](net_dim.md#c.dim_sample "dim_sample") \*s)
:   set a sample's fields with given values including the completion parameter

**Parameters**

`u16 event_ctr`
:   number of events to set

`u64 packets`
:   number of packets to set

`u64 bytes`
:   number of bytes to set

`u64 comps`
:   number of completions to set

`struct dim_sample *s`
:   DIM sample

struct [dim_cq_moder](net_dim.md#c.dim_cq_moder "dim_cq_moder") net_dim_get_rx_moderation(u8 cq_period_mode, int ix)
:   provide a CQ moderation object for the given RX profile

**Parameters**

`u8 cq_period_mode`
:   CQ period mode

`int ix`
:   Profile index

struct [dim_cq_moder](net_dim.md#c.dim_cq_moder "dim_cq_moder") net_dim_get_def_rx_moderation(u8 cq_period_mode)
:   provide the default RX moderation

**Parameters**

`u8 cq_period_mode`
:   CQ period mode

struct [dim_cq_moder](net_dim.md#c.dim_cq_moder "dim_cq_moder") net_dim_get_tx_moderation(u8 cq_period_mode, int ix)
:   provide a CQ moderation object for the given TX profile

**Parameters**

`u8 cq_period_mode`
:   CQ period mode

`int ix`
:   Profile index

struct [dim_cq_moder](net_dim.md#c.dim_cq_moder "dim_cq_moder") net_dim_get_def_tx_moderation(u8 cq_period_mode)
:   provide the default TX moderation

**Parameters**

`u8 cq_period_mode`
:   CQ period mode

void net_dim(struct [dim](net_dim.md#c.net_dim "dim") \*dim, struct [dim_sample](net_dim.md#c.dim_sample "dim_sample") end_sample)
:   main DIM algorithm entry point

**Parameters**

`struct dim *dim`
:   DIM instance information

`struct dim_sample end_sample`
:   Current data measurement

**Description**

Called by the consumer.
This is the main logic of the algorithm, where data is processed in order
to decide on next required action.

void rdma_dim(struct [dim](net_dim.md#c.rdma_dim "dim") \*dim, u64 completions)
:   Runs the adaptive moderation.

**Parameters**

`struct dim *dim`
:   The moderation struct.

`u64 completions`
:   The number of completions collected in this round.

**Description**

Each call to rdma_dim takes the latest amount of completions that
have been collected and counts them as a new event.
Once enough events have been collected the algorithm decides a new
moderation level.
