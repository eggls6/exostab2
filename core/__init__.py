import sys

from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

import pandas as pd
from scipy.interpolate import NearestNDInterpolator as NIP
from scipy import spatial

# from core import utils

def create_app():

    app = Flask(__name__)

    return app


app = create_app()


limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["100 per second", "2000 per minute"],
)

def create_csv_interpolator(path2model="./data/georgakarakos2024.csv", separator=",", header=['Mb', 'Mp', 'i', 'eb', 'ep','node','wp','inner','outer']):
    
    # Read stability model into pandas dataframe
    # header=['a','e','i','residence_time','cumulative_residence_time','nu6','3:1','IMC','OMB','JFC']
    df = pd.read_csv(path2model, sep=separator)

    if (set(df.columns) != set(header)):
        abort(400)
	    
    # Create interpolator
    interpolator = NIP(df[header[0:7]],df[header[7:]],rescale=True)
    
    return interpolator


interpolator = create_csv_interpolator()


def makeKDtree(path2model="./data/georgakarakos2024.csv", separator=",", header=['Mb', 'Mp', 'i', 'eb', 'ep','node','wp','inner','outer']):
    """Create a KDtree from the stability grid data to allow for neighboring gridpoint queries."""
    
    dfg = pd.read_csv(path2model,sep=separator)
    
    #check if every column is present
    if (set(header) != set(dfg.columns)):
        abort(400)
        
    #create cKDTree    
    coordinates = dfg[header[0:7]].to_numpy()
    tree = spatial.cKDTree(coordinates)
    
    return tree, dfg


tree, modeldf = makeKDtree()


from core import routes  # noqa: E402, F401, I001
