# Concept 3
Here I try to streamline the idea from the ground up, thinking about modular YAML files held at each level (0. web frontend; 1. api; 2. database; 2. cache; 3. multi-tenant platform; 4. IaaS).

Most of this explanation focusses on facilitating multi-tenant PaaS use-cases. Only the last example shows IaaS.

Decided to make applications and services the same thing, with just a `stateful` parameter to differentiate them. Services are designed with a similar philophy to CloudFoundry's. These are generally stateful systems which offer things like databases, queues, caches and application gateways (e.g.: proxy to other server / some SaaS or DBaaS).

For the application services, most of their requirements can be automatically inferred by shebang lines, reading package.json and similar techniques. These can also be explicitly set, like environment variables are expected to be.

The PaaS 'package' has its `initial_` services, and an option to allow these to be extended by other services. Without this set, only new `stateless` services are allowed.
E.g.: if service requires RabbitMQ and it's not installed in PaaS, then install it.

Nothing in this design prevents the IaaS layer from being extended to support 2-way integration with Apache Brooklyn, Chef, Puppet, Ansible, Fabric and others. This opens the platform up to huge community & industry maintained marketplaces.

## CLI

    python -m offregister -c ~/offscale/sample-rest-api/deploy.yml -d iaas-name -s stop
    python -m offregister -c ~/offscale/sample-rest-api/deploy.yml -d iaas-name -s start --dns foo.foo.com

Adding a `--dns` here replaces (doesn't append) any existing dns from the deploy.yml.

Next is to figure out, a `-s heal` syntax maybe with a `--min` to ensure a threshold of servers—running this service—are online.

## Service (for an application)
Sets requirements for application, and this file is added to the repository of the application. E.g.: foo-rest-api.git

```yaml
# Note: this is placed as deploy.yml in the application repository, e.g.: foo-rest-api.git
name: 'foo-rest-api'
type: 'service'
version: '0.0.1'
root: 'offscale/sample-rest-api.git' # defaults to '.'
stateless: true
supported_platforms:
  - name: 'Platform name 77'
    has:
      - interpreters:
        - name: 'python'
          version: '>2.6<3'
      - os:
        - name: 'Ubuntu'
          version: '>12.10'
internals: {
  inferred: true
}
services:
  - name: 'postgres'  # resolve name to official, else require <owner>/<name>
    version: '>9.6'
    to_env: 'POSTGRES_URI'
  - name: 'redis'
    to_env: 'REDIS_URI'
security:
  - protocol: 'HTTPS'
    TLS: '>=1.3'
    certificates: 'certbot'
dns:
  - 'bar.can.com'
```

## Service (for a database/cache)
E.g.: redis-for-paas.git repo. This sets entry points for installation on different platforms, credentials (RBAC) and cluster configuration
```yaml
# Note: place this in a repo like mypaas-redis-service.git, call it 'service.yaml'

name: 'redis'
type: 'service'
version: '0.0.1'
stateless: false
supported_platforms:
  - name: 'Platform name 62'
    has:
      - interpreters:
        - name: 'lua'
          version: '>5.1'
      - os:
        - name: 'Ubuntu'
          version: '>12.10'
internals: {
  inferred: false,
  tasks:
    - module: 'offregister-redis'
      type: 'fabric'
      kwargs: {
        version: 4,
        auth:
          - username: 'foo'
            password: {"$ref": "env:REDIS_PASSWORD"}
      }
}
env_entry_points:
  - name: 'URI' # There's only one env, so it's auto translated to whatever alias is set in application.yaml
cluster_entry_points:
  - name: 'cluster_size'
    type: 'unsigned'
    constrains: '&1!=0'  # odd
  - name: 'cluster-config-file'
    type: 'string'  # regex allowed! - Maybe even go full JSON-schema here...
  - name: 'cluster-node-timeout'
    type: 'unsigned'
  - name: 'cluster-slave-validity-factor'
    type: 'unsigned'
  - name: 'cluster-migration-barrier'
    type: 'unsigned'
  - name: 'cluster-require-full-coverage'
    type: 'boolean'
```

## Package (for a PaaS)
Sets requirements for multi-tenant PaaS, including initial applications, initial services and location.

```yaml
# Note: this is usually placed in a different repo, one which operations/DevOps and management look at

name: 'paas-name'
type: 'package'
version: '0.0.1'
destination:
   - provider: 'azure'
     credentials: ''
     zone: 'Australia East'
     threshold: null # set a number of servers allowed here
   - provider: 'vagrant'
     type: 'docker'
   - provider: 'docker'
   # &etc.
# alternatively: `destination: 'iaas-name'` if IaaS layer separately deployed
initial_credentials:
  - key: ''
initial_services:
  - name: '../../foo-rest-api'
    location: 'filepath or git repo path both to application.yaml file'
  - name: 'offscale/postgres.git#master'
    options: '# cluster options, credentials &etc.'
  - name: 'offscale/redis.git#master'
    version: '>4'
    options: '# cluster options, credentials &etc.'
# &etc.
allow_services_to_define_others: true
core:
  - name: 'DNS server 3'
    type: 'DNS'
    service: 'offscale/offregister-consul.git#master'
  - name: 'DNS server 4'
    type: 'DNS'
    service: 'offscale/offregister-libcloud-dns-bridge.git#master'
    config:
      - provider: 'azure'
        credentials: ''
        zone: 'Australia East'
  - name: 'Resource allocator 7'
    type: 'resource-allocator'
    service: 'mesos'
sensors:
  - name: 'Logging service 2'
    type: 'logging'
    service:
      - name: 'InfluxDB'
        version: '1.5'
  - name: 'Alert service 3'
    type: 'alerts'
    service:
      - name: 'Nagios Core'
        version: '>4.3'
internals: {
  inferred: true # default
}
```

## IaaS
```yaml
# Note: this is usually placed in a different repo, one which operations/DevOps and management look at

name: 'iaas-name'
type: 'IaaS'
version: '0.0.1'
destination:
   - provider: 'azure'
     credentials: {}
     zone: 'Australia East'
   - provider: 'aws'
     credentials: {}
     zone: 'ap-southeast-2'
   - provider: 'docker'
   # &etc.
strategy: 'cheapest'
multicloud: false # default
initial_nodes: 15
threshold: {
  min: 15
  max: 15
} # always have 15; non elastic (can't create new or remove without replacing)
internals: {
  inferred: true # default; does basic networking and port opening
  extra:
    - save_to: 'etcd://localhost:2379' # default
}
```
