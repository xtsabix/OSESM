#import numpy
import math

print(f"TEST-Ausgabe")

def impedance_serial(r1, r2, C, f):  #r1, r2 .. Resistance, C ... Capacity, f ... frequency
    return r1+r2+1/(math.j*2*math.pi*f*C);

def impedance_prallel(r1, r2, C, f):
    return 1/((1/r1)+(1/r2)+(math.j*2*math.pi*f*C));

def check_cos_phi(cos_phi):    
    if 0 < cos_phi < 1:
        print(f"cos(phi) = {cos_phi:.3f} ist im gültigen Bereich.")
        return True
    else:
        print(f"Fehler: cos(phi) = {cos_phi:.3f} liegt außerhalb des Bereichs (0,1).")
        return False

def characteristics_serial_voltage(r1,r2,C,f, u, cos_phi): # u ... Voltage_rms, 0<cos_phi<=1, 
  if check_cos_phi(cos_phi):
      s=u**2/impedance_serial(r1, r2, C, f) # S=U*I , I=U/R ==> S=U^2/R
      p=s*cos_phi;
      q=math.sqrt(s**2-p**2)
      return f"Scheinleistung: = {s:.3f}VA; (Zusatzinfo:P={p:.3f}W; Q={p:.3f}VAr) "
  

def characteristics_serial_current(r1,r2,C,f, i, cos_phi): # i ... Voltage_rms, 0<cos_phi<=1, 
  if check_cos_phi(cos_phi):
      s=i**2*impedance_prallel(r1, r2, C, f) # S=U*I , I=U/R ==> S=U^2/R
      p=s*cos_phi;
      q=math.sqrt(s**2-p**2)
      return f"Scheinleistung: = {s:.3f}VA; (Zusatzinfo:P={p:.3f}W; Q={p:.3f}VAr) "
