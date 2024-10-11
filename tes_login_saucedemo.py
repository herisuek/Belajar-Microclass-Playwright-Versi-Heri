from playwright.sync_api import Page, expect
import pytest

def test_login(page: Page):
    page.goto("https://saucedemo.com") #untuk menaruh tujuan, harus menggunakan https atau http ternyata, kalau "saucedemo.com" saja tidak bisa berjalan botnya

    page.locator('input[placeholder="Username"]').fill("standard_user") #ternyata kalau inputnya dihapus tetep bisa berjalan, akan tetapi lebih baik menggunakan input
    page.locator('input[type="Password"]').fill("secret_sauce")
    page.locator('input[name="login-button"]').click()

    expect(page).to_have_title("Swag Labs") 
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    inventory_page_title = page.locator("//div[@class='app_logo']").text_content()
    assert inventory_page_title == 'Swag Labs'

    page.close()

test = [('standar_user','','Epic sadface: Password is required'),
        ('','secret_sauce','Epic sadface: Username is required'),]

@pytest.mark.parametrize('username, password, error' , test)
def test_login_negative(page: Page,username, password, error):
    page.goto("https://saucedemo.com")

    page.locator('input[placeholder="Username"]').fill(username) #ternyata kalau inputnya dihapus tetep bisa berjalan, akan tetapi lebih baik menggunakan input
    page.locator('input[type="password"]').fill(password)
    page.locator('input[name="login-button"]').click()
     
    galat = page.locator('[data-test="error"]').inner_text()
    
    assert galat == error

    page.close()