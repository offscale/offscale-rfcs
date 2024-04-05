With support to run natively—i.e., no Docker, no WSL—on Windows, Linux, macOS and others.

0. Build a package-manager for each "thing" where thing could be:
  - Application runtimes
    - [Node.js](https://nodejs.org)
    - [Deno](https://deno.com)
    - [Bun](https://bun.sh)
    - [Rust](https://rust-lang.org)
    - [Go](https://go.dev)
    - [Python](https://python.org)
    - &etc.
  - Application servers
    - Python
      - [Waitress](https://docs.pylonsproject.org/projects/waitress) (Python)
      - [modwsgi](https://modwsgi.readthedocs.io) (Python, for [Apache httpd](https://httpd.apache.org))
      - [uvicorn](https://www.uvicorn.org) (Python)
      - [Hypercorn](https://pgjones.gitlab.io/hypercorn) (Python)
      - [django/daphne](https://github.com/django/daphne) (Python)
    - WebAssembly (WASM)
      - [ngx_wasm_module](https://github.com/Kong/ngx_wasm_module) (many, for NGINX)
    - &etc ; e.g., see https://en.wikipedia.org/wiki/List_of_application_servers
  - Databases / storage layers
    - [PostgreSQL](https://postgresql.org)
    - [MySQL](https://www.mysql.com)
    - [MariaDB](https://mariadb.org)
    - [Redis](https://redis.io) (or better licensed forks/alternatives; like [Microsoft Garnet](https://github.com/microsoft/garnet))
    - [NATS](https://github.com/nats-io/nats-server)
    - [RabbitMQ](https://www.rabbitmq.com)
    - &etc.
  - Reverse proxies / HTTP(S) servers
    - [Apache httpd](https://httpd.apache.org)
    - [NGINX](https://nginx.org)
      - [OpenResty®](https://openresty.org)
    - [envoy](https://envoyproxy.io) [maybe?]
    - &etc.
  - Logging, alerting, event-storage
    - [Prometheus](https://prometheus.io)
    - [InfluxDB](https://github.com/influxdata/influxdb)
    - &etc.
  - Dashboards
    - [Grafana](https://grafana.com/oss/grafana/)
  - Systems which manage systems
    - [Docker](https://www.docker.com)
    - [Kubernetes](https://kubernetes.io)
    - [Apache Mesos](https://mesos.apache.org)
    - [Apache Brooklyn](https://brooklyn.apache.org)
  - Full-stack (similar to old [WAMP](https://en.wikipedia.org/wiki/WampServer)/[LAMP](https://en.wikipedia.org/wiki/LAMP_(software_bundle))/[XAMPP](https://en.wikipedia.org/wiki/XAMPP)); where aforementioned package-managers are mixed-and-matched:
    - [WordPress](https://wordpress.org)
    - [Open edX](https://openedx.org)
    - [Odoo](https://www.odoo.com)
    - [Taiga](https://taiga.io) (project management)
    - [MediaWiki](https://www.mediawiki.org/wiki/MediaWiki)
    - &etc.
1. Enable each part to be configured from (in order):
  a. CLI argument (if `--config` provided; this takes priority over ↓):
  b. Environment variable(s)
  c. Global configuration file
  d. Key/value store (if global configuration file enables such)
  e. Default value
2. Survey what is installed and what secrets have been stored
3. Ability to run all "thing"s as a service:
  - [Windows Service](https://en.wikipedia.org/wiki/Windows_service)
  - [systemd](https://en.wikipedia.org/wiki/Systemd)
  - [OpenRC](https://en.wikipedia.org/wiki/OpenRC)
  - [Launchd](https://en.wikipedia.org/wiki/Launchd)
