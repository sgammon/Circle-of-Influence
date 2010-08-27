# -*- coding: utf-8 -*-

from tipfy import RequestHandler, Response, redirect
from tipfy.ext.jinja2 import render_response
from ProvidenceClarity.main import PCException

from coi import COI

class FaviconHandler(COI, RequestHandler):
    
    def get(self):
        
        """ Returns the current favicon. """
        return redirect('/assets/images/static/favicon.ico')
        

class DemoHandler(COI, RequestHandler):
    
    def get(self):
        
        """ Experiments with the Stanford Protovis library. """
        raise PCException
        return render_response("protovis_graph.html")