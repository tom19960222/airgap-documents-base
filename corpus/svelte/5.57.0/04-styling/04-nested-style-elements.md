---
collection: svelte
version: "5.57.0"
title: "Nested <style> elements"
source_url: https://github.com/sveltejs/svelte/blob/svelte@5.57.0/documentation/docs/04-styling/04-nested-style-elements.md
fetched_at: 2026-08-29T01:26:56+02:00
---
There can only be one top-level `<style>` tag per component.

However, it is possible to have a `<style>` tag nested inside other elements or logic blocks.

In that case, the `<style>` tag will be inserted as-is into the DOM; no scoping or processing will be done on the `<style>` tag.

```svelte
<div>
	<style>
		/* this style tag will be inserted as-is */
		div {
			/* this will apply to all `<div>` elements in the DOM */
			color: red;
		}
	</style>
</div>
```
