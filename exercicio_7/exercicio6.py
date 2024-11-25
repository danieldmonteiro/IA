#Exercício 7.1.

print("\nLeitura de Arquivo e Operações com Números\n")

def leitura_arquivo():
    import os
    
    try:
        # Solicita o nome do arquivo ao usuário (não são aceitas extensões da Microsoft, só com a importação da biblioteca python-docx)

        nome_arquivo = input("\nDigite o nome do arquivo (com extensão): \n")
        
        # Exibe o diretório atual, usando a biblioteca OS: o arquivo deve estar dentro dele. Caso contrário, deve ser digitado o endereço do mesmo.

        print(f"\nProcurando o arquivo em: {os.getcwd()}\n")

        # Abre o arquivo e lê os números
        
        with open(nome_arquivo, 'r') as arquivo:
            numeros = [int(linha.strip()) for linha in arquivo]
        
        # Calcula os resultados
        soma = sum(numeros)
        media = soma / len(numeros)
        maior = max(numeros)
        menor = min(numeros)

        # Exibe os resultados
        print(f"\nSoma: {soma}\n")
        print(f"\nMédia: {media:.2f}\n")
        print(f"\nMaior número: {maior}\n")
        print(f"\nMenor número: {menor}\n")

    except FileNotFoundError:
        print("\nArquivo não encontrado. Verifique o nome e tente novamente!\n")
    except ValueError:
        print("\nO arquivo contém dados inválidos. Certifique-se de que há apenas números inteiros!\n")
    except ZeroDivisionError:
        print("\nO arquivo está vazio. Não é possível calcular os valores!\n")

leitura_arquivo()

#Exercício 7.2.

print("\nContagem de Palavras em Arquivo de Texto\n")

from collections import Counter
import string

def contar_palavras():
    
    try:

        #Solicita o nome do arquivo
        nome_arquivo = input("\nDigite o nome do arquivo (com extensão): \n")

        #Abre o arquivo
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:

            # Tornar o texto todo minúsculo
            conteudo = arquivo.read().lower()  
            
            # Remover pontuações
            tabela_traducao = str.maketrans("", "", string.punctuation)
            conteudo_sem_pontuacao = conteudo.translate(tabela_traducao)
            
            # Dividir o conteúdo em palavras
            palavras = conteudo_sem_pontuacao.split()
            
            # Limpeza extra: garantir que não haja espaços extras ou caracteres invisíveis
            palavras_limpas = [p.strip() for p in palavras if p.strip()]
            
            # Contar palavras distintas
            palavras_distintas = set(palavras_limpas)
            
            # Contar ocorrências da palavra "texto"
            contador = Counter(palavras_limpas)
            ocorrencias_texto = contador.get("texto", 0)
            
            # Exibir os resultados
            print()
            print(f"Total de palavras: {len(palavras)}")
            print(f"Palavras distintas: {len(palavras_distintas)}")
            print(f"Ocorrências da palavra 'texto': {ocorrencias_texto}")
            print()
    
    except FileNotFoundError:
        print(f"\nErro: o arquivo '{nome_arquivo}' não foi encontrado!\n")
    except Exception as e:
        print(f"\nOcorreu um erro: {e}")

contar_palavras()

#Exercício 7.3.

print("\nProcessamento de Logs de Treinamento de Modelos em AWS\n")

import csv

def analisar_csv():

    try:
        
        #Solicita o nome do arquivo
        nome_arquivo = input("\nDigite o nome do arquivo CSV (com extensão): \n")

        #Inicializa as variáveis para os cálculos
        tempo_total = 0
        soma_precisao = 0
        max_precisao = -float('inf')
        lote_max_precisao = None
        lotes_com_perda = []
        total_lotes = 0

        #Abre o arquivo CSV
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_csv:

            #Detecta o delimitador correto (vírgula ou ponto e vírgula)
            primeira_linha = arquivo_csv.readline()
            delimitador = ',' if ',' in primeira_linha else ';'

            #Volta para o início do arquivo para leitura completa
            arquivo_csv.seek(0)
            leitor = csv.DictReader(arquivo_csv, delimiter=delimitador)

            #Imprimir os nomes das colunas para depuração
            # print(f"Nomes das colunas no arquivo: {leitor.fieldnames}")

            #Itera sobre as linhas do CSV
            for linha in leitor:
                try:
                    
                    #Soma o tempo total
                    tempo_total += float(linha['Tempo(seg)'])  
                    
                    #Soma as precisões
                    soma_precisao += float(linha['Precisão(%)'])  
                    total_lotes += 1

                    #Verifica o lote com maior precisão
                    if float(linha['Precisão(%)']) > max_precisao:
                        max_precisao = float(linha['Precisão(%)'])
                        lote_max_precisao = linha['BatchID']

                    #Verifica os lotes com perda > 0.5
                    if float(linha['Perda']) > 0.5:
                        lotes_com_perda.append(linha['BatchID'])

                except KeyError as e:
                    print(f"\nErro: coluna '{e.args[0]}' não encontrada!\n")
                    return
                except ValueError as e:
                    print(f"\nErro ao processar valor em uma das colunas: {e}\n")
                    return

        #Calcula a precisão média
        precisao_media = soma_precisao / total_lotes if total_lotes > 0 else 0

        #Exibe as informações solicitadas
        print()
        print(f"Tempo total de treinamento: {int(tempo_total)} segundos")
        print(f"Precisão média: {precisao_media:.2f}%")
        print(f"Lote com maior precisão: {lote_max_precisao}")
        # print(f"- Lotes com perda > 0.5: {', '.join(lotes_com_perda) if lotes_com_perda else 'Nenhum'}")
        print(f"Lotes com perda > 0.5: {len(lotes_com_perda)}")
        print()

    except FileNotFoundError:
        print(f"\nErro: o arquivo '{nome_arquivo}' não foi encontrado!\n")
    except Exception as e:
        print(f"\nOcorreu um erro: {e}\n")


analisar_csv()

#Exercício 7.4.

print("\nAnálise de Custo de Serviços AWS a partir de Logs\n")

import csv

def analisar_servicos():

    try:

        #Solicita o nome do arquivo
        nome_arquivo = input("\nDigite o nome do arquivo CSV (com extensão): \n")

        #Inicializa as variáveis para os cálculos
        custo_total = 0
        custo_s3 = 0
        custo_ec2 = 0
        custo_lambda = 0
        servico_maior_custo = None
        maior_custo = -float('inf')
        servicos_unicos = set()  #Conjunto para armazenar serviços únicos

        #Abre o arquivo CSV
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_csv:
            leitor = csv.DictReader(arquivo_csv, delimiter=',')
            
            #Remove espaços extras dos nomes das colunas
            leitor.fieldnames = [nome.strip() for nome in leitor.fieldnames]
            # print(f"\nNomes das colunas no arquivo (ajustados): {leitor.fieldnames}\n")

            #Itera sobre as linhas do CSV
            for linha in leitor:
                try:
                    #Extrai dados da linha
                    nome_servico = linha['Nome do Serviço'].strip()
                    custo = float(linha['Custo'])

                    #Adiciona o nome do serviço ao conjunto
                    servicos_unicos.add(nome_servico)

                    #Atualiza valores globais
                    custo_total += custo

                    #Calcula custos específicos por serviço
                    if nome_servico.lower() == 's3':
                        custo_s3 += custo
                    elif nome_servico.lower() == 'ec2':
                        custo_ec2 += custo
                    elif nome_servico.lower() == 'lambda':
                        custo_lambda += custo

                    #Verifica serviço com maior custo
                    if custo > maior_custo:
                        maior_custo = custo
                        servico_maior_custo = nome_servico

                except KeyError as e:
                    print(f"\nErro: coluna '{e.args[0]}' não encontrada!\n")
                    return
                except ValueError as e:
                    print(f"\nErro ao processar valor em uma das colunas: {e}\n")
                    return

        #Exibe as informações solicitadas
        print()
        print(f"Custo total: {custo_total:.1f}")
        print(f"Custo total do S3: {custo_s3:.1f}")
        print(f"Custo total do EC2: {custo_ec2:.1f}")
        print(f"Custo total do Lambda: {custo_lambda:.1f}")
        print(f"Serviço com maior custo: {servico_maior_custo}")
        print(f"Total de serviços utilizados: {len(servicos_unicos)}")
        print()

    except FileNotFoundError:
        print(f"\nErro: o arquivo '{nome_arquivo}' não foi encontrado!")
    except Exception as e:
        print(f"\nOcorreu um erro: {e}\n")

analisar_servicos()

#Exercício 7.5.

print("\nDetecção de Picos de Consumo em Instâncias EC2\n")

import csv
from collections import defaultdict

def analisar_uso_cpu():
    try:

        #Solicita o nome do arquivo
        nome_arquivo = input("\nDigite o nome do arquivo CSV (com extensão): \n")

        #Dicionário para contar picos de UsoCPU por InstânciaID
        picos_por_instancia = defaultdict(int)
        total_picos_altos = 0
        todas_instancias = set()  #Conjunto para armazenar todas as instâncias únicas

        #Abre o arquivo CSV
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_csv:
            leitor = csv.DictReader(arquivo_csv, delimiter=',')

            #Remove espaços extras dos nomes das colunas
            leitor.fieldnames = [nome.strip() for nome in leitor.fieldnames]
            # print(f"\nNomes das colunas no arquivo (ajustados): {leitor.fieldnames}\n")

            #Itera sobre as linhas do CSV
            for linha in leitor:
                try:
                    #Extrai dados da linha
                    instancia_id = linha['InstânciaID'].strip()
                    uso_cpu = float(linha['UsoCPU(%)'])

                    #Adiciona a instância ao conjunto de todas as instâncias
                    todas_instancias.add(instancia_id)

                    #Verifica se o uso de CPU é maior do que 90%
                    if uso_cpu > 90:
                        total_picos_altos += 1
                        picos_por_instancia[instancia_id] += 1

                except KeyError as e:
                    print(f"\nErro: coluna '{e.args[0]}' não encontrada!\n")
                    return
                except ValueError as e:
                    print(f"\nErro ao processar valor em uma das colunas: {e}\n")
                    return

        #Adicionar instâncias sem picos ao dicionário
        for instancia in todas_instancias:
            if instancia not in picos_por_instancia:
                picos_por_instancia[instancia] = 0

        #Exibe as informações solicitadas
        print()
        print(f"Total de picos de CPU: {total_picos_altos}")
        for instancia, picos in sorted(picos_por_instancia.items()):
            print(f"Picos da instância {instancia}: {picos}")
        print()

    except FileNotFoundError:
        print(f"\nErro: o arquivo '{nome_arquivo}' não foi encontrado!\n")
    except Exception as e:
        print(f"\nOcorreu um erro: {e}\n")

analisar_uso_cpu()

#Exercício 7.6.

print("\nAcompanhamento de Alocações Spot EC2\n")

import csv

def analisar_tempo_vida_instancias():

    try:
         
        #Solicita o nome do arquivo
        nome_arquivo = input("\nDigite o nome do arquivo CSV (com extensão): \n")

        #Dicionários para armazenar dados e cálculos
        tempos_de_vida = {}  #Armazena o tempo de vida de cada InstânciaID
        total_tempo_vida = 0
        quantidade_instancias = 0

        #Abrir o arquivo CSV
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_csv:
            leitor = csv.DictReader(arquivo_csv, delimiter=',')

            #Remover espaços extras dos nomes das colunas
            leitor.fieldnames = [nome.strip() for nome in leitor.fieldnames]
            # print(f"\nNomes das colunas no arquivo (ajustados): {leitor.fieldnames}\n")

            #Iterar sobre as linhas do CSV
            for linha in leitor:
                try:
                    #Extrair dados da linha
                    instancia_id = linha['InstânciaID'].strip()
                    hora_inicial = int(linha['HoraInicial'])
                    hora_final = int(linha['HoraFinal'])

                    #Calcular o tempo de vida
                    tempo_vida = hora_final - hora_inicial

                    #Armazenar os dados
                    tempos_de_vida[instancia_id] = tempo_vida
                    total_tempo_vida += tempo_vida
                    quantidade_instancias += 1

                except KeyError as e:
                    print(f"\nErro: coluna '{e.args[0]}' não encontrada!\n")
                    return
                except ValueError as e:
                    print(f"\nErro ao processar valor em uma das colunas: {e}\n")
                    return

        #Determinar a instância com o maior tempo de vida
        instancia_maior_tempo = max(tempos_de_vida, key=tempos_de_vida.get)
        maior_tempo = tempos_de_vida[instancia_maior_tempo]

        #Calcular o tempo médio de vida
        tempo_medio = total_tempo_vida / quantidade_instancias if quantidade_instancias > 0 else 0

        #Exibir as informações
        print()

        for instancia, tempo in sorted(tempos_de_vida.items()):
            print(f"Tempo de vida da {instancia}: {tempo} horas")

        print(f"Maior tempo de vida: {maior_tempo} horas ({instancia_maior_tempo})")
        print(f"Tempo médio de vida: {tempo_medio:.1f} horas")
        print()

    except FileNotFoundError:
        print(f"\nErro: o arquivo '{nome_arquivo}' não foi encontrado!\n")
    except Exception as e:
        print(f"\nOcorreu um erro: {e}\n")

analisar_tempo_vida_instancias()
