RFCs
====

RFCs for offregister. Propose/review new: features; approaches; and refactoring will be proposed that aren't specific to any one repository.

FYI: Offscale has a focus on keeping *everything* OPEN-SOURCE


## Why use offscale?
Focusing on open-source, patent-free and cross platform technology: Python library API; cross-platform CLI, RESTful API; and frontend(s). Major unique features in the works:

  1. Multi-IaaS: Deploy to 50+ public and private clouds (Apache Libcloud + own Vagrant driver and extended Azure driver)
  2. Multi-PaaS: deploy various PaaS solutions onto any of these clouds: Mesosphere DC/OS; CloudFoundry; Deis; Flynn; &etc.
  3. Single-server dev tiers
    - Basic PaaS: deploy systems natively
    - Docker image creation tier: package images (without a single base; instead keep trying small [candidate] bases until one compiles)
  4. Multi configuration management: deploy services—wrap Puppet; Chef; Fabric; Ansible; &etc.—from the one config (that can reference existent recipes)

## License

Licensed under any of:

- Apache License, Version 2.0 ([LICENSE-APACHE](LICENSE-APACHE) or <https://www.apache.org/licenses/LICENSE-2.0>)
- MIT license ([LICENSE-MIT](LICENSE-MIT) or <https://opensource.org/licenses/MIT>)
- CC0 license ([LICENSE-CC0](LICENSE-CC0) or <https://creativecommons.org/publicdomain/zero/1.0/legalcode>)

at your option.

### Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in the work by you, as defined in the Apache-2.0 license, shall be
licensed as above, without any additional terms or conditions.
