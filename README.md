<h1>Calculadora de MDC com Threads</h1>
<br>
<div align="center">
  <a href="#-o-projeto">O Projeto</a> | <a href="#-tecnologias">Tecnologias</a> | <a href="#-como-funciona">Como Funciona</a> | <a href="#-resultado-esperado">Resultado Esperado</a>
</div>
<br>

# 👷🏻‍♂️ O Projeto
Esse é um projeto desenvolvido por mim em conjunto com Gabriel Pádua, para uma atividade de Programação Distribuída e Concorrente. O projeto implementa uma calculadora para encontrar o MDC (Máximo Divisor Comum) de diversos pares de números utilizando múltiplas threads para otimizar o processamento.

O algoritmo utiliza o Método de Euclides para o cálculo do MDC e o módulo `threading` do Python para paralelizar o processamento, garantindo eficiência em listas grandes de números.

# 🚀 Tecnologias
Estas são as tecnologias utilizadas no desenvolvimento do projeto:
- Python
- Módulo `threading`
- Módulo `queue`

# 📊 Como funciona
O projeto segue a seguinte lógica:
- Cria uma fila com pares de números para cálculo do MDC.
- Usa 4 threads para processar os cálculos em paralelo.
- Os resultados são armazenados em um dicionário e exibidos ao final.

# 📊 Resultado esperado
```bash
MDC(56, 48) = 8
MDC(18, 12) = 6
MDC(100, 75) = 25
MDC(125, 625) = 125
MDC(1071, 462) = 21
MDC(80, 32) = 16
MDC(144, 1024) = 16
MDC(168, 180) = 12
MDC(196, 38416) = 196
MDC(128, 96) = 32
MDC(315, 735) = 105
MDC(27993, 39879) = 21
MDC(4983, 5236) = 11
MDC(48756, 36936) = 12
MDC(3968, 8064) = 128

Cálculos finalizados!
```

________________________________________________________________________________________________________________________________________________________________________________
<div align="center">
  <p>Desenvolvido com 💙 Pedro Henrique Gomes Chagas e Gabriel Pádua</p> <br>
  <p>☎️ Entre em contato!<p> <br>
  <a display="flex" text-align="center" href="https://www.linkedin.com/in/pedrogchagas/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a> 
</div>
