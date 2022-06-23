#%%
import random



def quick_sort(A):
    
    less =[]
    greater = []
    equal = []

    if len(A) > 1:
        pivot = random.choice(A)
        for x in A:
            if x<pivot:
                less.append(x)
            elif x>pivot:
                greater.append(x)
            elif x==pivot:
                equal.append(x)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return A






if __name__=="__main__":
    test = [5, 1, 9, 7,7, 10, 8, 3, 0, 12]
    print(quick_sort(test))


# %%
