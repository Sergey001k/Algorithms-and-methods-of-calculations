def floatRange(start, stop, step):
    cur = start
    result = []
    
    while cur < stop:
        result.append(cur)
        cur += step

    return result