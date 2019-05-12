[offdocs] Concepts
==================

## Problem

Docs are distributed, in wiki(s), codebase(s), blog(s) and more. These cross languages, programming and natural.

## Stopgap solution

See [Travis CI file](https://github.com/Fantom-foundation/fantom-dev-web/blob/master/.travis.yml) for a current project, that generated an Angular site from Github wiki, and RFC markdown (on a git repo).

## Solution
YAML file like so:
```yaml
base_angular_repo: '.' # this repo
wiki:
- git: https://github.com/offscale/some-proj.wiki.git
  type: Github
  href: '/wiki0'
- git: https://github.com/offscale/some-proj.wiki.git
  type: Github
  href: '/wiki1'
blog:
- # TBD
code:
- git: https://github.com/offscale/some-proj.wiki.git
  branch: master
  system: sphinx-3.0
  generator: python -m comment_extraction antlr.py
  href: '/docs/go'
- git: https://github.com/offscale/some-proj.wiki.git
  branch: master
  system: sphinx-3.0
  generator: python -m comment_extraction antlr.py
  href: '/docs/rust'
- git: https://github.com/offscale/some-proj.wiki.git
  branch: master
  system: sphinx-3.0
  generator: python -m comment_extraction antlr.py
  href: '/docs/java'
```

Additionally each linked repository will trigger a rebuild of the central documentation, and the rebuild of the central documentation will trigger a rebuild of the website to a CDN. (the stopgap solution currently works this way)
