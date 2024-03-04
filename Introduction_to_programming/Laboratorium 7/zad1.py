def delete_duplicates(list2):
    list_sort = []
    for i in list2:
        if i not in list_sort:
            list_sort.append(i)
    print(list_sort)


list1 = ["2", "2", "4", ",", "3", "4", ","]
delete_duplicates(list1)
