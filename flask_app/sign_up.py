import mysql.connector
import db_connection as c

if c.connection and c.connection.is_connected():

    with c.connection.cursor() as cursor:
        while True:
            user = input("Set your username:")
            query = "SELECT username FROM users WHERE username LIKE '" + user + "';"
            result = cursor.execute(query)
            if len(cursor.fetchall()) == 0:
                break
            print("This username is already taken.")
        pwd = input("Set your password:")
        while True:
            email = input("Set your email:")
            query = "SELECT email FROM users WHERE email LIKE '" + email + "';"
            result = cursor.execute(query)
            if len(cursor.fetchall()) == 0:
                break
            print("This email is already taken.")
        first_name = input("Set your first name:")
        last_name = input("Set your last name:")

        print("Insert your billing/address")

        street = input("Set your street:")
        number = input("Set your building number:")
        zone = input("Set your zono/colony:")
        
        city = input("Set your city:")
        query = "SELECT id, city FROM cities WHERE city LIKE '" + city + "';"
        result = cursor.execute(query)
        rows = cursor.fetchall()
        if len(rows) == 0:
            query = "INSERT INTO cities (city) VALUES ('" + city + "');"
            result = cursor.execute(query)
            query = "SELECT id FROM cities ORDER BY id DESC LIMIT 1"
            result = cursor.execute(query)
            rows = cursor.fetchall()
        city = rows[0][0]

        state = input("Set your state")
        query = "SELECT id, state FROM states WHERE state LIKE '" + state + "';"
        result = cursor.execute(query)
        rows = cursor.fetchall()
        if len(rows) == 0:
            query = "INSERT INTO states (state) VALUES ('" + state + "');"
            result = cursor.execute(query)
            query = "SELECT id FROM states ORDER BY id DESC LIMIT 1"
            result = cursor.execute(query)
            rows = cursor.fetchall()
        state = rows[0][0]
        
        country = input("Set your country")
        query = "SELECT id, country FROM countries WHERE country LIKE '" + country + "';"
        result = cursor.execute(query)
        rows = cursor.fetchall()
        if len(rows) == 0:
            query = "INSERT INTO countries (country) VALUES ('" + country + "');"
            result = cursor.execute(query)
            query = "SELECT id FROM countries ORDER BY id DESC LIMIT 1"
            result = cursor.execute(query)
            rows = cursor.fetchall()
        country = rows[0][0]

        zip = input("Set your zip code:")

        #Insert user values
        query = f"""INSERT INTO addresses
        (street, building_number, zone, city_id, state_id, country_id, zip_code)
        VALUES
        ('{street}',{number},'{zone}',{city},{state},{country},{zip});"""
        result = cursor.execute(query)
        query = "SELECT id FROM addresses ORDER BY id DESC LIMIT 1"
        result = cursor.execute(query)
        address = cursor.fetchall()[0][0]
        query = f"""INSERT INTO users
        (username, email, pwd, first_name, last_name, address_id)
        VALUES
        ('{user}','{email}','{pwd}','{first_name}','{last_name}',{address})"""
        result = cursor.execute(query)
c.connection.commit()
cursor.close()
c.connection.close()