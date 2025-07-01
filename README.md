# 🤖 Jogo da Velha com IA Invencível
## Protótipo de um Jogo da Velha com interface gráfica e um oponente de Inteligência Artificial que utiliza o algoritmo Minimax, tornando-o impossível de ser derrotado.

# 📖 Sobre o Projeto
## O objetivo deste projeto é demonstrar a aplicação de um algoritmo clássico de busca adversária em um ambiente de jogo. Foi implementado o jogo da velha, onde o jogador humano (X) enfrenta uma inteligência artificial (O). A IA é capaz de analisar o estado do jogo e tomar a decisão ótima em todas as jogadas, resultando em um empate no melhor dos casos para o jogador humano.

# ✨ Funcionalidades
## Interface gráfica intuitiva: Criada com a biblioteca Tkinter, permitindo uma jogabilidade fácil e visual.

## IA invencível: O oponente é controlado pelo algoritmo Minimax, que garante uma jogada perfeita a cada turno.

## Feedback visual claro: Ao final de uma partida, o sistema desenha uma linha sobre a sequência vencedora e destaca as células correspondentes, indicando claramente o resultado.

## Jogar novamente: Um botão de "Reiniciar Jogo" permite iniciar novas partidas de forma rápida.

# 🧠 Minimax
## O coração deste projeto é a implementação do algoritmo Minimax. Ele funciona sob a premissa de um jogo de dois jogadores com informações perfeitas, onde cada jogador tenta maximizar seu ganho e minimizar sua perda.

## A lógica pode ser resumida em três pontos:

## Árvore de Possibilidades: A IA gera uma árvore com todos os movimentos futuros possíveis a partir do estado atual do tabuleiro.

## Sistema de Pontuação: Cada estado final do jogo (vitória, derrota ou empate) recebe uma pontuação:

## +10: para uma vitória da IA (Maximizador).

## -10: para uma derrota da IA (vitória do Humano, o Minimizador).

## 0: para um empate.

## Recursão e Escolha Ótima: O algoritmo navega recursivamente pela árvore de trás para frente. Ele assume que o oponente (humano) sempre escolherá a jogada que leva ao menor placar para a IA. Sabendo disso, a IA escolhe o caminho que garante o maior placar possível para si mesma, mesmo contra um oponente perfeito.

## Para um jogo com um número limitado de estados como o Jogo da Velha, o Minimax consegue explorar todas as possibilidades, tornando a IA imbatível.

# 📸 Screenshots
## Aqui você pode adicionar imagens do seu jogo em ação!

## Tela Inicial do Jogo:
![Tela Inicial](tela_inicial.png)

## Jogo em Andamento:
![Jogo em Andamento](tela_andamento.png)

## Tela de Vitória (com destaque e linha):
![Tela de Vitória](tela_vitoria.png)

# 🛠️ Tecnologias Utilizadas
## Python 3: Linguagem de programação principal.

## Tkinter: Biblioteca padrão do Python para a criação da interface gráfica (GUI). Não requer instalação adicional.
