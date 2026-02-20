from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
	val: int
	left: Optional['Node'] = None
	rigth: Optional['Node'] = None

class BinaryTree:
	def __init__ (self):
		self.root = None

	def insert(self, root: Node, key: int) -> Node :
		if root is None:
			return Node(key)
		if key < root.val:
			root.left = self.insert(root.left, key)
		else:
			root.rigth = self.insert(root.rigth, key)
		return root

# Peoceso: Insercion y recorrido In-Order (Ordenado)
tree = BinaryTree()
root = tree.insert(None, 50)
for val in [30,70,20,40]:
	tree.insert(root, val)	
	print(root)
print("Hola Mundo")	 
