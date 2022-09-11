def convert_list(actions):
    thanos = []
    splitted_actions = actions.split(',')
    for i in range(0, len(splitted_actions)):
        if(splitted_actions[i] != ","):
            thanos.append(splitted_actions[i])
    return thanos 

def thanos_split(code,get):
    split_par = code.split("]")
    
    split_par2 = split_par[0].split("[")
    actions = split_par2[1]
    url = split_par[1]
    if(get=="url"):
        return str(url)
    elif(get=="actions"):
        return convert_list(actions)