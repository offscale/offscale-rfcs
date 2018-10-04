Binary—Rust?—reimplementation
=============================

## Keep syntax simple
Steal idea + arguments from Fabric:

    run, sudo, cd, get, put, upload_template, shell_env

The main idea here is to go from the official 'Getting Started' guide to successful single node and successful clustered deployment, as quickly and obviously as possible. Preferably orthogonal to the guide.

## Use AST traversal to infer percentages

    [50/500 run operations]
    [87/90 sudo operations]
    [137/590 total] (23.220338983050847457%)

## Produce binaries

    offregister_postgres <keyword arguments>
    offregister_postgres -c <config_file>

### Alternate use

    offregister_postgres --check -c <config_file>

Checks what current host has, possible output format:

    configs:
    - init_d: true
    status:
    - postgres_service: 'stopped'
    version: 9.6.4
With nonzero exit-codes if current host hasn't been bootstrapped.

## Check command
Produce a simple syntax like:

    version: 9.6.4
    os:
    - Ubuntu 16.04
    - Ubuntu 18.04
    config:
    - path: /etc/postgresql/9.6/main/postgresql.conf
      sha256: 21004c91274b71d5eb0265dc40f8e0a47c78a1a868adcec4a771deb5e848797b
      size: 22K
    service:
     - postgres: running
    alive_script:
     - shell: /bin/sh
       cmd: pg_isready
       exit_code: 0

### Generalised solution

    offcheck -c <config_file>

### Generate config file
Should be possible by analysing the source code, figuring out which files are edited and when an init file is modified, and when any file is added/removed.

Maybe a special generated section—or better yet: merge semantics—such that only a few manual edits are required.

## Client/server—or peer—mode

Often clustered applications are being deployed. But maybe we need a cluster to deploy the cluster. Say we don't know the IP addresses and ports ahead of time, so we need to do some service discovery, but only at initial bootstrap (static peer list).

    offregister_postgres --serve --port 88426 --host cool_dns_name0.tldn

Which will only begin boostrapping the node—as if `offregister_postgres` was run— only when some condition is reached (based on internal logic).

### Generalise

    offconsensus --serve --port 88426 --host cool_dns_name0.tldn \
                 --run 'offregister_postgres -c <config_file>' \
                 --discovery_mode static --discovery_file peers.json \
                 --role master
Other mode:

    offconsensus --serve --port 88426 --host cool_dns_name0.tldn \
                 --run 'offregister_postgres -c <config_file>' \
                 --discovery_mode dynamic --discovery_stop 'n>=3' \
                 --role slave

## Metrics
Need ability to push metrics—e.g.: deployment progress—to servers, like syslog, InfluxDB, PrometheusDB &etc.

## Discovery
Basic key/value store functionality, exposed in an abstracted interface (so you can use etcd, consul, Apache Zookeeper &etc). This will be necessary for the dynamic node discovery step.

---

## TODO
Figure out how different clustering schemes settings should be exposed, see Apache Brooklyn for one [good] idea.
