# test_decentromeshpro.py
"""
Tests for DecentroMeshPro module.
"""

import unittest
from decentromeshpro import DecentroMeshPro

class TestDecentroMeshPro(unittest.TestCase):
    """Test cases for DecentroMeshPro class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DecentroMeshPro()
        self.assertIsInstance(instance, DecentroMeshPro)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DecentroMeshPro()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
