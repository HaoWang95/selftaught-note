## Actions
An action is a plain JavaScript object that has a `type` field. Consider an action as an event that describes something that happened in the app.

## Action Creators
An action creators is a function that creates and returns an action object. We typically use these so we don't have to write the action object by hand every time.

## Reducers
A reducer is a function that receives the current state and an action object, decides how to update the state if necessary, and returns the new state, `(state, action) => newState`. Consider a reducer as an event listener which handles events based on the received action type.

## Store
The current Redux app state lives in an object called store.
Store is created by passing in an reducer, and has a method called getState that returns the current state value.

## Dispatch
The Redux store has a method called `dispatch`. The only way to update the state is to call dispatch and pass in an action object. Consider dispatch as triggering an event. 

## Selectors
Selectors are functions that know how to extract specific pieces of information from a store value.

## Thunk
A `thunk` is a specific kind of Redux function that can contain asynchronous logic.