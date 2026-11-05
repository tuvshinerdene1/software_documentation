Scrum master role - make sure the work goes smooth and makes sure team properly utilizes scrum technique. 
Whole team should be responsible for keep the DoD in Scrum team.
Outdated documentation means that the story is not done.

## the documentation goal
diagrams communicate structures, behavior, and relationships at a glance. they serve on-boarding engineers, reviewers and auditors. - each needing a different zoom level:
* reduce cognitive load for readers
* make implicit architecture explicit.
* enable faster code reviews 

## Pragmatic UML: the diagrams that matter
UML has 14 diagram types - in practice, three cover 90% of software documentation needs. Focus on what communicates not what is complete.
1. sequence diagram - shows how components interact over time. ideal for documenting API calls, authentication flows, and event-driven processes.
2. class diagram - shows data structures and relationships. Documents domain models, inheritance hierarchies, and database entity relationships
3. deployment diagram - shows where components run. Documents cloud infrastructure, container orchastration etc.

## BPMN: Documenting Business Processes
Business Process Model and Notation(BPMN-2.0) is the standard for documenting workflows and business processes. Unlike UML, BPMN is designed to be readable by both technical and non-technical stakeholders.

key BPMN elements:
1. events - start, intermediate, end (circles)
2. tasks - work units (rounded rectangles)
3. gateways - gateways (decisions and forks (diamonds))
4. pools & lanes - actors and responsibilities 

### when to use BPMN vs UML
BPMN - user journeys, approval workflows, business logic with multiple actors 
UML - system internals, class structures, technical interaction sequences (UML is mainly for developers & technical people)

## C4 Model
level 1 - system context (= use case)
level 2 - containers (= component diagram)
level 3 - components (= component diagram)
level 4 - code (=class, sequence diagram etc)

not all 4 necessary

## Diagram as code 
### why ? 
- automated rendering in CI/CD pipelines
- no binary files
- changes are tracked via git
- diagrams live in the repository alongside code
## tools for diagram as code 
- mermaid.js - native in gitlab, sequence, flowchart, class, 
- plant uml - more powerful syntax. C4, UML, BPMN. renders via server or plug in

## common diagramming mistakes 
1. **too much detail at wrong level** - showing method structures in a c4 context diagram. each zoom level has a purpose. dont mix them. context = business view, code = implementation view
2. **diagrams stored as binary files only** - saving only png/svg without the source code means the diagram cannot be versioned, reviewed, or automatically regenerated. always commit the sources.
3. **outdated diagrams** - a diagram that doesnt match the current system is worse than no diagram - it actively misleads. treat diagram updates as part of your DoD
4. **no audience consideration** - using uml notation for a diagram intended for business stakeholders. match diagram type and complexity to the reader, not to your technical comfort zone.


*method signature - full detail of method* 
 