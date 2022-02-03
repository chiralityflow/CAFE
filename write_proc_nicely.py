import os
# get subprocess and turn it back into madgraph naming conventions
proc = os.environ["d"]
# non-particles
proc = proc.replace('P1_', '')
proc = proc.replace('_', '> ')
proc = proc.replace('/','')
# electrons
proc = proc.replace('elm','el- ')
proc = proc.replace('elp','el+ ')
proc = proc.replace('erm','er- ')
proc = proc.replace('erp','er+ ')
# muons
proc = proc.replace('mulm','mul- ')
proc = proc.replace('mulp','mul+ ')
proc = proc.replace('murm','mur- ')
proc = proc.replace('murp','mur+ ')
# photons
# choose whether using chiral photons or not (cannot be both)
# proc = proc.replace('a','a ')
proc = proc.replace('al','al ')
proc = proc.replace('ar','ar ')

# group same final-state particles for easier human reading
final_state = proc.split('> ')[-1]
initial_state = proc.split('> ')[0]
particles = [word for word in final_state.split(' ') if word != '']

# check for multiple instances of the same particle
to_remove = []
for ipart, part in enumerate(particles):
    # if not already considered same particle before and there are multiple instances of this particle
    if not part in to_remove and particles.count(part) > 1:
        # we don't want to consider it again
        to_remove.append(part)
        # simplify output
        particles[ipart] = str(particles.count(part)) + part

# update particles in final state and re-join with initial state
particles = [part for part in particles if part not in to_remove]
final_state = ' '.join(particles)        
proc = initial_state + '> ' + final_state

# put subproc in sentence
proc = 'In SubProcess: \n' + proc

print(proc)