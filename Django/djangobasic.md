# Views
Django has two types of views; function-based views and class-based views. Django originally started our with function-based views, but then added class-based views as a way to templatize functionality so that you did not have to write boilerplate code over and over again.

## Function based views
* pros
  * Simple to implement
  * Easy to read
  * Explicit code flow
  * Straightforward usage of decorators
  * Good for one-off or specialized functionality
* cons
  * Hard to extend and reuse the code
  * Handling of HTTP method via conditional handling

## Class based views
* pros
  * Code reusability
  * Dry
  * Code extendability
  * Code structuring
  * Built-in generic class-based views
* Cons
  * Harder to read and understand
  * Implicit code flow
  * Use of view decorators require extra import, or method override


# Where to find base template and other templates
Yes, you can use `{% extends "base.html" %}` to extend the base.html file from your project directory.
Important thing to note is where to place the base.html file.

Follow the steps below as it can be quite important:
* open project_name/project_name/settings.py and find the TEMPLATES array and update the 'DIRS' : [] to 'DIRS': [os.path.join(BASE_DIR, 'templates')]
* Create a directory at root level named templates. The location of this folder will be project_name/templates
* Place all templates here in projects_name/templates that you want to access from all the apps. File: project_name/templates/base.html
* Extend this base file from any application-specific template, that might be located at project_name/app_name/templates/app_name template_file.html by using {% extends "base.html" %}.
  