package w1

import (
	"slices"
	"strconv"
	"strings"
	"testing"

	"github.com/treejamie/hackerrank-90days/testutils"
)



func TestMiniMaxSum(t *testing.T){
	// the test cases
	tcs := []string{
		"tc/2_0.txt",
		"tc/2_1.txt",
		"tc/2_14.txt",
	}

	// iterate over the tests
	for _, tc := range tcs {
		// read in the files
		lines, _ := testutils.ReadLines(tc)

		// we want the first line for args
		parts := strings.Fields(lines[0])

		// turn that into a slice of 5 int32
		args := make([]int64, 5)
		for i, arg := range parts{
			n, _ := strconv.ParseInt(arg, 10, 64)
			args[i] = int64(n)
		}

		// parse what we expect to get as a return
		parts = strings.Fields(lines[2])

		// turn that into a slice of 2 int32
		expected := make([]int64, 2)
		for i, arg := range parts{
			n, _ := strconv.ParseInt(arg, 10, 64)
			expected[i] = int64(n)
		}
		//fmt.Printf("%T\n", args)

		// now test
		got := MiniMaxSum(args)
		
		if ! slices.Equal(got, expected) {
			t.Errorf("TestMiniMaxSum: got %d, expected %d", got, expected)
		}

	}

}