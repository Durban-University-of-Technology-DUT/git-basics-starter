import unittest
from utils.data_utils import parse_csv, filter_data, convert_to_json

class TestDataUtils(unittest.TestCase):

    def setUp(self):
        self.csv_data = "name,age\nAlice,30\nBob,25"
        self.parsed_data = [
            {"name": "Alice", "age": "30"},
            {"name": "Bob", "age": "25"}
        ]

    def test_parse_csv(self):
        result = parse_csv(self.csv_data)
        self.assertEqual(result, self.parsed_data)

    def test_filter_data(self):
        filtered = filter_data(self.parsed_data, "age", "30")
        self.assertEqual(filtered, [{"name": "Alice", "age": "30"}])

    def test_convert_to_json(self):
        json_str = convert_to_json(self.parsed_data)
        expected_json = '[{"name": "Alice", "age": "30"}, {"name": "Bob", "age": "25"}]'
        self.assertEqual(json_str, expected_json)

if __name__ == '__main__':
    unittest.main()
