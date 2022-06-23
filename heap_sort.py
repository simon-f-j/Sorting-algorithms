#%%

def bubble_down(A,i,n):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and A[largest]<A[left]:
        largest,left = left,largest
    
    if right < n and A[largest] < A[right]:
        largest, right = right, largest

    if largest != i:
        A[i], A[largest] = A[largest],A[i]
        bubble_down(A,largest,n)


def heap_sort(A):
    n = len(A)
    for i in range(n //2 -1, -1,-1):
        bubble_down(A,i,n)
    for i in range(n-1,0,-1):
        A[0],A[i] = A[i],A[0]
        bubble_down(A,0,i)
    return A
# %%
