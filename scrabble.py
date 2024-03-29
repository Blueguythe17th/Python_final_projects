import random


class Scrabble_Game:
    def __init__(self):
        self.board = [[' ' for i in range(15)] for i in range(15)]
        self.players = ["player 1", "player 2"]
        self.current_player = random.choice(self.players)
        self.bag = self.create_tile_bag()
        self.tiles = {"player 1":self.draw_tiles(7), "player 2":self.draw_tiles(7)}
        self.scores = {"player 1":0, "player 2":0}
        self.skipped_turns = 0
    def create_tile_bag(self):
        letter_count = {'E':12, 'A':9, 'I':9, 'O':8, 'N':6, 'R':6, 'T':6, 'L': 4, 'S': 4, 'U': 4, 'D': 4, 'G': 3, 'B': 2, 'C': 2, 'M': 2, 'P': 2, 'F': 2, 'H': 2, 'V': 2, 'W': 2,'Y': 2, 'K': 1, 'J': 1, 'X': 1, 'Q': 1, 'Z': 1}
        tile_bag = []
        for letter,count in letter_count.items():
            for i in range(count):
                tile_bag.append(letter)
        return tile_bag
    def draw_tiles(self, num_tiles):
        tiles = random.sample(self.bag, num_tiles)
        for tile in tiles:
            self.bag.remove(tile)
        return tiles
    def print_board(self):
        for row in self.board:
            print(row)
    def print_scores(self):
        for player,score in self.scores:
            print(player + " has " + score + " points.")
    def validate_word(self, word):
        with open("dictionary.txt") as file:
            dictionary = file.read()
            if word in dictionary:
                return True
            else:
                return False
    def validate_placement(self, word, row, column, direction):
        if row < 0 or column < 0:
            return False
        elif (column + len(word)) > 15 and direction == "H":
            return False
        elif (row + len(word)) > 15 and direction == "V":
            return False
        else:
            tiles = self.tiles[self.current_player].copy()
            i = row
            j = column
            for letter in word:
                print(i, j, letter)
                # print(self.board[i][j] == " ")
                # print(letter in tiles)
                # print(tiles)
                if (self.board[i][j] == " ") and (letter in tiles):
                    tiles.remove(letter)
                elif self.board[i][j] == letter:
                    pass
                else:
                    return False
                if direction == "H":
                    j += 1
                else:
                    i += 1
            self.tiles[self.current_player] = tiles
            return True

    def place_word(self, word, row, column, direction):
        for letter in word:
            self.board[row][column]=letter
            if direction == "V":
                row += 1
            else:
                column += 1
    def calculate_word_score(self, word):
        letter_values = {'Q':10, 'Z':10, 'J':8, 'X':8, 'K':5, 'F':4, 'H':4, 'V':4, 'W':4, 'Y':4, 'B':3, 'C':3, 'M':3, 'P':3, 'D':2, 'G':2, 'A':1, 'E':1, 'I':1, 'L':1, 'N':1, 'O':1, 'R':1, 'S':1, 'T':1, 'U':1}
        score = 0
        for c in word:
            score += letter_values[c]
        return score
    def play_turn(self):
        print(self.current_player + "'s turn.")
        self.print_board()
        print("Your tiles are " + str(self.tiles[self.current_player]))
        word = input("Enter a word to create it (or press return to skip): ")
        if word == "":
            self.skipped_turns += 1
            return
        self.skipped_turns = 0
        word = word.upper()
        row = int(input("Where do you want to put this word? Enter a row: ")) - 1
        column = int(input("Enter a column: ")) - 1
        direction = input("Which direction should the word go? Enter 'H' (Horizontal) or 'V' (Vertical): ").upper()
        while not self.validate_placement(word, row, column, direction):
            print("That placement is invalid.")
            word = input("Please enter a new word: ").upper()
            row = int(input("Enter a row: ")) - 1
            column = int(input("Enter a column: ")) - 1
            direction = input("Enter a direction (H or V): ").upper()
        tiles_to_draw = 7 - len(self.tiles[self.current_player])
        self.tiles[self.current_player].extend(self.draw_tiles(tiles_to_draw))
        if not self.validate_word(word):
            score = 0
            print("That's not a valid scrabble word, so you get 0 points.")
        else:
            score = self.calculate_word_score(word)
            print("Your word gets " + str(score) + " points")
            self.place_word(word, row, column, direction)
        self.scores[self.current_player]+=score
       #  if self.current_player == self.players[0]:
            # self.current_player = self.players[1]
        # else:
            # self.current_player = self.players[0]
        # play = input(self.current_player + ", would you like to keep playing or end the game? Enter 'continue' or 'end': ")
        # if play == "end":
            # self.forfeit = True
        # at the beginning of the turn print the board
        # ask player for word
        # validate that this word is in the dictionary
        # ask the player what the starting position is and the direction they want to put the word in
        # calculate the score of the word
        # draw tiles
    def play_game(self):
        print("Welcome to scrabble!")
        while not self.game_over():
            self.play_turn()
            if self.current_player == self.players[0]:
                self.current_player = self.players[1]
            else:
                self.current_player = self.players[0]
        print("Game over. The final scores are " + str(self.scores["player 1"]) + " for player one and " + str(self.scores["player 2"]) + " for player two.")
        if self.scores["player 1"] < self.scores["player 2"]:
            print("Player 2 wins!")
        else:
            print("Player 1 wins!")
        # say 'welcome to scrabble'
        # have a while loop: while the game isn't over, call self.play_turn
        # after the loop ends, calculate if players still have any tiles
        # game_over will return true or false based on if the bag has any tiles
    def game_over(self):
        if len(self.bag) == 0 and (len(self.tiles["player 1"]) == 0 or len(self.tiles["player 2"]) == 0):
            return True
        elif self.skipped_turns == 6:
            return True
        else:
            return False


scrabble_game = Scrabble_Game()
scrabble_game.play_game()