import numpy as np
import csv
from scipy.integrate import trapz
import sim_functions

##### Saving simulation data for Figure 4a #####

# Name of csv file
filename = "Fig4a_data.csv"

# Parameters for Fig 4a
b = [0.01, 0.1, 0.3, 0.5, 0.65, 0.8, 1.0] 
initial_y0 = [100,0] # solutions will be period 1
Beta = 50
delta = 5 
a = 20
g = 5
c = 1

# writing to csv file
with open(filename, 'w') as csvfile: # Switch 'w' to an 'a' to append to an existing csv file
   # creating a csv writer object
   csvwriter = csv.writer(csvfile)
    
   # writing the fields - comment for existing file
   csvwriter.writerow(['b_val','int_S','int_g']) 

   for i in b:
    result = sim_functions.solver_pulse_hyp(initial_y0, i, Beta, delta, a, g, c)
    
    # writing the data rows
    int_S = trapz(result[0],result[2])
    TotalSg = result[0] + g  # TotalS + g
    InverseS = np.reciprocal(TotalSg)
    int_g = trapz(InverseS,result[2])
    csvwriter.writerow([i,int_S,int_g])
   
   # Close the file object
   csvfile.close()


##### Saving simulation data for Figures 4b-d #####
# Note: the number of years run to avoid transient behavior was increased to 1050 in solver_pulse_hyp() to reach period 1 solution for Fig. 4d

# Name of csv file
filename = "Fig4bcd_data.csv"

# Constant Params for b-d
initial_y0 = [100,0] # solutions will be period 1
c = 1
Beta = 50
delta = 5 

# Parameters [b,a,g,'figure_letter'] for figures b-d
params = [[10,20,5,'b'], [10,200,50,'c'], [19,20,5,'d']]

# writing to csv file
with open(filename, 'w') as csvfile: # Switch 'w' to an 'a' to append to an existing csv file
   # creating a csv writer object
   csvwriter = csv.writer(csvfile)
    
   # writing the fields - comment for existing file
   csvwriter.writerow(['fig_letter','int_S','int_g']) 

   for i in params:
    result = sim_functions.solver_pulse_hyp(initial_y0, i[0], Beta, delta, i[1], i[2], c)
    
    # writing the data rows
    int_S = trapz(result[0],result[2])
    TotalSg = result[0] + i[2]  # TotalS + g
    InverseS = np.reciprocal(TotalSg)
    int_g = trapz(InverseS,result[2])
    csvwriter.writerow([i[3],int_S,int_g])
   
   # Close the file object
   csvfile.close()







