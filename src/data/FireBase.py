#=======LIBRERIAS DELSDK PARA EL ACCESO A LOS DATOS DE firebase DESDE EL MODULO ADMINISTRADOR
import firebase_admin 
from firebase_admin import credentials #ACCESO A LAS LLAVES PRIVADAS DEL MODULO DE ADMIN O DATOS DE ALMACVENAMIENTO
from firebase_admin import db  #ACCESO A LA BASE DE DATOS
from firebase_admin import firestore  #ACCESO A LA BASE DE DATOS
import threading
from datetime import datetime, date, time, timedelta

'''https://googleapis.dev/python/firestore/latest/document.html'''

class FIREBASE_CLASS():
    def __init__(self,AgentName,cropModel):
        self.cropModel = cropModel
        self.PathCredentials = '/home/pi/Desktop/RealAgent/src/data/ClaveFirebase.json'
        self.urlDatabase = 'https://manageragents-2a3f6-default-rtdb.firebaseio.com/'
        self.AgentName = AgentName
        cred=credentials.Certificate(self.PathCredentials)
        firebase_admin.initialize_app(cred,{
            'databaseURL': self.urlDatabase
        })  
        firestoreDb = firestore.client()
        self.CropDoc_ref = firestoreDb.collection(u''+f'{self.AgentName}').document(u'Crop')
        self.IrrPresDoc_ref = firestoreDb.collection(u''+f'{self.AgentName}').document(u'Irrigation-Prescription')
        self.ResultIrrDoc_ref= firestoreDb.collection(u''+f'{self.AgentName}').document(u'ResultIrrigation-Prescription')
        self.SensorsDoc_ref= firestoreDb.collection(u''+f'{self.AgentName}').document(u'Sensors')

        doc = self.CropDoc_ref.get()
        if doc.exists:
            self.Crop = doc.to_dict()
            #fecha de siembra/seed time
            self._dateseed = str(self.Crop['SeedDate']).split('/')
            self.cropModel.seedTime = date(int(self._dateseed[2]),int(self._dateseed[1]),int(self._dateseed[0]))
            #Crop/cultivo
            self.cropModel.typeCrop =  self.Crop['TypeCrop'] 
            #pwp
            self.cropModel.pointWp =  float(self.Crop['pwp'])
            #capacidad de campo / fiel capacity
            self.cropModel.FieldCap = float(self.Crop['field_capacity'])
        else:
            print(u' Crop No such document!')
            self.CropDoc_ref.set({
                u'TypeCrop' : 'Potato',
                u'pwp' : 0,
                u'field_capacity':0,
                u'SeedDate': '1/1/2021',
                u'daysCrop':0
            })
        doc = self.IrrPresDoc_ref.get()
        if doc.exists:
            self.Irrig_Presc = doc.to_dict()
            #riego-prescripcion/ irrigation-prescription
            self.cropModel.prescMode = self.Irrig_Presc['PrescriptionMethod']
            self.cropModel.presctime = self.Irrig_Presc['PrescriptionTime']
            self.cropModel.irrigationtime = self.Irrig_Presc['IrrigationTime']
        else:
            print(u' irrigation-prescription No such document!')
            self.IrrPresDoc_ref.set({
                u'IrrigationMethod': 'drip',
                u'constanFlow': 1,
                u'PrescriptionTime': '00:00',
                u'IrrigationTime': '00:00',
                u'PrescriptionMethod' : 'Weather_Station',
                u'manualValves' : "OFF"
            })
        doc = self.ResultIrrDoc_ref.get()
        if doc.exists:
            pass
        else:
            self.ResultIrrDoc_ref.set({
                u'LastPrescriptionDate': '0/0/0/',
                u'NetPrescription':0,
                u'LastIrrigationDate': '0/0/0/',
                u'irrigationApplied' : 0,
                u'IrrigationState' : 'off',
                u'DaysCrop':0
            })
        doc = self.SensorsDoc_ref.get()
        if doc.exists:
            pass
        else:
            self.SensorsDoc_ref.set({
                u''+f'{self.cropModel.seedTime}':{
                    u'00:00:00':{
                        u'VWC1' :0,
                        u'VWC2' :0,
                        u'VWC3' :0,
                        u'VWC4' :0,
                        u'temperature' :0,
                        u'CanopyTemperature':0,
                        u'RH' : 0,
                        u'soilTemperature':0
                    }
                    
                },
            })    

    

        #changes to movil APP
        self.docRefview = firestoreDb.collection(u''+f'{self.AgentName}').document(u'Irrigation-Prescription')
        self.IrrigationPrescription = self.docRefview.get().to_dict()
        self.callback_done = threading.Event() 
        doc_watch = self.docRefview.on_snapshot(self.on_snapshot) 

    def on_snapshot(self,doc_snapshot, changes, read_time):
        for change in changes:
            if change.type.name == 'ADDED':
                pass
            elif change.type.name == 'MODIFIED':
                #print(f' paht: {change.document.to_dict()}')
                self.changeData = change.document.to_dict()
                print('change data ================== : ')
                self.compare(self.IrrigationPrescription,self.changeData)
                self.IrrigationPrescription = self.changeData
            elif change.type.name == 'REMOVED':
                pass
        self.callback_done.set()    


    def compare(self,first, second):
        self.sharedKeys = set(first.keys()).intersection(second.keys())
        for self.key in self.sharedKeys:
            if first[self.key] != second[self.key]:
                print("Key: {}, Value 1: {}, Value 2: {}".format(self.key, first[self.key], second[self.key]))  
                if (self.key == 'PrescriptionMethod') :
                    self.cropModel.prescMode  = second[self.key]
                elif (self.key == 'PrescriptionTime') :
                    self.cropModel.presctime = second[self.key] 
                elif (self.key == 'IrrigationTime') :
                    self.cropModel.irrigationtime  = second[self.key]     