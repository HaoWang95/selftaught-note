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
By extending a **StatelessWidget**, **override the build method** will create the UI. Also, in the main.dart, we can define some basic theme settings which can be used or overriden across the app.
```Dart
class CounterApp extends StatelessWidget {
  const CounterApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Second Flutter Demo',
      theme: ThemeData(
          // set the color to light blue and choose the default light mode to be light
          primaryColor: Colors.lightBlue[800], brightness: Brightness.light),
      home: const Home(),
    );
  }
}
```
In Flutter, it can be quite easy to perform tasks like theme switch.
```Dart
class CounterApp extends StatelessWidget{
    const CounterApp({Key? key}) : super(key: key)

    // create a static ValueNotifier that can be accessed throughout the app
    static final ValueNotifier<ThemeMode> themeToggle = ValueNotifier(ThemeMode.light);

    @override
    Widget build(BuildContext context){
        return ValueListenableBuilder(
            valueListenable: themeToggle,
            builder(_, ThemeMode currentMode, __){
                title: 'Second Flutter App',
                theme: ThemeData(primarySwatch: Colors.indigo),
                darkTheme: ThemeData.dark(),
                themeMode: currentMode,
                home: const Home(),
            }
        );
    }
}
```