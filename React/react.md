## **React**

Based on some previous experience, I've had some knowledge and experiences using React. But what I have noted is that React is envolving and is absorbing more and more concepts. Some of the core areas I should focus on is Redux, TypeScript, Hooks and testing with Jest.

### **Lifecycle**
> Mounting
    When an instance of a component is being created and inserted into the DOM.
> - constructor()
> - static getDerivedStateFromProps()
> - render()
> - componentDidMount()

> Updating 
    Changes to props and state can cause an updating.
> - static getDerivedStateFromProps()
> - shouldComponentUpdate()
> - render()
> - getSnapshotBeforeUpdate()
> - componentDidUpdate()

> Unmounting
> - componentWillUnmount()

```JavaScript
static getDerivedStateFromProps(props, state)
getSnapshotBeforeUpdate(prevProps, prevState)
```
> - componentDidMount is invoked immediately after a component is mounted. If we need to load data from an endpoint, this is the place to instantiate the network request. Also, this is where to set up any subscriptions. And if we do that, we need to unsubscribe in componentWillUnmount()
> - getDerivedStateFromProps is invoked before calling the render method, both on initial mount and on subsequent updates. It should return an object to update the state, or null to update nothing.
> - getSnapshotBeforeUpdate is invoked before the most recently rendered output is committed to DOM. It enables components to capture some information from the DOM before it is potentially changed. Any value returned by this lifecycle method will be passed as a parameter to componentDidUpdate().

### **Hooks**
Hooks are functions that let us hook into React state and lifecycle features from functional components.

### **Lazy-loading**
React Suspense is a `React Component` that suspends a component being rendered until a certaion condition has been met and will display a fallback option. **React Suspense only works with dynamic importing(Lazy loading)**.

### Since React 17, **import React is not needed to render JSX.**
