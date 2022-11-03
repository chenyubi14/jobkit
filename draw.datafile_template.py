import numpy as np
import sys
import matplotlib.pyplot as plt


SMALL_SIZE = 12
MEDIUM_SIZE = 14
BIGGER_SIZE = 16

plt.rc('font', size=BIGGER_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
#plt.figure(figsize=(4,6))


# load data
if len(sys.argv) < 2:
	print('Error! Enter the dat filename as one argument')
	sys.exit()
print('Will plot the two columns in .dat or .txt file.')

filename= sys.argv[1] 

data=np.loadtxt(filename) # this one works

x=data[:,0]
y=data[:,1]


#####################################################################
labeltype=0 # no labels
# save your often used labels
#####################################################################

# edit lables
#####################################################################
if labeltype == 0:
	legend=''
	#plt.legend()
	title=''
	xlabel=''
	xlabelunit=' ()'
	ylabel=''
	ylabelunit=' ()'
	color='tab:red'
#####################################################################


# black, tab:blue, tab:green, tab:orange
plt.plot(x, y, color=color, label=legend)
#plt.scatter(x, y, color=color, label=legend)
plt.title(title) # add title
plt.xlabel(xlabel+xlabelunit) # x label 
plt.ylabel(ylabel+ylabelunit) # y label
plt.tight_layout()
#plt.ylim([0, 400])
#plt.ylim([0, 3000])


figname= filename[:-3] + 'png'
print('\tfigure saved as \n%s' % (figname))
plt.savefig(figname,dpi=600)

plt.show()
plt.close()
