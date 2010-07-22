from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import os, ProvidenceClarity

pc = ProvidenceClarity.initialize()

class MainHandler(webapp.RequestHandler):
    
    def get(self):
        global pc
        self.response.out.write(str(dir(pc))+'<br /><br />')
        self.response.out.write(str(dir(pc.config))+'<br /><br />')
        self.response.out.write(str(pc.config.get('images_url','handlers',False))+'<br /><br />')
        self.response.out.write(str(pc.config.get('invalid_key','handlers',False))+'<br /><br />')
        self.response.out.write(str(pc.config.dump())+'<br /><br />')            
        self.response.out.write('<br /><b>Done.</b>')
        
class PrintEnvironmentHandler(webapp.RequestHandler):

    def get(self):

        for name in os.environ.keys():
            self.response.out.write("%s = %s<br />\n" % (name, os.environ[name]))
        
class LoginHandler(webapp.RequestHandler):
    
    def get(self):
        self.redirect(users.create_login_url("/"))
        
class LogoutHandler(webapp.RequestHandler):
    
    def get(self):
        self.redirect(users.create_logout_url("/"))
        
class SetupProtos(webapp.RequestHandler):
    
    def get(self):

        global pc
        
        d = pc.api.data
        self.response.out.write('d = '+str(d))
        
#(r'^(/admin)(.*)$',appengine_admin.Admin),
application = webapp.WSGIApplication([('/protos',SetupProtos),('/env',PrintEnvironmentHandler),('/login',LoginHandler),('/logout',LogoutHandler),('/*',MainHandler)],debug=True)
        
def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()