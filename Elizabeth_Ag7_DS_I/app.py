imovel = input("Insira o tipo do seu imóvel:")
consumo_mensal = float(input("Qual o consumo mensal de água em metros cúbicos (m3):"))
match imovel: 
    case "comercial":
        print("Tarifa comercial aplicada- consulte o plano corporativo")
    case     "apartamento" if consumo_mensal <10:
        print("Consumo econômico- excelente controle de água!")
    case "apartamento" | "casa" if consumo_mensal == 25:  
        print("Consumo moderado- dentro do padrão residencial")
    case _:
        print("Consumo excessivo- adote medidas de economia e verifique vazamentos")
        
        
        

