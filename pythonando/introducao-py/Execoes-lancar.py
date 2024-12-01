# exemplo de uma lib, que não permite usar números negativos

def operacao(num1, num2):
    if num1 <= 0 or num2 <= 0:
        raise ValueError('operacao NÃO pode usar números negativos, nem zeros')
    return (((num1 * num2) + num1 + num2) / (num2 - num1))


print(operacao(int(input('Digite um Número: ')), int(input('Digite outro número: '))))
