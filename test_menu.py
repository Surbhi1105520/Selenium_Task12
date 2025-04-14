import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver


# List of all top menu items
menu_items = [
    "Courses",
    "Login",
    "Sign up",
    "Practice",
    "Resources",
    "LIVE Classes",
    "Our Solutions"
]

@pytest.mark.parametrize("item", menu_items)
def test_menu_structure(driver, item):
    wait = WebDriverWait(driver, 10)
    xpath = f"//*[normalize-space(text())='{item}']"

    try:
        # Wait until element is present in DOM
        element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

        # Scroll into view
        driver.execute_script("arguments[0].scrollIntoView(true);", element)

        # Optional: wait until it's visible on screen
        wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

        assert element.is_displayed(), f"❌ Element not visible: {item}"

        # Parent
        parent = driver.find_element(By.XPATH, f"{xpath}/..")

        # First child of parent
        first_child = driver.find_element(By.XPATH, f"{xpath}/../*[1]")

        # Second following sibling (if it exists)
        try:
            second_sibling = driver.find_element(By.XPATH, f"{xpath}/following-sibling::*[2]")
            second_sibling_tag = second_sibling.tag_name
        except:
            second_sibling_tag = "None"

        # Ancestors, following siblings, preceding elements
        ancestors = driver.find_elements(By.XPATH, f"{xpath}/ancestor::*")
        following_siblings = driver.find_elements(By.XPATH, f"{xpath}/following-sibling::*")
        preceding_elements = driver.find_elements(By.XPATH, f"{xpath}/preceding::*")

        print(f"\n🧩 Menu: {item}")
        print(f"Element Tag: {element.tag_name}")
        print(f"Parent Tag: {parent.tag_name}")
        print(f"First Child of Parent: {first_child.tag_name}")
        print(f"Second Following Sibling: {second_sibling_tag}")
        print(f"Ancestors Count: {len(ancestors)}")
        print(f"Following Siblings Count: {len(following_siblings)}")
        print(f"Preceding Elements Count: {len(preceding_elements)}")

    except Exception as e:
        pytest.fail(f"❌ Failed to interact with '{item}': {str(e)}")
