while True:
    try:
        x = int(input('Digite um numero: '))
        print(5/x)
        break
    except ValueError:
        print('Digite um número inteiro...')
    except ZeroDivisionError:
        print('Não digite 0!')
    finally:
        print('Sempre passa por aqui, enquanto estiver no loop\n')

print('Fora do loop')
