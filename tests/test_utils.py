import json

import pytest

from scr.utils import read_operations_json

# ========================================
# ====== Тесты read_operations_json ======
# ========================================


@pytest.mark.parametrize(
    "file_content, expected_result, description",
    [
        (None, [], "FileNotFoundError"),  # Файла нет -> []
        ("", [], "Empty file"),  # Файл пуст -> []
        (json.dumps({"key": "value"}), [], "Not a list JSON"),  # json не список -> []
        (json.dumps([{"key": 1}]), [{"key": 1}], "Valid JSON list"),  # Исправный json -> [{'key': 1}]
    ],
)
def test_read_json_file(tmp_path, file_content, expected_result, description):
    if file_content is not None:
        file_path = tmp_path / "test.json"
        file_path.write_text(file_content, encoding="utf-8")
        file_to_read = str(file_path)
    else:
        file_to_read = "nonexistent.json"

    result = read_operations_json(file_to_read)
    assert result == expected_result, f"Failed case: {description}"
