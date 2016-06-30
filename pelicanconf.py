#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'wumb0'
SITENAME = u'wumb0.in'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#--------------User Conf----------------
CSS_FILES = ("http://yui.yahooapis.com/pure/0.6.0/pure-min.css", "http://yui.yahooapis.com/pure/0.6.0/grids-responsive-min.css", '/theme/custom.css')
THEME = 'themes/mytheme1'
FAVICON = 'skel/images/favicon.png'
PLUGINS = [ 'pelican_fontawesome',] #'minification' ]
#--------------/User Conf----------------