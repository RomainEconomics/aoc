package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {

	fileName := "2024/day_02/data/input.txt"
	// fileName := "2024/day_02/data/input_test.txt"

	file, err := os.Open(fileName)
	if err != nil {
		fmt.Println(err)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	part1 := 0
	part2 := 0

	for scanner.Scan() {
		line := scanner.Text()
		reports := formatLine(line)
		if isSafe(reports) {
			part1 += 1
			part2 += 1
		} else {
			for i := 0; i < len(reports); i++ {
				newReports := make([]int, 0, len(reports)-1)
				newReports = append(newReports, reports[:i]...)
				newReports = append(newReports, reports[i+1:]...)
				if isSafe(newReports) {
					part2 += 1
					break
				}
			}
		}
	}

	fmt.Println("Part 1:", part1) // 332
	fmt.Println("Part 2:", part2) // 398

}

func formatLine(line string) []int {
	nums := strings.Fields(line)
	reports := make([]int, len(nums))

	for idx, v := range nums {
		val, _ := strconv.Atoi(v)
		reports[idx] = val
	}

	return reports
}

func isSafe(reports []int) bool {
	return isSortedAscending(reports) || isSortedDescending(reports)
}
func isSortedAscending(reports []int) bool {
	for i := 1; i < len(reports); i++ {
		if reports[i] <= reports[i-1] || reports[i]-reports[i-1] > 3 {
			return false
		}
	}
	return true
}

func isSortedDescending(reports []int) bool {
	for i := 1; i < len(reports); i++ {
		if reports[i] >= reports[i-1] || reports[i-1]-reports[i] > 3 {
			return false
		}
	}
	return true
}
