## **Testing React**
Based on previous understanding of Node.js, the syntax of testing a React component should be similiar to testing Node.js code. But in Node.js, unit testing is more about testing endpoint and middlewares, while testing in React might focus more on components.

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

#### SetUp/Teardown
Use a pair of *beforeEach* and *afterEach* blocks. beforeEach render React tree to a DOM element that's attached to document. afterEach cleans up and unmount the tree from the document.

#### act()
A helper from react-dom/test-utils, to make sure all updates related to these units have been processed and applied to the DOM before you make any assertions.
```JavaScript
act(() => {
    // render components
});
// make assertions
```
#### Rendering
Test whether a component renders correctly for given props.

#### Data Fetching
Mock requests with dummy data. 

#### Mocking Modules
Mocking out some modules with self-defined or randomly-generated replacements if these modules do not work well inside testing environment or may not be as essential to the test itself.

#### Events
Dispatching events on elements

#### Timers
Timer-based functions to schedule work in the future. 

#### Snapshot testing
Save snapshots of data with toMatchSnapshot/toMatchInlineSnapshot. We save the rendered component output and ensure that a change to it has to be explicitly committed as a change to the snapshot.