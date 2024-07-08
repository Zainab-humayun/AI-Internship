def intersection(set1,set2):
    inter=set()
    for x in set1:
        if x in set2:    
            inter.add(x)
    return inter

def union(set1,set2):
    union=set()
    for x in set1:
        union.add(x)
    for y in set2:
        union.add(y)
    return union

def main():
    set1={'2','3','4','55','43'}
    set2={'3','1','65','72','55'}
    intersec= intersection(set1,set2)
    print("Intersection of the 2 sets is: ", intersec)
    uni=union(set1,set2)
    print("Union of the 2 sets is: ", uni)

if __name__ == "__main__":
    main()

