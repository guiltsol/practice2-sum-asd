class Node:
    def __init__(self, data):
        self.data = data #значение 
        self.next = None #указатель на слелующий элемент списка
        self.prev = None #указатель на предыдущий элемент списка 

class DoublyLinkedList:
    def __init__(self):#конструктор
        self.head = None

    def add_node(self, data):#функция добавления в двусвязный список
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def remove_node(self, data):#функция удаления из двусвязного списка 
        if not self.head:
            return
        temp = self.head
        if temp.data == data:
            self.head = temp.next
            temp.next.prev = None
            return
        while temp:
            if temp.data == data:
                if temp.next:
                    temp.next.prev = temp.prev
                temp.prev.next = temp.next
                return
            temp = temp.next

    def cyclic_permutation(self):#функция циклического сдвига двусвязного списка 
        if not self.head or not self.head.next:
            return
        old_head = self.head
        self.head = old_head.next
        self.head.prev = None
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = old_head
        old_head.prev = temp
        old_head.next = None

    def print_list(self):#функция печати двусвязного списка 
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

if __name__ == "__main__":
    dll = DoublyLinkedList()#создаем двусвязный список 
    n=int(input("Введите кол-во элементов которое хотите добавить в двусвязный список:"))
    for j in range(n):#заполняем двусвязный список 
      print("a[",j,"]= ",end=" ")
      i=input()#вводим значение которое хотим добавить в список
      dll.add_node(i)#добавляем значение в список 
    print("Наш список:")
    dll.print_list()#выводим на экран двусвязный список 
    print("Введите элемент который хотите удалить из двусвязного списка:")
    i=input()#вводим элемент который хотим удалить из списка 
    dll.remove_node(i)#удаляем из списка заданный элемент
    print("Наш список:")  
    dll.print_list()
    print("Совершить циклический сдвиг?: 1.Да 2.Нет")
    k=int(input())
    if k==1:
      dll.cyclic_permutation()#совершаем циклический сдвиг
      print("Циклический сдвиг совершен:")
      dll.print_list()
    else:
      print("Завершение программы")