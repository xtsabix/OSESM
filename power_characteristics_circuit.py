import cmath
import math

# Funktion zur Berechnung der Impedanz in einer Serienschaltung
def berechne_impedanz_serien(R1, C, f):
    omega = 2 * math.pi * f
    Z_R = R1  # Impedanz des Widerstands (reell)
    Z_C = complex(0, -1 / (omega * C))  # Impedanz des Kondensators (imaginär)
    Z_gesamt = Z_R + Z_C  # Gesamtimpedanz in Serie
    return Z_gesamt

# Funktion zur Berechnung der Impedanz in einer Parallelschaltung
def berechne_impedanz_parallel(R2, C, f):
    omega = 2 * math.pi * f
    Z_R = R2  # Impedanz des Widerstands (reell)
    Z_C = complex(0, -1 / (omega * C))  # Impedanz des Kondensators (imaginär)
    # Gesamtimpedanz in Parallel
    Z_gesamt = 1 / (1 / Z_R + 1 / Z_C)
    return Z_gesamt

# Funktion zur Berechnung von Scheinleistung, Wirkleistung und Blindleistung
def berechne_leistungen(U, Z_gesamt):
    Z_betrag = abs(Z_gesamt)  # Betrag der Impedanz
    Z_phase = cmath.phase(Z_gesamt)  # Phasenwinkel der Impedanz
    
    I = U / Z_betrag  # Strom (I = U / Z)
    
    # Scheinleistung (S = U * I)
    S = U * I
    
    # Wirkleistung (P = U * I * cos(phi))
    P = U * I * math.cos(Z_phase)
    
    # Blindleistung (Q = U * I * sin(phi))
    Q = U * I * math.sin(Z_phase)

    print(f"Scheinleistung: {S:.3f} VA; P={P:.3f} W; Q={Q:.3f} VAr")

    return abs(S), abs(P), abs(Q)