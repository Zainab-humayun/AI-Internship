# def intersection(set1,set2):
#     inter=set()
#     for x in set1:
#         if x in set2:    
#             inter.add(x)
#     return inter

# def union(set1,set2):
#     union=set()
#     for x in set1:
#         union.add(x)
#     for y in set2:
#         union.add(y)
#     return union
class Sets():
    def __init__(self, set1,set2):
        self.set1=set1
        self.set2=set2

    def intersection(self):
        inter=set()
        for x in self.set1:
            if x in self.set2:    
                inter.add(x)
        return inter

    def union(self):
        union=set()
        for x in self.set1:
            union.add(x)
        for y in self.set2:
            union.add(y)
        return union

def main():
    
    list_set1=(input("Enter elements of first set: ").split()) ##use split to convert to list
    set1=set(list_set1) ##convert to set (removes repeated items)
    list_set2=(input("Enter elements of second set: ")).split()
    set2= set(list_set2)

    var_operations= Sets(set1,set2)
    print("Intersection of the 2 sets is: ", var_operations.intersection())
    print("Union of the 2 sets is: ", var_operations.union())
    
##below code for when classes were not used
    # intersec= intersection(set1,set2)
    # print("Intersection of the 2 sets is: ", intersec)
    # uni=union(set1,set2)
    # print("Union of the 2 sets is: ", uni)


if __name__ == "__main__":
    main()

