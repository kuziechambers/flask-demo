from typing import Any, Dict

from flask_demo.main import main


def handler():
    """

    Project handler

    Args:
        event: event
    Raises:
        Exception: re-raises Exception when anything fails inside the main. This will
        make sure any unhandled exceptions don't go unlogged
    Returns:
        "Completed" - Project completed successfully

    """
    try:
        main()
    except Exception as err:
        print(err)
        raise
    else:
        return "Completed"
