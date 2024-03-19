import pandas as pd


def read_from_console():
    """
    Reads user input from console using input() with a prompt and returns it.

    Returns:
        str. Input received from console.
    """
    user_input = input('Please enter your input: ')
    return user_input


def read_from_file(file_path):
    """
    Reads from file by file_path and returns the file content.
    If the path doesn't exist or other errors occur throws according exceptions.

    Args:
        file_path (str): the path of the file to read from relative to the project path.

    Returns:
        str. Content of the file at the requested path.

    Raises:
        FileNotFoundError: If the specified file_path does not exist.
        IOError: If an error occurs while reading the file.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_path}' not found.")
    except IOError as e:
        raise IOError(f"Error reading file '{file_path}': {e}")


def read_with_pandas(file_path):
    """
    Reads from a csv file by file_path using pandas and returns the file content as dataframe.
    If the path doesn't exist or other errors occur throws according exceptions.

    Args:
        file_path (str): the path of the file to read from relative to the project path.

    Returns:
        pd.DataFrame. DataFrame of the content of the file at the requested path.

    Raises:
        FileNotFoundError: If the specified file_path does not exist.
        IOError: If an error occurs while reading the file.
    """
    try:
        content = pd.read_csv(file_path)
        return content
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_path}' not found.")
    except IOError as e:
        raise IOError(f"Error reading file '{file_path}': {e}")
