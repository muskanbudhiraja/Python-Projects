
from typing import Any
from unittest.mock import patch
from src.main import start


@patch("uvicorn.run")
def test_start(mock_run: Any) -> None:
    """test start"""
    start()

    # pylint: disable=duplicate-code
    mock_run.assert_called_once_with(
        "src.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
