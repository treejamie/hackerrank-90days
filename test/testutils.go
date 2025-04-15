package testutils

import (
	"os"
	"strings"
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
