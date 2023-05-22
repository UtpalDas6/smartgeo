from flask import Blueprint,render_template,session
from flask_login import login_required
#from .models import User,Entitymaster
import sqlite3,json
dashboards = Blueprint('dashboards',__name__,template_folder='templates',
    static_folder='static',)
path = "./velzon/smartgeo.db"
def getusername(): 
    conn = sqlite3.connect(path)
    SQL = "SELECT username from loggedinuser order by id desc limit 1"
    rows = (conn.execute(SQL))
    USERNAME = ''
    for row in rows:
        return row[0]
@dashboards.route('/')
@login_required
def index():
    username = session.get('user_name','Admin')
    conn = sqlite3.connect(path)
    cursor = conn.execute('SELECT * FROM recommendation_table_new')
    data1 = cursor.fetchall()
    cursor = conn.execute('SELECT * FROM entity_master')
    data2 = cursor.fetchall()
    cursor = conn.execute('SELECT * FROM facilities')
    data3 = cursor.fetchall()
    cursor = conn.execute('SELECT * FROM offices')
    data4 = cursor.fetchall()
    cursor = conn.execute('SELECT * FROM residential')
    data5 = cursor.fetchall()
    cursor = conn.execute('SELECT * FROM entity_details')
    data6 = cursor.fetchall()
    cursor = conn.execute('SELECT * FROM customer_branchmap')
    data7 = cursor.fetchall()
    # Close the connection
    conn.close()
    return render_template('dashboards/index.html',username=username,recos=json.dumps(data1),entity=json.dumps(data2),facility=json.dumps(data3),offices=json.dumps(data4),residential=json.dumps(data5),entity_details=json.dumps(data6),customer_branchmap=json.dumps(data7))

@dashboards.route('/dashboard-analytics/')
@login_required
def dashboard_analytics():
    return render_template('dashboards/dashboard-analytics.html')

@dashboards.route('/dashboard-crm/')
@login_required
def dashboard_crm():
    return render_template('dashboards/dashboard-crm.html')

@dashboards.route('/dashboard-crypto/')
@login_required
def dashboard_crypto():
    conn = sqlite3.connect(path)
    cursor = conn.execute('SELECT * FROM recommendation_table_new')
    data1 = cursor.fetchall()
    cursor = conn.execute('SELECT * FROM entity_master')
    data2 = cursor.fetchall()
    cursor = conn.execute('SELECT * FROM facilities')
    data3 = cursor.fetchall()
    cursor = conn.execute('SELECT * FROM offices')
    data4 = cursor.fetchall()
    cursor = conn.execute('SELECT * FROM residential')
    data5 = cursor.fetchall()
    cursor = conn.execute('SELECT * FROM entity_details')
    data6 = cursor.fetchall()
    cursor = conn.execute('SELECT * FROM customer_branchmap')
    data7 = cursor.fetchall()
    # Close the connection
    conn.close()
    return render_template('dashboards/dashboard-crypto.html',recos=json.dumps(data1),entity=json.dumps(data2),facility=json.dumps(data3),offices=json.dumps(data4),residential=json.dumps(data5),entity_details=json.dumps(data6),customer_branchmap=json.dumps(data7))   

@dashboards.route('/dashboard-projects/')
@login_required
def dashboard_projects():
    return render_template('dashboards/dashboard-projects.html')

@dashboards.route('/dashboard-results/')
@login_required
def dashboard_results():
    username = (session.get('user_name'))
    conn = sqlite3.connect(path)
    cursor = conn.execute('SELECT * FROM recommendation_table_new')
    data1 = cursor.fetchall()
    cursor = conn.execute('SELECT * FROM entity_master')
    data2 = cursor.fetchall()
    cursor = conn.execute('SELECT * FROM facilities')
    data3 = cursor.fetchall()
    cursor = conn.execute('SELECT * FROM offices')
    data4 = cursor.fetchall()
    cursor = conn.execute('SELECT * FROM residential')
    data5 = cursor.fetchall()
    cursor = conn.execute('SELECT * FROM entity_details')
    data6 = cursor.fetchall()
    cursor = conn.execute('SELECT * FROM customer_branchmap')
    data7 = cursor.fetchall()
    cursor = conn.execute('SELECT * FROM recommendation_table_new')
    data8 = cursor.fetchall()
    return render_template('dashboards/dashboard-results.html',username = session.get('user_name','Admin'),recos=json.dumps(data1),entity=json.dumps(data2),facility=json.dumps(data3),offices=json.dumps(data4),residential=json.dumps(data5),entity_details=json.dumps(data6),customer_branchmap=json.dumps(data7),results=json.dumps(data8))

@dashboards.route('/dashboard-nft/')
@login_required
def dashboard_nft():
    return render_template('dashboards/dashboard-nft.html')

@dashboards.route('/dashboard-job/')
@login_required
def dashboard_job():
    return render_template('dashboards/dashboard-job.html')  
