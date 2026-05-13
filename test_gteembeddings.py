# test_gteembeddings.py
"""
Tests for GTEEmbeddings module.
"""

import unittest
from gteembeddings import GTEEmbeddings

class TestGTEEmbeddings(unittest.TestCase):
    """Test cases for GTEEmbeddings class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GTEEmbeddings()
        self.assertIsInstance(instance, GTEEmbeddings)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GTEEmbeddings()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
