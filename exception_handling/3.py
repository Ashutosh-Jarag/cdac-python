def possible_index_error(lst,index):
    try:
        print(lst[index])
    except IndexError as e:
        print(e)
    else:
        print("Index is valid")


possible_index_error([1,2,3],1)
possible_index_error([1,2,3],3)