import pandas
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

data = pandas.read_csv('iphone_price_dataset.csv')
# print(data.head())                                     # head() returns the first five rows of the data.
plt.scatter(data['version'],data['price'])               # scatter() method takes columns as a parameter.
print("Graphical representation of the iphone (version vs price) is : ")
print(plt.show())                                        # show() method dislays the data in the form of graph.

# .......NOW SOURCE CODE FOR PRICE PREDICTION PART ...

ml_model = LinearRegression()
ml_model.fit(data[['version']],data[['price']])          # fit() method requires parmeters in the form of 2-D array.
print("Enter the iphone version to predict its price : ")
n=int(input())
result = ml_model.predict([[n]])
print("The price of the iphone version - {} will be : \n{} $.".format(n,result[0][0]))
print("{} $ ==> {} INR ".format(result[0][0],result[0][0]*74.59))

print("......... IPHONE PRICE PREDICTION COMPLETED .........")