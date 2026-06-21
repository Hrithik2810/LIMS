from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'lims_secret_key_change_this_later'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/causes')
def causes():
    return render_template('index.html') # Placeholder pointing to home

@app.route('/donate')
def donate():
    return render_template('donate.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f"Thank you, {name}! Your message has been sent successfully.", "success")
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)