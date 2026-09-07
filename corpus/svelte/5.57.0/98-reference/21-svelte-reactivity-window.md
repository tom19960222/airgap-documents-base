---
collection: svelte
version: "5.57.0"
title: "svelte/reactivity/window"
source_url: https://github.com/sveltejs/svelte/blob/svelte@5.57.0/documentation/docs/98-reference/21-svelte-reactivity-window.md
fetched_at: 2026-08-29T01:26:56+02:00
---
This module exports reactive versions of various `window` values, each of which has a reactive `current` property that you can reference in reactive contexts (templates, [deriveds]($derived) and [effects]($effect)) without using [`<svelte:window>`](svelte-window) bindings or manually creating your own event listeners.

```svelte
<script>
	import { innerWidth, innerHeight } from 'svelte/reactivity/window';
</script>

<p>{innerWidth.current}x{innerHeight.current}</p>
```

> MODULE: svelte/reactivity/window
