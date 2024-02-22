package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

func main() {

	fileName := "2023/day_01/data/input.txt"

	digitMap := map[string]string{
		"one":   "1",
		"two":   "2",
		"three": "3",
		"four":  "4",
		"five":  "5",
		"six":   "6",
		"seven": "7",
		"eight": "8",
		"nine":  "9",
	}

	// Part 1

	file, err := os.Open(fileName)
	if err != nil {
		fmt.Println(err)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	sumPart1 := 0
	sumPart2 := 0

	for scanner.Scan() {
		line := scanner.Text()

		sumPart1 += extractNumPart1(line)
		sumPart2 += extractNumPart2(line, digitMap)

	}

	fmt.Println("Part 1:", sumPart1) // 55816
	fmt.Println("Part 2:", sumPart2) // 54980

}

func extractNumPart1(s string) int {
	var digits []int
	for _, c := range s {
		if c >= '0' && c <= '9' {
			digits = append(digits, int(c-'0'))
		}
	}

	firstDigit := strconv.Itoa(digits[0])
	lastDigit := strconv.Itoa(digits[len(digits)-1])

	num, _ := strconv.Atoi(firstDigit + lastDigit)
	return num
}

func extractNumPart2(s string, digitMap map[string]string) int {
	re := regexp.MustCompile(`\d|one|two|three|four|five|six|seven|eight|nine`)
	matches := re.FindAllString(s, -1)

	var firstDigit string
	var secondDigit string

	val1, exist1 := digitMap[matches[0]]
	if exist1 {
		firstDigit = val1
	} else {
		firstDigit = matches[0]
	}

	val2, exist2 := digitMap[matches[len(matches)-1]]

	if exist2 {
		secondDigit = val2
	} else {
		secondDigit = matches[len(matches)-1]
	}

	num, _ := strconv.Atoi(firstDigit + secondDigit)

	return num
}
