import os
import pytest
from datetime import datetime
from pyls import getDescriptionsOfFilesInDir, formatResults, displayResults

# Mock directory structure for testing
@pytest.fixture
def mock_directory(tmpdir):
    # Create files
    file1 = tmpdir.join("file1.txt")
    file1.write("content")

    file2 = tmpdir.join("script.sh")
    file2.write("echo 'Hello World'")
    os.chmod(str(file2), 0o755)  # Make it executable

    # Create directories
    dir1 = tmpdir.mkdir("dir1")
    dir2 = tmpdir.mkdir("dir2")

    return tmpdir

def test_getDescriptionsOfFilesInDir(mock_directory):
    descriptions = getDescriptionsOfFilesInDir(str(mock_directory))

    assert len(descriptions) == 4
    assert any(d["filename"] == "file1.txt" for d in descriptions)
    assert any(d["filename"] == "script.sh" and d["filetype"] == "x" for d in descriptions)
    assert any(d["filename"] == "dir1" and d["filetype"] == "d" for d in descriptions)
    assert any(d["filename"] == "dir2" and d["filetype"] == "d" for d in descriptions)

def test_formatResults_long_format(mock_directory):
    descriptions = getDescriptionsOfFilesInDir(str(mock_directory))
    formatted_results = formatResults(descriptions, long_format=True, filetype=False)

    assert len(formatted_results) == 4
    for result in formatted_results:
        assert len(result.split("\t")) == 3  # Expecting 3 columns: modtime, filesize, filename

def test_formatResults_filetype(mock_directory):
    descriptions = getDescriptionsOfFilesInDir(str(mock_directory))
    formatted_results = formatResults(descriptions, long_format=False, filetype=True)

    assert len(formatted_results) == 4
    assert any("script.sh*" in result for result in formatted_results)  # Executable file
    assert any("dir1/" in result for result in formatted_results)  # Directory

def test_formatResults_long_format_and_filetype(mock_directory):
    descriptions = getDescriptionsOfFilesInDir(str(mock_directory))
    formatted_results = formatResults(descriptions, long_format=True, filetype=True)

    assert len(formatted_results) == 4
    for result in formatted_results:
        assert len(result.split("\t")) == 3  # Expecting 3 columns
        assert any(result.endswith("*") or result.endswith("/") or not result[-1].isalnum() for result in formatted_results)

def test_displayResults(capsys):
    sample_lines = ["Line 1", "Line 2", "Line 3"]
    displayResults(sample_lines)

    captured = capsys.readouterr()
    assert captured.out == "Line 1\nLine 2\nLine 3\n"
