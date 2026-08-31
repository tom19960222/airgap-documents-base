---
collection: svelte
version: "5.57.0"
title: "<svelte:head>"
source_url: https://github.com/sveltejs/svelte/blob/svelte@5.57.0/documentation/docs/05-special-elements/05-svelte-head.md
fetched_at: 2026-08-29T01:26:56+02:00
---
```svelte
<svelte:head>...</svelte:head>
```

This element makes it possible to insert elements into `document.head`. During server-side rendering, `head` content is exposed separately to the main `body` content.

As with `<svelte:window>`, `<svelte:document>` and `<svelte:body>`, this element may only appear at the top level of your component and must never be inside a block or element.

```svelte
<svelte:head>
	<title>Hello world!</title>
	<meta name="description" content="This is where the description goes for SEO" />
</svelte:head>
```
