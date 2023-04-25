from flask_app import app, render_template, redirect, request, session, flash, bcrypt


@app.route('/')
def main():
    return render_template('index.html')