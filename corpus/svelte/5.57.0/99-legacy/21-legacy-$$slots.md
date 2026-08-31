---
collection: svelte
version: "5.57.0"
title: "$$slots"
source_url: https://github.com/sveltejs/svelte/blob/svelte@5.57.0/documentation/docs/99-legacy/21-legacy-$$slots.md
fetched_at: 2026-08-29T01:26:56+02:00
---
In runes mode, we know which [snippets](snippet) were provided to a component, as they're just normal props.

In legacy mode, the way to know if content was provided for a given slot is with the `$$slots` object, whose keys are the names of the slots passed into the component by the parent.

```svelte
<!--- file: Card.svelte --->
<div>
	<slot name="title" />
	{#if $$slots.description}
		<!-- This <hr> and slot will render only if `slot="description"` is provided. -->
		<hr />
		<slot name="description" />
	{/if}
</div>
```

```svelte
<!--- file: App.svelte --->
<Card>
	<h1 slot="title">Blog Post Title</h1>
	<!-- No slot named "description" was provided so the optional slot will not be rendered. -->
</Card>
```
