import webapp2

from google.appengine.ext import ndb

class Person(ndb.Model):
  name = ndb.StringProperty(required = True)
  height = ndb.IntegerProperty(required = True)
  intrests = ndb.StringProperty(required = False, repeated = False)

class DemoHandler(webapp2.RequestHandler):
  def get(self):
      # jordan = Person(name='jordan',height=72)
      # seemong = Person(name= 'See Mong', height=42)
      # print (jordan)
      # jordan.put()
      # seemong.put()
      # self.response.write('hello world')
      my_query = Person.query()
      print (my_query)
      persons = my_query.fetch()
      print(persons)
      seemongs = my_query.filter(Person.name == 'See mong').fetch()
      print(seemongs)
      tall_people = my_query.filter(Person.height > 90).fetch()
      ordered_names = my_query.order(Person.name).fetch()
      results = str(ordered_names)
      self.response.write(results)

app = webapp2.WSGIApplication([
        ('/', DemoHandler),
], debug = True)
