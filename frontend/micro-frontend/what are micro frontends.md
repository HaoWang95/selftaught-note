# What are micro frontends
In general, it refers to vertically arranged systems and teams.
Instead of mastering a specific technology, they all focus on providing the best user experience for the area they work on.
* Teams work autonomously in their field of expertise.
* Teams can choose the technology stack that fits best for the job
* The apps are loosely coupled and only integrate in the frontend, eg, via links
> Use fragments to integrate different parts of a page.
The term `frontend integration` describes a set of techniques you use to assemble the user interfaces(pages and fragments) of the team into an integrated application. You can group these techniques into three categories: **routing**, **composition**, and  **communication**. `Frontend integration` describes a set of tools and techniques to combine the team's UI into a coherent application for the end ser. 
* **routing and page transitions** 
Get from a page owned by team A to a page owned by Team B. The solutions can be straightforward. We can add an HTML link. If we want to enable client-side navigation, which renders the next page without having to do a reload, it gets more sophisticated. We can implement this by having a shared `application shell` or using a meta-framework like `single-spa`/
* **composition**
This is the process of getting the fragments and putting them in the right slots. A separate composition service or technique does the final assembly. It goes to 2 categories in general.
    * Server-side composition, for example with SSI, ESI, Tailor or Podium
    * Client-side composition, for example with iframes, Ajax, or web components
* Shared topics
    * Web performance
    * Design system
    * Sharing knowledge                                                                                                             


