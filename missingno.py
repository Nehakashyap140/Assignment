arr=[1,3,4,5,6,7,8,9,10]
missing_element = []
for ele in range(arr[0], arr[-1]+1):
    if ele not in arr:
        missing_element.append(ele)
        print(missing_element)

