def aa(x):
  return x**2

print(aa(3))


def deriv(aa,x):
  deltax=(1/1000000)
  return (aa(x+deltax) - aa(x))/deltax
  
for i in range(-3,4):
  print(i,deriv(aa,i))


# import matplotlib.pyplot as plt
# import numpy as np


"""
# 100 linearly spaced numbers
x = np.linspace(0,1,10)
eta1=0.05
eta2=0.1
lmd1= 2.8
# the function, which is y = x^2 here
y = 0.5*(-(1/3)*eta1*x**2 + np.sqrt( ((1/3)*eta1*x**2)**2-4*(3*x**2*2.8**2-1)) 

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the function
plt.plot(x,y, 'r')

# show the plot
plt.show()
"""