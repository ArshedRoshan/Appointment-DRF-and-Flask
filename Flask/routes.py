from flask import Flask,render_template,request,redirect
from app import apps
import requests
import json
from flask import session




app = apps()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            url = 'http://127.0.0.1:8000/token'
            data = {'username': username, 'password': password}
            response = requests.post(url, data=data)
            print('data',data)
            print('resss',response.status_code)
        
            if response.status_code == 200:
                access_token = response.json()['access']
                refresh_token = response.json()['refresh']
                
                session['access_token'] = access_token
                session['refresh_token'] = refresh_token
                return redirect('/home')
            else:
                return 'Error: ' + response.text
        except requests.exceptions.RequestException as e:
            return f'Request Exception: {e}'
        except Exception as e:
            return f'Unexpected Error: {e}'
    else:
        return render_template('login.html')







@app.route('/add_appointments',methods=['GET', 'POST'])
def add_appointment():
    access_token = session.get('access_token')
    
    if not access_token:
        return redirect('/')
    
    headers = {'Authorization': 'Bearer ' + access_token}
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'Email': request.form['Email'],
            'date': request.form['date'],
            'note': request.form['note']
        }
        try:
            response = requests.post('http://127.0.0.1:8000/add',data=data,headers=headers)
            print('assss',response)
            return redirect('/home')
        except requests.exceptions.RequestException as e:
            return f'Request Exception: {e}'
        except Exception as e:
             return f'Unexpected Error: {e}'
            
    return render_template('new_appointment.html')

@app.route('/get_user/<int:id>',methods = ['GET','POST'])
def gett(id):
    access_token = session.get('access_token')
    
    if not access_token:
        return redirect('/')
    
    headers = {'Authorization': 'Bearer ' + access_token}
    try:
        response = requests.get('http://localhost:8000/update_appoinment/{}'.format(id),headers=headers)
        appointment = response.json()
        return render_template('update_appointment.html', appointment=appointment)
    except requests.exceptions.RequestException as e:
            return f'Request Exception: {e}'
    except Exception as e:
            return f'Unexpected Error: {e}'



@app.route('/update_appointments/<int:id>', methods=['GET', 'POST','PUT'])
def update_appointment(id):
    
    access_token = session.get('access_token')
    if not access_token:
        return redirect('/')
    
    headers = {'Authorization': 'Bearer ' + access_token}
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'Email': request.form['Email'],
            'date': request.form['date'],
            'note': request.form['note']
        }
        try:
            response = requests.put('http://localhost:8000/update_appoinment/{}'.format(id),data=data,headers=headers)
        
            return redirect('/home')
        except requests.exceptions.RequestException as e:
            return f'Request Exception: {e}'
        except Exception as e:
            return f'Unexpected Error: {e}'
        
   

@app.route('/delete_appointment/<int:id>',methods=['POST','GET'])
def del_appo(id):
    response = requests.delete('http://127.0.0.1:8000/delete_appointments/{}'.format(id))
    try:
        appointment = response.json()
        print('rererer',response.text)
    except json.JSONDecodeError:
        appointment = json.loads(response.text)
    return redirect('/home')


@app.route('/home')
def home():
    access_token = session.get('access_token')
    if not access_token:
        return redirect('/')
    response = requests.get('http://127.0.0.1:8000/get_appointment', headers={'Authorization': f'Bearer {access_token}'})
    appointments = response.json()
    
    return render_template('application_list.html',appointments=appointments)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')





    
