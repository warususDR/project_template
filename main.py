from app.io.input import read_from_file, read_from_console, read_with_pandas
from app.io.output import print_to_file, print_to_console, print_with_pandas


def main():
    try:
        print_to_console(read_from_console())  # from console to console
        print_to_console(read_from_file("data//input_pandas.csv"))  # from file to console
        print_to_console(read_with_pandas("data//input_pandas.csv").to_string())  # pandas csv to console
        print_to_file(read_from_file("data//input_pandas.csv"), "data//output_file.txt")  # to file
        print_with_pandas(read_with_pandas("data//input_pandas.csv"), "data//output_pandas.csv")  # pandas to file
    except FileNotFoundError as e:
        print(e)
    except IOError as e:
        print(e)


if __name__ == "__main__":
    main()
