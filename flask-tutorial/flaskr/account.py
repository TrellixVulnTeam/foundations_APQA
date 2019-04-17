from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import generate_password_hash

from flaskr.db import get_db

import sys

bp = Blueprint('account', __name__, url_prefix='/account')

@bp.route('/', methods=['GET'])
def account_overview():
	return render_template('account/account_settings.html')

@bp.route('/change_username', methods=['POST'])
def change_username():
	new_username = request.form['new_username']
	db = get_db()
	db.execute('UPDATE user SET username="{}" WHERE id="{}"'.format(new_username, session['user_id']))
	db.commit()
	session['username']=new_username
	return redirect(url_for('account.account_overview'))



@bp.route('/change_password', methods=['POST'])
def change_password():
	new_password = request.form['new_password']
	db = get_db()
	db.execute('UPDATE user SET password="{}" WHERE id="{}"'.format(generate_password_hash(new_password), session['user_id']))
	db.commit()
	return redirect(url_for('account.account_overview'))

@bp.route('/delete_notes', methods=['POST'])
def delete_notes():
	db = get_db()
	db.execute('DELETE FROM post WHERE author_id="{}"'.format(session['user_id']))
	db.commit()
	return redirect(url_for('index'))

@bp.route('/delete_account', methods=['POST'])
def delete_account():
	db = get_db()
	db.execute('DELETE FROM user WHERE id="{}"'.format(session['user_id']))
	db.commit()
	return redirect(url_for('auth.register'))
