About Exostab 2.0
================
This service provides stability limits for circumbinary planets, based on system parameters. The query returns results of a list of systems similar to the desired system from a set of long term numerical simulations discussed in Georgakarakos et al. (2024). Results are ranked starting with the configuraiton that is closest to the desired system (Rank 0). Similar systems are presented ordered by the KDtree distance (tree distance) in the database. For each system two stability limits are provided:

#. The inner stability border: The inner border provides the planetary semimajor axis that separates unstable zones near the binary from areas with potentially mixed stable and unstable orbits.
#. The outer stability border: The outer border provides the planetary semimajor axis that separates potentially mixed stable and unstable zones with zones of orbital stability

There are likely no planets orbiting stellar binaries closer than the inner border. Almost all circumbinary planets found so far are orbiting the double star beyond the outer border. The region between the inner and outer border can be considered a "gray zone" featuring islands of stability and instability. Systems that would fall into that zone require a dedicated investigation to assertain their dynamical stability.
