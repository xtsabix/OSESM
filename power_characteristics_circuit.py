import cmath
import math


# Funktion zur Berechnung der Impedanz in einer Serienschaltung
def berechne_impedanz_serien(r1, c, f):
    omega = 2 * math.pi * f
    z_r = r1  # Impedanz des Widerstands (reell)
    z_c = complex(0, -1 / (omega * c))  # Impedanz des Kondensators (imaginär)
    z_gesamt = z_r + z_c  # Gesamtimpedanz in Serie
    return z_gesamt


# Funktion zur Berechnung der Impedanz in einer Parallelschaltung
def berechne_impedanz_parallel(r2, c, f):
    omega = 2 * math.pi * f
    z_r=r2  # Impedanz des Widerstands (reell)
    z_c=complex(0, -1 / (omega * c))  # Impedanz des Kondensators (imaginär)
    # Gesamtimpedanz in Parallel
    z_gesamt = 1 #/ (1 / z_r + 1 / z_c)
    return z_gesamt


# Funktion zur Berechnung von Scheinleistung, Wirkleistung und Blindleistung
def berechne_leistungen(u, z_gesamt):
    z_betrag = abs(z_gesamt)  # Betrag der Impedanz
    z_phase = cmath.phase(z_gesamt)  # Phasenwinkel der Impedanz

    i = u / z_betrag  # Strom (i = u / z)

    # Scheinleistung (S = u * i)
    s = u * i

    # Wirkleistung (P = u * i * cos(phi))
    p = u * i * math.cos(z_phase)

    # Blindleistung (Q = u * i * sin(phi))
    q = u * i * math.sin(z_phase)

    print(f"Scheinleistung: {s:.3f} VA; P={p:.3f} W; Q={q:.3f} VAr")

    return abs(s), abs(p), abs(q)
