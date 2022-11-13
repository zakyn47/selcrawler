from selenium.webdriver.common.by import By


class Locators(object):

    BODY = (By.XPATH, "/html/body/*")


class AlzaLocators(object):
    """A class for Alza.cz locators."""


    # Alza home page locators
    SEARCH_FIELD = (By.ID, "edtSearch")
    SEARCH_BUTTON = (By.ID, "btnSearch")
    ITEMS = (By.ID, "boxes")

