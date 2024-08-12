import unittest
from utils.file_utils import write_file, read_file
from utils.data_utils import parse_csv, filter_data, convert_to_json

class TestEndToEnd(unittest.TestCase):

    def setUp(self):
        self.test_file = "full_test_data.csv"
        self.csv_content = "name,age\nAlice,30\nBob,25\nCharlie,35"
        write_file(self.test_file, self.csv_content)

    def tearDown(self):
        import os
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_full_workflow(self):
        # Step 1: Read file
        content = read_file(self.test_file)
        self.assertIn("Alice", content)

        # Step 2: Parse CSV
        parsed_data = parse_csv(content)
        self.assertEqual(len(parsed_data), 3)

        # Step 3: Filter data
        filtered_data = filter_data(parsed_data, "age", "30")
        self.assertEqual(len(filtered_data), 1)
        self.assertEqual(filtered_data[0]["name"], "Alice")

        # Step 4: Convert to JSON
        json_str = convert_to_json(filtered_data)
        self.assertTrue('"age": "30"' in json_str)

if __name__ == '__main__':
    unittest.main()
