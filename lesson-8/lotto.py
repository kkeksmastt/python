import random


class LottoCard:
    def __init__(self, player):
        self.player = player
        self.card = []
        self.create()

    def create(self):
        while len(self.card) < 27:
            line = []
            while len(line) < 5:
                b = random.randrange(1, 90)
                if b in line or b in self.card:
                    continue
                else:
                    line.append(b)
            line.sort()
            while len(line) < 9:
                ind = random.randrange(0, 9)
                line.insert(ind, '-')
            for i in line:
                self.card.append(i)
        self.card.insert(9, '\n')
        self.card.insert(19, '\n')


class LottoGame:
    def __init__(self, p1, p2):
        self.p1 = p1.player
        self.p1_card = p1.card
        self.p2 = p2.player
        self.p2_card = p2.card

    def start(self):
        bars = []
        while True:
            p_card = '\n' + 'Игрок' + '\n' + ' ' + ' '.join(str(x) for x in self.p1_card) + '\n' + ' --' * 9 + '\n'
            c_card = '\n' + 'Компьютер' + '\n' + ' ' + ' '.join(str(x) for x in self.p2_card) \
                     + '\n' + ' --' * 9 + '\n'
            print(c_card)
            counter_p = 0
            while True:
                bar = random.randrange(1, 90)
                if bar not in bars:
                    break
            bars.append(bar)
            rem_bar = 90 - len(bars)
            print(p_card)
            print(f'Боченок № {bar}\n')
            txt = input(f'Хотите зачеркнуть число? y or n. Боченков осталось: {rem_bar}\n')
            if txt == 'y':
                if bar in self.p1_card:
                    ind = self.p1_card.index(bar)
                    self.p1_card[ind] = '-'
                    counter_p += 1
                else:
                    print('Победа компьютера!')
                    break
            elif txt == 'n':
                if bar in self.p1_card:
                    print('Победа компьютера!')
                    break
            if counter_p == 15:
                print('Вы победили!')
                break
            counter_c = 0
            if bar in self.p2_card:
                ind = self.p2_card.index(bar)
                self.p2_card[ind] = '-'
                counter_c += 1
            if counter_c == 15:
                print('Победа компьютера!')
                break


player_human = LottoCard('Игрок')
player_computer = LottoCard('компьютер')
h = LottoGame(player_human, player_computer)
h.start()
