This script processes Bader charge analysis data for VASP calculations.

It performs the following tasks:
- Reads atomic charge data from 'ACF.dat' (output of Bader analysis).
- Extracts valence electron counts for each element from the 'POTCAR' file.
- Determines the number and type of ions from the 'POSCAR' file.
- Calculates the effective Bader charge for each atom by subtracting the Bader charge from the valence electron count.
- Computes and prints the average Bader charge for each element.
- Writes the element-wise Bader charges to 'bader.txt'.

Required files in the working directory:
- ACF.dat: Output from Bader charge analysis.
- POTCAR: VASP pseudopotential file.
- POSCAR: VASP structure file.

Outputs:
- Prints summary information and average Bader charges per element.
- Writes detailed Bader charges for each atom to 'bader.txt'.

Note:
- The script expects the files to be formatted as in standard VASP workflows.
- If the number of ions does not match between POSCAR and ACF.dat, the script will exit with an error.
