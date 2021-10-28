# PowerShell Starter
Why I'm starting a section for PowerShell is for most laptops I've been using were Windows laptops. Though it's quite a popular trend for many application developers to use Mac and deploy applications in containers(or Linux environment). But hence my machines are normally Windows, so I just start a PowerShell session to get familiar with scripting under Windows environment(So I can perform various tasks under Windows without any further knowledge of the .Net framework). 
```ps1
Get-Service
```

___

PowerShell core is based on .NET Core.
```ps1
Get-Service | Where-Object Status -eq 'Stopped' | Select-object Status, Name
```
