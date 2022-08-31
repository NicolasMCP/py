# Nícolas Ramos
# data: 6/8/2022
# Livro Use a cabeça Python pág. 193
# Código proprio solicitadas as modificações no livro.

def busque_letras(frase: str, letras: str) -> str:
    """
    Devolve as letras (fornecidas) encontradas (em ordem alfabética) na frase dada.
    """
    busque = set(letras.lower())
    return ''.join(sorted(busque.intersection(set(frase.lower()))))


if __name__ == "__main__":
    encontre = 'nxy'
    print(f"Nicolas, {encontre}       >>-->", busque_letras("Nicolas", encontre))
    print("Hitch-hiker, aeiou >>-->", busque_letras("Hitch-hiker", 'aeiou'))
    print(f"Galaxy, {encontre}        >>-->", busque_letras("Galaxy", encontre))
    print(f"Sky, {encontre}           >>-->", busque_letras("Sky", encontre))
