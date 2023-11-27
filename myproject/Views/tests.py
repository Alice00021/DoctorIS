from login import Ui_LoginForm
import pytest
import psycopg2

conn = psycopg2.connect(
            dbname="Больница", 
            user="postgres", 
            password="2118", 
            host="localhost"
        )
        
        # Создаем объект курсора для выполнения SQL-запросов
cur = conn.cursor()
cur.execute("SELECT lastname, firstname, patient_code  FROM patient WHERE lastname = %s AND firstname = %s AND patient_code = %s ",
                 ('Калинин', 'Иван', 3613 ))
user = cur.fetchone()  
  
cur.execute("INSERT INTO patient  VALUES (%s, %s, %s, %s, %s)", 
            (18181, 'Иванова', 'Мария', 'Игоревна', '2020-02-02'))
cur.execute("SELECT patient_code, lastname, firstname, middlename  FROM patient WHERE patient_code = %s  AND lastname = %s AND firstname = %s AND middlename = %s AND birthday = %s ",
                 (18181, 'Иванова', 'Мария', 'Игоревна', '2020-02-02'))

user2=cur.fetchone() 
print(user)
print(user2)
# Тестирование входных данных
def test_valid_input_login():
    result=user
    assert result == ('Калинин', 'Иван', 3613)
    
def test_valid_input_register():
    result=user2
    assert result == (18181, 'Иванова', 'Мария', 'Игоревна')
    
def test_valid_input_login_2():
    cur.execute("SELECT lastname, firstname, patient_code  FROM patient WHERE lastname = %s AND firstname = %s AND patient_code = %s ",
                 ('Чесноков', 'Никита', 16789 ))
    user = cur.fetchone()  
    result=user
    assert result == ('Чесноков', 'Никита', 16789 )
      
def test_valid_input_login_3():
    cur.execute("SELECT lastname, firstname, patient_code  FROM patient WHERE lastname = %s AND firstname = %s AND patient_code = %s ",
                 ('Сомова', 'Софья', 13093 ))
    user = cur.fetchone()  
    result=user
    assert result == ('Сомова', 'Софья', 13093 )
    
def test_valid_input_login_4():
    cur.execute("SELECT lastname, firstname, patient_code  FROM patient WHERE lastname = %s AND firstname = %s AND patient_code = %s ",
                 ('Чистяков', 'Даниил',  13092 ))
    user = cur.fetchone()  
    result=user
    assert result == ('Чистяков', 'Даниил',  13092 )

def test_valid_input_login_5():
    cur.execute("SELECT lastname, firstname, patient_code  FROM patient WHERE lastname = %s AND firstname = %s AND patient_code = %s ",
                 ('Фролов', 'Владимир', 1023 ))
    user = cur.fetchone()  
    result=user
    assert result == ('Фролов', 'Владимир', 1023 )
    
def test_valid_input_login_6():
    cur.execute("SELECT lastname, firstname, patient_code  FROM patient WHERE lastname = %s AND firstname = %s AND patient_code = %s ",
                 ('Соколова', 'Алина', 13004 ))
    user = cur.fetchone()  
    result=user
    assert result == ('Соколова', 'Алина', 13004 )
    
def test_valid_input_login_7():
    cur.execute("SELECT lastname, firstname, patient_code  FROM patient WHERE lastname = %s AND firstname = %s AND patient_code = %s ",
                 ('Михеев', 'Егор', 12008 ))
    user = cur.fetchone()  
    result=user
    assert result == ('Михеев', 'Егор', 12008)
    
def test_valid_input_login_8():
    cur.execute("SELECT lastname, firstname, patient_code  FROM patient WHERE lastname = %s AND firstname = %s AND patient_code = %s ",
                 ('Кузнецов', 'Роман', 10001 ))
    user = cur.fetchone()  
    result=user
    assert result == ('Кузнецов', 'Роман', 10001)
    



