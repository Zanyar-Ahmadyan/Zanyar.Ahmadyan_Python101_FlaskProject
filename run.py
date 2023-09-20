from flask import Flask, request, render_template

app = Flask(__name__)

# Define a route for the form submission page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the student number, name, and surname from the form
        student_number = request.form['student_number']
        name = request.form['name']
        surname = request.form['surname']

        # Create or open the data.txt file and append the information
        with open('data.txt', 'a') as file:
            file.write(f'Student Number: {student_number}, Name: {name}, Surname: {surname}\n')

        # Return a response or redirect to another page
        return f'Student Number: {student_number}<br>Name: {name}<br>Surname: {surname}'

    # Render the HTML form
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
