from simtk.openmm import *
from simtk.openmm.app import *
from simtk.unit import *

pdb = PDBFile('villin.pdb')
topology = pdb.topology
positions = pdb.positions

platform = Platform.getPlatformByName('Reference')
ff = ForceField('ff14SB.xml')
system = ff.createSystem(topology)
integrator = VerletIntegrator(1*femtosecond)

simulation = Simulation(topology, system, integrator, platform)
simulation.context.setPositions(positions)

print("The ffxml potential energy is: %s" % simulation.context.getState(getEnergy=True).getPotentialEnergy())

prmtop = AmberPrmtopFile('ff14SB.top')
inpcrd = AmberInpcrdFile('ff14SB.crd')

system2 = prmtop.createSystem()
integrator2 = VerletIntegrator(1*femtosecond)

simulation2 = Simulation(prmtop.topology, system2, integrator2, platform)
simulation2.context.setPositions(inpcrd.positions)

print("The AMBER potential energy is: %s" % simulation2.context.getState(getEnergy=True).getPotentialEnergy())
