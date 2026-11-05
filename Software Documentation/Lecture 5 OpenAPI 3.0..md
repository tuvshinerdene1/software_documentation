**API 409**- An http client-side statuse code indicating that request is perfectly valid, but it cannot be processed because it conflicts with the current state of the server's resource.


## Quiz
1. Which arc42 section holds the C4 Context diagram


## OpenAPI 3.0 - the parts of a contract
### Mandatory top-level
- openapi - version string, 
- info - title, version, description, contact read by every renderer
- paths - one item per endpoint, router + method 
- components - reusable schemas and security scemes 

### Optional but recommended 
- servers - production, staging, dev Switcher in Redoc
- tags - group operations , drive navigation
- security - global default auth. Reduces duplication
- examples - on every request and response, without examples, the spec is a skeleton
## Swagger UI vs Redoc
both render the same YAML. They differ in look and feel and one has a buton the other does not.

both open-source tools used to render interactive documentation from OpenAI specifications, but they serve different design preferences and use cases.

README can include anything (including API docs)

In API development and web frameworks, renderers are the components responsible for transforming raw data (like objects, databases queries , or dictionaries)  into the final format (like json or xml) returned to the client 

| Dimension  | Swagger UI                                   | Redoc                                                                   |
| ---------- | -------------------------------------------- | ----------------------------------------------------------------------- |
| layout     | tag list on the left, ops in main column     | single column, three-pane per operation, longer page, clearer narrative |
| try-it-out | yes - emit real requests from the page       | Read-only - samples visible, no execution                               |
| hosting    | static bundle, mount anywhere                | react renderer, node or static-hosted build                             |
| best for   | sandbox style exploration during integration | public facing reference documentation                                   |
## Good practices 
### realistic examples 
Every request and everyrespones must carry at least one example - success and error
### explicit error codes 
Document every HTTP status that can come back - not only the success 

### Version in the URL
path-prefix changes - /v1/, /v2/ - protect earlier integrators and give readers a switchers
### changing at every endpoint
Each path gets an x-changelog extension - what changed, when , why. Redoc sufraces it directly.


[[HATEOAS]]

## Three take-aways
1. OpenAPI 3.0 makes intent verifiable - Spec, request, response, example - one file, four responsibilities 
2. The renderer is a choice - redoc for reference, SwaggerUI for sandbox - same spec, different framing
3. Examples are the contract - Error examples, not just success examples - the renderer shows what the client engineer will read

## Six common pitfalls 
1. **Cargo-cult Swagger 2.0** - pasting the swagger 2.0 template without the discipline behind it. Headers, no-schemas 
2. **Vague-description** - "Updates a thing" renderers read it, no engineer can act on it
3. **Success-only** - only 200 documented. the 4xx and 5xx stay a surprise as production
4. **Over-confident spec** - "Always returns 200" The handler raises. The reader gets lied to
5. **Lying-example** - Example body contradicts the schema. Classis post-rename drift
6. **Real-Secrets-in-examples** - a working bearer token in spec. ships in the next commit and goes public

## Versioning, deprecation
### Strategy A - path prefix
/v1/, /v2/, /v3/ in the URL
Old and new versions coexist. Switcher in the renderer is trivial. old integrators keep their scripts working.
Use when the breaking change is structural.

### Strategy B - header
X-API-Version: 2 in the request
Same URL, version in metadata. Single spec, branches in code. Cheap to host.
Use for additive change 

### Breaking change matrix

| Additive : non breaking                                                     | Deprecate: warn first                                                                   | Breaking: version up                                                    |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| New endpoint, new optional field, new error code with example. Same version | Mark deprecated: true, add sunset header, ship a successor endpoint, document migration | Renamed field, removed endpoint, response shape change. new path-prefix |
