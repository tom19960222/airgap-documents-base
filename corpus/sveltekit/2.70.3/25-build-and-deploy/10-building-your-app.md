---
collection: sveltekit
version: "2.70.3"
title: "Building your app"
source_url: https://github.com/sveltejs/kit/blob/@sveltejs/kit@2.70.3/documentation/docs/25-build-and-deploy/10-building-your-app.md
fetched_at: 2026-08-18T10:57:39-04:00
---
Building a SvelteKit app happens in two stages, which both happen when you run `vite build` (usually via `npm run build`).

Firstly, Vite creates an optimized production build of your server code, your browser code, and your service worker (if you have one). [Prerendering](page-options#prerender) is executed at this stage, if appropriate.

Secondly, an _adapter_ takes this production build and tunes it for your target environment — more on this on the following pages.

## During the build

SvelteKit will load your `+page/layout(.server).js` files (and all files they import) for analysis during the build. Any code that should _not_ be executed at this stage must check that `building` from [`$app/environment`]($app-environment) is `false`:

```js
+++import { building } from '$app/environment';+++
import { initialiseDatabase } from '$lib/server/database';

+++if (!building) {+++
	initialiseDatabase();
+++}+++

export function load() {
	// ...
}
```

## Preview your app

After building, you can view your production build locally with `vite preview` (via `npm run preview`). Note that this will run the app in Node, and so is not a perfect reproduction of your deployed app — adapter-specific adjustments like the [`platform` object](adapters#Platform-specific-context) do not apply to previews.
