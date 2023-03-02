class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head: Node = None
    
    def display(self):
        if not self.head:
            print("Tidak ada node")
            return
        
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
            if current:
                print(" -> ", end=" ")
        print()
        return

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)
        return

    def delete(self, data):
        if not self.head:
            print("Tidak ada node")
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

        print("Data tidak ditemukan")

    def search(self, data):
        if not self.head:
            print("Tidak ada Node")
            return 
        
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return

def clear():
    import os
    os.system("cls|clear")

if __name__ == "__main__":
    linked_list = LinkedList()
    while True:
        print("============================================")
        print(" Kelompok 8")
        print(" Anggota : Ahmad nur sahid (2206042)")
        print("         : R Muhammad Arya Fajar S (2206066)")
        print("         : Azki Fadilah (2206048)")
        print("--------------------------------------------")
        print("Menu: ")
        print("(1) Tambah data")
        print("(2) Delete data")
        print("(3) Tampilkan data")
        print("(4) Cari data")
        print("(5) Keluar")

        index = input("pilih: ")
        clear()

        if index == "1":
            data = int(input("Masukkan data yang ingin ditambahkan: "))
            linked_list.insert(data)
        elif index == "2":
            data = int(input("Masukkan data yang ingin dihapus: "))
            linked_list.delete(data)
        elif index == "3":
            linked_list.display()
        elif index == "4":
            data = int(input("Masukkan data yang di cari: "))
            if (linked_list.search(data)):
                print(f"Data {data} ditemukan")
            else:
                print("Data Yang di cari tidak ditemukan")
        elif index == "5":
            break
        else:
            print("Input tidak valid")