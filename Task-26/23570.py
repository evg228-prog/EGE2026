with open(r'.\files\26_23570.txt') as file:
    N, K = map(int, file.readline().split())
    file = file.readlines()
    dachas = [int(i) for i in file[:N]]
    machines = [list(map(int, i.split())) for i in file[N:]]

dachas = sorted(dachas)
machines = sorted(machines, key=lambda x: (x[1], -x[0]))

summ = 0
last_mod = 0
for dacha in dachas:
    for machine in machines.copy():
        if machine[0] >= dacha:
            summ += machine[1]
            last_mod = machine[0]
            break
        else:
            machines.remove(machine)
print(summ, last_mod)

# 1879667450 924