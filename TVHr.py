import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df,x='Size of TV',y='Average time spent watching TV in a week')
        fig.show()
def getDataSource(data_path):
    Size=[]
    hours=[]
    with open(data_path) as csv_file:
        csvReader=csv.DictReader(csv_file)
        for row in csvReader:
            hours.append(float(row['Average time spent watching TV in a week']))
            Size.append(float(row['Size of TV']))
    return {'x':Size,'y':hours}
def findCorelation(DataSource):
     Corelation=np.corrcoef(DataSource['x'],DataSource['y'])
     print('Corelation between Size of TV  and Hours spend watching TV',Corelation[0,1])
def setup():
    data_path='./TVH.csv'
    plotFigure(data_path)
    DataSource=getDataSource(data_path)
    findCorelation(DataSource)
setup()