import cPickle
import pprint
import sys


m_format = sys.argv[1]

res = cPickle.load(open('checkpoints/{}/complete_results_final_model.pik'.format(m_format)))


print "\n\nPrecision \n\n"

for i in range(len(res['precision'])):
	print('\n'.join('{}: {}'.format(*k) for k in enumerate(res['precision'][i].tolist())))

print "\n\nRecall\n\n"

for i in range(len(res['recall'])):
        print('\n'.join('{}: {}'.format(*k) for k in enumerate(res['recall'][i].tolist())))

print "\n\nThreshold\n\n"
print res['threshold']


print "\n\nTime\n\n"

for i in range(len(res['time'])):
        print('\n'.join('{}: {}'.format(*k) for k in enumerate(res['time'][i].tolist())))

#for i in range(len(res['threshold'])):
#        print('\n'.join('{}: {}'.format(*k) for k in enumerate(res['threshold'][i].tolist())))


print "\n\n" 
print res['checkpoints']
