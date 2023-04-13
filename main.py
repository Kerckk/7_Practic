class Notebook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def delete_record(self, attribute, value):
        for record in self.records:
            if record[attribute] == value:
                self.records.remove(record)

    def search_records(self, attribute, value):
        search_results = []
        for record in self.records:
            if record[attribute] == value:
                search_results.append(record)
        return search_results

    def sort_records(self, attribute):
        self.records.sort(key=lambda x: x[attribute])

    def modify_record(self, index, attribute, value):
        self.records[index][attribute] = value

    def print_records(self):
        for record in self.records:
            print(record)

notebook = Notebook()
record1 = {"name": "John", "surname": "Smith", "phone": "+1 555 12345", "email": "john.smith@mail.com", "birthdate": "01/01/1990", "notes": ""}
record2 = {"name": "Alice", "surname": "Jones", "phone": "+1 555 45678", "email": "alice.jones@mail.com", "birthdate": "02/02/1995", "notes": ""}
notebook.add_record(record1)
notebook.add_record(record2)
notebook.print_records()
notebook.delete_record("phone", "+1 555 12345")
notebook.print_records()
search_results = notebook.search_records("surname", "Jones")
for result in search_results:
    print(result)
notebook.sort_records("birthdate")
notebook.print_records()
notebook.modify_record(0, "notes", "Likes to play basketball")
notebook.print_records()