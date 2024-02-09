from LinkedList import LinkedList


def run_tests():
    print("\n")
    list1 = LinkedList()
    list1.insert_at_end(3)
    list1.insert_at_end(1)
    list1.insert_at_end(5)

    list2 = LinkedList()
    list2.insert_at_end(2)
    list2.insert_at_end(4)
    list2.insert_at_end(6)

    print("Список 1:")
    list1.print_list()
    print("Список 2:")
    list2.print_list()

    # Реверсування списку
    list1.reverse()
    print("Реверсований список 1:")
    list1.print_list()

    # Сортування списку
    list1.sort()
    print("Відстортований список 1:")
    list1.print_list()
    list2.sort()
    print("Відстортований список 2:")
    list2.print_list()

    # Об'єднання відсортованих списків
    merged_list = LinkedList.merge_sorted_lists(list1, list2)
    print("Обʼєднання спиків 1 і 2:")
    while merged_list:
        print(merged_list.data, end=" -> ")
        merged_list = merged_list.next
    print(None)
    print("\n")


if __name__ == "__main__":
    run_tests()
