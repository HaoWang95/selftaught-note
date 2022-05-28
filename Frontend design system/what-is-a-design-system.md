# What is a design system in general
As a web application developer, it should not feel weird to know about **design system**.
Organizations of every shape are reusing UI patterns to save time and money. But there's a chasm between the design systems created by IBM, Microsoft, AirBnb, Google and the design systems created by most developers.

**The concept of reusable user interface isn't new**. A UI component encapsulates the visual and functional properties of discrete user interface pieces, like the LOGO bricks. Modern user interfaces are assembled from hundreds of modular UI components that are rearranged to deliver different user experiences.

Design systems contain reusable UI components that help teams build complex, durable and accessible user interfaces across projects. Since both designers and developers contribute to the UI components, the design system servers as a bridge between disciplines. It is also the "source of truth" for an organization's common components.

The holistic scope of a design system encompasses assests, overarching design principles, contribution structure, governance and more. Few things are certain for developers. Production design systems must include the UI components and the frontend infrastructure behind it all.
* Common reusable UI components
* Design tokens: styling-specific variables such as brand colors and spacing.
* Documentation site: usage instructions, narrative, do's and don'ts
The parts are packaged up, versioned, and distributed to consumer apps via a package manager. 

# Understand the workflow
Design systems are an investment in frontend infrastructure.
* Build UI components in isolation
    - Every design system is composed of UI components. Storybook can be the workbench to build UI components in isolation outside of the apps. Then we can integrate timesaving addons that help you increase components durability.(Actions, A11y, Controls, Interactions)
* Review to reach consensus and gather feedback
    - UI development is a team sport that requires alignment between developers, designers, and other disciplines. We'll publish work-in-progress UI components to loop stakeholders into the development process so we can ship faster.
* Test to prevent UI bugs
    - Design systems are a single source of truth and a single point of failure. Minor UI bugs in basic components can snowball into company-wide-incidents. We can automate tests to help to mitigate the inevitable bugs to ship durable, accessible UI components with confidence.
* Document to accelerate adoption
* Distribute the design system to consumer projects

# Architecting systems
Miscommunication is rampant as team grows. Existing UI patterns go undocumented or are lost altogether. That means developer reinvent the wheel instead of building new features. Over time, projects are littered with one-off components. Despite the best intentions of an experienced team, UI components were endlessly rebuilt or pasted into place. UI patterns that were supposed to be the same diverged in appearance and functionality. Each component was a unique snowflake which made it impossible for new developers to discern the source of truth, much less contribute. (正确的废话, 大道理谁都知道)

## Where does the design system live
You can think of a design system as another component library, but it serves an entire org instead of serving one app. **A design system focuses on UI primitives, while project-specific component libraries can contain anything from composite components to screens**. Therefore, a design system **must be independent of any project and also a dependency of all projects**. Changes propagate throughout the organization via a vesioned package distributed by a package manager(yarn/npm). Projects can reuse design systems components and further customize if needed.

## What belongs and what doesn't
Design systems should only contain **pure and presentational components**. These components deal with how UI appears, respond exclusively to props, do not contain app-specific business logic, and are agnositic to how data loads. These properties are essential in allowing the component to be reusbale. 