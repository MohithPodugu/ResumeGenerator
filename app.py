from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the home page (index.html)
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Extract form data from the POST request
        details = {
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "contact": request.form.get('contact'),
            "role": request.form.get('role'),
            "profile": request.form.get('profile'),
            "education": request.form.get('education'),
            "additional_education": request.form.get('additional_education'),
            "experience": request.form.get('experience'),
            "past_experience": request.form.get('past_experience'),
            "skills": request.form.get('skills').split(','),  # Convert comma-separated skills into a list
            "projects": request.form.get('projects'),
        }
        # Render the resume.html template with the collected details
        return render_template('resume.html', details=details)
    return render_template('index.html')

# Route for the tips page
@app.route('/tips')
def tips():
    return render_template('tips.html')

if __name__ == '__main__':
    app.run(debug=True)
