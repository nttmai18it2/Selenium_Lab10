import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        chrome_driver_path = "C:/Users/ADMIN/Documents/KiemThu/chromedriver.exe"
        driver = webdriver.Chrome(chrome_driver_path)

        driver.get("http://practice.automationtesting.in/")
        title = driver.title
        driver.set_window_size(500,400)

        print(driver.current_url)
        self.assertTrue(title == "Automation Practice Site")
        
if  __name__ == "__main__":
    unittest.main()