# -*- coding: utf-8 -*-
"""Практична робота №1: оператори, умови, цикли."""
import math
VALUES = (3, 4, 5)
STUDENT = 'Рева Вероніка'

def expressions(a,b,c):
    return {'Сума квадратів':a*a+b*b+c*c,'Середнє':(a+b+c)/3,'Дискримінант':b*b-4*a*c,'Гіпотенуза':math.hypot(a,b),'Трикутник':a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a,'Залишок':a%b if b else None,'Ціла частина':a//b if b else None}

def convert(raw):
    try:
        x=float(raw); return {'int':int(x),'float':x,'bool':bool(x),'type':type(x).__name__,'str':str(x)}
    except ValueError: return {'Помилка':'Потрібно ввести число'}

def classify_grade(score):
    if not 0<=score<=100: raise ValueError('Бал поза діапазоном')
    if score>=90:return 'A'
    elif score>=82:return 'B'
    elif score>=74:return 'C'
    elif score>=64:return 'D'
    elif score>=60:return 'E'
    elif score>=35:return 'FX'
    return 'F'

def triangle_type(a,b,c):
    if min(a,b,c)<=0 or a+b<=c or a+c<=b or b+c<=a:return 'не є трикутником'
    sides=sorted((a,b,c))
    if a==b==c:return 'рівносторонній'
    if abs(sides[0]**2+sides[1]**2-sides[2]**2)<1e-9:return 'прямокутний'
    if a==b or a==c or b==c:return 'рівнобедрений'
    return 'різносторонній'

def triangle_area(a,b,c):
    if triangle_type(a,b,c)=='не є трикутником':return 0.0
    p=(a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

def factorial(n):
    if n<0:raise ValueError('n має бути невід’ємним')
    result=1
    for k in range(2,n+1):result*=k
    return result

def harmonic_sum(n):return sum(1/k for k in range(1,n+1))

def multiplication_table(n):
    for i in range(1,n+1):print(' '.join(f'{i*j:4}' for j in range(1,n+1)))

def calculator(commands):
    history=[]
    for line in commands:
        if line=='quit':break
        if line=='history':print('Історія:',history);continue
        parts=line.split()
        if len(parts)!=3:print('Невірний формат');continue
        try:
            x,op,y=float(parts[0]),parts[1],float(parts[2])
            if op in ('/','//','%') and y==0:raise ZeroDivisionError
            result={'+':lambda:x+y,'-':lambda:x-y,'*':lambda:x*y,'/':lambda:x/y,'//':lambda:x//y,'%':lambda:x%y,'**':lambda:x**y}.get(op)
            if result is None:print('Невідомий оператор');continue
            value=result();history.append(f'{line} = {value}');print(history[-1])
        except (ValueError,ZeroDivisionError,OverflowError):print('Помилка обчислення')
    return history

def main():
    a,b,c=VALUES
    print('1.1. Вирази:', {k:round(v,2) if isinstance(v,float) else v for k,v in expressions(a,b,c).items()})
    print('1.2. Перетворення:',convert(str(a)),'помилка:',convert('abc'))
    print(f'Ім’я: {STUDENT:>20}, номер: {int(a):04d}, len={len(STUDENT)}, id={id(STUDENT)}, range={list(range(2,8,2))}')
    print('2.1. ЄКТС:',[(v,classify_grade(v)) for v in (0,34,35,59,60,63,64,73,74,81,82,89,90,100)])
    print('2.2. Трикутник:',triangle_type(3,4,5),'площа:',triangle_area(3,4,5))
    print('3.1. Факторіал:',factorial(6),'гармонічна сума:',round(harmonic_sum(6),6));multiplication_table(4)
    print('3.2. Калькулятор:');calculator(['8 + 2','8 / 0','bad','history','quit'])
if __name__=='__main__':main()
