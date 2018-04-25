from mesa.visualization.ModularVisualization import ModularServer
from .model import SwarmModel

from mesa.visualization.modules import CanvasGrid
from mesa.visualization.modules import ChartModule
from mesa.visualization.UserParam import UserSettableParameter


def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "r": 0.5}

    if agent.stable:
        portrayal["Color"] = "green"
        portrayal["Layer"] = 0
    else:
        portrayal["Color"] = "red"
        portrayal["Layer"] = 1
        portrayal["r"] = 0.4
    return portrayal


grid = CanvasGrid(agent_portrayal, 50, 50, 500, 500)
chart = ChartModule([
    {"Label": "Connections", "Color": "#0000FF"}],
    data_collector_name='datacollector'
)
stabilitychart= ChartModule([
    {"Label": "Stability", "Color":"#0B6623"}
], data_collector_name='datacollector')
feidler= ChartModule([
    {"Label": "Feidler", "Color":"#B20000"}
])
area= ChartModule([
    {"Label":"Area", "Color":"#FF7F24"}
])
model_params = {
    "N": UserSettableParameter('slider', "Number of agents", 50, 2, 100, 1,
                               description="Choose how many agents to include in the model"),
    "width": 50,
    "height": 50,
    "numNeighbors": UserSettableParameter('slider', "Number of Neighbors", 4, 2,20), 
    "swarmType": UserSettableParameter('choice', 'Swarm Type', value='Basic',
                                              choices=['Basic', 'Roots'])
}

server = ModularServer(SwarmModel, [grid, chart, stabilitychart,feidler, area], "Swarm Model", model_params)
server.port = 8521
