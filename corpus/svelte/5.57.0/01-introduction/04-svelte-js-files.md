---
collection: svelte
version: "5.57.0"
title: ".svelte.js and .svelte.ts files"
source_url: https://github.com/sveltejs/svelte/blob/svelte@5.57.0/documentation/docs/01-introduction/04-svelte-js-files.md
fetched_at: 2026-08-29T01:26:56+02:00
---
Besides `.svelte` files, Svelte also operates on `.svelte.js` and `.svelte.ts` files.

These behave like any other `.js` or `.ts` module, except that you can use runes. This is useful for creating reusable reactive logic, or sharing reactive state across your app (though note that you [cannot export reassigned state]($state#Passing-state-across-modules)).

> [!LEGACY]
> This is a concept that didn't exist prior to Svelte 5
