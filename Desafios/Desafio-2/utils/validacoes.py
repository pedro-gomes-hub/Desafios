def entrada_inteiro(msg):
    try:
        return int(input(msg))
    except:
        return None


def entrada_float(msg):
    try:
        return float(input(msg))
    except:
        return None