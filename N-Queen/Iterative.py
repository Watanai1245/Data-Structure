import time
start_time = time.time()
class NQueens:
    def __init__(self, size):
        self.size = size
        self.solutions = 0
        self.solve()

    def solve(self):
        positions = [-1] * self.size
        self.put_queen(positions, 0)
        print("Input : " + str(n))
        print("Number of Solution(s) : " + str(self.solutions))

    def put_queen(self, positions, target_row):
        if target_row == self.size:
            self.show_full_board(positions)
            self.solutions += 1
        else:
            for column in range(self.size):
                if self.check_place(positions, target_row, column):
                    positions[target_row] = column
                    self.put_queen(positions, target_row + 1)


    def check_place(self, positions, ocuppied_rows, column):
        for i in range(ocuppied_rows):
            if positions[i] == column or \
                positions[i] - i == column - ocuppied_rows or \
                positions[i] + i == column + ocuppied_rows:

                return False
        return True

    def show_full_board(self, positions):
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[row] == column:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("\n")

    def show_short_board(self, positions):
        line = ""
        for i in range(self.size):
            line += str(positions[i]) + " "
        print(line)

def main():
    NQueens(n)

if __name__ == "__main__":
    n = 15
    main()

print("-> %s seconds <-" % (time.time() - start_time))