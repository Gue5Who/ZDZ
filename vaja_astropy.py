from astropy import units as u

v = 20 * u.km/u.s
 
t = 5 * u.s

s = v * t
print(s.to(u.pc))  # 100.0 

print(s.value)  # 100.0
print(s.unit)   # km


#Lahko definiramo svoje enote
kms = u.km / u.s
#ali
u.def_unit('kms', u.km / u.s)

v = 20 * kms
print(v)  # 20.0 km / s