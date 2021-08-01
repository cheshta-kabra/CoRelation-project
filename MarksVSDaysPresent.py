import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df,x='Days Present',y='Marks In Percentage')
        fig.show()
def getDataSource(data_path):
    daysPresent=[]
    Marks=[]
    with open(data_path) as csv_file:
        csvReader=csv.DictReader(csv_file)
        for row in csvReader:
            daysPresent.append(float(row['Days Present']))
            Marks.append(float(row['Marks In Percentage']))
    return {'x':daysPresent,'y':Marks}
def findCorelation(DataSource):
     Corelation=np.corrcoef(DataSource['x'],DataSource['y'])
     print('Corelation between Days Present  and Marks Scored',Corelation[0,1])
def setup():
    data_path='./MarksDay Present.csv'
    plotFigure(data_path)
    DataSource=getDataSource(data_path)
    findCorelation(DataSource   )
setup()
