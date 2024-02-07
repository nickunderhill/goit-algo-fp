class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Реверсування
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Сортування вставками
    def sort(self):
        if not self.head or not self.head.next:
            return

        sorted_list = LinkedList()

        current = self.head
        while current:
            next_node = current.next
            current.next = None
            sorted_list.insert_sorted(current.data)
            current = next_node

        self.head = sorted_list.head

    def insert_sorted(self, value):
        new_node = Node(value)
        if not self.head or self.head.data >= value:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data < value:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    # Злиття двох відсортованих списків
    @staticmethod
    def merge_sorted_lists(list1, list2):
        h1 = list1.head
        h2 = list2.head
        dummy = Node()
        tail = dummy
        while h1 and h2:
            if h1.data < h2.data:
                tail.next, h1 = h1, h1.next
            else:
                tail.next, h2 = h2, h2.next
            tail = tail.next
        tail.next = h1 or h2
        return dummy.next
