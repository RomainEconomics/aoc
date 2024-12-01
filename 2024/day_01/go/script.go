package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {

	// fileName := "2024/day_01/data/input_test.txt"
	fileName := "2024/day_01/data/input.txt"

	part1 := Part1(fileName) // 3574690
	part2 := Part2(fileName) // 22565391

	fmt.Println("Part 1:", part1)
	fmt.Println("Part 2:", part2)

}

func readFile(fileName string) ([]int, []int) {
	l1, l2 := []int{}, []int{}

	file, err := os.Open(fileName)
	if err != nil {
		fmt.Println(err)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()
		values := strings.Fields(line)

		val1, _ := strconv.Atoi(values[0])
		val2, _ := strconv.Atoi(values[1])

		l1 = append(l1, val1)
		l2 = append(l2, val2)
	}

	return l1, l2

}

func Part1(fileName string) int {
	l1, l2 := readFile(fileName)

	sort.Ints(l1)
	sort.Ints(l2)

	s := 0

	for i := 0; i < len(l1); i++ {
		value := l1[i] - l2[i]
		if value >= 0 {
			s += value
		} else {
			s -= value
		}
	}
	return s
}

func Part2(fileName string) int {
	l1, l2 := readFile(fileName)

	m := make(map[int]int)
	sum := 0

	for _, x1 := range l1 {

		_, ok := m[x1]

		if !ok {
			for _, x2 := range l2 {
				if x1 == x2 {
					m[x1]++
				}
			}
		}
		sum += x1 * m[x1]
	}
	return sum
}
