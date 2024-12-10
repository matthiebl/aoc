
class Constants:
    input_file_ext: str = ".in"
    example_file_ext: str = ".ex"
    input_file: str = "{year}/{day}" + input_file_ext
    example_file: str = "{year}/{day}" + example_file_ext
    script_file: str = "{day}.py"
    input_file_re = r"\d{4}\/\d{2}.in"
