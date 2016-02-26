#!/usr/bin/env python
# from argparse import ArgumentParser
# from boids_master import BoidsMaster
# from getGraph import plotGreenDistribution
# from matplotlib import pyplot as plt

# def parseArgs():
#     '''
#     Entry point from the command line.

#     :Example:

#     >>> getGreenGraph --from London --to Cambridge --steps 10 --out outGraph.png
#     '''
#     prs= ArgumentParser(description="Greengraph package - Generates a graph with the proportion of green pixels between two locations")
#     prs.add_argument('--from',help='Start position, default = London', dest='startPos', default='London')
#     prs.add_argument('--to',help='End position, default = Cambridge', dest='endPos', default='Cambridge')
#     prs.add_argument('--steps',help='Number of steps between start and end, default = 10', default=10, type=int)
#     prs.add_argument('--out',help='Name of output image, default = outGraph.png', default='outGraph.png')
#     arguments=prs.parse_args()

#     plotGreenDistribution(arguments.startPos, arguments.endPos, arguments.steps,arguments.out)


# if __name__=='__main__':
#     parseArgs()
