from BinaryTreeNode import BinaryTreeNode
from collections import namedtuple


Person = namedtuple('Person',['etternavn','fornavn','adresse','postnummer','poststed'])

test_person = Person('KRISTIANSEN','MORTEN KRISTIAN','LEINANYTTA 36','7224','MELHUS')

test_BinaryTree_Node = BinaryTreeNode(test_person)

def test_value_get():
    assert test_BinaryTree_Node.value.etternavn == 'KRISTIANSEN'

def test_value_set():
    new_test_BinaryTree_Node = test_BinaryTree_Node.value._replace(etternavn='ELLINGSEN')
    assert new_test_BinaryTree_Node.etternavn == 'ELLINGSEN'

