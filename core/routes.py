import sys

from flask import abort, redirect, request
from flask_limiter.util import get_remote_address
import re

from core import utils
from core import app, limiter, interpolator, tree, modeldf

import numpy as np
import pandas as pd
from scipy.interpolate import NearestNDInterpolator as NIP
from scipy import spatial

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    return (
        "Error 404: Page not found<br /> \
        Check your spelling to ensure you are accessing the correct endpoint.",
        404,
    )


@app.errorhandler(400)
def missing_parameter(e):
    return (
        '{"Error 400": "Incorrect parameters or too many results to return \
        (maximum of 1000 in a single request)<br /> \
        Check your request and try again."}',
        400,
    )


@app.errorhandler(429)
def ratelimit_handler(e):
    return '{"Error 429": "You have exceeded your rate limit:<br />' + e.description + ' "}', 429


@app.errorhandler(500)
def internal_server_error(e):
    return '{"Error 500": "Internal server error:<br />' + e.description + ' "}', 500


# Redirects user to the Center for the Protection of Dark and Quiet Sky homepage
@app.route("/")
def root():
    return redirect("https://apexgroup.web.illinois.edu/")

# The fun starts here
@app.route("/stabilityborders/")
def stabilityborders():
    """Interpolates 
    
    Parameters:
    -----------
    interpolator ... scipy interpolation function 
    point
    
    
    Returns:
    --------
    interpolated_data ...  array(7)
 
    
    nearest neighbors from database ... JSON string
    """
    
    global interpolator 
   
    m1 = request.args.get("m1")
    m2 = request.args.get("m2")
    mp = request.args.get("mp")
    ab = request.args.get("ab")
    eb = request.args.get("eb")
    ep = request.args.get("ep")
    ip = request.args.get("ip")
    wp = request.args.get("wp")
    nodep = request.args.get("nodep")
    
    point = np.array([  float(m1),float(m2),float(mp),
			float(ab),float(eb),float(ep),
			float(ip),float(wp),float(nodep)])
   
    # check for mandatory parameters
    if [x for x in point if x is None]:
        abort(400)
 
     # check for parameter values
    if [x for x in point if x < 0]:
        abort(400)
    
    if (point[4] > 1): abort(400)
    if (point[5] > 1): abort(400)
    if (point[6] > 360): abort(400)
    if (point[7] > 360): abort(400)
    if (point[8] > 360): abort(400)	
	

    # ipoint=[log10Mb,log10Mp,i,eb,ep,node,wp]
    ipoint = utils.point2ipoint(point)
    
    # Interpolate input
    iresult = interpolator(ipoint)[0]
    #print(iresult)
   
    scaledresult = float(ab)*10.**iresult 
 
    # convert interpolation result to JASON format
    result = utils.iresult2JASON(point,scaledresult)
    
    return result

@app.route("/closestgridpoints/")
def closestgridpoints(outheader=['m1','m2','mp','ab',
                                 'eb','ep','ip','wp','nodep',
                                 'inner_border','outer_border',
                                 'tree_distance'], npoints=5,p1=5,p2=8,p3=2,
                                 myorient='records'):

    """Determine model gridpoints closest to requested system."""
    global tree, modeldf

    m1 = request.args.get("m1")
    m2 = request.args.get("m2")
    mp = request.args.get("mp")
    ab = request.args.get("ab")
    eb = request.args.get("eb")
    ep = request.args.get("ep")
    ip = request.args.get("ip")
    wp = request.args.get("wp")
    nodep = request.args.get("nodep")
    npoints = request.args.get("npoints")
    myorient = request.args.get("orient")

    point = np.array([  float(m1),float(m2),float(mp),
                        float(ab),float(eb),float(ep),
                        float(ip),float(wp),float(nodep)])

    # check for mandatory parameters
    if [x for x in point if x is None]:
        abort(400)
    
   # check for parameter values
    if [x for x in point if x < 0]:
        abort(400)

    if (point[4] > 1): abort(400)
    if (point[5] > 1): abort(400)
    if (point[6] > 360): abort(400)
    if (point[7] > 360): abort(400)
    if (point[8] > 360): abort(400)
    if (float(npoints) > 200): abort(400)


    # ipoint=[log10Mb,log10Mp,i,eb,ep,node,wp]
    ipoint = utils.point2ipoint(point)
    
    qresdd, qresii =tree.query(ipoint, int(npoints))
    
    dfaspect = modeldf.iloc[qresii]
    neighbordf = dfaspect.copy()
    neighbordf.reset_index(inplace=True, drop=True)   
 
    neighbordf['inner_border'] = round(10.**neighbordf['inner']*float(ab),p1)
    neighbordf['outer_border'] = round(10.**neighbordf['outer']*float(ab),p1)
    neighbordf['m1'] = point[0]
    neighbordf['m2'] = round((10.**neighbordf['Mb'])*(point[0]+point[1]),p1)
    neighbordf['mp'] = round((10.**neighbordf['Mp'])*(point[0]+point[1]),p2)
    neighbordf['ab'] = point[3]
    neighbordf['ip'] = round(np.rad2deg(neighbordf['i']),p3)
    neighbordf['wp'] = round(np.rad2deg(neighbordf['wp']),p3)
    neighbordf['nodep'] = round(np.rad2deg(neighbordf['node']),p3)
    neighbordf['tree_distance'] = qresdd.round(p2)

    return neighbordf[outheader].to_json(orient=str(myorient))


def get_forwarded_address(request):
    forwarded_header = request.headers.get("X-Forwarded-For")
    if forwarded_header:
        return request.headers.getlist("X-Forwarded-For")[0]
    return get_remote_address

