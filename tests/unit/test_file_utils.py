import unittest
from utils.file_utils import read_file, write_file, file_exists
import os

class TestFileUtils(unittest.TestCase):

    def setUp(self):
        self.test_file = "test.txt"
        self.content = "Hello, World!"
        with open(self.test_file, 'w') as f:
            f.write(self.content)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_read_file(self):
        result = read_file(self.test_file)
        self.assertEqual(result, self.content)

    def test_write_file(self):
        new_content = "Goodbye, World!"
        write_file(self.test_file, new_content)
        with open(self.test_file, 'r') as f:
            self.assertEqual(f.read(), new_content)

    def test_file_exists(self):
        self.assertTrue(file_exists(self.test_file))
        self.assertFalse(file_exists("non_existent_file.txt"))

if __name__ == '__main__':
    unittest.main()
