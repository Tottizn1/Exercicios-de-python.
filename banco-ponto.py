from datetime import datetime

empresa = {
    "nome": "Metalex chapas LTDA",
    "cnpj": "12.345.678/0001-99",
    "endereco": "Rua Vaz de Gusmão, 123 - Vila Velha"
}

jose = {
    "nome": "José Martinez",
    "cpf": "100.200.300-00",
    "data": "",
    "hora": "",
    "matricula": 1
}

carlos = {
    "nome": "Carlos Almeida",
    "cpf": "200.300.400-01",
    "data": "",
    "hora": "",
    "matricula": 2
}

# 1. A função agora apenas se preocupa em IMPRIMIR os dados recebidos
def imprimir_ponto(funcionario):
    # Preenche a data e hora atual no momento da impressão
    agora = datetime.now()
    funcionario["data"] = agora.strftime("%d/%m/%Y")
    funcionario["hora"] = agora.strftime("%H:%M:%S")

    print("-" * 30)
    print("Empresa:", empresa["nome"])
    print("CNPJ:", empresa["cnpj"])
    print("Endereço:", empresa["endereco"])
    print("-" * 30)
    print("Nome:", funcionario["nome"])
    print("CPF:", funcionario["cpf"])
    print("Data:", funcionario["data"])
    print("Hora:", funcionario["hora"])
    print("Matrícula:", funcionario["matricula"])
    print("-" * 30)

# 2. O input e a lógica de decisão ficam no fluxo principal (fora da função)
nome_buscado = input("Digite o nome do funcionário (Jose ou Carlos): ").strip().lower()

# 3. Verificação (usando .lower() para evitar problemas com maiúsculas/minúsculas)
if "josé" in nome_buscado or "jose" in nome_buscado:
    imprimir_ponto(jose)
elif "carlos" in nome_buscado:
    imprimir_ponto(carlos)
else:
    print("Funcionário não encontrado.")
