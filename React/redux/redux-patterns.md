# Do not mutate state
**Actual mutation of state values should always be avoided, both inside reducers and in all other application code.** Mutating state is the most common cause of bugs in Redux applications, including components failing to re-render properly, and will also break time-travel debugging in the Redux DevTools.
Use something like **`redux-immutable-state-invariant`** to catch mutations during development, and **`Immer`** to avoid accidental mutations in state updates.

# Reducers must not have side effects
Reduer functions should only depend on their state and action arguments. and should not calculate and return a new state value based on those arguments. **Reducers must not execute any kind of asynchronous logic(AJAX calls, timeouts, promises, async await), generate random values, modify variables outside the reducer, or run other code that affects things outside the scope of the reducer function.** This is to gurantee that reducers will behave predictably when called. If we are doing time-travel debugging, reducer functions may be called multiple times, with earlier actions to produce the current state value. If a reducer has side effects, this would cause those side effects to be executed during the debugging process. and result in the application behaving in unexpected ways.

# Do not put non-serializable values in State or Actions
**Avoid putting non-serializable values such as Promises, Symbols, Maps/Sets, functions or class instances into redux store or dispatched actions.** 

# Only one redux store per app.
**A standard redux application should only have a single Redux store instance, which will be used by the whole application.**

## Use Redux tookit to write redux logic.
Using RTK will simplify the logic and ensures that the app is set up with good defaults.

## Use Immer for writing Immutable updates
Writing immutable update logic by hand is frequently difficult and prone to errors. **`Immer`** allows to write simpler immutable updates using `mutative` logic, and even freezes the state in development to catch mutations elsewhere in the app. **Use `Immer` for writing immutable update logic, preferably as part of RTK.**

## Structure files as feature folders with single-file logic.
Apps should structure files using a **`feature folder` approach** that with a given feature, the Redux logic should be written as a `slice` file, using RTK `createSlice` API. 
* /src
  * index.tsx: Entry point that renders the React component tree
  * /app
    * store.ts: store setup
    * rootReducer.ts: root reducer
    * App.tsx: root React component
  * /common: hooks, generic components, utils, etc,
  * /features
    * /todos: a single feature folder
      * todoSlice.ts: Redux reducer logic and associated actions
      * ToDo.tsx: A React component

## Put as much logic as possible in Reducers
Try to put as much of the logic for calculating a new state into the appropriate reducer, rather than in the code that prepares and dispatches the action.
