---
collection: kernel
version: "6.8"
title: "Sequence counters and sequential locks"
source_url: https://www.kernel.org/doc/html/v6.8/locking/seqlock.html
fetched_at: 2026-08-21T03:33:17+00:00
---
# Sequence counters and sequential locks

## Introduction

Sequence counters are a reader-writer consistency mechanism with
lockless readers (read-only retry loops), and no writer starvation. They
are used for data that's rarely written to (e.g. system time), where the
reader wants a consistent set of information and is willing to retry if
that information changes.

A data set is consistent when the sequence count at the beginning of the
read side critical section is even and the same sequence count value is
read again at the end of the critical section. The data in the set must
be copied out inside the read side critical section. If the sequence
count has changed between the start and the end of the critical section,
the reader must retry.

Writers increment the sequence count at the start and the end of their
critical section. After starting the critical section the sequence count
is odd and indicates to the readers that an update is in progress. At
the end of the write side critical section the sequence count becomes
even again which lets readers make progress.

A sequence counter write side critical section must never be preempted
or interrupted by read side sections. Otherwise the reader will spin for
the entire scheduler tick due to the odd sequence count value and the
interrupted writer. If that reader belongs to a real-time scheduling
class, it can spin forever and the kernel will livelock.

This mechanism cannot be used if the protected data contains pointers,
as the writer can invalidate a pointer that the reader is following.

## Sequence counters (`seqcount_t`)

This is the raw counting mechanism, which does not protect against
multiple writers. Write side critical sections must thus be serialized
by an external lock.

If the write serialization primitive is not implicitly disabling
preemption, preemption must be explicitly disabled before entering the
write side section. If the read section can be invoked from hardirq or
softirq contexts, interrupts or bottom halves must also be respectively
disabled before entering the write section.

If it's desired to automatically handle the sequence counter
requirements of writer serialization and non-preemptibility, use
[Sequential locks (seqlock_t)](seqlock.md#seqlock-t) instead.

Initialization:

```
/* dynamic */
seqcount_t foo_seqcount;
seqcount_init(&foo_seqcount);

/* static */
static seqcount_t foo_seqcount = SEQCNT_ZERO(foo_seqcount);

/* C99 struct init */
struct {
        .seq   = SEQCNT_ZERO(foo.seq),
} foo;
```

Write path:

```
/* Serialized context with disabled preemption */

write_seqcount_begin(&foo_seqcount);

/* ... [[write-side critical section]] ... */

write_seqcount_end(&foo_seqcount);
```

Read path:

```
do {
        seq = read_seqcount_begin(&foo_seqcount);

        /* ... [[read-side critical section]] ... */

} while (read_seqcount_retry(&foo_seqcount, seq));
```

### Sequence counters with associated locks (`seqcount_LOCKNAME_t`)

As discussed at [Sequence counters (seqcount_t)](seqlock.md#seqcount-t), sequence count write side critical
sections must be serialized and non-preemptible. This variant of
sequence counters associate the lock used for writer serialization at
initialization time, which enables lockdep to validate that the write
side critical sections are properly serialized.

This lock association is a NOOP if lockdep is disabled and has neither
storage nor runtime overhead. If lockdep is enabled, the lock pointer is
stored in struct seqcount and lockdep's "lock is held" assertions are
injected at the beginning of the write side critical section to validate
that it is properly protected.

For lock types which do not implicitly disable preemption, preemption
protection is enforced in the write side function.

The following sequence counters with associated locks are defined:

> - `seqcount_spinlock_t`
> - `seqcount_raw_spinlock_t`
> - `seqcount_rwlock_t`
> - `seqcount_mutex_t`
> - `seqcount_ww_mutex_t`

The sequence counter read and write APIs can take either a plain
seqcount_t or any of the seqcount_LOCKNAME_t variants above.

Initialization (replace "LOCKNAME" with one of the supported locks):

```
/* dynamic */
seqcount_LOCKNAME_t foo_seqcount;
seqcount_LOCKNAME_init(&foo_seqcount, &lock);

/* static */
static seqcount_LOCKNAME_t foo_seqcount =
        SEQCNT_LOCKNAME_ZERO(foo_seqcount, &lock);

/* C99 struct init */
struct {
        .seq   = SEQCNT_LOCKNAME_ZERO(foo.seq, &lock),
} foo;
```

Write path: same as in [Sequence counters (seqcount_t)](seqlock.md#seqcount-t), while running from a context
with the associated write serialization lock acquired.

Read path: same as in [Sequence counters (seqcount_t)](seqlock.md#seqcount-t).

### Latch sequence counters (`seqcount_latch_t`)

Latch sequence counters are a multiversion concurrency control mechanism
where the embedded seqcount_t counter even/odd value is used to switch
between two copies of protected data. This allows the sequence counter
read path to safely interrupt its own write side critical section.

Use seqcount_latch_t when the write side sections cannot be protected
from interruption by readers. This is typically the case when the read
side can be invoked from NMI handlers.

Check [`raw_write_seqcount_latch()`](seqlock.md#c.raw_write_seqcount_latch "raw_write_seqcount_latch") for more information.

## Sequential locks (`seqlock_t`)

This contains the [Sequence counters (seqcount_t)](seqlock.md#seqcount-t) mechanism earlier discussed, plus an
embedded spinlock for writer serialization and non-preemptibility.

If the read side section can be invoked from hardirq or softirq context,
use the write side function variants which disable interrupts or bottom
halves respectively.

Initialization:

```
/* dynamic */
seqlock_t foo_seqlock;
seqlock_init(&foo_seqlock);

/* static */
static DEFINE_SEQLOCK(foo_seqlock);

/* C99 struct init */
struct {
        .seql   = __SEQLOCK_UNLOCKED(foo.seql)
} foo;
```

Write path:

```
write_seqlock(&foo_seqlock);

/* ... [[write-side critical section]] ... */

write_sequnlock(&foo_seqlock);
```

Read path, three categories:

1. Normal Sequence readers which never block a writer but they must
   retry if a writer is in progress by detecting change in the sequence
   number. Writers do not wait for a sequence reader:

   ```
   do {
           seq = read_seqbegin(&foo_seqlock);

           /* ... [[read-side critical section]] ... */

   } while (read_seqretry(&foo_seqlock, seq));
   ```
2. Locking readers which will wait if a writer or another locking reader
   is in progress. A locking reader in progress will also block a writer
   from entering its critical section. This read lock is
   exclusive. Unlike rwlock_t, only one locking reader can acquire it:

   ```
   read_seqlock_excl(&foo_seqlock);

   /* ... [[read-side critical section]] ... */

   read_sequnlock_excl(&foo_seqlock);
   ```
3. Conditional lockless reader (as in 1), or locking reader (as in 2),
   according to a passed marker. This is used to avoid lockless readers
   starvation (too much retry loops) in case of a sharp spike in write
   activity. First, a lockless read is tried (even marker passed). If
   that trial fails (odd sequence counter is returned, which is used as
   the next iteration marker), the lockless read is transformed to a
   full locking read and no retry loop is necessary:

   ```
   /* marker; even initialization */
   int seq = 0;
   do {
           read_seqbegin_or_lock(&foo_seqlock, &seq);

           /* ... [[read-side critical section]] ... */

   } while (need_seqretry(&foo_seqlock, seq));
   done_seqretry(&foo_seqlock, seq);
   ```

## API documentation

seqcount_init

`seqcount_init (s)`

> runtime initializer for seqcount_t

**Parameters**

`s`
:   Pointer to the seqcount_t instance

SEQCNT_ZERO

`SEQCNT_ZERO (name)`

> static initializer for seqcount_t

**Parameters**

`name`
:   Name of the seqcount_t instance

__read_seqcount_begin

`__read_seqcount_begin (s)`

> begin a seqcount_t read section w/o barrier

**Parameters**

`s`
:   Pointer to seqcount_t or any of the seqcount_LOCKNAME_t variants

**Description**

__read_seqcount_begin is like read_seqcount_begin, but has no smp_rmb()
barrier. Callers should ensure that smp_rmb() or equivalent ordering is
provided before actually loading any of the variables that are to be
protected in this critical section.

Use carefully, only in critical code, and comment how the barrier is
provided.

**Return**

count to be passed to [`read_seqcount_retry()`](seqlock.md#c.read_seqcount_retry "read_seqcount_retry")

raw_read_seqcount_begin

`raw_read_seqcount_begin (s)`

> begin a seqcount_t read section w/o lockdep

**Parameters**

`s`
:   Pointer to seqcount_t or any of the seqcount_LOCKNAME_t variants

**Return**

count to be passed to [`read_seqcount_retry()`](seqlock.md#c.read_seqcount_retry "read_seqcount_retry")

read_seqcount_begin

`read_seqcount_begin (s)`

> begin a seqcount_t read critical section

**Parameters**

`s`
:   Pointer to seqcount_t or any of the seqcount_LOCKNAME_t variants

**Return**

count to be passed to [`read_seqcount_retry()`](seqlock.md#c.read_seqcount_retry "read_seqcount_retry")

raw_read_seqcount

`raw_read_seqcount (s)`

> read the raw seqcount_t counter value

**Parameters**

`s`
:   Pointer to seqcount_t or any of the seqcount_LOCKNAME_t variants

**Description**

raw_read_seqcount opens a read critical section of the given
seqcount_t, without any lockdep checking, and without checking or
masking the sequence counter LSB. Calling code is responsible for
handling that.

**Return**

count to be passed to [`read_seqcount_retry()`](seqlock.md#c.read_seqcount_retry "read_seqcount_retry")

raw_seqcount_begin

`raw_seqcount_begin (s)`

> begin a seqcount_t read critical section w/o lockdep and w/o counter stabilization

**Parameters**

`s`
:   Pointer to seqcount_t or any of the seqcount_LOCKNAME_t variants

**Description**

raw_seqcount_begin opens a read critical section of the given
seqcount_t. Unlike [`read_seqcount_begin()`](seqlock.md#c.read_seqcount_begin "read_seqcount_begin"), this function will not wait
for the count to stabilize. If a writer is active when it begins, it
will fail the [`read_seqcount_retry()`](seqlock.md#c.read_seqcount_retry "read_seqcount_retry") at the end of the read critical
section instead of stabilizing at the beginning of it.

Use this only in special kernel hot paths where the read section is
small and has a high probability of success through other external
means. It will save a single branching instruction.

**Return**

count to be passed to [`read_seqcount_retry()`](seqlock.md#c.read_seqcount_retry "read_seqcount_retry")

__read_seqcount_retry

`__read_seqcount_retry (s, start)`

> end a seqcount_t read section w/o barrier

**Parameters**

`s`
:   Pointer to seqcount_t or any of the seqcount_LOCKNAME_t variants

`start`
:   count, from [`read_seqcount_begin()`](seqlock.md#c.read_seqcount_begin "read_seqcount_begin")

**Description**

__read_seqcount_retry is like read_seqcount_retry, but has no smp_rmb()
barrier. Callers should ensure that smp_rmb() or equivalent ordering is
provided before actually loading any of the variables that are to be
protected in this critical section.

Use carefully, only in critical code, and comment how the barrier is
provided.

**Return**

true if a read section retry is required, else false

read_seqcount_retry

`read_seqcount_retry (s, start)`

> end a seqcount_t read critical section

**Parameters**

`s`
:   Pointer to seqcount_t or any of the seqcount_LOCKNAME_t variants

`start`
:   count, from [`read_seqcount_begin()`](seqlock.md#c.read_seqcount_begin "read_seqcount_begin")

**Description**

read_seqcount_retry closes the read critical section of given
seqcount_t. If the critical section was invalid, it must be ignored
(and typically retried).

**Return**

true if a read section retry is required, else false

raw_write_seqcount_begin

`raw_write_seqcount_begin (s)`

> start a seqcount_t write section w/o lockdep

**Parameters**

`s`
:   Pointer to seqcount_t or any of the seqcount_LOCKNAME_t variants

**Context**

check [`write_seqcount_begin()`](seqlock.md#c.write_seqcount_begin "write_seqcount_begin")

raw_write_seqcount_end

`raw_write_seqcount_end (s)`

> end a seqcount_t write section w/o lockdep

**Parameters**

`s`
:   Pointer to seqcount_t or any of the seqcount_LOCKNAME_t variants

**Context**

check [`write_seqcount_end()`](seqlock.md#c.write_seqcount_end "write_seqcount_end")

write_seqcount_begin_nested

`write_seqcount_begin_nested (s, subclass)`

> start a seqcount_t write section with custom lockdep nesting level

**Parameters**

`s`
:   Pointer to seqcount_t or any of the seqcount_LOCKNAME_t variants

`subclass`
:   lockdep nesting level

**Description**

See [Runtime locking correctness validator](lockdep-design.md)

**Context**

check [`write_seqcount_begin()`](seqlock.md#c.write_seqcount_begin "write_seqcount_begin")

write_seqcount_begin

`write_seqcount_begin (s)`

> start a seqcount_t write side critical section

**Parameters**

`s`
:   Pointer to seqcount_t or any of the seqcount_LOCKNAME_t variants

**Context**

sequence counter write side sections must be serialized and
non-preemptible. Preemption will be automatically disabled if and
only if the seqcount write serialization lock is associated, and
preemptible. If readers can be invoked from hardirq or softirq
context, interrupts or bottom halves must be respectively disabled.

write_seqcount_end

`write_seqcount_end (s)`

> end a seqcount_t write side critical section

**Parameters**

`s`
:   Pointer to seqcount_t or any of the seqcount_LOCKNAME_t variants

**Context**

Preemption will be automatically re-enabled if and only if
the seqcount write serialization lock is associated, and preemptible.

raw_write_seqcount_barrier

`raw_write_seqcount_barrier (s)`

> do a seqcount_t write barrier

**Parameters**

`s`
:   Pointer to seqcount_t or any of the seqcount_LOCKNAME_t variants

**Description**

This can be used to provide an ordering guarantee instead of the usual
consistency guarantee. It is one wmb cheaper, because it can collapse
the two back-to-back wmb()s.

Note that writes surrounding the barrier should be declared atomic (e.g.
via WRITE_ONCE): a) to ensure the writes become visible to other threads
atomically, avoiding compiler optimizations; b) to document which writes are
meant to propagate to the reader critical section. This is necessary because
neither writes before nor after the barrier are enclosed in a seq-writer
critical section that would ensure readers are aware of ongoing writes:

```
seqcount_t seq;
bool X = true, Y = false;

void read(void)
{
        bool x, y;

        do {
                int s = read_seqcount_begin(&seq);

                x = X; y = Y;

        } while (read_seqcount_retry(&seq, s));

        BUG_ON(!x && !y);
}

void write(void)
{
        WRITE_ONCE(Y, true);

        raw_write_seqcount_barrier(seq);

        WRITE_ONCE(X, false);
}
```

write_seqcount_invalidate

`write_seqcount_invalidate (s)`

> invalidate in-progress seqcount_t read side operations

**Parameters**

`s`
:   Pointer to seqcount_t or any of the seqcount_LOCKNAME_t variants

**Description**

After write_seqcount_invalidate, no seqcount_t read side operations
will complete successfully and see data older than this.

SEQCNT_LATCH_ZERO

`SEQCNT_LATCH_ZERO (seq_name)`

> static initializer for seqcount_latch_t

**Parameters**

`seq_name`
:   Name of the seqcount_latch_t instance

seqcount_latch_init

`seqcount_latch_init (s)`

> runtime initializer for seqcount_latch_t

**Parameters**

`s`
:   Pointer to the seqcount_latch_t instance

unsigned raw_read_seqcount_latch(const seqcount_latch_t \*s)
:   pick even/odd latch data copy

**Parameters**

`const seqcount_latch_t *s`
:   Pointer to seqcount_latch_t

**Description**

See [`raw_write_seqcount_latch()`](seqlock.md#c.raw_write_seqcount_latch "raw_write_seqcount_latch") for details and a full reader/writer
usage example.

**Return**

sequence counter raw value. Use the lowest bit as an index for
picking which data copy to read. The full counter must then be checked
with [`raw_read_seqcount_latch_retry()`](seqlock.md#c.raw_read_seqcount_latch_retry "raw_read_seqcount_latch_retry").

int raw_read_seqcount_latch_retry(const seqcount_latch_t \*s, unsigned start)
:   end a seqcount_latch_t read section

**Parameters**

`const seqcount_latch_t *s`
:   Pointer to seqcount_latch_t

`unsigned start`
:   count, from [`raw_read_seqcount_latch()`](seqlock.md#c.raw_read_seqcount_latch "raw_read_seqcount_latch")

**Return**

true if a read section retry is required, else false

void raw_write_seqcount_latch(seqcount_latch_t \*s)
:   redirect latch readers to even/odd copy

**Parameters**

`seqcount_latch_t *s`
:   Pointer to seqcount_latch_t

**Description**

The latch technique is a multiversion concurrency control method that allows
queries during non-atomic modifications. If you can guarantee queries never
interrupt the modification -- e.g. the concurrency is strictly between CPUs
-- you most likely do not need this.

Where the traditional RCU/lockless data structures rely on atomic
modifications to ensure queries observe either the old or the new state the
latch allows the same for non-atomic updates. The trade-off is doubling the
cost of storage; we have to maintain two copies of the entire data
structure.

Very simply put: we first modify one copy and then the other. This ensures
there is always one copy in a stable state, ready to give us an answer.

The basic form is a data structure like:

```
struct latch_struct {
        seqcount_latch_t        seq;
        struct data_struct      data[2];
};
```

Where a modification, which is assumed to be externally serialized, does the
following:

```
void latch_modify(struct latch_struct *latch, ...)
{
        smp_wmb();      // Ensure that the last data[1] update is visible
        latch->seq.sequence++;
        smp_wmb();      // Ensure that the seqcount update is visible

        modify(latch->data[0], ...);

        smp_wmb();      // Ensure that the data[0] update is visible
        latch->seq.sequence++;
        smp_wmb();      // Ensure that the seqcount update is visible

        modify(latch->data[1], ...);
}
```

The query will have a form like:

```
struct entry *latch_query(struct latch_struct *latch, ...)
{
        struct entry *entry;
        unsigned seq, idx;

        do {
                seq = raw_read_seqcount_latch(&latch->seq);

                idx = seq & 0x01;
                entry = data_query(latch->data[idx], ...);

        // This includes needed smp_rmb()
        } while (raw_read_seqcount_latch_retry(&latch->seq, seq));

        return entry;
}
```

So during the modification, queries are first redirected to data[1]. Then we
modify data[0]. When that is complete, we redirect queries back to data[0]
and we can modify data[1].

NOTE2:

> When data is a dynamic data structure; one should use regular RCU
> patterns to manage the lifetimes of the objects within.

**NOTE**

> The non-requirement for atomic modifications does _NOT_ include
> the publishing of new entries in the case where data is a dynamic
> data structure.
>
> An iteration might start in data[0] and get suspended long enough
> to miss an entire modification sequence, once it resumes it might
> observe the new entry.

seqlock_init

`seqlock_init (sl)`

> dynamic initializer for seqlock_t

**Parameters**

`sl`
:   Pointer to the seqlock_t instance

DEFINE_SEQLOCK

`DEFINE_SEQLOCK (sl)`

> Define a statically allocated seqlock_t

**Parameters**

`sl`
:   Name of the seqlock_t instance

unsigned read_seqbegin(const seqlock_t \*sl)
:   start a seqlock_t read side critical section

**Parameters**

`const seqlock_t *sl`
:   Pointer to seqlock_t

**Return**

count, to be passed to [`read_seqretry()`](seqlock.md#c.read_seqretry "read_seqretry")

unsigned read_seqretry(const seqlock_t \*sl, unsigned start)
:   end a seqlock_t read side section

**Parameters**

`const seqlock_t *sl`
:   Pointer to seqlock_t

`unsigned start`
:   count, from [`read_seqbegin()`](seqlock.md#c.read_seqbegin "read_seqbegin")

**Description**

read_seqretry closes the read side critical section of given seqlock_t.
If the critical section was invalid, it must be ignored (and typically
retried).

**Return**

true if a read section retry is required, else false

void write_seqlock(seqlock_t \*sl)
:   start a seqlock_t write side critical section

**Parameters**

`seqlock_t *sl`
:   Pointer to seqlock_t

**Description**

write_seqlock opens a write side critical section for the given
seqlock_t. It also implicitly acquires the spinlock_t embedded inside
that sequential lock. All seqlock_t write side sections are thus
automatically serialized and non-preemptible.

**Context**

if the seqlock_t read section, or other write side critical
sections, can be invoked from hardirq or softirq contexts, use the
_irqsave or _bh variants of this function instead.

void write_sequnlock(seqlock_t \*sl)
:   end a seqlock_t write side critical section

**Parameters**

`seqlock_t *sl`
:   Pointer to seqlock_t

**Description**

write_sequnlock closes the (serialized and non-preemptible) write side
critical section of given seqlock_t.

void write_seqlock_bh(seqlock_t \*sl)
:   start a softirqs-disabled seqlock_t write section

**Parameters**

`seqlock_t *sl`
:   Pointer to seqlock_t

**Description**

_bh variant of [`write_seqlock()`](seqlock.md#c.write_seqlock "write_seqlock"). Use only if the read side section, or
other write side sections, can be invoked from softirq contexts.

void write_sequnlock_bh(seqlock_t \*sl)
:   end a softirqs-disabled seqlock_t write section

**Parameters**

`seqlock_t *sl`
:   Pointer to seqlock_t

**Description**

write_sequnlock_bh closes the serialized, non-preemptible, and
softirqs-disabled, seqlock_t write side critical section opened with
[`write_seqlock_bh()`](seqlock.md#c.write_seqlock_bh "write_seqlock_bh").

void write_seqlock_irq(seqlock_t \*sl)
:   start a non-interruptible seqlock_t write section

**Parameters**

`seqlock_t *sl`
:   Pointer to seqlock_t

**Description**

_irq variant of [`write_seqlock()`](seqlock.md#c.write_seqlock "write_seqlock"). Use only if the read side section, or
other write sections, can be invoked from hardirq contexts.

void write_sequnlock_irq(seqlock_t \*sl)
:   end a non-interruptible seqlock_t write section

**Parameters**

`seqlock_t *sl`
:   Pointer to seqlock_t

**Description**

write_sequnlock_irq closes the serialized and non-interruptible
seqlock_t write side section opened with [`write_seqlock_irq()`](seqlock.md#c.write_seqlock_irq "write_seqlock_irq").

write_seqlock_irqsave

`write_seqlock_irqsave (lock, flags)`

> start a non-interruptible seqlock_t write section

**Parameters**

`lock`
:   Pointer to seqlock_t

`flags`
:   Stack-allocated storage for saving caller's local interrupt
    state, to be passed to [`write_sequnlock_irqrestore()`](seqlock.md#c.write_sequnlock_irqrestore "write_sequnlock_irqrestore").

**Description**

_irqsave variant of [`write_seqlock()`](seqlock.md#c.write_seqlock "write_seqlock"). Use it only if the read side
section, or other write sections, can be invoked from hardirq context.

void write_sequnlock_irqrestore(seqlock_t \*sl, unsigned long flags)
:   end non-interruptible seqlock_t write section

**Parameters**

`seqlock_t *sl`
:   Pointer to seqlock_t

`unsigned long flags`
:   Caller's saved interrupt state, from [`write_seqlock_irqsave()`](seqlock.md#c.write_seqlock_irqsave "write_seqlock_irqsave")

**Description**

write_sequnlock_irqrestore closes the serialized and non-interruptible
seqlock_t write section previously opened with [`write_seqlock_irqsave()`](seqlock.md#c.write_seqlock_irqsave "write_seqlock_irqsave").

void read_seqlock_excl(seqlock_t \*sl)
:   begin a seqlock_t locking reader section

**Parameters**

`seqlock_t *sl`
:   Pointer to seqlock_t

**Description**

read_seqlock_excl opens a seqlock_t locking reader critical section. A
locking reader exclusively locks out *both* other writers *and* other
locking readers, but it does not update the embedded sequence number.

Locking readers act like a normal spin_lock()/spin_unlock().

The opened read section must be closed with [`read_sequnlock_excl()`](seqlock.md#c.read_sequnlock_excl "read_sequnlock_excl").

**Context**

if the seqlock_t write section, *or other read sections*, can
be invoked from hardirq or softirq contexts, use the _irqsave or _bh
variant of this function instead.

void read_sequnlock_excl(seqlock_t \*sl)
:   end a seqlock_t locking reader critical section

**Parameters**

`seqlock_t *sl`
:   Pointer to seqlock_t

void read_seqlock_excl_bh(seqlock_t \*sl)
:   start a seqlock_t locking reader section with softirqs disabled

**Parameters**

`seqlock_t *sl`
:   Pointer to seqlock_t

**Description**

_bh variant of [`read_seqlock_excl()`](seqlock.md#c.read_seqlock_excl "read_seqlock_excl"). Use this variant only if the
seqlock_t write side section, *or other read sections*, can be invoked
from softirq contexts.

void read_sequnlock_excl_bh(seqlock_t \*sl)
:   stop a seqlock_t softirq-disabled locking reader section

**Parameters**

`seqlock_t *sl`
:   Pointer to seqlock_t

void read_seqlock_excl_irq(seqlock_t \*sl)
:   start a non-interruptible seqlock_t locking reader section

**Parameters**

`seqlock_t *sl`
:   Pointer to seqlock_t

**Description**

_irq variant of [`read_seqlock_excl()`](seqlock.md#c.read_seqlock_excl "read_seqlock_excl"). Use this only if the seqlock_t
write side section, *or other read sections*, can be invoked from a
hardirq context.

void read_sequnlock_excl_irq(seqlock_t \*sl)
:   end an interrupts-disabled seqlock_t locking reader section

**Parameters**

`seqlock_t *sl`
:   Pointer to seqlock_t

read_seqlock_excl_irqsave

`read_seqlock_excl_irqsave (lock, flags)`

> start a non-interruptible seqlock_t locking reader section

**Parameters**

`lock`
:   Pointer to seqlock_t

`flags`
:   Stack-allocated storage for saving caller's local interrupt
    state, to be passed to [`read_sequnlock_excl_irqrestore()`](seqlock.md#c.read_sequnlock_excl_irqrestore "read_sequnlock_excl_irqrestore").

**Description**

_irqsave variant of [`read_seqlock_excl()`](seqlock.md#c.read_seqlock_excl "read_seqlock_excl"). Use this only if the seqlock_t
write side section, *or other read sections*, can be invoked from a
hardirq context.

void read_sequnlock_excl_irqrestore(seqlock_t \*sl, unsigned long flags)
:   end non-interruptible seqlock_t locking reader section

**Parameters**

`seqlock_t *sl`
:   Pointer to seqlock_t

`unsigned long flags`
:   Caller saved interrupt state, from [`read_seqlock_excl_irqsave()`](seqlock.md#c.read_seqlock_excl_irqsave "read_seqlock_excl_irqsave")

void read_seqbegin_or_lock(seqlock_t \*lock, int \*seq)
:   begin a seqlock_t lockless or locking reader

**Parameters**

`seqlock_t *lock`
:   Pointer to seqlock_t

`int *seq`
:   Marker and return parameter. If the passed value is even, the
    reader will become a *lockless* seqlock_t reader as in [`read_seqbegin()`](seqlock.md#c.read_seqbegin "read_seqbegin").
    If the passed value is odd, the reader will become a *locking* reader
    as in [`read_seqlock_excl()`](seqlock.md#c.read_seqlock_excl "read_seqlock_excl"). In the first call to this function, the
    caller *must* initialize and pass an even value to **seq**; this way, a
    lockless read can be optimistically tried first.

**Description**

read_seqbegin_or_lock is an API designed to optimistically try a normal
lockless seqlock_t read section first. If an odd counter is found, the
lockless read trial has failed, and the next read iteration transforms
itself into a full seqlock_t locking reader.

This is typically used to avoid seqlock_t lockless readers starvation
(too much retry loops) in the case of a sharp spike in write side
activity.

Check [Sequence counters and sequential locks](seqlock.md) for template example code.

**Context**

if the seqlock_t write section, *or other read sections*, can
be invoked from hardirq or softirq contexts, use the _irqsave or _bh
variant of this function instead.

**Return**

the encountered sequence counter value, through the **seq**
parameter, which is overloaded as a return parameter. This returned
value must be checked with [`need_seqretry()`](seqlock.md#c.need_seqretry "need_seqretry"). If the read section need to
be retried, this returned value must also be passed as the **seq**
parameter of the next [`read_seqbegin_or_lock()`](seqlock.md#c.read_seqbegin_or_lock "read_seqbegin_or_lock") iteration.

int need_seqretry(seqlock_t \*lock, int seq)
:   validate seqlock_t "locking or lockless" read section

**Parameters**

`seqlock_t *lock`
:   Pointer to seqlock_t

`int seq`
:   sequence count, from [`read_seqbegin_or_lock()`](seqlock.md#c.read_seqbegin_or_lock "read_seqbegin_or_lock")

**Return**

true if a read section retry is required, false otherwise

void done_seqretry(seqlock_t \*lock, int seq)
:   end seqlock_t "locking or lockless" reader section

**Parameters**

`seqlock_t *lock`
:   Pointer to seqlock_t

`int seq`
:   count, from [`read_seqbegin_or_lock()`](seqlock.md#c.read_seqbegin_or_lock "read_seqbegin_or_lock")

**Description**

done_seqretry finishes the seqlock_t read side critical section started
with [`read_seqbegin_or_lock()`](seqlock.md#c.read_seqbegin_or_lock "read_seqbegin_or_lock") and validated by [`need_seqretry()`](seqlock.md#c.need_seqretry "need_seqretry").

unsigned long read_seqbegin_or_lock_irqsave(seqlock_t \*lock, int \*seq)
:   begin a seqlock_t lockless reader, or a non-interruptible locking reader

**Parameters**

`seqlock_t *lock`
:   Pointer to seqlock_t

`int *seq`
:   Marker and return parameter. Check [`read_seqbegin_or_lock()`](seqlock.md#c.read_seqbegin_or_lock "read_seqbegin_or_lock").

**Description**

This is the _irqsave variant of [`read_seqbegin_or_lock()`](seqlock.md#c.read_seqbegin_or_lock "read_seqbegin_or_lock"). Use it only if
the seqlock_t write section, *or other read sections*, can be invoked
from hardirq context.

**Note**

Interrupts will be disabled only for "locking reader" mode.

**Return**

> 1. The saved local interrupts state in case of a locking reader, to
>    be passed to [`done_seqretry_irqrestore()`](seqlock.md#c.done_seqretry_irqrestore "done_seqretry_irqrestore").
> 2. The encountered sequence counter value, returned through **seq**
>    overloaded as a return parameter. Check [`read_seqbegin_or_lock()`](seqlock.md#c.read_seqbegin_or_lock "read_seqbegin_or_lock").

void done_seqretry_irqrestore(seqlock_t \*lock, int seq, unsigned long flags)
:   end a seqlock_t lockless reader, or a non-interruptible locking reader section

**Parameters**

`seqlock_t *lock`
:   Pointer to seqlock_t

`int seq`
:   Count, from [`read_seqbegin_or_lock_irqsave()`](seqlock.md#c.read_seqbegin_or_lock_irqsave "read_seqbegin_or_lock_irqsave")

`unsigned long flags`
:   Caller's saved local interrupt state in case of a locking
    reader, also from [`read_seqbegin_or_lock_irqsave()`](seqlock.md#c.read_seqbegin_or_lock_irqsave "read_seqbegin_or_lock_irqsave")

**Description**

This is the _irqrestore variant of [`done_seqretry()`](seqlock.md#c.done_seqretry "done_seqretry"). The read section
must've been opened with [`read_seqbegin_or_lock_irqsave()`](seqlock.md#c.read_seqbegin_or_lock_irqsave "read_seqbegin_or_lock_irqsave"), and validated
by [`need_seqretry()`](seqlock.md#c.need_seqretry "need_seqretry").
