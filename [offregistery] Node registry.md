offstrategy/offswitch/offset/offregister
========================================

Proposed new node registry approach.

## Currently

  - etcd only (old 2.3.8; which is hierarchical)
  - folder per cluster
  - duplicate node details everywhere
    - `/unclustered/node0`
      `/mesos/node0`

## Proposal

 - etcd, zookeeper, consul &etc.
 - folder/tag per cluster
 - duplicate node name everywhere, but keep only one that has the contents of the node, e.g.:
   - `/default_registry/node0`, then
     `/unclustered/node0` points to `/default_registry/node0`
