package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"sort"
	"strconv"
	"strings"
)

// Complete the minimumAbsoluteDifference function below.
func minimumAbsoluteDifference(arr []int32) int32 {
	var min int32 = 10000000

	iarr := arr
	sort.SliceStable(iarr, func(i, j int) bool {
		return iarr[i] < iarr[j]
	})

	for i := 0; i < len(iarr)-1; i++ {
		diff := abs(iarr[i] - iarr[i+1])
		if diff < min {
			min = diff
		}
	}

	return min
}

func abs(num int32) int32 {
	if num >= 0 {
		return num
	} else {
		return -1 * num
	}
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 1024*1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 1024*1024)

	nTemp, err := strconv.ParseInt(readLine(reader), 10, 64)
	checkError(err)
	n := int32(nTemp)

	arrTemp := strings.Split(readLine(reader), " ")

	var arr []int32

	for i := 0; i < int(n); i++ {
		arrItemTemp, err := strconv.ParseInt(arrTemp[i], 10, 64)
		checkError(err)
		arrItem := int32(arrItemTemp)
		arr = append(arr, arrItem)
	}

	result := minimumAbsoluteDifference(arr)

	fmt.Fprintf(writer, "%d\n", result)

	writer.Flush()
}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
