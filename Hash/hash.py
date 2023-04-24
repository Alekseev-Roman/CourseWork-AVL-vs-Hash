import time

class Node:
    def __init__(self, key):
        self.key = key
        self.child = None
        self.parent = None

    def __str__(self):
        result = 'Key: ' + str(self.key)
        if self.parent:
            result += ', parent: ' + str(self.parent.key)
        else:
            result += ', parent: None'
        if self.child:
            result += ', child: ' + str(self.child.key)
        else:
            result += ', child: None'
        return result

class Hash_table:
    def __init__(self):
        self.P = 7757
        self.table = [Node(None) for a in range(self.P)]

    def hash_func(self, key):
        return key % self.P

    def add_key(self, key):
        hash = self.hash_func(key)
        new_node = Node(key)
        if self.table[hash].key == None:
            self.table[hash] = new_node
        else:
            node = self.table[hash]
            while True:
                if node.child == None:
                    node.child = new_node
                    new_node.parent = node
                    break
                elif node.key == key:
                    break
                else:
                    node = node.child

    def add_key_time(self, key):
        time_start = time.perf_counter()
        hash = self.hash_func(key)
        new_node = Node(key)
        if self.table[hash].key == None:
            self.table[hash] = new_node
        else:
            node = self.table[hash]
            while True:
                if node.child == None:
                    node.child = new_node
                    new_node.parent = node
                    break
                elif node.key == key:
                    break
                else:
                    node = node.child
        dif_time = (time.perf_counter() - time_start) * 100
        #print(f"Время, затраченное для добавление элемента - {dif_time:0.4f} мс")
        return dif_time

    def search_key(self, key):
        hash = self.hash_func(key)
        node = self.table[hash]
        while True:
            if node.key == key:
                return node
            else:
                node = node.child
                if node == None:
                    print("Элемента с ключом {} в хэш-таблице нет".format(key))
                    return Node(None)

    def search_key_time(self, key):
        time_start = time.perf_counter()
        hash = self.hash_func(key)
        node = self.table[hash]
        while True:
            if node.key == key:
                dif_time = (time.perf_counter() - time_start) * 100
                #print(f"Время, затраченное для поиск элемента - {dif_time:0.4f} мс")
                return dif_time
            else:
                node = node.child
                if node == None:
                    print("Элемента с ключом {} в хэш-таблице нет".format(key))
                    dif_time = (time.perf_counter() - time_start) * 100
                    #print(f"Время, затраченное для поиск элемента - {dif_time:0.4f} мс")
                    return dif_time

    def delete_key(self, key):
        hash = self.hash_func(key)
        node = self.search_key(key)
        if not node:
            return
        else:
            p_node = node.parent
            c_node = node.child
            if not p_node:
                if not c_node:
                    self.table[hash] = Node(None)
                else:
                    self.table[hash] = c_node
            else:
                p_node.child = c_node

    def delete_key_time(self, key):
        time_start = time.perf_counter()
        hash = self.hash_func(key)
        node = self.search_key(key)
        if not node:
            dif_time = (time.perf_counter() - time_start) * 100
            #print(f"Время, затраченное для удаления элемента - {dif_time:0.4f} мс")
            return dif_time
        else:
            p_node = node.parent
            c_node = node.child
            if not p_node:
                if not c_node:
                    self.table[hash] = Node(None)
                else:
                    self.table[hash] = c_node
            else:
                p_node.child = c_node
        dif_time = (time.perf_counter() - time_start) * 100
        #print(f"Время, затраченное для удаления элемента - {dif_time:0.4f} мс")
        return dif_time

if __name__ == '__main__':
    #nodes = list(map(int, input().split()))
    nodes = [a for a in range(1000000)]
    hash_table = Hash_table()
    for a in nodes:
        hash_table.add_key(a)