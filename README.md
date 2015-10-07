# PostgreSQL module for node and backendjs

Convert JSON types, arrays and numbers into Javascript types, binary as Buffers, the rest as strings.

# Usage

```javascript
  var pg = require("bkjs-pgsql");

  var db = new pg.Database("postgresql://postgres@127.0.0.1/backend");
  db.connect(function(err) {
     if (err) return console.log(err);
     client.setNotify(function(msg) { logger.log('pgsql: notify:', msg) });
  });

  db.query("SELECT name FROM sqlite_master WHERE type='$1'", ["table"], function(err, tables) {
    console.log(err, tables);
  });
```

## Database class
- `new Database(url)` - create new database object, it is not connected yet
- Properties:
  - `open` - returns 1 if the db is open
  - `name` - returns the db name
  - `socket` - returns the TCP socket once connected
  - `affected_rows` - returns number of rows affected by the last operation
  - `inserted_oid` - last auto generated ID
- Methods
  - `connect([callback])` - connect to the server, if no callback is given an exception will be thrown on error
  - `query(sql, [values], [callback])` - execute any SQL statement asynchronously, if a callback
     is given it will be passed an array with result if exists, otherwise empty array
  - `querySync(sql, [values])` - execute a SQL statement in blocking mode, returns array with result
  - `close([callback])` - close the database, on completion call the callback if given
  - `destroy()` - close the database, free memory, this object cannot be used anymore
  - `reset()` - reset internal memory, free results, this is called before every query but in case of huge result
     returned and processed to free memory this can be called manually.
  - `setNonblocking(flag)` - enable or disable blocking behaviour, default is non-blocking
  - `setNotify(callback)` - attach notification callback to be called on every NOTIFY message from the server

# Author 

Vlad Seryakov

