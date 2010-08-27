# -*- coding: utf-8 -*-
"""
    urls
    ~~~~

    URL definitions.

    :copyright: 2009 by tipfy.org.
    :license: BSD, see LICENSE.txt for more details.
"""
from tipfy import Rule


def get_rules(app):
    """Returns a list of URL rules for the Hello, World! application.

    :param app:
        The WSGI application instance.
    :return:
        A list of class:`tipfy.Rule` instances.
    """
    rules = [
        Rule('/', endpoint='pc-index', handler='coi.handlers.DemoHandler'),
        Rule('/favicon.ico', endpoint='favicon', handler='coi.handlers.FaviconHandler'),        

        ## Dev Rules
        Rule('/dev/env', endpoint='pc-dev-env', handler='coi.handlers.dev.EnvHandler'),
        Rule('/dev/platform', endpoint='pc-dev-platform', handler='coi.handlers.dev.PlatformHandler'),        

    ]

    return rules