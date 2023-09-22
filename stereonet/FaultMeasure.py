class FaultMeasure:
    def __init__(self, row_data):
        self.strike = int(row_data[0])
        self.dip = int(row_data[1])
        self.plunge = int(row_data[2])
        self.fault_type = row_data[3]
