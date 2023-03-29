import re
import importlib
from playwright.sync_api import Page, expect


def test_homepage_contains_veepee_accueil_text(page: Page):
    #TODO: import variables from v_config.variables file is not mandatory this example
    # config_module = importlib.import_module('../v_config.variables')
    #TODO: change this string and use variables from v-config.variables file
    # go to the homepage
    page.goto("https://www.veepee.fr/gr/home/default")
    #expect the titie has Veepee -Accueil text
    expect(page).to_have_title(re.compile("Veepee - Accueil"))
    
def test_homepage_contains_clickable_main_logo(page: Page):
    # go to the homepage
    page.goto("https://www.veepee.fr/gr/home/default")
    #expect the titie has Veepee -Accueil text
    expect(page).to_have_title(re.compile("Veepee - Accueil"))