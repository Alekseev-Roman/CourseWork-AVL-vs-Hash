import time

class Node:
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None
        self.height = 0

    def __str__(self):
        left = self.left_child.key if self.left_child else None
        right = self.right_child.key if self.right_child else None
        return 'key: {}, left: {}, right: {}'.format(self.key, left, right)

class AVLTree:
    def __init__(self):
        self.root = None

    def print_tree(self):
        self.print_AVL(False, '', self.root)
        print()

    def print_AVL(self, isL, prefix, node):
        if(node != None):
            print(prefix, end='')
            if isL:
                print('└── L ', end='')
            else:
                print('└── R ', end='')
            print(node.key)
            if isL:
                prefix += '│   '
            else:
                prefix += '    '
            self.print_AVL(True, prefix, node.left_child)
            self.print_AVL(False, prefix, node.right_child)

    def add_key(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self.root = self.add_node(key, self.root)

    def add_key_time(self, key):
        time_start = time.perf_counter()
        if not self.root:
            self.root = Node(key)
        else:
            self.root = self.add_node(key, self.root)
        dif_time = (time.perf_counter() - time_start) * 100
        return dif_time
        #print(f"Время, затраченное для добавление элемента - {dif_time:0.4f} мс")

    def add_node(self, key, node):
        if not node:
            node = Node(key)
        elif key < node.key:
            node.left_child = self.add_node(key, node.left_child)
            if self.get_height(node.left_child) - self.get_height(node.right_child) >= 2:
                if key < node.left_child.key:
                    node = self.small_right_rotate(node)
                else:
                    node = self.big_right_rotate(node)
        elif key > node.key:
            node.right_child = self.add_node(key, node.right_child)
            if self.get_height(node.right_child) - self.get_height(node.left_child) >= 2:
                if key < node.right_child.key:
                    node = self.big_left_rotate(node)
                else:
                    node = self.small_left_rotate(node)
        else:
            return node
        node.height = max(self.get_height(node.left_child), self.get_height(node.right_child)) + 1
        return node

    def get_height(self, node):
        if not node:
            return 0
        else:
            return node.height

    def small_left_rotate(self, node_a):
        node_b = node_a.right_child
        node_a.right_child = node_b.left_child
        node_b.left_child = node_a

        node_a.height = max(self.get_height(node_a.right_child), self.get_height(node_a.left_child)) + 1
        node_b.height = max(self.get_height(node_b.right_child), self.get_height(node_b.left_child)) + 1

        return node_b

    def small_right_rotate(self, node_b):
        node_a = node_b.left_child
        node_b.left_child = node_a.right_child
        node_a.right_child = node_b

        node_a.height = max(self.get_height(node_a.right_child), self.get_height(node_a.left_child)) + 1
        node_b.height = max(self.get_height(node_b.right_child), self.get_height(node_b.left_child)) + 1

        return node_a

    def big_left_rotate(self, node_a):
        node_b = node_a.right_child
        node_a.right_child = self.small_right_rotate(node_b)
        node_c = self.small_left_rotate(node_a)

        return node_c

    def big_right_rotate(self, node_a):
        node_b = node_a.left_child
        node_a.left_child = self.small_left_rotate(node_b)
        node_c = self.small_right_rotate(node_a)

        return node_c

    def get_root(self):
        return self.root

    def search_key(self, key):
        node = self.root
        while True:
            if key == node.key:
                return node
            else:
                if key < node.key:
                    if node.left_child == None:
                        #print("Узла с ключом {} нет в дереве".format(key))
                        return Node(None)
                    node = node.left_child
                else:
                    if node.right_child == None:
                        #print("Узла с ключом {} нет в дереве".format(key))
                        return Node(None)
                    node = node.right_child

    def search_key_time(self, key):
        time_start = time.perf_counter()
        node = self.root
        while True:
            if key == node.key:
                dif_time = (time.perf_counter() - time_start) * 100
                #print(f"Время, затраченное для поиск элемента - {dif_time:0.4f} мс")
                return dif_time
            else:
                if key < node.key:
                    if node.left_child == None:
                        #print("Узла с ключом {} нет в дереве".format(key))
                        dif_time = (time.perf_counter() - time_start) * 100
                        #print(f"Время, затраченное для поиск элемента - {dif_time:0.4f} мс")
                        return dif_time
                    node = node.left_child
                else:
                    if node.right_child == None:
                        #print("Узла с ключом {} нет в дереве".format(key))
                        dif_time = (time.perf_counter() - time_start) * 100
                        #print(f"Время, затраченное для поиск элемента - {dif_time:0.4f} мс")
                        return dif_time
                    node = node.right_child

    def delete_key(self, key):
        if self.search_key(key).key == -1:
            return
        else:
            self.root = self.delete_node(key, self.root)

    def delete_key_time(self, key):
        time_start = time.perf_counter()
        if self.search_key(key).key == -1:
            return
        else:
            self.root = self.delete_node(key, self.root)
        dif_time = (time.perf_counter() - time_start) * 100
        #print(f"Время, затраченное для удаления элемента - {dif_time:0.4f} мс")
        return dif_time

    def delete_node(self, key, node):
        if not node:
            return None
        if key < node.key:
            node.left_child = self.delete_node(key, node.left_child)
        elif key > node.key:
            node.right_child = self.delete_node(key, node.right_child)
        else:
            node_L = node.left_child
            node_R = node.right_child
            if node_R == None:
                return node_L
            min_node = self.search_min(node_R)
            min_node.right_child = self.remove_min(node_R)
            min_node.left_child = node_L
            if self.root.key == key:
                self.root = min_node
            return self.balance(min_node)
        return self.balance(node)

    def remove_min(self, node):
        if not node.left_child:
            return node.right_child
        node.left_child = self.remove_min(node.left_child)
        return self.balance(node)

    def search_min(self, node):
        if node.left_child:
            return self.search_min(node.left_child)
        else:
            return node

    def balance(self, node):
        if self.get_height(node.right_child) - self.get_height(node.left_child) >= 2:
            if self.get_height(node.right_child.right_child) - self.get_height(node.right_child.left_child) < 0:
                node.right_child = self.small_right_rotate(node.right_child)
            return self.small_left_rotate(node)

        if self.get_height(node.left_child) - self.get_height(node.right_child) >= 2:
            if self.get_height(node.left_child.right_child) - self.get_height(node.left_child.left_child) > 0:
                node.left_child = self.small_left_rotate(node.left_child)
            return self.small_right_rotate(node)

        return node


if __name__ == '__main__':
    nodes = list(map(int, input().split()))
    avl_tree = AVLTree()
    for index, node in enumerate(nodes):
        avl_tree.add_key(node)
    avl_tree.print_tree()
    avl_tree.add_key(200)
    avl_tree.print_tree()
    avl_tree.add_key(199)
    avl_tree.print_tree()
