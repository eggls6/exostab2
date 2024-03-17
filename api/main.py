"""
Exostab 2.0 - Dynamical Stability Assessment for Extra Solar Planets
"""

__version__ = "0.1.0"


import os
import sys

from core import app

sys.path.insert(0, os.path.dirname(__file__))


def residence_times(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    message = 'It works!\n'
    version = 'Python v' + sys.version.split()[0] + '\n'

    response = '\n'.join([message, version])
    return [response.encode()]
