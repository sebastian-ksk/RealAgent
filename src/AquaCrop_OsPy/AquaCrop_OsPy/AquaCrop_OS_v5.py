
import os
import pandas as pd
from datetime import datetime, timedelta
# from aquacrop.classes import    *
# from aquacrop.core import       *
import subprocess,os
import math
import time



'''
path_py=os.getcwd()
Para_Potato={'CropType ':'2', 'CalendarType ':'1', 'SwitchGDD ':'0', 'PlantingDate ':'01/03', 'HarvestDate ':'01/08', 'Emergence ':'15', 'MaxRooting ':'50', 'Senescence ':'105', 'Maturity ':'125', 'HIstart ':'46', 'Flowering ':'-999', 'YldForm ':'77', 'GDDmethod ':'3', 'Tbase ':'2', 'Tupp ':'26', 'PolHeatStress ':'0', 'Tmax_up ':'-999', 'Tmax_lo ':'-999', 'PolColdStress ':'0', 'Tmin_up ':'-999', 'Tmin_lo ':'-999', 'BioTempStress ':'0', 'GDD_up ':'7', 'GDD_lo ':'0', 'fshape_b ':'13.8135', 'PctZmin ':'70', 'Zmin ':'0.3', 'Zmax ':'0.6', 'fshape_r ':'1.5', 'fshape_ex ':'-6', 'SxTopQ ':'0.048', 'SxBotQ ':'0.012', 'a_Tr ':'1', 'SeedSize ':'15', 'PlantPop ':'40000', 'CCmin ':'0.05', 'CCx ':'0.92', 'CDC ':'0.01884', 'CGC ':'0.126', 'Kcb ':'1.1', 'fage ':'0.15', 'WP ':'18', 'WPy ':'100', 'fsink ':'0.5', 'bsted ':'0.000138', 'bface ':'0.001165', 'HI0 ':'0.85', 'HIini ':'0.01', 'dHI_pre ':'2', 'a_HI ':'0', 'b_HI ':'10', 'dHI0 ':'5', 'Determinant ':'0', 'exc ':'0', 'MaxFlowPct ':'33.33', 'p_up1 ':'0.2', 'p_up2 ':'0.6', 'p_up3 ':'0.7', 'p_up4 ':'0.8', 'p_lo1 ':'0.6', 'p_lo2 ':'1', 'p_lo3 ':'1', 'p_lo4 ':'1', 'fshape_w1 ':'3', 'fshape_w2 ':'3', 'fshape_w3 ':'3', 'fshape_w4 ':'0', 'ETadj ':'1', 'Aer ':'5', 'LagAer ':'3', 'beta ':'12', 'GermThr ':'0.2', 'GermThr ':'0.2'}
out_path ='./Lote'#ruta donde se encuentra el lote
path_AQ_os='/home/pi/Desktop/IntIrrAgent05292021/AquaCrop_OsPy/AquaCropOS_v50a'
# path_AQ_os='H:/AquaCrop/Aquacrop_Raspberry/aquacropos_v60a/AquaCropOS_v50a'
# out_path='H:/Lotes/Holanda_PumpStation/Holanda1'
# irr=[83.64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19.41, 6.17, 4.41, 8.1, 4.71, 5.77, 3.24, 2.69, 2.16, 2.9, 2.46, 2.37, 4.58, 4.26, 6.35, 5.56, 7.58, 8.53, 5.42, 6.29, 7, 0, 0.57, 0, 0, 0, 0, 0.98, 0, 2.33, 2.6, 3.41, 1.53, 0, 2.05, 0, 0, 0, 2.26, 3.38, 4.19, 2.71, 3.57, 4.22, 3.69, 3.47, 3.06, 2.82, 1.25, 1.32, 3.05, 2.34, 3.7, 0, 0, 2.76, 4.24, 2.28, 2.07, 1.98, 3.37, 3.81, 3.37, 3.37, 2.5, 2.94, 3.15, 3.91, 3.25, 0, 2.95, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
dir_weather='./Date_Weather_station/Weather_station_2.csv'
'''

###
path_py=os.getcwd()
Para_Potato={'CropType ':'2', 'CalendarType ':'1', 'SwitchGDD ':'0', 'PlantingDate ':'01/03', 'HarvestDate ':'01/08', 'Emergence ':'15', 'MaxRooting ':'50', 'Senescence ':'105', 'Maturity ':'125', 'HIstart ':'46', 'Flowering ':'-999', 'YldForm ':'77', 'GDDmethod ':'3', 'Tbase ':'2', 'Tupp ':'26', 'PolHeatStress ':'0', 'Tmax_up ':'-999', 'Tmax_lo ':'-999', 'PolColdStress ':'0', 'Tmin_up ':'-999', 'Tmin_lo ':'-999', 'BioTempStress ':'0', 'GDD_up ':'7', 'GDD_lo ':'0', 'fshape_b ':'13.8135', 'PctZmin ':'70', 'Zmin ':'0.3', 'Zmax ':'0.6', 'fshape_r ':'1.5', 'fshape_ex ':'-6', 'SxTopQ ':'0.048', 'SxBotQ ':'0.012', 'a_Tr ':'1', 'SeedSize ':'15', 'PlantPop ':'40000', 'CCmin ':'0.05', 'CCx ':'0.92', 'CDC ':'0.01884', 'CGC ':'0.126', 'Kcb ':'1.1', 'fage ':'0.15', 'WP ':'18', 'WPy ':'100', 'fsink ':'0.5', 'bsted ':'0.000138', 'bface ':'0.001165', 'HI0 ':'0.85', 'HIini ':'0.01', 'dHI_pre ':'2', 'a_HI ':'0', 'b_HI ':'10', 'dHI0 ':'5', 'Determinant ':'0', 'exc ':'0', 'MaxFlowPct ':'33.33', 'p_up1 ':'0.2', 'p_up2 ':'0.6', 'p_up3 ':'0.7', 'p_up4 ':'0.8', 'p_lo1 ':'0.6', 'p_lo2 ':'1', 'p_lo3 ':'1', 'p_lo4 ':'1', 'fshape_w1 ':'3', 'fshape_w2 ':'3', 'fshape_w3 ':'3', 'fshape_w4 ':'0', 'ETadj ':'1', 'Aer ':'5', 'LagAer ':'3', 'beta ':'12', 'GermThr ':'0.2', 'GermThr ':'0.2'}
dic_parameters={"CODE":"Tibasosa1",	"LAT":"5.78291",	"LON":"-73.1047",	"AREA":"7841.31",	"CLAY":"26.72",	"SILT":"54.61",	"SAND":"18.19",	"SP":"58.95",	"FC1010":"46.373",	"PWP1010":"26.013",	"HC":"1.07",	"DENSITY":"1.14",	"TYPE SOIL":"SiltLoam",	"CROP":"Potato.CRO",	"MODEL":"BETTER",	"SEEDTIME":"44261",	"DAYS_CROP":"121",	"PRESCRIPTION":"0",	"Ks":"0",	"DAY_START":"0",	"WEEK":"0",	"Kc":"NaN",	"root depth":"NaN",	"TAW":"NaN",	"MAE":"NaN",	"L1":"0.1",	"L2":"0.1",	"FC1020":"45.737",	"PWP1020":"25.47"}
#rutas agente real 
out_path ='/home/pi/Desktop/RealAgent/src/AquaCrop_OsPy/AquaCrop_OsPy/Lote'#ruta donde se encuentra el lote
path_AQ_os='/home/pi/Desktop/RealAgent/src/AquaCrop_OsPy/AquaCropOS_v50a' #Agente real 1  
dir_weather='/home/pi/Desktop/RealAgent/src/AquaCrop_OsPy/AquaCrop_OsPy/Date_Weather_station/Weather_station_2.csv'


'''
out_path ='/home/pi/Desktop/IntIrrAgent05292021/AquaCrop_OsPy/AquaCrop_OsPy/Lote'#ruta donde se encuentra el lote
path_AQ_os='/home/pi/Desktop/IntIrrAgent05292021/AquaCrop_OsPy/AquaCropOS_v50a'
dir_weather='/home/pi/Desktop/IntIrrAgent05292021/AquaCrop_OsPy/AquaCrop_OsPy/Date_Weather_station/Weather_station_2.csv'
'''
Corn= [25,37,40,30,    0.30,1.2,0.5,   0,0.4572] # days, crop_cofficient, root_depth
Potato= [25,30,36,30,   0.5, 1.15, 0.75,  0,0.3048]
Tomato= [25,30,30,25,   0.60,1.15,0.8,  0.04,0.3048]
Barley= [40,60,60,40,   0.30,1.15,0.25, 0,0.498]
Wheat= [40,60,60,37,    0.30,1.15,0.4,  0,0.519]
Quinoa= [25,60,60,35,   0.30,1.2,0.5,   0,0.4645]
Onion=[21,42,49,38,    0.40,0.85,0.35, 0.04,0.165]

class AquaCrop_os():
    def __init__(self,cropModel):
#         print('Aquacrop OS')
        self.cropModel = cropModel
        self.parameters()
        pass

    def parameters(self):
        print('ingresa a editar parametros')

        SEEDTIME=self.cropModel.seedTime 
        CROP=self.cropModel.typeCrop 
        
        PWP1010=float(self.cropModel.pointWp )
        PWP1020=float(self.cropModel.pointWp )
        FC1010=float(self.cropModel.FieldCap )
        FC1020=float(self.cropModel.FieldCap )

        DAYS_CROP=float(self.cropModel.dayscrop )
        WEEK= (DAYS_CROP/7) +1


        with open(out_path+'/Parameters.txt', 'r',errors='ignore') as fin:
            data = fin.read().splitlines(True)
        for clave, valor in dic_parameters.items():
            # print(clave, valor)
            cnt=0
            for linea in data:

                if linea.find('FC1010')==0 :
                    data[cnt]='FC1010\t'+FC1010+'\n'
                if linea.find('PWP1010')==0 :
                    data[cnt]='PWP1010\t'+PWP1010+'\n'
                if linea.find('FC1020')==0 :
                    data[cnt]='FC1020\t'+FC1020+'\n'
                if linea.find('PWP1020')==0 :
                    data[cnt]='PWP1020\t'+PWP1020+'\n'  

                if linea.find('CROP')==0 :
                    data[cnt]='CROP\t'+CROP+'\n'

                if linea.find('SEEDTIME')==0 :
                    data[cnt]='SEEDTIME\t'+SEEDTIME+'\n'
                if linea.find('DAYS_CROP')==0 :
                    data[cnt]='DAYS_CROP\t'+DAYS_CROP+'\n'
                if linea.find('WEEK')==0 :
                    data[cnt]='WEEK\t'+WEEK+'\n'

                elif linea.find(clave)==0:
                    data[cnt]= clave+'\t'+valor+'\n'
                    break
                cnt+=1

        path=out_path+'/Parameters.txt'
        out=open(path, 'w',errors='ignore')  
        for linea in data:
            out.write(linea)            
        out.close()
        print('sale de editar')



    def EditClock(self,path_AQ_os,SEED_TIME,T_day):
        SEED_TIME=datetime.strptime(SEED_TIME, "%Y-%m-%d")
        day_end=SEED_TIME+ timedelta(days=T_day)
        path1=path_AQ_os+'/Input/Clock.txt'
        #exribe los datos
        out=open(path1, 'w',errors='ignore')    
        #version 5
        out.write('%% ---------- Clock parameter inputs for AquaCropOS ---------- %%\n')
        out.write('%% Simulation start time (yyyy-mm-dd) %%\n')
        out.write('SimulationStartTime : '+str(SEED_TIME)[:10]+'\n')
        out.write('%% Simulation end time (yyyy-mm-dd) %%\n')
        out.write('SimulationEndTime : '+str(day_end)[:10]+'\n')
        out.write('%% Simulate off-season (N or Y) %%\n')
        out.write('OffSeason : N        \n')
        out.close()
#         print('Config Clock.txt')
        return
    def EditSoil(self,path_AQ_os,cro,Sat1010,fc1010,pwp1010,Ksat1010):
        
        if cro[:-4]=='Maize':
            root_max=[0.23,0.46,0.69,0.92,2.30]
            Dz=[0.23,0.23,0.23,0.23,1.38]

        elif cro[:-4]=='Potato':
            root_max=[0.15,0.30,0.45,0.61,1.50]
            Dz=[0.15,0.15,0.15,0.15,0.90]

        elif cro[:-4]=='Tomato':
            root_max=[0.15,0.30,0.45,0.60,1.00]
            Dz=[0.15,0.15,0.15,0.14,0.40]

        elif cro[:-4]=='Wheat':
            root_max=[0.26,0.52,0.78,1.04,1.50]
            Dz=[0.26,0.26,0.26,0.26,0.46]

        elif cro[:-4]=='Barley':
            root_max=[0.25,0.50,0.75,1.,1.30]
            Dz=[0.25,0.25,0.25,0.25,0.30]

        elif cro[:-4]=='Quinoa':
            root_max=[0.23,0.46,0.69,0.92,1.00]
            Dz=[0.23,0.23,0.23,0.23,0.08]
           
        elif cro[:-4]=='Onion':
            root_max=[0.10,0.20,0.20,0.20,0.20]
            Dz=[0.10,0.10,0.0,0.00,0.00]
       
        #version 5    
        path=path_AQ_os+'/Input/Soil.txt'
        out=open(path, 'w',errors='ignore')      
        out.write('%% ---------- Soil parameter inputs for AquaCropOS ---------- %%\n')
        out.write('%% Soil profile filename %%\n')
        out.write('SoilProfile.txt\n')
        out.write('%% Soil textural properties filename %%\n')
        out.write('N/A\n')
        out.write('%% Soil hydraulic properties filename %%\n')
        out.write('SoilHydrology.txt\n')
        out.write('%% Calculate soil hydraulic properties (0: No, 1: Yes) %%\n')
        out.write('CalcSHP : 0\n')
        out.write('%% Total thickness of soil profile (m) %%\n')
        out.write('zSoil : '+str(root_max[4])+'\n')
        out.write('%% Total number of compartments %%\n')
        out.write('nComp : 12\n')
        out.write('%% Total number of layers %%\n')
        out.write('nLayer : 1\n')
        out.write('%% Thickness of soil surface skin evaporation layer (m) %%\n')
        out.write('EvapZsurf : 0.04\n')
        out.write('%% Minimum thickness of full soil surface evaporation layer (m) %%\n')
        out.write('EvapZmin : 0.15\n')
        out.write('%% Maximum thickness of full soil surface evaporation layer (m) %%\n')
        out.write('EvapZmax : 0.30\n')
        out.write('%% Maximum soil evaporation coefficient %%\n')
        out.write('Kex : 1.1\n')
        out.write('%% Shape factor describing reduction in soil evaporation %%\n')
        out.write('fevap : 4\n')
        out.write('%% Proportional value of Wrel at which soil evaporation layer expands %%\n')
        out.write('fWrelExp : 0.4\n')
        out.write('%% Maximum coefficient for soil evaporation reduction due to sheltering effect of withered canopy %%\n')
        out.write('fwcc : 50\n')
        out.write('%% Adjust default value for readily evaporable water (0: No, 1: Yes) %%\n')
        out.write('AdjREW : 0\n')
        out.write('%% Readily evaporable water (mm) (only used if adjusting) %%\n')
        out.write('REW : 9\n')
        out.write('%% Adjust curve number for antecedent moisture content (0:No, 1:Yes) %%\n')
        out.write('AdjCN : 1\n')
        out.write('%% Curve number %%\n')
        out.write('CN : 72\n')
        out.write('%% Thickness of soil surface (m) used to calculate water content to adjust curve number %%\n')
        out.write('zCN : 0.3\n')
        out.write('%% Thickness of soil surface (m) used to calculate water content for germination %%\n')
        out.write('zGerm : 0.3\n')
        out.write('%% Depth of restrictive soil layer (set to negative value if not present) %%\n')
        out.write('zRes : -999\n')
        out.write('%% Capillary rise shape factor %%\n')
        out.write('fshape_cr : 16\n')
        out.close()          
       
        path=path_AQ_os+'/Input/SoilHydrology.txt'

        out=open(path, 'w',errors='ignore')  
        out.write('%% ------------- Soil hydraulic properties for AquaCropOS -------------- %%\n')
        out.write('%%Layer    Thickness(m)    thS(m3/m3)    thFC(m3/m3)    thWP(m3/m3)    Ksat(mm/day)    %%\n')
        out.write('1        '+str(root_max[4])+'             '+str(float(Sat1010)/100)+'         '+str(float(fc1010)/100)+'           '+str(float(pwp1010)/100)+'           '+str( float(Ksat1010)*240)+'\n')
        # out.write('1        '+str(root_max[1])+'             '+str(float(Sat1010)/100)+'         '+str(float(fc1010)/100)+'           '+str(float(pwp1010)/100)+'           '+str( float(Ksat1010)*240)+'\n')
        # out.write('1        '+str(root_max[2])+'             '+str(float(Sat1010)/100)+'         '+str(float(fc1010)/100)+'           '+str(float(pwp1010)/100)+'           '+str( float(Ksat1010)*240)+'\n')
        # out.write('1        '+str(root_max[3])+'             '+str(float(Sat1010)/100)+'         '+str(float(fc1010)/100)+'           '+str(float(pwp1010)/100)+'           '+str( float(Ksat1010)*240)+'\n')
        # out.write('1        '+str(root_max[4])+'             '+str(float(Sat1010)/100)+'         '+str(float(fc1010)/100)+'           '+str(float(pwp1010)/100)+'           '+str( float(Ksat1010)*240)+'\n')
        # out.close()
       

#         print('Config SoilProfile.txt')
#         print('Config SoilHydrology.txt')
        return    
    def EditWeatherInput(self,path_AQ_os,out_path,p,n):
        Tmin=10
        Tmax=20
        ET0=2.5
        #edita
        df_a=pd.read_csv(out_path+'/'+p +'.csv', sep='\t')
        df_w=pd.DataFrame()
        df_w=df_w.fillna(0)
        df_a['Date'] = pd.to_datetime(df_a['Date'])
        df_w ['Day'] = df_a['Date'].dt.day
        df_w ['Month'] = df_a['Date'].dt.month
        df_w ['Year'] = df_a['Date'].dt.year

        ceros=[0]*(len(df_a)-n-1)
        df_w ['Tmin(C)']=list(df_a['Tmin(C)'][:n+1])+ceros
        df_w ['Tmax(C)']=list(df_a['Tmax(C)'][:n+1])+ceros
        df_w ['Prcp(mm)']=list(df_a['Rain(mm)'][:n+1])+ceros
        df_w ['Et0(mm)']=list(df_a['ET0'][:n+1])+ceros

       
        # df_w ['Tmin(C)'] = df_a['Tmin(C)']    
        # df_w ['Tmax(C)'] = df_a['Tmax(C)']
        # df_w ['Prcp(mm)'] =df_a['Rain(mm)']
        # df_w ['Et0(mm)'] = df_a['ET0']

        #remplaza los valores de cero por valores promedio
        df_w['Tmin(C)']=df_w['Tmin(C)'].replace([0], [Tmin])
        df_w['Tmax(C)']=df_w['Tmax(C)'].replace([0], [Tmax])
        df_w['Et0(mm)']=df_w['Et0(mm)'].replace([0], [ET0])
        rain_T=sum(df_w ['Prcp(mm)'])
       
         
        #version 5
        df_w.to_csv(path_AQ_os+'/Input/Weather.txt',header=False, sep='\t',float_format="%.2f",na_rep='0',index=False)
       
        with open(path_AQ_os+'/Input/Weather.txt', 'r',errors='ignore') as fin:
            data = fin.read().splitlines(True)
       
        out=open(path_AQ_os+'/Input/Weather.txt', 'w',errors='ignore')  
        out.write('%% ---------- Weather input time-series for AquaCropOS ---------- %%\n')
        out.write('%% Day Month Year MinTemp MaxTemp Precipitation ReferenceET %%\n')
        for linea in data:
            out.write(linea)            
        out.close()

#         print('Config Weather.txt')
        return rain_T

    def EditCropInput(self,path_AQ_os,out_path,p,crop,SEED_TIME,T_day):
        # SEED_TIME='2015-05-01'
        SEED_T=datetime.strptime(SEED_TIME, "%Y-%m-%d")
        day_end=SEED_T+ timedelta(days=T_day-1)
        D_T=str(day_end)[:-9]
        D_T=D_T.split('-')
        md=str(D_T[1])
        dd=str(D_T[2])
#         print(md+'/'+dd)
        S_T=SEED_TIME.split('-')
        ms=str(S_T[1])
        ds=str(S_T[2])
       
        path=path_AQ_os+'/Input/CropMix.txt'
        out=open(path, 'w',errors='ignore')    
        out.write('%% ---------- Crop mix options for AquaCropOS ---------- %%\n')
        out.write('%% Number of crop options %%\n')
        out.write('1\n')
        out.write('%% Specified planting calendar %%\n')
        out.write('N\n')
        out.write('%% Crop rotation filename %%\n')
        out.write('CropRotation.txt\n')
        out.write('%% Information about each crop type %%\n')
        out.write('%% CropType, CropFilename, IrrigationFilename %%\n')
        out.write(crop[:-4]+', Crop.txt, IrrigationManagement.txt\n')
        # out.write('arracaha, Crop.txt, IrrigationManagement.txt\n')
        out.close()
        path1=path_AQ_os+'/Input/Crop.txt'
        # SEED_TIME='2015-05-01'
       
        SEED_TIME=datetime.strptime(SEED_TIME, "%Y-%m-%d")
#         print(str(SEED_TIME.day)+'/'+str(SEED_TIME.month))
        with open(path1, 'r',errors='ignore') as fin:
            data = fin.read().splitlines(True)
        # print(len(data))
        for clave, valor in Para_Potato.items():
            # print(clave, valor)
            cnt=0
            for linea in data:
                if linea.find('PlantingDate :')==0 :
                    #Planting Date (dd/mm)
                    data[cnt]='PlantingDate : '+ds+'/'+ms+'\n'
                elif linea.find('HarvestDate :')==0 :
                    # Harvest Date (dd/mm)
                    data[cnt]='HarvestDate : '+dd+'/'+md+'\n'
                elif linea.find(clave+':')==0:
                    data[cnt]= clave+': '+valor+'\n'
                    break
                cnt+=1
        path=path_AQ_os+'/Input/Crop.txt'
        out=open(path, 'w',errors='ignore')  
        for linea in data:
            out.write(linea)            
        out.close()
       
        path=path_AQ_os+'/Input/InitialWaterContent.txt'
        out=open(path, 'w',errors='ignore')            
        out.write('%% ---------- Initial soil water content for AquaCropOS ---------- %%\n')
        out.write('%% Type of value (Prop (i.e. WP/FC/SAT), Num (i.e. XXX m3/m3), Pct (i.e. % TAW)) %%\n')
        out.write('Prop\n')
        out.write('%% Method (Depth: Inteprolate depth points; Layer: Constant value for each soil layer) %%\n')
        out.write('Layer\n')
        out.write('%% Number of input points (NOTE: Must be at least one point per soil layer) %%\n')
        out.write('1\n')
        out.write('%% Input data points (Depth/Layer   Value) %%\n')
        out.write('1 FC\n')
        out.close()
       

#         print('Config Weather.txt')
        return
    def Edit_Irr(self,path_AQ_os,out_path,p,T_day):
        path=path_AQ_os+'/Input/IrrigationManagement.txt'
        cnt=0
        with open(path, 'r',errors='ignore') as fin:
            data = fin.read().splitlines(True)
        # print(len(data))

        for linea in data:
#             print(cnt)
#             print(cnt,linea)
            if linea.find('IrrMethod :')==0:
                data[cnt]= 'IrrMethod : 3\n'
            elif linea.find('SMT1 :')==0:
                data[cnt]= 'SMT1 : 75\n'
            elif linea.find('SMT2 :')==0:
                data[cnt]= 'SMT2 : 75\n'
            elif linea.find('SMT3 :')==0:
                data[cnt]= 'SMT3 : 75\n'
            elif linea.find('SMT4 :')==0:
                data[cnt]= 'SMT4 : 75\n'

            elif linea.find('AppEff :')==0:
                data[cnt]= 'AppEff : 90\n'#por defecto en 90
            elif linea.find('WetSurf :')==0:
                data[cnt]= 'WetSurf : 100\n'#por defecto 100
               

            cnt+=1
        out=open(path, 'w',errors='ignore')  
        for linea in data:
            out.write(linea)            
        out.close()

        ##edita el riego
        df_a=pd.read_csv(out_path+'/'+p +'.csv', sep='\t')
        df_w=pd.DataFrame()
        df_w=df_w.fillna(0)

        df_a['Date'] = pd.to_datetime(df_a['Date'])
        df_w ['Day'] = df_a['Date'][:T_day].dt.day
        df_w ['Month'] = df_a['Date'][:T_day].dt.month
        df_w ['Year'] = df_a['Date'][:T_day].dt.year
        # df_w ['Depth'] = irr[:T_day]
        df_w ['Depth'] = df_a['Irrigation(mm)'][:T_day]
        # H:\AquaCrop\Aquacrop_Raspberry\aquacropos_v60a\AquaCropOS_v50a\Input
        path=path_AQ_os+'/Input/IrrigationSchedule.txt'
#         print(path)
        df_w.to_csv(path,header=False, sep='\t',float_format="%.2f",na_rep='0',index=False)

        with open(path, 'r',errors='ignore') as fin:
            data = fin.read().splitlines(True)
        out=open(path, 'w',errors='ignore')  
        out.write('%% -------- Irrigation schedule time-series for AquaCropOS -------- %%\n')
        out.write('%% Day Month Year Irrigation(mm) %%\n')
        for linea in data:
            out.write(linea)            
        out.close()
#         print('IrrigationManagement')
        return df_w    

    def RunModel(self):
        os.chdir(path_AQ_os)
#         print('Entra subproces')
#         subprocess.Popen(["octave","AquaCropOS_RUN.m"])
        p = subprocess.run(["octave","AquaCropOS_RUN.m"], stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        os.chdir(path_py)
        print(p)
        time.sleep(5)

#         while p.stdout!=b'Run AquaCrop\n':
#                time.sleep(3)
#                print('Error Ejecutando Octave')
#                pass
        CropGrowth=pd.read_csv(path_AQ_os+'/Output/Sample_CropGrowth.txt',sep='\t')
        FinalOutput=pd.read_csv(path_AQ_os+'/Output/Sample_FinalOutput.txt',sep='\t')
        WaterContents=CropGrowth=pd.read_csv(path_AQ_os+'/Output/Sample_WaterContents.txt',sep='\t')
        WaterFluxes=CropGrowth=pd.read_csv(path_AQ_os+'/Output/Sample_WaterFluxes.txt',sep='\t')
       
        

        return WaterFluxes,CropGrowth,FinalOutput,WaterContents
#     def RunModel(self):
#         os.chdir(path_AQ_os)
#         print('Entra subproces')
#         # subprocess.Popen(["C:\Program Files\GNU Octave\Octave-6.2.0\mingw64\bin\octave-gui.exe","AquaCropOS_RUN.m"])
#         subprocess.Popen(["octave","AquaCropOS_RUN.m"])
#         CropGrowth=pd.read_csv(path_AQ_os+'/Output/Sample_CropGrowth.txt',sep='\t')
#         FinalOutput=pd.read_csv(path_AQ_os+'/Output/Sample_FinalOutput.txt',sep='\t')
#         WaterContents=CropGrowth=pd.read_csv(path_AQ_os+'/Output/Sample_WaterContents.txt',sep='\t')
#         WaterFluxes=CropGrowth=pd.read_csv(path_AQ_os+'/Output/Sample_WaterFluxes.txt',sep='\t')
#        
#         os.chdir(path_py)
#
#         return WaterFluxes,CropGrowth,FinalOutput,WaterContents

    #funcion coefeiciente de cultivo
    def f_cropcoeff(self,day,model):
        parameters=[]
        if model[:-4]=='Corn':
            parameters=Corn
        elif model[:-4]=='Potato':
            parameters=Potato    
        elif model[:-4]=='Tomato':
            parameters=Tomato
        elif model[:-4]=='Wheat':
            parameters=Wheat
        elif model[:-4]=='Barley':
            parameters=Barley
        elif model[:-4]=='Quinoa':
            parameters=Quinoa
        elif model[:-4]=='Onion':
            parameters=Onion

            # temp=0
            # for i in range(len(cropcoeff)):
            #     for j in range (7):
            #         if day+1==temp:
            #             Kc=cropcoeff[i]
            #             return Kc
            #         temp=temp+1    
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
   
        if cro[:-4]=='Corn':
            z0=Corn[7]
            zx=Corn[8]
            t0=5
            tx=108
            mad=0.55
        elif cro[:-4]=='Potato':
            z0=Potato[7]
            zx=Potato[8]
            t0=6
            tx=100
            mad=0.25
        elif cro[:-4]=='Tomato':
            z0=Tomato[7]
            zx=Tomato[8]
            t0=7
            tx=55
            mad=0.50
        elif cro[:-4]=='Wheat':
            z0=Wheat[7]
            zx=Wheat[8]
            t0=11
            tx=93
            mad=0.55
        elif cro[:-4]=='Barley':
            z0=Barley[7]
            zx=Barley[8]
            t0=14
            tx=60
            mad=0.50
        elif cro[:-4]=='Quinoa':
            z0=Quinoa[7]
            zx=Quinoa[8]
            t0=9
            tx=83
            mad=0.50
        elif cro[:-4]=='Onion':
            z0=Onion[7]
            zx=Onion[8]
            t0=7
            tx=105
            mad=0.25
                   
        #rutina para comocer rootdepth
        #se define que el valor maximo de raiz efectiva esta en d/2 donde se supone que esta el 70% de la raiz
        #para siembra directa inicia en 0, transplante inicia en 0.04
        # z0=0.04
        # zx=0.165
        # tx=105
        # t0=7
        nn=1
        z=z0+(zx-z0) *(((t-(t0/2))/(tx-(t0/2)))**(1/nn))  
        z=z.real
       
        if z>=zx:
            z=zx
        elif z<=0:
            z=0.0001
        # print(z)
        return z,mad  

    # parametros de entrada (dia, dir_carpetalote, nombre del lote)
    def irrET0(self,n,dir_lote):
        with open(dir_lote+'/Parameters.txt','r',errors='ignore') as fin:
            data = fin.read().splitlines()
        fc1010=data[8].split()
        pwp1010=data[9].split()  
        A1=data[3].split()      
        model=data[14].split()
        model=model[1]
        crop=data[13].split()
        crop=crop[1]
        pwp1010=float(pwp1010[1])
        fc1010=float(fc1010[1])
        fc1020=data[27].split()
        pwp1020=data[28].split()          
        

        pwp1020=float(pwp1020[1])
        fc1020=float(fc1020[1])
        
        # print(pwp1010,fc1010)
        A1=float(A1[1])    
        model=data[14].split()
        model=model[1]
        dfIrr=pd.DataFrame()
        dfIrr=dfIrr.fillna(0)
        if model=='BETTER':    
            # zzz=pd.read_csv(dir_lote+'/Out/ET0_Weather_Station_pres.csv',sep='\t')
            zzz=pd.read_csv(dir_lote+'/Weather_Station_pres.csv',sep='\t')

        else:
            zzz=pd.read_csv(dir_lote+'/Weather_Station_pres.csv',sep='\t')
        dfIrr=pd.DataFrame(zzz)
        last_linepar='01/06/20 12:47:07 30.81 58.46 32.08 58.87 0.1 0.1 33.9 33.9 33.9 33.9 320 320 320 320 1 1 1 1 0.9'
        d=last_linepar.split(' ')  
        D1=float(d[12])        
        Dis1=float(d[16])        
        Ef=float(d[20])
        sp_crcoeff=self.f_cropcoeff(n,crop)
        sp_rootdepth,sp_mae=self.rootDepth(n,crop)      
        for o in range(len(dfIrr)):
            if n==o:
                ET=float(dfIrr['ET0'][o])      
                rain=float(dfIrr['Rain(mm)'][o])
                if n!=0:
                    Irr=float(dfIrr['Irrigation(mm)'][o-1]) #toma el riego de el dia anterior
                    depl=float(dfIrr['depl'][o-1]) #toma la deplecion de el dia anterior
                else:
                    Irr=0
                    depl=0
        ETc=ET*sp_crcoeff
        try:
          ET_rain=ET/rain
          k=1.011*math.exp(-0.001143*ET_rain)-1.011*math.exp(-0.5208*ET_rain)
        except:
          k=0.0  
        eff_rain=rain*k
        d_TAW=((fc1010-pwp1010)/100)*sp_rootdepth*1000
        d_MAD=d_TAW*sp_mae
   
        irr_freq=0
        kc_day=sp_crcoeff
        root_day=sp_rootdepth
        if  Irr + eff_rain > depl+ETc:            
            deficit = 0.0
        else:
            deficit = (depl - Irr - eff_rain + ETc)
           
        if  deficit>= d_MAD:
            irr_pres_net = depl - Irr - eff_rain + ETc # (mm)  
            if irr_pres_net!=0 and irr_pres_net>0:
                irr_pres_gross = irr_pres_net/Ef # (mm)
                # irr_area = irr_pres_gross *(A1*0.8) # Field area per treatment (mm*m²)
                # irr_time = irr_area * 60 / (D1*Dis1 ) # D_T*A/n*dq  = irr_pres_area/(320*1Liter/hour) = >  (mm*m²*h) /mm*m² = h *60 = minutes
                # if ETc!=0:
                #     irr_freq = irr_pres_gross/ETc
            else:
                irr_pres_net=0.0
                # irr_pres_gross=0.0
                # irr_area =0.0
                # irr_time =0.0
                # irr_freq =0.0            
        else:
            irr_pres_net=0.0
            # irr_pres_gross=0.0
            # irr_area =0.0
            # irr_time =0.0
            # irr_freq =0.0
        depl=deficit
        ks= (d_TAW-depl)/(d_TAW*(1-sp_mae))
        if ks<0:
            ks=0
        ETcadj=ks*ETc
        if n>=130 and crop=='Onion.CRO' :
            irr_pres_net=0.0
        dfIrr.loc[n,'Irrigation(mm)']= irr_pres_net
        dfIrr.loc[n,'depl']= deficit  
        dfIrr.loc[n,'ks']=ks
        dfIrr.loc[n,'ETcadj']=ETcadj
        dfIrr.loc[n,'eff_rain']=eff_rain
        dfIrr.loc[n,'ETc']=ETc
        dfIrr.loc[n,'sp_crcoeff']=sp_crcoeff
        dfIrr.loc[n,'sp_rootdepth']=sp_rootdepth
        dfIrr.loc[n,'d_TAW']=d_TAW
        dfIrr.loc[n,'d_MAD']=d_MAD
        dfIrr.loc[n,'Prescription(mm)']= irr_pres_net    
        if model=='BETTER':    
            dfIrr.set_index('Date',inplace=True)
            # dfIrr.to_csv(dir_lote+'/Out/ET0_Weather_Station_pres.csv',header=True, sep='\t',float_format="%.2f")
            dfIrr.to_csv(dir_lote+'/Weather_Station_pres.csv',header=True, sep='\t',float_format="%.2f")

        else:
            dfIrr.set_index('Date',inplace=True)
            dfIrr.to_csv(dir_lote+'/Weather_Station_pres.csv',header=True, sep='\t',float_format="%.2f")
        return irr_pres_net,ks,sp_mae,d_TAW,kc_day,root_day,deficit
    def sim_irr_VWC_Day(self,path_AQ_os,out_path,p,n):
            #quitar el retun para continuar  
        with open(out_path+'/Parameters.txt','r',errors='ignore') as fin:
            data = fin.read().splitlines()
        fin.close()
        Sat1010=data[7].split()
        fc1010=data[8].split()
        pwp1010=data[9].split()
        Ksat1010=data[10].split()#hidraulic conductivity    
        crop=data[13].split()
        crop=crop[1]
        Type_soil=data[12].split()
        Type_soil=Type_soil[2]
        pwp1010=float(pwp1010[1])
        fc1010=float(fc1010[1])
        Sat1010=float(Sat1010[1])
        Ksat1010=float(Ksat1010[1])
        model=data[14].split()
        model=model[1]
        DAYS_CROP=data[15].split()
        DAYS_CROP=DAYS_CROP[1]
        SEED_TIME=data[15].split()
        SEED_TIME=SEED_TIME[1]
        T_day=data[16].split()
        T_day=int(T_day[1])  #length crop

           
                ####################33
   
        self.EditClock(path_AQ_os,SEED_TIME,T_day)
        self.EditWeatherInput(path_AQ_os,out_path,p,n)
        self.EditSoil(path_AQ_os,crop,Sat1010,fc1010,pwp1010,Ksat1010)
        self.EditCropInput(path_AQ_os,out_path,p,crop,SEED_TIME,T_day)    
        self.Edit_Irr(path_AQ_os,out_path,p,T_day)
       
        Flux,Growth,Final,Water=self.RunModel()
        #####################33
        self.IrrSensor(n,path_AQ_os,out_path)

        return
   
    def IrrSensor(self,n,path_AQ_os,dir_lote):
   
        with open(out_path+'/Parameters.txt','r',errors='ignore') as fin:
            data = fin.read().splitlines(True)
        fc1010=data[8].split()
        pwp1010=data[9].split()  
        A1=data[3].split()      
        crop=data[13].split()
        crop=crop[1]
        pwp1010=float(pwp1010[1])
        fc1010=float(fc1010[1])
      
        A1=float(A1[1])
        model=data[14].split()
        model=model[1]
        dfIrr=pd.DataFrame()
        dfIrr=dfIrr.fillna(0)
        DAYS_CROP=data[16].split()
        DAYS_CROP=DAYS_CROP[1]
        m=int(DAYS_CROP)-n
        print(data[27].split())
        L1=data[25].split()
        L2=data[26].split()
        fc1020=data[27].split()
        pwp1020=data[28].split()          
        pwp1020=float(pwp1020[1])
        fc1020=float(fc1020[1])
        L1=float(L2[1])
        L2=float(L2[1])
        L2 = L1+L2
        root_lv=[]
        if crop[:-4]=='Maize':
            root_lv=[0.23,0.46,0.69,0.92,2.30]
        elif crop[:-4]=='Potato':
            root_lv=[0.15,0.31,0.45,0.61,1.50]
        elif crop[:-4]=='Tomato':
            root_lv=[0.15,0.31,0.45,0.61,1.00]
        elif crop[:-4]=='Wheat':
            root_lv=[0.26,0.52,0.78,1.04,1.50]
        elif crop[:-4]=='Barley':
            root_lv=[0.25,0.50,0.75,1.00,1.30]
        elif crop[:-4]=='Quinoa':
            root_lv=[0.23,0.47,0.69,0.92,1.00]
        elif crop[:-4]=='Onion':
            root_lv=[0.10,0.20,0.20,0.20,0.20]    
#         L1=root_lv[0]
#         L2=root_lv[1]  
   
        if model=='BETTER':    
            zzz=pd.read_csv(dir_lote+'/VWC_pres.csv',sep='\t')
        else:
            zzz=pd.read_csv(dir_lote+'/VWC_pres.csv',sep='\t')
   
        dfIrr=pd.DataFrame(zzz)
#         last_linepar='01/06/20 12:47:07 30.81 58.46 32.08 58.87 0.1 0.1 33.9 33.9 33.9 33.9 320 320 320 320 1 1 1 1 0.9'
#         d=last_linepar.split(' ')  
#         D1=float(d[12])        
#         Dis1=float(d[16])        
#         Ef=float(d[20])
        sp_crcoeff=self.f_cropcoeff(n,crop)
        sp_rootdepth,sp_mae=self.rootDepth(n,crop)
        kc_day=sp_crcoeff
        root_day=sp_rootdepth  
        for o in range(len(dfIrr)):
            if n==o:
                ET=float(dfIrr['ET0'][o])      
                rain=float(dfIrr['Rain(mm)'][o])
   
                if n!=0:
                    Irr=float(dfIrr['Irrigation(mm)'][o-1]) #toma el riego de el dia anterior
                    depl=float(dfIrr['depl'][o-1]) #toma la deplecion de el dia anterior
                else:
                    Irr=0
                    depl=0
   
        ETc=ET*sp_crcoeff
        try:
          ET_rain=ET/rain
          k=1.011*math.exp(-0.001143*ET_rain)-1.011*math.exp(-0.5208*ET_rain)
        except:
          k=0.0  
        eff_rain=rain*k
        ETc=ET*sp_crcoeff
        try:
           
            with open(path_AQ_os+'/Output/Sample_WaterContents.txt', 'r',errors='ignore') as fin:
                data = fin.read().splitlines(True)
            g=data[n+1]
            g= g.split()
            WC1=float(g[6])*100
            WC2=float(g[7])*100
        except:
            WC1=float(fc1010)-1
            WC2=float(fc1020)
            pass
 
   
        if sp_rootdepth <=  L1:
   
            deficit=(fc1010-WC1)*(sp_rootdepth/100)*1000
            d_TAW=((fc1010-pwp1010)/100)*sp_rootdepth*1000
#         elif (sp_rootdepth >  L1) and  (sp_rootdepth <=  L2):  
        elif (sp_rootdepth >  L1) :  
   
            deficit= (    ( (fc1010-WC1)*(L1/100) ) + ( (fc1020-WC2) * ( (sp_rootdepth-L1)/100) )    )*1000
            d_TAW=((fc1010-pwp1010)/100)*L1*1000    +     ((fc1020-pwp1020)/100)*(sp_rootdepth-L1)*1000
   
        deficit=round(deficit,4)  
        if deficit<0:
            deficit=0
        d_MAD=d_TAW*sp_mae  
        if  deficit>= d_MAD:  
            irr_pres_net = deficit # (mm)
#             irr_pres_gross = irr_pres_net/Ef # (mm)
#             irr_area = irr_pres_gross *(A1*0.8) # Field area per treatment (mm*m²)
#             irr_time = irr_area * 60 /(D1*Dis1)  # D_T*A/n*dq  = irr_pres_area/(320*1Liter/hour) = >  (mm*m²*h) /mm*m² = h *60 = minutes
#             # deficit=0.0
        else:
            irr_pres_net =0.0
#             irr_pres_gross =0.0
#             irr_area =0.0
#             irr_time =0.0
           
        depl=deficit
        ks= (d_TAW-depl)/(d_TAW*(1-sp_mae))
        if ks<0:
            ks=0
        ETcadj=ks*ETc
        if n>=130 and crop[:-4]=='Onion':
            irr_pres_net=0.0
   
        dfIrr.loc[n,'Irrigation(mm)']= str(irr_pres_net)
        dfIrr.loc[n,'depl']= str(deficit)  
        dfIrr.loc[n,'ks']=str(ks)
        dfIrr.loc[n,'ETcadj']=str(ETcadj)
        dfIrr.loc[n,'eff_rain']=str(eff_rain)
        dfIrr.loc[n,'ETc']=str(ETc)
        dfIrr.loc[n,'sp_crcoeff']=str(sp_crcoeff)
        dfIrr.loc[n,'sp_rootdepth']=str(sp_rootdepth)
        dfIrr.loc[n,'d_TAW']=str(d_TAW)
        dfIrr.loc[n,'d_MAD']=str(d_MAD)
        dfIrr.loc[n,'Prescription(mm)']= str(irr_pres_net)
   
        if model=='BETTER':    
            dfIrr.set_index('Date',inplace=True)
            # dfIrr.to_csv(dir_lote+'/Out/VWC_VWC_pres.csv',header=True, sep='\t',float_format="%.2f")
            dfIrr.to_csv(dir_lote+'/VWC_pres.csv',header=True, sep='\t',float_format="%.2f")

        else:
            dfIrr.set_index('Date',inplace=True)
            dfIrr.to_csv(dir_lote+'/VWC_pres.csv',header=True, sep='\t',float_format="%.2f")
       
        return irr_pres_net,ks,sp_mae,d_TAW,kc_day,root_day,deficit

    def reset_tablas(self,path_AQ_os,out_path,p,n):
        #actualiza los datos de metereologicos
        df_a=pd.read_csv(out_path+'/'+p+'.csv', sep='\t')
        date=df_a['Date']
        df_a=pd.DataFrame()
        df_a=df_a.fillna(0)
        df_a['Date']=date
        df=pd.read_csv(dir_weather, sep='\t')
        defalut_Tmax=str('{0:.2f}'.format(df['Tmax(C)'].mean()))
        defalut_Tmin=str('{0:.2f}'.format(df['Tmin(C)'].mean()))

        aux1 = pd.merge(left=df_a ,right=df, left_on='Date', right_on='Date',how='left')  
        aux1 = aux1.reindex(columns=['Date',  'Tmax(C)', 'Tmin(C)', 'ET0','Rain(mm)','Irrigation(mm)', 'depl', 'ks', 'ETcadj', 'ETc', 'eff_rain', 'sp_crcoeff', 'sp_rootdepth', 'd_TAW', 'd_MAD', 'WC1', 'WC2', 'Total rain', 'Total irrigation', 'Yiel(ton/ha)', 'WUE (Kg/m3)', 'IWUE (Kg/m3)','Prescription(mm)'])            
        aux1.to_csv(out_path+'/'+p+'.csv', sep='\t',index=False)
        return
       
    # def better_yield(df_1,df_2,df_3,df_4,n):
    def better_yield(self,df_1,df_2,n):
        df_a=pd.read_csv(out_path+'/Agent_Better.csv', sep='\t')
        df=pd.read_csv(dir_weather, sep='\t')
        defalut_Tmax=str('{0:.2f}'.format(df['Tmax(C)'].mean()))
        defalut_Tmin=str('{0:.2f}'.format(df['Tmin(C)'].mean()))
        df_a.drop(columns=[ 'Tmax(C)'],inplace=True)
        df_a.drop(columns=[ 'Tmin(C)'],inplace=True)
        df_a.drop(columns=[ 'ET0'],inplace=True)
        df_a.drop(columns=[ 'Rain(mm)'],inplace=True)
        aux1 = pd.merge(left=df_a ,right=df, left_on='Date', right_on='Date',how='left')  
        aux1 = aux1.reindex(columns=['Date',  'Tmax(C)', 'Tmin(C)', 'ET0','Rain(mm)','Irrigation(mm)', 'depl', 'ks', 'ETcadj', 'ETc', 'eff_rain', 'sp_crcoeff', 'sp_rootdepth', 'd_TAW', 'd_MAD', 'WC1', 'WC2', 'Total rain', 'Total irrigation', 'Yiel(ton/ha)', 'WUE (Kg/m3)', 'IWUE (Kg/m3)','Better_Method','Prescription(mm)','Negotiation'])
        aux1.to_csv(out_path+'/Agent_Better.csv', sep='\t',index=False)
        #une los datos de salida de la simulacion de los 4 metodos en uno solo dataframe
    #     frame=pd.concat([df_1,df_2,df_3,df_4])
        frame=pd.concat([df_1,df_2])
        #ordena las simulaciones por mejor IWUE(Kg/m3) y WUE(Kg/m3)
        df=frame.sort_values(by=['Yield','IWUE(Kg/m3)','WUE(Kg/m3)'],ascending=False)
        df.to_csv(out_path+'/Better_Method.csv',index=False,header=True, sep='\t',float_format="%.2f")
        #alamcena los datos
        df=pd.read_csv(out_path+'/Better_Method.csv', sep='\t')
        #alamcena la mejor metodo de  prescripcion
        better=df.loc[0,'method']
        metodo=df['method'].tolist()
        #abre el archivo que contiene los datos del cultivo (historial de riego)
        df_Ag_Better=pd.read_csv(out_path+'/Agent_Better.csv', sep='\t')
        #abre el archivo que contiene el mejor metodo de  prescipcion
        df_m0=pd.read_csv(out_path+'/'+metodo[0] +'.csv', sep='\t')
        # df_m1=pd.read_csv(out_path+'/'+m[1] +'.csv', sep='\t')
        # df_m2=pd.read_csv(out_path+'/'+m[2] +'.csv', sep='\t')
        # df_m3=pd.read_csv(out_path+'/'+m[3] +'.csv', sep='\t')
       
        df_Ag_Better.loc[n,'Irrigation(mm)']=df_m0.loc[n,'Irrigation(mm)']
        df_Ag_Better.loc[n,'depl']=df_m0.loc[n,'depl']
    
        df_Ag_Better.loc[n,'ks']=df_m0.loc[n,'ks']
        df_Ag_Better.loc[n,'ETcadj']=df_m0.loc[n,'ETcadj']
        df_Ag_Better.loc[n,'ETc']=df_m0.loc[n,'ETc']
        df_Ag_Better.loc[n,'eff_rain']=df_m0.loc[n,'eff_rain']
        df_Ag_Better.loc[n,'sp_crcoeff']=df_m0.loc[n,'sp_crcoeff']
        df_Ag_Better.loc[n,'sp_rootdepth']=df_m0.loc[n,'sp_rootdepth']
        df_Ag_Better.loc[n,'d_TAW']=df_m0.loc[n,'d_TAW']
        df_Ag_Better.loc[n,'d_MAD']=df_m0.loc[n,'d_MAD']
        df_Ag_Better.loc[n,'WC1']=df_m0.loc[n,'WC1']
        df_Ag_Better.loc[n,'WC2']=df_m0.loc[n,'WC2']
    #     df_Ag_Better.loc[n,'WC2']=df_m0.loc[n,'WC2']
     
        df_Ag_Better.loc[n,'Total rain']=df_m0.loc[n,'Total rain']
        df_Ag_Better.loc[n,'Total irrigation']=df_m0.loc[n,'Total irrigation']
        df_Ag_Better.loc[n,'Yiel(ton/ha)']=df_m0.loc[n,'Yiel(ton/ha)']
       
        df_Ag_Better.loc[n,'IWUE (Kg/m3)']=df_m0.loc[n,'IWUE (Kg/m3)']
        df_Ag_Better.loc[n,'WUE (Kg/m3)']=df_m0.loc[n,'WUE (Kg/m3)']    
        df_Ag_Better.loc[n,'Better_Method']=better
        df_Ag_Better.to_csv(out_path+'/Agent_Better.csv', sep='\t',float_format="%.2f",index=False)
    
        # df_Ag_Better.loc[n,'Prescription(mm)']=df_m0.loc[n,'Prescription(mm)']    
        # df_Ag_Better.loc[n,'Total rain']=df.loc[0,'Total rain']
        # df_Ag_Better.loc[n,'Total irrigation']=df.loc[0,'Seasonal irrigation (mm)']
        # df_Ag_Better.loc[n,'Yiel(ton/ha)']=df.loc[0,'Yield (tonne/ha)']
        # df_Ag_Better.loc[n,'IWUE (Kg/m3)']=df.loc[0,'IWUE(Kg/m3']
        # df_Ag_Better.loc[n,'WUE (Kg/m3)']=df.loc[0,'WUE(Kg/m3']
        for met in metodo[1:]:
            df_aux=pd.read_csv(out_path+'/'+met+'.csv', sep='\t')
    #         print(out_path+'/'+met+'.csv')
            df_aux.loc[n,'Prescription(mm)']=df_aux.loc[n,'Irrigation(mm)']  
            df_aux.loc[n,'Irrigation(mm)']=df_m0.loc[n,'Irrigation(mm)']
            df_aux.loc[n,'depl']=df_m0.loc[n,'depl']
           
            df_aux.to_csv(out_path+'/'+met+'.csv', sep='\t',float_format="%.2f",index=False)
        return
    def main(self,path_AQ_os,out_path,p,n):
    
        #quitar el retun para continuar  
        with open(out_path+'/Parameters.txt','r',errors='ignore') as fin:
            data = fin.read().splitlines()
        fin.close()
        Sat1010=data[7].split()
        fc1010=data[8].split()
        pwp1010=data[9].split()
        Ksat1010=data[10].split()#hidraulic conductivity    
        crop=data[13].split()
        crop=crop[1]
        Type_soil=data[12].split()
        Type_soil=Type_soil[2]
        pwp1010=float(pwp1010[1])
        fc1010=float(fc1010[1])
        Sat1010=float(Sat1010[1])
        Ksat1010=float(Ksat1010[1])
        model=data[14].split()
        model=model[1]
        DAYS_CROP=data[15].split()
        DAYS_CROP=DAYS_CROP[1]
        SEED_TIME=data[15].split()
        SEED_TIME=SEED_TIME[1]
        T_day=data[16].split()
        T_day=int(T_day[1])  #length crop
       
        #actualiza los datos de metereologicos
    
        df_a=pd.read_csv(out_path+'/'+p+'.csv', sep='\t')
        df=pd.read_csv(dir_weather, sep='\t')
        defalut_Tmax=str('{0:.2f}'.format(df['Tmax(C)'].mean()))
        defalut_Tmin=str('{0:.2f}'.format(df['Tmin(C)'].mean()))
        df_a.drop(columns=[ 'Tmax(C)'],inplace=True)
        df_a.drop(columns=[ 'Tmin(C)'],inplace=True)
        df_a.drop(columns=[ 'ET0'],inplace=True)
        df_a.drop(columns=[ 'Rain(mm)'],inplace=True)
        aux1 = pd.merge(left=df_a ,right=df, left_on='Date', right_on='Date',how='left')  
        if p=='Agent_Better':
            aux1 = aux1.reindex(columns=['Date',  'Tmax(C)', 'Tmin(C)', 'ET0','Rain(mm)','Irrigation(mm)', 'depl', 'ks', 'ETcadj', 'ETc', 'eff_rain', 'sp_crcoeff', 'sp_rootdepth', 'd_TAW', 'd_MAD', 'WC1', 'WC2', 'Total rain', 'Total irrigation', 'Yiel(ton/ha)', 'WUE (Kg/m3)', 'IWUE (Kg/m3)','Better_Method','Prescription(mm)','Negotiation'])
        else:
            aux1 = aux1.reindex(columns=['Date',  'Tmax(C)', 'Tmin(C)', 'ET0','Rain(mm)','Irrigation(mm)', 'depl', 'ks', 'ETcadj', 'ETc', 'eff_rain', 'sp_crcoeff', 'sp_rootdepth', 'd_TAW', 'd_MAD', 'WC1', 'WC2', 'Total rain', 'Total irrigation', 'Yiel(ton/ha)', 'WUE (Kg/m3)', 'IWUE (Kg/m3)','Prescription(mm)'])            
        aux1.to_csv(out_path+'/'+p+'.csv', sep='\t',index=False)

        if p =='Weather_Station_pres':
            self.irrET0(n,out_path)  
        elif p =='VWC_pres':
            self.sim_irr_VWC_Day(path_AQ_os,out_path,p,n)
        self.EditClock(path_AQ_os,SEED_TIME,T_day)
        rain_T=self.EditWeatherInput(path_AQ_os,out_path,p,n)
        self.EditSoil(path_AQ_os,crop,Sat1010,fc1010,pwp1010,Ksat1010)
        self.EditCropInput(path_AQ_os,out_path,p,crop,SEED_TIME,T_day)    
        self.Edit_Irr(path_AQ_os,out_path,p,T_day)
        Flux,Growth,Final,Water=self.RunModel()
       
        df_F=Final
        ##version 5
        df_F['IWUE(Kg/m3)']=df_F['Yield']*1000/df_F['TotIrr']
        df_F['WUE(Kg/m3)']=df_F['Yield']*1000/(df_F['TotIrr']+rain_T)
        df_F['Total rain']=rain_T
        df_F['method']=p
    #     print (df_F)
        df_Ag=pd.read_csv(out_path+'/'+p+'.csv', sep='\t')
    #     print('imprime el valor de lluvia',df_F.loc[0,'Total rain'])
        df_Ag.loc[n,'Total rain']=df_F.loc[0,'Total rain']
        df_Ag.loc[n,'Total irrigation']=df_F.loc[0,'TotIrr']
        df_Ag.loc[n,'Yiel(ton/ha)']=df_F.loc[0,'Yield']
        df_Ag.loc[n,'IWUE (Kg/m3)']=df_F.loc[0,'IWUE(Kg/m3)']
        df_Ag.loc[n,'WUE (Kg/m3)']=df_F.loc[0,'WUE(Kg/m3)']
    #     print(Water.loc[n,'0.15m']*100)
        df_Ag.loc[n,'WC1']=Water.loc[n,'0.15m']*100
        df_Ag.loc[n,'WC2']=Water.loc[n,'0.25m']*100
    
        df_Ag.to_csv(out_path+'/'+p+'.csv', sep='\t',float_format="%.2f",index=False)  
        ##Version 6
        # df_F['IWUE(Kg/m3)']=df_F['Yield (tonne/ha)']*1000/df_F['Seasonal irrigation (mm)']
        # df_F['WUE(Kg/m3)']=df_F['Yield (tonne/ha)']*1000/(df_F['Seasonal irrigation (mm)']+rain_T)
        # df_F['Total rain']=rain_T
        # df_F['method']=p
        # df_Ag=pd.read_csv(out_path+'/'+p+'.csv', sep='\t')
        # print('imprime el valor de lluvia',df_F.loc[0,'Total rain'])
        # df_Ag.loc[n,'Total rain']=df_F.loc[0,'Total rain']
        # df_Ag.loc[n,'Total irrigation']=df_F.loc[0,'Seasonal irrigation (mm)']
        # df_Ag.loc[n,'Yiel(ton/ha)']=df_F.loc[0,'Yield (tonne/ha)']
        # df_Ag.loc[n,'IWUE (Kg/m3)']=df_F.loc[0,'IWUE(Kg/m3)']
        # df_Ag.loc[n,'WUE (Kg/m3)']=df_F.loc[0,'WUE(Kg/m3)']
        # df_Ag.loc[n,'WC1']=Water.loc[n,'th1']
        # df_Ag.loc[n,'WC2']=Water.loc[n,'th2']
        # df_Ag.to_csv(out_path+'/'+p+'.csv', sep='\t',float_format="%.2f")    
        return Flux,Growth,Final,Water

    def Pres_Aquacrop(self): 
            


        soilparam=open('./Parameters/SoilConfparameters.txt','r')
        linespar =soilparam.read().splitlines()
        last_linepar=linespar[-1]
        d=last_linepar.split(' ')
        pwp1010=float(d[2])
        fc1010=float(d[3])        
        pwp1020=float(d[4])        
        fc1020=float(d[5])
        L1=float(d[6])
        L2=float(d[7])
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

        with open(out_path+'/Parameters.txt', 'r',errors='ignore') as fin:
          data = fin.read().splitlines(True)
        cnt=0
        for linea in data:
          if linea.find('FC1010')==0:
              data[cnt]= 'FC1010              '+str(fc1010)+'\n'                   
          elif linea.find('PWP1010')==0:
              data[cnt]= 'PWP1010             '+str(pwp1010)+'\n'                   
          elif linea.find('FC1020')==0:
              data[cnt]= 'FC1020              '+str(fc1020)+'\n'                   
          elif linea.find('PWP1020')==0:
              data[cnt]= 'PWP1020             '+str(pwp1020)+'\n'                   
          elif linea.find('L1')==0:
              data[cnt]= 'L1                  '+str(L1)+'\n'                   
          elif linea.find('L2')==0:
              data[cnt]= 'L2                  '+str(L2)+'\n'
          cnt+=1
        out=open(out_path+'/Parameters.txt', 'w',errors='ignore')
        for linea in data:
          out.write(linea)
        out.close()
        timeacq=time.asctime()
        hour=str(time.strftime("%H:%M:%S"))
        date=str(time.strftime("%d/%m/%y"))
        param=open('./Parameters/ETparametersAuto.txt','r')
        linespar =param.read().splitlines()
        date1=datetime.strptime(self.Aut_seedtime.text(), "%d/%m/%y")
        date2=datetime.strptime(date, "%d/%m/%y")
        delta=date2-date1
        day=delta.days
        # os.system('python3 /home/pi/Desktop/IntIrrAgent05292021/AquaCrop_OsPy/AquaCrop_OsPy/Station_2.py')

        Flux_1,Growth_1,Final_1,Water_1=self.main(path_AQ_os,out_path,'VWC_pres',day)
        time.sleep(3)
        Flux_2,Growth_2,Final_2,Water_2=self.main(path_AQ_os,out_path,'Weather_Station_pres',day)
        self.better_yield(Final_1,Final_2,day)
        self.main(path_AQ_os,out_path,'Agent_Better',day)
        df_better=pd.read_csv(out_path+'/Agent_Better.csv',sep='\t')
        print('sale de Pres_Aquacrop')
        return
    def save_AuPres(self):

        date=str(time.strftime("%d/%m/%y"))  
        date1=datetime.strptime(self.Aut_seedtime.text(), "%d/%m/%y")
        date2=datetime.strptime(date, "%d/%m/%y")
        day=abs(date2-date1).days  

        soilparam=open('./Parameters/SoilConfparameters.txt','r')
        linespar =soilparam.read().splitlines()
        last_linepar=linespar[-1]
        d=last_linepar.split(' ')
        pwp1010=float(d[2])
        fc1010=float(d[3])        
        pwp1020=float(d[4])        
        fc1020=float(d[5])
        L1=float(d[6])
        L2=float(d[7])
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
        
        
        df_better=pd.read_csv(out_path+'/Agent_Better.csv',sep='\t')
        irr_pres_net = float(df_better.loc[day,'Irrigation(mm)'])
        print(f'riego: {irr_pres_net}')
        ET = float(df_better.loc[day,'ET0'])
        sp_crcoeff = float(df_better.loc[day,'sp_crcoeff'])
        ETc = float(df_better.loc[day,'ETc'])
        rain = float(df_better.loc[day,'Rain(mm)'])
        sp_rootdepth = float(df_better.loc[day,'sp_rootdepth'])
        sp_mae = float(df_better.loc[day,'Irrigation(mm)'])
        d_MAD = float(df_better.loc[day,'d_MAD'])
        d_TAW = float(df_better.loc[day,'d_TAW'])
        deficit = float(df_better.loc[day,'depl'])
        try:
            ET_rain=ET/rain
            k=1.011*math.exp(-0.001143*ET_rain)-1.011*math.exp(-0.5208*ET_rain)
        except:
            k=0.0            
        eff_rain=rain*k
        
        sp_mae=round(d_TAW/d_MAD,2)
        irr_pres_gross = irr_pres_net/Ef # (mm)
        irr_area = irr_pres_gross *A1 # Field area per treatment (mm*m²)
        irr_time = irr_area * 60 / (D1*Dis1 ) # D_T*A/n*dq  = irr_pres_area/(320*1Liter/hour) = >  (mm*m²*h) /mm*m² = h *60 = minutes 
        irr_freq = irr_pres_gross/ETc
        
        presct1=round(irr_area*float(self.Aut_Rate1.text())/100,2)
        presct2=round(irr_area*float(self.Aut_Rate2.text())/100,2)
        presct3=round(irr_area*float(self.Aut_Rate3.text())/100,2)
        presct4=round(irr_area*float(self.Aut_Rate4.text())/100,2)
        timet1=round(irr_time*float(self.Aut_Rate1.text())/100,2)
        timet2=round(irr_time*float(self.Aut_Rate2.text())/100,2)
        timet3=round(irr_time*float(self.Aut_Rate3.text())/100,2)
        timet4=round(irr_time*float(self.Aut_Rate4.text())/100,2)
        print('ET_presct1: ',presct1, 'ET_presct2: ',presct2,'ET_presct3: ',presct3, 'ET_presct4: ' ,presct4)
        self.Aut_time1.setText(str(timet1))
        self.Aut_time2.setText(str(timet2))
        self.Aut_time3.setText(str(timet3))
        self.Aut_time4.setText(str(timet4))
        
        #......IrrigationParameters
        hour=str(time.strftime("%H:%M:%S"))
        day=str(time.strftime("%d/%m/%y"))
        a0=self.Aut_IrrSch.text()
        a1=self.Aut_Morning.text()
        a2=self.Aut_Afternoon.text()
        a3=self.Aut_Rate1.text()
        a4=self.Aut_Rate2.text()        
        a5=self.Aut_Rate3.text()
        a6=self.Aut_Rate4.text()
        a7=self.Aut_seedtime.text()
        print("Irrigation parameters"+' '+str(day)+' '+str(hour)+' '+str(a0)+' '+str(a1)+' '+str(a2)+' '+str(a3)+' '+str(a4)+' '+str(a5)+' '+str(a6)+' '+str(a7)+'\n')
        semiautpres=open('./Prescription/Autopres.txt','w')
        semiautpres.write(str(day)+' '+str(hour)+' '+str(round(presct1,2))+' '+str(round(presct2,2))+' '+str(round(presct3,2))+' '+str(round(presct4,2))+' '+str(round(timet1,2))+' '+str(round(timet2,2))+' '+str(round(timet3,2))+' '+str(round(timet4,2))+'\n')
        semiautpres.close()
        print('sale save')
        return    
