import json

def prepares_data_operations(path, number):
    '''Возвращает отсортированный список подготовленных операций по заданному количеству извлекая данные из json-файла'''
    #Загружает словарь с данными по всем опрациям из json-файла
    with open(path, encoding='utf-8') as file_operations:
        all_operations = json.load(file_operations)

    #Формирует список только с необходимыми данными
    operations = [operation for operation in all_operations if 'state' in operation and operation['state'] == 'EXECUTED']

    #Сортирует список по дате и возвращает нужное количество
    operations_sorted  = sorted(operations, key=lambda oper: oper["date"], reverse=True)[:number]

    return operations_sorted

def date_format(date):
    """Возвращает дату в необходимом формате"""
    date_format = date[:10].split("-")
    date_format.reverse()
    return ".".join(date_format)

def disguise_accounts(operation_to, operation_from=None):
    """Возвращает операцию в замаскированных счетах"""
    to_mask_beg = operation_to.split(' ')[0]
    to_mask_end = f"**{operation_to.split(' ')[-1][-4:]}"

    if operation_from:
        from_mask_beg = ' '.join(operation_from.split(" ")[:-1])
        if ' '.join(operation_from.split(" ")[:-1]) == "Счет":
            from_mask_end = f"**{operation_from.split(' ')[-1][-4:]}"
        else:
            fro_mask = [elem if ind not in range(6, 12) else "*" for ind, elem in
                        enumerate(operation_from.split(" ")[-1])]
            from_mask_end = ' '.join([''.join(fro_mask[i:i + 4]) for i in range(0, len(fro_mask), 4)])
    else:
        from_mask_beg = ""
        from_mask_end = ""

    return(f"{from_mask_beg} {from_mask_end} -> {to_mask_beg} {to_mask_end}")
