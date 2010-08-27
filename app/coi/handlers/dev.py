import os, logging
from coi import COI
from tipfy import RequestHandler, Response


class PlatformHandler(COI, RequestHandler):
    
    def get(self):
        
        """ Outputs the platform objects' info. """
        
        response = "<b>Object: </b><pre>%s</pre>\n\n" % str(self.platform)
        response = response + "<br /><b>Handler: </b><pre>%s</pre>\n\n" % str(self)
        response = response + "<br /><b>Dir: </b><br /><pre>%s</pre>\n\n" % str(dir(self.platform))
        
        return Response(response)


class EnvHandler(COI, RequestHandler):
    
    def get(self):
        
        """ Returns the current favicon. """
        
        stack = ''
        for entry in os.environ:
            stack = stack+'<li><b>'+str(entry)+'</b>: '+str(os.environ[entry])+'</li>'
        
        return Response('<ul>%s</ul>' % stack)