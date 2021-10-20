# Know what is build context and how to navigate between pages
Based on what I learned in day2, Flutter shares a common layout pattern just like what we do in web pages. Also the **Row** and **Column** just work like a FlexBox. Also, Flutter has provided the built-in router to navigate between pages.
## > BuildContext
BuildContext can help to track the widget tree, like where the widget are located in the tree. For example, we can define the basic ThemeData at the root the app(in main.dart) and then override the settings in some of the deeper widgets.

# Some common widgets
Here are some of the common widgets in Flutter which can work as a foundation to build apps.
> Container
> Row
> Column
> Image
> Text
> Icon
> ElevatedButton(Some books or videos refer this as RaisedButton, RaisedButton is depreciated)
> Scaffold(Fundemental starter to build Flutter apps)
> AppBar

To get started and get hands dirty, consider to set the index page as a stateless widget.
```Dart
class App extends StatelessWidget{

    @override
    Widget build(BuildContext context){
        return MaterialApp(
            title: 'Give a title here',
            theme: // Provide some default theme setting here
            home: // index ui widget instance, we'll use a stateful widget here.
        )
    }
}
```