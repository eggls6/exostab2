About Exostab 2.0
================
This service provides dynamical stability limit predictions for circumbinary planets, based on user specified system parameters. 
An :ref:`API` query to `https://apexgroup.web.illinois.edu/stability/circumbinary/` returns actual simulation results for the system closest to your query input parameters from a set of long term numerical simulations discussed in Georgakarakos et al. (2024).
A call to `https://apexgroup.web.illinois.edu/stability/circumbinarygrid/` returns a list of systems similar to the desired system. 
Results are ranked starting with the configuraiton that is closest to the desired system (Rank 0). Similar systems are presented ordered by the KDtree distance (tree distance) in the database. For each system two stability limits are provided:

#. The inner stability border: The inner border provides the planetary semimajor axis that separates unstable zones near the binary from areas with potentially mixed stable and unstable orbits.
#. The outer stability border: The outer border provides the planetary semimajor axis that separates potentially mixed stable and unstable zones with zones of orbital stability

There are likely no planets orbiting stellar binaries closer than the inner border. Almost all circumbinary planets found so far are orbiting the double star beyond the outer border. The region between the inner and outer border can be considered a "gray zone" featuring islands of stability and instability. Systems that would fall into that zone require a dedicated investigation to assertain their dynamical stability.

Dynamical Model
---------------
The dynamical model used in the calculations so far is the Newtonian gravitational three body problem. 
Relativistic and tidal limits of this model are discussed in, e.g. Naoz et al. (2013) and Correia et al. (2016).  


Numerical Integration Method
----------------------------
At the heart of our simulations is the logarithmic Hamiltonian leapfrog integrator (LHLI) with time
transformation developed in Mikkola (1997). This code is not only symplectic in nature which guarantees adequate
conservation of system energy and angular momentum, it is also one of the few symplectic algorithms that can handle
highly eccentric orbits and strong, localized gravitational interactions without loss of accuracy.

References
----------
Correia, A. C., Boue, G., and Laskar, J. 2016, Celestial Mechanics and Dynamical Astronomy, 126, 189
Georgakarakos, N., Eggl, S., Ali-Dib and Dobbs-Dixon, I., submitted. 
Mikkola, S., 1997. Practical Symplectic Methods with Time Transformation for the Few-Body Problem. Celestial Mechanics and Dynamical Astronomy 67, 145–165.
Naoz, S., Kocsis, B., Loeb, A. and Yunes, N., 2013. Resonant post-Newtonian eccentricity excitation in hierarchical three-body systems. The Astrophysical Journal, 773(2), p.187.
