arr=list(map(int,input().split()))

print( max([arr.count(i) for i in list(set(arr))]) )

