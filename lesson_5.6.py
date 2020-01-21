plan = {}
hours = []
with open('less_5.6.txt') as m_file:
    for i in m_file:
        i_spl = i.split()
        #print(i_spl[0])
        i_nam = i_spl[0]
        all_h = i_spl[1:]
        plan[i_nam] = 0
        for types in all_h:
            try:
                plan[i_nam] += int(types[:types.find("(")])
            except ValueError:
                pass
    print(plan)