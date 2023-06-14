import pytest

from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def set_size():
    browser.config.window_width = 360
    browser.config.window_height = 740

    
def test_success_search(set_size):  # Check result of search
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_unsuccess_results(set_window_size):  # Check message "unsuccess search"
    browser.open('https://google.com')
    textUnsuccess = 'янапотаповазвездаророолоролоролоролорлорлорлорлололлор'
    browser.element('[name="q"]').should(be.blank).type(textUnsuccess).press_enter()
    browser.element('.card-section').should(have.text(' ничего не найдено'))
    print('Result was not found')
