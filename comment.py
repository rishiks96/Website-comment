from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import random

# Load the Excel file into a DataFrame
df = pd.read_excel('Comments Sheet.xlsx')

i = 0
j = 10

while i < j:

    # Extract values from each column
    column1_values = df['First Name'].dropna().tolist()  
    column2_values = df['Last Name'].dropna().tolist()  
    column3_values = df['Comment'].dropna().tolist()  
    column4_values = df['Website Link'].dropna().tolist()

    # Pick a random value from each column
    random_value_column1 = random.choice(column1_values)
    random_value_column2 = random.choice(column2_values)
    random_value_column3 = random.choice(column3_values)
    random_value_column4 = random.choice(column4_values)

    # Generate email address
    x = random.randint(0,500)

    if x%2 == 0:
        email = random_value_column1 + random_value_column2 + str(x)+ "@gmail.com"
    else:
        email = random_value_column1 + str(x)+ random_value_column2 + "@gmail.com"


    # Assign these random values to variables
    name = random_value_column1 + " " + random_value_column2
    comment = random_value_column3
    url = random_value_column4

    print(f"Value from Column1: {name}")
    print(f"Value from Column3: {comment}")
    print(f"Value from Column0: {email}")
    print(f"Value from Column4: {url}")


    driver = webdriver.Chrome()

    driver.get(url)

    # Time to wait for the page to load
    time.sleep(5)

    # Find the form fields and fill them
    name_field = driver.find_element(By.ID, 'author')  # Replace 'name' with the actual 'name' attribute of the name field
    email_field = driver.find_element(By.ID, 'email')  # Replace 'email' with the actual 'name' attribute of the email field
    comment_field = driver.find_element(By.ID, 'comment')  # Replace 'comment' with the actual 'name' attribute of the comment field

    # Enter the information into the form fields
    name_field.send_keys(name)
    email_field.send_keys(email)
    comment_field.send_keys(comment)

    # Find and click the submit button
    submit_button = driver.find_element(By.ID, 'submit')  # Replace with the actual XPath of the submit button
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()

    # Close the browser after a few seconds
    time.sleep(5)
    driver.quit()
    i += 1


