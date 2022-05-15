
#include <iostream>
using namespace std;
void printSolution(int **board, int sizeOfBoard)
{
    for (int i = 0; i < sizeOfBoard; i++) {
        for (int j = 0; j < sizeOfBoard; j++)
            printf(" %d ", board[i][j]);
        printf("\n");
    }
}
bool isSafe(int **board, int sizeOfBoard, int row, int col)
{
    int i, j;
    for (i = 0; i < col; i++)
        if (board[row][i])
            return false;
    for (i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if (board[i][j])
            return false;

    for (i = row, j = col; j >= 0 && i < sizeOfBoard; i++, j--)
        if (board[i][j])
            return false;
 
    return true;
}
bool solveNQUtil(int **board,int sizeOfBoard, int col)
{
    if (col >= sizeOfBoard)
        return true;
    for (int i = 0; i < sizeOfBoard; i++) {
        if (isSafe(board,sizeOfBoard, i, col)) {
            board[i][col] = 1;
            if (solveNQUtil(board,sizeOfBoard, col + 1))
                return true;
            board[i][col] = 0;
        }
    }
    return false;
}

bool solveNQ(int **board, int sizeOfBoard)
{
    if (solveNQUtil(board,sizeOfBoard, 0) == false) {
        printf("Solution does not exist");
        return false;
    }
 
    printSolution(board, sizeOfBoard);
    return true;
}

int main()
{
    int sizeOfBoard = 0;
    cout<<"Enter the value of N i.e. the value of row/column of the board: -";
    cin>>sizeOfBoard;
    int** board = new int*[sizeOfBoard];
    for (int i = 0; i < sizeOfBoard; i++) {
        board[i] = new int[sizeOfBoard];
    }
    for(int i = 0; i<sizeOfBoard; i++)
    {
        for(int j = 0; j<sizeOfBoard; j++)
        {
            board[i][j] = 0;
        }
    }
    solveNQ(board, sizeOfBoard);
    return 0;
}