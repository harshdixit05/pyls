def getLongFormatResults(results):
    """
    Takes a list of file descriptions and returns a list of formatted strings
    with detailed information including last modified date, file size, and filename.

    Inputs -
    results = List of dictionaries, like returned by getDescriptionsOfFilesInDir()

    Outputs:
    List of strings in the format: "YYYY-MM-DD HH:MM:SS <filesize> <filename>"
    """
    assert isinstance(results, list), "results should be a list"

    list_result = []
    for i in results:
        filesize = str(i["filesize"])
        modtime = str(i["modtime"])
        filename = i["filename"]
        list_result.append(modtime + "\t" + filesize + "\t" + filename)
    return list_result
def formatResultsWithFileType(results):
    """
    Formats the list of file descriptions to include file type indicators
    (e.g., '/' for directories and '*' for executable files).

    Inputs -
    results = List of dictionaries, like returned by getDescriptionsOfFilesInDir()

    Outputs:
    List of strings with file type indicators.
    """
    assert isinstance(results, list), "results should be a list"

    list_result = []
    for i in results:
        if i["filetype"] == 'd':
            filename = i["filename"] + "/"
        elif i["filetype"] == 'x':
            filename = i["filename"] + "*"
        else:
            filename = i["filename"]
        list_result.append(filename)
    return list_result
def getLongFormatResults(results):
    """
    Takes a list of file descriptions and returns a list of formatted strings
    with detailed information including last modified date, file size, and filename.

    Inputs -
    results = List of dictionaries, like returned by getDescriptionsOfFilesInDir()

    Outputs:
    List of strings in the format: "YYYY-MM-DD HH:MM:SS <filesize> <filename>"
    """
    assert isinstance(results, list), "results should be a list"

    list_result = []
    for i in results:
        filesize = str(i["filesize"])
        modtime = str(i["modtime"])
        filename = i["filename"]
        list_result.append(modtime + "\t" + filesize + "\t" + filename)
    return list_result
import argparse

parser = argparse.ArgumentParser(
    prog="pyls",
    description="Lists files in given or current directory",
    epilog="Poor man's ls",
)

parser.add_argument(
    "dirname",
    help="Name of directory to list the contents of",
    action="store",
    nargs="?",
    default=".",
)

parser.add_argument(
    "-F",
    "--filetype",
    help="""Adds an extra character to the end of the printed
                            filename that indicates its type.""",
    action="store_true",
)

parser.add_argument(
    "-l",
    "--long-format",
    help="Presents more details about files in columnar format",
    action="store_true",
)

args = parser.parse_args()

def main(arguments):
    """
    Processes the whole program and assigns it to functions
    :param arguments:
    """
    lines = getDescriptionsOfFilesInDir(arguments.dirname)
    result_list = formatResults(lines, arguments.long_format, arguments.filetype)
    displayResults(result_list)

def displayResults(lines):
    """
    Takes a list of lines and prints them all to the standard output.

    Input:
    lines = List of strings

    Output:
    On standard output
    """
    assert isinstance(lines, list), "lines should be a list"

    for line in lines:
        print(line)

if __name__ == '__main__':
    main(args)
