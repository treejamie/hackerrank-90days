/*
This is the first challenge of week 1.

https://www.hackerrank.com/challenges/three-month-preparation-kit-plus-minus/problem

Given an array of integers, calculate the ratios of its elements that are
positive, negative, and zero. Print the decimal value of each fraction on a
new line with 6 places after the decimal.
*/
package w1

import "fmt"

func PlusMinus(arr []int32) [3]string {

	// the length is used a lot, so calculate that once
	l := float64(len(arr))

	// make three slices for each of the values
	p, n, z := []int32{}, []int32{}, []int32{}

	// fill up the slice dependant on the value
	for _, value := range arr {
		// three cases, I know, I know, I could have used ifs
		// but just switch on true instead.
		switch {
		case value > 0:
			p = append(p, value)
		case value < 0:
			n = append(n, value)
		default:
			z = append(z, value)
		}
	}
	// now calculate the ratios
	var p_ratio float64 = float64(len(p)) / l 
	var n_ratio float64 = float64(len(n)) / l 
	var z_ratio float64 = float64(len(z)) / l

	// make an array for the solutions
	// note: it MUST have three items and only 3, so array - not slice
	solution := [3]string{}
	solution[0] = fmt.Sprintf("%.6f", p_ratio)
	solution[1] = fmt.Sprintf("%.6f", n_ratio)
	solution[2] = fmt.Sprintf("%.6f", z_ratio)

	// HackerRank wants you to print them
	for _, value := range solution {
		fmt.Println(value)
	}

	// return the solution
	return solution
}
