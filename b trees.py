class Node:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []
        self.next = None


class BPlusTree:
    def __init__(self, t=3):
        self.root = Node(leaf=True)
        self.t = t


    def search(self, key, node=None):
        if node is None:
            node = self.root

        if node.leaf:
            return self._search_in_list(node.keys, key, 0)

        i = self._find_index(node.keys, key, 0)
        return self.search(key, node.children[i])

    def _search_in_list(self, arr, key, i):
        if i >= len(arr):
            return False
        if arr[i] == key:
            return True
        return self._search_in_list(arr, key, i + 1)


    def insert(self, key):
        new_key, new_child = self._insert_recursive(self.root, key)

        if new_child:
            new_root = Node()
            new_root.keys = [new_key]
            new_root.children = [self.root, new_child]
            self.root = new_root

    def _insert_recursive(self, node, key):
        if node.leaf:
            self._insert_into_sorted(node.keys, key)
            if len(node.keys) < 2 * self.t:
                return None, None
            return self._split_leaf(node)

        i = self._find_index(node.keys, key, 0)
        new_key, new_child = self._insert_recursive(node.children[i], key)

        if new_child is None:
            return None, None

        node.keys.insert(i, new_key)
        node.children.insert(i + 1, new_child)

        if len(node.keys) < 2 * self.t:
            return None, None

        return self._split_internal(node)


    def _find_index(self, keys, key, i):
        if i >=  len(keys) or key < keys[i]:
            return i
        return self._find_index(keys, key, i + 1)

    def _insert_into_sorted(self, arr, key, i=0):
        if i >= len(arr):
            arr.append(key)
            return
        if key < arr[i]:
            arr.insert(i, key)
            return
        self._insert_into_sorted(arr, key, i + 1)

    def _split_leaf(self, node):
        mid = len(node.keys) // 2
        new_node = Node(leaf=True)

        new_node.keys = node.keys[mid:]
        node.keys = node.keys[:mid]

        new_node.next = node.next
        node.next = new_node

        return new_node.keys[0], new_node

    def _split_internal(self, node):
        mid = len(node.keys) // 2
        new_node = Node()

        promote = node.keys[mid]

        new_node.keys = node.keys[mid + 1:]
        node.keys = node.keys[:mid]

        new_node.children = node.children[mid + 1:]
        node.children = node.children[:mid + 1]

        return promote, new_node


    def traverse_leaves(self):
        leftmost = self._get_leftmost(self.root)
        return self._collect_leaves(leftmost)

    def _get_leftmost(self, node):
        if node.leaf:
            return node
        return self._get_leftmost(node.children[0])

    def _collect_leaves(self, node):
        if node is None:
            return []
        return node.keys + self._collect_leaves(node.next)



if __name__ == "__main__":
    bpt = BPlusTree(t=2)

    data = [10, 20, 5, 6, 12, 30, 7, 17]
    for x in data:
        bpt.insert(x)

    print("Search 6:", bpt.search(6))
    print("Search 15:", bpt.search(15))
    print("Traversal:", bpt.traverse_leaves())