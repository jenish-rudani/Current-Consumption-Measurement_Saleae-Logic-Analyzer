# Current Consumption Measurement
An extension for Saleae Logic Analyser that determines the area under curve of an analog voltage measurement against 18 Ohm resistor to determine average current consumption
![AUC](Images/AUC.png)

# Circuit Diagram
Connect your target in series with 18 ohm resistor and attach Saleae Logic Probes across this resistor to measure analog voltage. Extension will calculate Average Current as per below

$$  averageCurrent = {averageVoltage/18} $$


## Instructions
1. Install this extension by clicking "Install"
2. Add a measurement by clicking on the "Annotations panel" on the right, then the Measurements "+" icon.
3. Drag the measurement selection window over your recorded data.
