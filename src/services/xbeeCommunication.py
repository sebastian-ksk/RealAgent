
import sys
from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice,XBee64BitAddress,OperatingMode,RemoteATCommandPacket
from datetime import datetime, date, time, timedelta #para fechas y hora

# "/dev/ttyUSB0"

class XbeeCommunication():
    Path_Data=""
    
    def __init__(self, UsbDirection, baudRate,sensors, firebase):
        self.FireBase = firebase
        self.XbeesValvesSystem={'Agent_1': '0013A20041573102', 
        'Agent_2': '0013A20040E8762A',
        'Agent_3': '0013A20040E7412C',
        'Agent_4': '0013A20040E8816B'}
        print('xbee  ')
        self.sensors = sensors
        self.Path_Data = '/home/pi/Desktop/RealAgent/src/storage'
        self.device=XBeeDevice(UsbDirection,baudRate)
        self.device.open()
        print('xbee init ')
        # self.subproces_Sens=Thread(target=self.xbeeComm.runCallback)
        # self.subproces_Sens.daemon=True
        # self.subproces_Sens.start()

    def runCallback(self):
        try: 
            self.device.add_data_received_callback(self.data_receive_callback)
            print("Waiting for data...\n")
            input()
        finally:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
            if self.device is not None and self.device.is_open():
                self.device.close()  

    def data_receive_callback(self, xbee_message):
        self.message=str(xbee_message.data.decode()).split(':')
        print(str(datetime.now()).split()[1])
        print(str(xbee_message.data.decode()))
        self.today = date(datetime.now().year,datetime.now().month,datetime.now().day)
        if self.message[0] == 'IRRIG':
            if self.message[1].split(";")[0]=="COMPLETE":
                print('End Irrigation')
                self.save_data_Xbee(f"{self.Path_Data}/Irrigation_finished.txt",self.message[1])
                
                try:
                    self.FireBase.ResultIrrDoc_ref.update({
                            u'IrrigationState':'OFF',
                            u'LastIrrigationDate' : str(self.today),
                            u'irrigationApplied' : self.xbee_message.split(';')[2]
                        })
                except:
                    pass        
            else:
                print('Irrigation Start')
                self.save_data_Xbee(f"{self.Path_Data}/Irrigation_started.txt",self.message[1])
                try:
                    self.FireBase.ResultIrrDoc_ref.update({
                        u'IrrigationState':'ON'
                    })
                except:
                    print('error update data ')
                    pass    
      
      
        elif self.message[0]=="SENSORS":
            print('sensores')
            self.save_data_Xbee(f"{self.Path_Data}/Sensor_data.txt",self.message[1])
            self.messageSens = self.message[1].split('\x00')
            print(str(self.messageSens[0]))
            self.sensors.allSensors = [float(x) for x in str(self.messageSens[0]).split(';')]
            try:
                self.FireBase.SensorsDoc_ref.update({
                        u''+f'{str(self.today)}':{
                            u''+f'{datetime.now().hour}:{datetime.now().minute}':{
                                u'VWC1' :self.sensors.allSensors[0],
                                u'VWC2' :self.sensors.allSensors[1],
                                u'VWC3' :self.sensors.allSensors[2],
                                u'VWC4' :self.sensors.allSensors[3],
                                u'temperature' :self.sensors.allSensors[4],
                                u'CanopyTemperature':self.sensors.allSensors[5],
                                u'RH' : self.sensors.allSensors[6],
                                u'soilTemperature':self.sensors.allSensors[7]
                            }
                            
                        }  
                        
                    })
            except:
                pass    



    def save_data_Xbee(self,directory,message):
        
        self.dir_file = directory
        self.SaveFile = open(self.dir_file, 'a',errors='ignore')
        self.SaveFile.write(f'{str(datetime.now()).split()[0]};{str(datetime.now()).split()[1]};{message};\n')
        self.SaveFile.close()




    def sendIrrigationOrder(self,message,Agent,presc):
        try:
            print(self.XbeesValvesSystem[f'Agent_{Agent}'])
            self.remote_device=RemoteXBeeDevice(self.device,XBee64BitAddress.from_hex_string(self.XbeesValvesSystem[f'Agent_{Agent}']))     
            self.device.send_data(self.remote_device,f'{message};1;{presc}')   
            print('send xbee order .') 
            return True
        except:
            return False