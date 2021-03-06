## **React Hooks**

By using Hooks, I can use hooks to build features without writing a class.


### Basic hooks
**useState**
**useEffect**
**useContext**

### Advanced hooks
**useReducer**
**useCallback**
**useMemo**
**useRef**
**useImperativeHandle**
**useLayoutEffect**
**useDebugValue**

_Understanding_ these hooks, _knowing how to_ apply these hooks into functional components and being able to _write customized hooks_ are keypoints to be a good frontend dev with React.

### **Concurrent mode**
With concurrent mode, React can schedule tasks in a more granular way, pausing its work building elements, checking for differences, and updating the DOM for previous state changes to make sure it responds to user interactions. React will pause or discard rendering work to make high-priority changes, by discarding unnecessary tasks, React arrives at the desired UI more quickly.
In short conclusion, React can pause longer-running updates to quickly react to user interactions in concurrent mode.

### **Suspense**
Components built to work with **Suspense** can now *suspend* if they are not ready to return their UI.

### **useRef**
The useRef hook can be used to directly access DOM nodes, as well as persiste a mutable value across rerenders of a component. We could use useRef to obtain the underlying DOM nodes to perform DOM operations imperatively.

### **useCallback**
The main purpose of React useCallback hook is to memorize functions(which in return can improve the app's performance). This is because every time the component rerenders, it also re-creates functions that are defined inside it. Normally, if there is a change of state, that means the re-render of this component, by default, it will also re-create all functions defined in this component.
To use useCallback, we need to have an array of dependencies. The dependency array helps React understand when to return the memorized function and when to re-create it.
