import java.util.Arrays;

/**
 * 
 * Run in the neetcode text editor.
 */
public class UniquePaths {

  // Optimized Dynamic Programming Solution (best) | Time: O(m * n), Space: O(n)
  public int uniquePaths(int m, int n) {
    int[] row = new int[n];
    Arrays.fill(row, 1);

    for (int i = 0; i < m - 1; i++) {
      int[] newRow = new int[n];
      Arrays.fill(newRow, 1);

      for (int j = n - 2; j >= 0; j --) {
      newRow[j] = newRow[j + 1] + row[j];
      }
      row = newRow;
    }
    
    return row[0];
  }
  
}