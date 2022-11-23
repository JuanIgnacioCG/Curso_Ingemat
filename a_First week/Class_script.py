#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: gonzalo
"""

#This is a template for the class on data management for science/engineering purpose

#%% Importing data from a set of .csv files

# The best way to treat data from .csv files is the use of pandas library

# To use a library, the first step is to import the library

# =============================================================================
# import
# =============================================================================

# Once the library is imported we need to define the path to the folder containing the files (relative or absolute) 

# =============================================================================
# folder_path=
# =============================================================================

# And the name of the files, for this we may either list all of them individually
# or if we are interested in all the files of a folder we can use the listdir(path) command of the os library


# =============================================================================
# import os
# files=
# =============================================================================

# Files can now be read using pandas by creating a dataframe from each of them
# If the names have some kind of logic we can import them in a loop!

# =============================================================================
# numberofdays=10
# File_path=
# for i in range(numberofdays):
#     locals()['df'+str(i)]=pd.read_csv(File_path, index_col=0)       #Number to string formats in python https://pyformat.info/#number 
# =============================================================================

#%% Once the data is imported we should check if it is good.

# To use the data we can work using the dataframe, but numperical treatment of data is easier using numpy library

# =============================================================================
# import
# =============================================================================

# We can store all the data in several diferent maners, but today we are going to make 2 arrays
# 1 array for the Forces  and one for the displacements with shapes (n_points,n_tests)

# =============================================================================
# displacements=
# forces=
# =============================================================================

# First step is to check visually if the sata has sense -> plot (let's import the pyplot module of the matplotlib library)

# =============================================================================
# import 
# =============================================================================


# And plot some part of it both as lines and scattered points






# =============================================================================
# # Example with lines
# 
# figLines  = plt.figure()
# axLines=figLines.add_subplot(xlim=(np.min(displacements),np.max(displacements)),ylim=(np.min(forces),np.max(forces)))
# axLines.set_title('F-'+'\u0394'+'L with Lines')
# axLines.set_xlabel('disp [mm]')
# axLines.set_ylabel('F [N]')
# 
# for i in np.random.randint(0,n_curves,size=10):
#     axLines.plot(displacements[:,i],F[:,i],forces=str(i))   
# 
# axLines.legend()
# =============================================================================


# =============================================================================
# figPoints =
# axPoints=
# # title
# # xlabel
# # ylabel
# 
# for i in np.random.randint(0,n_curves,size=10):
#     axPoints.scatter()
#     
# axPoints.legend()
# =============================================================================

#%% And now we can manipulate    
# Data is from Force/displacemnt curves of samples with L0=10cm and circular section of 1cm diameter
# The displacement is in mm and the forces are in N

# First obtain the engineering stress/strain curves: S_e=F/A0;  e_e=displacement/L0 
# File prepared to work on MPa for stress and % for strain

# =============================================================================
# strain_eng=
# stress_eng=
# =============================================================================

# And the true stress/strain curves: e_T=Ln(1+e_e); S_T=S_e*(1+e_e)

# =============================================================================
# strain_true=
# stress_true=
# =============================================================================


# And plot the results:


# =============================================================================
# # Example with lines
# 
# figLines  = plt.figure()
# axLines=figLines.add_subplot(xlim=(np.min(displacements),np.max(displacements)),ylim=(np.min(forces),np.max(forces)))
# axLines.set_title('\u03c3'+'-'+'\u03B5'+'L with Lines')
# axLines.set_xlabel('\u03B5 [%]')
# axLines.set_ylabel('\u03c3'+' [MPa]')
# 
# for i in np.random.randint(0,n_curves,size=10):
#     axLines.plot(displacements[:,i],F[:,i],forces=str(i))   
# 
# axLines.legend()
# =============================================================================



#%% And we can try to fit our data to a model

# This data answers the following model: sigma=E*(epsilon-epsilon_p*np.exp(-1/(n*(epsilon_p))))
# Where epsilon_p is the plastic strain, which can be modeled with:
# epsilon_p=0 if epsilon<=e_y, epsilon_p=epsilon-e_y if epsilon>=e_y 
# and E, n and e_y are materials parameters

# We can use the following expresion for epsilon_p: 
# (epsilon_p=np.where(np.zeros_like(epsilon)>epsilon-e_y,np.zeros_like(epsilon),epsilon-e_y))


# To obtain the parameters of our curve, we can use scipy.optimize.curve_fit

# =============================================================================
# from scipy.optimize import curve_fit
# =============================================================================

# This method requires to program a function that depends first on the independent variables and then  to the parameters to fit
#  y=f(x,a,b,c)


# =============================================================================
# def func(epsilon,E,e_y,n):
# 
#     return(sigma)
# =============================================================================

# curvefit returns 2 data arrays:
    # first array (1D) has the mean values for each parameter
    # first array (2D) has the covariance for each parameter pair

# p_ave, p_cov = curve_fit(func, xdata, ydata, bounds=([100e3,0,1],[500e3,0.05,10])) %For one curve

# Lets plot the initial data and the fitted curve together for some curves

# =============================================================================
# # figFitted =
# axFitted=
# # title
# # xlabel
# # ylabel
# 
# for i in np.random.randint(0,n_curves,size=10):
#     axFitted.scatter()
# axFitted.plot()
# axFitted.legend()
# =============================================================================


#%% To end we can look at the values of the fitted parameters

# np.mean
# np.std

# histogram with them
# np.hist(vals, bins=nbins)


