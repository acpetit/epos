import numpy as np
import matplotlib.pyplot as plt
import helpers

def multiplicity(epos, MC=False):
	# plot multiplicity
	f, ax = plt.subplots()
	ax.set_title('planet multiplicity')
	ax.set_xlabel('planets per system')
	ax.set_ylabel('number of systems')

	ax.set_xlim(0, 9)
	ax.set_ylim(0.5, 1e4) # 7.	
	ax.set_yscale('log')

	# MC data
	if MC:
		ss=epos.synthetic_survey
		ax.plot(ss['multi']['bin'], ss['multi']['count'], 
			ls='', marker='+', mew=2, ms=10, color='k',label=epos.name)
	
		# observations in same region 
		ax.plot(epos.obs_zoom['multi']['bin'], epos.obs_zoom['multi']['count'], 
			drawstyle='steps-mid', 
			ls='-', marker='', color='k', label='Kepler subset')

	# observations
	ax.plot(epos.multi['bin'], epos.multi['count'], drawstyle='steps-mid', 
		ls='--', marker='', color='gray', label='Kepler all')
		
	ax.legend(loc='upper right', shadow=False, prop={'size':14}, numpoints=1)
	
	prefix= 'output' if MC else 'survey'
	
	helpers.save(plt, '{}{}/multiplicity'.format(epos.plotdir,prefix))

def multiplicity_cdf(epos, MC=False):
	# plot multiplicity cdf
	f, ax = plt.subplots()
	ax.set_title('planet multiplicity')
	ax.set_xlabel('planets per system')
	ax.set_ylabel('cumulative number of planets')

	ax.set_xlim(0, 9)
	ax.set_ylim(-0.01,1.05)
	#ax.set_yscale('log')

	# MC data
	if MC:
		ss=epos.synthetic_survey
		bincounts= np.sort(ss['multi']['cdf'])
		cdf= np.arange(bincounts.size, dtype=float)/bincounts.size
		ax.plot(bincounts, cdf, 
			drawstyle='steps-mid', 
			ls='-', marker='', mew=2, ms=10, color='b',label=epos.name)
	
		# observations in same region 
		bincounts= np.sort(epos.obs_zoom['multi']['cdf'])
		cdf= np.arange(bincounts.size, dtype=float)/bincounts.size
		ax.plot(bincounts, cdf,  
			drawstyle='steps-mid', 
			ls='-', marker='', color='k', label='Kepler subset')

	# observations
	#ax.plot(epos.multi['bin'], epos.multi['count'], drawstyle='steps-mid', 
	#	ls='--', marker='', color='gray', label='Kepler all')
		
	ax.legend(loc='lower right', shadow=False, prop={'size':14}, numpoints=1)
	
	prefix= 'output' if MC else 'survey'
	
	helpers.save(plt, '{}{}/cdf'.format(epos.plotdir,prefix))
	
def periodratio(epos, MC=False):
	# plot multiplicity
	f, ax = plt.subplots()
	ax.set_title('period ratio adjecent planets')
	ax.set_xlabel('period outer/inner')
	ax.set_ylabel('PDF')

	ax.set_xlim(1, 10)
	ax.set_xscale('log')
	for s in [ax.set_xticks,ax.set_xticklabels]: s([1,2,3,4,5,7,10])
		
	#bins=np.linspace(1,10, 9*5+1)
	bins=np.logspace(0,1, 15)
	
	# MC data
	if MC:
		ss=epos.synthetic_survey
		ax.hist(ss['multi']['Pratio'], bins=bins, ec='b', histtype='step', label=epos.name)
	
		# Observed zoom
		ax.hist(epos.obs_zoom['multi']['Pratio'], bins=bins, ec='k', histtype='step', label='Kepler subset')
	else:
		# observed all
		ax.hist(epos.multi['Pratio'], bins=bins, color='b', label='Kepler all')
	
	prefix= 'output' if MC else 'survey'

	if MC: ax.legend(loc='upper right', shadow=False, prop={'size':14}, numpoints=1)
		
	helpers.save(plt, '{}{}/periodratio'.format(epos.plotdir, prefix))	

def periodratio_cdf(epos, MC=False):

	# plot multiplicity CDF
	f, ax = plt.subplots()
	ax.set_title('period ratio adjacent planets')
	ax.set_xlabel('period outer/inner')
	ax.set_ylabel('CDF')

	ax.set_xlim(1, 10)
	ax.set_xscale('log')
	for s in [ax.set_xticks,ax.set_xticklabels]: s([1,2,3,4,5,7,10])

	# MC data
	if MC:
		ss=epos.synthetic_survey
		Psort= np.sort(ss['multi']['Pratio'])
		cdf= np.arange(Psort.size, dtype=float)/Psort.size
		ax.plot(Psort, cdf, color='b', label=epos.name)
	
		# Observed zoom
		Psort= np.sort(epos.obs_zoom['multi']['Pratio'])
		cdf= np.arange(Psort.size, dtype=float)/Psort.size
		ax.plot(Psort, cdf, color='k', label='Kepler subset')

	else:
		for resonance in [2./1., 3./2.]: ax.axvline(resonance, ls=':', color='g')

	# all observed
	Psort= np.sort(epos.multi['Pratio'])
	cdf= cdf= np.arange(Psort.size, dtype=float)/Psort.size
	ax.plot(Psort, cdf ,color='gray' if MC else 'k', label='Kepler all')	
	
	prefix= 'output' if MC else 'survey'
	
	if MC: ax.legend(loc='lower right', shadow=False, prop={'size':14}, numpoints=1)
		
	helpers.save(plt, '{}{}/periodratio.cdf'.format(epos.plotdir,prefix))	