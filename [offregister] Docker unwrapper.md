Unwrap Docker
=============

De-encapsulating Docker would enable a variety of new possibilities.

## Use cases
- Native install
  - Faster deployments and running [less abstraction than Docker!]
  - Utilise language virtual environment
    - python2: virtualenv; python3: venv; ruby: rbenv; node: n; &etc
  - Tie in stateful and nontraditional services
    - databases; queues; caches; search engines; API gateways; &etc.
  - Environmental variables within daemon (e.g.: systemd)
  - Good for dev tier app deployments [not for test or prod tiers]
- Brute-force candidate Docker image creation
  - Try base images, stop when first compiles (e.g.: alpine else Ubuntu)
  - With first image that worked:
    - Output Dockerfile to git
    - Upload image to Object Storage

## Problems/questions to solve
- Port binding
- cgroups?
- Mesos?

## Integration
Stack orchestration
- Chef, Puppet, Fabric, Ansible, &etc.

---

## Development details
- Dockerfile to architecture independent YAML
  - Candidate schema for what this would look like: [ [offregister] 2nd YAML concept.md](%5Boffregister%5D%202nd%20YAML%20concept.md)
- Docker Compose parsing would be a good idea also
