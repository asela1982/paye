def tax_salary(x):
    if x <= 100000:
        return 0
    elif x>100000 and x<=150000:
        return (x*0.04)-4000
    elif x>150000 and x<=200000:
        return (x*0.08)-10000
    elif x>200000 and x<=250000:
        return (x*0.12)-18000
    elif x>250000 and x<=300000:
        return (x*0.16)-28000
    elif x>300000 and x<=350000:
        return (x*0.20)-40000
    else:
        return (x*0.24)-54000


def tax_bonus(income,bonus):
    # import libraries
    pass