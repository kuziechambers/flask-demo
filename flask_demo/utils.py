"""
Store commonly used utilities here

"""
import json
from typing import Any

from selenium import webdriver


def json_data_dump(data_dict: Any, file_name: str):
    """

    Args:
        data_dict: Dictionary that you want saved as JSON
        file_name: Name of the JSON file
    """

    file_path = f"data/{file_name}"
    
    with open(file_path, "w") as json_outfile:
        json.dump(data_dict, json_outfile)


def json_data_read(file_path: str):
    """

    Args:
        file_path: Path of the JSON file
    """

    with open(f"data/{file_path}", "r") as json_outfile:
        json_result = json.load(json_outfile)

    return json_result


def get_chrome_driver():
    """

    Args:

    Returns:
        driver: Instance of webdriver

    """

    driver = webdriver.Chrome()
    driver.set_window_size(1000, 1000)
    driver.implicitly_wait(5)

    return driver
