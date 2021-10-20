# Know what is build context and how to navigate between pages
Based on what I learned in day2, Flutter shares a common layout pattern just like what we do in web pages. Also the **Row** and **Column** just work like a FlexBox. Also, Flutter has provided the built-in router to navigate between pages.
## > BuildContext
BuildContext can help to track the widget tree, like where the widget are located in the tree. For example, we can define the basic ThemeData at the root the app(in main.dart) and then override the settings in some of the deeper widgets.