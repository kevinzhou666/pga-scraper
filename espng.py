#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()


def stats():
    driver = webdriver.Chrome()
    driver.get('https://www.espn.com/golf/stats')

    # Wait for the tables and their titles to load
    tables = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'Table__TBODY'))
    )
    titles = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'Table__Title'))
    )

    # Iterate through each table and print its title and data
    for index, (title, table) in enumerate(zip(titles, tables)):
        title_text = title.text
        table_text = table.text
        
        print()
        print(f"Title: {title_text}")
        print("Table Data:")
        
        #Text Parsing
        #print(type(table_text))
        stats_lines = table_text.split('\n')

        for i in range(0, (len(stats_lines)-1), 4):
            print(f'{stats_lines[i]} | {stats_lines[i+1]} | {stats_lines[i+2]} | {stats_lines[i+3]}')


'''
Now we are going to get into going into the standings page
'''



def standings(col):
    driver = webdriver.Chrome()
    driver.get('https://www.espn.com/golf/standings')
    time.sleep(5)

    tables = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'Table__TBODY'))
    )



    tabletitles = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'Table__Title'))
    )

    for index, t in enumerate(tables):

        table = t.text
        tablelist = table.split('\n')

        ## List comprehension
        max_length_first = max(len(str(item)) for item in tablelist[::3])
        max_length_second = max(len(item) for item in tablelist[1::3])

        print(tabletitles[index].text)
        for i in range(0, len(tablelist), col):
            print(f'{tablelist[i]:<{max_length_first}}\t| {tablelist[i+1]:<{max_length_second}}\t| {tablelist[i+2]}')
        print("\n")



def main():
    print("Welcome to the accesible golf scoreboard")
    continues = True
    while continues:
        print("Select your scoreboard interest")
        print("1. Standings\n2. Stats\n")
        choice = input("Put in your choice: ")

        if choice == "1":
            standings(3)
        else:
            stats()

if __name__ == "__main__":
    main()









