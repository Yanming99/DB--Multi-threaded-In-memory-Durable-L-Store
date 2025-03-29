import pickle

class Page:

    def __init__(self):
        self.num_records = 0
        self.data = {}

    def has_capacity(self):
        # Returns size of dictionary as bytes
        return len(pickle.dumps(self.data))

    def write(self, value):
        self.num_records += 1
        
        # Size of current bytes in page
        size_data = self.has_capacity()
        
        # Size of value being inserted
        size_value = len(pickle.dumps(value))

        # 4096 Bytes is ideal
        if(size_data + size_value) >= 4096:
            # Make another page handled by table.py
            return "Error Code???"
        else:
            self.data[len(self.data)+1] = value
        pass

