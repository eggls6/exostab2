Exostab 2.0 API
=============

Retrieve stability borders for a circumbinary planet
-----------------------------------------------------------

.. http:get:: /circumbinary/
   :noindex:

   Retrieve stability borders for circumbinary planets

   :query m1: (*required*) -- Mass of primary star [Msun]
   :query m2: (*required*) -- Mass of secondary star [Msun]
   :query mp: (*required*) -- Mass of circumbinary planet [Msun]
   :query ab: (*required*) -- Semimajor axis of binary star orbit [au]
   :query eb: (*required*) -- Eccentricity of binary star orbit 
   :query ep: (*required*) -- Eccemtricity (initial) of circumbinary planet orbit 
   :query ip: (*required*) -- Inclination of circumbinary planet orbit with respect to binary orbit [deg]
   :query wp: (*required*) -- Argument of periapsis of circumbinary planet orbit [deg]
   :query nodep: (*required*) -- Longitude of the ascending node of circumbinary planet orbit [deg]


**Example Request**
    .. tabs::

        .. code-tab:: browser
            https://apexgroup.web.illinois.edu/stability/circumbinary/?m1=1&m2=0.5&mp=0.0001&ab=0.5&eb=0.3&ep=0.5&ip=20&wp=90&nodep=0

        .. code-tab:: python

            import requests
            import json

            url = 'https://apexgroup.web.illinois.edu/stability/circumbinary/;'
            params = {      'm1': 1,
                            'm2': 0.5,
                            'mp': 0.0001,
                            'ab': 0.5,
                            'eb': 0.3,
                            'ep': 0.5,
                            'ip': 20,
                            'wp': 90,
                            'nodep': 0,
                            }
            r = requests.get(url, params=params)
            print(json.dumps(r.json(), indent=4))

        .. code-tab:: bash

            curl -X GET "https://apexgroup.web.illinois.edu/stability/circumbinary/?m1=1&m2=0.5&mp=0.0001&ab=0.5&eb=0.3&ep=0.5&ip=20&wp=90&nodep=0" -H "accept: application/json"


**Example Response**

.. sourcecode:: json

    [
        {"a_b":0.5,"a_inner":3.74998909,"a_outer":4.09996363,"e_b":0.3,"e_p":0.5,"i_p":20.0,"m_1":1.0,"m_2":0.5,"m_p":0.0001,"node_p":0.0,"w_p":90.0}
        ,
            
        {"a_b":0.5,"a_inner":3.74998909,"a_outer":4.09996363,"e_b":0.3,"e_p":0.5,"i_p":20.0,"m_1":1.0,"m_2":0.5,"m_p":0.0001,"node_p":0.0,"w_p":90.0}
    ]


Retrieve nearby stability border grid for a circumbinary planet
---------------------------------------------------------------

.. http:get:: /circumbinarygrid/
    :noindex:

    Returns model gridpoints with stability limits closest to requested system.

    :query m1: (*required*) -- Mass of primary star [Msun]
    :query m2: (*required*) -- Mass of secondary star [Msun]
    :query mp: (*required*) -- Mass of circumbinary planet [Msun]
    :query ab: (*required*) -- Semimajor axis of binary star orbit [au]
    :query eb: (*required*) -- Eccentricity of binary star orbit 
    :query ep: (*required*) -- Eccemtricity (initial) of circumbinary planet orbit 
    :query ip: (*required*) -- Inclination of circumbinary planet orbit with respect to binary orbit [deg]
    :query wp: (*required*) -- Argument of periapsis of circumbinary planet orbit [deg]
    :query nodep: (*required*) -- Longitude of the ascending node of circumbinary planet orbit [deg]
    :query npoints: (*required*) -- Number of requested grid points (must be between 2 and 200) 
    :query myorient: (*optional*) -- Orientation of resulting JSON table (‘split’, ‘records’, ‘index’, ‘columns’, ‘values’, ‘table’) 

**Example Request**
    .. tabs::
        .. code-tab:: browser
            https://apexgroup.web.illinois.edu/stability/circumbinarygrid/?m1=1&m2=0.5&mp=0.0001&ab=0.5&eb=0.3&ep=0.5&ip=20&wp=90&nodep=0&npoints=8&orient=table

        .. code-tab:: python

            import requests
            import json

            url = 'https://apexgroup.web.illinois.edu/stability/circumbinarygrid/'
              params = {    'm1': 1,
                            'm2': 0.5,
                            'mp': 0.0001,
                            'ab': 0.5,
                            'eb': 0.3,
                            'ep': 0.5,
                            'ip': 20,
                            'wp': 90,
                            'nodep': 0,
                            'npoints: 8',
                            'myorient: table'
                            }
            r = requests.get(url, params=params)
            print(json.dumps(r.json(), indent=4))

        .. code-tab:: bash

            curl -X GET "https://apexgroup.web.illinois.edu/stability/circumbinarygrid/?m1=1&m2=0.5&mp=0.0001&ab=0.5&eb=0.3&ep=0.5&ip=20&wp=90&nodep=0&npoints=8&orient=table" -H "accept: application/json"


**Example Response**

.. sourcecode:: json

    [
      {"schema": {"fields":
                 [{"name":"index","type":"integer"},
                  {"name":"m1","type":"number"},
                  {"name":"m2","type":"number"},
                  {"name":"mp","type":"number"},
                  {"name":"ab","type":"number"},
                  {"name":"eb","type":"number"},
                  {"name":"ep","type":"number"},
                  {"name":"ip","type":"number"},
                  {"name":"wp","type":"number"},
                  {"name":"nodep","type":"number"},
                  {"name":"inner_border","type":"number"},
                  {"name":"outer_border","type":"number"},
                  {"name":"tree_distance","type":"number"}],
                  
                  "primaryKey":["index"],"pandas_version":"1.4.0"},
                  
                  "data":
                 [{"index":0,"m1":1.0,"m2":0.45,"mp":0.00015,"ab":0.5,"eb":0.3,"ep":0.5,"ip":18.0,"wp":90.0,"nodep":0.0,"inner_border":3.74999,"outer_border":4.09996,"tree_distance":0.18525769},
                  {"index":1,"m1":1.0,"m2":0.45,"mp":0.00015,"ab":0.5,"eb":0.2,"ep":0.5,"ip":18.0,"wp":90.0,"nodep":0.0,"inner_border":3.64998,"outer_border":3.84999,"tree_distance":0.21052414},
                  {"index":2,"m1":1.0,"m2":0.45,"mp":0.00015,"ab":0.5,"eb":0.3,"ep":0.4,"ip":18.0,"wp":90.0,"nodep":0.0,"inner_border":2.94999,"outer_border":3.2,"tree_distance":0.21052414},
                  {"index":3,"m1":1.0,"m2":0.45,"mp":0.00015,"ab":0.5,"eb":0.3,"ep":0.6,"ip":18.0,"wp":90.0,"nodep":0.0,"inner_border":5.1996,"outer_border":5.50009,"tree_distance":0.21052414},
                  {"index":4,"m1":1.0,"m2":0.45,"mp":0.00015,"ab":0.5,"eb":0.4,"ep":0.5,"ip":18.0,"wp":90.0,"nodep":0.0,"inner_border":4.0,"outer_border":4.20001,"tree_distance":0.21052414},
                  {"index":5,"m1":1.0,"m2":0.45,"mp":0.00015,"ab":0.5,"eb":0.2,"ep":0.6,"ip":18.0,"wp":90.0,"nodep":0.0,"inner_border":5.0,"outer_border":5.25013,"tree_distance":0.2330674},
                  {"index":6,"m1":1.0,"m2":0.45,"mp":0.00015,"ab":0.5,"eb":0.2,"ep":0.4,"ip":18.0,"wp":90.0,"nodep":0.0,"inner_border":2.80001,"outer_border":2.99999,"tree_distance":0.2330674},
                  {"index":7,"m1":1.0,"m2":0.45,"mp":0.00015,"ab":0.5,"eb":0.4,"ep":0.4,"ip":18.0,"wp":90.0,"nodep":0.0,"inner_border":3.09999,"outer_border":3.24997,"tree_distance":0.2330674}]
        }
    ]
