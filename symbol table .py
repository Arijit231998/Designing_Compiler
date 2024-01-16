class SymbolTable:
    def __init__(self):
        self.table_size = 15
        self.table = [[] for _ in range(self.table_size)]

    def hash(self, key):
        return hash(key) % self.table_size

    def insert(self, key, value):
        index = self.hash(key)
        chain = self.table[index]
        for item in chain:
            if item[0] == key:
                item[1] = value
                return
        chain.append([key, value])

    def search(self, key):
        index = self.hash(key)
        chain = self.table[index]
        for item in chain:
            if item[0] == key:
                return item[1]
        return None

    def remove(self, key):
        index = self.hash(key)
        chain = self.table[index]
        for item in chain:
            if item[0] == key:
                chain.remove(item)
                return

    def update(self, key, value):
        index = self.hash(key)
        chain = self.table[index]
        for item in chain:
            if item[0] == key:
                item[1] = value
                return

    def show(self):
        for index, chain in enumerate(self.table):
            for item in chain:
                print(f"Index: {index}, Key: {item[0]}, Value: {item[1]}")


if __name__ == "__main__":
    symbol_table = SymbolTable()

    while True:
        print("\nMenu:")
        print("1. Search for a key")
        print("2. Add a key-value pair")
        print("3. Update a key-value pair")
        print("4. Remove a key-value pair")
        print("5. Show all entries")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            key = input("Enter the key to search: ")
            value = symbol_table.search(key)
            if value is not None:
                print(f"Value for key '{key}': {value}")
            else:
                print(f"Key '{key}' not found.")
        elif choice == '2':
            key = input("Enter the key to add: ")
            value = input("Enter the value: ")
            symbol_table.insert(key, value)
            print("Key-value pair added successfully.")
        elif choice == '3':
            key = input("Enter the key to update: ")
            value = input("Enter the new value: ")
            symbol_table.update(key, value)
            print("Key-value pair updated successfully.")
        elif choice == '4':
            key = input("Enter the key to remove: ")
            symbol_table.remove(key)
            print("Key-value pair removed successfully.")
        elif choice == '5':
            print("All entries in the symbol table:")
            symbol_table.show()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")