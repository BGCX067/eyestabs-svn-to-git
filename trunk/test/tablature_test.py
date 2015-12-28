################################################################################

# User Libs
import test_utils
import test.unittest as unittest

import tablature as tab

# Std Libs
import os

################################################################################

class TestTablature(unittest.TestCase):
    def test_fixtures_work(self):
        self.assert_(os.path.exists(test_utils.fixture_path('tab/tab1.txt')))

################################################################################

if __name__ == '__main__':
    unittest.main()