from typing import Any, Optional


class Node:
    def __init__(self, value: Optional[Any] = None, next: Optional['Node'] = None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return 'Node[{value}]'.format(
            value=str(self.value)
        )


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.lenght = 0

    def __str__(self) -> str:
        if self.head is not None:
            corrent = self.head
            value = [str(corrent.value)]
            while corrent.next is not None:
                corrent = corrent.next
                value.append(str(corrent.value))
            return f'[{' '.join(value)}]'
        return 'LinkedList []'

    def append(self, elem: Any) -> None:
        new_node = Node(elem)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        self.lenght += 1

    def remove(self, index) -> None:
        cur_node = self.head
        cur_index = 0
        if self.lenght == 0 or self.lenght <= index:
            raise IndexError
        if cur_node is not None:
            if index == 0:
                self.head = cur_node.next
                self.lenght -= 1
                return

        while cur_node is not None:
            if cur_index == index:
                break
            prev = cur_node
            cur_node = cur_node.next
            cur_index += 1

        prev.next = cur_node.next
        self.lenght -= 1


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print(my_list)
print()
my_list.remove(0)
print(my_list)
