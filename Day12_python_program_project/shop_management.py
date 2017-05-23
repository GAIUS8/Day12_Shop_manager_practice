from models import *



menu = 0
customer = Customer('1', None)
customer_order = SubwaySandwichOrder(customer, None, None, None, False)


def main_menu():

    while True:
        print("\n" * 30)
        print('------------------------------------------')
        print('------------- SUBWAY MANAGER -------------')
        print('1. 고객 주문')
        print('2. 주문 변경')
        print('3. 계산')
        print('4. 종료')
        print('------------------------------------------')
        menu = input('메뉴를 선택하십시오:')

        if menu == '1':
            order_menu()
        elif menu == '2':
            change_order_menu()
        elif menu == '3':
            calculator_menu()
        elif menu == '4':
            exit()
        else:
            pass

def order_menu():
    while True:
        print('------------------------------------------')
        print('------------- SUBWAY MANAGER -------------')
        print('--------------- 1. 고객 주문 ---------------')
        print('1. 고객 프로필 입력')
        print('2. 메뉴 선택')
        print('3. 메인메뉴로')
        print('------------------------------------------')
        menu = input(':')

        if menu == '1':
            global customer
            global customer_order
            customer_number = input('고객번호를 입력하여 주십시오.(정수):')
            customer_name = input('고객 이름을 입력하여 주십시오.:')
            customer = Customer(customer_number, customer_name)
            if customer == None:
                print('고객정보 입력에 오류가 발생했습니다')
            else:
                print('고객 정보가 입력되었습니다')
        elif menu == '2':
            print('위 고객의 메뉴를 선택합니다.')

            bread_list = list(bread_dict.keys())
            print('빵을 골라주세요 \n 1. {} \n 2. {} \n 3. {} \n'.format(
                bread_list[0], bread_list[1], bread_list[2]))
            choiced_bread = bread_list[int(input())-1]

            topping_list = list(topping_dict.keys())
            print('토핑을 골라주세요 \n 1. {} \n 2. {} \n 3. {} \n'.format(
                topping_list[0], topping_list[1], topping_list[2]))
            choiced_topping = topping_list[int(input())-1]

            sauce_list = list(sauce_dict.keys())
            print('소스를 골라주세요 \n 1. {} \n 2. {} \n 3. {} \n'.format(
                sauce_list[0], sauce_list[1], sauce_list[2]))
            choiced_sauce = sauce_list[int(input()) - 1]

            print(choiced_sauce)

            total_price = bread_dict[choiced_bread] + topping_dict[choiced_topping] + sauce_dict[choiced_sauce]
            customer_order = SubwaySandwichOrder(customer, choiced_bread, choiced_topping, choiced_sauce, total_price, False)

        elif menu == '3':
            main_menu()
        else:
            print('제대로 누를때까지 안끝납니다아아아아아아')


def change_order_menu():
    global customer_order
    while True:
        print('------------------------------------------')
        print('------------- SUBWAY MANAGER -------------')
        print('--------------- 2. 주문 변경 ---------------')
        print('1. 변경할 주문 선택')
        print('2. 메뉴 재선택')
        print('3. 메인메뉴로')
        print('------------------------------------------')
        menu = input(':')

        if menu == '1':
            print('현재 미구현된 기능 입니다')
        elif menu == '2':
            print('현재는 토핑만 변경 가능합니다.')
            print('변경가능한 토핑: 미트볼, 튜나, 에그마요')
            new_meat = input('위의 토핑 중 하나를 정확히 입력하여 주십시오.')
            customer_order.meat(new_meat)
        elif menu == '3':
            main_menu()
        else:
            pass


def calculator_menu():
    while True:
        print("\n" * 30)
        print('------------------------------------------')
        print('------------- SUBWAY MANAGER -------------')
        print('---------------- 3. 계 산  ----------------')
        print('1. 고객 단위 계산')
        print('2. 주문 단위 계산')
        print('3. 메인메뉴로')
        print('------------------------------------------')
        menu = input(':')

        if menu == '1':
            print('현재 미구현된 기능입니다')
        elif menu == '2':
            print('현재 미구현된 기능입니다')
        elif menu == '3':
            main_menu()
        else:
            pass

bread_dict = {
    '파마산':1200,
    '식빵':2400,
    '바게트빵': 3000,
}

topping_dict = {
    '미트볼':2000,
    '야채샐러드':2200,
    '치킨커리':1800,
}

sauce_dict = {
    '바베큐': 300,
    '스파이시': 200,
    '머스타드':100,
}


subway_sinsa = Subway('신사역점')
worker = Worker(
    subway=subway_sinsa,
    name='박보영'
)
# customer1 = Customer(1, '이한영')
# Customer내부서 해야할 것
# 주문하기(어떤 직원에게)
#   쿠키 선택하기
# 종류 바꾸기(어떤 직원에게, 어떤 Order를)
# order1 = SubwaySandwichOrder(customer1, '파마산', '미트볼', '바베큐', 4000, False)
# order1.choose_set(True)
# order1.choose_set(False)
# order1.choose_cookie('초코칩')
# order1.meat = '튜나'
#
# worker.notice_price(order1)
# worker.get_paid(order1, 8000)
# customer1.pay(4000)
# customer1.meat('튜나')

main_menu()
