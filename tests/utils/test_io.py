import pytest
from cstag_cli.utils.io import _determine_format, read_sam, write_sam

from io import BytesIO
import pysam


def test_determine_format():
    sam_stream = BytesIO(b"@SQ\tSN:chr1\tLN:1000\n")
    bam_stream = BytesIO(b"BAM\x01")

    assert _determine_format(sam_stream) == "r"
    assert _determine_format(bam_stream) == "rb"


def test_read_sam_with_sam_file(tmp_path):
    sam_content = b"@SQ\tSN:chr1\tLN:1000\n"
    sam_file = tmp_path / "test.sam"
    sam_file.write_bytes(sam_content)

    # SAMファイルを読み込む
    with read_sam(str(sam_file)) as bam_file:
        header = bam_file.header
        assert "SQ" in header


def test_write_sam(tmp_path, capsys):
    sam_string = "@SQ\tSN:chr1\tLN:1000\n"
    # 一時ファイルのパスを作成
    temp_file_path = tmp_path / "temp.sam"
    # SAMデータを一時ファイルに書き込む
    with open(temp_file_path, "w") as f:
        f.write(sam_string)

    sam = pysam.AlignmentFile(str(temp_file_path), "r")
    write_sam(sam)

    captured = capsys.readouterr()
    assert sam_string in captured.out
