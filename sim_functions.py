from scipy.integrate import solve_ivp
import numpy as np

## Constant Birth Models
def deriv_y_lin_constant(t,y,b,d,Beta,delta):
  S, I = y
  dS = b - d*S - Beta*I*S
  dI = Beta*I*S - d*I - delta*I
  return [dS,dI]

def deriv_y_hyp_constant(t,y,b,Beta,delta,a,g,c):
  S, I = y
  dS = b - Beta*I*S - a*S/(g+S+c*I)
  dI = Beta*I*S - delta*I - a*c*I/(g+S+c*I)
  return [dS,dI]


## Pulsed Birth Models
def deriv_y_lin_pulse(t,y,d,Beta,delta):
  S,I = y
  dS = - d*S - Beta*I*S
  dI = Beta*I*S - d*I - delta*I
  return [dS,dI]

def deriv_y_hyp_pulse(t,y,Beta,delta,a,g,c):
  S,I = y
  dS = - Beta*I*S - a*S/(g+S+c*I)
  dI = Beta*I*S - delta*I - a*c*I/(g+S+c*I)
  return [dS,dI]

def period_tracker(svals):
    if np.max(svals) - np.min(svals) < 0.0001:
        period = 1
    else: #Not period 1
        data = svals[::2]
        if np.max(data) - np.min(data) < 0.0001:
            period = 2
        else: # Not period 1 or 2
            data = svals[::3]
            if np.max(data) - np.min(data) < 0.0001:
                period = 3
            else:
                data = svals[::4]
                if np.max(data) - np.min(data) < 0.0001:
                    period = 4
                else:
                    data = svals[::5]
                    if np.max(data) - np.min(data) < 0.0001:
                        period = 5
                    else:
                        data = svals[::6]
                        if np.max(data) - np.min(data) < 0.0001:
                            period = 6  
                        else:
                            print('Period greater than 6')
                            period = '>6'
                            print(svals)
    return period

## Constant birth simulations
def solver_constant_lin(IC, b, d, Beta, delta):
    for i in range(0,2):
        if i == 0:
            t = np.linspace(0,350,200) 
            time = [0,350]
            y0 = IC
        else:
            t = np.linspace(0,1,1000) # times to integrate for: t=0 to t=1 years, 1000 time points in range
            time = [0,1]
            y0 = [S[-1],I[-1]] # use number of susceptibles and infecteds from the end of the first integration as the new initial conditions
        ysol = solve_ivp(deriv_y_lin_constant,time,y0,method='RK45',args=(b,d,Beta,delta),dense_output=True, rtol = 1e-13, atol = 1e-323)
        S,I=ysol.sol(t)
    return [S,I,t]

def solver_constant_hyp(IC, b, Beta, delta, a, g, c):
    for i in range(0,2):
        if i == 0:
            t = np.linspace(0,350,200)
            time = [0,350]
            y0 = IC
        else:
            t = np.linspace(0,1,1000)
            time = [0,1]
            y0 = [S[-1],I[-1]]
        ysol = solve_ivp(deriv_y_hyp_constant,time,y0,method='RK45',args=(b,Beta,delta,a,g,c),dense_output=True, rtol = 1e-13, atol = 1e-323)
        S,I=ysol.sol(t)
    return [S,I,t]


## Pulsed birth simulations
def solver_pulse_lin(IC, b, d, Beta, delta):
    # Initialize storage arrays
    svals = np.array([])
    TotalS = np.array([])
    TotalI = np.array([])
    Total_time = np.array([])
    for i in range(0,2):
        if i == 0:
            year = 350
        else:
            year = period 
            #year = 5 
        for t in range(0,year):
            # Create time steps for one year
            time = np.linspace(t,t+1,500)
            time2 = [t,t+1]
            if i ==0 and t == 0:
                y0 = IC 
            else:
                # Add birth pulse
                y0 = [S[-1]+b,I[-1]]
            print('sim num: ' + str(t))
            ysol = solve_ivp(deriv_y_lin_pulse,time2,y0,method='Radau',args=(d,Beta,delta),dense_output=True,rtol=1e-13, atol=1e-323)
            S,I=ysol.sol(time)
            if t >= 300:
                # Track number of susceptibles at the start of each year, used to calculate period
                svals = np.append(svals,S[0])
            if t == 349:
                period = period_tracker(svals)
                if period == '>6':
                    TotalS = np.append(TotalS,S[-1])
                    TotalI = np.append(TotalI,I[-1])
                    return [TotalS,TotalI,Total_time,period]
            if i == 1:
                # Store solution for each year, remove overlapping time steps and solutions
                TotalS = np.append(TotalS,S[:-1])
                TotalI = np.append(TotalI,I[:-1])
                Total_time = np.append(Total_time,time[:-1])
    return [TotalS,TotalI,Total_time,period]

def solver_pulse_hyp(IC, b, Beta, delta, a, g, c):
    # Initialize storage arrays
    svals = np.array([])
    TotalS = np.array([])
    TotalI = np.array([])
    Total_time = np.array([])
    for i in range(0,2):
        if i == 0:
            year = 350
        else:
            year = period 
        for t in range(0,year):
            # Create time steps for one year
            time = np.linspace(t,t+1,500)
            time2 = [t,t+1]
            if i ==0 and t == 0:
                y0 = IC 
            else:
                # Add birth pulse
                y0 = [S[-1]+b,I[-1]]
            print('sim num: ' + str(t))
            ysol = solve_ivp(deriv_y_hyp_pulse,time2,y0,method='Radau',args=(Beta,delta,a,g,c),dense_output=True,rtol=1e-13, atol=1e-323)
            S,I=ysol.sol(time)
            if t >= 300:
                # Track number of susceptibles at the start of each year, used to calculate period
                svals = np.append(svals,S[0])
            if t == 349:
                period = period_tracker(svals)
                if period == '>6':
                    TotalS = np.append(TotalS,S[-1])
                    TotalI = np.append(TotalI,I[-1])
                    return [TotalS,TotalI,Total_time,period]
            if i == 1:
                # Store solution for each year, remove overlapping time steps and solutions
                TotalS = np.append(TotalS,S[:-1])
                TotalI = np.append(TotalI,I[:-1])
                Total_time = np.append(Total_time,time[:-1])
    return [TotalS,TotalI,Total_time,period]