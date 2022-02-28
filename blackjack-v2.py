# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 15:05:35 2021

@author: pvval
"""

# definição da carteira com métoso de adicionar e subtrair carteira
import random

#Classe Pessoa define característica de jogador ou dealer
# ter método para adicionar ou subtrair da carteira
# definir e controlar carteiras
# armazenar a mao
# Método para cada decisão

class Pessoa(object):
    def __init__(self,dinheiro, aposta, mao):
        self.dinheiro = dinheiro
        self.aposta = aposta
        self.mao = mao
        
    # Método de subtrair carteira
    def subtrair(self,subtraendo):
        self.subtraendo=subtraendo
        self.dinheiro = self.dinheiro - self.subtraendo
        return self.dinheiro

    # Método de adicionar carteira
    def adicionar(self,parcela):
        self.parcela=parcela
        self.dinheiro = self.dinheiro + self.parcela
        return self.dinheiro

    # Método para apagar dados antes de reiniciar jogo
    def __del__(self):
        print("Tchau!")

   	# Método para ler tamanho da mao
    def __len__(self):
        return self.mao



jogador = Pessoa(dinheiro=100, aposta=0, mao=[0,0,0,0,0,0,0,0,0,0,0,0])
dealer = Pessoa(dinheiro=10000, aposta=0, mao=[0,0,0,0,0,0,0,0,0,0,0,0])

# Classe Baralho
# ter método para embaralhar
# armazenar e controlar baralhos
# atributo iniciado deve ser começado com False e pilha_de_cartas com baralho sem embaralhar

class Baralho(object):

    def __init__(self,iniciado, pilha_de_cartas):
        self.iniciado = iniciado
        self.pilha_de_cartas = pilha_de_cartas
  
    def embaralhando(self):
#        print (self.pilha_de_cartas)
        random.shuffle(self.pilha_de_cartas)
        self.iniciado=True
#        print (self.pilha_de_cartas)

# Executando programa

inicia_baralho = [11, 2 ,3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11, 2 ,3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11, 2 ,3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11 ,2 ,3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
        
baralho_dealer = Baralho (iniciado=False, pilha_de_cartas=inicia_baralho)

quero_jogar=True

repetir_pergunta=True

while quero_jogar==True:
    

    while repetir_pergunta==True:

        if jogador.dinheiro<0:
            print ("Vc quebrou! O jogo acabou")
            quero_jogar==False
            break        

        print ("Caro jogador, você possui ", jogador.dinheiro, "créditos! O jogo se encerra quando você não mais desejar jogar, quando seus créditos se encerrarem ou quando você quebrar a banca.")

        print ("Você deseja jogar uma partida de blackjack (S/s ou N/n)?")
    
        resp_digitado = input()
    
        if resp_digitado !="N" and resp_digitado !="n" and resp_digitado !="S" and resp_digitado !="s":

            #repete próximo loop
            print ("Você digitou uma opção inválida. Responda novamente!")
            repetir_pergunta = True
            continue
            
        elif resp_digitado =="N" or resp_digitado =="n":
        
            quero_jogar=False
            repetir_pergunta = False
            break
        else:
            baralho_dealer.embaralhando ()
            quero_jogar = True
            repetir_pergunta = False
            print("O baralho foi embaralhado!")
            break
            
    if quero_jogar == False:
        print("Fim da partida!")
        break #saída

    else:     
        #não repetir pergunta e ir para jogo
        
        # dar cartas

        jogador.mao[0]=baralho_dealer.pilha_de_cartas[0]
        dealer.mao[0]=baralho_dealer.pilha_de_cartas[1]
        jogador.mao[1]=baralho_dealer.pilha_de_cartas[2]
        dealer.mao[1]=baralho_dealer.pilha_de_cartas[3]

        soma_dealer = dealer.mao[0]+dealer.mao[1]
        # perguntar aposta
        
        repetir_pergunta3=True
        
        while repetir_pergunta3 == True:
               


            print("Digite sua aposta:")
        
            jogador.aposta = float (input())
        
            if jogador.aposta >0 and jogador.aposta <=jogador.dinheiro:
                repetir_pergunta3= False
                break
            else:
                print("Saldo solicitado incorreto incorreto! Aposta de ve ser maior que 0 até", jogador.dinheiro)
                continue
        
        
        
        # inserir imprimir cartas jogador e primeira carta do dealer_

        print ("Sua mão é: ", jogador.mao[0], " e ", jogador.mao[1], ".")
        print ("Primeira carta dealer: ", dealer.mao[0])
        
        
        repetir_pergunta2=True

        # repetir jogadas e aplicar lógica

        contador3=2
        ficar=2
        while repetir_pergunta2==True:

            # iniciar processo de decisão
            # projeto não pede essas regras: Abrir,Dobrar ou Desistir.
            print('Digite o número 1 para Ficar, 2 para Pedir e 3 para Desistir:')

            opcao = int(input())
                
            if opcao != 1 and opcao != 2 and opcao!=3:
                #repete próximo loop
                print ("Você digitou uma opção inválida. Responda novamente!")
                repetir_pergunta2 = True
                continue


                

        # imprimir resultados e atualização da carteira

       

            elif opcao ==1:
            
                contador = 0
                soma_dealer=0
                soma_dealer = dealer.mao[0]+dealer.mao[1]
                soma_jogador=0
                #ficar=1
                #ficar +=1
            
                while contador < ficar:

                    soma_jogador += jogador.mao[contador]
                    contador += 1
            
                    if soma_jogador > 21:
                
                        contador2 = 0
                
                        while contador2 < ficar:
                            if jogador.mao[contador2] == 11:
                                jogador.mao[contador2]=1
                                contador2+=1
                                break
                            else : continue
           
                if soma_jogador>21:
                    
                    
                    print ("Vc perdeu sua aposta!")
                    jogador.dinheiro = jogador.dinheiro-jogador.aposta

                    jogador.aposta=0
                    jogador.mao=[0,0,0,0,0,0,0,0,0,0,0,0]
                    jogador.aposta=0
                    dealer.mao=[0,0,0,0,0,0,0,0,0,0,0,0]
                    dealer.aposta=0
                    contador=0
                    contador2=0
                    contador3=2
                    repetir_pergunta=True
                    repetir_pergunta2=False
                    repetir_pergunta3=True                
                    del(resp_digitado)
                    del(opcao)
                
                    break


                elif soma_jogador==soma_dealer:
                    print ("Empate! Dinheiro devolvido!")
                    jogador.aposta=0
                    jogador.mao=[0,0,0,0,0,0,0,0,0,0,0,0]
                    jogador.aposta=0
                    dealer.mao=[0,0,0,0,0,0,0,0,0,0,0,0]
                    dealer.aposta=0
                    contador=0
                    contador2=0
                    contador3=2
                    repetir_pergunta=True
                    repetir_pergunta2=False
                    repetir_pergunta3=True
                    del(resp_digitado)
                    del(opcao)
                    break #continue loop principal
                
                elif soma_jogador > soma_dealer:
                    print ("Parabéns vc ganhou!")
                    jogador.dinheiro = jogador.dinheiro+jogador.aposta
                    print ("Seu novo saldo para apostas é de: ", jogador.dinheiro)
                                # zerar todas as variáveis
                    jogador.aposta=0
                    jogador.mao=[0,0,0,0,0,0,0,0,0,0,0,0]
                    jogador.aposta=0
                    dealer.mao=[0,0,0,0,0,0,0,0,0,0,0,0]
                    dealer.aposta=0
                    contador=0
                    contador2=0
                    contador3=2
                    repetir_pergunta=True
                    repetir_pergunta2=False
                    repetir_pergunta3=True
                    del(resp_digitado)
                    del(opcao)
               
                    break
            
                else:
                    print ("Vc perdeu sua aposta!")
                    jogador.dinheiro = jogador.dinheiro-jogador.aposta

                    jogador.aposta=0
                    jogador.mao=[0,0,0,0,0,0,0,0,0,0,0,0]
                    jogador.aposta=0
                    dealer.mao=[0,0,0,0,0,0,0,0,0,0,0,0]
                    dealer.aposta=0
                    contador=0
                    contador2=0
                    contador3=2
                    repetir_pergunta=True
                    repetir_pergunta2=False
                    repetir_pergunta3=True                
                    del(resp_digitado)
                    del(opcao)
                
                    break

 
            
            elif opcao == 2:
            

                ficar+=1        
                jogador.mao[contador3]=  baralho_dealer.pilha_de_cartas[contador3+2]
            
            
            
                print ("Sua nova mão é: ", jogador.mao)
            
                repetir_pergunta2=True
                contador3+=1
                continue

            else:
                print ("Vc desistiu!")
                jogador.dinheiro = jogador.dinheiro-(jogador.aposta/2)

                jogador.aposta=0
                jogador.mao=[0,0,0,0,0,0,0,0,0,0,0,0]
                jogador.aposta=0
                dealer.mao=[0,0,0,0,0,0,0,0,0,0,0,0]
                dealer.aposta=0
                contador=0
                contador2=0
                contador3=2
                repetir_pergunta=True
                repetir_pergunta2=False
                repetir_pergunta3=True                
                del(resp_digitado)
                del(opcao)
                
                break
                
            
            
        continue    
            
        
        

        # jogar novamente até acabar carteira ou do jogador ou do dealer_
