"""Fichier qui implémente la classe Morpion pour jouer dans le terminal"""

import json
import numpy


def move_hash(move):
    temp = "ABC"
    row, col = move
    return temp[row] + str(col + 1)


class Player:
    "Constante des joueurs"
    O = 1
    X = -1
    NULL = 0


class Morpion:
    "Classe qui encapsule toutes les fonctions du Morpions"

    def __init__(self, load_json: bool = True) -> None:
        self.state = numpy.zeros((3, 3))
        self.player_id = Player.O
        if load_json:
            with open("min_max.json", encoding="utf-8") as move_files:
                self.best_moves = json.load(move_files)
        else:
            self.best_moves = None
        self.state_hash = ""
    
    def __repr__(self) -> str:
        temp = "ABC"
        repr_str = "   1   2   3"
        count1 = 0
        for row in self.state:
            repr_str += "\n"
            repr_str += temp[count1] + " "
            count2 = 0
            for col in row:
                match col:
                    case 0:
                        repr_str += "   "
                    case 1:
                        repr_str += " O "
                    case -1:
                        repr_str += " X "
                    case _:
                        raise ValueError

                if count2 != 2:
                    count2 += 1
                    repr_str += "|"
            if count1 != 2:
                count1 += 1
                repr_str += "\n  -----------"
        return repr_str

    def __call__(self):
        self.play_loop()

    def update_hash(self, move):
        "Update the string that represent the current state"
        row_id, col_id = move
        self.state_hash += "ABC"[row_id] + str(col_id + 1)

    def winning_condition(self):
        "Test si la partie est terminée. Renvoie un couple bool,"
        for i in range(3):
            row, col = self.count_row(i), self.count_col(i)
            if abs(row) == 3 or abs(col) == 3:
                return True, self.player_id
        diag, anti_diag = self.count_diag(1), self.count_diag(-1)
        if abs(diag) == 3 or abs(anti_diag) == 3:
            return True, self.player_id
        for row in self.state:
            for col in row:
                if col == 0:
                    return False, None
        return True, 0

    def count_row(self, row_id):
        "Renvoie la somme de la ligne row_id"
        return self.state[row_id, 0] + self.state[row_id, 1] + self.state[row_id, 2]

    def count_col(self, col):
        "Renvoie la somme de la colone col_id"
        return self.state[0, col] + self.state[1, col] + self.state[2, col]

    def count_diag(self, diag):
        "Renvoie la somme selon la diagonale ou l'antidiagonale"
        match diag:
            case 1:
                return self.state[0, 0] + self.state[1, 1] + self.state[2, 2]
            case -1:
                return self.state[0, 2] + self.state[1, 1] + self.state[2, 0]
            case _:
                raise ValueError

    def valid_play(self, command: str):
        "Vérifie si l'entrée est valide"
        try:
            stripped_input = command.strip().split(" ")
            if len(stripped_input) == 1:
                row, col = stripped_input[0][0], int(stripped_input[0][-1]) - 1
            else:
                row, col = stripped_input[0], int(stripped_input[-1]) - 1
            match row:
                case "A":
                    row = 0
                case "B":
                    row = 1
                case "C":
                    row = 2
                case _:
                    raise ValueError
        except ValueError:
            return False

        if row > 3 or row < 0:
            return False
        if col > 3 or col < 0:
            return False
        if self.state[row, col]:
            return False
        return row, col

    def play_loop(self):
        "Boucle de jeu"

        # Initilisation
        self.state = numpy.zeros((3, 3))
        temp = "ABC"
        # Initilisation des variables 
        win, player = ...

        while not win:
            # Etape 0 : afficher l'état du jeu

            # TODO

            # Etape 1 : demander la commande à l'utilisateur
            command = ... 
            # Etape 1.1 : valider l'entrée 
            valid = ...
            
            # Etape 1.2 : Redemander l'entrée si elle est invalide 
            while not valid:
                command = ...
                valid = ...
            
            # Etape 2 : Mettre à jour notre état de jeu
            row, col = ...
            self.update_hash(...)
            self.state[...] = ...

            # Etape 3 : Vérifier la terminaison du jeu
            win, player = ...

            # Etape 4 : Demander à un autre joeur de jouer
            self.player_id = ...

        # Etape 5 : Terminer le jeu
        if player == Player.NULL:
            ...
        else:
            ...

        # Etape 6 : Rejouer ?
        command = input("Play again ?\n")
        ...

    


if __name__ == "__main__":
    Morpion(load_json=True)()
