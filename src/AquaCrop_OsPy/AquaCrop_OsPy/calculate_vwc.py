# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 20:59:56 2021

@author: Hector Sanabria
"""


import pandas as pd 
from datetime import datetime ,timedelta
from datetime import date

import time 
import sys 
dir_actual='/home/pi/Desktop/RealAgent/src/AquaCrop_OsPy/AquaCrop_OsPy'
dir_weather=dir_actual+'/Date_Weather_station/Weather_station_15m.csv'
out_path =dir_actual+'/Lote'#ruta donde se encuentra el lote

'''
dir_actual='/home/pi/Desktop/IntIrrAgent05292021/AquaCrop_OsPy/AquaCrop_OsPy'
dir_weather=dir_actual+'/Date_Weather_station/Weather_station_15m.csv'
out_path ='/home/pi/Desktop/IntIrrAgent05292021/AquaCrop_OsPy/AquaCrop_OsPy/Lote'#ruta donde se encuentra el lote


dir_actual='.'
dir_weather_cp=dir_actual+'\Date_Weather_station\Weather_station_2.csv'

dir_weather=dir_actual+'\Date_Weather_station\Weather_station_15m.csv'
out_path ='H:\AquaCrop\Aquacrop_Raspberry\Funciona_raspberry\Copia\AquaCrop_OsPy\AquaCrop_OsPy\Lote'#ruta donde se encuentra el lote
'''
# out_vwc='./CalSensorData'
out_vwc='./SensorsData/CalSensorData'



Corn= [25,37,40,30,    0.30,1.2,0.5,   0,0.4572]
Potato= [25,30,36,30,   0.5,1.15,0.75,  0,0.3048]
Tomato= [25,30,30,25,   0.60,1.15,0.8,  0.04,0.3048]
Barley= [40,60,60,40,   0.30,1.15,0.25, 0,0.498]
Wheat= [40,60,60,37,    0.30,1.15,0.4,  0,0.519]
Quinoa= [25,60,60,35,   0.30,1.2,0.5,   0,0.4645]
Onion=[21,42,49,38,    0.40,0.85,0.35, 0.04,0.165]
f_vwc=1
class  calculo_vwc():
    def __init__(self):
        pass
    def f_cropcoeff(self,day,model):
         parameters=[]
         if model=='Corn':
             parameters=Corn
         elif model=='Potato':
             parameters=Potato
         elif model=='Tomato':
             parameters=Tomato
         elif model=='Wheat':
             parameters=Wheat
         elif model=='Barley':
             parameters=Barley
         elif model=='Quinoa':
             parameters=Quinoa
         elif model=='Onion':
             parameters=Onion
     
         d_1=parameters[0]
         d_2=parameters[1]
         d_3=parameters[2]
         d_4=parameters[3]
         Kc_ini=parameters[4]
         Kc_mid=parameters[5]
         Kc_end=parameters[6]
         Kc=0
         if day<=d_1:
             Kc=Kc_ini
         elif day>d_1 and day<= (d_1+d_2):
             m=(Kc_mid-Kc_ini)/d_2
             Kc=m*(day-d_1)+Kc_ini
         elif day>d_1+d_2 and day<= (d_1+d_2+d_3):
             Kc=Kc_mid
         elif day> (d_1+d_2+d_3) and day<= (d_1+d_2+d_3+d_4):
             m=(Kc_end-Kc_mid)/d_4
             Kc=m*(day-(d_1+d_2+d_3))+Kc_mid
         return Kc

    def rootDepth(self, t,cro):
        if cro=='Corn':
            z0=Corn[7]
            zx=Corn[8]
            t0=5
            tx=108
            mad=0.55
        elif cro=='Potato':
            z0=Potato[7]
            zx=Potato[8]
            t0=6
            tx=100
            mad=0.25
        elif cro=='Tomato':
            z0=Tomato[7]
            zx=Tomato[8]
            t0=7
            tx=55
            mad=0.50
        elif cro=='Wheat':
            z0=Wheat[7]
            zx=Wheat[8]
            t0=11
            tx=93
            mad=0.55
        elif cro=='Barley':
            z0=Barley[7]
            zx=Barley[8]
            t0=14
            tx=60
            mad=0.50
        elif cro=='Quinoa':
            z0=Quinoa[7]
            zx=Quinoa[8]
            t0=9
            tx=83
            mad=0.50
        elif cro=='Onion':
            z0=Onion[7]
            zx=Onion[8]
            t0=7
            tx=105
            mad=0.25
                   
        nn=1
        z=z0+(zx-z0) *(((t-(t0/2))/(tx-(t0/2)))**(1/nn))  
        z=z.real
           
        if z>=zx:
            z=zx
        elif z<=0:
            z=0.0001
        return z,mad
    
    def hour_irr(self,h1,h2,h_irr):
        if h1>= h_irr and h2<= h_irr:
            
            print('esta en el transcurso de tiempo')
            #leer aachivo de riego si esta dentro del rago de horas agrega el riego 
            irr=True 
        else:
            irr=False
        return irr    
    def calcular_vwc_L2(self,L,vwc_1):
        # with open(out_vwc+'1.txt','r',errors='ignore') as fin:
        #     a = fin.read().splitlines(True)
        # So=float(a[len(a)-1].split('\t')[3])
        
        # So=vwc_1/100
        So=vwc_1
        A = float(-0.02897)
        B = float(-0.00040329)
        Sc = float( 0.01099)
        L = L/1000
        # L=0.5
        wc_2= A*L +(So*(1+B*(L**2)))+Sc
        # wc_2=wc_2*100
#         print(L , wc_2)
        
        return round(wc_2,3)
   
    def calcular_vwc(self,Lv,deple,rain,irr,etc,Fc,L):
        if deple == -999:
            with open(out_vwc+Lv+'.txt','r',errors='ignore') as fin:
                a = fin.read().splitlines(True)
            depl_1=a[len(a)-1].split('\t')
            depl_1=float(depl_1[2])
        else:
            depl_1=deple
        # print('depl e un timepo anterior',depl_1)
        if str(depl_1)=='nan' :
            depl_1=0
        if str(rain)=='nan':
            rain=0
        if str(irr)=='nan':
            irr=0
        if str(etc)=='nan':
            etc=0
        if str(Fc)=='nan':
            Fc=0
        if str(L)=='nan':
            L=0
        # if n==1:
        #     depl_1=((Fc-vwc_1)/100)*L1
        # else:
        #     depl_1=((Fc-vwc_1)/100)*(L-root)            
        depl=depl_1-rain-irr+etc
        # if depl<0:
        #     depl=0
        vwc= Fc-((depl/L)*100)
        return round(depl,3),round(vwc,3),round(depl_1,3),Fc
    #vwc_15m(self,Lv,porcentaje del tratamiento)
    
    def pres_to_mm(self,pres,Rate,area,Ef):
        irr_area=pres/(Rate/100)
        irr_pres_gross= irr_area/area
        irr=irr_pres_gross * Ef  #irr_pres_net
        return round(irr,3)
    
    def vwc_15m(self,Lv,Rate):
        Rate=float(Rate)
        try:
            df_send=pd.read_csv(out_path+'/Agent_Better.csv',sep='\t')
        except:
            df_send=pd.read_csv(out_path+'\Agent_Better.csv',sep='\t')

        with open(out_path+'/Parameters.txt','r',errors='ignore') as fin:
            data = fin.read().splitlines(True)
        crop=data[13].split()[1]
        crop=crop[:-4]
        fc1010=float(data[8].split()[1])
        pwp1010=float(data[9].split()[1])
        fc1020=float(data[27].split()[1])
        sat=float(data[7].split()[1])
        pwp1020=float(data[28].split() [1])         
        L1=round(float(data[25].split()[1])*1000,3)
        L2=round(float(data[26].split()[1])*1000,3)
        
        timeacq=time.asctime()
        hour=str(time.strftime("%H:%M:%S"))
        date=str(time.strftime("%Y-%m-%d"))
        SEED_TIME=data[15].split()[1]
    #lee datos estacion
    # def vwc_15m(self,Lv,len_data):

    #     df1=pd.read_csv(dir_weather_cp, sep='\t')
    #     df1=df1[:len_data]
    #     df1.to_csv(dir_weather,header=True, sep='\t',float_format="%.2f",na_rep='0',index=False)
        with open(dir_weather,'r',errors='ignore') as fin:
            
    #    with open(dir_weather_cp,'r',errors='ignore') as fin:
            a = fin.read().splitlines(True)
        t1=a[len(a)-1].split('\t')
        t2=a[len(a)-2].split('\t')
        h1 = datetime.strptime(t1[0]+" "+t1[1], "%Y-%m-%d %H:%M:%S")   #un timpo anterior 
        h2 = datetime.strptime(t2[0]+" "+t2[1], "%Y-%m-%d %H:%M:%S")    #dos tiempos anteriores
        # h_irr = datetime.strptime(t2[0]+" "+t2[1], "%Y-%m-%d %H:%M:%S")    #dos tiempos anteriores
        day=str(time.strftime("%Y-%m-%d"))
        h_depl = datetime.strptime(day+' 00:10:00', "%Y-%m-%d %H:%M:%S")    
        h_irr = datetime.strptime(day+' 12:10:00', "%Y-%m-%d %H:%M:%S")    
        
        #semi autommatico         
        with open('./Prescription/SemiAutompres.txt','r',errors='ignore') as fin:
            a = fin.read().splitlines(True)
        h_Semi=a[len(a)-1].split(' ')
        
        #semi autommatico         
        with open('./Prescription/Manualpres.txt','r',errors='ignore') as fin:
            a = fin.read().splitlines(True)
        h_Manual=a[len(a)-1].split(' ')
        #semi autommatico         
        with open('./Prescription/Autopres.txt','r',errors='ignore') as fin:
            a = fin.read().splitlines(True)
        h_Auto=a[len(a)-1].split(' ')
        
       
        fecha1 = datetime.strptime(SEED_TIME, "%Y-%m-%d")
        a=str(fecha1 + timedelta(days=int(h_Semi[0])))
        h_Semi[0]=a.split(' ')[0]
        aux_Manual=h_Manual[0].split('/')
        h_Manual[0]=aux_Manual[2]+'-'+aux_Manual[1]+'-'+aux_Manual[0]
        aux_auto=h_Auto[0].split('/')
        h_Auto[0]='20'+aux_auto[2]+'-'+aux_auto[1]+'-'+aux_auto[0]
        h_irr1 = datetime.strptime(h_Semi[0]+' '+h_Semi[1], "%Y-%m-%d %H:%M:%S")    
        h_irr2 = datetime.strptime(h_Manual[0]+' '+h_Manual[1], "%Y-%m-%d %H:%M:%S")    
        h_irr3 = datetime.strptime(h_Auto[0]+' '+h_Auto[1], "%Y-%m-%d %H:%M:%S")
        irr1 = self.hour_irr(h1,h2,h_irr1)
        irr2 = self.hour_irr(h1,h2,h_irr2)
        irr3 = self.hour_irr(h1,h2,h_irr3)
        soilparam=open('./Parameters/SoilConfparameters.txt','r')
        linespar =soilparam.read().splitlines()
        last_linepar=linespar[-1]
        d=last_linepar.split(' ')
        pwp1010=float(d[2])
        fc1010=float(d[3])        
        pwp1020=float(d[4])        
        fc1020=float(d[5])
        L1=round(float(d[6])*1000,3)
        L2=round(float(d[7])*1000,3)
        A1=float(d[8])
        A2=float(d[9])        
        A3=float(d[10])        
        A4=float(d[11])        
        D1=float(d[12])        
        D2=float(d[13])        
        D3=float(d[14])        
        D4=float(d[15])        
        Dis1=float(d[16])        
        Dis2=float(d[17])        
        Dis3=float(d[18])        
        Dis4=float(d[19])         
        Ef=float(d[20])            
        soilparam.close()
        
        if irr1 == True:
            pres=float(h_Semi[2]) #prescription
            irr=self.pres_to_mm(pres,Rate,A1,Ef)
            
        elif irr2 == True:
#             irr=h_Manual[]
            pres=float(h_Manual[2]) #prescription
            irr=self.pres_to_mm(pres,Rate,A1,Ef)
        elif irr3 == True:
#             irr= h_Auto[]
            pres=float(h_Auto[2]) #prescription
            irr=self.pres_to_mm(pres,Rate,A1,Ef)
        else:
            irr=0
            
        dh = h1-h2
        
        d_et0=round(float(t1[4])-float(t2[4]),3)
        d_rain=round(float(t1[5])-float(t2[5]),3)
        if d_et0<0:
            d_et0=0
        if d_rain<0:
            d_rain=0

        # if dh.days==0 and str(dh).find('0:15')>=0:
        #     d_et0=float(t1[4])-float(t2[4])
        #     d_rain=float(t1[5])-float(t2[5])
        #     print('calcula')
            
        # else:
        #     d_rain=0
        #     d_et0=0

        # param=open('./Parameters/ETparametersAuto.txt','r')
        # linespar =param.read().splitlines()
        date1=datetime.strptime(SEED_TIME, "%Y-%m-%d")
        date2=datetime.strptime(date, "%Y-%m-%d")
        delta=abs(date2-date1)
        j=delta.days

        Kc=self.f_cropcoeff(j,crop)
        root_depth,Mae=self.rootDepth(j,crop)  
        CONT_DAYS,CONT_WEEK,root_depth = j,int(j/7)+1,round(root_depth*1000,3)
                
        
        if h1>= h_depl and h2<= h_depl:
            # print('esta en el transcurso de tiempo')
            #leer aachivo de riego si esta dentro del rago de horas agrega el deplecion   
            # deple=round(df_send['depl'][j],3)
            # if Lv=='1':
            #     vwc=round(df_send['WC1'][j],3)
            # else:
            #     vwc=round(df_send['WC2'][j],3)
            # deple=((fc1010-vwc)/100)*L1
            # print('Calcula deple con WC1 ',deple)
            deple=-999

        else:
            deple=-999

       
        # irr=4
        etc=round(d_et0*Kc,3)
        # print('d_et0',d_et0)
        # print('d_rain',d_rain,'irr',irr,'etc',etc,'fc1010',fc1010,'L',L1)
        if Lv=='1':            
            depl,vwc_1,depl_1,Fc=self.calcular_vwc(Lv,deple,d_rain,irr,etc,fc1010,L1)
            if vwc_1 >= float(sat):
                vwc_1=sat
                depl=float(fc1010)-float(sat)

            # depl_1=0 #deplecion anterior
            # out=open('./SensorsData/CalSensorData1.txt', 'w',errors='ignore')
    #         out=open(out_vwc+'1.txt', 'w',errors='ignore')
            out=open(out_vwc+Lv+'.txt', 'a',errors='ignore')
            # out.write("data\thour\tdepl\tvwc\tdepl_t1\td_rain\tirr\tetc\tFc\tL\n")
            out.write(str(t1[0])+'\t'+str(t1[1])+'\t'+str(depl)+'\t'+str(vwc_1)+'\t'+str(depl_1)+'\t'+str(d_rain)+'\t'+str(irr)+'\t'+str(etc)+'\t'+str(Fc)+'\t'+str(L1)+'\n')
            out.close()
#             print('WC1\t',vwc_1)

        else:
            f=0.3
            depl,vwc_1,depl_1,Fc=self.calcular_vwc(Lv,deple,d_rain*f,irr*f,etc*f,fc1010,L2)
            vwc_2 = self.calcular_vwc_L2(L2,vwc_1)
            if vwc_2 >= float(sat):
                vwc_2=sat            
                depl=float(fc1010)-float(sat)

            # vwc_2 = self.calcular_vwc_L2(L2)

            # depl_1=0 #deplecion anterior
            # out=open('./SensorsData/CalSensorData1.txt', 'w',errors='ignore')
    #         out=open(out_vwc+'1.txt', 'w',errors='ignore')
            out=open(out_vwc+Lv+'.txt', 'a',errors='ignore')
            # out.write("data\thour\tdepl\tvwc\tdepl_t1\td_rain\tirr\tetc\tFc\tL\tvwc2\n")
            out.write(str(t1[0])+'\t'+str(t1[1])+'\t'+str(depl)+'\t'+str(vwc_1)+'\t'+str(depl_1)+'\t'+str(d_rain)+'\t'+str(irr)+'\t'+str(etc)+'\t'+str(Fc)+'\t'+str(L1)+'\t'+str(vwc_2)+'\n')
            out.close()
#             print('WC2\t',vwc_2)


# 
# def main():
#     calculo_vwc().vwc_15m('1','100')
#     calculo_vwc().vwc_15m('2','100')
# if __name__ == '__main__':
#     main()
#  
# sys.exit(0)