import os
import random
import copy

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
#Banco de inimigos
#=============================================

inimigos = {
    "Goblin": {
        "nome": "Goblin",
        "vida": 30,
        "dano fisico": 6,
        "dano magico": 0,
        "resistencia": "fisico",
        "tipo_ataque": "fisico"
    },
    "Fada": {
        "nome": "Fada",
        "vida": 20,
        "dano fisico": 0,
        "dano magico": 5,
        "tipo_ataque": "magico",
        "resistencia": "magico"
    },
    "Fantasma": {
        "nome": "Fantasma",
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
    },
    "Espada Comum"  : {
        "nome": "Espada Comum",
        "bonus": {"dano fisico": 5}
    },
    "Cajado Raro"  : {
        "nome": "Cajado Raro",  
        "bonus": {"dano magico": 10}
    }, 
    "Espada Rara"  : {
        "nome": "Espada Rara",
        "bonus": {"dano fisico": 10}
    }
}

personagem = {
    "nome": "Nome",
    "vida": 20, 
    "vida_max": 20,
    "dano fisico": 5,
    "dano magico": 5,
    "classe": "Humano"
}
#Função para criar inimigos com base no banco de dados pra evitar que altere as informações originais do dicionario 
#======================================================================================================================

def criar_inimigo(tipo_ataque):
    return copy.deepcopy(inimigos[tipo_ataque])

#Sistema de combate, onde o jogador escolhe o tipo de ataque e o dano é calculado com base no tipo e na resistência do inimigo
#==============================================================================================================================

def calcular_dano(tipo_ataque, inimigo):
    if tipo_ataque == "fisico":
        danoBase = personagem["dano fisico"] #aq ele vai definir o dano do personagem baseado na classe escolhida
        chance_crit = 20 #aq é a porcentagem de chance de acerto crítico, que pode ser ajustada conforme necessário

    else:
        danoBase = personagem["dano magico"] 
        chance_crit = 10

    if random.randint(1, 100) <= chance_crit: #Ele sorteia um número entre 1 e 100, e se for menor ou igual a chance de acerto crítico, o dano é dobrado
        print("\nAtaque crítico!")
        return danoBase * 2
    
    if inimigo["resistencia"] == tipo_ataque: #Se o inimigo tiver resistência ao tipo de dano, o dano é reduzido pela metade
        print("\nO inimigo é resistente ao seu tipo de ataque!")
        return danoBase // 2
    
    return danoBase
    
#Sistema de defesa e esquiva
#======================================

def defesa_esquiva(dano): #O dano entre parenteses é o dano que o inimigo causaria ao jogador, e a função vai calcular se o jogador consegue defender ou esquivar do ataque
    escolha = input("\nDeseja tentar defender ou esquivar? (1 - defender/2 - esquivar): ").lower()

    if escolha == "1":
        dano = dano // 2
        print("\nVocê tentou defender! O dano foi reduzido pela metade.")

    elif escolha == "2":
        if random.randint(1, 100) <= 30: #Gera um número aleatório entre 1 e 100, e se for menor ou igual a 30, o jogador consegue esquivar do ataque
            print("\nVocê conseguiu esquivar do ataque!")
            return 0
        else:
            print("\nVocê falhou ao tentar esquivar!")
        
    return dano

#sistema de ataque do jogador, onde ele escolhe o tipo de ataque e o dano é calculado com base no tipo e na resistência do inimigo
#=====================================================================================================================================

def vez_do_jogador(inimigo): #o inimigo entre parenteses é o inimigo que o jogador está enfrentando, e a função vai permitir que o jogador escolha o tipo de ataque e calcular o dano causado ao inimigo
    print("\nÉ sua vez de atacar!")

    escolha = input("\nEscolha o tipo de ataque (1 - físico/2 - mágico): ").lower() # aq ele define o tipo de ataque 

    if escolha == "1":
        tipo_ataque = "fisico"
    elif escolha == "2":    
        tipo_ataque = "magico"
    else:
        print("Opção inválida!")
        return
    dano = calcular_dano(tipo_ataque, inimigo) # aq ele chama a função calcular_dano para calcular o dano causado ao inimigo com base no tipo de ataque escolhido e na resistência do inimigo
    inimigo["vida"] -= dano # aq ele subtrai o dano calculado da vida do inimigo, e depois imprime o dano causado e a vida restante do inimigo
    print(f"\nVocê causou {dano} de dano ao inimigo! Vida restante do inimigo: {inimigo['vida']}")


    #aq ele define a função drop, que é chamada quando o inimigo é derrotado, e tem uma chance de 50% de dropar um item aleatório do banco de dados de itens
    #============================================================================================================================================================

def drop(inimigo): 
    if random.randint(1, 100) <= 50:
        item_key = random.choice(list(itens.keys()))
        item = itens[item_key]

        inventario.append(item["nome"])
        print(f"\nO inimigo dropou um item: {item['nome']}!")
        for atributo, bonus in item["bonus"].items():
            print(f"{atributo} +{bonus}")
        
        for atributo, bonus in item["bonus"].items():
            if atributo in personagem:
                personagem[atributo] += bonus
                print(f"Seu {atributo} aumentou em {bonus}!")
            else: 
                personagem[atributo] = bonus
    else:
        print("\nO inimigo não dropou nenhum item.")


#Sistema de batalha, onde o jogador e o inimigo se alternam atacando até que um dos dois seja derrotado
#========================================================================================================================


def batalha(inimigo): #o inimigo entre parenteses é o inimigo que o jogador está enfrentando, e a função vai controlar o fluxo da batalha, alternando entre a vez do jogador e a vez do inimigo até que um dos dois seja derrotado
    limpar_tela()
    print(f"Um {inimigo ['nome']} apareceu!")
    print(f"O(a){inimigo ['nome']} tem resistência a ataques {inimigo['resistencia']}!")
    print(f"O(a){inimigo ['nome']} tem o tipo de ataque {inimigo['tipo_ataque']}!")

    while inimigo["vida"] > 0 and personagem["vida"] > 0: #loop pra continuar a batalha enquanto o inimigo e o personagem tiverem vida
        print("\n================================")
        print(f"Vida do(a) {inimigo['nome']}: {inimigo['vida']}")
        print(f"Sua vida: {personagem['vida']}")

        print("================================")
        print(f"\nVez do(a) {inimigo['nome']}")
        if inimigo["tipo_ataque"] == "fisico":
         dano_inimigo = inimigo["dano fisico"]
        else:
            dano_inimigo = inimigo["dano magico"]
        dano = defesa_esquiva(dano_inimigo) #aq ele chama a função defesa_esquiva para calcular o dano que o inimigo causaria ao jogador, e depois subtrai esse dano da vida do jogador
        personagem["vida"] -= dano
        print(f"O inimigo causou {dano} de dano em você! Sua vida restante: {personagem['vida']}")
        input("Precione Enter para continuar: \n")

        if personagem["vida"] <= 0:
            print("Você foi derrotado! Fim de jogo.")
            return

        print("================================")
        print(f"\nVez do(a) {personagem['nome']}")
        vez_do_jogador(inimigo)
        input("Precione Enter para continuar: \n")

    if inimigo["vida"] <= 0:
        print(f"Você derrotou o {inimigo['nome']}! Parabéns!")
        drop(inimigo) #aq ele chama a função drop para verificar se o inimigo dropa um item após ser derrotado


#Função para mostrar o menu do jogo, status do personagem e inventário
#===========================================================================


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
            print("Descansando...")
            personagem["vida"] = personagem["vida_max"]
            input("Pressione Enter para continuar...")
        elif escolha == "4":
            limpar_tela()
            break
        elif escolha == "5":
            print("Saindo do jogo...")
            exit()
            break
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
            # se a pessoa decidir explorar a área, o sistema sortea de 1 ate 3 pra decidir o que vai acontecer, se ele vai lutar, se ele vai achar um bau, ou passar direto
            # se ele achar um bau e decidir abrir, ele sorteia um item com o mesmo sistema de sortear inimigo dentro do dicionario, e adiciona o item no inventario
            evento = random.randint(1, 3)
            if evento == 1:
                inimigo = criar_inimigo(random.choice(list(inimigos.keys()))) #aq ele cria um inimigo aleatório para o jogador enfrentar, escolhendo um tipo de inimigo aleatoriamente do banco de dados de inimigos
                batalha(inimigo)
            elif evento == 2:
                print("Você achou um baú!")
                op = input("Deseja abrir? (S/N): ").lower()
                if op == "s":
                    item_key = (random.choice(list(itens.keys())))
                    item = itens[item_key]
                    print(f"\nVocê achou {item['nome']}!")
                    inventario.append(item["nome"])
                    for atributo, bonus in item["bonus"].items():
                        if atributo in personagem:
                            personagem[atributo] += bonus
                            print(f"Seu {atributo} aumentou em {bonus}!")
                        else: 
                            personagem[atributo] = bonus
                        input("Aperte Enter para continuar: ")
                else:
                    print("Você seguiu em frente")
            elif evento == 3:
                print("Você explorou a área... Porem não encontrou nada!")
                input("Aperte Enter para continuar: ")       
        elif escolha == "2":
            limpar_tela()
            menu()
        elif escolha == "3":
            print("Saindo do jogo...")
            exit()
        else:
            print("Opção inválida. Tente novamente.")

#Aq define o personagem, classe e inventário do jogo
#=============================================

inventario = ["Armadura de couro"]

personagem["nome"] = input("Digite o nome do personagem: ")
personagem["classe"] = input("Escolha a classe do personagem (Mago/Guerreiro/Druida): ")
if personagem["classe"].lower() == "mago":
    personagem["vida_max"] = 15
    personagem["vida"] = personagem["vida_max"]
    personagem["dano fisico"] = 3
    personagem["dano magico"] = 10
    inventario.append("Cajado do Mago")

elif personagem["classe"].lower() == "guerreiro":
    personagem["vida_max"] = 25
    personagem["vida"] = personagem["vida_max"]
    personagem["dano fisico"] = 10
    personagem["dano magico"] = 2
    inventario.append("Espada do Guerreiro")

elif personagem["classe"].lower() == "druida":
    personagem["vida_max"] = 20
    personagem["vida"] = personagem["vida_max"]
    personagem["dano fisico"] = 5
    personagem["dano magico"] = 8
    inventario.append("Cajado do Druida")
else:
    print("Classe inválida. O personagem será criado como Humano.")

#Aq começa o jogo de fato
#=============================================

limpar_tela()
print(f"Bem-vindo, {personagem['nome']}! Você escolheu a classe {personagem['classe']}.\n")
input("Pressione Enter para começar...")
limpar_tela()

print("\nVocê se encontra em uma floresta misteriosa. O que deseja fazer?")
decisoes()

print("\n Você se depara com uma ruina antiga. O que deseja fazer?")
decisoes()

#No modelo q ta aq agr, ficar so adicionando areas e colocando as decisoes ja funciona perfeito