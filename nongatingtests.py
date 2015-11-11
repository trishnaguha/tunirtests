import unittest
import re
from .testutils import system

class TunirNonGatingtests(unittest.TestCase):

    def test_bash(self):
        """Tests the bash version as the same of upstream"""
        out, err, eid = system('bash --version')
        out = out.decode('utf-8')
        self.assertIn("-redhat-linux-gnu", out, out)

    def test_bind(self):
        """Tests bind: local resolver can qualify 127.0.0.1"""
        out, err, eid = system('dig +timeout=1 +short 127.0.0.1 localhost')
        out = out.decode('utf-8')
        self.assertIn("127.0.0.1", out, out)

if __name__ == '__main__':
    unittest.main()
