technic = {"phones": ["IPhone", "Xiaomi", "Samsung", "Honor"], "televisions": ["Samsung", "Xiaomi", "Panasonic"],
           "headphones": ["AirPods", "JBL", "Beats"]}

search = input("Enter what do you want to search: ")

if search == "phones" or search == "televisions" or search == "headphones":
    print(technic[search])
