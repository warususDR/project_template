import unittest
import pandas as pd
import os
from app.io.input import read_from_file, read_with_pandas


class TestReadFromFile(unittest.TestCase):
    def setUp(self):
        self.file_path = 'test_input.txt'
        with open(self.file_path, 'w') as f:
            f.write('I love naukma.')

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    # Correct return result test
    def test_read_from_file_reads_correctly(self):
        content = read_from_file(self.file_path)
        expected_content = 'I love naukma.'
        self.assertEqual(content, expected_content)

    # File not found error handling test
    def test_read_from_file_handles_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_from_file('something/some.txt')

    # Io error test, reading directory as file
    def test_read_from_file_handles_io_error(self):
        with self.assertRaises(IOError):
            read_from_file('data')


class TestReadWithPandas(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({'odd': [1, 3, 5], 'Even': [2, 4, 6]})
        self.file_path = 'test_input.csv'
        self.df.to_csv(self.file_path, index=False)

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    # Correct dataframe reading test
    def test_read_with_pandas_reads_correctly(self):
        df_read = read_with_pandas(self.file_path)
        self.assertTrue(self.df.equals(df_read))

    # File not found test
    def test_read_with_pandas_handles_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_with_pandas('something/some.csv')

    # IO error test, reading a directory as file
    def test_read_with_pandas_handles_io_error(self):
        with self.assertRaises(IOError):
            read_with_pandas('data')


if __name__ == '__main__':
    unittest.main()
