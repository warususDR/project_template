import pandas as pd


def print_to_console(text):
    """
        Outputs given text to console.

        Args:
            text (str): text to output into console
    """
    print(text)
    return None


def print_to_file(text, file_path):
    """
    Writes the given text to the specified file.
    Text is not appended to the end of the file, file is rewritten.

    Args:
        text (str): the text to be written to the file.
        file_path (str): the path of the file to write to, relative to the project path.

    Raises:
        FileNotFoundError: If the specified file_path does not exist.
        IOError: If an error occurs while writing to the file.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(text)
        return None
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_path}' not found.")
    except IOError as e:
        raise IOError(f"Error writing to file '{file_path}': {e}")


def print_with_pandas(text, file_path):
    """
    Writes the given dataframe to the specified csv file in text format (without indexes) using pandas.
    Text is not appended to the end of the file; the file is rewritten.

    Args:
        text (pd.DataFrame): the text to be written to the file.
        file_path (str): the path of the file to write to, relative to the project path.

    Raises:
        FileNotFoundError: If the specified file_path does not exist.
        IOError: If an error occurs while writing to the file.
    """
    try:
        text.to_csv(file_path, index=False)
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_path}' not found.")
    except IOError as e:
        raise IOError(f"Error writing to file '{file_path}': {e}")
