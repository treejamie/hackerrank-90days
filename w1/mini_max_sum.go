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

// If false, don't print to STDOUT
const PRINT bool = false

func sumInt64(arr []int64) int64{
	// make the sum variable
	var sum int64

	// iterate over the slice and add valie to the sum
	for _, value := range(arr){
		sum += int64(value)

	}
	return sum
}

func MiniMaxSum(arr []int64) []int64 {
	/*
	Clone the arr to give two slices, minimum and maximum.
	Sort each slice and pop the last value - this gives max and min values.
	Sum and you're done.
	*/
	// min sum: drop the max
	mn := slices.Clone(arr)
	slices.Sort(mn)
	mnSum := sumInt64(mn[:len(mn)-1])

	// max sum: drop the min
	mx := slices.Clone(arr)
	slices.Sort(mx)
	slices.Reverse(mx)
	mxSum := sumInt64(mx[:len(mx)-1])

	// print: HackerRank insists on it for some challenges
	if PRINT {
		fmt.Printf("%d %d", mnSum, mxSum)
	}

	// return: makes it easier to test
	return []int64{mnSum, mxSum}
}
