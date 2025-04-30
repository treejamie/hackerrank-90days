package w1

import (
	"fmt"
	"strings"
	"testing"

	"github.com/treejamie/hackerrank-90days/testutils"
)



func TestTimeConversion(t * testing.T){
	tcs := []string{
		"tc/3_0.txt",
		"tc/3_1.txt",
	}
	// iterate over the tests
	for _, tc := range tcs {
		// read: read in the lines of the file
		lines, _ := testutils.ReadLines(tc)

		// we want the first line for args
		args := strings.Fields(lines[0])

		// third line for expected
		_expected := strings.Fields(lines[2])

		// now call the function
		got := TimeConversion(args)

		fmt.Println(got)
	}

}