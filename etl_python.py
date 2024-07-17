from csv import reader
from collections import defaultdict
import time

from pathlib import Path

path_do_txt = "data\measurements.txt"

def processar_temperaturas(path_do_txt: Path):
    print("Iniciando o processamento do arquivo.")

    start_time = time.time() # Tempo de início

    temperatura_por_station = defaultdict(list)

    with open(path_do_txt, 'r', encoding="utf-8") as file:
        _reader = reader(file, delimiter=';')
        for row in _reader:
            nome_da_station, temperatura = str(row[0]), float(row[1])
            temperatura_por_station[nome_da_station].append(temperatura)
    
    print("Dados carregados. Calculando estatísticas...")

    # Dicionário para armazenar os resultados calculados
    results = {}

    for station, temperatures in temperatura_por_station.items():
        min_temp = min(temperatures)
        mean_temp = sum(temperatures) / len(temperatures)
        max_temp = max(temperatures)
        results[station] = (min_temp, mean_temp, max_temp)

    print("Estatísticas calculada. Ordenando...")
    # Ordenando os resultados pelo nome da estação
    sorted_results = dict(sorted(results.items()))

    end_time = time.time() # Tempo de término
    print(f"Processamento concluído em {end_time - start_time:.2f} segundos.")

    return sorted_results

dados_processados = processar_temperaturas(path_do_txt)

print(dados_processados)