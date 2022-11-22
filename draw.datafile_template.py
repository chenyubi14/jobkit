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

data=np.loadtxt(filename) # this one works for data with several columns.
# np.loadtxt has other tags like 
##	dtype=<class 'float'>, data type, could be str or float
##	comments='#', ignore comments in the data file, could be ['#', '!']
##	delimiter=None, string used to separate values, default is whitespace, could be commas, dots, etc
##	skiprows=0, skip the first few rows of the data file, which are usually comments
##	usecols=None, use specific columns in the data file, will ignore other columns
# if the above does't work, consider np.genfromtxt
## np.genfromtxt is a more general function which can handle txt with missing values
##	invalid_raise=False, can ignore the invalid columns errors, and continue reading the data file
###		This is useful when the data file has a mixed number of columns, and 
###		like 3-column gives one type of data and 11-column gives another type.
###		You can use "skip_header=1, invalid_raise=False" combined to achieve the automatic reading of different columns
###		It will assume the number of columns is same as the first row it encounters

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
