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