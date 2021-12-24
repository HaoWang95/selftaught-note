# CSS GRID
CSS Grid is a set of css properties for building 2-dimensional layouts.
The main idea is to divide a container into rows and columns that can be filled with child elements.

## Grid principles
Grid layout applies to two levels of DOM hierarchy. An element with `display:grid` becomes a grid container. Its child elements then become grid items.

>- **`display: grid;`** to define a grid container.
>- **`grid-template-columns`** and **`grid-template-rows`** to define the size of each of the columns and rows in the grid. 
>- **`grid-gap`** property defines the amount of space to add to the gutter between each grid cell. We can optionally provide two values to specify vertical and horizontal spacing individually.(for example: `grid-gap: 0.5rem 1rem`)

## Grid details
>- **`grid-line`** makes up the structure of the grid. A grid line can be vertical or horizontal and lie on either side of a row of or a column. The `grid-gap`, if defined, lies atop of the grid-lines;
>- **`grid-track`** is the space betweeen two adjacent grid lines. A grid has horizontal tracks(rows) and vertical tracks(columns).
>- **`grid-cell`** is a single space on the grid, where a horizontal grid track and a vertical grid track overlap.
>- **`grid-area`** is a rectangular area on the grid container which is made up by one or more `grid cells`. 