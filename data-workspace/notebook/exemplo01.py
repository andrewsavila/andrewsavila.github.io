lista_dados = [
    {"membro": "pai", "nome": "André Wanderley de Souza", "idade": 51, "peso": 68},
    {"membro": "mae", "nome": "Cleuza Samai Alves Souza", "idade": 54, "peso": 52},
    {"membro": "filho", "nome": "Augusto Samai de Souza", "idade": 22, "peso": 55},
    {"membro": "filho", "nome": "Álvaro Samai de Souza", "idade": 15, "peso": 45}
]

print("Essa família tem quatro membros")
for item in lista_dados:
    print(f"O {item['membro']} se chama {item['nome']}, tem {item['idade']} anos e pesa {item['peso']} kg")