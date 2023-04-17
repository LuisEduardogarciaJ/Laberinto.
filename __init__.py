
from pyamaze import maze,agent

#--------------------------------------------
#Crear un laberinto
#---------------------------------------------
m=maze(25,40)
m.CreateMaze()

#----------------------------------------------
#Por agente en el laberinto
#----------------------------------------------
a=agent(m, footprints=True,filled=True)

#-------------------------------------------------
#Graficar trayectoria del agente
#--------------------------------------------------
m.tracePath({a:m.path},delay=25)
m.run()