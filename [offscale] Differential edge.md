offscale: Differential edge
===========================
Open-source; Rust; cross-platform (incl. Linux, Mac, & Windows); native focus (.deb, .msi, .pkg), with preference for non VM languages (Rust, Swift, C++) and typed, functional approaches.

## DevOps
- [Rust] Improve speed and reliability of bootstrapping, including developer machine
- [Rust] Orchestrate node configuration during deployment, using consensus
- [Go] Support multiple public and private cloud providers
- Mix-and-match of components: Kubernetes, Mesos, Consul, Mesos DNS, SkyDNS2, etcd, Postgres, MySQL, MS SQL Server, Cassandra, ScyllaDB, MongoDB, RabbitMQ, Elastic, Lucene, Docker, Docker Compose, nginx, Apache HTTPD, caddy, squid, IIS, and etc.

## Code-generation driven development (CDD)
Speedup multi-tier application development by **36x**. Tries to overcome the tradeoffs between: documentation & test coverage, performance, and rapid development.

Approach:
- Translate changes across language boundaries:
  - TypeScript (Angular);
  - Swift (iOS);
  - Java and/or Kotlin (Android);
  - Rust and/or TypeScript (REST API)
- Static code generation (complete)
- Dynamic code generation (complete)

## Business logic interfaces
0. Expose an interface for business analysts and management to use
1. Use *CDD*, so these interfaces, can have equal performance to those hand-engineered.
   - With complete dynamic and complete static code generation, one can, for example:
      1. Manager builds multi entity form wizard, with table, graph and Google Maps outputs.
      2. Code is dynamically generated, and deployed live to production
      3. Post-hoc, engineers statically code generate, and optimise number of requests (to REST API, and to database), and efficiency of requests (change index type for database column, optimise database query)
2. With RBAC, enable 'management-deployers' to allocate new API, database &etc. servers, new apps to the various app stores, and new domains & subdomains

## Big data potential
- Interfaces to explore data can be deeper, with well structured schemas and language-independent ontologies
- Most use-cases for NoSQL are actually schema-full scenarios, where the schema is defined at another layer (e.g.: user created surveys). With CDD, this goes up the pipeline, and make for very efficient Big Data queries, e.g.: with SQL
- Big Data interfaces can be exposed to management, and they can refine the data that's gathered through their business logic interfaces.