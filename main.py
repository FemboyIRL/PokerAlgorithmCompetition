from game_logic import PokerEngine, Player
from algorithms.example_algorithm import ExampleAlgorithm  

def main():
    player1 = Player(name='Player 1', balance=1000, algorithm=ExampleAlgorithm())
    player2 = Player(name='Player 2', balance=1000, algorithm=ExampleAlgorithm())
    
    players = [player1, player2]
    
    poker_engine = PokerEngine()
    poker_engine.start_game(players)
    
    round_counter = 0
    while round_counter < 5:  # Simulando 5 rondas
        round_counter += 1
        print(f"Round {round_counter} starts")
        poker_engine.run_round()
    
    winner = poker_engine.resolve_winner()
    print(f"The winner is {winner.name}!")

if __name__ == "__main__":
    main()

