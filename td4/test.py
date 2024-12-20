# test.py

from main import hello  # Importer la fonction hello depuis main

def test_hello():
    assert hello() == "Hello world!"  # Corriger la casse et la chaîne attendue
