import pytest
import project.py


def test_get_file_name():
    assert get_file_name("h.png") == "input/hi.png"
    assert get_file_name("ciao") == "input/ciao"
    assert get_file_name("input") == "input/input"


def test_get_output_folder():
    assert get_output_folder() == "outputs/output."
