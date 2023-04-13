#subroutine to model the change in num of prey and num of predators
def NumOfPreyAndPred(Prey, Predators, A, B, C, D, E):
    counter = 0
    while Prey > 1 and Predators > 1:
        counter = counter + 1
        PreyGrowth = E**(A-(C*Predators))
        Prey = Prey*PreyGrowth // 1
        PredatorsGrowth = E**((D*C*Prey)-B)
        Predators = Predators*PredatorsGrowth // 1
        print("Generation {}: \n Prey = {} \n Predators = {} \n".format(counter, Prey, Predators))


#Main
NumOfPreyAndPred(30, 5, 0.8, 0.5, 0.1, 0.3, 2.718)
