import os
import pandas as pd
from datetime import datetime, timedelta, date
import subprocess, os
import math
import time
import os.path
from os import path, sep
import asyncio
import csv


class DocumentsCreate:
    def __init__(self, seedDate, endDaysCrop):
        self.seedTime = datetime.strptime(seedDate, "%Y-%m-%d")
        self.EndDaysCrop = endDaysCrop
        self.createDocument(
            "/home/pi/Desktop/Real_Agent/RealAgent-master/src/AquaCrop_OsPy/AquaCrop_OsPy/Lote/Agent_Better.csv"
        )
        self.createDocument(
            "/home/pi/Desktop/Real_Agent/RealAgent-master/src/AquaCrop_OsPy/AquaCrop_OsPy/Lote/VWC_pres.csv"
        )
        self.createDocument(
            "/home/pi/Desktop/Real_Agent/RealAgent-master/src/AquaCrop_OsPy/AquaCrop_OsPy/Lote/Weather_Station_pres.csv"
        )
        self.createClimaticDocument(
            "/home/pi/Desktop/RealAgent/src/AquaCrop_OsPy/AquaCrop_OsPy/Date_Weather_station/Weather_station_2.csv"
        )

    def createClimaticDocument(self, directory):
        if path.isfile(f"{directory}"):
            print("dir exist")
        else:
            with open(
                f"{directory}",
                "a",
            ) as dataF:
                writer = csv.writer(dataF, delimiter="\t")
                writer.writerow(
                    [
                        "Date",
                        "Tmax(C)",
                        "Tmin(C)",
                        "ET0",
                        "Rain(mm)",
                    ]
                )
                for i in range(self.EndDaysCrop + 1):
                    self.DatesCrop = [str(self.seedTime + timedelta(days=i)).split()[0]]
                    writer.writerow(
                        self.DatesCrop,
                    )
            dataF.close()

    def createDocument(self, directory):
        if path.isfile(f"{directory}"):
            print("dir exist")
        else:
            with open(
                f"{directory}",
                "a",
            ) as dataH:
                writer = csv.writer(dataH, delimiter="\t")
                writer.writerow(
                    [
                        "Date",
                        "Tmax(C)",
                        "Tmin(C)",
                        "ET0",
                        "Rain(mm)",
                        "Irrigation(mm)",
                        "depl",
                        "ks",
                        "ETcadj",
                        "ETc",
                        "eff_rain",
                        "sp_crcoeff",
                        "sp_rootdepth",
                        "d_TAW",
                        "d_MAD",
                        "WC1",
                        "WC2",
                        "Total rain",
                        "Total irrigation",
                        "Yiel(ton/ha)",
                        "WUE (Kg/m3)",
                        "IWUE (Kg/m3)",
                        "Prescription(mm)",
                    ]
                )
                for i in range(self.EndDaysCrop + 1):
                    self.DatesCrop = [str(self.seedTime + timedelta(days=i)).split()[0]]
                    writer.writerow(
                        self.DatesCrop,
                    )

            dataH.close()