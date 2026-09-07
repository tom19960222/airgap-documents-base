---
collection: svelte
version: "5.57.0"
title: "<svelte:document>"
source_url: https://github.com/sveltejs/svelte/blob/svelte@5.57.0/documentation/docs/05-special-elements/03-svelte-document.md
fetched_at: 2026-08-29T01:26:56+02:00
---
```svelte
<svelte:document onevent={handler} />
```

```svelte
<svelte:document bind:prop={value} />
```

Similarly to `<svelte:window>`, this element allows you to add listeners to events on `document`, such as `visibilitychange`, which don't fire on `window`. It also lets you use [attachments](@attach) on `document`.

As with `<svelte:window>`, this element may only appear the top level of your component and must never be inside a block or element.

```svelte
<svelte:document onvisibilitychange={handleVisibilityChange} {@attach someAttachment} />
```

You can also bind to the following properties:

- `activeElement`
- `fullscreenElement`
- `pointerLockElement`
- `visibilityState`

All are readonly.
