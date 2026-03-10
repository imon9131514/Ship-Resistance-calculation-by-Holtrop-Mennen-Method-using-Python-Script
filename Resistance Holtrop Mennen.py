import math

def calculate_variables(E2,E3,E4,E5,E6,E7,E8,E9,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22):
    E25 = (E19/(9.8*E2)**(1/2))                 #Froude Number
    E26 = E20/E11                               #Prismatic Co-efficient
    E27 = (-0.75/100)*(E2*0.5)                  #Longitudinal Position of the Centre of Forward of Half Length as a % of Length
    E28 = (1-E26+(0.06*E26*E27/(4*E26-1)))*E2   #Parameter Reflecting the Length of the Run
    if (E5/E2) > 0.05 :                              
        E29 = (E5/E2)**0.2228446
    elif 0.02<(E5/E2) and (E5/E2) < 0.05 :
        E29 = 48.2*(E5/E2-0.02)**(2.078)+0.479948
    else :
        E29 = 0.479948                              #Co-Efficient Accounted for Average Moulded Draft over Length Value
    E30 = (1+0.003*E15)                             #Co-Efficient Accounted for Specific Shape of the Afterbody
    E31 = E30*(0.93+E29*(E4/E28)**(0.92497)*(0.95-E26)**(-0.521448)*(1-E26+0.0225*E27)**(0.6906))                   #Factor describing Viscous Resistance of the Hull form
    E32 = E2*((2*E5)+E4)*((E11)**(1/2))*(0.453+0.4425*E20-0.2862*E11-0.003467*(E4/E5)+0.3696*E12)+2.38*(E9/E20)     #Wetted area of the Hull
    E34 = (E2*E19)/(1.1902*10**(-6))                #Reynold's Number
    E35 = 0.075/(math.log(E34)-2)**2                      #Friction Co-Efficient
    E33 = 0.5*1025*E32*E19**(2*E35)                  #Frictional Resistance
    E36 = 0                                         #Appendages Resistance Factor (1+k2)
    E37 = 0.5*1025*(E19**2)*E14*E36*E35              #Resistance Appendages
    if (E4/E2)<0.11 :
        E38 = 0.229577*(E4/E2)**0.33333
    elif (E4/E2)>0.25 :
        E38 = 0.5-0.0625*(E4/E2)
    else : 
        E38 = E4/E2                                 #Parameter Accounted for Breadth over Length
        
        
    #E39 = 1+89*(math.exp((-1)*((E2/E4)**(0.80856))*((1-E12)**(0.30484))*((1-E26-0.0225*E27)**(0.6367))*((E28/E4)**(0.34574))*((100*(E7/E2**3))**(0.16302))))
    E39 = 1 
    #Angle of the Waterline at the Bow in Degrees with Referenace to the Centre Plane
    
    E40 = 2223105*E38**(3.78613)*(E5/E4)**(1.07961)*(90-E39)**(-1.37565)       #Parameter Accounted for Average Moulded Draft, Breadth and iE

    E41 = ((0.56*E9**(1.5))/(E4*E5*(0.31*E9**(1/2)+E5-E10)))                   #Co-Efficient that Determines the Influence of the Bulbous Bow on the Wave Resistance

    E42 = math.exp(-1.89*E41**(1/2))                                          #Parameter Accounted for the Reduction of the RW due to the Action of Bulbous Bow

    E43 = 1-0.8*E13/(E4*E5*E11)                                             #Influence of a Transom Stern on the Wave Resistance
    
    if E26<0.8 :
        E44 = 8.07981*E26-13.8673*E26**(2)+6.984388*E26**(3)
    else :
        E44 = 1.73014-0.7067*E26                                        #Co-Efficient dependant on CP
    E45 = 0.0140407*(E2/E5)-1.75254*E7**(1/3)/E2-4.79323*(E4/E2)-E44     #Co-efficient m1
    
    if (E2**3/E7)<512 :
        E46 = -1.69385
    elif (E2**3/E7)>1727 :
        E46 = 0
    else :
        E46 = -1.69385+(E2/E7**(1/3)-8)/2.36                             #Co-Efficient dependant on Length and Displacement
        
    E47 = E46*E26**2*(math.exp(-0.1*E25**(-2)))                           #Co-Efficient m2
    if (E2/E4)<12 :
        E48 = 1.446*E26-0.03*(E2/E4)                                    #Co-Efficient lamda λ
    else :
        E48 = 1.446*E26-0.36
    E49 = E40*E42*E43*E7*1025*9.8*(math.exp(E45*E25**(-0.9)+E47*math.cos(E48*E25**(-2))))      #Wave-Making & Wave-Breaking Resistance
    E50 = 0.56*math.sqrt(E9)/(E5-1.5*E10)                               #Co-Efficient for the Emergence of the Bow
    E51 = E19/(9.8*(E5-E10-0.25*(E9)**(1/2)+(0.15*E19**2)))**(1/2)         #Froude Number Based on the Immersion
    #E52 = 0.11*math.exp(-3*E50**(-2))*(E51**(3))*(E9**(1.5))*1025*9.8/(1+E51**2) #Additional Pressure Resistance of Bulbous Bow
    E53 = E19/math.sqrt(2*9.8*E13/(E4+E4*E12))                          #Froude Number Based on the Draft
    if E53<5 :
        E54 = 0.2*(1-0.2*E53)
    else :                                                              #Co-Efficient related to the Froude Number Based on the Transom Immersion
        E54 = 0                                                         
    E55 = 0.5*1025*(E19**2)*E13*E54                                        #Additional Pressure Resistance of Immersed Transom
    if (E5/E2)>0.04 :
        E56 = 0.04                                                      #Co-Efficient dependant on Length and Forward Draft
    else :
        E56 = E5/E2
    E57 = ((0.105*(3.8742*10**(-4))**(1/3))-0.005579)/E2**(1/3)            #Correlation Allowance Co-Efficient
    E58 = 0.5*1025*(E19**2)*E57*E32                                        #Model-ship Correlation Resistance
    
    #E59 = E33*E31+E37+E49+E52+E55+E58                                   #Total Resistance
    E60 = E33*E31+E37+E49+0+0+E58                                       #Total Resistance Without Bow
    
    return E60

# Taking input for the variables
E2 = float(input("Enter value for LWL: "))
E3 = float(input("Enter value for LBP: "))
E4 = float(input("Enter value for Breadth Moulded: "))
E5 = float(input("Enter value for Draught Moulded on F.P : "))
E6 = float(input("Enter value for Draught Moulded on A.P : "))
E7 = float(input("Enter value for Displacement Volume Moulded : "))
E8 = float(input("Enter value for Longitudinal Centre Of Buoyancy: "))
E9 = float(input("Enter value for Transverse Bulb Area: "))
E10 = float(input("Enter value for Centre Of Bulb Area above keel line: "))
E11 = float(input("Enter value for Midship Section Co-efficient: "))
E12 = float(input("Enter value for Waterplane Area CO-efficient: "))
E13 = float(input("Enter value for Transom Area: "))
E14 = float(input("Enter value for Wetted Area Appendages: "))
E15 = float(input("Enter value for Stern Shape Parameter: "))
E16 = float(input("Enter value for Propeller Diameter: "))
E17 = float(input("Enter value for Number of Propeller Blades: "))
E18 = float(input("Enter value for Clearance Propeller with keel line: "))
E19 = float(input("Enter value for Ship Speed: "))
E20 = float(input("Enter value for Block Co-efficient: "))
E21 = float(input("Enter value for Immersion of Propeller Shaft: "))
E22 = float(input("Enter value for Density in kg/m3: "))

E60 = calculate_variables(E2,E3,E4,E5,E6,E7,E8,E9,E10,E11,E12,E13,E14,E15,E16,E17,E18,E19,E20,E21,E22)

# Printing the calculated results
#print("Total Resistance is :", E59)
print("Total Resistance without Bulbous Bow is :", E60)
