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
