#from wikipedia : https://en.wikipedia.org/wiki/Viterbi_algorithm#Example

obs = ('Practicing', 'Islam', 'beautifies', 'individual', 'character')
states = ('V', 'ADJ', 'N')
start_p = {'V': 0.3, 'ADJ': 0.3, 'N': 0.4}
trans_p = {'V': {'N': 0.6, 'ADJ': 0.3, 'V': 0.1}, 'ADJ': {'N': 0.6, 'ADJ': 0.1, 'V': 0.3}, 'N': {'N': 0.1, 'ADJ': 0.2, 'V': 0.7}}

emit_p = {'V': {'Practicing': 0.3, 'beautifies': 0.7,'Islam': 0, 'individual': 0, 'character': 0},
          'ADJ': {'individual': 0.5, 'Practicing': 0.3, 'character': 0.2, 'Islam': 0, 'beautifies': 0},
          'N':{'Islam': 0.2, 'individual': 0.4, 'character':0.4, 'Practicing':0, 'beautifies': 0}}

def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    for st in states:
        V[0][st] = {"prob": start_p[st] * emit_p[st][obs[0]], "prev": None}

    # Run Viterbi when t > 0
    for t in range(1, len(obs)):
        V.append({})
        for st in states:
            max_tr_prob = max(V[t-1][prev_st]["prob"]*trans_p[prev_st][st] for prev_st in states)
            for prev_st in states:
                if V[t-1][prev_st]["prob"] * trans_p[prev_st][st] == max_tr_prob:
                    max_prob = max_tr_prob * emit_p[st][obs[t]]
                    V[t][st] = {"prob": max_prob, "prev": prev_st}
                    break
    for line in dptable(V):
        print(line)
    opt = []
    
# The highest probability
    max_prob = max(value["prob"] for value in V[-1].values())
    previous = None
    # Get most probable state and its backtrack
    for st, data in V[-1].items():
        if data["prob"] == max_prob:
            opt.append(st)
            previous = st
            break

    # Follow the backtrack till the first observation
    for t in range(len(V) - 2, -1, -1):
        opt.insert(0, V[t + 1][previous]["prev"])
        previous = V[t + 1][previous]["prev"]

    print(V)
    print('The steps of states are ' + ' '.join(opt) + ' with highest probability of %s' % max_prob)
    return V

def dptable(V):
    # Print a table of steps from dictionary
    yield " ".join(("%12d" % i) for i in range(len(V)))
    for state in V[0]:
        yield "%.7s: " % state + " ".join("%.7s" % ("%f" % v[state]["prob"]) for v in V)
        
viterbi(obs, states, start_p, trans_p, emit_p)
