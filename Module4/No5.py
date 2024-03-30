class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
A = Node(1,Node(3,Node(5,Node(7,Node(11)))))
def sistem(kumpulan,target):
    data = kumpulan
    x = 1
    while data is not None:
        if data.data == target:
            return ["Data "+str(target)+" terdapat di Node ke"+str(x),True]
        x += 1
        return ['tidak ada',False]