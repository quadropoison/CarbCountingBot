from api_commands import APICommandsReceiver, APICommandsInvoker, GetProduct
from api_requestor import UrlBuilder
from db_adapter import DatabaseAdapter
from db_queries import QueryBuilder, Operation


def main():
    print(DatabaseAdapter.get_version())
    # data = DatabaseAdapter.select_query("Select * from products_test")

    query = QueryBuilder.build(Operation.insert, "Default, 'Papaya4', 10, Default")
    DatabaseAdapter.insert_query(query)

    query = QueryBuilder.build(Operation.select, Operation.product_name_clause("Pa"))
    data = DatabaseAdapter.select_query(query)

    for a in data:
        print(a)

    # url = UrlBuilder.build('https://api.nal.usda.gov', 'ndb/search', format='json', q='apple',
    #                        fg='Fruits and Fruit Juices', ds='Standard Reference', sort='n',
    #                        offset='0', max='200',
    #                        api_key='apikey')
    # print(url)
    #
    # receiver = APICommandsReceiver(url)
    # invoker = APICommandsInvoker()
    #
    # command1 = GetProduct(receiver)
    # command2 = GetProduct(receiver)
    # command3 = GetProduct(receiver)
    #
    # invoker.store_command(command1)
    # invoker.store_command(command2)
    # invoker.store_command(command3)
    #
    # api_responses = invoker.execute_commands()
    #
    # for response in api_responses:
    #     items = response
    #     for item in items['list']['item']:
    #         print("name - " + item['name'] + "| ndbno - " + item['ndbno'])


if __name__ == "__main__":
    main()
