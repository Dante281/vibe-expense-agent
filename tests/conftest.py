import os
import pytest
import tempfile
import shutil


@pytest.fixture(autouse=True)
def setup_test_db(monkeypatch):
    """
    Automatically creates a temporary database file for tests to avoid
    modifying the production expenses.json file.
    """
    temp_dir = tempfile.mkdtemp()
    temp_db_path = os.path.join(temp_dir, "test_expenses.json")

    # Initialize with an empty JSON array
    with open(temp_db_path, "w") as f:
        f.write("[]")

    monkeypatch.setenv("EXPENSE_DB_PATH", temp_db_path)

    yield temp_db_path

    # Clean up files
    try:
        shutil.rmtree(temp_dir)
    except OSError:
        pass
