from time import sleep

from selenium import webdriver

# Modern Selenium handles the driver automatically!
driver = webdriver.Chrome()  # You can also use Chrome(), Firefox(), etc.

driver.get("https://www.google.com/")

sleep(2)  # Wait for the page to load
print(driver.title)

page_content = driver.page_source

with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
    file.write(page_content)
        
print("Page content successfully saved to Webpage_task_11.txt")
driver.quit()  # Close the browser when done
