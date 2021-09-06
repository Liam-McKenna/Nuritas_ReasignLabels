from time import time

import solver


def reassign_labels(n):
    with open(f'peptides_{n}.txt') as peptides_h:
        content = peptides_h.readlines()
        tot = int(content[0].strip())
        peptides = [l.strip() for l in content[1:]]
        assert len(peptides) == tot
    print(f"Solves for {n} peptides...")
    time_start = time()

    try:
        solution = solver.reassign_labels(peptides)
    except AttributeError:
        raise Exception(
            "Please implement function 'reassign_labels' in solver.py file.")

    if len(solution) == 0:
        raise Exception(
            "Please implement function 'reassign_labels' in solver.py file.")

    print(f"...done in {round((time() - time_start), 3)}s")

#     test(solution)


# def test(solution):
#     for i in range(len(solution)):
#         for pep in solution:
#             if int(pep.split("_", 1)[1]) == i+1:
#                 found = True
#                 break
#             else:
#                 found = False
#         if found == False:
#             print('found pep_'+str(i+1)+':' + str(found))
#     if found == True:
#         print('All records exist')


if __name__ == '__main__':
    reassign_labels(10)
    reassign_labels(1000)
    reassign_labels(10000)
