def solution(query_type, query_data):
    counter = 0
    data_bank = {}
    for type in query_type:
        match type:
            case "insert":
                insert(data_bank, query_data[counter])
            case "addToValue":
                addToValue(data_bank, query_data[counter])
            case "addToKey":
                data_bank = addToKey(data_bank, query_data[counter])
            case "get":
                get(data_bank, query_data[counter])
        counter += 1


def insert(data_bank, data_list):
    data_bank.update({data_list[0]: data_list[1]})
    print(data_bank)


def addToValue(data_bank, data_list):
    for key, value in data_bank.items():
        new_value = value + data_list[0]
        temp = {key: new_value}
        data_bank.update(temp)
    print(data_bank)


def addToKey(data_bank, data_list):
    key_list = data_bank.keys()
    new_list = []
    for item in key_list:
        item = item + data_list[0]
        new_list.append(item)
    data_bank = dict(zip(new_list, data_bank.values()))
    print(data_bank)
    return data_bank


def get(data_bank, data_list):
    print(data_bank.get(data_list[0]))
    return data_bank.get(data_list[0])

solution(["insert", "insert", "addToValue", "addToKey", "get"], [[1, 2], [2, 3], [2], [1], [3]])