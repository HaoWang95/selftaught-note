# **Flexbox**
Flexbox is used to configure one-dimensional layout, flexbox can be used to adjust the layout of elements vertically or horizontally.

If the flexbox has one weakness, it's the overwhelming number of options it provides. It introduces 12 new properties to CSS, including some **shorthand properties**.

## Flexbox principles
Flexbox begins with the familiar display property. Applying **`display: flex`** to an element turns it into a *flex container*. By default, flex items **align side by side, left to right, and all in one row.**

>- The `flex` property, which is applied to the flex items, provides a number of options. It is a shorthand for three different sizing properties: **flex-grow, flex-shrink, and flex-basis**. By assigning an element with `flex: 1; or flex: 2;`, we only used flex-grow, leaving the other two properties to their default values.

>- **flex-basis** defines a sort of starting point for the size of an element, which is an initial main size.
>- **flex-grow**: once `flex-basis` is computed for each flex item, they will add up to a total width, sometimes it will leave a remainder. The remainer will be consumed by flex items based on their flex-grow values, which is specified as a non-negative integer. If an item has a `flex-grow: 0;`, it won't grow past its flex basis. If any items have a non-zero growth factor, those items will grow until all of the remaining spaces is used up.
>- **flex-shrink** allows a similar principles as `flex-grow`. If the total width of flex elements exceed the size available in the flex container. Without using `flex-shrink`, an overflow can be posted on screen. THe `flex-shrink` value for each item indicates whether it should shrink to prevent overflow. If an item has a `flex-shrink: 0;`, it will not shrink. Items with a value greater than 0 will shrink until there is no overflow. An item with a higher value will shrink more than an item with a lower value. 
