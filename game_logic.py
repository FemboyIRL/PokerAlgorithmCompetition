from random import shuffle

class Card:
    def __init__(self, value, rank, suit):
        self.value = value
        self.rank = rank
        self.suit = suit
        self.fullname = f"{rank} of {suit}"

    def __str__(self):
        return self.fullname 

class Player:
    def __init__(self, name, balance, algorithm):
        self.name = name
        self.balance = balance  
        self.algorithm = algorithm

    def make_decision(self, game_state):
        return self.algorithm.make_decision(game_state)

class GameState:
    def __init__(self, players, deck, community_cards, current_bet, pot, round_number):
        self.players = players  # Lista de jugadores
        self.deck = deck  # Baraja de cartas
        self.community_cards = community_cards  # Cartas comunitarias
        self.current_bet = current_bet  # Apuesta actual
        self.pot = pot  # Dinero acumulado en el bote
        self.round_number = round_number  # Número de ronda (pre-flop, flop, turn, river)


def create_deck():
    # Creamos la baraja vacia
    deck = []

    # Palos de las cartas
    suits = ("Heart", "Diamond", "Club", "Spade")

    # Rangos de las cartas
    ranks = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King")

    # Rellenamos la baraja de cartas
    for suit in suits:
        for i, rank in enumerate(ranks):
            deck.append(Card(i+2, rank, suit))
    
    for card in deck:
        print(card)

    return deck


# Función para inicializar el estado del juego
def initialize_game_state(players):

    deck = create_deck()

    shuffle(deck)  # Barajar las cartas
    
    # Inicializamos el estado del juego
    return GameState(players, deck, [], 0, 0, 0)

class PokerEngine:
    def __init__(self):
        self.game_state = None
        self.players = []
        self.current_player_index = 0

    def start_game(self, players):
        self.players = players
        self.game_state = initialize_game_state(players)
    
    def run_round(self):
        for player in self.players:
            decision = player.make_decision(self.game_state)
            self.handle_decision(player, decision)

    def handle_decision(self, player, decision):
        if decision == 'fold':
            print(f"{player.name} folds.")
        elif decision == 'call':
            print(f"{player.name} calls.")
        elif decision == 'raise':
            print(f"{player.name} raises.")

    def resolve_winner(self):
        
        return self.players[0]  # El primer jugador como ganador, se debe agregar lógica real

