---
collection: svelte
version: "5.57.0"
title: "{#key ...}"
source_url: https://github.com/sveltejs/svelte/blob/svelte@5.57.0/documentation/docs/03-template-syntax/04-key.md
fetched_at: 2026-08-29T01:26:56+02:00
---
```svelte
<!--- copy: false  --->
{#key expression}...{/key}
```

Key blocks destroy and recreate their contents when the value of an expression changes. When used around components, this will cause them to be reinstantiated and reinitialised:

```svelte
{#key value}
	<Component />
{/key}
```

It's also useful if you want a transition to play whenever a value changes:

```svelte
{#key value}
	<div transition:fade>{value}</div>
{/key}
```
