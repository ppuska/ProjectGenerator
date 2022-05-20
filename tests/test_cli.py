"""Module to test the command line interface of the project"""
import os.path
from os import system

import pytest

WORK_DIR = "generated"
PACKAGE = "test"


@pytest.fixture
def clean():
    """Cleans the filesystem"""
    import shutil

    cwd = os.path.abspath(WORK_DIR)
    try:
        shutil.rmtree(cwd)

    except FileNotFoundError:
        pass

    except PermissionError:
        pytest.skip("Permission error, maybe the directory is open somewhere", allow_module_level=True)

    os.mkdir(cwd)


def test_cli(clean):
    """Tests the cli with an empty directory"""
    exit_status = system(f"pyprogen -n {PACKAGE} --git {WORK_DIR} > nul")
    assert exit_status == 0
    assert os.system(f"cd {WORK_DIR}/src/{PACKAGE}") == 0  # check if the package is a valid directory
    assert os.system(f"cd {WORK_DIR}/src/{PACKAGE} && git log 2> nul") == 128


@pytest.mark.xfail
def test_no_name():
    """Test erroneous cli input"""
    exit_status = system(f"pyprogen {WORK_DIR} 2> nul")
    assert exit_status == 0
