# Code splitting and lazy loading
The react code-splitting and lazy loading is usually associated with **react router**. It is required to use **React.Suspense** to render the component/page and provide a **fallback element** to handle the fallback.

# For react-reudx and some common typescript issues
**`React redux`** has its type definitions in a separate **@types/react-redux** typedefs package on NPM. In addition to typing the library funcions, the type also exports some helpers to make it easier to write typesafe interfaces between the Redux store and React components.

RTK Redux Toolkit is already writting in TypeScript, so its TS type definitions are built-in.

# Upgrading a React project from JavaScript to TypeScript
- Module not found: Error: Can't resolve './App' in the src folder
A temporary solution is in index.js
```JavaScript
import App from './App.tsx' // explicitly define the import type
```

# Know how to create app with templates.
There are many **tempaltes available** to create a react app. My current way is still simply create a react app and then add dependencies step by step. For example, another good way to start might be create a project with `--template typescript-redux`
- When creating a new project with tempalte of TypeScript, it will automatically create a `tsconfig.json` to manage the TypeScript behavior.

# redux-toolkit cheat-sheet
This blog is quite helpful to have a quick tour of the redux-toolkit.
- https://blog.shancw.net/2021/10/19/redux-toolkit-cheat-sheet/

# A recommended approach to structure Redux features

# When creating a store using Redux with **configureStore()**
- A default reducer must be provided


# The error of **Module not found: Error: Can't resolve \node_modules\rc-field-form\node_modules\@babel\runtime\helpers\esm Did you mean 'getPrototypeOf.js?'** (This is the error after updating to the latest react-scripts).
This error also comes with **(BREAKING CHANGE: The request `filename` failed to resolve only because it was resolved as fully specified (probably because the origin is strict EcmaScript Module, eg. a module with JavaScript minetype, a '.mjs' or a '.js' file where package.json contains "type": "module"). The extension in the request is mandatory for it to be fully specified. Add the extension to the request)**

- There's actaully not a developer's issue with this error. There are some dependencies error not fully resolved after **creating or updating a project with the newest version cra create-react-app which uses the newest version of webpack and create-react-app**.

1. Delete `node_modules` and `yarn.lock` permanently.
2. yarn install or npm i to reinstall every dependencies

## React-router, difference between `NavLink` and `Link`
The Link component is used to navigate the different routes on the site. But NavLink is used to add the style attributes to the active routes.