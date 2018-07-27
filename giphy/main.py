import jinja2
import webapp2
import os
import json
import urllib
import urllib2
from google.appengine.ext import ndb

jinja_environment = jinja2.Environment(
    loader = jinja2.FileSystemLoader(
        os.path.dirname(__file__) + '/templates'))

class UserSearch(ndb.Model):
    term = ndb.StringProperty(required = True)
    count = ndb.IntegerProperty(required = True)
    created_at = ndb.DateTimeProperty(auto_now_add = True)
    unexpected_at = ndb.DateTimeProperty(auto_now = True)

    def increment(self):
        self.count = self.count + 1

class MainPage(webapp2.RequestHandler):
    def get(self):
        search_term = self.request.get('q')
        # trying to get User search

        params = {'api_key' : '7NiIezJTWDywvl2jTn3zFDdylgsVBz1L',
                    'q': search_term,
                    'rating': 'g'
                    }

        form_data = urllib.urlencode(params)
        api_url = 'https://api.giphy.com/v1/gifs/search?'+ form_data

        response = urllib2.urlopen(api_url)
        content = json.loads(response.read())

        gif_urls = []
        for img in content['data']:
            url = img['images']['original']['url']
            gif_urls.append(url)


        if search_term:
            term = search_term.lower()
            key = ndb.Key('UserSearch', term)
            search = key.get()
            if not search:
                search = UserSearch(key=key, count=0, term=term)
            search.increment()
            search.put()

        else:
            search_term = "dog"


        template = jinja_environment.get_template('main.html')
        variables = {'gif_urls':gif_urls}
        self.response.out.write(template.render(variables))

class RecentSearches(webapp2.RequestHandler):
    def get(self):
        recentSearches = UserSearch.query().order(-UserSearch.created_at).fetch(limit=10)
        template = jinja_environment.get_template('recent.html')
        self.response.out.write(template.render({'all_searches':recentSearches}))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/recent', RecentSearches)
    ])
# kegluneq
