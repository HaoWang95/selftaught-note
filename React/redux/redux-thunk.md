# Thunk

- **What is a Thunk**
Thunk is a programming term that means `a piece of code that does some delayed work`. Rather than execute some logic `now`, we can wirte a function body or code that can be used to perform the work later. In redux, **`thunks` are a pattern of writing functions with logic inside that can interact with a Redux store's `dispatch` and `getState` methods.**

Using thunks requires the **redux-thunk** middleware to be added to the Redux store as part of its configuration.

## Writing thunks
A thunk function is a function that accepts two arguments: the Redux store **`dispatch`** method, and the Redux store **`getState`** method. Thunk functions are not directly called by the application code, they are passed into **store.dispatch()**:
```JavaScript
// A thunk function may contain any arbitary logic, sync or async, and can call dispatch or getState at any time.
const thunkFunction = (dispatch, getState) => {
    // logic here to dispatch actions and read state
}

store.dispatch(thunkFunction)
```

In the same way that Redux normally `uses action creators to generate action objects for dispatching` instead of writing action objects by hand, we normally use `thunk action creators` to generate thunk functions that are dispatched. A thunk action creator is a function that may have some arguments, and returns a new thunk function. The thunk typically closes over any arguments passed to the action creator, so they can be used in the logic.
```JavaScript
export let fetchToDoId = (todoId) => {
    return async function fetchToDosThunk(dispatch, getState){
        await client.get(`api/todo/${todoId}`).then(
            resp => {
                dispatch(todosLoaded(response.data))
            }
        )
    }
}
```

Thunks allow to write additional Redux-related logic separate from a UI layer. This logic can include side effects, such as async requests or generating random values, as well as logic that requries dispatching multiple actions or access to the Redux store state.

Redux reducers must not contain side effects, but real applications require logic that has side effects. Some of that may live inside components, but some need to live outside the UI layer. Thunks and other Redux middlewaare give us a place to put thoes side effects.

It's common to have logic directly in components, such as making an async request in a click handler or a useEffect hook and then processing the results. However, it's often necessary to move as much of that logic as possible outside the UI layer. This may be done to improve testabiblity of the logic, to keep the UI layer as thin and presentational as possible, or to improve code reuse and sharing.

In a sense, a thunk is a loophole where we can write any code that needs to interact with the Redux store, ahead of time, without needing to know which Redux store will be used. This keeps the logic from being bound to any specific Redux store instance and keeps it reusable.

## Thunk use cases
- Moving complex logic out of component
- Making async requests or other async logic
- Writing logic that needs to dispatch multiple actions in a row or over time.
- Writing logic that needs access to getState to make decisions or include other state values in an action.

**Thunks are best used for complex synchronous logic, and simple to moderate async logic such as making a standard AJAX request and dispatching actions based on the request values.**

## Redux thunk middleware
Dispatching thunk functions requires the redux-thunk middleware has been added into the Redux store as part of its configuration.