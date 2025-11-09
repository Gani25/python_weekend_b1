import cricket_player_class as cpc

virat = cpc.cricket_player("Virat","Kohli",1987,"Male","India")

virat.add_runs(50)
virat.add_runs(60,80,35)

print(virat)

chris = cpc.cricket_player("Chris","Gayle",1983,"Male","Australia")

chris.add_runs(100)
chris.add_runs(10,50)
chris.add_runs(95,49)

print(chris)


# Try same thing but with football players -> goals