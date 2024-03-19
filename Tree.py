class BNode:

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


class BinarySearchTree:

    def __init__(self):
        self.root = BNode()
        self.size = 0

    def is_empty(self):
        return not self.size

    def add(self, value, node=None):
        if self.is_empty():
            self.root = BNode(value)
            self.size += 1

        else:
            if node is None:
                node = self.root

            if value > node.value:
                if node.right is None:
                    node.right = BNode(value)
                    self.size += 1
                else:
                    self.add(value, node.right)
            else:
                if node.left is None:
                    node.left = BNode(value)
                    self.size += 1
                else:
                    self.add(value, node.left)

    def print_tree(self, node=None):
        if self.is_empty():
            return

        if node == None:
            node = self.root

        if node.left:
            self.print_tree(node.left)
        print(node.value)
        if node.right:
            self.print_tree(node.right)

    def is_value_in(self, value, node=None):
        if node is None:
            node = self.root

        if node is None:
            return None

        if value == node.value:
            return True

        if value > node.value:
            if node.right:
                return self.is_value_in(value, node.right)
            else:
                return False
        else:
            if node.left:
                return self.is_value_in(value, node.left)
            else:
                return False

    def get_track_to_value(self, value, track=None, node=None):
        if node is None:
            node = self.root

        if node is None:
            return None

        if track is None:
            track = []

        if value == node.value:
            return track if track else None

        if value > node.value:
            if node.right:
                track.append(1)
                return self.get_track_to_value(value, track, node.right)
            else:
                return None
        else:
            if node.left:
                track.append(0)
                return self.get_track_to_value(value, track, node.left)
            else:
                return None

    def get_track_to_node(self, node_id, track=None, node=None):
        if node is None:
            node = self.root

        if node is None:
            return None

        if track is None:
            track = []

        if id(node) == node_id:
            return track

        if node.right:
            track.append(1)
            res = self.get_track_to_node(node_id, track, node.right)
            if res is not None:
                return res
            track.pop()
        if node.left:
            track.append(0)
            res = self.get_track_to_node(node_id, track, node.left)
            if res is not None:
                return res
            track.pop()

    def remove_node(self, value):
        self.root = self._remove_node(value, self.root)

    def _remove_node(self, value, node=0):
        if node is None:
            return None

        if value < node.value:
            node.left = self._remove_node(value, node.left)
        elif value > node.value:
            node.right = self._remove_node(value, node.right)
        else:
            if not node.left:
                return node.right

            elif not node.right:
                return node.left

            curr = node.right
            while curr.left:
                curr = curr.left
            node.value = curr.value
            node.right = self._remove_node(curr.value, node.right)
        return node