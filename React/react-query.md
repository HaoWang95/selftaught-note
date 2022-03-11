# Client State
Information relevant to browser session.
* User's theme

# Server state
Information relevant to the backend

# Use React query to manage server state.
* Loading
* Error state
* Pagination, infinite scroll
* Prefetching
* Mutations
* De-duplication of requests
* Retry on error
* Callbacks

# React-query
* staleTime
  * staleTile is used for re-fetching
* cacheTime
  * cache data expires after cacheTime

# isFetching vs isLoading
* isFetching -> the async query function has not yet resolved
* isLoading -> no cached data, plus isFetching
