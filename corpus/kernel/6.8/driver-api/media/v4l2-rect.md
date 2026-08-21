---
collection: kernel
version: "6.8"
title: "2.25. V4L2 rect helper functions"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/media/v4l2-rect.html
fetched_at: 2026-08-21T03:41:20+00:00
---
# 2.25. V4L2 rect helper functions

void v4l2_rect_set_size_to(struct [v4l2_rect](../../userspace-api/media/v4l/dev-overlay.md#c.v4l2_rect "v4l2_rect") \*r, const struct [v4l2_rect](../../userspace-api/media/v4l/dev-overlay.md#c.v4l2_rect "v4l2_rect") \*size)
:   copy the width/height values.

**Parameters**

`struct v4l2_rect *r`
:   rect whose width and height fields will be set

`const struct v4l2_rect *size`
:   rect containing the width and height fields you need.

void v4l2_rect_set_min_size(struct [v4l2_rect](../../userspace-api/media/v4l/dev-overlay.md#c.v4l2_rect "v4l2_rect") \*r, const struct [v4l2_rect](../../userspace-api/media/v4l/dev-overlay.md#c.v4l2_rect "v4l2_rect") \*min_size)
:   width and height of r should be >= min_size.

**Parameters**

`struct v4l2_rect *r`
:   rect whose width and height will be modified

`const struct v4l2_rect *min_size`
:   rect containing the minimal width and height

void v4l2_rect_set_max_size(struct [v4l2_rect](../../userspace-api/media/v4l/dev-overlay.md#c.v4l2_rect "v4l2_rect") \*r, const struct [v4l2_rect](../../userspace-api/media/v4l/dev-overlay.md#c.v4l2_rect "v4l2_rect") \*max_size)
:   width and height of r should be <= max_size

**Parameters**

`struct v4l2_rect *r`
:   rect whose width and height will be modified

`const struct v4l2_rect *max_size`
:   rect containing the maximum width and height

void v4l2_rect_map_inside(struct [v4l2_rect](../../userspace-api/media/v4l/dev-overlay.md#c.v4l2_rect "v4l2_rect") \*r, const struct [v4l2_rect](../../userspace-api/media/v4l/dev-overlay.md#c.v4l2_rect "v4l2_rect") \*boundary)
:   r should be inside boundary.

**Parameters**

`struct v4l2_rect *r`
:   rect that will be modified

`const struct v4l2_rect *boundary`
:   rect containing the boundary for **r**

bool v4l2_rect_same_size(const struct [v4l2_rect](../../userspace-api/media/v4l/dev-overlay.md#c.v4l2_rect "v4l2_rect") \*r1, const struct [v4l2_rect](../../userspace-api/media/v4l/dev-overlay.md#c.v4l2_rect "v4l2_rect") \*r2)
:   return true if r1 has the same size as r2

**Parameters**

`const struct v4l2_rect *r1`
:   rectangle.

`const struct v4l2_rect *r2`
:   rectangle.

**Description**

Return true if both rectangles have the same size.

bool v4l2_rect_same_position(const struct [v4l2_rect](../../userspace-api/media/v4l/dev-overlay.md#c.v4l2_rect "v4l2_rect") \*r1, const struct [v4l2_rect](../../userspace-api/media/v4l/dev-overlay.md#c.v4l2_rect "v4l2_rect") \*r2)
:   return true if r1 has the same position as r2

**Parameters**

`const struct v4l2_rect *r1`
:   rectangle.

`const struct v4l2_rect *r2`
:   rectangle.

**Description**

Return true if both rectangles have the same position

bool v4l2_rect_equal(const struct [v4l2_rect](../../userspace-api/media/v4l/dev-overlay.md#c.v4l2_rect "v4l2_rect") \*r1, const struct [v4l2_rect](../../userspace-api/media/v4l/dev-overlay.md#c.v4l2_rect "v4l2_rect") \*r2)
:   return true if r1 equals r2

**Parameters**

`const struct v4l2_rect *r1`
:   rectangle.

`const struct v4l2_rect *r2`
:   rectangle.

**Description**

Return true if both rectangles have the same size and position.

void v4l2_rect_intersect(struct [v4l2_rect](../../userspace-api/media/v4l/dev-overlay.md#c.v4l2_rect "v4l2_rect") \*r, const struct [v4l2_rect](../../userspace-api/media/v4l/dev-overlay.md#c.v4l2_rect "v4l2_rect") \*r1, const struct [v4l2_rect](../../userspace-api/media/v4l/dev-overlay.md#c.v4l2_rect "v4l2_rect") \*r2)
:   calculate the intersection of two rects.

**Parameters**

`struct v4l2_rect *r`
:   intersection of **r1** and **r2**.

`const struct v4l2_rect *r1`
:   rectangle.

`const struct v4l2_rect *r2`
:   rectangle.

void v4l2_rect_scale(struct [v4l2_rect](../../userspace-api/media/v4l/dev-overlay.md#c.v4l2_rect "v4l2_rect") \*r, const struct [v4l2_rect](../../userspace-api/media/v4l/dev-overlay.md#c.v4l2_rect "v4l2_rect") \*from, const struct [v4l2_rect](../../userspace-api/media/v4l/dev-overlay.md#c.v4l2_rect "v4l2_rect") \*to)
:   scale rect r by to/from

**Parameters**

`struct v4l2_rect *r`
:   rect to be scaled.

`const struct v4l2_rect *from`
:   from rectangle.

`const struct v4l2_rect *to`
:   to rectangle.

**Description**

This scales rectangle **r** horizontally by **to->width** / **from->width** and
vertically by **to->height** / **from->height**.

Typically **r** is a rectangle inside **from** and you want the rectangle as
it would appear after scaling **from** to **to**. So the resulting **r** will
be the scaled rectangle inside **to**.

bool v4l2_rect_overlap(const struct [v4l2_rect](../../userspace-api/media/v4l/dev-overlay.md#c.v4l2_rect "v4l2_rect") \*r1, const struct [v4l2_rect](../../userspace-api/media/v4l/dev-overlay.md#c.v4l2_rect "v4l2_rect") \*r2)
:   do r1 and r2 overlap?

**Parameters**

`const struct v4l2_rect *r1`
:   rectangle.

`const struct v4l2_rect *r2`
:   rectangle.

**Description**

Returns true if **r1** and **r2** overlap.

bool v4l2_rect_enclosed(struct [v4l2_rect](../../userspace-api/media/v4l/dev-overlay.md#c.v4l2_rect "v4l2_rect") \*r1, struct [v4l2_rect](../../userspace-api/media/v4l/dev-overlay.md#c.v4l2_rect "v4l2_rect") \*r2)
:   is r1 enclosed in r2?

**Parameters**

`struct v4l2_rect *r1`
:   rectangle.

`struct v4l2_rect *r2`
:   rectangle.

**Description**

Returns true if **r1** is enclosed in **r2**.
