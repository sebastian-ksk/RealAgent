# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 17:05:28 2020

@author: Hector Sanabria
"""
import collections
import sys
import hashlib
import hmac
import time
import requests
import json
from datetime import datetime ,timedelta
from datetime import date
import pandas as pd 
DID="001D0A0117A4"
ownerpass="multiagent"
tokenID="6BA678C3A1844C6B9B9767F9543331A1"
# api="https://api.weatherlink.com/v1/StationStatus.json?user="+DID+"&pass="+ownerpass+"&apiToken="+tokenID
api="https://api.weatherlink.com/v1/NoaaExt.json?user="+DID+"&pass="+ownerpass+"&apiToken="+tokenID
# api="https://api.weatherlink.com/v1/StationStatus.json?user="+DID+"&pass="+ownerpass+"&apiToken="+tokenID
# dir_T=".\weather.txt"
# print("v2 API URL: "+api)
# r = requests.get(api) 
# text=r.text
# print(text)
# text=text.split()
dir_actual='/home/pi/Desktop/RealAgent/src/AquaCrop_OsPy/AquaCrop_OsPy'
dir_T=dir_actual+"/Date_Weather_station/Intelligent_Irrigation.csv"
dir_weather=dir_actual+'/Date_Weather_station/Weather_station_15m.csv'
dir_rain=dir_actual+'/Date_Weather_station/Rain_2014_2021.txt'
dir_weather2=dir_actual+'/Date_Weather_station/Weather_station_3.csv'


def tabla(dir_T):
    df=pd.DataFrame()              #Dataset temperature max
    df=df.fillna(0)
    df_F=pd.DataFrame()              #Dataset temperature max
    df_F=df_F.fillna(0)
    with open(dir_T,'r',errors='ignore') as fin:
        a = fin.read().splitlines(True)
    aux_1=[]
    aux_2=[]
    aux_3=[]
    aux_4=[]
    
    for c in range(6,len(a)-1):
        b=a[c].replace('"','')
        b=b.split(',')
        # print(b[0])
        f=b[0].split(' ')
        f=f[0].split('/')
        x = datetime(int('20'+str(f[2])), int(f[0]), int(f[1]))
        
        aux_1.append(x)
        aux_2.append(float(b[7]))
        aux_3.append(float(b[22]))
        aux_4.append(float(b[27]))
       
    df['Date']=aux_1
    df['Temp']=aux_2
    df['Rain']=aux_3
    df['ET']=aux_4
    fecha=df['Date']
    a=df['Date'].unique()       #saca todas las fechas sin repetir 
    t1=[]
    t2=[]
    t3=[]
    t4=[]
    t5=[]
    for x in a :
        dat=df[(df['Date']==x)]
        tmax=dat['Temp'].max()
        tmin=dat['Temp'].min()
        ET=sum(dat['ET'])   #9 es el valor de la columana donde esta almmacenado ET
        rain=sum(dat['Rain'])   #9 es el valor de la columana donde esta almmacenado Rain daily (mm)
        t1.append(tmax)
        if tmin<0:
            tmin=7.89
        t2.append(tmin)
        t3.append(ET)
        t4.append(rain)
        t5.append(x)
    
    df_F['Date']=t5
    df_F['Tmax(C)']=t1
    df_F['Tmin(C)']=t2
    df_F['ET0']=t3
    df_F['Rain(mm)']=t4
    df_F.set_index('Date',inplace=True)

    df_F.to_csv(dir_weather,header=True, sep='\t',float_format="%.2f",na_rep='0')
    print('ok')
def generate_date(start,per):
    fecha_in=datetime.strptime(start, "%Y-%m-%d")
    # fecha_in=start
    dfr=pd.DataFrame()
    dfr=dfr.fillna(0)
    datelist = pd.Series(pd.date_range(fecha_in, periods=per).tolist())
    dfr['Date']=datelist
    f=[]
    for d in dfr['Date']:
        a=d.strftime( "%Y-%m-%d")
        f.append(a)
    dfr['Date']=f
    return dfr
def station():
    try:
        df=pd.read_csv(dir_weather, sep='\t')
    
        r = requests.get(api) 
        text=r.text
        t=text.split(',{')
        weater=open(dir_T,'a',errors='ignore')
        for x in range(len(t)):
            if x==0:
                t[0] = t[0].replace("[","")
            else:
                t[x] = '{'+str(t[x].replace("]",""))
            res = json.loads(t[x])
            hora=res["observation_time_rfc822"]
            res=res["davis_current_observation"]
            
            temp_day_low_f=str(format((float(res['temp_day_low_f'])-32)/1.8, '0.2f'))
            temp_day_high_f=str(format((float(res['temp_day_high_f'])-32)/1.8, '0.2f'))
            et_day =str(format(float(res['et_day'])*25.4, '0.3f'))
            rain_day_in=str(format(float(res['rain_day_in'])*25.4, '0.3f'))
            print(et_day)
            print(rain_day_in)
        today = str(date.today()).split()[0]        #calculo de fecha actual
        Hour = str(time.strftime("%X"))        #calculo de fecha actual
        df = df.reindex(columns=['Date', 'Hour' ,'Tmax(C)', 'Tmin(C)', 'ET0','Rain(mm)'])
        # df=pd.DataFrame()
        # df=df.fillna(0)
        df=df.append({'Date' : today , 'Hour' : Hour ,'Tmax(C)' : temp_day_high_f, 'Tmin(C)' : temp_day_low_f, 'ET0' : et_day, 'Rain(mm)' : rain_day_in} , ignore_index=True)
        df.set_index('Date',inplace=True)
        df.to_csv(dir_weather,header=True, sep='\t',float_format="%.3f",na_rep='0')

        print('Successful download WeaterLink')
    
    except:
        print("error saving data hourly") 
def combinar_datos():
    try:
        
        dir_weather1='.\Date_Weather_station\Weather_station.csv'    #usa datos del servidor 
        dir_weather2='.\Date_Weather_station\Weather_station_2.csv'  #usa datos de la nueva estacion
        
        df1=pd.read_csv(dir_weather1, sep='\t')
        df2=pd.read_csv(dir_weather2, sep='\t')
        f_in2=df2.loc[0,'Date']
        f_in1=df1.loc[0,'Date']
        df1.set_index('Date',inplace=True)
        df2.set_index('Date',inplace=True)
        df1=df1[f_in1:f_in2]
        df1.reset_index(inplace=True)
        df1=df1=df1[:-1]
        df1.set_index('Date',inplace=True)
        df3=pd.concat([df1,df2])
        df3.to_csv(dir_weather2,header=True, sep='\t',float_format="%.2f",na_rep='0')
    except:
        print('error al unir datos de estaciones ')
def main():
    
    #rutina para actualizar los datos cuando se tiene la tabla completadescargada de la pagina de weatherlink
    # tabla(dir_T)  
    # print('ingresa')
    station()   

    # while True:
    #     Hour = (time.strftime("%X").split(':'))
    #     if Hour[1]=='30' or Hour[1]=='0' or Hour[1]=='00' or Hour[1]=='45' or Hour[1]=='15': 
    #         # print('ingresa al if')
        # print(Hour)
        # time.sleep(60)

    # combinar_datos()
if __name__ == '__main__':

    main()
 
sys.exit(0)        


# https://s3.amazonaws.com/export-wl2-live.weatherlink.com/data/Intelligent_Irrigation_6-9-20_12-00_AM_1_Year_1609020135_v2.csv