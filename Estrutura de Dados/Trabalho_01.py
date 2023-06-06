while entrada != 'stop':
    entrada = input().split()
    if entrada[0] == 'enqueue':
        for i in range(entrada[1]):
            processo = input().split()
            if processo [1] == 'scramble':
                temp = []
                for j in processo[2:]:
                    temp.append(int(j))
                