from BinaryTree import BinaryTree
from collections import namedtuple
import pytest


persons_binary_tree = BinaryTree()

persons_lst = []
person_tuple = namedtuple('person_tuple',['etternavn','fornavn','adresse','postkode','poststed'])
counter = 0
with open ('Personer.dta',encoding = 'ISO-8859-1') as file:
        for i in file:
            if counter == 15:
                break
            persons_lst.append(person_tuple(*i.replace('\n','').split(';')))
            counter+=1

for i in range (len(persons_lst)):
    persons_binary_tree.insert(value = persons_lst[i])

def test_find_left_most():
    assert persons_binary_tree.findLeftMost(persons_binary_tree._root).value == persons_lst[10]

def test_find_min():
    assert persons_binary_tree.findMin().value == persons_lst[10]


def test_find_right_most():
    assert persons_binary_tree.findRightMost(persons_binary_tree._root).value == persons_lst[5]

def test_find_max():
    assert persons_binary_tree.findMax().value == persons_lst[5]

def test_find():
    assert persons_binary_tree.find(persons_lst[0]) is not None


def test_delete_min():
    assert persons_binary_tree.deleteMin() is not None

def test_delete_max():
    assert persons_binary_tree.deleteMax() is not None

def test_delete():
    assert persons_binary_tree.delete(persons_lst[0]) is not None




