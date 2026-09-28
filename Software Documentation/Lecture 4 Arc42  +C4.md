ADR - Architecture Decision Records
## Entry quiz
1. how did you distinguish a functional from a non-functional requirement in M3?
	1. functional requirement defines the functionality of system whereas non functional requirement defines the quality attributes of the system with measurable boundaries 

2. which verificaiton method did you pick up for your slowest requirement - and why?
	1. 
3. what surprised you in the Men vs Ai comparison table?
	1. ai requirement verification was bit general compared to human written requirement. 

Traceability - Linking one document to another document using citing so that reader of later document can trace up to previous documents.


## arc 42 - 12 building blocks 
1. introduction & goals - fundemental requirements, especially quality goals
2. architecture constraints - regulations and external constraints 
3. system scope & context  - external systems and interfaces
4. solution strategy - core ideas and solution approaches
5. building block view - structure of source code, modularization, hierarchically refined. usually the most extensive section of an architecture documentation.
6. runtime view - important runtime scenarios
7. deployment view - hardware, infrastructure and deployment
8. cross cutting concepts  - overarching topics , often very technical and detailed: technology choices, recurring patterns, development and deployment processes. Grows with every concept you decide
9. architecture decisions  - important decisions, unless described elsewhere
10. quality requirements  - quality tree and quality scenarios 
11. risks & technical debt - known problems and risks
12. glossary - important and specific terms 

in this week we will cover 3,5,6

C4 advantage - converstion between documentation and code is pretty straigthforward 


## C4 four zoom levels
1. **System context** : one box- your system - the software system as a central box, surrounded by its users and other interacting systems
2. **container**: web app, api, db... - the high-level shape of the architecture, showing applications, databases, and tech choices
3. **component** : components inside one container - the structural building blocks inside an individual container, mapping responsibilities and interfaces.
4. **code**: class-level diagram - implementation details (like UML class diagrams ), often auto-generated from source code.

### System context
System context is the environment and all external elements - such as users, hardware, and other software - that interact with a system but lie outside its operational boundary.

Key elements:
- the core system: the main product or software treated as a single black box in the center
- external entities (Actors): people, organizations, or external hardware/software systems that communicate with the core system.
- system boundaries: the dividing line that separates what is inside the system's control from its external environment
- interface  and data flows : the communication channels , inputs, and outputs passing data between the system and the outside world


why it matters :
- defines scope
- improves communication
- identifies dependencies

Diagram as code - drawing diagram with code.
The reason of why uml is used commonly - c4 uses uml officially.


## arc42 vs c4 - and how to combine them
prose for context, diagrams for structure, ADRs for reasoning

arc42 - prose driven, twelve sections tell a story what is why this what risks, c4 diagrams  travel as illustrations inside the prose 
c4 - diagram driven, notation of boxes and arrows, the prose sits beside not inside the diagram

template - эх загвар
to fill in template, we use c4.

how to combine - arc42 $3 holds the c4 context diagram: arc $5 holds the Container and Component diagrams. the rest of arc42 stays prose.

ADR - the smallest counter-measure to tribal knowledge

homework: what documents are used for Sisi??
