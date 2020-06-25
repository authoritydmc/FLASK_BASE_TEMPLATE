from flask import render_template,redirect,url_for,Blueprint


print("Initialial ->",__name__," pacakge->",__package__)

bp=Blueprint('route1',__name__)

@bp.route('/abc')
@bp.route('/')
def home():
    return render_template('base.html')