#     ______                  __   __
#    /_  __/_      __ __  __ / /_ / /_   ____   ____
#     / /  | | /| / // / / // __// __ \ / __ \ / __ \
#    / /   | |/ |/ // /_/ // /_ / / / // /_/ // / / /
#   /_/    |__/|__/ \__, / \__//_/ /_/ \____//_/ /_/
#                  /____/

"""
Twython
-------

Twython is a library for Python that wraps the Twitter API.

It aims to abstract away all the API endpoints, so that additions to the library
and/or the Twitter API won't cause any overall problems.

Questions, comments? ryan@venodesigns.net
"""

__author__ = 'Ryan McGrath <ryan@venodesigns.net>'
__version__ = '2.9.0'

from .twython import Twython
from .streaming import TwythonStreamer, TwythonStreamHandler
from .exceptions import TwythonError, TwythonRateLimitError, TwythonAuthError
