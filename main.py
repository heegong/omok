# 오목 구현

# 소스코드
import os
import copy
def cls():
    os.system('cls')

def show_omok(ls):
    cls()
    for i in ls:
        for j in i:
            if j==-1:           # 빈색
                print_que = '\033[38;5;7m'+'□'


            elif j==0:          # 하얀색
                print_que = '\033[38;5;15m'+'■'

            elif j==1:          # 검은색
                print_que = '\033[38;5;237m'+'■'

            elif j==2:          # 선택
                print_que = '\033[38;5;10m'+'■'
            
            print(end=print_que+' ')
        print()





def main():
    x,y = 0,0
    max_range = 10      # 몇칸인지 설정
    omok_ls = [[-1 for __ in range(max_range)] for _ in range(max_range)]
    qu_omok_ls = copy.deepcopy(omok_ls)

    what_my_point = 0

    while True:
        show_omok(qu_omok_ls)
        x_y_st = input('\033[38;5;15m'+'\n\n이동 : ').upper()
        if x_y_st=='W':
            if x!=0:
                x-=1

        elif x_y_st=='A':
            if y!=0:
                y-=1

        elif x_y_st=='S':
            if x!=max_range-1:
                x+=1

        elif x_y_st=='D':
            if y!=max_range-1:
                y+=1
        
        else:
            if what_my_point == 0:
                omok_ls[x][y] = 1
                what_my_point = 1

            else:
                omok_ls[x][y] = 0
                what_my_point = 0


        qu_omok_ls = copy.deepcopy(omok_ls)
        
        qu_omok_ls[x][y] = 2
        


if __name__ == "__main__":
    main()
