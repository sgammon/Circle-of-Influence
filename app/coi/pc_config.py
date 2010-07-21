import os
import logging

config = {

    'platform':
    {
        'name':'Circle of Influence',
        'public':False
    },

    'logging':
    {
        'handler':logging,
        'tag':True,
        'threshold':'debug'
    },
    
    'data':
    {
        'index_on_put': True,
        'path_prefix': False,
        'import_prefix': False
    },
    
    'handlers':
    {
        'template_root':'templates/',
        'images_url':'/assets/images/static/p-c/',
        'style_url':'/assets/style/static/p-c/',
        'script_utl':'/assets/script/static/p-c/'
    },
    
    'security':
    {
        'enable_security':False,
    }

}

def get(key,module,default=None):
    
    if module in config:
        if key in config[module]:
            return config[module][key]
        else: return default
    else: return default
    
def dump():
    
    return config    