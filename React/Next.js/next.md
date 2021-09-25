# **Next.js**

> - Client-side navigation
The `Link` component enables client-side navigation between two pages in the same Next.js app.
Client-side navigation means that the page transition happens using JavaScript, which is faster than the default navigation done by the browser.

> - Code splitting and prefetching
**Next.js** does the code splitting automatically, so each page only loads what's necessary for that page. That means when the homepage is rendered, the code for other page is not served initially. This ensures that the first page loads quickly even if you have hundreds of pages.
Only loading the code for the page also means that the pages become isolated. If a certain page throws an error, the rest of the application would still work.

Further more, in a production build of Next.js, whenever `Link` components appear in the browser's viewport, Next.js automatically prefetches the code for the linked page in the background. By the time you click tthe link, the code for the destination page will already be loaded in the background, and the page transition will be near-instant.

* If you are using an external page outside of the Next.js app, use an `<a>` tag without `Link`.

> - File-based routing
