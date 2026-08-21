---
collection: kernel
version: "6.8"
title: "splice and pipes"
source_url: https://www.kernel.org/doc/html/v6.8/filesystems/splice.html
fetched_at: 2026-08-21T03:38:25+00:00
---
# splice and pipes

## splice API

splice is a method for moving blocks of data around inside the kernel,
without continually transferring them between the kernel and user space.

ssize_t splice_to_pipe(struct [pipe_inode_info](splice.md#c.pipe_inode_info "pipe_inode_info") \*pipe, struct splice_pipe_desc \*spd)
:   fill passed data into a pipe

**Parameters**

`struct pipe_inode_info *pipe`
:   pipe to fill

`struct splice_pipe_desc *spd`
:   data to fill

**Description**

> **spd** contains a map of pages and len/offset tuples, along with
> the struct pipe_buf_operations associated with these pages. This
> function will link that data to the pipe.

ssize_t copy_splice_read(struct file \*in, loff_t \*ppos, struct [pipe_inode_info](splice.md#c.pipe_inode_info "pipe_inode_info") \*pipe, size_t len, unsigned int flags)
:   Copy data from a file and splice the copy into a pipe

**Parameters**

`struct file *in`
:   The file to read from

`loff_t *ppos`
:   Pointer to the file position to read from

`struct pipe_inode_info *pipe`
:   The pipe to splice into

`size_t len`
:   The amount to splice

`unsigned int flags`
:   The SPLICE_F_\* flags

**Description**

This function allocates a bunch of pages sufficient to hold the requested
amount of data (but limited by the remaining pipe capacity), passes it to
the file's ->read_iter() to read into and then splices the used pages into
the pipe.

**Return**

On success, the number of bytes read will be returned and **\*ppos**
will be updated if appropriate; 0 will be returned if there is no more data
to be read; -EAGAIN will be returned if the pipe had no space, and some
other negative error code will be returned on error. A short read may occur
if the pipe has insufficient space, we reach the end of the data or we hit a
hole.

int splice_from_pipe_feed(struct [pipe_inode_info](splice.md#c.pipe_inode_info "pipe_inode_info") \*pipe, struct splice_desc \*sd, splice_actor \*actor)
:   feed available data from a pipe to a file

**Parameters**

`struct pipe_inode_info *pipe`
:   pipe to splice from

`struct splice_desc *sd`
:   information to **actor**

`splice_actor *actor`
:   handler that splices the data

**Description**

> This function loops over the pipe and calls **actor** to do the
> actual moving of a single [`struct pipe_buffer`](splice.md#c.pipe_buffer "pipe_buffer") to the desired
> destination. It returns when there's no more buffers left in
> the pipe or if the requested number of bytes (**sd->total_len**)
> have been copied. It returns a positive number (one) if the
> pipe needs to be filled with more data, zero if the required
> number of bytes have been copied and -errno on error.
>
> This, together with splice_from_pipe_{begin,end,next}, may be
> used to implement the functionality of [`__splice_from_pipe()`](splice.md#c.__splice_from_pipe "__splice_from_pipe") when
> locking is required around copying the pipe buffers to the
> destination.

int splice_from_pipe_next(struct [pipe_inode_info](splice.md#c.pipe_inode_info "pipe_inode_info") \*pipe, struct splice_desc \*sd)
:   wait for some data to splice from

**Parameters**

`struct pipe_inode_info *pipe`
:   pipe to splice from

`struct splice_desc *sd`
:   information about the splice operation

**Description**

> This function will wait for some data and return a positive
> value (one) if pipe buffers are available. It will return zero
> or -errno if no more data needs to be spliced.

void splice_from_pipe_begin(struct splice_desc \*sd)
:   start splicing from pipe

**Parameters**

`struct splice_desc *sd`
:   information about the splice operation

**Description**

> This function should be called before a loop containing
> [`splice_from_pipe_next()`](splice.md#c.splice_from_pipe_next "splice_from_pipe_next") and [`splice_from_pipe_feed()`](splice.md#c.splice_from_pipe_feed "splice_from_pipe_feed") to
> initialize the necessary fields of **sd**.

void splice_from_pipe_end(struct [pipe_inode_info](splice.md#c.pipe_inode_info "pipe_inode_info") \*pipe, struct splice_desc \*sd)
:   finish splicing from pipe

**Parameters**

`struct pipe_inode_info *pipe`
:   pipe to splice from

`struct splice_desc *sd`
:   information about the splice operation

**Description**

> This function will wake up pipe writers if necessary. It should
> be called after a loop containing [`splice_from_pipe_next()`](splice.md#c.splice_from_pipe_next "splice_from_pipe_next") and
> [`splice_from_pipe_feed()`](splice.md#c.splice_from_pipe_feed "splice_from_pipe_feed").

ssize_t __splice_from_pipe(struct [pipe_inode_info](splice.md#c.pipe_inode_info "pipe_inode_info") \*pipe, struct splice_desc \*sd, splice_actor \*actor)
:   splice data from a pipe to given actor

**Parameters**

`struct pipe_inode_info *pipe`
:   pipe to splice from

`struct splice_desc *sd`
:   information to **actor**

`splice_actor *actor`
:   handler that splices the data

**Description**

> This function does little more than loop over the pipe and call
> **actor** to do the actual moving of a single [`struct pipe_buffer`](splice.md#c.pipe_buffer "pipe_buffer") to
> the desired destination. See pipe_to_file, pipe_to_sendmsg, or
> pipe_to_user.

ssize_t splice_from_pipe(struct [pipe_inode_info](splice.md#c.pipe_inode_info "pipe_inode_info") \*pipe, struct file \*out, loff_t \*ppos, size_t len, unsigned int flags, splice_actor \*actor)
:   splice data from a pipe to a file

**Parameters**

`struct pipe_inode_info *pipe`
:   pipe to splice from

`struct file *out`
:   file to splice to

`loff_t *ppos`
:   position in **out**

`size_t len`
:   how many bytes to splice

`unsigned int flags`
:   splice modifier flags

`splice_actor *actor`
:   handler that splices the data

**Description**

> See __splice_from_pipe. This function locks the pipe inode,
> otherwise it's identical to [`__splice_from_pipe()`](splice.md#c.__splice_from_pipe "__splice_from_pipe").

ssize_t iter_file_splice_write(struct [pipe_inode_info](splice.md#c.pipe_inode_info "pipe_inode_info") \*pipe, struct file \*out, loff_t \*ppos, size_t len, unsigned int flags)
:   splice data from a pipe to a file

**Parameters**

`struct pipe_inode_info *pipe`
:   pipe info

`struct file *out`
:   file to write to

`loff_t *ppos`
:   position in **out**

`size_t len`
:   number of bytes to splice

`unsigned int flags`
:   splice modifier flags

**Description**

> Will either move or copy pages (determined by **flags** options) from
> the given pipe inode to the given file.
> This one is ->write_iter-based.

ssize_t splice_to_socket(struct [pipe_inode_info](splice.md#c.pipe_inode_info "pipe_inode_info") \*pipe, struct file \*out, loff_t \*ppos, size_t len, unsigned int flags)
:   splice data from a pipe to a socket

**Parameters**

`struct pipe_inode_info *pipe`
:   pipe to splice from

`struct file *out`
:   socket to write to

`loff_t *ppos`
:   position in **out**

`size_t len`
:   number of bytes to splice

`unsigned int flags`
:   splice modifier flags

**Description**

> Will send **len** bytes from the pipe to a network socket. No data copying
> is involved.

ssize_t vfs_splice_read(struct file \*in, loff_t \*ppos, struct [pipe_inode_info](splice.md#c.pipe_inode_info "pipe_inode_info") \*pipe, size_t len, unsigned int flags)
:   Read data from a file and splice it into a pipe

**Parameters**

`struct file *in`
:   File to splice from

`loff_t *ppos`
:   Input file offset

`struct pipe_inode_info *pipe`
:   Pipe to splice to

`size_t len`
:   Number of bytes to splice

`unsigned int flags`
:   Splice modifier flags (SPLICE_F_\*)

**Description**

Splice the requested amount of data from the input file to the pipe. This
is synchronous as the caller must hold the pipe lock across the entire
operation.

If successful, it returns the amount of data spliced, 0 if it hit the EOF or
a hole and a negative error code otherwise.

ssize_t splice_direct_to_actor(struct file \*in, struct splice_desc \*sd, splice_direct_actor \*actor)
:   splices data directly between two non-pipes

**Parameters**

`struct file *in`
:   file to splice from

`struct splice_desc *sd`
:   actor information on where to splice to

`splice_direct_actor *actor`
:   handles the data splicing

**Description**

> This is a special case helper to splice directly between two
> points, without requiring an explicit pipe. Internally an allocated
> pipe is cached in the process, and reused during the lifetime of
> that process.

ssize_t do_splice_direct(struct file \*in, loff_t \*ppos, struct file \*out, loff_t \*opos, size_t len, unsigned int flags)
:   splices data directly between two files

**Parameters**

`struct file *in`
:   file to splice from

`loff_t *ppos`
:   input file offset

`struct file *out`
:   file to splice to

`loff_t *opos`
:   output file offset

`size_t len`
:   number of bytes to splice

`unsigned int flags`
:   splice modifier flags

**Description**

> For use by do_sendfile(). splice can easily emulate sendfile, but
> doing it in the application would incur an extra system call
> (splice in + splice out, as compared to just sendfile()). So this helper
> can splice directly through a process-private pipe.

Callers already called rw_verify_area() on the entire range.

ssize_t splice_file_range(struct file \*in, loff_t \*ppos, struct file \*out, loff_t \*opos, size_t len)
:   splices data between two files for copy_file_range()

**Parameters**

`struct file *in`
:   file to splice from

`loff_t *ppos`
:   input file offset

`struct file *out`
:   file to splice to

`loff_t *opos`
:   output file offset

`size_t len`
:   number of bytes to splice

**Description**

> For use by ->copy_file_range() methods.
> Like [`do_splice_direct()`](splice.md#c.do_splice_direct "do_splice_direct"), but vfs_copy_file_range() already holds
> start_file_write() on **out** file.

Callers already called rw_verify_area() on the entire range.

## pipes API

Pipe interfaces are all for in-kernel (builtin image) use. They are not
exported for use by modules.

struct pipe_buffer
:   a linux kernel pipe buffer

**Definition**:

```
struct pipe_buffer {
    struct page *page;
    unsigned int offset, len;
    const struct pipe_buf_operations *ops;
    unsigned int flags;
    unsigned long private;
};
```

**Members**

`page`
:   the page containing the data for the pipe buffer

`offset`
:   offset of data inside the **page**

`len`
:   length of data inside the **page**

`ops`
:   operations associated with this buffer. See **pipe_buf_operations**.

`flags`
:   pipe buffer flags. See above.

`private`
:   private data owned by the ops.

struct pipe_inode_info
:   a linux kernel pipe

**Definition**:

```
struct pipe_inode_info {
    struct mutex mutex;
    wait_queue_head_t rd_wait, wr_wait;
    unsigned int head;
    unsigned int tail;
    unsigned int max_usage;
    unsigned int ring_size;
    unsigned int nr_accounted;
    unsigned int readers;
    unsigned int writers;
    unsigned int files;
    unsigned int r_counter;
    unsigned int w_counter;
    bool poll_usage;
#ifdef CONFIG_WATCH_QUEUE;
    bool note_loss;
#endif;
    struct page *tmp_page;
    struct fasync_struct *fasync_readers;
    struct fasync_struct *fasync_writers;
    struct pipe_buffer *bufs;
    struct user_struct *user;
#ifdef CONFIG_WATCH_QUEUE;
    struct watch_queue *watch_queue;
#endif;
};
```

**Members**

`mutex`
:   mutex protecting the whole thing

`rd_wait`
:   reader wait point in case of empty pipe

`wr_wait`
:   writer wait point in case of full pipe

`head`
:   The point of buffer production

`tail`
:   The point of buffer consumption

`max_usage`
:   The maximum number of slots that may be used in the ring

`ring_size`
:   total number of buffers (should be a power of 2)

`nr_accounted`
:   The amount this pipe accounts for in user->pipe_bufs

`readers`
:   number of current readers of this pipe

`writers`
:   number of current writers of this pipe

`files`
:   number of struct file referring this pipe (protected by ->i_lock)

`r_counter`
:   reader counter

`w_counter`
:   writer counter

`poll_usage`
:   is this pipe used for epoll, which has crazy wakeups?

`note_loss`
:   The next read() should insert a data-lost message

`tmp_page`
:   cached released page

`fasync_readers`
:   reader side fasync

`fasync_writers`
:   writer side fasync

`bufs`
:   the circular array of pipe buffers

`user`
:   the user who created this pipe

`watch_queue`
:   If this pipe is a watch_queue, this is the stuff for that

bool pipe_has_watch_queue(const struct [pipe_inode_info](splice.md#c.pipe_inode_info "pipe_inode_info") \*pipe)
:   Check whether the pipe is a watch_queue, i.e. it was created with O_NOTIFICATION_PIPE

**Parameters**

`const struct pipe_inode_info *pipe`
:   The pipe to check

**Return**

true if pipe is a watch queue, false otherwise.

bool pipe_empty(unsigned int head, unsigned int tail)
:   Return true if the pipe is empty

**Parameters**

`unsigned int head`
:   The pipe ring head pointer

`unsigned int tail`
:   The pipe ring tail pointer

unsigned int pipe_occupancy(unsigned int head, unsigned int tail)
:   Return number of slots used in the pipe

**Parameters**

`unsigned int head`
:   The pipe ring head pointer

`unsigned int tail`
:   The pipe ring tail pointer

bool pipe_full(unsigned int head, unsigned int tail, unsigned int limit)
:   Return true if the pipe is full

**Parameters**

`unsigned int head`
:   The pipe ring head pointer

`unsigned int tail`
:   The pipe ring tail pointer

`unsigned int limit`
:   The maximum amount of slots available.

struct [pipe_buffer](splice.md#c.pipe_buffer "pipe_buffer") \*pipe_buf(const struct [pipe_inode_info](splice.md#c.pipe_inode_info "pipe_inode_info") \*pipe, unsigned int slot)
:   Return the pipe buffer for the specified slot in the pipe ring

**Parameters**

`const struct pipe_inode_info *pipe`
:   The pipe to access

`unsigned int slot`
:   The slot of interest

struct [pipe_buffer](splice.md#c.pipe_buffer "pipe_buffer") \*pipe_head_buf(const struct [pipe_inode_info](splice.md#c.pipe_inode_info "pipe_inode_info") \*pipe)
:   Return the pipe buffer at the head of the pipe ring

**Parameters**

`const struct pipe_inode_info *pipe`
:   The pipe to access

bool pipe_buf_get(struct [pipe_inode_info](splice.md#c.pipe_inode_info "pipe_inode_info") \*pipe, struct [pipe_buffer](splice.md#c.pipe_buffer "pipe_buffer") \*buf)
:   get a reference to a pipe_buffer

**Parameters**

`struct pipe_inode_info *pipe`
:   the pipe that the buffer belongs to

`struct pipe_buffer *buf`
:   the buffer to get a reference to

**Return**

`true` if the reference was successfully obtained.

void pipe_buf_release(struct [pipe_inode_info](splice.md#c.pipe_inode_info "pipe_inode_info") \*pipe, struct [pipe_buffer](splice.md#c.pipe_buffer "pipe_buffer") \*buf)
:   put a reference to a pipe_buffer

**Parameters**

`struct pipe_inode_info *pipe`
:   the pipe that the buffer belongs to

`struct pipe_buffer *buf`
:   the buffer to put a reference to

int pipe_buf_confirm(struct [pipe_inode_info](splice.md#c.pipe_inode_info "pipe_inode_info") \*pipe, struct [pipe_buffer](splice.md#c.pipe_buffer "pipe_buffer") \*buf)
:   verify contents of the pipe buffer

**Parameters**

`struct pipe_inode_info *pipe`
:   the pipe that the buffer belongs to

`struct pipe_buffer *buf`
:   the buffer to confirm

bool pipe_buf_try_steal(struct [pipe_inode_info](splice.md#c.pipe_inode_info "pipe_inode_info") \*pipe, struct [pipe_buffer](splice.md#c.pipe_buffer "pipe_buffer") \*buf)
:   attempt to take ownership of a pipe_buffer

**Parameters**

`struct pipe_inode_info *pipe`
:   the pipe that the buffer belongs to

`struct pipe_buffer *buf`
:   the buffer to attempt to steal

bool generic_pipe_buf_try_steal(struct [pipe_inode_info](splice.md#c.pipe_inode_info "pipe_inode_info") \*pipe, struct [pipe_buffer](splice.md#c.pipe_buffer "pipe_buffer") \*buf)
:   attempt to take ownership of a [`pipe_buffer`](splice.md#c.pipe_buffer "pipe_buffer")

**Parameters**

`struct pipe_inode_info *pipe`
:   the pipe that the buffer belongs to

`struct pipe_buffer *buf`
:   the buffer to attempt to steal

**Description**

> This function attempts to steal the `struct page` attached to
> **buf**. If successful, this function returns 0 and returns with
> the page locked. The caller may then reuse the page for whatever
> he wishes; the typical use is insertion into a different file
> page cache.

bool generic_pipe_buf_get(struct [pipe_inode_info](splice.md#c.pipe_inode_info "pipe_inode_info") \*pipe, struct [pipe_buffer](splice.md#c.pipe_buffer "pipe_buffer") \*buf)
:   get a reference to a [`struct pipe_buffer`](splice.md#c.pipe_buffer "pipe_buffer")

**Parameters**

`struct pipe_inode_info *pipe`
:   the pipe that the buffer belongs to

`struct pipe_buffer *buf`
:   the buffer to get a reference to

**Description**

> This function grabs an extra reference to **buf**. It's used in
> the tee() system call, when we duplicate the buffers in one
> pipe into another.

void generic_pipe_buf_release(struct [pipe_inode_info](splice.md#c.pipe_inode_info "pipe_inode_info") \*pipe, struct [pipe_buffer](splice.md#c.pipe_buffer "pipe_buffer") \*buf)
:   put a reference to a [`struct pipe_buffer`](splice.md#c.pipe_buffer "pipe_buffer")

**Parameters**

`struct pipe_inode_info *pipe`
:   the pipe that the buffer belongs to

`struct pipe_buffer *buf`
:   the buffer to put a reference to

**Description**

> This function releases a reference to **buf**.
