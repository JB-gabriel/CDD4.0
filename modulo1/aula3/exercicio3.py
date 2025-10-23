time1=input("time 1: ")
time2=input("time 2: ")
gols1=int(input("gols 1: "))
gols2=int(input("gols 2: "))

if gols1>gols2:
    print(f"O vencedor é o time {time1} com total de gols: {gols1}")
elif gols1==gols2:
    print("empate")
else:
    print(f"O vencedor é o {time2} com o total de gols: {gols2}")
