# Сериализатор БД ответа -> Словаря

def serialize(db_result):
    """ Сериализатор БД -> Словарь """
    result = []
    for row in db_result:
        result.append({key: value for key, value in dict(row).items()})
    return result
