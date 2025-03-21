import threading
import queue

# Função principal utilizada para calcular MDC (Máximo Divisor Comum)
def calcular_mdc(a, b):
    # Aqui usamos o algoritmo de Euclides para o cálculo
    while b:
        a, b = b, a % b
    return a

# Função que roda a thread
def calcular_pares(fila, resultados):
    # Enquanto a fila não estiver vazia, pega os pares e calcula o MDC
    while not fila.empty():
        try:
            # Tenta pegar um par da fila
            i, num1, num2 = fila.get_nowait()
           
            # Calcula o MDC e armazena o resultado na lista de resultados
            resultados[i] = calcular_mdc(num1, num2)
           
            # Marca a tarefa como concluída
            fila.task_done()
       
        # Se a fila estiver vazia, encerra o while
        except queue.Empty:
            break

# Números para teste (cálculo do MDC)
pares_numeros = [
    (56, 48),
    (18, 12),
    (100, 75),
    (125, 625),
    (1071, 462),
    (80, 32),
    (144, 1024),
    (168, 180),
    (196, 38416),
    (128, 96),
    (315, 735),
    (27993, 39879),
    (4983, 5236),
    (48756, 36936),
    (3968, 8064)
]

# Cria uma fila e adiciona os pares de números nela
fila = queue.Queue()
for i, par in enumerate(pares_numeros):
    fila.put((i, *par))

# Armazena os resultados dos cálculos
resultados = {}

# Lista de threads
threads = []

# Cria e inicia 4 threads para fazer os cálculos em paralelo
for _ in range(4):
    t = threading.Thread(target=calcular_pares, args=(fila, resultados))
    threads.append(t)
    t.start()

# Espera todas as threads finalizarem
for t in threads:
    t.join()

# Exibe os resultados dos cálculos
for i, (num1, num2) in enumerate(pares_numeros):
    print(f"MDC({num1}, {num2}) = {resultados[i]}")

# Acabou ;)👌👍
print("\nCálculos finalizados!")
