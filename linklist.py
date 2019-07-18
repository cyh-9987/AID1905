"""
实现单链表的构建和功能操作
重点代码
"""
import time
class Node:
    def __init__(self,val,next = None):
        self.val=val
        self.next=next

class Linklist:
    def __init__(self):
        self.head=Node(None)

    def init_list(self, list):

        p=self.head
        for i in list:
            p.next=Node(i)
            p=p.next
    def show(self):

        p=self.head.next
        while p is not None:
            print(p.val)
            p=p.next
    def is_empty(self):
        if self.head.next is None:
            return True
        else:
            return False
    def clear(self):
        self.head.next = None

    def append(self,val):
        node=Node(val)
        p=self.head
        while p.next is not None:
            p=p.next
        p.next=node

    def head_insert(self,val):
        node=Node(val)
        node.next=self.head.next
        self.head.next=node

    def insert(self,index,val):
        node=Node(val)
        p=self.head
        for i in range(index):
            if p.next is None:
                break
            p=p.next
        node.next=p.next
        p.next=node

    def remove(self,val):
        p=self.head
        while p.next and p.next.val!=val:
            p=p.next
        if p.next is None:
            raise ValueError("x not in linklist")
        else:
            p.next=p.next.next

    def get_index(self,val):
        p = self.head
        count=0
        while p.next and p.next.val != val:
            count+=1
            p = p.next
        if p.next is None:
            raise ValueError("x not in linklist")
        return count

    def get_val(self,index):
        p=self.head.next
        for i in range(index):
            if p.next is None:
                raise IndexError("index out of range")
            p=p.next
        return p.val

    def combination(self,linklist02):
        p=self.head
        while p.next is not None:
            p=p.next
        p.next=linklist02.head.next

    def sort(self):
        l=Linklist()
        l.init_list('')
        p=self.head
        while p.next is not None:
            min=p.next.val
            a=p.next
            while a is not None:
                if min >a.val:
                    min=a.val
                a = a.next
            l.append(min)
            self.remove(min)
        return l

    # def sort2(self):
    #     index=0
    #     p=self.head
    #     while p.next is not None:
    #         min=p.next.val
    #         a=p
    #         c = a
    #         while a.next is not None:
    #             if min >a.next.val:
    #                 c=a
    #                 min=a.next.val
    #             a = a.next
    #         nob=c
    #         c.next=c.next.next
    #         nob.next=p.next
    #         p.next=nob
    #         index+=1



# l1=Linklist()
# l2=Linklist()
# l1.init_list([36,35,5455])
# # l2.init_list([23,4576,688,2,4,4,67])
# # l1.combination(l2)
# l1.sort2()
# l1.show()

if __name__ == "__main__":

    l1=Linklist()
    l2=Linklist()
    l1.init_list([34,35,5455,6,767,4])
    l2.init_list([23,4576,688,2,4,4,67])
    l1.combination(l2)
    a=l1.sort()
    a.show()
