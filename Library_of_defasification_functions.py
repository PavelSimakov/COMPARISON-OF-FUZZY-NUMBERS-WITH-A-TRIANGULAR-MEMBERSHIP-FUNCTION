import math         

def GCD(a, b):                              #Наибольший общий делитель (The greatest common divisel)
    while b:
        a, b = b, a % b
    return a

def Diskriminant(A, B, C):                  #Считаем дискриминант для метода USt4 (We calculate the discriminant for the USt4 method)
    
    gcd=(GCD(GCD(A,B),C))
    
    A=A/gcd
    B=B/gcd
    C=C/gcd

    D=pow(B,2)-4*A*C
    if D>0:
        X1=(B+math.sqrt(D))/(2*A)
        X2=(B-math.sqrt(D))/(2*A)
        if 0<X1 and X1<1:
            return X1
        else:
            return X2
    else:
        X1=-B/(2*A)
        return X1

def Equation(x, a, b, c, A, B, C):          #Находим lamda для метода USt2 (Finding lamda for USt2 method)
    if x<b:
        myA=((c-x)/(c-a))-((b-x)/(c-a))*math.log((b-x)/(b-a))
    if x<B:
        myB=((C-x)/(C-A))-((B-x)/(C-A))*math.log((B-x)/(B-A))
    if x==b:
        myA=(c-b)/(c-a)
    if x==B:
        myB=(C-B)/(C-A)
    if x>b:
        myA=((c-x)/(c-a))-((b-x)/(c-a))*math.log((x-b)/(c-b))
    if x>B:
        myB=((C-x)/(C-A))-((B-x)/(C-A))*math.log((x-B)/(C-B))
    lamda=myA+myB-1
    return lamda

def Method_of_division_in_half(P, eps):     #Метод деления пополам для метода USt1 (Bisection method for USt1 method)
    tL=0 
    tR=1
    teps=0.5
    while teps>eps:
        t=(tL+tR)/2
        f=t-t*math.log(t)
        if f == P:
            fi=t
            break
        elif f < P:
            tL=t
            teps=teps/2
        else:
            tR=t
            teps=teps/2
        fi=t
    return fi

def Adamo(a, b, c, A, B, C, alfa):          #Метод Адамо (Adamo method) 
    o=c-(c-b)*alfa
    O=C-(C-B)*alfa
    return o, O

def CofMax(a, b, c, A, B, C):               #Метод центра максимумов (Center maxima method)
    o=b
    O=B
    return o, O

def CofMass(a, b, c, A, B, C):              #Метод Центра масс (Center of Mass Method)
    o=(a+b+c)/3
    O=(A+B+C)/3
    return o, O

def Medians(a, b, c, A, B, C):              #Метод Медианы (Median Method)
    o=(a+2*b+c)/4
    O=(A+2*B+C)/4
    return o, O

def Chang(a, b, c, A, B, C):                #Метод - индекс Чанга (Method - Chang Index)
    o=(c**2-a**2-a*b+b*c)/6
    O=(C**2-A**2-A*B+B*C)/6
    return o, O

def PAv(a, b, c, A, B, C):                  #Метод - возможное среднее (Method - Possible Average)
    o=(a+4*b+c)/6
    O=(A+4*B+C)/6
    return o, O

def Jager(a, b, c, A, B, C):                #Метод - индекс Ягера (Method - Yager index)
    o=(a+2*b+c)/4
    O=(A+2*B+C)/4
    return o, O

def USt1(a, b, c, A, B, C):                 #Метод - USt1 (Method - USt1)
    eps=0.0001
    if (a+c)/2==b:
        o=b
    elif(a+c)/2<b:
        o=b-(b-a)*Method_of_division_in_half((((b-a)-(c-b))/(2*(b-a))), eps)
    elif(a+c)/2>b:
        o=b+(c-b)*Method_of_division_in_half((((c-b)-(b-a))/(2*(c-b))), eps)
    if (A+C)/2==B:
        O=B
    elif(A+C)/2<B:
        O=B-(B-A)*Method_of_division_in_half((((B-A)-(C-B))/(2*(B-A))), eps)
    elif(A+C)/2>B:
        O=B+(C-B)*Method_of_division_in_half((((C-B)-(B-A))/(2*(C-B))), eps)
    return o, O

def USt2(a, b, c, A, B, C):                 #Метод - USt2 (Method - USt2) 
    i=0
    if c<=A:
        o=0
        O=1
    elif C<=a:
        o=1
        O=0
    else:
        x1=max(a,A)
        x2=min(c,C)
        lamda1=Equation(x1, a, b, c, A, B, C)
        lamda2=Equation(x2, a, b, c, A, B, C)
        if lamda1==0:
            ystar=x1
        elif lamda2==0:
            ystar=x2
        else:
            eps=0.00001
            while (x2-x1)>eps:
                x0=(x1+x2)/2
                Fx0=Equation(x0, a, b, c, A, B, C)
                Fx2=Equation(x2, a, b, c, A, B, C)
                if(Fx0*Fx2)>0:
                    x2=x0
                else:
                    x1=x0
            ystar=x0
        if ystar<b:
            myA=((c-ystar)/(c-a))-((b-ystar)/(c-a))*math.log((b-ystar)/(b-a))
            myA = float('{:.1f}'.format(myA))      
            i=i+1
        elif ystar==b:
            myA=(c-b)/(c-a)
            myA = float('{:.1f}'.format(myA)) 
            i=i+1
        else:
            myA=((c-ystar)/(c-a))-((b-ystar)/(c-a))*math.log((ystar-b)/(c-b))
            myA = float('{:.1f}'.format(myA)) 
            i=i+1
        if myA<0.5:
            o=0
            O=1
        elif myA>0.5:
            o=1
            O=0
        else:
            o=1
            O=1
    if i>0:
        return o, O, myA
    else:
         myA=777
    return o, O, myA

def USt4(a, b, c, A, B, C):                 #Метод - USt4 (Method - USt4)
    e=(4*b*c-pow((a+b), 2))/(4*(c-a))
    t_star1=(2*c-a-b)/(2*(c-a))
    delta=(pow((c+b), 2)-4*a*b)/(4*(c-a))
    t_star2=(c+b-2*a)/(2*(c-a))

    E=(4*B*C-pow((A+B), 2))/(4*(C-A))
    T_star1=(2*C-A-B)/(2*(C-A))
    DELTA=(pow((C+B), 2)-4*A*B)/(4*(C-A))
    T_star2=(C+B-2*A)/(2*(C-A))

    if DELTA<=e:
        dAB=1
    elif c<=A:
        dAB=0
    else:
        tDAe=t_star1
        tFBe=(C+B-2*A-math.sqrt(pow((C+B-2*A),2)+4*(A-e)*(C-A)))/(2*(C-A))
        tDA_DELTA=(2*c-a-b-math.sqrt(pow((2*c-a-b),2)-4*(c-DELTA)*(c-a)))/(2*(c-a))
        if tFBe>=tDAe:
            dAB=tFBe
        elif tDA_DELTA>=T_star2:
            dAB=tDA_DELTA
        else:
            dAB=Diskriminant((c-a)+(C-A), ((2*c-a-b)+(C+B-2*A)), c-A)
    if delta<=E:
        dBA=1
    elif C<=a:
        dBA=0
    else:
        tDBE=T_star1
        tFAE=(c+b-2*a-math.sqrt(pow((c+b-2*a),2)+4*(a-E)*(c-a)))/(2*(c-a))
        tDB_delta=(2*C-A-B-math.sqrt(pow((2*C-A-B),2)-4*(C-delta)*(C-A)))/(2*(C-A))
        if tFAE>=tDBE:
            dBA=tFAE
        elif tDB_delta>=t_star2:
            dBA=tDB_delta
        else:
            dBA=Diskriminant((C-A)+(c-a), ((2*C-A-B)+(c+b-2*a)), C-a)
    if dAB>dBA:
        o=1
        O=0
    elif dAB<dBA:
        o=0
        O=1
    else:
        o=1
        O=1
    dAB = float('{:.1f}'.format(dAB))     
    dBA = float('{:.1f}'.format(dBA))
    return o, O, dAB, dBA