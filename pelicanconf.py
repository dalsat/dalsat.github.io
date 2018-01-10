#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tommaso Dal Sasso'
SITENAME = 'Tommaso Dal Sasso'
SITEURL = ''

THEME = 'themes/ilredeitopi'
PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

STATIC_PATHS = ['images', 'download', 'CNAME']
ARTICLE_PATHS = ['posts']
ARTICLE_URL = 'posts/{date:%Y-%m-%d}-{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y-%m-%d}-{slug}/index.html'
AUTHOR_SAVE_AS = ''

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
        #   ('Another social link', '#'),)

# ('tag', 'url', 'icon')
SOCIAL = (
    ("GitHub", "https://github.com/ilredeitopi", "github"),
    ("SmalltalkHub", "http://smalltalkhub.com/#!/~dalsat", "rocket"),
    ("Twitter", "https://twitter.com/ilredeitopi", "twitter"),
    ("Email", "mailto:tommaso [dot] dalsasso [at] gmail [dot] com", "envelope"),
    # ("Blog", SITEURL + "/blog", "paragraph")
)


DEFAULT_PAGINATION = False
SHOW_BLOG_MENU = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
