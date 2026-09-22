import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/*
Run in the neetcode text editor.
*/
public class PartitionEqualSubsetSum {
 
  // Dynamic Programming solution (best) | Time: O(n * target), Space: O(target),
  // where n is the length of the array nums and target is the sum of array
  // elements divided by 2.
  public boolean canPartition(int[] nums) {
    if (Arrays.stream(nums).sum() % 2 != 0){
      return false;
    }

    Set<Integer> dp = new HashSet<>();
    dp.add(0);
    int target = Arrays.stream(nums).sum() / 2;

    for (int i = nums.length - 1; i >= 0; i--){
    Set<Integer> nextDP = new HashSet<>();
      for (int t : dp){
        if (t + nums[i] == target){
          return true;
        }
        nextDP.add(t + nums[i]);
        nextDP.add(t);
      }
      dp = nextDP;
    }
    return false;
  }

}
