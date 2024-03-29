__all__ = (
    'Subway',
    'SubwaySandwichOrder',
    'Worker',
    'Customer',
)




class Subway:
    """서브웨이 매장"""

    def __init__(self, name, money=None):
        self.__name = name
        self.money = 10000000 if money is None else money
        print('{} 생성'.format(self.name))

    @property
    def name(self):
        return '서브웨이 {}'.format(self.__name)


class Worker:
    """서브웨이 직원"""

    def __init__(self, subway, name):
        self.subway = subway
        self.name = name
        print('{}의 {}직원 생성'.format(
            self.subway.name,
            self.name,
        ))

    @staticmethod
    def notice_price(order):
        """매개변수로 주어진 order의 가격을 알려줌"""
        print('주문하신 샌드위치 {}의 가격은 {}원 입니다'.format(
            # order.SET_DICT[order.is_set],
            order.get_set_text(),
            order.total_price
        ))

    def get_paid(self, order, paid):
        '손님이 낸 돈 받기'
        if order.total_price == paid:
            self.subway.money += paid
            print('샌드위치값으로 {}원을 받았습니다.\n매장의 시재는 {}입니다.'.format(
                paid,
                self.subway.money,
            ))
        elif order.total_price > paid:
            print('돈을 더내주세요')
        else:
            self.subway.money += order.total_price
            print('샌드위치값으로 {}원을 받았습니다.\n매장의 시재는 {}입니다.\n거스름돈은 {}입니다'.format(
                paid,
                self.subway.money,
                paid - order.total_price
            ))


class Customer:
    def __init__(self, number, name):
        self.money = 100000
        self.number = number
        self.name = name


class SubwaySandwichOrder:
    """서브웨이 샌드위치를 주문하는 클래스다"""
    SET_DICT = {
        True: '세트메뉴',
        False: '단품'
    }

    def get_set_text(self):
        """
        자신의 is_set Boolean값에 따라 다른 텍스트를 리턴
        :return: '단품' 또는 '세트메뉴'
        """
        return self.SET_DICT[self.is_set]

    def __init__(self, customer, bread_type, meat, sauce, price, is_set_menu=None):
        '주문시 필수적으로 골라야 하는 것들'
        self.customer = customer
        self.bread_type = bread_type
        self._meat = meat
        self.sauce = sauce
        self.price = price
        self.is_set = is_set_menu
        if is_set_menu is None:
            is_set = input('세트로 하실래요? (y/N):')
            self.is_set = True if is_set.lower() == 'y' else False
        print('빵은 {}, 고기는 {}, 소스는 {}를 선택했습니다. {}이며, 가격은 {}입니다.'.format(
            self.bread_type,
            self._meat,
            self.sauce,
            '{}'.format(self.get_set_text()),
            self.price))

    def choose_set(self, is_set):
        '세트인지 단품인지 결정하기'
        self.is_set = is_set
        print('주문번호 {}번 고객님은 {}를 선택했습니다'.format(
            self.customer.number,
            '{}'.format(self.get_set_text()),
        ))

    def choose_cookie(self, cookie_type):
        '세트일 경우 쿠키 종류 선택하기'
        if self.is_set:
            self.cookie_type = cookie_type
            print('주문번호 {}번 고객님은 {}쿠키를 선택했습니다.'.format(self.customer.number, self.cookie_type))
        else:
            print('단품고객은 쿠키를 선택할 수 없습니다.')

    @property
    def total_price(self):
        """세트메뉴일때와 아닐때의 주문 총액 리턴"""
        return self.price + 1900 if self.is_set else self.price

    @property
    def meat(self):
        return self._meat

    @meat.setter
    def meat(self, new_meat):
        '고기 종류를 변경하기'
        self._meat = new_meat
        available_meat = {
            '미트볼',
            '튜나',
            '에그마요',
        }
        if new_meat in available_meat:
            print('고기 종류를 {}로 변경하였습니다.'.format(self._meat))
        else:
            print('그런 메뉴는 없습니다.')

# class Screen:
#     '''메뉴를 보여주는 UI 화면 구성 '''
#
#     @staticmethod
#     def order_menu():
#         while True:
#             print("\n" * 30)
#             print('------------------------------------------')
#             print('------------- SUBWAY MANAGER -------------')
#             print('--------------- 1. 고객 주문 ---------------')
#             print('1. 고객 프로필 입력')
#             print('2. 메뉴 선택')
#             print('3. 메인메뉴로')
#             print('------------------------------------------')
#             menu = input(':')
#
#             if menu == '1':
#                 pass
#             elif menu == '2':
#                 pass
#             elif menu == '3':
#                 pass
#             else:
#                 pass
#
#     @staticmethod
#     def change_order_menu():
#
#     @staticmethod
#     def calculator_menu():
#
#     menu = 0
#
#     @staticmethod
#     def main_menu():
#         while True:
#             print("\n" * 30)
#             print('------------------------------------------')
#             print('------------- SUBWAY MANAGER -------------')
#             print('1. 고객 주문')
#             print('2. 주문 변경')
#             print('3. 계산')
#             print('4. 종료')
#             print('------------------------------------------')
#             menu = input('메뉴를 선택하십시오:')
#
#             if menu == '1':
#                 order_menu()
#             elif menu == '2':
#                 pass
#             elif menu == '3':
#                 pass
#             elif menu == '4':
#                 break
#             else:
#                 pass
#
#             # class Customer(SubwaySandwichOrder):
#             #     customer_money = 10000
#             #
#             #     def __init__(self, bread_type, meat, sauce, price, customer_num, money):
#             #         super().__init__(bread_type, meat, sauce, price)
#             #         '고객번호와 가진 돈을 초기화 속성으로 지정해주기'
#             #         self.customer_num = customer_num
#             #         self.money = money
#             #
#             #     def pay(cls, price):
#             #         '샌드위치값 계산하기'
#             #         cls.customer_money -= price
#             #         print('{}원을 계산하고 {}원이 남았습니다'.format(price, cls.customer_money))
