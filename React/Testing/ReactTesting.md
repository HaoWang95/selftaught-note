Before stepping into React Testing, there are some common patterns of writing testing code in both backend and frontend applications
* Test Runner
  * Test runner is a tool that picks up files that contains unit tests, executes them and writes the test results to console or log files. **Mocha** and **Jasmine** are two popular test runners used within the JavaScript community.
* Assertion Library
  * It verifies the result of test. **Chai**, **Should** and **Expect** are examples of JavaScript assertion libraries.
* Mocks
  * Used in unit testing a component. A component under test has many dependencies. These dependencies are usually replaced by stubs or mocks. Stubs simulate a dependent object. Mocks offer an additional feature over stubs. With mocks, tests can be written to verify if the component under test has called the mocks as expected.
* Mocking library
  * Facilitates the usage of mocks in unit testing.

# React Testing Library
React Testing Library is opinionated, as it provides a philosophy to test applications.
* Test the app the ways users use it, not just the internal implementation
* Find elements by accessibility markers, not test IDs.

## React Testing Library vs Jest
* React Teting Library
  * Provides virtual DOM for tests
* Jest
  * Test Runner
    * Finds Tests
    * Runs tests
    * Determines whether tests pass or fail

## Enzyme
Enzyme is another powerful testing tool that can be utilized into a React app.


## Assertions
* expect(element.textContent).toBe('String value here');
* expect(elementArray).toHaveLength(10)

> jest-dom comes with create-react-app
> src/setupTest.ts imports it before each test, makes matchers available
> DOM-based matchers


# Types of Tests
* Unit tests
  * Test one unit of code in isolation
* Integration tests
  * How multiple units work together
* Functional tests
  * Tests a particular function of software
* Acceptance/E2E tests
  * Cypress or Selenium

