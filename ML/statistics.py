import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
print(f"Mean = {np.mean(speed)}")
print(f"Median = {np.median(speed)}")
print(f"Mode = {stats.mode(speed)}")
print(f"Standard Deviation = {np.std(speed)}")
print(f"Variance = {np.var(speed)}")
print(f"Percentile = {np.percentile(speed, 90)}") # Calculate the speed 90% cars are slower than



#generate 250 values randomly between 1-5
data = np.random.uniform(1.0, 5.0, 250)
print(data)

#plt.hist(data, 5) #Represent data with 5 bars on histogram
#plt.show()


data1 = np.random.uniform(1.0, 10.0, 1000000)
#plt.hist(data1, 50)
#plt.show()

#normal distribution
normaldata = np.random.normal(1.0, 10.0, 1000000)
#plt.hist(normaldata, 50)
#plt.show()
#plt.scatter(normaldata,data1)
#plt.show()


x1 = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y1 = [99,86,87,88,111,86,103,87,94,78,77,85,86]


slope, intercept, r, p, std_err = stats.linregress(x1, y1)
print(f"slope = {slope}, intercept = {intercept}")
def drawline(x):
    line = (slope * x) + intercept
    return line

mymodel = list(map(drawline, x1))
print(mymodel)
#plt.scatter(x1, speed)
#plt.plot(x1, mymodel)
#plt.show()

#predict the speed of 10 year old car

predictspeed = drawline(10)
print(predictspeed)

#Bad Correlation/lesser r value depicts the linear regression will result in bad fit.


x2 = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y2 = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x2, y2)


mymodel = list(map(drawline, x2))

plt.scatter(x2, y2)
plt.plot(x2, mymodel)
plt.show()
print(f"R value: {r}")  #smaller value i.e. 0.013 denotes a bad fit i.e. straight line as data is not normal distribution



