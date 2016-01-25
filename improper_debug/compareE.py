import parmed as pmd
from simtk.openmm import *
from simtk.openmm.app import *
from simtk.unit import *

parm = pmd.load_file('ala399SBildn.top', 'ala399SBildn.crd')
system = parm.createSystem()

print('AMBER energies:')
print(pmd.openmm.energy_decomposition_system(parm, system, nrg=kilojoules_per_mole))

amber_total = 0
for i in pmd.openmm.energy_decomposition_system(parm, system, nrg=kilojoules_per_mole):
    amber_total += i[1]

print('Total: %s' % amber_total)

pdb = PDBFile('ala3.pdb')
topology = pdb.topology

ff = ForceField('ff99SBildn.xml')

system2 = ff.createSystem(topology)

ommtop = pmd.openmm.load_topology(topology, system2, xyz=parm.positions)

# system3 = ommtop.createSystem()

print('Converted ffxml - OpenMM system:')
print(pmd.openmm.energy_decomposition_system(ommtop, system2, nrg=kilojoules_per_mole))

system2_total = 0
for i in pmd.openmm.energy_decomposition_system(ommtop, system2, nrg=kilojoules_per_mole):
    system2_total += i[1]
    
print('Total: %s' % system2_total)    

#print('Converted ffxml - ParmEd system:')
#print(pmd.openmm.energy_decomposition_system(ommtop, system3))

#system3_total = 0
#for i in pmd.openmm.energy_decomposition_system(ommtop, system3):
#    system3_total += i[1]
    
#print('Total: %s' % system3_total)    

ff4 = ForceField('amber99sbildn.xml')

system4 = ff4.createSystem(topology)

ommtop4 = pmd.openmm.load_topology(topology, system4, xyz=parm.positions)

print('Old ffxml - OpenMM system:')
print(pmd.openmm.energy_decomposition_system(ommtop, system4, nrg=kilojoules_per_mole))

system4_total = 0
for i in pmd.openmm.energy_decomposition_system(ommtop, system4, nrg=kilojoules_per_mole):
    system4_total += i[1]

print('Total: %s' % system4_total) 
