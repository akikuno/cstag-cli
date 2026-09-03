from argparse import Namespace
from unittest.mock import MagicMock

import pytest

from cstag_cli import main


def test_run_append_closes_alignment_file(monkeypatch: pytest.MonkeyPatch) -> None:
    alignment_file = MagicMock()
    managed_file = MagicMock()
    managed_file.__enter__.return_value = alignment_file
    read_sam = MagicMock(return_value=managed_file)
    append = MagicMock()
    monkeypatch.setattr(main, "read_sam", read_sam)
    monkeypatch.setattr(main, "append", append)

    main.run_append(Namespace(file="reads.sam", long=True), MagicMock())

    read_sam.assert_called_once_with("reads.sam")
    append.assert_called_once_with(alignment_file, True)
    managed_file.__exit__.assert_called_once_with(None, None, None)


def test_run_append_closes_alignment_file_after_error(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    managed_file = MagicMock()
    managed_file.__enter__.return_value = MagicMock()
    monkeypatch.setattr(main, "read_sam", MagicMock(return_value=managed_file))
    monkeypatch.setattr(
        main,
        "append",
        MagicMock(side_effect=RuntimeError("append failed")),
    )

    with pytest.raises(RuntimeError, match="append failed"):
        main.run_append(Namespace(file="reads.sam", long=False), MagicMock())

    assert managed_file.__exit__.call_count == 1
