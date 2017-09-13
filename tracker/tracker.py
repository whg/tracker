import pymongo

db_client = pymongo.MongoClient()
db = db_client['tracker']
version = float('.'.join(pymongo.version.split('.')[:2]))

def set_db(name):
    db = db_client[name]

def update(obj, name, value):
    if version < 3.0:
        func = db[obj.__class__.__name__].update
    else:
        func = db[obj.__class__.__name__].update_one

    func({
        'name': name
    }, { '$set' : { 'value': value } }, upsert=True)
    
def create(obj, name, value=None, dtype=None):
    hidden_name  = '_{}'.format(name)
    if value is None:
        value = dtype()
    obj.__dict__[hidden_name] = value

    getter = lambda self: self.__dict__[hidden_name]
    
    def setter(self, v):
        self.__dict__[hidden_name] = v
        update(self, name, v)
        
    obj.__class__ = type(obj.__class__.__name__, (obj.__class__,), {
        name: property(getter, setter),
    })

