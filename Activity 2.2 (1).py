database = []

def add_record(name, age, city):
    record = (name, age, city)
    database.append(record)  

def display_records():
    print("Records in the database:")
    for record in database:
        print(f"Name: {record[0]}, Age: {record[1]}, City: {record[2]}")

def main():
    
    add_record("Alice", 30, "New York")
    add_record("Bob", 25, "Los Angeles")
    add_record("Charlie", 35, "Chicago")
    
 
    display_records()

if __name__ == "__main__":
    main()


