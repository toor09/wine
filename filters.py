def format_year(age: int) -> str:
    """Return the form of the word year depending on its age"""

    if age % 10 == 1 and age != 11:
        return "год"
    if age % 10 in range(2, 5) and age not in range(12, 15):
        return "года"
    return "лет"
