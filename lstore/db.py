from lstore.table import Table

class Database:
    def __init__(self):
        # We use a dictionary to hold tables by name.
        self.tables = {}

    # Not required for milestone 1.
    def open(self, path):
        pass

    def close(self):
        pass

    """
    Creates a new table.
    :param name: string         # Table name
    :param num_columns: int     # Number of columns (user columns)
    :param key_index: int       # Index of table key in columns
    """
    def create_table(self, name, num_columns, key_index):
        table = Table(name, num_columns, key_index)
        self.tables[name] = table
        return table

    """
    Deletes the specified table.
    """
    def drop_table(self, name):
        if name in self.tables:
            del self.tables[name]

    """
    Returns table with the passed name.
    """
    def get_table(self, name):
        return self.tables.get(name, None)
