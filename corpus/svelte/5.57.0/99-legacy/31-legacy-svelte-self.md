---
collection: svelte
version: "5.57.0"
title: "<svelte:self>"
source_url: https://github.com/sveltejs/svelte/blob/svelte@5.57.0/documentation/docs/99-legacy/31-legacy-svelte-self.md
fetched_at: 2026-08-29T01:26:56+02:00
---
The `<svelte:self>` element allows a component to include itself, recursively.

It cannot appear at the top level of your markup; it must be inside an if or each block or passed to a component's slot to prevent an infinite loop.

```svelte
<script>
	export let count;
</script>

{#if count > 0}
	<p>counting down... {count}</p>
	<svelte:self count={count - 1} />
{:else}
	<p>lift-off!</p>
{/if}
```

> [!NOTE]
> This concept is obsolete, as components can import themselves:
> ```svelte
> <!--- file: App.svelte --->
> <script>
> 	import Self from './App.svelte'
> 	export let count;
> </script>
>
> {#if count > 0}
> 	<p>counting down... {count}</p>
> 	<Self count={count - 1} />
> {:else}
> 	<p>lift-off!</p>
> {/if}
> ```
