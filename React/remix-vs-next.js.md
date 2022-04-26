# Remix VS Next.js
Next.js is one of the most popular frameworks used for server-side rendering. Remix is a ultimate solution published by the same team that creates React Router.

## Routing
The similarities between Remix and Next.js are routings. Both frameworks follow file-based routing system and support nested routing and dynamic route segments.

## Data Loading on Next.js
* Server-side rending at runtime
* Server-side rendering at build time
* Client-side rendering at runtime
* A mix of server-side runtime, client-side and server-side build time and client-side runtime.
In Next.js, developers can use all the above techniques with different functionality to export data from a page.
We can use **`getServerSideProps`** to load the data on the server side at runtime while **`getStaticProps`** and **getStaticPath** can be used to load the data from the server-side at build time.
>- getServerSideProps. Next.js will pre-render this page each request using the data returned by `getServerSideProps`.
```JavaScript
export async function getServerSideProps(context){
    return{
        props: {}
    }
}
```
>- getStaticPaths. Next.js will statically pre-render all the paths specified by `getStaticPaths`. `getStaticPaths` must be used with `getStaticProps`.
```JavaScript
export async function getStaticPaths(){
    return {
        paths: [
            {params: {...}}
        ],
        fallback: true // false or 'blocking'
    }
}
```
>- getSaticProps. Next.js will pre-render this page at build time using the props returned by `getStaticProps`

## Data Loading on Remix
In Remix, there are only two methods to load the data. You can use the server-side at runtime and the client-side at runtime to render the data.
We need to export a **`loader`** function from a route to load data from the server-side and `useFetcher` hook in Remix to load data on the client-side.

Next.js supports server-side rendering(SSR), static site generation(SSG), incremental site generation(ISG) and client-side rendering(CSR).
On the other hand, Remix only supports server-side rendering(SSR) and client-side rendering(CSR).

## Sessions and Cookies
There are no built-in functions to interact with cookies or sessions in Next.js. But we can use popular libraries like Cookie.js or NextAuth.js to perform user authentication and save session data into a cookie.
Remix support for cookies and sessions out of the box.
```JavaScript
import { createCookie } from "remix";

const cookie = createCookie("cookie-name", {
  expires: new Date(Date.now() + 60),
  httpOnly: true,
  maxAge: 60,
  path: "/",
  sameSite: "lax",
  secrets: ["s3cret1"],
  secure: true
});
```
