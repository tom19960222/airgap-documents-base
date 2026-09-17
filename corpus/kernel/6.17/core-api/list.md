---
collection: kernel
version: "6.17"
title: "Linked Lists in Linux"
source_url: https://www.kernel.org/doc/html/v6.17/core-api/list.html
fetched_at: 2026-09-16T16:19:10+00:00
---
# [Linked Lists in Linux](list.md#id1)

Author:
:   Nicolas Frattaroli <[nicolas.frattaroli@collabora.com](mailto:nicolas.frattaroli%40collabora.com)>

Contents

- [Linked Lists in Linux](list.md#linked-lists-in-linux)

  - [Introduction](list.md#introduction)
  - [Linux implementation of doubly linked lists](list.md#linux-implementation-of-doubly-linked-lists)

    - [Declaring a node](list.md#declaring-a-node)
    - [Declaring and initializing a list](list.md#declaring-and-initializing-a-list)
    - [Adding nodes to the list](list.md#adding-nodes-to-the-list)
    - [Traversing the list](list.md#traversing-the-list)
    - [Removing nodes from the list](list.md#removing-nodes-from-the-list)
    - [Traversing whilst removing nodes](list.md#traversing-whilst-removing-nodes)
    - [Cutting a list](list.md#cutting-a-list)
    - [Moving entries and partial lists](list.md#moving-entries-and-partial-lists)
    - [Rotating entries](list.md#rotating-entries)
    - [Swapping entries](list.md#swapping-entries)
    - [Splicing two lists together](list.md#splicing-two-lists-together)
    - [Concurrency considerations](list.md#concurrency-considerations)
    - [Further reading](list.md#further-reading)
  - [Full List API](list.md#full-list-api)

## [Introduction](list.md#id2)

Linked lists are one of the most basic data structures used in many programs.
The Linux kernel implements several different flavours of linked lists. The
purpose of this document is not to explain linked lists in general, but to show
new kernel developers how to use the Linux kernel implementations of linked
lists.

Please note that while linked lists certainly are ubiquitous, they are rarely
the best data structure to use in cases where a simple array doesn’t already
suffice. In particular, due to their poor data locality, linked lists are a bad
choice in situations where performance may be of consideration. Familiarizing
oneself with other in-kernel generic data structures, especially for concurrent
accesses, is highly encouraged.

## [Linux implementation of doubly linked lists](list.md#id3)

Linux’s linked list implementations can be used by including the header file
`<linux/list.h>`.

The doubly-linked list will likely be the most familiar to many readers. It’s a
list that can efficiently be traversed forwards and backwards.

The Linux kernel’s doubly-linked list is circular in nature. This means that to
get from the head node to the tail, we can just travel one edge backwards.
Similarly, to get from the tail node to the head, we can simply travel forwards
“beyond” the tail and arrive back at the head.

### [Declaring a node](list.md#id4)

A node in a doubly-linked list is declared by adding a `struct list_head`
member to the data structure you wish to be contained in the list:

```c
struct clown {
        unsigned long long shoe_size;
        const char *name;
        struct list_head node;  /* the aforementioned member */
};
```

This may be an unfamiliar approach to some, as the classical explanation of a
linked list is a list node data structure with pointers to the previous and next
list node, as well the payload data. Linux chooses this approach because it
allows for generic list modification code regardless of what data structure is
contained within the list. Since the `struct list_head` member is not a pointer
but part of the data structure proper, the `container_of()` pattern can be used by
the list implementation to access the payload data regardless of its type, while
staying oblivious to what said type actually is.

### [Declaring and initializing a list](list.md#id5)

A doubly-linked list can then be declared as just another `struct list_head`,
and initialized with the `LIST_HEAD_INIT()` macro during initial assignment, or
with the [`INIT_LIST_HEAD()`](list.md#c.INIT_LIST_HEAD "INIT_LIST_HEAD") function later:

```c
struct clown_car {
        int tyre_pressure[4];
        struct list_head clowns;        /* Looks like a node! */
};

/* ... Somewhere later in our driver ... */

static int circus_init(struct circus_priv *circus)
{
        struct clown_car other_car = {
              .tyre_pressure = {10, 12, 11, 9},
              .clowns = LIST_HEAD_INIT(other_car.clowns)
        };

        INIT_LIST_HEAD(&circus->car.clowns);

        return 0;
}
```

A further point of confusion to some may be that the list itself doesn’t really
have its own type. The concept of the entire linked list and a
`struct list_head` member that points to other entries in the list are one and
the same.

### [Adding nodes to the list](list.md#id6)

Adding a node to the linked list is done through the [`list_add()`](list.md#c.list_add "list_add") macro.

We’ll return to our clown car example to illustrate how nodes get added to the
list:

```c
static int circus_fill_car(struct circus_priv *circus)
{
        struct clown_car *car = &circus->car;
        struct clown *grock;
        struct clown *dimitri;

        /* State 1 */

        grock = kzalloc(sizeof(*grock), GFP_KERNEL);
        if (!grock)
                return -ENOMEM;
        grock->name = "Grock";
        grock->shoe_size = 1000;

        /* Note that we're adding the "node" member */
        list_add(&grock->node, &car->clowns);

        /* State 2 */

        dimitri = kzalloc(sizeof(*dimitri), GFP_KERNEL);
        if (!dimitri)
                return -ENOMEM;
        dimitri->name = "Dimitri";
        dimitri->shoe_size = 50;

        list_add(&dimitri->node, &car->clowns);

        /* State 3 */

        return 0;
}
```

In State 1, our list of clowns is still empty:

```
     .------.
     v      |
.--------.  |
| clowns |--'
'--------'
```

This diagram shows the singular “clowns” node pointing at itself. In this
diagram, and all following diagrams, only the forward edges are shown, to aid in
clarity.

In State 2, we’ve added Grock after the list head:

```
     .--------------------.
     v                    |
.--------.     .-------.  |
| clowns |---->| Grock |--'
'--------'     '-------'
```

This diagram shows the “clowns” node pointing at a new node labeled “Grock”.
The Grock node is pointing back at the “clowns” node.

In State 3, we’ve added Dimitri after the list head, resulting in the following:

```
     .------------------------------------.
     v                                    |
.--------.     .---------.     .-------.  |
| clowns |---->| Dimitri |---->| Grock |--'
'--------'     '---------'     '-------'
```

This diagram shows the “clowns” node pointing at a new node labeled “Dimitri”,
which then points at the node labeled “Grock”. The “Grock” node still points
back at the “clowns” node.

If we wanted to have Dimitri inserted at the end of the list instead, we’d use
[`list_add_tail()`](list.md#c.list_add_tail "list_add_tail"). Our code would then look like this:

```c
static int circus_fill_car(struct circus_priv *circus)
{
        /* ... */

        list_add_tail(&dimitri->node, &car->clowns);

        /* State 3b */

        return 0;
}
```

This results in the following list:

```
     .------------------------------------.
     v                                    |
.--------.     .-------.     .---------.  |
| clowns |---->| Grock |---->| Dimitri |--'
'--------'     '-------'     '---------'
```

This diagram shows the “clowns” node pointing at the node labeled “Grock”,
which points at the new node labeled “Dimitri”. The node labeled “Dimitri”
points back at the “clowns” node.

### [Traversing the list](list.md#id7)

To iterate the list, we can loop through all nodes within the list with
[`list_for_each()`](list.md#c.list_for_each "list_for_each").

In our clown example, this results in the following somewhat awkward code:

```c
static unsigned long long circus_get_max_shoe_size(struct circus_priv *circus)
{
        unsigned long long res = 0;
        struct clown *e;
        struct list_head *cur;

        list_for_each(cur, &circus->car.clowns) {
                e = list_entry(cur, struct clown, node);
                if (e->shoe_size > res)
                        res = e->shoe_size;
        }

        return res;
}
```

The [`list_entry()`](list.md#c.list_entry "list_entry") macro internally uses the aforementioned `container_of()` to
retrieve the data structure instance that `node` is a member of.

Note how the additional [`list_entry()`](list.md#c.list_entry "list_entry") call is a little awkward here. It’s only
there because we’re iterating through the `node` members, but we really want
to iterate through the payload, i.e. the `struct clown` that contains each
node’s `struct list_head`. For this reason, there is a second macro:
[`list_for_each_entry()`](list.md#c.list_for_each_entry "list_for_each_entry")

Using it would change our code to something like this:

```c
static unsigned long long circus_get_max_shoe_size(struct circus_priv *circus)
{
        unsigned long long res = 0;
        struct clown *e;

        list_for_each_entry(e, &circus->car.clowns, node) {
                if (e->shoe_size > res)
                        res = e->shoe_size;
        }

        return res;
}
```

This eliminates the need for the [`list_entry()`](list.md#c.list_entry "list_entry") step, and our loop cursor is now
of the type of our payload. The macro is given the member name that corresponds
to the list’s `struct list_head` within the clown data structure so that it can
still walk the list.

### [Removing nodes from the list](list.md#id8)

The [`list_del()`](list.md#c.list_del "list_del") function can be used to remove entries from the list. It not only
removes the given entry from the list, but poisons the entry’s `prev` and
`next` pointers, so that unintended use of the entry after removal does not
go unnoticed.

We can extend our previous example to remove one of the entries:

```c
static int circus_fill_car(struct circus_priv *circus)
{
        /* ... */

        list_add(&dimitri->node, &car->clowns);

        /* State 3 */

        list_del(&dimitri->node);

        /* State 4 */

        return 0;
}
```

The result of this would be this:

```
     .--------------------.
     v                    |
.--------.     .-------.  |      .---------.
| clowns |---->| Grock |--'      | Dimitri |
'--------'     '-------'         '---------'
```

This diagram shows the “clowns” node pointing at the node labeled “Grock”,
which points back at the “clowns” node. Off to the side is a lone node labeled
“Dimitri”, which has no arrows pointing anywhere.

Note how the Dimitri node does not point to itself; its pointers are
intentionally set to a “poison” value that the list code refuses to traverse.

If we wanted to reinitialize the removed node instead to make it point at itself
again like an empty list head, we can use [`list_del_init()`](list.md#c.list_del_init "list_del_init") instead:

```c
static int circus_fill_car(struct circus_priv *circus)
{
        /* ... */

        list_add(&dimitri->node, &car->clowns);

        /* State 3 */

        list_del_init(&dimitri->node);

        /* State 4b */

        return 0;
}
```

This results in the deleted node pointing to itself again:

```
     .--------------------.           .-------.
     v                    |           v       |
.--------.     .-------.  |      .---------.  |
| clowns |---->| Grock |--'      | Dimitri |--'
'--------'     '-------'         '---------'
```

This diagram shows the “clowns” node pointing at the node labeled “Grock”,
which points back at the “clowns” node. Off to the side is a lone node labeled
“Dimitri”, which points to itself.

### [Traversing whilst removing nodes](list.md#id9)

Deleting entries while we’re traversing the list will cause problems if we use
[`list_for_each()`](list.md#c.list_for_each "list_for_each") and [`list_for_each_entry()`](list.md#c.list_for_each_entry "list_for_each_entry"), as deleting the current entry would
modify the `next` pointer of it, which means the traversal can’t properly
advance to the next list entry.

There is a solution to this however: [`list_for_each_safe()`](list.md#c.list_for_each_safe "list_for_each_safe") and
[`list_for_each_entry_safe()`](list.md#c.list_for_each_entry_safe "list_for_each_entry_safe"). These take an additional parameter of a pointer to
a `struct list_head` to use as temporary storage for the next entry during
iteration, solving the issue.

An example of how to use it:

```c
static void circus_eject_insufficient_clowns(struct circus_priv *circus)
{
        struct clown *e;
        struct clown *n;      /* temporary storage for safe iteration */

        list_for_each_entry_safe(e, n, &circus->car.clowns, node) {
              if (e->shoe_size < 500)
                      list_del(&e->node);
        }
}
```

Proper memory management (i.e. freeing the deleted node while making sure
nothing still references it) in this case is left as an exercise to the reader.

### [Cutting a list](list.md#id10)

There are two helper functions to cut lists with. Both take elements from the
list `head`, and replace the contents of the list `list`.

The first such function is [`list_cut_position()`](list.md#c.list_cut_position "list_cut_position"). It removes all list entries from
`head` up to and including `entry`, placing them in `list` instead.

In this example, it’s assumed we start with the following list:

```
     .----------------------------------------------------------------.
     v                                                                |
.--------.     .-------.     .---------.     .-----.     .---------.  |
| clowns |---->| Grock |---->| Dimitri |---->| Pic |---->| Alfredo |--'
'--------'     '-------'     '---------'     '-----'     '---------'
```

With the following code, every clown up to and including “Pic” is moved from
the “clowns” list head to a separate `struct list_head` initialized at local
stack variable `retirement`:

```c
static void circus_retire_clowns(struct circus_priv *circus)
{
        struct list_head retirement = LIST_HEAD_INIT(retirement);
        struct clown *grock, *dimitri, *pic, *alfredo;
        struct clown_car *car = &circus->car;

        /* ... clown initialization, list adding ... */

        list_cut_position(&retirement, &car->clowns, &pic->node);

        /* State 1 */
}
```

The resulting `car->clowns` list would be this:

```
     .----------------------.
     v                      |
.--------.     .---------.  |
| clowns |---->| Alfredo |--'
'--------'     '---------'
```

Meanwhile, the `retirement` list is transformed to the following:

```
       .--------------------------------------------------.
       v                                                  |
.------------.     .-------.     .---------.     .-----.  |
| retirement |---->| Grock |---->| Dimitri |---->| Pic |--'
'------------'     '-------'     '---------'     '-----'
```

The second function, [`list_cut_before()`](list.md#c.list_cut_before "list_cut_before"), is much the same, except it cuts before
the `entry` node, i.e. it removes all list entries from `head` up to but
excluding `entry`, placing them in `list` instead. This example assumes the
same initial starting list as the previous example:

```c
static void circus_retire_clowns(struct circus_priv *circus)
{
        struct list_head retirement = LIST_HEAD_INIT(retirement);
        struct clown *grock, *dimitri, *pic, *alfredo;
        struct clown_car *car = &circus->car;

        /* ... clown initialization, list adding ... */

        list_cut_before(&retirement, &car->clowns, &pic->node);

        /* State 1b */
}
```

The resulting `car->clowns` list would be this:

```
     .----------------------------------.
     v                                  |
.--------.     .-----.     .---------.  |
| clowns |---->| Pic |---->| Alfredo |--'
'--------'     '-----'     '---------'
```

Meanwhile, the `retirement` list is transformed to the following:

```
       .--------------------------------------.
       v                                      |
.------------.     .-------.     .---------.  |
| retirement |---->| Grock |---->| Dimitri |--'
'------------'     '-------'     '---------'
```

It should be noted that both functions will destroy links to any existing nodes
in the destination `struct list_head *list`.

### [Moving entries and partial lists](list.md#id11)

The [`list_move()`](list.md#c.list_move "list_move") and [`list_move_tail()`](list.md#c.list_move_tail "list_move_tail") functions can be used to move an entry
from one list to another, to either the start or end respectively.

In the following example, we’ll assume we start with two lists (“clowns” and
“sidewalk” in the following initial state “State 0”:

```
     .----------------------------------------------------------------.
     v                                                                |
.--------.     .-------.     .---------.     .-----.     .---------.  |
| clowns |---->| Grock |---->| Dimitri |---->| Pic |---->| Alfredo |--'
'--------'     '-------'     '---------'     '-----'     '---------'

      .-------------------.
      v                   |
.----------.     .-----.  |
| sidewalk |---->| Pio |--'
'----------'     '-----'
```

We apply the following example code to the two lists:

```c
static void circus_clowns_exit_car(struct circus_priv *circus)
{
        struct list_head sidewalk = LIST_HEAD_INIT(sidewalk);
        struct clown *grock, *dimitri, *pic, *alfredo, *pio;
        struct clown_car *car = &circus->car;

        /* ... clown initialization, list adding ... */

        /* State 0 */

        list_move(&pic->node, &sidewalk);

        /* State 1 */

        list_move_tail(&dimitri->node, &sidewalk);

        /* State 2 */
}
```

In State 1, we arrive at the following situation:

```
    .-----------------------------------------------------.
    |                                                     |
    v                                                     |
.--------.     .-------.     .---------.     .---------.  |
| clowns |---->| Grock |---->| Dimitri |---->| Alfredo |--'
'--------'     '-------'     '---------'     '---------'

      .-------------------------------.
      v                               |
.----------.     .-----.     .-----.  |
| sidewalk |---->| Pic |---->| Pio |--'
'----------'     '-----'     '-----'
```

In State 2, after we’ve moved Dimitri to the tail of sidewalk, the situation
changes as follows:

```
    .-------------------------------------.
    |                                     |
    v                                     |
.--------.     .-------.     .---------.  |
| clowns |---->| Grock |---->| Alfredo |--'
'--------'     '-------'     '---------'

      .-----------------------------------------------.
      v                                               |
.----------.     .-----.     .-----.     .---------.  |
| sidewalk |---->| Pic |---->| Pio |---->| Dimitri |--'
'----------'     '-----'     '-----'     '---------'
```

As long as the source and destination list head are part of the same list, we
can also efficiently bulk move a segment of the list to the tail end of the
list. We continue the previous example by adding a [`list_bulk_move_tail()`](list.md#c.list_bulk_move_tail "list_bulk_move_tail") after
State 2, moving Pic and Pio to the tail end of the sidewalk list.

```c
static void circus_clowns_exit_car(struct circus_priv *circus)
{
        struct list_head sidewalk = LIST_HEAD_INIT(sidewalk);
        struct clown *grock, *dimitri, *pic, *alfredo, *pio;
        struct clown_car *car = &circus->car;

        /* ... clown initialization, list adding ... */

        /* State 0 */

        list_move(&pic->node, &sidewalk);

        /* State 1 */

        list_move_tail(&dimitri->node, &sidewalk);

        /* State 2 */

        list_bulk_move_tail(&sidewalk, &pic->node, &pio->node);

        /* State 3 */
}
```

For the sake of brevity, only the altered “sidewalk” list at State 3 is depicted
in the following diagram:

```
      .-----------------------------------------------.
      v                                               |
.----------.     .---------.     .-----.     .-----.  |
| sidewalk |---->| Dimitri |---->| Pic |---->| Pio |--'
'----------'     '---------'     '-----'     '-----'
```

Do note that [`list_bulk_move_tail()`](list.md#c.list_bulk_move_tail "list_bulk_move_tail") does not do any checking as to whether all
three supplied `struct list_head *` parameters really do belong to the same
list. If you use it outside the constraints the documentation gives, then the
result is a matter between you and the implementation.

### [Rotating entries](list.md#id12)

A common write operation on lists, especially when using them as queues, is
to rotate it. A list rotation means entries at the front are sent to the back.

For rotation, Linux provides us with two functions: [`list_rotate_left()`](list.md#c.list_rotate_left "list_rotate_left") and
[`list_rotate_to_front()`](list.md#c.list_rotate_to_front "list_rotate_to_front"). The former can be pictured like a bicycle chain, taking
the entry after the supplied `struct list_head *` and moving it to the tail,
which in essence means the entire list, due to its circular nature, rotates by
one position.

The latter, [`list_rotate_to_front()`](list.md#c.list_rotate_to_front "list_rotate_to_front"), takes the same concept one step further:
instead of advancing the list by one entry, it advances it *until* the specified
entry is the new front.

In the following example, our starting state, State 0, is the following:

```
     .-----------------------------------------------------------------.
     v                                                                 |
.--------.   .-------.   .---------.   .-----.   .---------.   .-----. |
| clowns |-->| Grock |-->| Dimitri |-->| Pic |-->| Alfredo |-->| Pio |-'
'--------'   '-------'   '---------'   '-----'   '---------'   '-----'
```

The example code being used to demonstrate list rotations is the following:

```c
static void circus_clowns_rotate(struct circus_priv *circus)
{
        struct clown *grock, *dimitri, *pic, *alfredo, *pio;
        struct clown_car *car = &circus->car;

        /* ... clown initialization, list adding ... */

        /* State 0 */

        list_rotate_left(&car->clowns);

        /* State 1 */

        list_rotate_to_front(&alfredo->node, &car->clowns);

        /* State 2 */

}
```

In State 1, we arrive at the following situation:

```
     .-----------------------------------------------------------------.
     v                                                                 |
.--------.   .---------.   .-----.   .---------.   .-----.   .-------. |
| clowns |-->| Dimitri |-->| Pic |-->| Alfredo |-->| Pio |-->| Grock |-'
'--------'   '---------'   '-----'   '---------'   '-----'   '-------'
```

Next, after the [`list_rotate_to_front()`](list.md#c.list_rotate_to_front "list_rotate_to_front") call, we arrive in the following
State 2:

```
     .-----------------------------------------------------------------.
     v                                                                 |
.--------.   .---------.   .-----.   .-------.   .---------.   .-----. |
| clowns |-->| Alfredo |-->| Pio |-->| Grock |-->| Dimitri |-->| Pic |-'
'--------'   '---------'   '-----'   '-------'   '---------'   '-----'
```

As is hopefully evident from the diagrams, the entries in front of “Alfredo”
were cycled to the tail end of the list.

### [Swapping entries](list.md#id13)

Another common operation is that two entries need to be swapped with each other.

For this, Linux provides us with [`list_swap()`](list.md#c.list_swap "list_swap").

In the following example, we have a list with three entries, and swap two of
them. This is our starting state in “State 0”:

```
     .-----------------------------------------.
     v                                         |
.--------.   .-------.   .---------.   .-----. |
| clowns |-->| Grock |-->| Dimitri |-->| Pic |-'
'--------'   '-------'   '---------'   '-----'
```

```c
static void circus_clowns_swap(struct circus_priv *circus)
{
        struct clown *grock, *dimitri, *pic;
        struct clown_car *car = &circus->car;

        /* ... clown initialization, list adding ... */

        /* State 0 */

        list_swap(&dimitri->node, &pic->node);

        /* State 1 */
}
```

The resulting list at State 1 is the following:

```
     .-----------------------------------------.
     v                                         |
.--------.   .-------.   .-----.   .---------. |
| clowns |-->| Grock |-->| Pic |-->| Dimitri |-'
'--------'   '-------'   '-----'   '---------'
```

As is evident by comparing the diagrams, the “Pic” and “Dimitri” nodes have
traded places.

### [Splicing two lists together](list.md#id14)

Say we have two lists, in the following example one represented by a list head
we call “knie” and one we call “stey”. In a hypothetical circus acquisition,
the two list of clowns should be spliced together. The following is our
situation in “State 0”:

```
    .-----------------------------------------.
    |                                         |
    v                                         |
.------.   .-------.   .---------.   .-----.  |
| knie |-->| Grock |-->| Dimitri |-->| Pic |--'
'------'   '-------'   '---------'   '-----'

    .-----------------------------.
    v                             |
.------.   .---------.   .-----.  |
| stey |-->| Alfredo |-->| Pio |--'
'------'   '---------'   '-----'
```

The function to splice these two lists together is [`list_splice()`](list.md#c.list_splice "list_splice"). Our example
code is as follows:

```c
static void circus_clowns_splice(void)
{
        struct clown *grock, *dimitri, *pic, *alfredo, *pio;
        struct list_head knie = LIST_HEAD_INIT(knie);
        struct list_head stey = LIST_HEAD_INIT(stey);

        /* ... Clown allocation and initialization here ... */

        list_add_tail(&grock->node, &knie);
        list_add_tail(&dimitri->node, &knie);
        list_add_tail(&pic->node, &knie);
        list_add_tail(&alfredo->node, &stey);
        list_add_tail(&pio->node, &stey);

        /* State 0 */

        list_splice(&stey, &dimitri->node);

        /* State 1 */
}
```

The [`list_splice()`](list.md#c.list_splice "list_splice") call here adds all the entries in `stey` to the list
`dimitri`’s `node` list_head is in, after the `node` of `dimitri`. A
somewhat surprising diagram of the resulting “State 1” follows:

```
    .-----------------------------------------------------------------.
    |                                                                 |
    v                                                                 |
.------.   .-------.   .---------.   .---------.   .-----.   .-----.  |
| knie |-->| Grock |-->| Dimitri |-->| Alfredo |-->| Pio |-->| Pic |--'
'------'   '-------'   '---------'   '---------'   '-----'   '-----'
                                          ^
          .-------------------------------'
          |
.------.  |
| stey |--'
'------'
```

Traversing the `stey` list no longer results in correct behavior. A call of
[`list_for_each()`](list.md#c.list_for_each "list_for_each") on `stey` results in an infinite loop, as it never returns
back to the `stey` list head.

This is because [`list_splice()`](list.md#c.list_splice "list_splice") did not reinitialize the list_head it took
entries from, leaving its pointer pointing into what is now a different list.

If we want to avoid this situation, [`list_splice_init()`](list.md#c.list_splice_init "list_splice_init") can be used. It does the
same thing as [`list_splice()`](list.md#c.list_splice "list_splice"), except reinitalizes the donor list_head after the
transplant.

### [Concurrency considerations](list.md#id15)

Concurrent access and modification of a list needs to be protected with a lock
in most cases. Alternatively and preferably, one may use the RCU primitives for
lists in read-mostly use-cases, where read accesses to the list are common but
modifications to the list less so. See [Using RCU to Protect Read-Mostly Linked Lists](../RCU/listRCU.md) for more
details.

### [Further reading](list.md#id16)

- [How does the kernel implements Linked Lists? - KernelNewbies](https://kernelnewbies.org/FAQ/LinkedLists)

## [Full List API](list.md#id17)

void INIT_LIST_HEAD(struct list_head \*list)
:   Initialize a list_head structure

**Parameters**

`struct list_head *list`
:   list_head structure to be initialized.

**Description**

Initializes the list_head to point to itself. If it is a list header,
the result is an empty list.

void list_add(struct list_head \*new, struct list_head \*head)
:   add a new entry

**Parameters**

`struct list_head *new`
:   new entry to be added

`struct list_head *head`
:   list head to add it after

**Description**

Insert a new entry after the specified head.
This is good for implementing stacks.

void list_add_tail(struct list_head \*new, struct list_head \*head)
:   add a new entry

**Parameters**

`struct list_head *new`
:   new entry to be added

`struct list_head *head`
:   list head to add it before

**Description**

Insert a new entry before the specified head.
This is useful for implementing queues.

void list_del(struct list_head \*entry)
:   deletes entry from list.

**Parameters**

`struct list_head *entry`
:   the element to delete from the list.

**Note**

[`list_empty()`](list.md#c.list_empty "list_empty") on entry does not return true after this, the entry is
in an undefined state.

void list_replace(struct list_head \*old, struct list_head \*new)
:   replace old entry by new one

**Parameters**

`struct list_head *old`
:   the element to be replaced

`struct list_head *new`
:   the new element to insert

**Description**

If **old** was empty, it will be overwritten.

void list_replace_init(struct list_head \*old, struct list_head \*new)
:   replace old entry by new one and initialize the old one

**Parameters**

`struct list_head *old`
:   the element to be replaced

`struct list_head *new`
:   the new element to insert

**Description**

If **old** was empty, it will be overwritten.

void list_swap(struct list_head \*entry1, struct list_head \*entry2)
:   replace entry1 with entry2 and re-add entry1 at entry2’s position

**Parameters**

`struct list_head *entry1`
:   the location to place entry2

`struct list_head *entry2`
:   the location to place entry1

void list_del_init(struct list_head \*entry)
:   deletes entry from list and reinitialize it.

**Parameters**

`struct list_head *entry`
:   the element to delete from the list.

void list_move(struct list_head \*list, struct list_head \*head)
:   delete from one list and add as another’s head

**Parameters**

`struct list_head *list`
:   the entry to move

`struct list_head *head`
:   the head that will precede our entry

void list_move_tail(struct list_head \*list, struct list_head \*head)
:   delete from one list and add as another’s tail

**Parameters**

`struct list_head *list`
:   the entry to move

`struct list_head *head`
:   the head that will follow our entry

void list_bulk_move_tail(struct list_head \*head, struct list_head \*first, struct list_head \*last)
:   move a subsection of a list to its tail

**Parameters**

`struct list_head *head`
:   the head that will follow our entry

`struct list_head *first`
:   first entry to move

`struct list_head *last`
:   last entry to move, can be the same as first

**Description**

Move all entries between **first** and including **last** before **head**.
All three entries must belong to the same linked list.

int list_is_first(const struct list_head \*list, const struct list_head \*head)
:   - tests whether **list** is the first entry in list **head**

**Parameters**

`const struct list_head *list`
:   the entry to test

`const struct list_head *head`
:   the head of the list

int list_is_last(const struct list_head \*list, const struct list_head \*head)
:   tests whether **list** is the last entry in list **head**

**Parameters**

`const struct list_head *list`
:   the entry to test

`const struct list_head *head`
:   the head of the list

int list_is_head(const struct list_head \*list, const struct list_head \*head)
:   tests whether **list** is the list **head**

**Parameters**

`const struct list_head *list`
:   the entry to test

`const struct list_head *head`
:   the head of the list

int list_empty(const struct list_head \*head)
:   tests whether a list is empty

**Parameters**

`const struct list_head *head`
:   the list to test.

void list_del_init_careful(struct list_head \*entry)
:   deletes entry from list and reinitialize it.

**Parameters**

`struct list_head *entry`
:   the element to delete from the list.

**Description**

This is the same as [`list_del_init()`](list.md#c.list_del_init "list_del_init"), except designed to be used
together with [`list_empty_careful()`](list.md#c.list_empty_careful "list_empty_careful") in a way to guarantee ordering
of other memory operations.

Any memory operations done before a [`list_del_init_careful()`](list.md#c.list_del_init_careful "list_del_init_careful") are
guaranteed to be visible after a [`list_empty_careful()`](list.md#c.list_empty_careful "list_empty_careful") test.

int list_empty_careful(const struct list_head \*head)
:   tests whether a list is empty and not being modified

**Parameters**

`const struct list_head *head`
:   the list to test

**Description**

tests whether a list is empty _and_ checks that no other CPU might be
in the process of modifying either member (next or prev)

**NOTE**

using [`list_empty_careful()`](list.md#c.list_empty_careful "list_empty_careful") without synchronization
can only be safe if the only activity that can happen
to the list entry is [`list_del_init()`](list.md#c.list_del_init "list_del_init"). Eg. it cannot be used
if another CPU could re-[`list_add()`](list.md#c.list_add "list_add") it.

void list_rotate_left(struct list_head \*head)
:   rotate the list to the left

**Parameters**

`struct list_head *head`
:   the head of the list

void list_rotate_to_front(struct list_head \*list, struct list_head \*head)
:   Rotate list to specific item.

**Parameters**

`struct list_head *list`
:   The desired new front of the list.

`struct list_head *head`
:   The head of the list.

**Description**

Rotates list so that **list** becomes the new front of the list.

int list_is_singular(const struct list_head \*head)
:   tests whether a list has just one entry.

**Parameters**

`const struct list_head *head`
:   the list to test.

void list_cut_position(struct list_head \*list, struct list_head \*head, struct list_head \*entry)
:   cut a list into two

**Parameters**

`struct list_head *list`
:   a new list to add all removed entries

`struct list_head *head`
:   a list with entries

`struct list_head *entry`
:   an entry within head, could be the head itself
    and if so we won’t cut the list

**Description**

This helper moves the initial part of **head**, up to and
including **entry**, from **head** to **list**. You should
pass on **entry** an element you know is on **head**. **list**
should be an empty list or a list you do not care about
losing its data.

void list_cut_before(struct list_head \*list, struct list_head \*head, struct list_head \*entry)
:   cut a list into two, before given entry

**Parameters**

`struct list_head *list`
:   a new list to add all removed entries

`struct list_head *head`
:   a list with entries

`struct list_head *entry`
:   an entry within head, could be the head itself

**Description**

This helper moves the initial part of **head**, up to but
excluding **entry**, from **head** to **list**. You should pass
in **entry** an element you know is on **head**. **list** should
be an empty list or a list you do not care about losing
its data.
If **entry** == **head**, all entries on **head** are moved to
**list**.

void list_splice(const struct list_head \*list, struct list_head \*head)
:   join two lists, this is designed for stacks

**Parameters**

`const struct list_head *list`
:   the new list to add.

`struct list_head *head`
:   the place to add it in the first list.

void list_splice_tail(struct list_head \*list, struct list_head \*head)
:   join two lists, each list being a queue

**Parameters**

`struct list_head *list`
:   the new list to add.

`struct list_head *head`
:   the place to add it in the first list.

void list_splice_init(struct list_head \*list, struct list_head \*head)
:   join two lists and reinitialise the emptied list.

**Parameters**

`struct list_head *list`
:   the new list to add.

`struct list_head *head`
:   the place to add it in the first list.

**Description**

The list at **list** is reinitialised

void list_splice_tail_init(struct list_head \*list, struct list_head \*head)
:   join two lists and reinitialise the emptied list

**Parameters**

`struct list_head *list`
:   the new list to add.

`struct list_head *head`
:   the place to add it in the first list.

**Description**

Each of the lists is a queue.
The list at **list** is reinitialised

list_entry

`list_entry (ptr, type, member)`

> get the struct for this entry

**Parameters**

`ptr`
:   the `struct list_head` pointer.

`type`
:   the type of the `struct this` is embedded in.

`member`
:   the name of the list_head within the struct.

list_first_entry

`list_first_entry (ptr, type, member)`

> get the first element from a list

**Parameters**

`ptr`
:   the list head to take the element from.

`type`
:   the type of the `struct this` is embedded in.

`member`
:   the name of the list_head within the struct.

**Description**

Note, that list is expected to be not empty.

list_last_entry

`list_last_entry (ptr, type, member)`

> get the last element from a list

**Parameters**

`ptr`
:   the list head to take the element from.

`type`
:   the type of the `struct this` is embedded in.

`member`
:   the name of the list_head within the struct.

**Description**

Note, that list is expected to be not empty.

list_first_entry_or_null

`list_first_entry_or_null (ptr, type, member)`

> get the first element from a list

**Parameters**

`ptr`
:   the list head to take the element from.

`type`
:   the type of the `struct this` is embedded in.

`member`
:   the name of the list_head within the struct.

**Description**

Note that if the list is empty, it returns NULL.

list_next_entry

`list_next_entry (pos, member)`

> get the next element in list

**Parameters**

`pos`
:   the type \* to cursor

`member`
:   the name of the list_head within the struct.

list_next_entry_circular

`list_next_entry_circular (pos, head, member)`

> get the next element in list

**Parameters**

`pos`
:   the type \* to cursor.

`head`
:   the list head to take the element from.

`member`
:   the name of the list_head within the struct.

**Description**

Wraparound if pos is the last element (return the first element).
Note, that list is expected to be not empty.

list_prev_entry

`list_prev_entry (pos, member)`

> get the prev element in list

**Parameters**

`pos`
:   the type \* to cursor

`member`
:   the name of the list_head within the struct.

list_prev_entry_circular

`list_prev_entry_circular (pos, head, member)`

> get the prev element in list

**Parameters**

`pos`
:   the type \* to cursor.

`head`
:   the list head to take the element from.

`member`
:   the name of the list_head within the struct.

**Description**

Wraparound if pos is the first element (return the last element).
Note, that list is expected to be not empty.

list_for_each

`list_for_each (pos, head)`

> iterate over a list

**Parameters**

`pos`
:   the `struct list_head` to use as a loop cursor.

`head`
:   the head for your list.

list_for_each_rcu

`list_for_each_rcu (pos, head)`

> Iterate over a list in an RCU-safe fashion

**Parameters**

`pos`
:   the `struct list_head` to use as a loop cursor.

`head`
:   the head for your list.

list_for_each_continue

`list_for_each_continue (pos, head)`

> continue iteration over a list

**Parameters**

`pos`
:   the `struct list_head` to use as a loop cursor.

`head`
:   the head for your list.

**Description**

Continue to iterate over a list, continuing after the current position.

list_for_each_prev

`list_for_each_prev (pos, head)`

> iterate over a list backwards

**Parameters**

`pos`
:   the `struct list_head` to use as a loop cursor.

`head`
:   the head for your list.

list_for_each_safe

`list_for_each_safe (pos, n, head)`

> iterate over a list safe against removal of list entry

**Parameters**

`pos`
:   the `struct list_head` to use as a loop cursor.

`n`
:   another `struct list_head` to use as temporary storage

`head`
:   the head for your list.

list_for_each_prev_safe

`list_for_each_prev_safe (pos, n, head)`

> iterate over a list backwards safe against removal of list entry

**Parameters**

`pos`
:   the `struct list_head` to use as a loop cursor.

`n`
:   another `struct list_head` to use as temporary storage

`head`
:   the head for your list.

size_t list_count_nodes(struct list_head \*head)
:   count nodes in the list

**Parameters**

`struct list_head *head`
:   the head for your list.

list_entry_is_head

`list_entry_is_head (pos, head, member)`

> test if the entry points to the head of the list

**Parameters**

`pos`
:   the type \* to cursor

`head`
:   the head for your list.

`member`
:   the name of the list_head within the struct.

list_for_each_entry

`list_for_each_entry (pos, head, member)`

> iterate over list of given type

**Parameters**

`pos`
:   the type \* to use as a loop cursor.

`head`
:   the head for your list.

`member`
:   the name of the list_head within the struct.

list_for_each_entry_reverse

`list_for_each_entry_reverse (pos, head, member)`

> iterate backwards over list of given type.

**Parameters**

`pos`
:   the type \* to use as a loop cursor.

`head`
:   the head for your list.

`member`
:   the name of the list_head within the struct.

list_prepare_entry

`list_prepare_entry (pos, head, member)`

> prepare a pos entry for use in [`list_for_each_entry_continue()`](list.md#c.list_for_each_entry_continue "list_for_each_entry_continue")

**Parameters**

`pos`
:   the type \* to use as a start point

`head`
:   the head of the list

`member`
:   the name of the list_head within the struct.

**Description**

Prepares a pos entry for use as a start point in [`list_for_each_entry_continue()`](list.md#c.list_for_each_entry_continue "list_for_each_entry_continue").

list_for_each_entry_continue

`list_for_each_entry_continue (pos, head, member)`

> continue iteration over list of given type

**Parameters**

`pos`
:   the type \* to use as a loop cursor.

`head`
:   the head for your list.

`member`
:   the name of the list_head within the struct.

**Description**

Continue to iterate over list of given type, continuing after
the current position.

list_for_each_entry_continue_reverse

`list_for_each_entry_continue_reverse (pos, head, member)`

> iterate backwards from the given point

**Parameters**

`pos`
:   the type \* to use as a loop cursor.

`head`
:   the head for your list.

`member`
:   the name of the list_head within the struct.

**Description**

Start to iterate over list of given type backwards, continuing after
the current position.

list_for_each_entry_from

`list_for_each_entry_from (pos, head, member)`

> iterate over list of given type from the current point

**Parameters**

`pos`
:   the type \* to use as a loop cursor.

`head`
:   the head for your list.

`member`
:   the name of the list_head within the struct.

**Description**

Iterate over list of given type, continuing from current position.

list_for_each_entry_from_reverse

`list_for_each_entry_from_reverse (pos, head, member)`

> iterate backwards over list of given type from the current point

**Parameters**

`pos`
:   the type \* to use as a loop cursor.

`head`
:   the head for your list.

`member`
:   the name of the list_head within the struct.

**Description**

Iterate backwards over list of given type, continuing from current position.

list_for_each_entry_safe

`list_for_each_entry_safe (pos, n, head, member)`

> iterate over list of given type safe against removal of list entry

**Parameters**

`pos`
:   the type \* to use as a loop cursor.

`n`
:   another type \* to use as temporary storage

`head`
:   the head for your list.

`member`
:   the name of the list_head within the struct.

list_for_each_entry_safe_continue

`list_for_each_entry_safe_continue (pos, n, head, member)`

> continue list iteration safe against removal

**Parameters**

`pos`
:   the type \* to use as a loop cursor.

`n`
:   another type \* to use as temporary storage

`head`
:   the head for your list.

`member`
:   the name of the list_head within the struct.

**Description**

Iterate over list of given type, continuing after current point,
safe against removal of list entry.

list_for_each_entry_safe_from

`list_for_each_entry_safe_from (pos, n, head, member)`

> iterate over list from current point safe against removal

**Parameters**

`pos`
:   the type \* to use as a loop cursor.

`n`
:   another type \* to use as temporary storage

`head`
:   the head for your list.

`member`
:   the name of the list_head within the struct.

**Description**

Iterate over list of given type from current point, safe against
removal of list entry.

list_for_each_entry_safe_reverse

`list_for_each_entry_safe_reverse (pos, n, head, member)`

> iterate backwards over list safe against removal

**Parameters**

`pos`
:   the type \* to use as a loop cursor.

`n`
:   another type \* to use as temporary storage

`head`
:   the head for your list.

`member`
:   the name of the list_head within the struct.

**Description**

Iterate backwards over list of given type, safe against removal
of list entry.

list_safe_reset_next

`list_safe_reset_next (pos, n, member)`

> reset a stale list_for_each_entry_safe loop

**Parameters**

`pos`
:   the loop cursor used in the list_for_each_entry_safe loop

`n`
:   temporary storage used in list_for_each_entry_safe

`member`
:   the name of the list_head within the struct.

**Description**

list_safe_reset_next is not safe to use in general if the list may be
modified concurrently (eg. the lock is dropped in the loop body). An
exception to this is if the cursor element (pos) is pinned in the list,
and list_safe_reset_next is called after re-taking the lock and before
completing the current iteration of the loop body.

int hlist_unhashed(const struct hlist_node \*h)
:   Has node been removed from list and reinitialized?

**Parameters**

`const struct hlist_node *h`
:   Node to be checked

**Description**

Not that not all removal functions will leave a node in unhashed
state. For example, [`hlist_nulls_del_init_rcu()`](kernel-api.md#c.hlist_nulls_del_init_rcu "hlist_nulls_del_init_rcu") does leave the
node in unhashed state, but `hlist_nulls_del()` does not.

int hlist_unhashed_lockless(const struct hlist_node \*h)
:   Version of hlist_unhashed for lockless use

**Parameters**

`const struct hlist_node *h`
:   Node to be checked

**Description**

This variant of [`hlist_unhashed()`](list.md#c.hlist_unhashed "hlist_unhashed") must be used in lockless contexts
to avoid potential load-tearing. The `READ_ONCE()` is paired with the
various `WRITE_ONCE()` in hlist helpers that are defined below.

int hlist_empty(const struct hlist_head \*h)
:   Is the specified hlist_head structure an empty hlist?

**Parameters**

`const struct hlist_head *h`
:   Structure to check.

void hlist_del(struct hlist_node \*n)
:   Delete the specified hlist_node from its list

**Parameters**

`struct hlist_node *n`
:   Node to delete.

**Description**

Note that this function leaves the node in hashed state. Use
[`hlist_del_init()`](list.md#c.hlist_del_init "hlist_del_init") or similar instead to unhash **n**.

void hlist_del_init(struct hlist_node \*n)
:   Delete the specified hlist_node from its list and initialize

**Parameters**

`struct hlist_node *n`
:   Node to delete.

**Description**

Note that this function leaves the node in unhashed state.

void hlist_add_head(struct hlist_node \*n, struct hlist_head \*h)
:   add a new entry at the beginning of the hlist

**Parameters**

`struct hlist_node *n`
:   new entry to be added

`struct hlist_head *h`
:   hlist head to add it after

**Description**

Insert a new entry after the specified head.
This is good for implementing stacks.

void hlist_add_before(struct hlist_node \*n, struct hlist_node \*next)
:   add a new entry before the one specified

**Parameters**

`struct hlist_node *n`
:   new entry to be added

`struct hlist_node *next`
:   hlist node to add it before, which must be non-NULL

void hlist_add_behind(struct hlist_node \*n, struct hlist_node \*prev)
:   add a new entry after the one specified

**Parameters**

`struct hlist_node *n`
:   new entry to be added

`struct hlist_node *prev`
:   hlist node to add it after, which must be non-NULL

void hlist_add_fake(struct hlist_node \*n)
:   create a fake hlist consisting of a single headless node

**Parameters**

`struct hlist_node *n`
:   Node to make a fake list out of

**Description**

This makes **n** appear to be its own predecessor on a headless hlist.
The point of this is to allow things like [`hlist_del()`](list.md#c.hlist_del "hlist_del") to work correctly
in cases where there is no list.

bool hlist_fake(struct hlist_node \*h)
:   Is this node a fake hlist?

**Parameters**

`struct hlist_node *h`
:   Node to check for being a self-referential fake hlist.

bool hlist_is_singular_node(struct hlist_node \*n, struct hlist_head \*h)
:   is node the only element of the specified hlist?

**Parameters**

`struct hlist_node *n`
:   Node to check for singularity.

`struct hlist_head *h`
:   Header for potentially singular list.

**Description**

Check whether the node is the only node of the head without
accessing head, thus avoiding unnecessary cache misses.

void hlist_move_list(struct hlist_head \*old, struct hlist_head \*new)
:   Move an hlist

**Parameters**

`struct hlist_head *old`
:   hlist_head for old list.

`struct hlist_head *new`
:   hlist_head for new list.

**Description**

Move a list from one list head to another. Fixup the pprev
reference of the first entry if it exists.

void hlist_splice_init(struct hlist_head \*from, struct hlist_node \*last, struct hlist_head \*to)
:   move all entries from one list to another

**Parameters**

`struct hlist_head *from`
:   hlist_head from which entries will be moved

`struct hlist_node *last`
:   last entry on the **from** list

`struct hlist_head *to`
:   hlist_head to which entries will be moved

**Description**

**to** can be empty, **from** must contain at least **last**.

hlist_for_each_entry

`hlist_for_each_entry (pos, head, member)`

> iterate over list of given type

**Parameters**

`pos`
:   the type \* to use as a loop cursor.

`head`
:   the head for your list.

`member`
:   the name of the hlist_node within the struct.

hlist_for_each_entry_continue

`hlist_for_each_entry_continue (pos, member)`

> iterate over a hlist continuing after current point

**Parameters**

`pos`
:   the type \* to use as a loop cursor.

`member`
:   the name of the hlist_node within the struct.

hlist_for_each_entry_from

`hlist_for_each_entry_from (pos, member)`

> iterate over a hlist continuing from current point

**Parameters**

`pos`
:   the type \* to use as a loop cursor.

`member`
:   the name of the hlist_node within the struct.

hlist_for_each_entry_safe

`hlist_for_each_entry_safe (pos, n, head, member)`

> iterate over list of given type safe against removal of list entry

**Parameters**

`pos`
:   the type \* to use as a loop cursor.

`n`
:   a `struct hlist_node` to use as temporary storage

`head`
:   the head for your list.

`member`
:   the name of the hlist_node within the struct.

size_t hlist_count_nodes(struct hlist_head \*head)
:   count nodes in the hlist

**Parameters**

`struct hlist_head *head`
:   the head for your hlist.
