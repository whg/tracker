Tracker
=======

```python
import tracker

class Thing(object):
    def __init__(self):
        tracker.create(self, 'level', 0)

    def update(self):
        self.level = 10
        
thing = Thing()
thing.update()
```

Then:

```js
$ mongo tracker
> db.Thing.find({})
{ "_id" : ObjectId("5990acdb3190aad0a45d5d94"), "name" : "level", "value" : 10 }
```
