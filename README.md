# Junior SE interview test
At Nuritas, we discover peptides from natural sources.
Every year we discover and characterize hundreds of thousands of new natural peptides and we save them in our Peptide Manager application.

When we save a peptide in our database we assign a unique ID which never changes and a readable label, which can change often, initially based on the ID.
For example, we add our 100th peptide and the label is "pep_100".

It might happen that the peptides we discover are variations of others and we don't want to consider them, so we move them to a different table.
This leave some gaps between peptide labels.
For example, if we move "pep_101" to the other table, the full list will be [..., "pep_100", "pep_102", ...] with a gap between label 100 and 102.

We really don't like this! We re-label the peptides to leave no discrepancies: "pep_102" should become "pep_101", "pep_103" should become "pep_102" and so on.
This operation is done every night, so more peptides and more gaps needs to be checked.

## Requirements

Write a function that given a list of peptide labels returns a list in the same order with their new labels, leaving no gaps.

Example:
Input: ["pep_1", "pep_10", "pep_2", "pep_7", "pep_14"]
Output: ["pep_1", "pep_4", "pep_2", "pep_3", "pep_5"]

Notes:
- input list is never empty
- it can have hundreds of thousands of entries
- execution time over **all datasets** should be **less than 1 minute**
- input files contain one peptide per line, and the first line contains the number of peptides in the file

## Solution
You can write your solution directly in the file `solver.py` and then run the test with the command
```bash
python reorder_peptides.py
```

You can then send the `solver.py` file (or your solution if in another language) without the peptides input files (we will use our own inputs).

Alternatively, you can write the solution in your preferred language.

Please make sure your code is readable and comment your implementation choices when needed.
