# Spring Security

### **Session Fixation**
Session fixation is an attacker impersonate a valid user by reusing a previously generated session ID. 

### **XSS**
Cross-site scripting allows the injection of the client-side scripts inot web servers exposed by the server, thereby permitting other users to run these.

### **CSRF**
Cross-site request forgery attacks assume that a URL that calls an action on a specific server can be extrated and reused from outside the application. If the server trusts the execution without doing any check on the origin request, one could execute it from any other place. 

Spring Security components provide a lot of flexibility, which offers quite a lot of options when adapting these to the architecture of our applications.

There are some different approaches to override the default Spring Security configuration.

Some of the common items that needs to be listed.
> **AuthenticationProvider**
> **AuthenticationManager**
> **UserDetailService**
> **Authentication** object in Authentication provider

Extends a WebSecurityConfigureAdapter to provide some configurations of Spring Security.