#%%
def bubble_sort(A):
    n = len(A)
    for i in range(n-2):
        for j in range(0,n-i-2):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
    return A

# %%
