def camelcase(s: str):
    return 1 + sum(1 for letter in s if (letter.isupper()))
