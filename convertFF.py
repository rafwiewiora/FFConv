import parmed as pmd

pmd.amber.AMBERHOME = '/Users/rafalpwiewiora/amber14/'
leaprc = pmd.amber.AmberParameterSet.from_leaprc('leaprc.ff14SB')
openmm = pmd.openmm.OpenMMParameterSet.from_parameterset(leaprc)
openmm.write('ff14SB.xml')
