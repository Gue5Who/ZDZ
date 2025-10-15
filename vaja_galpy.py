from matplotlib import pyplot as plt
from matplotlib import *
from pylab import *
import astropy.units as u
from galpy.potential import *
import numpy as np
from galpy.potential import MWPotential2014
from galpy.orbit import Orbit
from astropy.coordinates import SkyCoord


pot = KeplerPotential(amp=2.0e30*u.kg)

#one astronomical unit
au = 1.496e11*u.m
#print(pot.vcirc(au))

#izberemo svojo normalizacijo
pot = [KeplerPotential(amp=1.0),
       PlummerPotential(b = 0.5),
       HernquistPotential(a = 0.5),
       NFWPotential(a = 0.5),
       IsochronePotential(b = 0.5),
       PowerSphericalPotential(alpha = 2, amp = 0.07),
       HomogeneousSpherePotential(amp=0.1)]

x = np.linspace(0.001,10,1000)



#plt.figure()
#for i in pot:
#    y = [i.vcirc(r) for r in x]
#    plt.plot(x,y)
#plt.xlabel('r [ro]')
#plt.ylabel('vcirc [vo]')
#plt.title('Plummer potential with b=0.5ro')
#plt.legend(['Kepler','Plummer','Hernquist','NFW','Isochrone','PowerSpherical', 'HomogeneousSphere'])
#plt.xlim(0,10)
#plt.ylim(0,1.5)
#plt.show()


#zdruzevanje potencialov
pot_kepler = KeplerPotential(amp=0.3)
pot_plummer = PlummerPotential(b = 0.5, amp=0.3) 

pot = pot_kepler + pot_plummer

pot = MWPotential2014


#plt.figure()
#y = [vcirc(pot, r) for r in x]
#plt.plot(x,y)
##plt.xlabel('r [ro]')
#plt.ylabel('vcirc [vo]')
#plt.title('Combined potential')
#plt.legend(['Kepler + Plummer'])
#plt.xlim(0,10)
#plt.ylim(0,1.5)
#plt.show()


#orbit [R,v_r,v_T,z,v_z,phi] skoraj cilindrične
o = Orbit([1,0,1,0,0,0]) 

#print(e.E(pot = MWPotential2014))
#print(e.e(pot = MWPotential2014))

o = Orbit([8122 *u.pc, 0.0 * u.km/u.s, 240 * u.km/u.s])

print(o.E(pot = MWPotential2014))

o = Orbit([20* u.deg, 30 * u.deg, 2* u.kpc, -1* u.mas/u.yr, 2* u.mas/u.yr, 5 * u.km/u.s ]
          ,radec = True, ro = 8.122*u.kpc, vo = 233*u.km/u.s,
            solarmotion = np.array([-11.1, 24.0, 7.25])*u.km/u.s)

#print(o.E(pot = MWPotential2014))

c = SkyCoord(ra = 20* u.deg, dec = 30 * u.deg, distance = 2* u.kpc,
                pm_ra_cosdec = -1* u.mas/u.yr, pm_dec = 2* u.mas/u.yr,
                radial_velocity = 5 * u.km/u.s)

o = Orbit(c)

print(o.E(pot = MWPotential2014))


ts = np.linspace(0,600,10000)*u.Myr

o.integrate(ts, MWPotential2014)
#o.plot3d()
#plt.figure()
#plt.plot(-o.x(ts), o.y(ts), 'k-')
#plt.xlabel('x [ro]')
#plt.ylabel('y [ro]')
#plt.show()

o = Orbit([[1,0,1,0,0,0], [1,0.05,1,0,0,0], [1,-0.05, 1,0,0,0]])
ts = np.linspace(0,7, 1000)

o.integrate(ts, MWPotential2014)

for ob in o:
    plt.plot(-ob.x(ts), ob.y(ts))

plt.show()


#Navodilo za DN. Mej uvod z malo teorije