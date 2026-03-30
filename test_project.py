import pytest
from project import import_file, get_choice, new_task, remove_task, modify_tasks, view_tasks, save_tasks, tasks
from unittest.mock import patch, mock_open

def main():
    test_get_choice_invalid_then_valid()
    test_get_choice_valid_input()
    test_import_file_no_file()
    test_new_task()
    test_save_tasks()
    test_view_tasks()

def test_import_file_no_file():
    with patch('builtins.open', side_effect=FileNotFoundError):
        import_file()
        assert tasks == []

def test_get_choice_valid_input():
    with patch('builtins.input', side_effect=['1']):
        assert get_choice() == 1

def test_get_choice_invalid_then_valid():
    with patch('builtins.input', side_effect=['a', '1']):
        with patch('os.system') as mocked_os:
            assert get_choice() == 1
            mocked_os.assert_called_with('clear')

def test_new_task():
    with patch('builtins.input', side_effect=['New Task']):
        with patch('os.system'):
            new_task()
            assert tasks[0] == 'New Task'

def test_view_tasks(capsys):
    tasks.extend(["Task 1", "Task 2"])
    view_tasks()
    captured = capsys.readouterr()
    assert "Task 1" in captured.out
    assert "Task 2" in captured.out

def test_save_tasks():
    mock_data = ["Task 1", "Task 2"]
    with patch('builtins.open', mock_open()) as mocked_file:
        tasks.extend(mock_data)
        save_tasks()
        mocked_file().write.assert_any_call('Task 1\n')
        mocked_file().write.assert_any_call('Task 2\n')

if __name__ == "__main__":
    main()
