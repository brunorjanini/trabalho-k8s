import requests
import time

URL = "http://20.69.18.162:8000/process"   # endereço da sua VM

NUM_REQUESTS = 5
INTERVAL = 2  # segundos entre cada requisição

tempos = []

for i in range(NUM_REQUESTS):
    print(f"\n=== Requisição {i+1} ===")
    inicio = time.time()

    r = requests.get(URL, timeout=30)
    fim = time.time()

    total = fim - inicio
    tempos.append(total)

    print("Status:", r.status_code)
    print("Tempo de processamento interno:", r.json().get("processing_time"))
    print("Tempo total:", total)

    time.sleep(INTERVAL)

media = sum(tempos) / len(tempos)
print("\n==============================")
print(f"Média do tempo total: {media:.4f} segundos")
print("==============================")
