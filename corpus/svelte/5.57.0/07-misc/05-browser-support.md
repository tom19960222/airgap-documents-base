---
collection: svelte
version: "5.57.0"
title: "Browser support"
source_url: https://github.com/sveltejs/svelte/blob/svelte@5.57.0/documentation/docs/07-misc/05-browser-support.md
fetched_at: 2026-08-29T01:26:56+02:00
---
The table below shows the minimum browser versions Svelte is expected to work in, derived from the browser APIs used by Svelte's internal code.

@include .generated/browser-support.md

This table only covers Svelte itself. It does not include [SvelteKit](/docs/kit), other Svelte libraries, or your own code.

## Exceptions

A few Svelte features require a higher minimum browser version. You'll only need to take the following table into consideration if you use these specific features.

@include .generated/browser-support-features.md
