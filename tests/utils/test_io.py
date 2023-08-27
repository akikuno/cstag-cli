from cstag_cli.utils.io import read_sam_lines_as_generator, read_sam_lines_as_list


def test_read_sam_lines_as_generator(tmp_path):
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("line1\nline2\nline3\n")
    lines = list(read_sam_lines_as_generator(test_file))
    assert lines == ["line1", "line2", "line3"]


def test_read_sam_lines_as_list(tmp_path):
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("line1\nline2\nline3\n")
    lines = read_sam_lines_as_list(test_file)
    assert lines == ["line1", "line2", "line3"]
