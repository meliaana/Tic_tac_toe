from typing import Optional


class Player:
    def __init__(self, name: str, sign: str, turn: bool, _id):
        self.sign = sign
        self.name = name
        self.turn = turn
        self._id = _id
        
    def ask_move(self, valid_moves):
        """ Ask Move Until It's Valid """
        while True:
            move = input(f"{self.name}'s turn: ")
            if not move.isdigit():
                print('Please Enter Digit !')
                continue
            move = int(move)
            if move in valid_moves:
                return move

            print('No no no')
            
      
    def __bool__(self):
        return self.turn

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.__str__()


class Game:
    board = [str(i) for i in range(1, 10)]
    valid_board = [i for i in range(1, 10)]

    
    def __init__(self, p_1: str, p_2: str):
        self.p1 = Player(p_1, 'X', _id=1, turn=True)
        self.p2 = Player(p_2, 'O', _id=2, turn=False)
        self.current_player = self.p1 or self.p2


    def get_board(self):
        """ Get Current State Of Board """
        for order, fig in enumerate(self.board, start=1):
            print(f'| {fig} ', end='')
            if order % 3 == 0:
                print('| ')

    def update_turn(self):
        """ Update's Turn And Current Player """
        self.p1.turn = not self.p1.turn
        self.p2.turn = not self.p2.turn
        self.current_player = self.p1 or self.p2

    def update_board(self, position):
        """ Updates Board And Validation """
        self.board[position-1] = self.current_player.sign
        self.valid_board.remove(position)
        
  

    def run(self) -> Optional[Player]:
        """ Runs Game """
        move_count = 0
        while move_count < 9:
            move = int(self.current_player.ask_move(self.valid_board))
            self.update_board(move)
            self.get_board()
            if self.check_winner():
                return self.current_player                
            self.update_turn()
            move_count += 1
        return None

    def check_winner(self) -> bool:
        """ Check's Winner On Board """
        for i in range(0,7,3):
            if self.board[i] == self.board[i+1] == self.board[i+2]:
                return True 
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6]:
                return True  
        if self.board[0] == self.board[4] == self.board[8]:
           return True  
        if self.board[2] == self.board[4] == self.board[6]:
            return True
        return False

    def play(self):
        """ Play Button """ 
        self.get_board()
        winner: Player = self.run()
        if winner is None:
            print("It's a draw!")
        else:
            print(str(winner), "is the winner")


if __name__ == "__main__":
    game = Game('Misho', 'Ana')
    game.play()