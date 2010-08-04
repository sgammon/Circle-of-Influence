# -*- coding: utf-8 -*-

from tipfy import RequestHandler, Response, redirect
from tipfy.ext.jinja2 import render_response


class FaviconHandler(RequestHandler):
    
    def get(self):
        
        """ Returns the current favicon. """
        
        return redirect('/assets/images/static/favicon.ico')
        

class DemoHandler(RequestHandler):
    
    def get(self):
        
        """ Experiments with the Stanford Protovis library. """
        
        return render_response("protovis_graph.html")