/**
 * 
 * Run in the neetcode text editor.
 */
public class LongestCommonSubSequence {

  // Dynamic Programming (Bottom up) solution | Time: O(m * n), Space: O(m * n),
  // where m is the length of the string text1 and n is the length of the string text2.
  public int longestCommonSubSequence(String text1, String text2) {
    int[][] dp = new int[text1.length() + 1][text2.length() + 1];

    for (int i = text1.length() - 1; i >= 0; i--) {
      for (int j = text2.length() - 1; j >= 0; j--) {
        if (text1.charAt(i) == text2.charAt(j)) {
          dp[i][j] = 1 + dp[i + 1][j + 1];
        } else {
          dp[i][j] = Math.max(dp[i][j + 1], dp[i + 1][j]);
        }
      }
    }

    return dp[0][0];
  }
  
}
