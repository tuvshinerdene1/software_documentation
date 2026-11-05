5 bhatti principles 
1. explained 
2. concise
3. clear
4. usable
5. trustworthy

## Quiz
1.Where in openai 3.0 do you put a request example ? 
2.Which renderer would you pick for a public api reference page ? why? 
3.Did you miss any hTTP error code in your spec? which one surprises clients most ? 

A perfect OpenAPI file can still leave the in-code method body undocumented. 

pipeline steps 
1. lint
2. generate
3. publish

## Code documentation anti-patterns
### Rest comments
comments that named the problem but never solved it. After a year they are a confession that nobody cared. (either fix or delete)
### Lying comments
A docstring that drifts away from the code is worse than no docstring - readers trust the comment not the body (check doc example against real output)
### AI drift
documentation generation should be first draft only.

[[Devops principle]]

Api descriptions should prioritize public methods because other developers will be using those. 

explanation and documentation are not same 

## Key take aways 
1. public api gets a docstring with example call - internals do not have to
2. a docstring without a generator is theatre - Sphinx publish it 
3. AI comments need the same verification protocol as prose documentation.

Internal documentation for developers is needed also. 

## Public API - yes, internal - sometimes 
