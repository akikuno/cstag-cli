import re
from unittest.mock import MagicMock

import pytest

from cstag_cli.append import appender


def _alignment_with_one_read() -> tuple[MagicMock, MagicMock]:
    read = MagicMock()
    read.is_unmapped = False
    read.query_sequence = "AC"
    read.cigarstring = "2M"
    read.query_name = "read-1"
    read.has_tag.return_value = True
    read.get_tag.return_value = "2"

    alignment = MagicMock()
    alignment.header = ""
    alignment.__iter__.return_value = iter([read])
    return alignment, read


def test_append_uses_query_sequence(monkeypatch: pytest.MonkeyPatch) -> None:
    alignment, read = _alignment_with_one_read()
    call = MagicMock(return_value=":2")
    monkeypatch.setattr(appender.cstag, "call", call)

    appender.append(alignment)

    call.assert_called_once_with(cigar="2M", md="2", seq="AC", long=False)
    read.set_tag.assert_called_once_with("cs", ":2", replace=True)


def test_append_preserves_error_and_adds_cause(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    alignment, _ = _alignment_with_one_read()
    original_error = ValueError("invalid alignment")
    monkeypatch.setattr(
        appender.cstag,
        "call",
        MagicMock(side_effect=original_error),
    )

    message = "invalid alignment. \nThis error occurred at read-1."
    with pytest.raises(ValueError, match=re.escape(message)) as error_info:
        appender.append(alignment)

    assert error_info.value.__cause__ is original_error
