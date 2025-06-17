import json

import pytest

from scr.utils import (find_unmapped_descriptions, generate_mapping_from_descriptions, get_unique_descriptions,
                       read_operations_json)

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


# ============================================
# ====== Тесты  get_unique_descriptions ======
# ============================================


def test_get_unique_descriptions():
    data = [
        {"description": "A"},
        {"description": "B"},
        {"description": "A"},
        {"description": " "},
        {"description": None},
        {},
    ]
    result = get_unique_descriptions(data)
    assert result == {"A", "B", ""}


# ======================================================
# ====== Тесты generate_mapping_from_descriptions ======
# ======================================================


def test_generate_mapping_from_descriptions():
    data = [{"description": "Test1"}, {"description": "Test2"}]
    result = generate_mapping_from_descriptions(data)
    assert result == {"Test1": "Test1", "Test2": "Test2"}


# ===============================================
# ====== Тесты  find_unmapped_descriptions ======
# ===============================================


def test_find_unmapped_descriptions():
    data = [
        {"description": "Оплата налогов"},
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
    ]
    mapping = {"перевод организации": "Организации", "открытие вклада": "Вклады"}
    result = find_unmapped_descriptions(data, mapping)
    assert "Оплата налогов" in result
    assert "Перевод организации" not in result
