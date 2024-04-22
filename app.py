from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def process_data():
    if request.method == 'POST':
        selected_options = request.form.getlist('selected_options')

        # Wyświetl wybrane opcje
        html_options = ""
        for option in selected_options:
            html_options += f"<li>{option}</li>"

        return render_template('process_data.html', options=html_options)

    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)