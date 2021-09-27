## HOC Higher-order components

Higher-order component is an advanced technique in React for reusing component logic. HOCs are not part of the React API. They are a pattern that emerges from React's compositional nature. A higher-order component is a function that takes a component and returns a new component. A normal component transforms props into UI, a higher-order component transforms component into another component.

A higher-order component does not modify the input component, nor does it uses inheritance to copy its behavior. A hoc composes the original component by wrapping it in a container component. A hoc is a pure function with zero side-effects.

## Code-splitting
As app grows, bundle will grow too. We need to keep an eye on the code we are including in the bundle so that it is not so large. Code-splitting is a feature supported by bundlers like webpack, rollup and browserify which can create multiple bundles that can be dynamically loaded at runtime.
Code-splitting can help to 'lazy-load' things that are just needed by users, which can dramatically improve the performance of the app. While the overall amount of code in the app is not reduced, just by avoiding loading code that the user may never need, and reduced the amount of code needed during the initial load.
**The best approach to introduce code-splitting into your app is through the dynamic import() syntax.**
```JavaScript
import ('something').then(
    something => {
        //do something
    }
)
```
When WebPack comes across this syntax, it automatically starts code-splitting the app.
*React.lazy functions lets you render a dynamic import as a regular component.* React.lazy takes a function that must call a dynamic import(). This must return a promise which resolves to a module with a default export containing a React component. The lazy component should then be rendered inside a Suspense component, which allows us to show shome fallback content while we're waiting for the lazy component to load.
```JavaScript
const something = React.lazy(() => import('something'));
function MyComponent() {
  return (
    <div>
      <Suspense fallback={<div>Loading...</div>}>
        <something />
      </Suspense>
    </div>
  );
}
```
**React.lazy and Suspense are not yet available for server-side rendering. When code-splitting a server rendered app, use Loadable Components.**

### Router-based code splitting
**A good place to start with code-splitting is routes.** 

## Context
Context provides a way to pass data through the component tree without having to pass props down manually at every level.

## **Strict Mode**
StrictMode is a tool for highlighting potential problems in an application. StrictMode does not render any visible UI. It activates additional checks and warnings for its descendants.
Strict mode checks are run in development mode only, it does not impact the production build.
