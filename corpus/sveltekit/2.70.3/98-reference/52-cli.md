---
collection: sveltekit
version: "2.70.3"
title: "Command Line Interface"
source_url: https://github.com/sveltejs/kit/blob/@sveltejs/kit@2.70.3/documentation/docs/98-reference/52-cli.md
fetched_at: 2026-08-18T10:57:39-04:00
---
SvelteKit projects use [Vite](https://vitejs.dev), meaning you'll mostly use its CLI (albeit via `npm run dev/build/preview` scripts):

- `vite dev` — start a development server
- `vite build` — build a production version of your app
- `vite preview` — run the production version locally

However SvelteKit includes its own CLI for initialising your project:

## svelte-kit sync

`svelte-kit sync` creates the `tsconfig.json` and all generated types (which you can import as `./$types` inside routing files) for your project. When you create a new project, it is listed as the `prepare` script and will be run automatically as part of the npm lifecycle, so you should not ordinarily have to run this command.
