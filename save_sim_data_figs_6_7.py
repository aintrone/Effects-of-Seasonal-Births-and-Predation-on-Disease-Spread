from scipy.integrate import trapz
import csv
import numpy as np
import sim_functions

# Name of csv file 
filename = "Fig7b_pulse_data.csv"

#g = np.concatenate([np.linspace(0.1,5,20), np.linspace(6,50,45)]) # g values for 7a
g = np.concatenate([[0.1], np.linspace(1,50,50)]) # g values for 7b
#g = np.concatenate([np.linspace(0.1,2,3), np.linspace(3,5,15), np.linspace(6,50,45)]) # g values for 7d

#delta = np.concatenate([np.linspace(0,3,14), np.linspace(4,80,77)]) # delta values for figure 6

# Change these parameters depending on the figure
initial_y0 = [100,1]
b = 10
Beta = 2
delta = 5 
a = 12
#g = 100
d = a/g
c = 1

# writing to csv file 
with open(filename, 'w') as csvfile: # Switch 'w' to an 'a' to append to an existing csv file
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # Pulsed birth simulations - comment below code chunk to run constant birth simulations
    # writing the fields - comment for existing file
    csvwriter.writerow(['Avg_Infect_over_1_period','g_val','Initial_Conditions','Max_total_pop','Min_total_pop', 'period']) 

    for i in g: # Fig 7
    #for i in delta: # Fig 6
        print(i)
        result = sim_functions.solver_pulse_hyp(initial_y0, b, Beta, delta, a, i, c) # Fig 6, 7
        #result = sim_functions.solver_pulse_lin(initial_y0, b, d, Beta, i) # Fig 6
        Infecteds = np.array(result[1])
        Susceptibles = np.array(result[0])
        Total_pop = Infecteds + Susceptibles
        if result[3] == '>6': #If the period is greater than 6
            csvwriter.writerow([None,i,initial_y0,None,None, result[3]])
        else:
            csvwriter.writerow([trapz(result[1],result[2])*(1/result[3]),i,initial_y0,np.max(Total_pop),np.min(Total_pop), result[3]])
        initial_y0 = [result[0][-1]+b,result[1][-1]] # use the ending S and I values as initial conditions for next simulation


    # # Constant birth simulations - comment below code chunk to run pulsed birth simulations
    # # writing the fields - comment for existing file
    # csvwriter.writerow(['Avg_Infect_over_1_period','g_val','Initial_Conditions','Max_total_pop','Min_total_pop']) 

    # for i in g: # Fig 7
    #     print(i)
    #     result = sim_functions.solver_constant_hyp(initial_y0, b, Beta, delta, a, i, c) # Fig 7
    #     Infecteds = np.array(result[1])
    #     Susceptibles = np.array(result[0])
    #     Total_pop = Infecteds + Susceptibles
    #     csvwriter.writerow([trapz(result[1],result[2]),i,initial_y0,np.max(Total_pop),np.min(Total_pop)])



    # Close the file object
    csvfile.close()

