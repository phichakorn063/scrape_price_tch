from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

app = Flask(__name__)

@app.route('/get-price', methods=['GET'])
def get_price():
    # ตั้งค่า WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://www.thaiwatsadu.com/th/product/%E0%B8%81%E0%B8%A3%E0%B8%B0%E0%B9%80%E0%B8%9A%E0%B8%B7%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%AB%E0%B8%A5%E0%B8%B1%E0%B8%87%E0%B8%84%E0%B8%B2-%E0%B8%8B%E0%B8%B5%E0%B8%94%E0%B8%B2%E0%B8%A3%E0%B9%8C%E0%B9%80%E0%B8%8A%E0%B8%84-%E0%B9%80%E0%B8%8C%E0%B8%AD%E0%B8%A3%E0%B9%88%E0%B8%B2-%E0%B8%A3%E0%B8%B8%E0%B9%88%E0%B8%99-%E0%B8%84%E0%B8%A5%E0%B8%B0%E0%B8%82%E0%B8%99%E0%B8%B2%E0%B8%94-%E0%B8%AA%E0%B8%B5%E0%B9%81%E0%B8%9A%E0%B8%A5%E0%B9%87%E0%B8%84%E0%B9%80%E0%B8%A7%E0%B8%87%E0%B9%80%E0%B8%81%E0%B9%89-60190804')

    # รอให้หน้าโหลด
    time.sleep(3)

    # ดึงข้อมูลราคา
    try:
        price_element = driver.find_element(By.CLASS_NAME, 'font-price')
        price = price_element.text
        driver.quit()
        return jsonify({'price': price})
    except Exception as e:
        driver.quit()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # ใช้ host='0.0.0.0' เพื่อให้ Flask เข้าถึงได้จากภายนอก และเปลี่ยนพอร์ต
    app.run(debug=True, host='0.0.0.0', port=5001)
