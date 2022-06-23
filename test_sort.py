#%%
import random
import pytest
from quick_sort import quick_sort




def test_sort():
    A = [random.randint(0,99) for n in range(20)]
    default_case = A.copy()
    default_case.sort()

    A = quick_sort(A)
    for item_default,item_compare in zip(default_case,A):
        assert item_default == item_compare

# %%
