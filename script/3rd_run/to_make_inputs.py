#Example of directory: /lustre/home/ciencias/fisica/pregrado/mc.remolina197/data/CLARA_RotationOutflowsData/tau10E5/vrot0/vout100

logtaus = [5,6,7]
vrots = [50,100]
vouts = [5,10,15,20]

for logtau in logtaus:
    for vrot in vrots:
        for vout in vouts:

            filename = 'tau10E'+str(logtau)+'_vrot'+str(vrot)+'_vout'+str(vout)
            path = '/lustre/home/ciencias/fisica/pregrado/mc.remolina197/data/CLARA_RotationOutflowsData/tau10E'+str(logtau)+'/vrot'+str(vrot)+'/vout'+str(vout)+'/'
            input_file = open(path+filename+'.input', 'w')

            input_file.write('% input files and formats*/\n')
            input_file.write('InputDir\t'+path+'\n')
            input_file.write('CubeName\tgrid_object_100\n')
            input_file.write('\n')
            input_file.write('% output files\n')
            input_file.write('OutputDir\t'+path+'\n')
            input_file.write('OutputFile\t'+filename+'\n')
            input_file.write('\n')
            input_file.write('\n')
            input_file.write('% define the problem/test to solve\n')
            input_file.write('NeufeldSlab\t0\n')
            input_file.write('NeufeldCube\t0\n')
            input_file.write('ExpandingSphere\t0\n')
            input_file.write('RotatingSphere\t0\n')
            input_file.write('OutflowRotationSphere\t1\n')
            input_file.write('TestParallelVel\t0\n')
            input_file.write('TestParallelVelFast\t0\n')
            input_file.write('TestFirstScatter\t0\n')
            input_file.write('TestRND\t0\n')
            input_file.write('TestPerpVel\t0\n')
            input_file.write('SimulationCube\t0\n')
            input_file.write('HomogeneousInit\t0\n')
            input_file.write('\n')
            input_file.write('% parameters for the tests\n')
            input_file.write('Test_a\t0.00014\n')
            input_file.write('Test_x\t2.0\n')
            input_file.write('OutputTestFile\ttest_b\n')
            input_file.write('\n')
            input_file.write('% define some physical parameters of the problem to solve\n')
            input_file.write('Temperature\t10000.0 % in  Kelvin\n')
            input_file.write('Tau\t1.0e'+str(logtau)+'\n')
            input_file.write('NumberDensityHI\t1e6\n')
            input_file.write('VmaxSphere\t0.0 % in km/s\n')
            input_file.write('VmaxRotation\t'+str(vrot)+' % in km/s\n')
            input_file.write('VmaxOutflow\t'+str(vout)+' % in km/s\n')
            input_file.write('\n')
            input_file.write('\n')
            input_file.write('% parameters of the dust model\n')
            input_file.write('GrainSize\t1.0e-6\n')
            input_file.write('TauDust\t1.0\n')
            input_file.write('DustAbsorptionProb\t0.5\n')
            input_file.write('\n')
            input_file.write('% parameters controling the algorithm\n')
            input_file.write('InputFrequency\t0.0 % 0 is the line center\n')
            input_file.write('TotalLuminosity\t1.0e5% in  UnitLymanLuminosity\n')
            input_file.write('LuminosityPerPackage\t1.0\n')
            input_file.write('EffectiveEta\t0.71\n')
            input_file.write('EffectiveDust\t1.0e-3\n')
            input_file.write('ThresholdCube\t10000.0\n')
            input_file.write('UseDust\t0\n')
            input_file.write('UseVelocities\t1\n')
            input_file.write('UseAtomSpeedUp\t0\n')
            input_file.write('\n')
            input_file.write('% output options for the photon list\n')
            input_file.write('OutputInitList         1\n')
            input_file.write('OutputFinalList        1\n')
            input_file.write('OutputBinary           0\n')
            input_file.write('\n')
            input_file.write('% Units\n')
            input_file.write('UnitMass_in_g\t1.989e+43\n')
            input_file.write('UnitVelocity_in_cm_per_s\t100000.0\n')
            input_file.write('UnitLength_in_cm\t3.08568e+21\n')
            input_file.write('UnitLymanLuminosity\t1.0e+41      % cgs\n')
            input_file.write('\n')
            input_file.write('RandomSeed\t14923\n')

            input_file.close()
