# REST

- **RE**presentational **S**tate **T**ransfer
- An architectural style
- Not the same as "JSON-based API using HTTP", but people will use it synonymously
- A way of building/organising services

RESTful service == a service built using REST principles

## Features/Principles/Constraints

RESTful services are about managing **resources**. Servers manage resources, clients make requests about them. Only **representations** of resources are communicated.

- Client-server separation : No dependency between the two
- Stateless : All information needed in a message is contained within a message
- Cache : Responses should tell users if they can be stored or not
- Uniform Interface : Consistency in service design; controls are predictable
- Layered System : Components only engage with layers they directly need to
- Code-on-Demand : The server can return code to extend behaviour

## Conventional REST

- JSON over HTTPS
- Standardised routes 