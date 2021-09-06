import copy


def reassign_labels(peptides):
    # copy the pep list to allow aterations not to alter the original
    peptidesPop = copy.copy(peptides)
    # for each number incrementer, i being the new value for the lowest pep
    for i in range(len(peptidesPop)):
        # get current lowest pep number
        lowNum = (min(int(pep.split("_", 1)[1]) for pep in peptidesPop))
        # if the lowest number exists in the list, do something:
        if 'pep_'+str(lowNum) in peptides:
            # replace the current lowest pep number with the incremented i value
            peptides = ['pep_'+str(i+1) if a ==
                        'pep_'+str(lowNum) else a for a in peptides]
        # remove the lowest pep form the pop list to stop redundent checking
        peptidesPop.remove("pep_" + str(lowNum))

    return peptides
