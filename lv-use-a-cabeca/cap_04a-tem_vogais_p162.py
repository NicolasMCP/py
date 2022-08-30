def tem_vogais(frase):
    """Devolve True ou False se tiver ou não vogais"""
    vogais = set('aeiou')
    encontradas = vogais.intersection(set(frase))
    # return ''.join(sorted(encontradas))
    return bool(encontradas)


if __name__ == "__main__":
    print("vogais >>-->", tem_vogais("Nicolas"), "  -  Nicolas")
    print("vogais >>-->", tem_vogais("Hitch-hiker"), "  -  Hitch-hiker")
    print("vogais >>-->", tem_vogais("Galaxy"), "  -  Galaxy")
    print("vogais >>-->", tem_vogais("Sky"), " -  Sky")
