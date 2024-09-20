from flask import Flask, render_template, url_for, request, redirect
import db_connection as c

app = Flask(__name__)

@app.route("/")
def function():
    if c.connection and c.connection.is_connected:
        with c.connection.cursor() as cursor:
            query = "SELECT * FROM countries;"
            result = cursor.execute(query)
            rows = cursor.fetchall()
            countries = ""
            for row in rows:
                countries += f'<option value="{row[0]}">{row[1]}</option>\n'
            
            query = "SELECT * FROM states;"
            result = cursor.execute(query)
            rows = cursor.fetchall()
            states = ""
            for row in rows:
                states += f'<option value="{row[0]}">{row[1]}</option>\n'
            
            query = "SELECT * FROM cities;"
            result = cursor.execute(query)
            rows = cursor.fetchall()
            cities = ""
            for row in rows:
                cities += f'<option value="{row[0]}">{row[1]}</option>\n'
    cursor.close()
    return render_template("index.html", countries=countries, states=states, cities=cities)

@app.route("/submit_user", methods=["get","post"])
def submit_user():
    if request.method == "POST":
        if c.connection and c.connection.is_connected:
            data = request.form
            user = data.get("username")
            pwd = data.get("pwd")
            email = data.get("email")
            first_name = data.get("first_name")
            last_name = data.get("last_name")
            street = data.get("street")
            number = data.get("building_number")
            zone = data.get("zone")
            country = data.get("country")
            state = data.get("state")
            city = data.get("city")
            zip = data.get("zip")
            with c.connection.cursor() as cursor:
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
    return render_template("registered_confirmation.html")

if __name__ == '__main__':
    app.run(debug=True, port=5000)