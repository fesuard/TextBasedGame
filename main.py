from game.game_start import GameStart
import traceback


if __name__ == '__main__':
    try:
        game = GameStart()
        game.start_game()

    except Exception as e:
        print("An error has occurred:")
        print(e)
        traceback.print_exc()
        input("Press Enter to exit...") # Prevents console from closing immediately
