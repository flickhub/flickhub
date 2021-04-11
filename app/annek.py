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
        resp = {'status': 'fail', 'msg': 'email or phone_number already exist'}
        return json.dumps(resp)
    
    sql_query= f"insert into users (first_name, last_name, email, phone_number, password) values ('{first_name}', '{last_name}', '{email}', '{phone_number}', '{password}');"

    # try: 
    result = connection.execute(sql_query)
    resp = {'status': 'ok', 'msg': 'user_created'}
    # except Exception as e:
    #     resp = {'status': 'fail', 'msg': 'issue with sql'}
        
    return json.dumps(resp)

def login(data, connection):
    if len(data) < 2:
        resp = {'status': 'fail', 'msg': 'param missing'}
        return json.dumps(resp)
    
    sql_query = 'Select * from users where '
    
    email = data.get('email', None)
    if email:
        sql_query = sql_query + f"email = '{email}';"
    else:
        phone_number = data.get('phone_number', None)
        sql_query = sql_query + f"phone_number = '{phone_number}';"
    
    result = connection.execute(sql_query)
    for row in result:
        break
    if row[5] == data.get('password', None):
        payload = {"user_id": row[0], 'valid_till': datetime.datetime.now().strftime('%d-%m-%yT%H:%M:%S')}
        jwt_token = jwt.encode(payload, "flickhub", algorithm = 'HS256')
        resp = {'status': 'ok', 'msg': 'login successful', 'jwt_token': jwt_token}
    else:
        resp = {'status': 'fail', 'msg': 'login failed'}
    
    return json.dumps(resp)
    
    