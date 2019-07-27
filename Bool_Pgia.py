from random import randint
class BPNumber:
    def __init__(self, number=None):
        self.number=number
        self.bulls=0
        self.pgia=0
    def random(self):
        i = 0
        c_numbers = []
        while i < 4:
            c_num = randint(1, 10)

            while True:
                if c_num in c_numbers:
                    c_num = randint(1, 10)
                else:
                    break
            c_numbers.append(c_num)
            i = i + 1
        return c_numbers


    def check_against(self,another_bp_number):
        for j in range(0, len(another_bp_number)):

            if another_bp_number[j] == self.number[j]:
                self.bulls = self.bulls + 1

            elif another_bp_number[j] in self.number and another_bp_number[j] != self.number[j]:
                 self.pgia +=1
        return self.bulls,self.pgia

class Player:
    def get_next_move(self):
        use_numbers = []
        i = 0
        while i < 4:
            use_num = int(input("enter the number"))
            use_numbers.append(use_num)
            i = i + 1
        #print(f"{use_numbers}")
        return BPNumber(use_numbers)

    def notify_result(self,result):
        print(f"your bool is:{result[0]}, your pgia is:{result[1]}")

    def notify_won(self):
        print("You won!!!")

    def notify_lost(self):
        print("You doesn't won!!!")

    def notify_game_over(self):
        print("game over :(")


def main():

    bPNumber=BPNumber()
    secret = bPNumber.random()
    #print(secret)
    player = Player()
    i=0
    while i<20:
        next_guess = player.get_next_move()
        result = next_guess.check_against(secret)
        #print(f"{result}")
        if result[0] == 4:
            player.notify_won()
            break

        player.notify_result(result)
        i+=1
        if i==20 and result[0]!=4:
            player.notify_lost()
            player.notify_game_over()

main()