
import statistics as stats

from code.StockData import StockData
file_path = os.path("data", "raw", "amzn.csv")
metrics = StockMetrics(file_path)

class StockMetrics(StockData):
    def __init__(self, path):
        # call the parent method's constructor
        super(StockMetrics, self).__init__(path)

        # now that we've ran self.load(), we can interact with "self.data" as a
        # list of lists
        self.load()

    def average01(self):
        """pt1
        """
        averages = []
        for row in self.data:
            print("old row", row)
            new_row = [float(val) for val in row [1:] if val != "" or val != " "]
            avg = stats.mean(new_row)
            print(avg)
            averages.append(avg)
        return averages
    
    def average01(self):
        averages = []
        print(self.data)
        for row in self.data:
            print(row)
            new_data = []
            print(new_data)
            for value in row[1:]:
                if value == "" or value == " ":
                    print('----emptyRow----')
                    continue
                else:
                    new_data.append(float(value))
                    print(new_data,'<------Row Value ADDED to list')
            averages.append(round(sum(new_data)/len(new_data),3))

        return averages

    def median02(self):
        median = []
        print(self.data)
        for row in self.data:
            print(row)
            new_data = []
            print(new_data)
            for value in row[1:]:
                if value == "" or value == " ":
                    print('----emptyRow----')
                    continue
                else:
                    new_data.append(float(value))
                    print(new_data,'<------Row Value ADDED to list')
            median.append(round(sum(new_data)/len(new_data),3))

        return median


    def stddev03(self):
        stddev = []
        print(self.data)
        for row in self.data:
            print(row)
            new_data = []
            print(new_data)
            for value in row[1:]:
                if value == "" or value == " ":
                    print('----emptyRow----')
                    continue
                else:
                    new_data.append(float(value))
                    print(new_data,'<------Row Value ADDED to list')
            stddev.append(round(sum(new_data)/len(new_data),3))

        return stddev
