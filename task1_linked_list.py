class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Додавання елемента в кінець списку
    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    # Виведення списку
    def print_list(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    # Реверсування списку
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    # Сортування Merge Sort
    def merge_sort(self, head):

        # Базовий випадок
        if not head or not head.next:
            return head

        # Знаходимо середину
        middle = self.get_middle(head)
        next_to_middle = middle.next

        # Розділяємо список
        middle.next = None

        # Рекурсивно сортуємо
        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        # Зливаємо
        sorted_list = self.sorted_merge(left, right)

        return sorted_list

    # Об'єднання двох відсортованих списків
    def sorted_merge(self, left, right):

        if not left:
            return right

        if not right:
            return left

        if left.data <= right.data:
            result = left
            result.next = self.sorted_merge(left.next, right)
        else:
            result = right
            result.next = self.sorted_merge(left, right.next)

        return result

    # Пошук середини списку
    def get_middle(self, head):

        if not head:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    # Запуск сортування
    def sort(self):
        self.head = self.merge_sort(self.head)

    # Об'єднання двох відсортованих списків
    @staticmethod
    def merge_two_sorted_lists(list1, list2):

        dummy = Node(0)
        tail = dummy

        left = list1.head
        right = list2.head

        while left and right:

            if left.data <= right.data:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next

            tail = tail.next

        # Додаємо залишок
        if left:
            tail.next = left

        if right:
            tail.next = right

        merged_list = LinkedList()
        merged_list.head = dummy.next

        return merged_list


# -----------------------------
# ТЕСТУВАННЯ
# -----------------------------

print("Початковий список:")
ll = LinkedList()

ll.append(5)
ll.append(1)
ll.append(9)
ll.append(3)
ll.append(7)

ll.print_list()

# Реверсування
print("\nРеверсований список:")
ll.reverse()
ll.print_list()

# Сортування
print("\nВідсортований список:")
ll.sort()
ll.print_list()

# -----------------------------
# Об'єднання двох списків
# -----------------------------

list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(5)

list2 = LinkedList()
list2.append(2)
list2.append(4)
list2.append(6)

print("\nПерший список:")
list1.print_list()

print("Другий список:")
list2.print_list()

merged = LinkedList.merge_two_sorted_lists(list1, list2)

print("Об'єднаний відсортований список:")
merged.print_list()