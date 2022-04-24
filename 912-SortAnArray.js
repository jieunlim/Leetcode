var sortArray = function (nums) {
  //insertion sort
  let key = 0;
  for (let i = 1; i < nums.length; i++) {
    key = nums[i];
    j = i - 1;

    while (j >= 0 && nums[j] > key) {
      nums[j + 1] = nums[j];
      nums[j] = key;
      j--;
    }
  }
  return nums;
};
