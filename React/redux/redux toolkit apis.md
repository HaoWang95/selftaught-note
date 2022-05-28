# createEntityAdapter
A function that generates a set of prebuilt reducers and selectors for performing CRUD operations on a **normalized state structure** containing instances of a particular type of data object. These reducer functions may be passed as case reducers to **`createReducer`** and **`createSlice`**. They may also be used as `mutating` helper functions inside of **`createReducer`** and **`createSlice`**.

```TypeScript
type Book = {
    bookId: string;
    title: string;
}

type Author = {
    name: string;
}

const bookAdapter = createEntityAdapter<Book>({
    selectId: (book: Book) => book.bookId,
    selectTitle: (book: Book) => book.title,

    sortComparer: (a, b) => a.title.localCompare(b.title)),
});

const bookSlice = createSlice({
    name: 'books',
    initialState: bookAdapter.getInitialState(),
    reducers: {
        bookAdded: bookAdapter.addone,
        bookReceived(state, action){
            bookAdapter.setAll(state, action.payload.books),
        }
    }
})

```

# createReducer()
A utitly that simplifies creating Redux reducer functions. It uses immer internally to drastically simplify immutable update logic by writing `mutative` code in your reducers.

```TypeScript
import { createAction, createReducer } from '@reduxjs/toolkit'

interface CounterState {
  value: number
}

const increment = createAction('counter/increment')
const decrement = createAction('counter/decrement')
const incrementByAmount = createAction<number>('counter/incrementByAmount')

const initialState = { value: 0 } as CounterState

const counterReducer = createReducer(initialState, (builder) => {
  builder
    .addCase(increment, (state, action) => {
      state.value++
    })
    .addCase(decrement, (state, action) => {
      state.value--
    })
    .addCase(incrementByAmount, (state, action) => {
      state.value += action.payload
    })
})
```

# createSlice
A function that accepts an initial state, an object of reducer functions, and a slice name, and automatically generates action creators and action types that correspond to the reducers and state.