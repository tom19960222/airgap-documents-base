---
collection: svelte
version: "5.57.0"
title: "<svelte:body>"
source_url: https://github.com/sveltejs/svelte/blob/svelte@5.57.0/documentation/docs/05-special-elements/04-svelte-body.md
fetched_at: 2026-08-29T01:26:56+02:00
---
```svelte
<svelte:body onevent={handler} />
```

Similarly to `<svelte:window>`, this element allows you to add listeners to events on `document.body`, such as `mouseenter` and `mouseleave`, which don't fire on `window`. It also lets you use [actions](use) on the `<body>` element.

As with `<svelte:window>` and `<svelte:document>`, this element may only appear at the top level of your component and must never be inside a block or element.

```svelte
<svelte:body onmouseenter={handleMouseenter} onmouseleave={handleMouseleave} use:someAction />
```
