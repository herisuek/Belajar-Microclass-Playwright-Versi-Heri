from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://saucedemo.com") #untuk menaruh tujuan, harus menggunakan https atau http ternyata, kalau "saucedemo.com" saja tidak bisa berjalan botnya

    title = page.title()
    print(title)

    page.locator('input[placeholder="Username"]').fill("standard_user") #ternyata kalau inputnya dihapus tetep bisa berjalan, akan tetapi lebih baik menggunakan input
    page.locator('input[type="Password"]').fill("secret_sauce")
    page.locator('input[name="login-button"]').click()
    
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click() #contoh tidak pakai input(lanjutan baris 12), tapi harus menggunakan tanda [], gbsa jalan kalau ga pake []
    page.locator('[name="add-to-cart-sauce-labs-bike-light"]').click()
    page.locator('[id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    page.locator('xpath=//button[@id="add-to-cart-sauce-labs-fleece-jacket"]').click() #relative xpath

    page.locator('[class="shopping_cart_link"]').click()
    page.locator('xpath=//button[@class="btn btn_action btn_medium checkout_button "]').click()  #harus pakai @, gbsa jalan kalau ga pake @
    
    page.locator("//input[@id='first-name']").fill('Heri')                    #xpath
    page.locator("(//input[@id='last-name'])[1]").fill('Setiyawan')           #xpath
    page.locator("//input[@id='postal-code']").fill('13770')                  #xpath

    page.locator('[data-test="continue"]').click()                            #attribute selector
    page.locator('[class="btn btn_action btn_medium cart_button"]').click()   #atribute selector 
    page.pause() #untuk berhenti supaya tidak ke close browsernya
    #browser.close() #langsung close browsernya
