class TreeNode(object):

    def __init__(self, data, parent=None, children=None):
        self._data = data
        self._parent = parent
        if parent is not None:
            parent.add_child(self)
        if children is None:
            children = []
        self._children = children

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    @property
    def children(self):
        return self._children

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def is_root(self):
        return self._parent is None

    def is_leaf(self):
        if len(self._children) == 0:
            return True
        else:
            return False

    def add_child(self, node):
        node._parent = self
        self._children.append(node)

    def __str__(self):
        return str(self._data)


class Tree(object):

    def __init__(self, root=None):
        self._root = root

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, value):
        self._root = value

    def is_empty(self):
        return self._root is None

    def depth(self, node):

        if node.is_root():
            return 0
        else:
            return 1 + self.depth(node._parent)

    def _height(self, node):

        if node.is_leaf():
            return 0
        else:
            return 1 + max(self._height(nodeC) for nodeC in node._children)

    def height(self):

        return self._height(self._root)

    def _preOrder(self, node):
        if not self.is_empty():
            print(node._data)
            for nodeC in node._children:
                self._preOrder(nodeC)

    def preOrder(self):
        self._preOrder(self._root)

    def _postOrder(self, node):
        if not self.is_empty():
            for nodeC in node._children:
                self._postOrder(nodeC)
            print(node._data)

    def postOrder(self):
        self._postOrder(self._root)
