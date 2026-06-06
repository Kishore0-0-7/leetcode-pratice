static void swap_int(int * const pNum1, int * const pNum2){
	const int buf = *pNum1;
	*pNum1 = *pNum2;
	*pNum2 = buf;
}

static void reverse_intArr(
	int * const nums,
	const int numsLen
){
	for (
		int left = 0, right = numsLen - 1;
		left < right;
		left += 1, right -= 1
	){
		swap_int(&nums[left], &nums[right]);
	}
}

static int search_intArr(
	const int * const nums,
	const int numsLen,

	const int target
){
	for (int i = 0; i < numsLen; i += 1){
		if (nums[i] == target){
			return i;
		}
	}
	return -1;
}

int * pancakeSort(
	int * const nums,
	const int numsLen,

	int * const pRetsLen
){
	int * const ret = (int *)malloc(sizeof (int) * (numsLen * 2));
	*pRetsLen = 0;

	for (int curLen = numsLen; curLen > 0; curLen -= 1){
		const int targetIdx = search_intArr(nums, curLen, curLen);
		assert(targetIdx >= 0);

		if (targetIdx == curLen - 1){
			continue;
		}

		if (targetIdx != 0){
			ret[*pRetsLen] = targetIdx + 1;
			*pRetsLen += 1;

			reverse_intArr(nums, targetIdx + 1);
		}

		ret[*pRetsLen] = curLen;
		*pRetsLen += 1;

		reverse_intArr(nums, curLen);
	}

	return ret;
}