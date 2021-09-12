# **Flask**

**Micro**
Flask is a **micro** web framework. It dependes on Jinja template engine and Werkzeug WSGI toolkit.
The micro means Flask aims to keep the core simple but extensible. By default, Flask does not include a database abstraction layer, form validation or anything else where different libraries already exist that can handle that.
**Configuration & Convention**
By convention, templates and static files are stored in subdirectories within the app's Python source tree, with the name templates and static respectively. 

**Dependencies**
> - Werkzeug implements WSGI, the standard Python interface between applications and servers.
> - Jinja, the template engine that renders the pages.
> - MakeupSage with Jinija. It escapes untrusted input when rendering templates to avoid injection attacks.
> - ItsDangerous securely signs data to ensure its integrity. This is to protectf Flask's session cookie.
> - Click is a framework for writing command line applications. It provides the flask command and allows adding custom management commands.
