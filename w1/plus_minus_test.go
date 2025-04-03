package w1

import (
	"os"
	"strconv"
	"strings"
	"testing"
)

// check is a shortcut function for error handling in test cases
// where error handling in a production manner would interfere with
// readability and perhaps performance of code.
func check(e error) {
    if e != nil {
        panic(e)
    }
}
// ReadLines is the most minimal function to read in the test case files.
// they should all be formatted in the right way, so error
// handling is not a massive concern
func ReadLines(path string) ([]string, error) {
	data, err := os.ReadFile(path)
	check(err)
	return strings.Split(strings.TrimSpace(string(data)), "\n"), nil
}

// Test_plus_minus ensures
func Test_plus_minus(t *testing.T){
	// test cases 
	tcs := []string{
		"tc/1_0.txt",
		"tc/1_1.txt",
		"tc/1_2.txt",
	}

	// now iterate over the test cases
	for _, tc := range tcs {
		// read in the files
		lines, _ :=  ReadLines(tc)
		// don't want the first line, but want the second
		// and split it up into a slice.
		parts := strings.Fields(lines[1])
		args := make([]int32, len(parts))
		for i, arg := range parts{
			n, _ := strconv.ParseInt(arg, 10, 32)
			args[i] = int32(n)

		}
		
		// we expect an array of strings three items long
		expected := [3]string{
			strings.TrimSpace(lines[3]),
			strings.TrimSpace(lines[4]),
			strings.TrimSpace(lines[5]),
		}

		// call the function
		got := PlusMinus(args)

		// and now compare got with expected
		if got != expected {
			t.Errorf("Test_plus_minus: %q, want %q", got, expected)
		}

	}
}