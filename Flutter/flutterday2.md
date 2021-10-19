# The Dart Programming Language
I can not write a Flutter app without knowing a bit of the Dart programming language.
* According to the official documentation
    * **Dart is a client-optimized language for the fast apps on any platform**
It is a faily young but very ambitious programming language. As far as what I know for now, it is a statically-typed programming language that supports both functional and OOP programming. Just like GoLang, it does not have much historial burden and much of the Flutter concept is quite similiar with React, so I won't call it 'a very tricky path' to learn Flutter if you know some React.

# The UI layouts.
Every piece of UI is a widget. Based on notes of day1, there are some common widgets.
> Layout: Row, Column, Scaffold, Stack
> Structures: Button, Toast, MenuDrawer
> Styles: TextStyle, Color, Padding
> Animations: FadeInPhoto, transformations
> Positioning and alignment: Centering and Padding.
It is important to know how these UI elements work just like I'll need to know how to style components to make pages look better.

## The build method
Every widget must have a build method. One of the most common example is a StatelessWidget that has a default build method with BuildContext as parameter. Note that a StatefulWidget has a createState method() that handles the state while the state object will be repsonsible to override the build method.
```Dart
class SubmitButton extends StatelessWidget{
    Widget build(context){
        return Button(
            child: Text('Submit')
        );
    }
}
```

## Widget Tree
The procedures of building a Flutter app is to compose different widgets together to form a **widget tree**. A Flutter app is represented by a **widget tree** just like DOM in the browser.
