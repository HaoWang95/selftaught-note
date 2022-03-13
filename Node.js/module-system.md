# The module system
* package -> Java, Go, PHP, Rust, Dart
* assembly -> .NET
* library -> Ruby

1. Why modules are necessary and different modules systems available in Node.js
2. CommonJS internals and module patterns
3. ES modules in Node.js
4. Differences and interoperablity between CommonJS and ESM

## Why moduls is needed
* Split codebase into multiple files
* Allowing code reuse across different projects
* Encapsulation
* Managing dependencies

## Module systems in JavaScript and Node.js
When JavaScript browser applications become more complicated and frameworks like jQuery, Backbone took over the ecosystem. the JavaScript community came up with several initiatives aimed at defining a module system that could be effectively adopted within JavaScript projects. The most successful ones were **asynchronous module definition(AMD)**, popularize by RequireJS, and later **Universal Module Definition.**

When Node.js was created, it was conceived as a server runtime for JavaScript with direct access to the underlying filesystem so there was a unique opportunity to introduce a different way to manage modules. The idea was not to rely on `HTML <script>` tags and resources accessible through URLs. Instead, the choice was to rely purely on JavaScript files available on the local filesystem. For its module system. Node.js came up with an implementation of the CommonJS specification, which was designed to provide a module system for JavaScript browserless environments.

Then there was an official proposal for a standard module system: ESM or ECMAScript modules, this tries to bridge the gap between how modules are managed on browsers and servers.
Now, ESM is becoming the de facto way to manage JavaScript modules in both browser and the server landscape.


## CommonJS modules
CommonJS is the first module system originally built into Node.js. The two main concepts of CommonJS specification:
1. require is a function that allows you to import a module from a local filesystem.
2. exports and module.exports are special variables that can be used to export public functionality from the current module.

## The module cache
Each module is only loaded and evaluated the first time it is required, since any subsquent call of require() will simply return the cached version.
* It makes it possible to have cycles within module dependencies
* It guarantees, to some extent, that the same instance is always returned when requiring the same module from within a given package.

## ES modules
The most important differentiator between ESM and CommonJS is that ES modules are static, whihc means that imports are described at the top level of every module and outside of any control flow statement.