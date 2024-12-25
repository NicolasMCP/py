from datetime import datetime, date

class Categoria:
    def __init__(self, categoria: str):
        self.categoria = categoria

class Produto:
    def __init__(self, codigo: int, nome: str, preco: float, categoria: Categoria):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

class Estoque:
    def __init__(self, produto: Produto, quantia: int):
        self.produto = produto
        self.quantia = quantia

class Cadastro:
    def __init__(self, nome: str, endereco: str, email: str, telefone: str, cpf: str):
        self.nome = nome
        self.endereco = endereco
        self.email = email
        self.telefone = telefone
        self.cpf = cpf

class Fornecedor(Cadastro):
    def __init__(self, nome: str, endereco: str, email: str, telefone: str, cpf: str,
                 contato: str, cnpj: str, ie: str):
        super().__init__(nome, endereco, email, telefone, cpf)
        self.contato = contato
        self.cnpj = cnpj
        self.ie = ie

class Cliente(Cadastro):
    def __init__(self, nome: str, endereco: str, email: str, telefone: str, cpf: str):
        super().__init__(nome, endereco, email, telefone, cpf)
        # Caso venha a ter muitos clientes PJ pode se incluir aqui CNPJ \
        # como opcional, visto que a maioria sera PF

class Funcionario(Cadastro):
    def __init__(self, nome: str, endereco: str, email: str, telefone: str, cpf: str):
        super().__init__(nome, endereco, email, telefone, cpf)

class Venda:
    def __init__(self, item_vendido: Produto, vendedor: Funcionario,
                 comprador: Cliente, quantia: int, data: datetime.now()):
        self.item_vendido = item_vendido
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantia = quantia
        self.data = data
