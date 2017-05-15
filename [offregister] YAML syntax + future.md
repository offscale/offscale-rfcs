offregister
===========

Proposed new syntax for apps; distributed-systems; and including other offregister- packages for offregister to provision onto nodes:

```yaml
name: cool_app
version: 0.0.1-alpha
author: Samuel Marks <samuel@offscale.io>
auth:
  - {location: env.AUTH_FILE, type: 'file'}
  - {location: env.AUTH_STR,  type: 'hashicorp_vault'}
nodes:
  - /unclustered/any-cluster-*
  min: 1
  max: 3
  locations:
    - Sydney
    - Melbourne
  providers:
    - Azure
    - AWS
    - private3y11
types:
  - fabric
store:  # store response/output
  - etcd
  - analytics_db
  - logfile
deps:
  - XOR
    - env.RDBMS_URI
    -
      install: offregister-postgres
      steps: 'all'
      env: {cluster: false}
  - XOR
    - env.CACHE_URI
    -
      install: offregister-redis
      steps: ['install_local0', 'serve_local1']
      env: {cluster: false}
env:
  COOL_APP_GIT_TAG: 'master'
sets_env:
  - COOL_APP_REST_API
  - COOL_APP_WWWROOT
  - COOL_APP_DOMAINS
  - COOL_APP_HTTPS_CERTS
init:
  - offregister-bootstrap  # from offregister-bootstrap python-package, runs everything in its `init:`
  - this.deploy_static     # from offregister-some-cool-app <-- repo where this file is
  - this.deploy            # from offregister-some-cool-app, which uses offregister-app-push
  # also uses offregister-web-servers which in turn uses offregister-systemd
  - this.serve             # from offregister-some-cool-app, uses offregister-githook & others
del:
  - this.stop              # stop daemons that init started
  - this.daemon_rm         # delete daemons
  - this.rm                # remove directories
  - this.teardown          # uninstall services / other dependencies
  - offregister-bootstrap  # from offregister-bootstrap python-package, runs everything in its `del:`
```

# TODO: philosophy
Figuring out exact why people should use offscale's suite rather than alternatives. Currently planning/experiencing unique feature-set of:

  - OPEN-SOURCE (always)
  - Multiple [50+] public, private, and local [incl. Vagrant] cloud providers integration
  - Utilisation of multiple configuration management / remote execution frameworks, like: Fabric; Ansible; Puppet; Docker; Chef; Salt, including scripts to migrate node registries/inventories between frameworks
  - Focus on bootstrapping multiple distributed systems, especially other PaaS and MultiPaaS (like Mesosphere's DC/OS)

… but, is that enough? - Could do all that then focus on corporate features like:

  - REST API with full RBAC integrated into LDAP/AD; focussing on hefty audit logging/reviewing workflow processes
  - Web apps and native mobile apps
  - Fancy analytics dashboards to explore—expenditure, load, and other metadata—per individual, team, department, location, and entire organisation.

Now would that be enough of a philosophy and feature-set to make an impact, or am I missing something? - Also please critique my proposed syntax :)
