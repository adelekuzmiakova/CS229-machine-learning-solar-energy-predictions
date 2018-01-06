
import numpy as np
import matplotlib.pyplot as plt

def main():
	x = np.loadtxt('xdata.txt')
    x = np.hstack((np.ones((x.shape[0], 1)),x)) 
    y = np.loadtxt('ydata.txt')
    theta = np.zeros(np.add(2, 1))
    # Define tolerance (the error term), delta, and iteration count: 
    tolerance = 1e-10
    delta = 100
    it = 0
    while delta > tolerance:
    	loss1 = loss(x, y, theta)
    	theta = np.subtract(theta, np.dot(np.dot(np.linalg.inv(hessian(x, theta)),
    		gradient(x,y,theta)), loss(x,y,theta))) loss2 = loss(x,y,theta)
    	delta = loss1 - loss2
    	it = it + 1
    	print(theta)

def hessian(x, theta):
	scale = np.multiply(sigmoid(np.dot(x, theta)), np.subtract(1, sigmoid(np.dot(x, theta)))) n = x.shape[0]
	p = x.shape[1]
	hess = np.zeros((p, p))
	for i in range(0, n):
		hess = np.add(hess, np.multiply(np.outer(x[i,], x[i,]), scale[i,])) 
	return np.divide(hess, np.negative(n))

def sigmoid(z):
	return np.divide(1, np.add(1, np.exp(np.negative(z))))

def gradient(x,y,theta):
	return np.divide(np.dot(np.multiply(sigmoid(np.multiply(np.negative(y),np.dot(x,theta))), y), x), x.shape[0])

def loss(x,y,theta):
	return np.divide(np.sum(np.log(np.add(1, np.exp(np.multiply(np.negative(y), np.dot(x,theta)))))), x.shape[0])
 
# Plot the scatterplot and decision boundary:
slope = np.divide(np.subtract(np.negative(theta[0]), np.multiply(theta[1], a)),theta[2])

plt.scatter(x=x[:,1], y=x[:,2], c=y, cmap='PiYG')
plt.plot(np.arange(0,10), slope, 'k-')
plt.axis([0,max(x[:,1])+1,-max(abs(x[:,2]))-1, max(abs(x[:,2]))+1]) # axis dimensions plt.xlabel('x1 data')
plt.ylabel('x2 data')
plt.title('Question 1 (c): Logistic regression') plt.savefig('Question_1_c.pdf')

if __name__ == "__main__": 
	main()