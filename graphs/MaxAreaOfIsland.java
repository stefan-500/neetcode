/*
Run in the neetcode text editor.
*/
public class MaxAreaOfIsland {

  // DFS solution (best) | Time: O(m * n), Space: O(m * n),
  // where m is the number of rows and n is the number of columns in the grid.
  public int maxAreaOfIsland(int[][] grid){
    int ROWS = grid.length, COLS = grid[0].length;
    
    int area = 0;
    for (int r = 0; r < ROWS; r++){
      for (int c = 0; c < COLS; c++){
        area = Math.max(area, dfs(grid, r, c));
      }
    }
    
    return area;
  }

  private int dfs(int[][] grid, int r, int c){
    if (r < 0 || c < 0 || r >= grid.length ||
        c >= grid[0].length || grid[r][c] == 0){
      return 0;
    }

    grid[r][c] = 0;
    return 1 + dfs(grid, r + 1, c) +
               dfs(grid, r - 1, c) +
               dfs(grid, r, c + 1) +
               dfs(grid, r, c - 1);
  }
}