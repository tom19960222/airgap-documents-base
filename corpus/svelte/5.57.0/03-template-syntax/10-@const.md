---
collection: svelte
version: "5.57.0"
title: "{@const ...}"
source_url: https://github.com/sveltejs/svelte/blob/svelte@5.57.0/documentation/docs/03-template-syntax/10-@const.md
fetched_at: 2026-08-29T01:26:56+02:00
---
> [!NOTE] `{@const x = y}` is legacy syntax — use [`{const x = $derived(y)}`](declaration-tags) instead

The `{@const ...}` tag defines a local constant.

```svelte
{#each boxes as box}
	{@const area = box.width * box.height}
	{box.width} * {box.height} = {area}
{/each}
```

`{@const}` is only allowed as an immediate child of a block — `{#if ...}`, `{#each ...}`, `{#snippet ...}` and so on — a `<Component />` or a `<svelte:boundary>`.
