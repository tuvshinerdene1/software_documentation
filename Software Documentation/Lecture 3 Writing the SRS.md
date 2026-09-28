# usage of ai

1. use
2. verify (check if its correct)
3. cite, source (explain where you found it)

! milestone 3 , 7 , 10 are worth 50% of total work

***homework : give one example from m2 where you had to choose SRS vs SDD***

[[Usability]]

software scope doesnt depend on total number of users, but the type of users 

# SRS Skeleton in detail
1. *Introduction*(purpose, scope, audience) - answers for whom, why now, what is in vs out of scope
2. *Overall description* - answers what context does the system live in (users, hardware, dependencies, constraints)
3. *Functional requirements* - answers what the system shall do, one numbered requirement per behaviour, with input/action/observable output
4. *Non functional requirements* - answers how fast , how reliable, how secure, how maintainable - with measurable boundaries 
5. *External interface requirements* - answers: which protocols, data formats, hardware ports
6. *Other requirements* - answers legal, regulatory, audit, localisation
7. *Appendices*(glossary, traceability matrix, assumptions) - answers what terms mean and how each requirement is verified 


| attribute      | what it measures                                                                 | Example                                                                                                                                    |
| -------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Performance    | The actual processing time required for a system to complete an entire task      | The database takes **3.0 seconds** to securely write, index, and save the comment.                                                         |
| Responsiveness | The time it takes for a user to receive immediate feedback or regain UI control. | The UI instantly locks the button and shows a loading spinner within **50 milliseconds**, even while the task processes in the background. |
**Traceability matrix** - useful for tracing who did which requirement when problem occurs
![[Pasted image 20260915114356.png]]

Why functional and non functional requirements are split into two: 
* clear division of responsibility
* distinct architectural impact
* targeted testing and verification
* accurate prioritization and cost estimation
* risk management and compliance 

# from story to testable requirement
user story -> precise verb -> input/action/observable output -> priority

**Story** - "As a researcher, I want to upload PDF so that i can search inside it"
**FR-12(should)** - The system shall accept a PDF of up to 20mb and report in JSON (ok, pages, indexedAt) within 5s, or (error, code) within 2s on the standard endpoint POST /docs. Failure boundary: 20mb is rejected with HTTP 413
## priority
1. must - system fails without it. Test failure blocks release.
2. should - stakeholder pain if missing, business case for it. ship with planned planned close-out
3. could - nice to have, post release roadmap
## traceability 
ID, Source, verify, owner

without traceability, an SRS is a wish list. With it, every line maps to a test, an ownder, and a source interview.

Requirement specification document acts as basis of contract

## Rinzler method
The primary requirement of rinzler method is to extract and structure software requirements using narrative stories rather than traditional, isolated technical specifications.

1. **Narrative-driven discovery**
	1. use stories to map requirements: Instead of writing abstract "the system shall..." statements, you must detail how an actor interacts with the system from beginning to end.
	2. gather cross-functional content: The method requires collaboration with stakeholders, system designers, and end - users to collect authentic user workflows.
2. **Elimination of ambiguity**
	1. precise language: the method explicitly demands removing industry jargon and loose wording to eliminate misinterpretation between developers and clients.
	2. visual storytelling: you must construct clean, professional process diagrams that seamlessly complement the narrative, allowing the visual layout to explain the process on its own.
3. **Clear document structure**
	1. a powerful executive summary: the requirements document must lead with a compelling summary capable of selling the project's value directly to senior management.
	2. frequent summarization: authers are required to use brief, periodic summaries to keep the reader anchored to key business objectives.
	3. logical part-to-purpose matching: Every section of the requirements blueprint must have an explicit, un-conflated purpose to prevent document bloat.

## Core methods for requirement verification
1. requirement reviews & inspections
2. prototyping & mockups 
3. model-based verification
4. acceptance test generation
5. requirements traceability mapping (creating Requirements Traceability Matrix)