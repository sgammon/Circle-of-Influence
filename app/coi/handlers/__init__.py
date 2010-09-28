# -*- coding: utf-8 -*-

from tipfy import RequestHandler, Response, redirect
from tipfy.ext.jinja2 import render_response

from ProvidenceClarity.exceptions import PCException
from coi import CircleOfInfluence as COI


class COIRequestHandler(RequestHandler):

    def __init__(self, *args, **kwargs):
        
        self.platform = COI()
        super(COIRequestHandler, self).__init__(*args, **kwargs)
    

class COIResponse(Response):
    pass
    

class FaviconHandler(COIRequestHandler):
    
    def get(self):
        
        """ Returns the current favicon. """
        return redirect('/assets/images/static/favicon.ico')
        

class DemoHandler(COIRequestHandler):
    
    def get(self):
        
        """ Experiments with the Stanford Protovis library. """
        return render_response("protovis_graph.html")