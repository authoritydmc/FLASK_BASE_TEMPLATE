from flask import  Flask
from .routes import route1

app=Flask(__name__)
app.register_blueprint(route1.bp)

print("Initial->",__name__," pacakge->",__package__)

