import pytest

from steps import App


@pytest.fixture
def app(request):
    app = App()
    request.addfinalizer(app.quit)
    return app


def test_add_and_remove_goods_to_cart(app: App):
    main_page, goods_page, cart_page = app.main_page, app.goods_page, app.cart_page

    app.login_as_customer()

    for i in range(3):
        counter_before = main_page.get_cart_counter()
        main_page.back()
        main_page.choose_first_good()
        goods_page.add_good_to_cart()
        goods_page.refresh()
        assert main_page.get_cart_counter() != counter_before

    goods_page.go_to_checkout()

    while not cart_page.is_cart_empty():
        cart_page.del_item_from_cart()

    main_page.open()
    assert main_page.get_cart_counter() == 0
