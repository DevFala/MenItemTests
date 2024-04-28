from Locators import men_category_locators

add_to_cart_button = men_category_locators.add_to_cart()
men_dropdown_button = men_category_locators.men_dropdown()
men_item_button = men_category_locators.men_item()


def click_add_to_cart():
    add_to_cart_button.click()


def click_men_dropdown():
    men_dropdown_button.click()


def click_men_item():
    men_item_button.click()
