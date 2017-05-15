Library refactor
================
Currently most `offregister-` packages are standalone, to be included within offregister JSON.

However, this doesn't make sense. Given a toy example:

```yaml
name: some_cool_app
version: 0.0.1
author: Samuel Marks <samuel@offscale.io>
types:
  - fabric
deps:
  - env.RDBMS_URI xor offregister-postgres
  - env.CACHE_URI xor offregister-redis
set_env:
  - COOL_APP_REST_API
  - COOL_APP_WWWROOT
  - COOL_APP_DOMAINS
  - COOL_APP_HTTPS_CERTS
init:
  - bootstrap         # from offregister-bootstrap
  - install           # from offregister-some-cool-app <-- repo where this file is
  - install daemon(s) # offregister-web-servers which uses offregister-systemd
  - deploy            # from offregister-app-push
  - serve             # from offregister-githook & other daemons
del:
  - stop and delete daemons
  - remove directories
  - uninstall services / other dependencies
```

Thus the only `offregister-` packages which should be within an offregister JSON are:
  - Distributed systems, like: Mesos; etcd; Postgres; Redis; Ceph; Deis, &etc.

Other packages which should appear within an offregister JSON are
  - Custom apps, like the example above
  - Bootstrap code (potentially)

Everything else should never appear in offregister JSON.
