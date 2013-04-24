from sudoku import *
import sys



def main():
    solver = SudokuSolver()
    if len(sys.argv) > 1:
        file= open(sys.argv[1], 'r')
        print(solver.solve(SudokuReader(file)))
        file.close()
        return 
    else: 
        print("""
Sudoku Solver
usage: python """ + str(sys.argv[0]) + """ filename
          where filename contains 9 lines with 9 letters 
          and no spacing between. Use zeros to denote blanks.
""")
    return 

if __name__ == '__main__':
    main()