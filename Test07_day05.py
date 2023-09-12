# - 메뉴는 [1]예매하기, [2]종료하기
# - 사용자로부터 좌석번호(index)를 입력받아 예매하는 시스템이다. (좌석은 10개이다.)
# - [V] [V] [V] [  ] [  ] [  ] [  ] [  ] [  ] [  ]
# - 예매가 완료되면 해당 좌석 값을 1로 변경한다.
# - 이미 예매가 완료된 좌석은 재구매할 수 없다.
# - 한 좌석당 예매 가격은 12000원이다.
# - 프로그램 종료 후, 해당 영화관의 총 매출액을 출력한다.


seats = ["[ ]"] * 10
price = 12000

while True :
    menu_sel = input("[1]예매하기, [2]종료하기 : ")
    if menu_sel.isdigit():
        if menu_sel == '1' :
            print("예매 가능한 좌석")
            for e in seats : print(e,end=" ")
            print()
            seat_sel = int(input("좌석을 선택하세요 : ")) - 1
            if seat_sel <= len(seats) :
                if seats[seat_sel] != "[V]" :
                    seats[seat_sel] = "[V]"
                else : print("이미 선택된 자리입니다.")
            else : print("없는 좌석입니다.")

        elif menu_sel == '2':
            print(f"총 금액 : {seats.count('[V]') * price}원")
            break
        else : print("없는 메뉴입니다 다시 선택하세요.")
    else : print("메뉴에 해당하는 숫자를 입력해주세요.")
