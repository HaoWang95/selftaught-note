# NESTJS

This file will contain notes on nestjs. 

## Install

To get started with nestjs, **npm install -g @nestjs/cli** to get started. This will install the nestjs cli globally. After the installation, we can use nestjs cli to generate and manage apps.

## A quick view of nest cli

Use **nest --help** to list all available nest cli commands 
Use **nest --version** to view the nest version information
Use **nest info** to view the overall nest and system information

## Generate a new app

Use **nest new app_name** to generate a new app. Then direct into the app folder, **nest start** or **npm run start** to start the template app. By default, navigate to **localhost:3000** to see the hello world result for the first run.

# Core concepts in Nestjs

Nestjs provides a clear project structure that developers can follow. And based on my previous learning, nestjs project structure is very similar with Angular. 

Besides the similarity with Angular, nestjs uses decorators to simplify the process of making code work. 

## Controllers

Nestjs controllers are responsible for handling requests and returning responses. It is decorated by **@Controller** decorator, we can also **specify routing paths in @Controller decorator**. Also, we can use a separate routing module to perform the routing task. In each of the controller, the http request processing methods can be annonated with **@Get(), @Put(), @Delete(), @Patch() decorators to react to different http request methods**.
