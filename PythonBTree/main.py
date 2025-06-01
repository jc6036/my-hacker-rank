from node import BNode
from tree import BTree

if __name__ == '__main__':
    mytree = BTree()

    for i in [5, 2, -1, 15, 20, 25, 1, 3, 55, 100, 230, -40, -60, 10]:
        mytree.insert(i)
    mytree.traverse()

    srch = mytree.search(15)
    if srch == None:
        print("Not Found")
    else:
        print(f"{srch.get_data()}")
    
    print(f"Height: {mytree.height()}")

    mytree.remove_by_val(10)
    mytree.traverse()
