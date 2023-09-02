import cstag


def append(sam, is_long: bool = False):
    # output header
    print(sam.header, end="")
    for read in sam:
        if read.is_unmapped:
            print(read.to_string())
            continue
        if not read.has_tag("MD"):
            raise ValueError("MD tag is not found in the input.")
        # append cstag and output alignments
        cs = cstag.call(cigar=read.cigarstring, md=read.get_tag("MD"), seq=read.seq, long=is_long)
        read.set_tag("cs", cs.replace("cs:Z:", ""), replace=True)
        print(read.to_string())
