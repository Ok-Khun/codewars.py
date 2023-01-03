def minimum(arr):
    m = arr[0]
    for i in arr:
        if i < m:
            m = i
    return m

def maximum(arr):
    m = arr[0]
    for i in arr:
        if i > m:
            m = i
    return m

