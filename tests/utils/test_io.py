from cstag_cli.utils.io import _determine_format, read_sam

from io import BytesIO


def test_determine_format():
    sam_stream = BytesIO(b"@SQ\tSN:chr1\tLN:1000\n")
    bam_stream = BytesIO(b"BAM\x01")

    assert _determine_format(sam_stream) == "r"
    assert _determine_format(bam_stream) == "rb"


def test_read_sam_with_sam_file(tmp_path):
    sam_content = b"@SQ\tSN:chr1\tLN:1000\n"
    sam_file = tmp_path / "test.sam"
    sam_file.write_bytes(sam_content)

    with read_sam(str(sam_file)) as bam_file:
        header = bam_file.header
        assert "SQ" in header
