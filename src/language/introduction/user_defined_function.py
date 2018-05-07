def repeat(s, exclaim):
    """
    return string 's' repeated 3 times
    if exclaim is true ,and exclamation marks

    :param s:
    :param exclaim:
    :return:
    """
    # result = s + s + s
    result = s * 3
    if exclaim:
        result += "! ! !"
    return result


print(repeat("yh", 1))
