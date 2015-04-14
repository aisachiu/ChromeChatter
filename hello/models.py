from google.appengine.ext import ndb

# Create your models here.

class chatMSG(ndb.Model):
    timestamp = ndb.DateTimeProperty()
    message = ndb.StringProperty()
    userid =  ndb.StringProperty()
