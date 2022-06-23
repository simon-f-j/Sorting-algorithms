#%%

def insertion_sort(collection: list) -> list:

    for insert_index, insert_value in enumerate(collection[1:]):
        temp_index = insert_index
        while insert_index >= 0 and insert_value < collection[insert_index]:
            collection[insert_index + 1] = collection[insert_index]
            insert_index -= 1
        if insert_index != temp_index:
            collection[insert_index + 1] = insert_value
    return collection


insertion_sort([5,43,6,3,5,7,8,1,3,1,2,2])
# %%
