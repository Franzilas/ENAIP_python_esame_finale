import pytest
from progetto.modulo1 import funzione1, funzione2, funzione3, classeDaFinire
#branchupdate

def test_funzione1():
    # TODO Aggiungere 2 o più test per coprire funzione1
    assert funzione1(2,5) == 10
    assert funzione1(4,2) == 8

def test_funzione2():
    # TODO Aggiungere 2 o più test per coprire funzione2
    assert funzione2("Giovanni") == "Buona serata Giovanni"
    assert funzione2("Franco") == "Buona serata Franco"

def test_funzione3():
    # TODO Aggiungere 2 o più test per coprire funzione3
    assert funzione3(5,10) == 10
    assert funzione3(-5,10) == 10


def test_metodo1():
    istanza = classeDaFinire("Nome", 10, "Milano")
    # TODO: Modificare l'assert per far passare il test
    assert istanza.metodo1() == "Ciao, sono Nome, ho 10 anni e vengo da Milano!"

def test_metodo2():
    istanza = classeDaFinire("Nome2", 35, "Trieste")
    istanza.metodo2(5)
    # TODO: Aggiungere un'asserzione per verificare il comportamento del metodo2
    assert istanza.metodo2(5) == "Ciao, il mio numero fortunato è 40 !"

