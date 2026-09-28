# Recap 
1. name the 4 docs types introduced 
	*user docs, developer docs, operations docs, process docs*
2. which anti-pattern explains "only ali can deploy"
	*tribal knowledge*
3. what is the target reader of a SRS
	*clients, customers, product owners, software developers and engineers, qa etc*
4. Why does the 'Good culture' column matter more than tools ?
	*culture of usage is more important than tool because even with excellent tool, if  the culture is not there, the resulting product will not be as good as intended.*
5. Give one example of defensible omission from your own project idea 
	*doctors unnecessary personal information in medical system*


# IEEE 830 vs ISO/IEC/IEEE 29148

|     |     |
| --- | --- |
|     |     |


use ieee 830 as your structural template, use the iso 29148 quality attributes as your acceptance criteria. The two are not competitors. they are layers.

# SRS Sections & Quality attributes
## Required SRS sections (IEEE 830 mapping)
1. scope, product, audience, constraints: answers for whom, why now, what is in vs out of scope
2. referenced documents & standards: 
3. specific requirements - functional, performance, design constraints
4. external interface requirements (user, hardware, software, communication)
5. non functional requirements (performance, security, reliability, maintainability)
6. other requirements - legal, regulatory , audit
7. appendices - glossary, traceability matrix, assumptions

## 8 ISO 29148 quality attributes
1. correct - the requirement is possible to implement with current technology
2. unambiguous
3. complete
4. consistent
5. randked for priority
6. verifiable
7. modifiable 
8. traceable 
if you cannot write a black-box test for your requirement, it is decoration. the gradable test of "verifiable" is: in one sentence, name the input, the action, the observable output, and the pass/fail boundary.

====
!important 
====
those 8 attributes will be on midterm 

# Template analysis - good vs bad

| bad                                                            | good                                                                                                                          |
| -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **ambiguous**- "the system shall be fast"                      | **verifiable** - "the search endpoint shall return results within 300ms for 5x104 catalogue entries on the reference VM"      |
| **not testable** - "the user interface shall be user-friendly" | **ranked&observable** - "Nielsen's then heuristics: a heuristic review with five target users shall reach a SUS score >= 75"  |
| **design masquerading** - "the system shall use PostgreSQL"    | **split SRS / SDD SRS:**"Persistence state must satisfy ACID on a single transaction" SDD:"Postgresql 16 is the chosen RDBMS" |
| **missing boundary** - "the system shall handle many users"    | "**measurable ceiling"** : "The API must sustain 200 concurrent requests at p95 , 500 ms with < 1% error rate."               |
**heuristic review** - an expert inspection method where usability specialists systematically evaluate a digital interface against established design principles

[[SUS Score]]

**requirement types** - functional, non functional, constraints 

## Concept test 

[[Cargo-Cult anti pattern]]