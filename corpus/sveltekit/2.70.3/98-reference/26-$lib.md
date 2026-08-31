---
collection: sveltekit
version: "2.70.3"
title: "$lib"
source_url: https://github.com/sveltejs/kit/blob/@sveltejs/kit@2.70.3/documentation/docs/98-reference/26-$lib.md
fetched_at: 2026-08-18T10:57:39-04:00
---
SvelteKit automatically makes files under `src/lib` available using the `$lib` import alias.

```svelte
<!--- file: src/lib/Component.svelte --->
A reusable component
```

```svelte
<!--- file: src/routes/+page.svelte --->
<script>
	import Component from '$lib/Component.svelte';
</script>

<Component />
```
