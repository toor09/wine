def format_year(value: int) -> str:
    """Return the form of the word year depending on its value"""
    if value % 10 == 1 and value != 11 and value % 100 != 11:
        return "год"
    elif 1 < value % 10 <= 4 and value != 12 and value != 13 and value != 14:
        return "года"
    else:
        return "лет"


if __name__ == "__main__":
    assert format_year(value=1) == "год"
    assert format_year(value=21) == "год"
    assert format_year(value=71) == "год"
    assert format_year(value=2) == "года"
    assert format_year(value=23) == "года"
    assert format_year(value=5) == "лет"
    assert format_year(value=7) == "лет"
    assert format_year(value=150) == "лет"
