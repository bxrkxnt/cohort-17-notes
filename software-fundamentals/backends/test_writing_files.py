from writing_files import write_file
from unittest.mock import patch

@patch("writing_files.open")
def test_write_file(mock_open):
    assert write_file("Not intended") == "Not intended"
    assert mock_open.called