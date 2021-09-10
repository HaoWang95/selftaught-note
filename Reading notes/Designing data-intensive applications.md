# Encoding and evolution.

## Language specific formats
Programming languages come with built-in support for encoding in-memory objects into byte sequences. For example, Java has java.io.Serializable, Python has pickle.

**Backward compatibility**
Newer code can read data that was written by older code.
**Forwawrd compatibility**
Older code can read data that was written by newer code.

Backward compatibility is normally not hard to achieve. 
As long as each field has a unique tag number, new code can always read old data, because the tag numbers still have the same meaning. The only detail is that if you add a new field, you cannot make it required. If you were to add a filed and make it required, that run-time check would fail if new code read data written by old code, because the old code will not have written the new field that you added. Therefore, to maintain backward compatibility, every field being added after the initial deployment of the schema must be optional or have a default value.

**Be careful** when chanigng the datatype of a field. Because values may lose precision or get damaged.

## Thinking about dataflow through databases
In a db, the process that writes to the database encodes the data, and the process that reads from the database decodes it.
In this situation, backward compatibility ensures we can decode what we previously wrote.

Also, it's common for many different processes to be accessing a database at the same time. It means that a value in the dababase may be written by a newer version of the code and subsequently read by an older version of the code that is still running.
In this situation, forward compatibility is required.

The key issue here is if we add a filed to a schema, and the newer code writes a value for that new field to the database. Subsequently, an older version of the code reads the record, updates it and writes it back. The desirable behavior is for the older code to keep the new field intact(the older code does not know about the new field at all), even though it couldn't be interpreted. As a developer, I need to be aware of this problem.

#### **This description is really impressive**
**The major difference between a thing that might go wrong and a thing that can not possibly go wrong is that when a thing that cannot go wrong goes wrong it usually turns out impossible to get at or repair.**

## Replication means keeping a copy of the data on multiple machines.
> - It can help to reduce latency, because by allocating a replication of data, it can be geologically closer to users.
> - Improve availability, if some replication center fails, the system can still work
> - Increase the read throughput

## Another approach is partitioning that splits a big database into smaller subsets.
* Replica, a replica is the node/machine that stores a copy of the database.

* **Master-slave/active-passive/leader-based** replication.
    * One of the replicas is designated as the primary db instance.
    * Client can read/query data from either the leader or slave machines.But writes are only allowed on the master node.
    * Data must be written on the master node first, whenever the master node writes new data, it sends the data change to all of its slaves/followers.
    * Synchronous replication: followers is guaranteed to have an update-to-date copy of the data that is consistent with the leader node. If the leader node, for some reason, suddenly fails, we can be sure that the data is still available on the follower. But the main disadvantage is it is impractical to make followers synchronoous, because the leader must block all writes and blocks util the synchronous replica is available. If any of the follower is down, the leader will be locked.
    * Semi-synchronous, one of the followers is synchronous and others are asynchronous. If the synchronous follower becomes unavailable, one of the async followers is made sync.
    * Asynchronous replication: master-slave based replication is often made asynchronous, if the leader fails and is not recoverable, any writes that have not been replicated are lost.

## Processes to set up new followers
* Take a consistent snapshot of the leader's database. Most db has the feature of taking the snapshot without taking a lock on the entire database. Like innobackupex.
* Copy the snapshot to the new follower node
* The follower and the leader will connect, the snapshot is associated with an exact position in the leader's replication log. 
* When the follower has processed the backlog of data changes since the snapshot, it will catch up the leader.

## Handlong outages of nodes.
There are two situations, one is the follower failure and the other one is leader failure.