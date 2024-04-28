from Actions.men_category_actions import click_add_to_cart, click_men_dropdown, click_men_item

from Locators.men_category_locators import men_dropdown, men_item, add_to_cart, add_to_cart_color_error, \
    add_to_cart_size_error

expected_error_message = "This is a required field."


# Function to run the test case
def open_men_products_and_add_to_cart():
    click_men_dropdown()
    click_men_item()
    click_add_to_cart()
    color_error_message = add_to_cart_color_error()
    size_error_message = add_to_cart_size_error()
    assert expected_error_message in color_error_message and expected_error_message in size_error_message
