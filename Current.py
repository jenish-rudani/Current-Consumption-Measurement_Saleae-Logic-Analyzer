from saleae.range_measurements import AnalogMeasurer
import numpy as np
from numpy import trapz

class Current(AnalogMeasurer):
    supported_measurements = ["area"]

    """
    Class initialisation
    """
    def __init__(self, requested_measurements):
        super().__init__(requested_measurements)
        self.batches = []

    """
    Does not process data. Simply attaches
    samples to be processed later.
    """
    def process_data(self, data):
        self.batches.append(data.samples)

    """
    Calculates Average Voltage and Divide by 5.6 Ohm Resistor.
    """  
    def measure(self):
        data = np.concatenate(self.batches)
        averageVoltage = np.mean(data)
        averageCurrent = averageVoltage / 18
        maxVoltage = np.amax(data)
        maxCurrent = maxVoltage / 18
        return {"Iavg" : round(averageCurrent,6),
                "Vavg": round(averageVoltage,6),
                "Vmax" : round(maxVoltage,6),
                "Imax" : round(maxCurrent,6)}
        
