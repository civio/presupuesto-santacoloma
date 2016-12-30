# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, url
#from django.conf.urls.i18n import i18n_patterns


MAIN_ENTITY_LEVEL = 'municipio'

# Main entity name. Must be the same used in data/entidades.csv
MAIN_ENTITY_NAME = 'Santa Coloma de Gramenet'

# Theme Budget Loader class name. Default: 'SimpleBudgetLoader'
BUDGET_LOADER = 'SantacolomaBudgetLoader'

# Theme Payments Loader class name. Default: 'PaymentsLoader'
# PAYMENTS_LOADER = 'SantacolomaPaymentsLoader'


# Show / hide Settings
# ----------------------

# Show Payments section in menu & home options. Default: False.
# SHOW_PAYMENTS = True

# Configure 'by area' payment breakdown. Default: ['area', 'payee', 'description']
# PAYMENTS_BREAKDOWN_BY_AREA = ['area', 'payee', 'description']

# Configure 'by payee' payment breakdown. Default: ['payee', 'area', 'description']
# PAYMENTS_BREAKDOWN_BY_PAYEE = ['payee', 'area', 'description']

# Show Tax Receipt section in menu & home options. Default: False.
# SHOW_TAX_RECEIPT = True

# Show Counties & Towns links in Policies section in menu & home options. Default: False.
# SHOW_COUNTIES_AND_TOWNS = True

# Search in entity names. Default: False.
# SEARCH_ENTITIES = True


# Budget Settings
# ----------------------

# Show an extra tab with institutional breakdown. Default: True.
# SHOW_INSTITUTIONAL_TAB  = False

# Show section pages. Still under development, see #347. Default: False.
# SHOW_SECTION_PAGES = True

# Are institutional codes consistent along the years. Default: False.
# Important: We need this to be True for the institutional treemap to work properly.
# CONSISTENT_INSTITUTIONAL_CODES = True

# Show an extra treemap in the Policy page, showing institutional breakdown. Default: False.
# Important: insitutional codes must be consistent along the years, see CONSISTENT_INSTITUTIONAL_CODES.
# SHOW_GLOBAL_INSTITUTIONAL_TREEMAP  = True

# Show an extra tab with funding breakdown (only applicable to some budgets). Default: False.
# SHOW_FUNDING_TAB = True

# Show an extra column with actual revenues/expenses. Default: True.
# Warning: the execution data still gets shown in the summary chart and in downloads.
# SHOW_ACTUAL = False

# Should we group elements at the economic subheading level, or list all of them,
# grouping by uid?. Default: True. (i.e. group by uid, show all elements)
# BREAKDOWN_BY_UID = False

# Include financial income/expenditures in overview and global policy breakdowns. Default: True.
# INCLUDE_FINANCIAL_CHAPTERS_IN_BREAKDOWNS = False

# Does the data includes a fifth functional classification level, subprogrammes?. Default: False
# USE_SUBPROGRAMMES = True


# Theme Settings
# ----------------------

# Supported languages. Default: ('es', 'Castellano')
LANGUAGES = (
  ('ca', 'Catal&agrave;'),
  ('es', 'Castellano'),
  # ('en', 'English'),
  # ('eu', 'Euskera'),
  # ('gl', 'Galego'),
)

# Facebook Aplication ID used in social_sharing temaplate. Default: ''
# In order to get the ID create an app in https://developers.facebook.com/
FACEBOOK_ID             = '240343343055114'

# Google Analytics ID. Default: ''
# In order to get the ID create a Google Analytics Acount in https://analytics.google.com/analytics/web/
ANALYTICS_ID            = 'UA-28946840-27'

# Setup Data Source Budget link
DATA_SOURCE_BUDGET      = 'http://www.gramenet.cat/ajuntament/info-economica/pressupost/'

# Setup Data Source Population link
DATA_SOURCE_POPULATION  = 'http://www.ine.es/jaxiT3/Tabla.htm?t=2861&L=0'

# Setup Data Source Inflation link
DATA_SOURCE_INFLATION   = 'http://www.ine.es/jaxiT3/Tabla.htm?t=10023&L=0'

# Setup Main Entity Web Url
MAIN_ENTITY_WEB_URL     = 'http://www.gramenet.cat/'

# Setup Main Entity Legal Url (if empty we hide the link)
MAIN_ENTITY_LEGAL_URL   = 'http://www.gramenet.cat/popups/avis-legal/'

# Setup Main Entity Legal Url (if empty we hide the link)
# MAIN_ENTITY_PRIVACY_URL = ''

# External URL for Cookies Policy (if empty we use out template page/cookies.html)
# COOKIES_URL             = ''

# We can define additional URLs applicable only to the theme. These will get added
# to the project URL patterns list.
# Must be needed to uncomment 3rd line in order to import i18n_patterns
# EXTRA_URLS = i18n_patterns('presupuesto-base.views',
#     url(r'^visita-guiada$', 'guidedvisit', name="guidedvisit"),
# )


# Welcome Settings
# ----------------------

# Programmes to feature as example in home page.
FEATURED_PROGRAMMES = ['1620', '1710', '3370', '2410', '3110']

# Number of programmes to feature in home page. Default: 3
# NUMBER_OF_FEATURED_PROGRAMMES = 3


# Overview Settings
# ----------------------

OVERVIEW_INCOME_NODES = [
                            {
                              'nodes': [['11', '113']],
                              'label.ca': 'Impost sobre béns immobles de naturalesa urbana',
                              'label.es': 'Impuesto a bienes inmuebles de naturaleza urbana',
                              'link_id': '11'
                            },
                            {
                              'nodes': [['11', '115']],
                              'label.ca': 'Impost sobre vehicles de tracció mecànica',
                              'label.es': 'Impuesto sobre vehículos de tracción mecánica',
                              'link_id': '11'
                            },
                            '13', '42', '45', '30', '33'
                        ]


OVERVIEW_EXPENSE_NODES = ['16', '17', '33', '92']

# How much padding between Sankey nodes. Default: 10 (Optional)
# Note: higher values will result in a more 'curvy accordion'.
# OVERVIEW_NODE_PADDING = 15

# How aggresive should the Sankey diagram reorder the nodes. Default: 0.79 (Optional)
# Note: 0.5 usually leaves nodes ordered as defined. 0.95 sorts by size (decreasing).
# OVERVIEW_RELAX_FACTOR = 0.5

# Adjust inflation in amounts in Overview page. Default: True
# ADJUST_INFLATION_IN_OVERVIEW = False

# Show Subtotals panel in Overview. Default: False
# SHOW_OVERVIEW_SUBTOTALS = True

# Calculate budget indicators (True), or show/hide the ones hardcoded in HTML (False). Default: True.
# CALCULATE_BUDGET_INDICATORS = False


# Treemap Settings
# ----------------------

# Treemaps minimum height or width to show labels. Default: 70 (Optional)
# TREEMAP_LABELS_MIN_SIZE = 70

# Allow overriding of default treemap color scheme
# COLOR_SCALE = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#e7969c', '#bcbd22', '#17becf']

# How many levels to show in the global institutional treemap? Default: 1.
# INSTITUTIONAL_MAX_LEVELS = 2
