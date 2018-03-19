# Concept 3
This is an alternative idea, focussing on facilitating multi-tenant PaaS use-cases.

The application repo stores a file in its root, similar to Procfile/Vagrantfile/Dockerfile.

Services are similar to those in CloudFoundry. These are generally stateful systems which offer things like databases, queues, caches and application gateways (e.g.: proxy to other server / some SaaS or DBaaS).

The PaaS 'package' has its `initial_` services and applications, and an option to allow these to be extended by applications.
E.g.: if application requires RabbitMQ and it's not installed in PaaS, then install it.

Nothing in this design prevents the IaaS layer from being extended to support 2-way integration with Apache Brooklyn, Chef, Puppet, Ansible, Fabric and others. This opens the platform up to huge community & industry maintained marketplaces.

## Application
Sets requirements for application, and this file is added to the repository of the application. E.g.: foo-rest-api.git

```yaml
# Note: this is placed in the application repository, e.g.: foo-rest-api.git

name: 'foo-rest-api'
version: '0.0.1'
supported_platforms:
  - name: 'Python 2'
    has:
      - interpreters:
        - name: 'python'
          version: '>2.6<3'
      - os:
        - name: 'Ubuntu'
          version: '>12.10'
services:
  - name: 'postgres'
    version: '>9.6'
    to_env: 'POSTGRES_URI'
  - name: 'redis'
    to_env: 'REDIS_URI'
security:
  - protocol:
      name: 'HTTPS'
      TLS: '>=1.3'
dns:
  - 'bar.can.com'
```

## System
E.g.: redis-for-paas.git repo. This sets entry points for installation on different platforms, credentials (RBAC) and cluster configuration
```yaml
# Note: place this in a repo like mypaas-redis-service.git, call it 'service.yaml'

name: 'redis'
version: '0.0.1'
supported_platforms:
  - name: 'Python 2'
    has:
      - interpreters:
        - name: 'lua'
          version: '>5.1'
      - os:
        - name: 'Ubuntu'
          version: '>12.10'
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

## Package
Sets requirements for multi-tenant PaaS, including initial applications, initial services and location.

```yaml
# Note: this is usually placed in a different repo, one which operations/DevOps or finance people look at

name: 'paas-name'
version: '0.0.1'
locations:
   - provider: 'azure'
     credentials: ''
     zone: ''
     threshold: null # set a number of servers allowed here
   - provider: 'vagrant'
     type: 'docker'
   - provider: 'docker'
   # &etc.
initial_credentials:
  - key: ''
initial_applications:
  - name: 'foo-rest-api'
    location: 'filepath or git repo path both to application.yaml file'
initial_services:
  - name: 'postgres'
    options: '# cluster options, credentials &etc.'
  - name: 'redis'
    options: '# cluster options, credentials &etc.'
# &etc.
allow_new_services_from_applications: true
```
