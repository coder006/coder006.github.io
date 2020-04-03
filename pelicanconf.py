#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ambar Mehrotra'
SITENAME = 'All Things Connected'
SITEURL = 'https://ambar.dev'

PATH = 'content'

TIMEZONE = 'Asia/Calcutta'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = 'feeds/all.atom.xml'
# FEED_ALL_RSS = 'feeds/all.rss.xml'
# AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
RSS_FEED_SUMMARY_ONLY = False

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('email', 'mehrotraambar@gmail.com'),
          ('twitter', 'https://twitter.com/decoder006'),
          ('github', 'https://github.com/coder006'),
          ('dev', 'https://dev.to/_notanengineer'))

DEFAULT_PAGINATION = 10

THEME = "themes/hyde"
STATIC_PATHS = ['images', 'extra']
PROFILE_IMAGE = "profile-picture.jpeg"
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True