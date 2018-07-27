import webapp2
import jinja2
import os
from google.appengine.ext import ndb
# START MAGIC CODE

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__))
)
#end magic CODE
class madLibs(ndb.Model):
    noun1 = ndb.StringProperty(required = True)
    verb1 = ndb.StringProperty(required = True)
    verb2 = ndb.StringProperty(required = True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        info_template = jinja_env.get_template('templates/info-input.html')
        self.response.write(info_template.render())
    #    self.response.write("info page here")
    def post(self):
        info_details = jinja_env.get_template('templates/info.html')
        noun1 = self.request.get("noun1")
        verb1 = self.request.get("verb1")
        verb2 = self.request.get("verb2")

        user_input = {
            'noun1': noun1,
            'verb1': verb1,
            'verb2': verb2
            }

        fieldObject = madLibs(noun1 = noun1, verb1 = verb1, verb2 = verb2)


        fieldObject.put()
    #    self.response.write('hello world')

        self.response.write(info_details.render(user_input))

class MadLibListHandler(webapp2.RequestHandler):
    def get(self):
        madLib_template = jinja_env.get_template('templates/query.html')
        self.response.write(madLib_template.render())

        my_query = madLibs.query()
        print(my_query)

        data = my_query.fetch()
        query_input = {}
        query_input["data"] = []


        for x in data:
            query_input["data"].append ( {
            'noun1': x.noun1,
            'verb1': x.verb1,
            'verb2': x.verb2,
            })
        print(query_input)
        self.response.write(madLib_template.render(query_input))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/list', MadLibListHandler)
    ], debug = True)
