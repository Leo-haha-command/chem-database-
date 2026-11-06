def extract(data):
    i = 0
    while i < len(data):
        if data.startswith("CE", i):
            return 1  # 1 = CE file
        if data.startswith("AL", i):
            return 2  # 2 = A level file
        if data.startswith("DSE", i):
            return 3  # 3 = DSE
        i += 1
    return 0  # or None, if no match