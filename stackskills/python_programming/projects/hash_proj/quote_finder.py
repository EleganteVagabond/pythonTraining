from data_structures.hashmap import HashMap

def parse_line(line) :
    return line.split(":")

def load_map_data(fname) :
    ret = HashMap()
    with open(fname,"r+") as f_reader :
        for line in f_reader :
            key, value = parse_line(line.strip())
            ret.put(key,value)
    return ret

def get_quote(email, hashmap) :
    v = hashmap.get(email)
    if v == None:
        return f"Email {email} not found in quotes database"
    else :
        return f"{email} says \"{v.value}\""


map = load_map_data("projects/hash_proj/data.txt")
print("Map data loaded! Beginning choice loop...")
print("Quote Finder v.01, (C) 2020")
while True :
    print("Please enter the email address you would like to find a quote for or 'exit' to end")
    choice = input(">")
    if choice == "exit" :
        break
    else :
        print(get_quote(choice,map))
