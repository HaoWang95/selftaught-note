## **Testing React**
Based on previous understanding of Node.js, the syntax of testing a React component should be similiar to testing Node.js code. But in Node.js, unit testing is more about testing endpoint and middlewares, while testing might focus more on React components.

Generally, React testing can be divided into two categories:
> - Rendering component trees
> - Running a complete app

React official documentation recommends Jest and React Testing Library.
> - Jest allows us access DOM via jsdom. Jest provides powerful features like mocking modules and timers to have more control over how the code executes.
> - React Testing Library provides a set of helpers that let us test React components without relying on their implementation details.

### **Testing patterns**
* Setup/Teardown
* act()
* Rendering
* Data Fetching
* Mocking Modules
* Events
* Timers
* Snapshot Testing
* Multiple Renderers