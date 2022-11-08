#sent = "Time flies like an arrow"
icecream = "3 1 3"
#x_seq = sent.split()
#x_seq = icecream.split() 

Q = ('N','V','Adj','Adv') # All possible states (Part of Speech)
O = ('Islam', 'necessitates', 'having','good','moral','qualities') #Observations/words
SP = {'N': 0.5, 'V': 0.3, 'Adj': 0.1, 'Adv': 0.1} #Start Probability for each POS

#Hint : You have to encode all transitions from all possible states to all other possible states even if the values are not stated (i.e, give them a probability of 0 or 1)
TP = {'N' : {'N': 0.1, 'V': 0.6, 'Adj': 0.2, 'Adv': 0.1},
      'V' : {'N': 0.5, 'V': 0.1, 'Adj': 0.15, 'Adv': 0.25},
      'Adj' : {'N': 0.6, 'V': 0.2, 'Adj': 0.1, 'Adv': 0.1},
      'Adv' : {'N': 0.05, 'V': 0.15, 'Adj': 0.6, 'Adv': 0.2}
      }
	  
EP = {'N' : {'Islam': 0.1,'necessitates': 0, 'having': 0, 'good': 0.4, 'moral': 0.15, 'qualities': 0.35},
      'V' : {'Islam': 0, 'necessitates': 0.2, 'having': 0.8, 'good': 0, 'moral': 0, 'qualities': 0},
      'Adj' : {'Islam': 0, 'necessitates': 0, 'having': 0, 'good': 0.7, 'moral': 0.3, 'qualities': 0},
      'Adv' : {'Islam': 0, 'necessitates': 0, 'having': 0, 'good': 0.2, 'moral': 0, 'qualities': 0}}

#TP = transition_probability
#EP = emission_probability

# this function consider all possible combination of states = pow(2,n)
def viterbi(O, Q, SP, TP, EP):    
    #a set that hold the final best probable path for the list of observations (max alpha)
    T = {}
    
    #for every possible state in Q
    for q in Q:
        #get probability of each starting state, create a tuple(pair of values)
        T[q] = (SP[q], [q]) #example: T[q] = (0.4,['Sunny'])        

    #for every possible observations in O
    for x in O:
        #create a set/dictionary to hold prob. for each observation
        U = {}       

        #for every next state in Q states
        for q_next in Q:

            #initialize max path and max_p
            max_path = None;
            max_p = 0

            #for every state in Q
            for q in Q:

                #set prob and path = prob of each start state
                (prob, path) = T[q]
                
                #calculate prob. of alpha[i,j]
                p = prob * TP[q][q_next] * EP[q_next][x]

                #compare p with default max_p
                if p > max_p:
                    max_p = p;
                    max_path = path+[q_next] #concatenation of paths

            #pick the best path at each alpha
            U[q_next] = (max_p, max_path)
            
        #print(U)    
        T = U

    return(T)

path = viterbi(O, Q, SP, TP, EP)
print(path)

