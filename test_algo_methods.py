from python_test import open_file, parse_command, copy_command, random_command, functional_command
import pytest
from unittest import mock


def test_open_file():
    assert open_file()


def test_exception_file_not_found():
    with pytest.raises(FileNotFoundError):
        open_file()
        print("file not found")


def test_parse_commads():
    assert parse_command()


def test_exception_on_parse_command():
    with pytest.raises(ValueError):
        parse_command()
        print("Data not found")


def test_copy_commads():
    assert copy_command()


def test_exception_on_copy_commands():
    with pytest.raises(ValueError):
        copy_command()
        print("Data not found")


def test_functional_commads():
    assert functional_command()


def test_exception_on_functional_commands():
    with pytest.raises(ValueError):
        functional_command()
        print("Data not found")


def test_random_commads():
    assert random_command()


def test_exception_on_random_commands():
    with pytest.raises(ValueError):
        random_command()
        print("Data not found")


def test_mock_random_commands():
    fixed_value = mock.Mock(name="mock object", return_value=2)
    if random_command() == fixed_value():
        pass

