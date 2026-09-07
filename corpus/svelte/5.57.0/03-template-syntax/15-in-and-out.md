---
collection: svelte
version: "5.57.0"
title: "in: and out:"
source_url: https://github.com/sveltejs/svelte/blob/svelte@5.57.0/documentation/docs/03-template-syntax/15-in-and-out.md
fetched_at: 2026-08-29T01:26:56+02:00
---
The `in:` and `out:` directives are identical to [`transition:`](transition), except that the resulting transitions are not bidirectional — an `in` transition will continue to 'play' alongside the `out` transition, rather than reversing, if the block is outroed while the transition is in progress. If an out transition is aborted, transitions will restart from scratch.

```svelte
<script>
  import { fade, fly } from 'svelte/transition';

  let visible = $state(false);
</script>

<label>
  <input type="checkbox" bind:checked={visible}>
  visible
</label>

{#if visible}
	<div in:fly={{ y: 200 }} out:fade>flies in, fades out</div>
{/if}
```
