"""Module to test the command line interface of the project"""
import os.path
from os import system

import pytest

WORK_DIR = "generated"


@pytest.fixture
def clean():
    """Cleans the filesystem"""
    import shutil

    cwd = os.path.abspath(WORK_DIR)
    try:
        shutil.rmtree(cwd)

    except FileNotFoundError:
        pass

    os.mkdir(cwd)


def test_cli(clean):
    """Tests the cli with an empty directory"""
    exit_status = system(f"pyprogen -n test {WORK_DIR}")
    assert exit_status == 0


@pytest.mark.xfail
def test_no_name():
    """Test erroneous cli input"""
    exit_status = system(f"pyprogen {WORK_DIR}")
    assert exit_status == 0
