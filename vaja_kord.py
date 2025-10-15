from astropy import units as u

from astropy.coordinates import SkyCoord
from astropy.coordinates import ICRS, Galactocentric, LSR, HeliocentricTrueEcliptic, GalacticLSR
from astropy.coordinates import CartesianRepresentation

c = SkyCoord(ra = 11.5, dec = -4, unit = 'deg', frame = 'icrs')
"""#ali
c = SkyCoord(ra = 11.5*u.deg, dec = -4*u.deg, frame = ICRS)

#za več objektov
c  = SkyCoord(ra = [11.5, 196.3, -300.2], dec = [-4, 0.0, 10.5], unit = 'deg', frame = 'icrs')

c = SkyCoord.from_name('M3')
"""
#print(c)
#print(c.ra, c.dec.deg) #po defaultu ti v urah izpise idk why

c = SkyCoord(ra = 11.5*u.deg , dec = -4*u.deg, pm_ra_cosdec = 4*u.mas/u.yr, pm_dec = -20*u.mas/u.yr, 
                distance = 3.0*u.kpc, radial_velocity = 2.0*u.km/u.s, frame = 'icrs')

"""c = SkyCoord(l = 0*u.deg, b = 0*u.deg, frame = 'galactic')

c = SkyCoord(x = 1.3*u.kpc, y = 2.0*u.kpc, z = 20.5*u.kpc, 
             v_x = 0*u.km/u.s, v_y = 220*u.km/u.s, v_z = 0*u.km/u.s,
             frame = 'heliocentrictrueecliptic', representation_type = 'cartesian')"""

#print(c)


d = c.transform_to('icrs')

#print(d)

e = c.transform_to(Galactocentric())



f = c.transform_to(HeliocentricTrueEcliptic(representation_type='cartesian',
                                            differential_type='cartesian')) #dif type za hitrost

print(f.cartesian.x)
print(f.cartesian.y)
print(f.cartesian.z)
print(f.velocity.d_x)
print(f.velocity.d_y)
print(f.velocity.d_z)


g = c.transform_to(LSR(representation_type='cartesian',
                      differential_type='cartesian')) 

print(g)

print(g.cartesian) #naredi le x,y,z ne hitrosti
print(g.velocity) #hitrost

h = c.transform_to(GalacticLSR())

print(h)
print(h.cartesian)
print(h.velocity)