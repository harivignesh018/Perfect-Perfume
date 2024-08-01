from flask import Flask, render_template, redirect, url_for
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app = flask(__name__)



if __name__ == "__main__":
    app.run(debug=True)