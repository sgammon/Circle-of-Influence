import os, logging
from . import COIRequestHandler, COIResponse


class PlatformHandler(COIRequestHandler):
    
    def get(self):
        
        """ Outputs the platform objects' info. """
        
        response = "<b>Object: </b><pre>%s</pre>\n\n" % str(self.platform)
        response = response + "<br /><b>DataController: </b><pre>%s</pre>\n\n" % str(self.platform.api.data)
        response = response + "<br /><b>Handler: </b><pre>%s</pre>\n\n" % str(self)
        response = response + "<br /><b>Dir: </b><br /><pre>%s</pre>\n\n" % str(dir(self.platform))
        
        return COIResponse(response)
        

class EnvHandler(COIRequestHandler):
    
    def get(self):
        
        """ Returns the current favicon. """
        
        stack = ''
        for entry in os.environ:
            stack = stack+'<li><b>'+str(entry)+'</b>: '+str(os.environ[entry])+'</li>'
        
        return COIResponse('<ul>%s</ul>' % stack)