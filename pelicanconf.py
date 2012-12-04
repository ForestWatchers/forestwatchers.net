#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"ForestWatchers.net"
SITENAME = u"ForestWatchers.net"
SITEURL = 'http://forestwatchers.net'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 4
THEME = 'theme'
STATIC_PATHS = (['images'])
FEED_DOMAIN = 'http://forestwatchers.net'
GOOGLE_ANALYTICS = 'UA-31623277-1'

DISQUS_SHORTNAME = 'forestwatchers'

OUTPUT_STATIC_DIR = 'assets'

# PAGES setup
INDEX_SAVE_AS = 'blog/index.html'
PAGE_URL = ('{slug}.html')
PAGE_SAVE_AS = ('{slug}.html')
PAGE_LANG_URL = ('{lang}/{slug}.html')
PAGE_LANG_SAVE_AS = ('{lang}/{slug}.html')

# ARTICLE setup
ARTICLE_URL = ('blog/{slug}.html')
ARTICLE_SAVE_AS = ('blog/{slug}.html')
ARTICLE_LANG_URL = ('{lang}/blog/{slug}.html')
ARTICLE_LANG_SAVE_AS = ('{lang}/blog/{slug}.html')
SUMMARY_MAX_LENGTH = 20
