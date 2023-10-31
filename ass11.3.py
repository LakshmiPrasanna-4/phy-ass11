# Write a program to print the following series
'''
1 3 5 7
2 4 6 8
3 5 7 9
4 6 8 10
'''

for i in range(1,5):
    k=i
    for j in range(2,6):
        print(k,end=' ')
        k=k+2
    print()
