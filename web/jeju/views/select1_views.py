from flask import Blueprint, render_template

bp = Blueprint('select1', __name__, url_prefix='/select')


@bp.route('/select1')
def open_select1():
    return render_template('select/select1.html')
