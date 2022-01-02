# **Next.js**

## Why I'm learning Next.js.(Remix is awesome as well, take a try)
To build a complete web application with React from scratch, there are many details to consider:
1. Code has to be bundled using a bundler like **`webpack`**(a new choice is **`Vite`**) and transformed using a compiler like **`Babel`**.
2. Code splitting for production optimization.
3. Statically pre-render some pages for performance and SEO. Also want to use some server-side rendering or client-side rendering.
4. Need some server-side code for data store.


### What does `Next.js` provide
1. Page-based routing system(Check [`Remix`](https://remix.run/), it does something similar). With support for dynamic routes.
2. Pre-rendreing, both [`static generation`](https://nextjs.org/docs/basic-features/pages#static-generation-recommended) and [`server side rendering`](https://nextjs.org/docs/basic-features/pages#server-side-rendering) are supported on per-page basis.
3. Automatic code-splitting for faster page loads.
4. Client-side routing with optimized prefetching.
5. Built-in CSS and Sass support, and support any CSS-in-JS library.
6. Dev env with [Fast refresh](https://nextjs.org/docs/basic-features/fast-refresh) support.

> - Client-side navigation
The `Link` component enables client-side navigation between two pages in the same Next.js app.
Client-side navigation means that the page transition happens using JavaScript, which is faster than the default navigation done by the browser.

> - Code splitting and prefetching
**Next.js** does the code splitting automatically, so each page only loads what's necessary for that page. That means when the homepage is rendered, the code for other page is not served initially. This ensures that the first page loads quickly even if you have hundreds of pages.
Only loading the code for the page also means that the pages become isolated. If a certain page throws an error, the rest of the application would still work.

Further more, in a production build of Next.js, whenever `Link` components appear in the browser's viewport, Next.js automatically prefetches the code for the linked page in the background. By the time you click tthe link, the code for the destination page will already be loaded in the background, and the page transition will be near-instant.

* If you are using an external page outside of the Next.js app, use an `<a>` tag without `Link`.

> - File-based routing
