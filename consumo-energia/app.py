# Entrada
aparelho = input("Informe o aparelho que está em uso:")
potencia = float(input("Qual é a potência do aparelho em watts (W):"))
tempo = float(input("Qual o tempo médio de uso diário em horas?"))
# Processamento
consumo_mensal = (potencia * tempo * 30) / 1000
custo_estimado = 0.73 * consumo_mensal 
# Saída
print("Aparelho:", aparelho)
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo_estimado:.2f} por mês")
