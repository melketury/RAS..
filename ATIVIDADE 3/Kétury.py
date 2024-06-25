from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np
import time

client = RemoteAPIClient()
sim = client.getObject('sim')

print("Iniciando simulação...")
sim.startSimulation()

#motores
roda_direita = sim.getObject('/direita')  
roda_esquerda = sim.getObject('/esquerda')  
print("Motores obtidos com sucesso.")

L = 0.172  
r = 0.065  

v = 0.2  
w = 0  

wr = ((2.0 * v) + (w * L)) / (2.0 * r)
wl = ((2.0 * v) - (w * L)) / (2.0 * r)

print(f"Velocidade angular da roda direita (wr): {wr}")
print(f"Velocidade angular da roda esquerda (wl): {wl}")


sim.setJointTargetVelocity(roda_direita, wr)
sim.setJointTargetVelocity(roda_esquerda, wl)
print("Velocidades definidas com sucesso.")

time.sleep(10)  

print("Parando a simulação...")
sim.stopSimulation()

print("Encerrando conexão...")
client.close()
print("Conexão encerrada.")
