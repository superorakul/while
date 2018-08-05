def search4vowels(phrase: str) -> set:
    """Здесь есть описание которое мне влом писать так что извините"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str='aeiou') -> set:
    """Возвращает множество букв из 'letters' найденных в указанной форме """
    return set(letters).intersection(set(phrase))
