## DataProc

Dataproc is googles managed hadoop offering which provides most of the
products available in the hadoop ecosystem. In this tut we will be going
through the basics of setting up a cluster and running basic jobs on our
cluster.

### DataProc key features

DataProc grants some key advantages over an on-premise offering, being managed
and all. Particularly, dataproc decouples storage and computation compared to
traditional Hadoop. As traditional Hadoop uses storage on each instance HDFS,
dataproc uses google buckets (i.e. object storage over block storage).

This makes the cluster much easier to scale and manage, and keeps the cluster
dynamic rather than static.

DataProc provides some diffent cluster types:
- Regular : Single master / Normal use
- Single-node : Master and data node on one instance / good for dev
- High-Availability : Production use, where data loss cant happen

Notable for DataProc are some other key features: 
- Initialization actions
- Scheduled deletion
- Pre-emptible VMs for cheaper computation

#### Heurestics
- GCE probably be the highest cost for the cluster, thus try to optimize the
  GCE costs if possible
- MR and HDFS are fundamental concepts to understand, but are rarely used
  directly anymore
- Connecting to master instances and running jobs in an old fashion is no
  longer done, we typically submit jobs using the gcloud SDK
