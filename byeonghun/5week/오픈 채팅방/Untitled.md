```
def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    return merge(leftList, rightList)
    
print(merge_sort([4,2,3,6,1,5])
//시간복잡도는?
//더 좋은 정렬 방법이 있을까?
```

