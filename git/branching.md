# Branching
## Quick guide

| Instance     |  Branch    | Description, Notes  |
| :---:        |  :---:     |         :---:       |
| Stable       |  stable    | Accepts merges from Working and hot fixes
| Working      |  master    | Accepts merges from Features/Issues and hot fixes
| Features/Issues | topic-* | Branch off HEAD of working
| Hot fix      |  hotfix-*  | branch off stable

## Main branches
The main repository will hold two everygreen branches
* master
* stable
The main branch should be considered `origin/master` and will be the main branch where the source code of HEAD always reflect a state with the latest delivered development changes for the next release. As a developer, I will be branching and mergeing from master.

Consider the `origin/stable` to always represent the latest code deployed to production. During development, the `stable` branch will be not interacted with.


## Feature branches
Feature branches are used when developing a new feature or enhancement which has the potential of a development lifespan longer than a single development. When starting the development, the deployment in which this feature will be released may not be known. No matter when the feature branch will be finished, it will always be merged back into the master branch.