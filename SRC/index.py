# Lista de nomes dos heróis e experiência
nomes_heroi = ["Capitão América", "Batman", "Mulher Maravilha", "Superman", "Morte", "Zoro", "Jesus"]
xp_heroi = [950, 1830, 4300, 6350, 7699, 9866, 225590]

# Função para calcular o nível com base na experiência
def calcular_nivel(xp):
# Dicionário que mapeia os intervalos de experiência para os níveis correspondentes
    niveis = {
        "Ferro": {"min": 0, "max": 1000},
        "Bronze": {"min": 1001, "max": 2000},
        "Prata": {"min": 2001, "max": 5000},
        "Ouro": {"min": 5001, "max": 7000},
        "Platina": {"min": 7001, "max": 8000},
        "Ascendente": {"min": 8001, "max": 9000},
        "Imortal": {"min": 9001, "max": 10000},
        "Radiante": {"min": 10001, "max": float('inf')}  # 'inf' representa um valor maior que 10000
    }

# Itera sobre os níveis e verifica em qual intervalo de experiência o valor se encaixa
    for nivel, intervalo in niveis.items():
        if intervalo["min"] <= xp <= intervalo["max"]:
            return nivel  # Retorna o nome do nível encontrado

# Laço de repetição para processar cada herói
for nome, xp in zip(nomes_heroi, xp_heroi):
    nivel = calcular_nivel(xp)
# Calcula o nível do herói com base na experiência
# Imprime o resultado
    print(f"O Herói de nome {nome} está no nível {nivel}")