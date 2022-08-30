def tem_vogais(frase):
    """Devolve as vogais encontradas na frase fornecida"""
    vogais = set('aeiou')
    encontradas = vogais.intersection(set(frase))
    return ''.join(sorted(encontradas))


if __name__ == "__main__":
    print("vogais >>-->", tem_vogais("Nicolas"))
    print("vogais >>-->", tem_vogais("Hitch-hiker"))
    print("vogais >>-->", tem_vogais("Galaxy"))
    print("vogais >>-->", tem_vogais("Sky"))
