from main_page import MainShopPage
from goods_page import PageOfGood
from cart_page import CartPage

MainShopPage.login_as_customer()
for i in range(3):
    MainShopPage.check_counter_before_adding_good()
    MainShopPage.choose_first_good()
    PageOfGood.add_good_to_cart()
    assert MainShopPage.check_counter_before_adding_good != PageOfGood.check_counter_after_adding_good()
PageOfGood.go_to_checkout

while CartPage.cart_not_empty():
    CartPage.del_item_from_cart()
MainShopPage.open_main_page()
MainShopPage.check_cart_is_empty()
