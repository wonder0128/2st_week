class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        cur_index = 0

        while cur_index != index :
            cur = cur.next
            cur_index += 1

        return cur

    def add_node(self, index, value):
        new_node = Node(value)

        # index의 값이 0이라면?
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        # index - 1번째의 노드가 필요
        prev_node = self.get_node(index - 1)

        next_node = prev_node.next
        prev_node.next = new_node
        new_node.next = next_node

    def delete_node(self, index):
        # index의 값이 0이라면?
        if index == 0:
            self.head = self.head.next
            return

        # index - 1번째 노드
        prev_node = self.get_node(index - 1)
        index_node = self.get_node(index)
        prev_node.next = index_node.next

        print("index번째 node를 제거하기")
    
linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
# print(linked_list.get_node(1).data) # -> 5를 들고 있는 노드를 반환해야 합니다!

linked_list.add_node(1, 6)
linked_list.add_node(0, 9)
linked_list.delete_node(0)
linked_list.print_all()
