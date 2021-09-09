## **Go package**

Every go source file, .go starts with **package**.
All .go files present in the same directory will belong to the same package.
> - Executable package. Only main is the executable package in GoLang. The main package will contain a main function that denotes the start of a program.
> - Utility package. Any packages other than the main package is a utility package. It contains utility function and other methods that can be utilized by an executable package.

## **Go module**
Module is for dependency management. A module is a collection of related packages with go.mod at root. 
> - Module import path
> - Dependency requirements of the module, otherwise this module can not be built. It defines both project's dependencies requirement and also locks them to their version. Like a dockerfile. 


**Create a go module**
```Go
go mod init FirstGoModule
```
