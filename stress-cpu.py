import threading
import time
import multiprocessing

# Função para estressar a CPU
def cpu_stress():
    while True:
        pass  # Loop infinito para ocupar a CPU

# Número de núcleos de CPU para estressar
cpu_cores = multiprocessing.cpu_count()  # Usa todos os núcleos disponíveis
threads = []

# Duração do teste de estresse em segundos
duration = 60

# Criar e iniciar as threads
for _ in range(cpu_cores):
    t = threading.Thread(target=cpu_stress)
    t.start()
    threads.append(t)

print(f"Iniciando teste de estresse da CPU com {cpu_cores} núcleos por {duration} segundos.")
time.sleep(duration)

# Finalizar o teste de estresse
print("Teste de estresse da CPU concluído.")
