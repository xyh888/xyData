from pathlib import Path
import json



def _get_KR_settings_dir(temp_name: str):
    """
    Get path where trader is running in.
    """
    cwd = Path.cwd()
    temp_path = cwd.joinpath(temp_name)

    # If .vntrader folder exists in current working directory,
    # then use it as trader running path.
    if temp_path.exists():
        return cwd, temp_path

    # Otherwise use home path of system.
    home_path = Path.home()
    temp_path = home_path.joinpath(temp_name)

    # Create .vntrader folder under home path if not exist.
    if not temp_path.exists():
        temp_path.mkdir()

    return home_path, temp_path

HOME_DIR, TEMP_DIR = _get_KR_settings_dir('.xyData')

def save_json_settings(filename: str, data: dict):
    """
    Save data into json file in temp path.
    """
    filepath = TEMP_DIR.joinpath(filename)
    with open(filepath, mode='w+') as f:
        json.dump(data, f, indent=4)

def load_json_settings(filename: str):
    """
    Load data from json file in temp path.
    """
    filepath = TEMP_DIR.joinpath(filename)

    if filepath.exists():
        with open(filepath, mode='r') as f:
            data = json.load(f)
        return data
    else:
        save_json_settings(filename, {})
        return {}