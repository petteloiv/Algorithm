
def selection_sort(arr, k):
    n = len(arr)
    global cnt
    for i in range(n-1):
        if cnt == k:
            break
        else:
            min_idx = i
            for j in range(i+1,n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            cnt+=1


a,k = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
selection_sort(arr, k)

# print(cnt)
if cnt == k:
    print(' '.join(map(str, arr)))
elif cnt < k:
    print(-1)
