import json
import jwt
import datetime

def check_details_exist(email, phone_number, connection):
    sql_query = f"select * from users where email = '{email}' or phone_number = '{phone_number}';"
    result = connection.execute(sql_query)
    rows = [x for x in result]
    return False if len(rows) == 0 else True


def user_sign_up(data, connection):
    if len(data) < 4:
        resp = {'status': 'fail', 'msg': 'param missing'}
        return json.dumps(resp)
    
    first_name = data['name'].split(' ')[0]
    last_name = data['name'][len(first_name)+1:]
    email = data['email']
    phone_number = data['phone_number']
    password = data['password']

    if check_details_exist(email, phone_number, connection):
        resp = {'status': 'fail', 'msg': 'Email or Phone_number already exist'}
        return json.dumps(resp)
    
    sql_query= f"insert into users (first_name, last_name, email, phone_number, password) values ('{first_name}', '{last_name}', '{email}', '{phone_number}', '{password}');"

    result = connection.execute(sql_query)
    sql_query = f"Select * from users where email = '{email}';"
    
    result = connection.execute(sql_query)
    for row in result:
        break
    
    payload = {"user_id": row[0], 'first_name': row[1],'created_on': datetime.datetime.now().strftime('%d-%m-%yT%H:%M:%S')}
    jwt_token = jwt.encode(payload, "flickhub", algorithm = 'HS256')
    
    resp = {'status': 'ok', 'msg': 'User Created', 'jwt_token': jwt_token}
        
    return json.dumps(resp)

def login(data, connection):
    if len(data) < 2:
        resp = {'status': 'fail', 'msg': 'Param Missing'}
        return json.dumps(resp)
    
    sql_query = 'Select * from users where '
    
    email = data.get('email', None)
    if email:
        resp = {'status': 'fail', 'msg': 'Email not found!'}
        sql_query = sql_query + f"email = '{email}';"
    else:
        resp = {'status': 'fail', 'msg': 'Phone number not found!'}
        phone_number = data.get('phone_number', None)
        sql_query = sql_query + f"phone_number = '{phone_number}';"
    
    result = connection.execute(sql_query)

    for row in result:
        break
    try:
        if row[5] == data.get('password', None):
            payload = {"user_id": row[0], 'first_name': row[1],'created_on': datetime.datetime.now().strftime('%d-%m-%yT%H:%M:%S')}
            jwt_token = jwt.encode(payload, "flickhub", algorithm = 'HS256')
            resp = {'status': 'ok', 'msg': 'Login Successful!', 'jwt_token': jwt_token}
        else:
            resp = {'status': 'fail', 'msg': 'Password Incorrect!'}
    except:
        pass
    return json.dumps(resp)
    
def user_activity_log(data, connection):
    activity_id = data['activity_id']
    additional_details = data['additional_details']
    user_id = data['user_id']

    sql_query= f"insert into user_activity (user_id, activity_id, additonal_details) values ('{user_id}', '{activity_id}', '{additional_details}');"

    result = connection.execute(sql_query)
    resp = {'status': 'ok', 'msg': 'User activity created'}
        
    return json.dumps(resp)
