# Flutter Widgets

Widgets is the basic building blocks of a Flutter app. Use flutter cli to create a new flutter app.
The Flutter series will start from the basic development of a Flutter app to some  general patterns of Flutter.
> Development
> Testing
> Performance and optimization
> Deployment

By following tutorials to create the first Flutter app and build a *Hello World* sample, there are some observations discovered from the first app.
> In the main.dart file, a main method that runs the app as the program entrance
> Dart is statically typed and supports OOP
> Basic building blocks are composition of UI elements into a *widget*. Therefore the basic UI building block in Flutter is widgets, the concept is pretty similiar with *React Components*.(I do hope Complex State Management is included as part of the Flutter framework so I don't need to borrow everything from the community like using the React)
> Widgets can be stateless or stateful.(Pretty straightforward to understand this, if a widget is stateless, we just need to think about the properties it receives. If a widget is stateful, we need to think about how it should handle the internal state)
> After defining a widget, a build method is responsible to build and return the UI.

## Scaffold
The Scaffold widget is the base of the screen for a single page. It is used to implement the basic functional layout structure of the app. It is easy to implement functional widgets like AppBar, FloatingActionButton, ButtonNavigationBar, Drawer, and many other more widgets on the app using the Scaffold widget.

## Life cycles
Life cycles for **UI components** are important in all front-end frameworks.
> Stateless widget
    > widget -> constructor -> build(), rebuilds when configuration changes
    
> Stateful widget
    > widget -> constructor -> createState() to produce a state object
    > state object -> initState() -> build()
    > widgetDidUpdate() when it receives new configuration
    > setState() when internal state changes 