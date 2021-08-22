# Encoding and evolution.

**Backward compatibility**
Newer code can read data that was written by older code.
**Forwawrd compatibility**
Older code can read data that was written by newer code.

Backward compatibility is normally not hard to achieve. 
As long as each field has a unique tag number, new code can always read old data, because the tag numbers still have the same meaning. The only detail is that if you add a new field, you cannot make it required. If you were to add a filed and make it required, that run-time check would fail if new code read data written by old code, because the old code will not have written the new field that you added. Therefore, to maintain backward compatibility, every field being added after the initial deployment of the schema must be optional or have a default value.