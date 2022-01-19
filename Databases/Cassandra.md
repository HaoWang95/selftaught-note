# Overview
Apache Cassandra is a distributed, NoSQL database. It is based on a partitioned wide column storage model with eventually consistent semantics. 
It is initially designed at Facebook using a staged event-driven architecture to implement a combination of Amazon's Dynamo distributed storage and replication techiniques and Google's Bigtable data and storage engine model. 
## Design objectives
* Full muti-master database replication
* Global availability at low latency
* Scaling out on commodity hardware
* Linear throughout increase with each additional processor
* Partitioned key-oriented queries
* Flexible schema

## Features
Cassandra provides the **`CQL(Cassandra Query Language)`**, an SQL-like query language to create and update database schema and access data. CQL allows users to organize data within a cluster of Canssandra nodes using:
* Keyspace
  ** Defines how a dataset is replicated, per datacenter. Replication is the number of copies saved per cluster. Keyspaces contain tables.
* Table
  ** Defines the typed schema for a collection of partitions. Tables contain partitions, which contain rows, which contain columns. Cassandra tables can flexibly add new columns to tables with zero downtime.
* Partition
  ** Defines the mandatory part of the primary key all rows in Cassandar must have to identify the node in a cluster where the row is stored. All performant quries supply the partition key in the query.
* Row
  ** Contains a collection of columns identified by a unique primary key made up of the partition key and optionally additional clustering keys.
* Column
  ** A single datum with a type which belongs a row