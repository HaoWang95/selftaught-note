# Understand AWS container service landscape
> Application networking(service discovery and service mesh)
* Cloud map
* App mesh

> Management(Deployment, scheduling, scaling, and management of containerized applications)
* ECS
* EKS
  
> Hosting(Where the containers run)
* EC2
* **Fargate**(Fargate is serverless)

> Image Registry
* Elastic Container Registry


> ALB(Application load balancer)
> Amazon aurora serverless

## Infrastructure as code
* Make infrastructure changes repeatable and predictable
* Release infrastructure changes using the same tools as code changes
* Relicate production environment in a staging environment to enable continuous testing

> INFRASTRUCTURE AS CODE TOOLS
* CloudFormation
* AWS CDK(This is quite important, it supports Java, Python, TypeScript...)
* Terraform by Hashicorp


## CDK
As noted above, CDK supports multiple programming language for modeling cloud infrastructure as reusable components.
> Core framework
> AWS Construct Library
> CDK CLI

**CDK Pipelines**
AWS CDK application.
