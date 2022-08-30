# Nícolas Ramos
# data: 6/8/2022
# Livro Use a cabeça Python pág. 162
# Código proprio semelhante ao exemplo do livro.

def tem_vogais(frase: str) -> str:
    """
    Devolve as vogais encontradas (em ordem alfabética) na frase fornecida.
    """
    vogais = set('aeiou')
    return ''.join(sorted(vogais.intersection(set(frase))))


if __name__ == "__main__":
    print("Nicolas, vogais     >>-->", tem_vogais("Nicolas"))
    print("Hitch-hiker, vogais >>-->", tem_vogais("Hitch-hiker"))
    print("Galaxy, vogais      >>-->", tem_vogais("Galaxy"))
    print("Sky, vogais         >>-->", tem_vogais("Sky"))
