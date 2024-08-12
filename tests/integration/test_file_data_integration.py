import unittest
from utils.file_utils import write_file, read_file
from utils.data_utils import parse_csv, convert_to_json

class TestFileDataIntegration(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_data.csv"
        self.csv_content = "name,age\nAlice,30\nBob,25"
        write_file(self.test_file, self.csv_content)

    def tearDown(self):
        import os
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_read_and_parse_csv(self):
        file_content = read_file(self.test_file)
        parsed_data = parse_csv(file_content)
        self.assertEqual(len(parsed_data), 2)
        self.assertEqual(parsed_data[0]["name"], "Alice")

    def test_parse_and_convert_to_json(self):
        file_content = read_file(self.test_file)
        parsed_data = parse_csv(file_content)
        json_str = convert_to_json(parsed_data)
        self.assertTrue('"name": "Alice"' in json_str)

if __name__ == '__main__':
    unittest.main()
