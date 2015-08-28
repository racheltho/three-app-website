import webapp2
from google.appengine.ext.webapp import template
import os

path = os.path.join(os.path.dirname(__file__), 'index.html')


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(template.render(path, {}))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ], debug=True)
