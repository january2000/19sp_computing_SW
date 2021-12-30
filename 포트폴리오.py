def report1_CT():
    print('컴퓨팅사고로 나만의 문제 해결하기')
    print('')
    print('1)분해:학교에서 집 가는 방법을 퇴근시간(월, 수, 목)과 퇴근시간이 아님(화요일)로 구분')
    print('2)패턴인식:교통수단(지하철,버스 등)별로 하교하는 방법을 구분하여 패턴화함')
    print('3)추상화: 하교하는 방법을 교통수단 선택과 환승으로 구분함')
    print('4)하교하기 알고리즘:')
    print('  1.퇴근시간(월, 수, 목요일)인지 퇴근시간이 아닌지(화요일) 파악하기')
    print('  2.퇴근시간이라면 지하철을 선택하고 퇴근시간이 아니라면 버스를 선택하기')
    print('  3.지하철을 이용할 경우')
    print('    3-1.혜화역에서 4호선을 탄 후 동대문역사문화공원에서 내리기')
    print('    3-2.동대문역사문화공원에서 2호선을 타고 왕십리에서 내리기')
    print('    3-3.왕십리에서 분당선을 타고 서현역에서 내리기')
    print('    3-4.서현역에서 3번 혹은 3-2번 버스를 타고 효자촌 현대, 동아아파트 정류장에서 내리기')
    print('  4.버스를 이용할 경우')
    print('    4-1.명륜3가.성대입구 정류소에서 140번 버스를 탄 후 순천향대학병원에서 내리기')
    print('    4-2.순천향대학병원에서 9401또는 9000번 버스를 탄 경우 우성프라자 정류장에서 내리고 1150번 버스를 탄 경우 임광아파트 후문 정류장에서 내리기')

def report2_flowchat():
    import turtle as t
    t.TurtleScreen._RUNNING = True
    t.bgpic('과제2.png')
    t.hideturtle()
    t.exitonclick()

def report3_student_list():
    student=[]

    x=input('학번은 무엇인가요?: ')
    student .append(x)

    y=input('이름은 무엇인가요?: ')
    student .append(y)

    z=int(input('중간고사 성적은 몇 점인가요?: '))
    student .append(z)

    a=int(input('기말고사 성적은 몇 점인가요?: '))
    student .append(a)

    avg=(student[2]+student[3])/2
    student .append(avg)

    print('student 1 = ', student)

def report4_pass_fail():
    test1=int(input('1차 시험 점수를 입력하세요: '))
    test2=int(input('2차 시험 점수를 입력하세요: '))

    if test1<50 or test2<50:
        print('불합격입니다.')
    elif (test1 + test2)/2<70:
        print('불합격입니다.')
    else:
        print('합격입니다! 축하드립니다!')

def report5_369game():
    print("<<369 게임>>")

    num=int(input("1부터 어디까지 진행할까요?: "))
    for num in  range(1,num+1):
        if num%10==3 or num%10==6 or num%10==9:
            num="짝"
        
        elif num%10==0:
            num="따봉"
        print(num, end= ' ')

def report6_free_function():
    #랜덤으로 이름을 지어주는 디지털 작명소

    def name_creating():
        while True:
            second= ['규','강','근','나','난','담','다','대','두','라','리','민','미','문','비','빈','봄','서','선','성','세','시','소','수','아','의','인','예','윤','연','지','정','종','준','재','진','채','찬','태','한','해','혜']
            third= ['국','건','기','근','나','늬','단','동','담','라','란','린','림','리','민','문','명','빈','숙','순','서','석','선','아','연','영','윤','이','원','애','주','준','진','지','자','정','창','태','희','형','호','팔','혜','혁','현']

            import random
            second_name = random.choice(second)
            third_name =  random.choice(third)
        
            print("부탁하신 이름은 %s %s %s입니다~!"%(family_name, second_name, third_name))
            answer=int(input("마음에 드시나요? 마음에 들지 않으시면 0을, 마음에 든다면 아무 숫자나 눌러주세요.:"))
            if answer == 0:
                 print("죄송합니다. 이름을 다시 지어드리겠습니다.")
                 print(' ')
            elif answer != 0:
                print("감사합니다! 또 이용해주세요")
                break
        
    print("<<김윤지 도사의 작명소>>")
    print(' ')
    print("마음에 드는 이름이 나올 때까지 지어드려요~!!")
    family_name = input("성이 무엇인가요?:")
    print(' ')


    name_creating()

while True:
    num = int(input('\n실행 과제 번호를 입력하세요.(1~6,종료:0)'))
    if num == 0:
        break
    elif num == 1:
        print('\n[과제1 실행]\n')
        report1_CT()
    elif num == 2:
        print('\n[과제2 실행]\n')
        report2_flowchat()
    elif num == 3:
        print('\n[과제3 실행]\n')
        report3_student_list()
    elif num == 4:
        print('\n[과제4 실행]\n')
        report4_pass_fail()
    elif num == 5:
        print('\n[과제5 실행]\n')
        report5_369game()
    elif num == 6:
        print('\n[과제6 실행]\n')
        report6_free_function()
    else:
        print('없는 과제 번호입니다. 다시 입력해주세요.')
    
