from config import PATH_OPERATIONS, NUMBER_OF_OPERATOINS
from utilits import prepares_data_operations, date_format, disguise_accounts

def main():
    """Выводит итоговый результат на экран"""
    operations = prepares_data_operations(PATH_OPERATIONS,NUMBER_OF_OPERATOINS)

    for operation in operations:
        date = date_format(operation['date'])
        from_to_accounts = disguise_accounts(operation['to'], operation.get('from'))

        print(f'''{date} {operation['description']}
{from_to_accounts}
{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}
''')

if __name__ == "__main__":
    main()