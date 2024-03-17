import numpy as np

#Internal
def iresult2JASON(x,r, p1 = 3, p2 = 8 ):
    myRound = np.round
    output = {"m_1":myRound(x[0],p1),
              "m_2": myRound(x[1],p1),
              "m_p": myRound(x[2],p2),
              "a_b": myRound(x[3],p2),
              "e_b": myRound(x[4],p1),
              "e_p": myRound(x[5],p2),
              "i_p": myRound(x[6],p2),
              "w_p": myRound(x[7],p2),
              "node_p": myRound(x[8],p2),
              
              "a_inner": myRound(r[0],p2),
              "a_outer": myRound(r[1],p2),
             }
    return output

def point2ipoint(point):

    # point = [m1,m2,mp,ab,eb,ep,ip,wp,nodep] 
    [m1,m2,mp,ab,eb,ep,ip,wp,nodep] = point 
    
    log10Mb = np.log10(m2/(m1+m2))
    log10Mp = np.log10(mp/(m1+m2))
    irad = np.deg2rad(ip)
    noderad = np.deg2rad(nodep)
    wprad = np.deg2rad(wp)
    
    ipoint = [log10Mb,log10Mp,irad,eb,ep,noderad,wprad]
    return ipoint



