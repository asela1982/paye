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
    import pandas as pd
    import pymysql
    import operator
    
    # connect to the database
    connection = pymysql.connect(host='us-cdbr-iron-east-01.cleardb.net',
                             user='b86c16bd05ee5b',
                             password='6be4d4c1',
                             db='heroku_f680ab9f7225c00')
    
    # construct the query that will fetch all the records from the paye table
    query = "SELECT * FROM paye"
    # pass the connection and query to pandas read_sql method to load the query data into a dataframe object
    df = pd.read_sql(query, connection)
    # calculate the relevant multiplier and round to the nearest 0.5th
    multiplier = round(operator.truediv(bonus,income)*2)/2
    # select the subset relevant to the multiplier
    df2 = df.copy()
    df2 = df2[df2.multiplier == multiplier]
    # select the row applicable for the given income and assign the results to a new dataframe
    df3 = df2[(df2['min']<=127500) & (df2['max']>=127500)]
    # extract the rate
    rate = df3.rate.values[0]
    return rate