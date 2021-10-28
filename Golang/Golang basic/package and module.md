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

**A standard go project needs the following directoies**
* src
    * src contains source code
* bin
    * after using go install, this is the binary exeutable.
* pkg
    * dependency packages

**GOROOT and GOPATH**
* GOPATH is the home path where the Go code resides. It is a path variable that is used be the go tool to look for go code written by users.
    * $HOME/go -> For linux
    * %USERPROFILE%\go -> For windows
* GOROOT is where the go installation took place. 
    * For windows, it can be C -> Program Files -> go -> bin