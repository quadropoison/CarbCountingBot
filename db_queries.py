class QueryBuilder:

    @staticmethod
    def build(operation, values):
        table = QueryBuilder.set_database_table()
        query = str()

        if operation.lower() == Operation.select:
            query = '{} * from {}'.format(operation, table)
            if values is not None:
                query = query + " where " + values

        if operation.lower() == Operation.insert:
            query = '{} into {} values ({})'.format(operation, table, values)

        if query is not "":
            print(query)
            return query + ";"
        else:
            print("db query is '>{}' no valid, try again".format(query))

    @staticmethod
    def set_database_table():
        table = "products_test"
        return table


class Operation:
    select = "select"
    insert = "insert"
    column_with_product_name = "name"

    @staticmethod
    def product_name_clause(product_name):
        search_string = "{} ilike '{}%'".format(Operation.column_with_product_name, product_name)
        return search_string

