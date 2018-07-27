import webapp2
import jinja2
import os

# START MAGIC CODE
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__))
)
#end magic CODE

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('Hello World! ')
        self.response.write('Hello Marie')

class HelloPage(webapp2.RequestHandler):
        def get(self):
            self.response.headers['Content-Type'] = 'text/html'
            page = ('<!DOCTYPE html>' +
            '<head>' +
            '</head>' +
            '<body>' +
            '<h1>Hello! </h1>' +
            '</body>' +
            '</html>')
            self.response.write(page)

class InfoPage(webapp2.RequestHandler):
    def get(self):
        info_template = jinja_env.get_template('templates/info-input.html')
        self.response.write(info_template.render())
    #    self.response.write("info page here")
    def post(self):
        info_details = jinja_env.get_template('templates/info.html')
        user_name = self.request.get('fullname')
        user_address = self.request.get('address')
        user_color = self.request.get('color')

        user_input = {
            'name': user_name,
            'address': user_address,
            'color': user_color
        }

        self.response.write(info_details.render(user_input))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/hello', HelloPage),
    ('/info', InfoPage)
], debug = True)
