import os

logtaus = [4]
vrots = [0,  50, 100]
vouts = [5,25,50]

for logtau in logtaus:
    for vrot in vrots:
        for vout in vouts:
            filename = 'tau10E'+str(logtau)+'_vrot'+str(vrot)+'_vout'+str(vout)
            path = '/hpcfs/home/ciencias/fisica/pregrado/mc.remolina197/data/CLARA_RotationOutflowsData/tau10E'+str(logtau)+'/vrot'+str(vrot)+'/vout'+str(vout)+'/'
            #os.system('qsub '+path+filename+'.sh')
            print 'qsub '+path+filename+'.sh'
