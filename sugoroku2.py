import random
from time import sleep

def main():
    print('これから双六を始めます。')
    print('マスの数を入力してください(20以上,40未満)')
    init = int(input('>>'))
    location1 = 0
    location2 = 0
    if  20 <= init < 40:
        for turn in range(1, 50):
            print( '今は' + str(turn) + 'ターンです。' )
            num_dice = random.randint(1, 12)
            print( 'プレイヤー1のサイコロの目は' + str(num_dice) + 'です')
            location1 += num_dice
            if init - location1 < 0:
                location1 = init - (init-location1)
            else:
                pass
            print('ゴールまであと' + str(abs(init - location1)) + 'マスです。')
            if location1 == init:
                break

            num_dice = random.randint(1, 12)
            print( 'プレイヤー2のサイコロの目は' + str(num_dice) + 'です')
            location2 += num_dice
            if init - location2 < 0:
                location2 = init - (init - location2)
            else:
                pass
            print('ゴールまであと' + str(abs(init - location2)) + 'マスです。')
            if location2 == init:
                break

        print('ゴールです！')
        if location1 == init:
            print('プレイヤー1の勝利です')
        else:
            print('プレイヤー2の勝利です')

    else:
        main()



if __name__ == '__main__':
    main()
