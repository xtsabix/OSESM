import unittest
import cmath
import math
from power_characteristics_circuit import berechne_impedanz_serien, berechne_impedanz_parallel, berechne_leistungen

class TestPowerCharacteristicsCircuit(unittest.TestCase):
    
    def test_berechne_impedanz_serien(self):
        """Test für die Berechnung der Impedanz in einer Serienschaltung"""
        R1 = 1  # Widerstand in Serie (Ohm)
        C = 1  # Kapazität (Farad)
        f = 1  # Frequenz (Hz)
        
        Z_serien = berechne_impedanz_serien(R1, C, f)
        
        # Test: Prüfen, ob der reale Teil der Impedanz korrekt ist
        self.assertAlmostEqual(Z_serien.real, 1, places=2, msg="Realer Teil der Impedanz ist falsch.")
        
        # Test: Prüfen, ob der Imaginärteil der Impedanz korrekt ist
        self.assertAlmostEqual(Z_serien.imag, -0.15915494309189535, places=2, msg="Imaginärer Teil der Impedanz ist falsch.")
    
    def test_berechne_impedanz_parallel(self):
        """Test für die Berechnung der Impedanz in einer Parallelschaltung"""
        R2 = 1  # Widerstand in Parallel (Ohm)
        C = 1    # Kapazität (Farad)
        f = 1  # Frequenz (Hz)
        
        Z_parallel = berechne_impedanz_parallel(R2, C, f)
        
        # Test: Prüfen, ob der reale Teil der Impedanz korrekt ist
        self.assertAlmostEqual(Z_parallel.real, 0.024704523031857644, places=2, msg="Realer Teil der Impedanz in Parallel ist falsch.")
        
        # Test: Prüfen, ob der Imaginärteil der Impedanz korrekt ist
        self.assertAlmostEqual(Z_parallel.imag, -0.15522309613464763, places=2, msg="Imaginärer Teil der Impedanz in Parallel ist falsch.")
    
    def test_berechne_leistungen(self):
        """Test für die Berechnung der Scheinleistung, Wirkleistung und Blindleistung"""
        U = 1  # Spannung in Volt (RMS)
        R1 = 1  # Widerstand in Serie (Ohm)
        C = 1  # Kapazität (Farad)
        f = 1  # Frequenz (Hz)
        
        Z_serien = berechne_impedanz_serien(R1, C, f)
        
        # Berechne die Leistungen
        S, P, Q = berechne_leistungen(U, Z_serien)
        
        # Test: Überprüfe die Scheinleistung, Wirkleistung und Blindleistung
        self.assertGreater(S, 0, msg="Scheinleistung sollte positiv sein.")
        self.assertGreater(P, 0, msg="Wirkleistung sollte positiv sein.")
        self.assertGreater(Q, 0, msg="Blindleistung sollte positiv sein.")
        
        # Teste auch mit einer anderen Spannung
        U = 10  # Spannung in Volt (RMS)
        S, P, Q = berechne_leistungen(U, Z_serien)
        
        self.assertGreater(S, 0, msg="Scheinleistung für andere Spannung sollte positiv sein.")
        self.assertGreater(P, 0, msg="Wirkleistung für andere Spannung sollte positiv sein.")
        self.assertGreater(Q, 0, msg="Blindleistung für andere Spannung sollte positiv sein.")
    

# Wenn die Datei direkt ausgeführt wird, werden die Tests ausgeführt
if __name__ == "__main__":
    unittest.main()
