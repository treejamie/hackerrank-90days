/*
This is the second challenge of week 1.

https://www.hackerrank.com/challenges/three-month-preparation-kit-mini-max-sum/problem

Given five positive integers, find the minimum and maximum values that
can be calculated by summing exactly four of the five integers. Then
print the respective minimum and maximum values as a single line of two
space-separated long integers.
*/
package w1

import (
	"fmt"
	"slices"
)

var HR bool = false

func sumint64(arr []int64) int64{
	// make the sum variable
	var sum int64

	// iterate
	for _, value := range(arr){
		sum += int64(value)

	}
	return sum
}

func MiniMaxSum(arr []int64) []int64 {
	// fmt.Println(arr)
	// copy arr for max values, sort it descending, pop last value
	mx := make([]int64, len(arr))
	copy(mx, arr)

	// sort mx ascending
	slices.SortFunc(mx, func(a, b int64) int {
		if a > b {
			return -1
		} else if a < b {
			return 1
		}
		return 0
	})
	mx = mx[:len(mx)-1]

	// sort the for minimum values ascending and pop last value
	slices.Sort(arr)
	mn := arr[:len(arr)-1]

	// now sum each
	mx_sum := sumint64(mx)
	mn_sum := sumint64(mn)

	// if we're on hackerank, print it out
	if HR {
		fmt.Printf("%d %d", mn_sum, mx_sum)
	}

	return []int64{mn_sum, mx_sum}
}
