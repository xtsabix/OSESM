import unittest
import cmath
import math
from power_characteristics_circuit import (
    berechne_impedanz_serien, 
    berechne_impedanz_parallel, 
    berechne_leistungen
)

class TestPowerCharacteristicsCircuit(unittest.TestCase):
    
    def test_berechne_impedanz_serien(self):
        """Test für die Berechnung der Impedanz in einer Serienschaltung."""
        r1 = 1  # Widerstand in Serie (Ohm)
        c = 1  # Kapazität (Farad)
        f = 1  # Frequenz (Hz)
        
        z_serien = berechne_impedanz_serien(r1, c, f)
        
        # Test: Prüfen, ob der reale Teil der Impedanz korrekt ist
        self.assertAlmostEqual(z_serien.real, 1, places=2, msg="Realer Teil der Impedanz ist falsch.")
        
        # Test: Prüfen, ob der Imaginärteil der Impedanz korrekt ist
        self.assertAlmostEqual(
            z_serien.imag, -0.15915494309189535, places=2, msg="Imaginärer Teil der Impedanz ist falsch."
        )
    
    def test_berechne_impedanz_parallel(self):
        """Test für die Berechnung der Impedanz in einer Parallelschaltung."""
        r2 = 1  # Widerstand in Parallel (Ohm)
        c = 1  # Kapazität (Farad)
        f = 1  # Frequenz (Hz)
        
        z_parallel = berechne_impedanz_parallel(r2, c, f)
        
        # Test: Prüfen, ob der reale Teil der Impedanz korrekt ist
        self.assertAlmostEqual(
            z_parallel.real, 0.024704523031857644, places=2, msg="Realer Teil der Impedanz in Parallel ist falsch."
        )
        
        # Test: Prüfen, ob der Imaginärteil der Impedanz korrekt ist
        self.assertAlmostEqual(
            z_parallel.imag, -0.15522309613464763, places=2, msg="Imaginärer Teil der Impedanz in Parallel ist falsch."
        )
    
    def test_berechne_leistungen(self):
        """Test für die Berechnung der Scheinleistung, Wirkleistung und Blindleistung."""
        u = 1  # Spannung in Volt (RMS)
        r1 = 1  # Widerstand in Serie (Ohm)
        c = 1  # Kapazität (Farad)
        f = 1  # Fre
