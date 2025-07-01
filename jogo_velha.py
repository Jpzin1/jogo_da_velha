import tkinter as tk
from tkinter import font
from functools import partial

# --- LÓGICA DA IA (MINIMAX) ---
JOGADOR_HUMANO = 'X'
JOGADOR_IA = 'O'

def verificar_vitoria(tab, jogador):
    vitorias = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in vitorias:
        if tab[combo[0]] == tab[combo[1]] == tab[combo[2]] == jogador:
            return combo
    return None

def verificar_empate(tab):
    return ' ' not in tab

def minimax(tab, profundidade, is_maximizador):
    vitoria_ia = verificar_vitoria(tab, JOGADOR_IA)
    if vitoria_ia: return 10
    vitoria_humano = verificar_vitoria(tab, JOGADOR_HUMANO)
    if vitoria_humano: return -10
    if verificar_empate(tab): return 0
    if is_maximizador:
        melhor_placar = -float('inf')
        for i in range(9):
            if tab[i] == ' ':
                tab[i] = JOGADOR_IA
                placar = minimax(tab, profundidade + 1, False)
                tab[i] = ' '
                melhor_placar = max(melhor_placar, placar)
        return melhor_placar
    else:
        melhor_placar = float('inf')
        for i in range(9):
            if tab[i] == ' ':
                tab[i] = JOGADOR_HUMANO
                placar = minimax(tab, profundidade + 1, True)
                tab[i] = ' '
                melhor_placar = min(melhor_placar, placar)
        return melhor_placar

def encontrar_melhor_jogada(tab):
    melhor_placar = -float('inf')
    melhor_jogada = -1
    for i in range(9):
        if tab[i] == ' ':
            tab[i] = JOGADOR_IA
            placar = minimax(tab, 0, False)
            tab[i] = ' '
            if placar > melhor_placar:
                melhor_placar = placar
                melhor_jogada = i
    return melhor_jogada

# --- CLASSE DA INTERFACE GRÁFICA (GUI) ---

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da veia")
        self.root.resizable(False, False)
        
        # Constante para o tamanho de cada célula do jogo
        self.CELL_SIZE = 110
        self.BOARD_SIZE = self.CELL_SIZE * 3

        # Fontes
        self.button_font = font.Font(family='Helvetica', size=36, weight='bold')
        self.status_font = font.Font(family='Helvetica', size=16)

        # Variáveis de estado do jogo
        self.tabuleiro = [' ' for _ in range(9)]
        self.game_over = False
        self.human_turn = True

        # Container principal para empilhar o canvas e os botões
        main_container = tk.Frame(root, width=self.BOARD_SIZE, height=self.BOARD_SIZE)
        main_container.pack(pady=10, padx=10)

        # Canvas para a linha da vitória (fica no fundo)
        self.line_canvas = tk.Canvas(main_container, width=self.BOARD_SIZE, height=self.BOARD_SIZE,
                                     highlightthickness=0)
        self.line_canvas.place(x=0, y=0)
        
        # Frame para os botões (fica por cima do canvas)
        self.board_frame = tk.Frame(main_container, width=self.BOARD_SIZE, height=self.BOARD_SIZE)
        self.board_frame.place(x=0, y=0)

        # Criar os botões do tabuleiro
        self.buttons = []
        for i in range(9):
            row, col = i // 3, i % 3
            button = tk.Button(self.board_frame, text=' ', font=self.button_font,
                               width=3, height=1, relief='groove',
                               command=partial(self.on_button_click, i))
            button.grid(row=row, column=col)
            self.buttons.append(button)
        
        # Armazena a cor original do botão para poder resetar depois
        self.original_button_color = self.buttons[0].cget("background")
        
        self.status_label = tk.Label(root, text="Sua vez de jogar (X)", font=self.status_font, pady=5)
        self.status_label.pack()
        self.restart_button = tk.Button(root, text="Reiniciar Jogo", font=self.status_font, command=self.restart_game)
        self.restart_button.pack(pady=10)

    def on_button_click(self, index):
        if self.tabuleiro[index] == ' ' and not self.game_over and self.human_turn:
            self.human_turn = False
            self.tabuleiro[index] = JOGADOR_HUMANO
            self.buttons[index].config(text=JOGADOR_HUMANO, state='disabled', disabledforeground='blue')
            
            if self.check_game_over(): return
            
            self.status_label.config(text="IA está pensando...")
            self.root.after(500, self.ai_move)

    def ai_move(self):
        if not self.game_over:
            jogada = encontrar_melhor_jogada(self.tabuleiro)
            if jogada != -1:
                self.tabuleiro[jogada] = JOGADOR_IA
                self.buttons[jogada].config(text=JOGADOR_IA, state='disabled', disabledforeground='red')
            
            if not self.check_game_over():
                self.status_label.config(text="Sua vez de jogar (X)")
                self.human_turn = True

    def check_game_over(self):
        vitoria_humano = verificar_vitoria(self.tabuleiro, JOGADOR_HUMANO)
        if vitoria_humano:
            self.end_game("Parabéns! Você venceu!", vitoria_humano, 'blue')
            return True

        vitoria_ia = verificar_vitoria(self.tabuleiro, JOGADOR_IA)
        if vitoria_ia:
            self.end_game("A IA venceu! Tente novamente.", vitoria_ia, 'red')
            return True

        if verificar_empate(self.tabuleiro):
            self.end_game("O jogo empatou!")
            return True
        
        return False

    def end_game(self, message, combo=None, color=None):
        """Função centralizada para terminar o jogo."""
        self.game_over = True
        self.status_label.config(text=message)
        if combo:
            self.draw_winning_line(combo, color)
            self._highlight_winning_cells(combo, color)
        
        for button in self.buttons:
            button.config(state='disabled')
    
    # NOVA FUNÇÃO PARA DESTACAR AS CÉLULAS
    def _highlight_winning_cells(self, combo, color):
        """Muda a cor de fundo das células vencedoras."""
        for index in combo:
            self.buttons[index].config(bg=color)

    def _get_cell_center(self, index):
        """Calcula as coordenadas do centro de uma célula."""
        row, col = index // 3, index % 3
        x = col * self.CELL_SIZE + self.CELL_SIZE // 2
        y = row * self.CELL_SIZE + self.CELL_SIZE // 2
        return x, y

    def draw_winning_line(self, combo, color):
        """Desenha a linha da vitória usando coordenadas calculadas."""
        start_x, start_y = self._get_cell_center(combo[0])
        end_x, end_y = self._get_cell_center(combo[2])
        self.line_canvas.create_line(start_x, start_y, end_x, end_y, width=10, fill=color, capstyle=tk.ROUND)

    def restart_game(self):
        self.game_over = False
        self.human_turn = True
        self.tabuleiro = [' ' for _ in range(9)]
        self.status_label.config(text="Sua vez de jogar (X)")
        self.line_canvas.delete("all")
        for button in self.buttons:
            # Reseta o botão para o estado e cor originais
            button.config(text=' ', state='normal', bg=self.original_button_color)

# --- Execução do Programa ---
if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()