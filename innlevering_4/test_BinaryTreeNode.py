from BinaryTreeNode import BinaryTreeNode
from collections import namedtuple
import pytest


Person = namedtuple('Person',['etternavn','fornavn','adresse','postnummer','poststed'])

test_person_1 = Person('KRISTIANSEN','MORTEN KRISTIAN','LEINANYTTA 36','7224','MELHUS')

test_person_2 = Person('OLDERVIK','SHARI LILL','KRÆKA 84','5948','FEDJE')

empty_test_person = Person('JOHNSEN', 'STIAN', 'HELLVEIEN 14', '666666', 'HELL')

test_person_1_BinaryTreeNode = BinaryTreeNode(test_person_1)

test_person_2_BinaryTreeNode = BinaryTreeNode(test_person_2)

empty_test_person_BinaryTreeNode = BinaryTreeNode(empty_test_person)
empty_test_person_BinaryTreeNode.value = None

def test_value_get():
    assert test_person_1_BinaryTreeNode.value.etternavn == 'KRISTIANSEN'

def test_value_set():
    new_test_person_BinaryTreeNode = test_person_1_BinaryTreeNode.value._replace(etternavn='ELLINGSEN')
    assert new_test_person_BinaryTreeNode.etternavn == 'ELLINGSEN'

def test_set_and_get_left():
    test_person_2_BinaryTreeNode.left = test_person_1_BinaryTreeNode.value
    assert test_person_2_BinaryTreeNode.left is not None

def test_set_and_get_right():
    test_person_2_BinaryTreeNode.right = test_person_1_BinaryTreeNode.value
    assert test_person_2_BinaryTreeNode.right is not None

#def test_str():
    #assert test_person_1_BinaryTreeNode.__str__() == "Person(etternavn='KRISTIANSEN', fornavn='MORTEN KRISTIAN', adresse='LEINANYTTA 36', postnummer='7224', poststed='MELHUS')"
def test_has_right():
    test_person_2_BinaryTreeNode.right = test_person_1_BinaryTreeNode.value
    assert test_person_2_BinaryTreeNode.hasRight() == True
    assert test_person_1_BinaryTreeNode.hasRight() == False
def test_has_left():
    test_person_2_BinaryTreeNode.left = test_person_1_BinaryTreeNode.value
    assert test_person_2_BinaryTreeNode.hasLeft() == True
    assert test_person_1_BinaryTreeNode.hasLeft() == False

def test__eq__():
    test_person_1_same = Person('KRISTIANSEN', 'MORTEN KRISTIAN', 'LEINANYTTA 36', '7224', 'MELHUS')
    test_person_1_same_BinaryTreeNode = BinaryTreeNode(test_person_1_same)
    assert test_person_1_BinaryTreeNode.__eq__(test_person_2_BinaryTreeNode) == False
    assert empty_test_person_BinaryTreeNode.__eq__(None) == True
    assert test_person_1_BinaryTreeNode.__eq__(None) == False

def test__ne__():
    assert empty_test_person_BinaryTreeNode.__ne__(test_person_1_BinaryTreeNode) == False
    assert test_person_1_BinaryTreeNode.__ne__(None) == True

@pytest.mark.xfail
def test__ne__fail():
    assert test_person_1_BinaryTreeNode.__ne__(test_person_2_BinaryTreeNode) == True
def test__lt__():

    assert test_person_1_BinaryTreeNode.__lt__(None) == False
    assert test_person_1_BinaryTreeNode.__lt__(test_person_2_BinaryTreeNode) == True
    assert empty_test_person_BinaryTreeNode.__lt__(None) == False

def test__le__():
    assert test_person_1_BinaryTreeNode.__le__(None) == False
    assert test_person_1_BinaryTreeNode.__le__(test_person_2_BinaryTreeNode) == True
    assert empty_test_person_BinaryTreeNode.__le__(None) == False

def test__gt__():
    assert test_person_1_BinaryTreeNode.__gt__(None) == False
    assert test_person_1_BinaryTreeNode.__gt__(test_person_2_BinaryTreeNode) == False
    assert empty_test_person_BinaryTreeNode.__gt__(None) == False

def test__ge__():
    assert test_person_1_BinaryTreeNode.__ge__(None) == False
    assert test_person_1_BinaryTreeNode.__ge__(test_person_2_BinaryTreeNode) == False
    assert empty_test_person_BinaryTreeNode.__ge__(None) == False
