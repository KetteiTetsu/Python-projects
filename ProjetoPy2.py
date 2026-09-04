#Produto A, 150, 5
#Produto B, 80, 2
#Produto C, 210,35
#Produto D, 120, 3

produtos = []
PESO = 5  # ajuste esse valor conforme necessário


for i in range(4):
    entrada = input(f"Produto {i+1} (nome,vendas,reclamações): ")
    nome, vendas, reclamacoes = entrada.split(",")
    produtos.append({
        "nome": nome.strip(),
        "vendas": int(vendas),
        "reclamacoes": int(reclamacoes),
        "pontuação": int(vendas) - (int(reclamacoes) * PESO)
    })

produtos_ordenados = sorted(produtos, key=lambda p: p["pontuação"], reverse=True)

print("\nRanking de produtos:")
for p in produtos_ordenados:
    print(f"{p['nome']} - vendas: {p['vendas']}, reclamações: {p['reclamacoes']}, pontuação: {p['pontuação']}")
