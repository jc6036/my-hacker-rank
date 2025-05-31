from node import BNode
from tree import BTree

if __name__ == '__main__':
    mytree = BTree()

    mytree.insert(5)
    mytree.insert(10)
    mytree.insert(2)
    mytree.insert(3)
    mytree.insert(15)
    mytree.traverse()

    srch = mytree.search(15)
    if srch == None:
        print("Not Found")
    else:
        print(f"{srch.get_data()}")
    
    print(f"Height: {mytree.height()}")

    mytree.remove_by_val(10)
    mytree.traverse()
