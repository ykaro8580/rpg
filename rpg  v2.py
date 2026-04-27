import os
import random
import copy

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
#Banco de inimigos
#=============================================

fraquezas = {
    "Fogo": "Agua",
    "Terra": "Ar",
    "Ar": "Fogo",
    "Agua": "Terra"
}

inimigos = {
    "Goblin": {
        "nome": "Goblin",
        "elemento": "Terra",
        "vida": 30,
        "dano fisico": 6,
        "dano magico": 0,
        "resistencia": "fisico",
        "tipo_ataque": "fisico"
    },
    "Fada": {
        "nome": "Fada",
        "elemento": "Ar",
        "vida": 20,
        "dano fisico": 0,
        "dano magico": 5,
        "tipo_ataque": "magico",
        "resistencia": "magico"
    },
    "Fantasma": {
        "nome": "Fantasma",
        "elemento": "Agua",
        "vida": 25,
        "dano fisico": 3,
        "dano magico": 7,
        "tipo_ataque": "magico",
        "resistencia": "fisico"
}
}

itens = {
    "Cajado Comum"  : {
        "nome": "Cajado Comum",
        "bonus": {"dano magico": 5},
        "valor": 25
    },
    "Espada Comum"  : {
        "nome": "Espada Comum",
        "bonus": {"dano fisico": 5},
        "valor": 25
    },
    "Cajado de Fogo"  : {
        "nome": "Cajado de Fogo",
        "elemento": "Fogo",
        "bonus": {"dano magico": 10},
        "valor": 50
    }, 
    "Espada Rara"  : {
        "nome": "Espada Rara",
        "bonus": {"dano fisico": 10},
        "valor": 50
    }
}

personagem = {
    "nome": None,
    "vida": 20, 
    "vida max": 20,
    "dano fisico": 5,
    "dano magico": 5,
    "classe": None,
    "fraqueza": None,
    "elemento_base": None,
    "moedas": 100,
}


def criar_inimigo(tipo_ataque):
    return copy.deepcopy(inimigos[tipo_ataque])



def calcular_dano_inimigo(inimigo):
    elementoInimigo = inimigo['elemento']

    if inimigo["tipo_ataque"] == "fisico":
        danoInimigo = inimigo["dano fisico"]
    else:
        danoInimigo = inimigo["dano magico"]
        elementoInimigo = inimigo["elemento"]

    if personagem['fraqueza'] == elementoInimigo:
        print(f"\nO inimigo é super efetivo contra você! Ele tem vantagem por ser do elemento {elementoInimigo}!")
        danoInimigo = danoInimigo * 2
    elif personagem['elemento_base'] == elementoInimigo:
        print(f"\nVocê tem resistencia ao inimigo por ser do elemento {elementoInimigo}!")
        danoInimigo = danoInimigo // 2

    return danoInimigo



def calcular_dano(tipo_ataque, elemento_ataque, inimigo, ataque_fisico):
    if tipo_ataque == "fisico":
        danoBase = personagem["dano fisico"]
        chance_crit = 20


        if ataque_fisico == "Golpe leve":
            danoBase = danoBase * 0.7
            chance_crit = chance_crit * 2
            print("\nVocê usou um golpe leve! Dano reduzido, mas chance de crítico aumentada!")
        elif ataque_fisico == "Golpe normal":
            pass
        elif ataque_fisico == "Golpe pesado":
            danoBase = danoBase * 2
            chance_crit = chance_crit // 2
            print("\nVocê usou um golpe pesado! Dano aumentado, mas chance de crítico reduzida!")
    else:
        danoBase = personagem["dano magico"] 
        chance_crit = 20

    if inimigo["resistencia"] == tipo_ataque:
        print("\nO inimigo é resistente ao seu tipo de ataque!")
        return danoBase // 2
    
    if elemento_ataque == fraquezas.get (inimigo["elemento"]):
        print(f"\nÉ SUPER EFETIVO! O {inimigo['nome']} é fraco contra {elemento_ataque}!")
        danoBase = danoBase * 2

    elif elemento_ataque == inimigo ["elemento"]:
        print (f"\nO inimigo tem resistencia a {elemento_ataque}...")
        danoBase = danoBase // 2
    
    if random.randint(1, 100) <= chance_crit:
        print("\nAtaque crítico!")
        return danoBase * 2
    
    return int(danoBase)
    


def defesa_esquiva(dano):
    while True:
        escolha = input("\nDeseja tentar defender ou esquivar? (1 - defender/2 - esquivar /3 - Abrir menu): ")

        if escolha == "1":
            dano = dano // 2
            print("\nVocê tentou defender! O dano foi reduzido pela metade.")
            return dano

        elif escolha == "2":
            if random.randint(1, 100) <= 30:
                print("\nVocê conseguiu esquivar do ataque!")
                return 0
            else:
                print("\nVocê falhou ao tentar esquivar!")
                return dano

        elif escolha == "3":
            limpar_tela()
            menu()
        else:
            print("Opção inválida, tente novamente.")



def vez_do_jogador(inimigo):
    print("\nÉ sua vez de atacar!")
    ataque_fisico = None 
    while True:
        escolha = input("\nEscolha o tipo de ataque (1 - Físico/2 - Mágico): ").lower()
        if escolha == "1":
            tipo_ataque = "fisico"
            print("\n--- Escolha o Ataque ---")
            print("\n1 - Golpe leve/ 2 - Golpe normal/ 3 - Golpe pesado/")
            op = input("\nSelecione: ")
            if op == "1":
                ataque_fisico = "Golpe leve"
            elif op == "2":
                ataque_fisico = "Golpe normal"
            elif op == "3":
                ataque_fisico = "Golpe pesado"
            else:
                print("Ataque inválido!")
                continue
            elemento_ataque = None
            break
        elif escolha == "2":
            tipo_ataque = "magico"
            print("\n--- Escolha o Elemento ---")
            print("\n1 - Fogo/ 2 - Agua/ 3 - Terra/ 4 - Ar")
            sub_escolha = input("\nSelecione: ")
            if sub_escolha == "1":
                elemento_ataque = "Fogo"
            elif sub_escolha == "2":
                elemento_ataque = "Agua"
            elif sub_escolha == "3":
                elemento_ataque = "Terra"
            elif sub_escolha == "4":
                elemento_ataque = "Ar"
            else:
                print("Elemento inválido!")
                continue
            break
        else:
            print("Opção inválida!")

    input("\nPressione Enter para atacar...")

    dano = calcular_dano(tipo_ataque, elemento_ataque, inimigo, ataque_fisico)
    inimigo["vida"] -= dano
    print("\n================================")
    print(f"Você usou {elemento_ataque if elemento_ataque else 'Ataque Fisico'}")
    print("================================")
    print(f"\nVocê causou {dano} de dano ao inimigo! Vida restante do inimigo: {inimigo['vida']}")



def drop(inimigo): 
    if random.randint(1, 100) <= 50:
        item_key = random.choice(list(itens.keys()))
        item = itens[item_key]

        inventario.append(item["nome"])
        print(f"\nO inimigo dropou um item: {item['nome']}! + 20 moedas!")
        personagem["moedas"] += 20
        for atributo, bonus in item["bonus"].items():
            print(f"{atributo} +{bonus}")
        
        for atributo, bonus in item["bonus"].items():
            if atributo in personagem:
                personagem[atributo] += bonus
                print(f"Seu {atributo} aumentou em {bonus}!")
            else: 
                personagem[atributo] = bonus
    else:
        print("\nO inimigo não dropou nenhum item. + 20 moedas!")
        personagem["moedas"] += 20



def batalha(inimigo): 
    limpar_tela()
    print(f"Um {inimigo ['nome']} apareceu!")
    print("================================")
    print(f"O(a) {inimigo ['nome']} tem resistência a ataques {inimigo['resistencia']}!")
    print(f"O(a) {inimigo ['nome']} tem o tipo de ataque {inimigo['tipo_ataque']}!")
    print(f"O(a) {inimigo ['nome']} tem o elemento {inimigo['elemento']}!")
    print("================================")

    while inimigo["vida"] > 0 and personagem["vida"] > 0: 
        print("\n================================")
        print(f"Vida do(a) {inimigo['nome']}: {inimigo['vida']}")
        print(f"Sua vida: {personagem['vida']}")
        print("================================")

        print(f"\nVez do(a) {inimigo['nome']}")
        dano_inimigo = calcular_dano_inimigo(inimigo)
        dano = defesa_esquiva(dano_inimigo)
        personagem["vida"] -= dano

        print("\n================================")
        print(f"O inimigo causou {dano} de dano em você! Sua vida restante: {personagem['vida']}")
        print("================================")
        input("\nPrecione Enter para continuar: \n")
        limpar_tela()

        if personagem["vida"] <= 0:
            print("Você foi derrotado! Fim de jogo.")
            return

        vez_do_jogador(inimigo)
        input("Precione Enter para continuar: \n")
        limpar_tela()

    if inimigo["vida"] <= 0:
        print(f"Você derrotou o {inimigo['nome']}! Parabéns!")
        drop(inimigo)



def status():
    print("================================")
    print("Status do personagem:")
    print("================================")
    for key, value in personagem.items():
        print(f"{key.capitalize():15}: {value}")



def mostrar_inventario():
    print("================================")
    print("Inventário:")
    print("================================")
    for item in inventario:
        print(f"- {item}")



def menu():
    while True:
        print("================================")
        print("Selecione uma opção:")
        print("================================")
        print("1. Status do personagem")
        print("2. Inventário")
        print("3. Descansar")
        print("4. Voltar ao jogo")
        print("5. Sair")

        escolha = input("\n Escolha uma opção: ")

        if escolha == "1":
            limpar_tela()
            status()
            input("Pressione Enter para continuar...")
            limpar_tela()
        elif escolha == "2":
            limpar_tela()
            mostrar_inventario()
            input("Pressione Enter para continuar...")
            limpar_tela()
        elif escolha == "3":
            limpar_tela()
            print("Descansando...")
            personagem["vida"] = personagem["vida max"]
            print("================================")
            print(f"Vida restaurada para {personagem['vida']}")
            print("================================")
            input("\nPressione Enter para continuar...")
            limpar_tela()
        elif escolha == "4":
            limpar_tela()
            break
        elif escolha == "5":
            print("Saindo do jogo...")
            exit()           
        else:
            print("Opção inválida. Tente novamente.")



def decisoes ():
    while True:
        print("================================")
        print("Escolha uma ação:")
        print("================================")
        print("1. Explorar")
        print("2. abrir o menu")
        print("3. Sair do jogo")

        escolha = input("\nEscolha uma opção: ")
        if escolha == "1":
            limpar_tela()
            evento = random.randint(1, 7)
            if evento == 1 or evento == 3 or evento == 5:
                inimigo = criar_inimigo(random.choice(list(inimigos.keys())))
                batalha(inimigo)
                break
            elif evento == 2 or evento == 4 or evento == 6:
                print("================================")
                print("Você achou um baú!")
                print("================================")
                op = input("\nDeseja abrir? (S/N): ").lower()
                if op == "s":
                        item_key = (random.choice(list(itens.keys())))
                        item = itens[item_key]
                        print("\n================================")
                        print(f"Você achou {item['nome']} + 10 moedas!")
                        personagem["moedas"] += 10
                        inventario.append(item["nome"])
                        for atributo, bonus in item["bonus"].items():
                            if atributo in personagem:
                                personagem[atributo] += bonus
                                print(f"Seu {atributo} aumentou em {bonus}!")
                                print("================================")                         
                            else: 
                                personagem[atributo] = bonus
                            input("\nAperte Enter para continuar: ")
                            limpar_tela()
                            break
                else:
                    print("\nVocê seguiu em frente")
                break
            elif evento == 7:
                print("================================")
                print("Você explorou a área... Encontrou o Mercado!")
                print("================================")
                input("\nAperte Enter para continuar: ")
                limpar_tela()

                itens_loja = random.sample(list(itens.keys()), 2)

                while True:
                    print("================================") 
                    print("Bem-vindo ao Mercado!")
                    print("================================") 
                    print(f"Suas moedas: {personagem['moedas']}")
                    print("\nItens disponíveis:")

                    for nome_item in itens_loja:
                        item = itens[nome_item]
                        print("================================")
                        print(f"{nome_item}")
                        print(f"Valor: {item['valor']} moedas")
                        for atributo, bonus in item["bonus"].items():
                            print(f"{atributo.capitalize()} + {bonus}")
                    print("================================")

                    escolha = input("\nDigite o nome do item, 'sair' ou 'menu': ").lower()

                    if escolha == "sair":
                        break
                    elif escolha == "menu":
                        limpar_tela()
                        menu()
                        continue

                    item_escolhido = None
                    for nome_item in itens_loja:
                        if nome_item.lower() == escolha:
                            item_escolhido = itens[nome_item]
                            break

                    if item_escolhido:
                        if personagem["moedas"] >= item_escolhido["valor"]:
                            personagem["moedas"] -= item_escolhido["valor"]
                            inventario.append(item_escolhido["nome"])

                            print("================================")
                            print(f"Você comprou {item_escolhido['nome']}!")

                            for atributo, bonus in item_escolhido["bonus"].items():
                                personagem[atributo] += bonus
                                print(f"{atributo} +{bonus}")
                            print("================================")
                        else:
                            print("\nMoedas insuficientes!")
                    else:
                        print("\nItem inválido.")
                    input("\nAperte Enter para continuar: ")    
                    limpar_tela()   
                    break
        elif escolha == "2":
            limpar_tela()
            menu()
        elif escolha == "3":
            limpar_tela()
            print("Saindo do jogo...")
            exit()
        else:
            print("Opção inválida. Tente novamente.")



inventario = ["Armadura de couro"]



personagem["nome"] = input("Digite o nome do personagem: ")
while True:
    personagem["classe"] = input("Escolha a classe do personagem (Mago/Guerreiro/Druida): ")
    if personagem["classe"].lower() == "mago":
        personagem["vida max"] = 15
        personagem["vida"] = personagem["vida max"]
        personagem["dano fisico"] = 3
        personagem["dano magico"] = 10
        personagem["elemento_base"] = "Agua"
        personagem["fraqueza"] = "Fogo"
        inventario.append("Cajado do Mago")
        break

    elif personagem["classe"].lower() == "guerreiro":
        personagem["vida max"] = 25
        personagem["vida"] = personagem["vida max"]
        personagem["dano fisico"] = 10
        personagem["dano magico"] = 2
        personagem["elemento_base"] = "Fogo"
        personagem["fraqueza"] = "Agua"
        inventario.append("Espada do Guerreiro")
        break

    elif personagem["classe"].lower() == "druida":
        personagem["vida max"] = 20
        personagem["vida"] = personagem["vida max"]
        personagem["dano fisico"] = 5
        personagem["dano magico"] = 8
        personagem["elemento_base"] = "Terra"
        personagem["fraqueza"] = "Ar"
        inventario.append("Cajado do Druida")
        break
    else:
        limpar_tela()
        print("\nClasse inválida! Escolha entre Mago, Guerreiro ou Druida.\n")



limpar_tela()
print(f"Bem-vindo, {personagem['nome']}! Você escolheu a classe {personagem['classe']}.\n")
input("Pressione Enter para começar...")
limpar_tela()

i = 0
while i < 10:
    print(f"--- Area {i+1} ---")
    decisoes()
    i += 1