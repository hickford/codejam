/* Google Code Jam Round 1C 2013 Problem A. Consonants
https://code.google.com/codejam/contest/2437488/dashboard#s=p0

In English, there are 26 letters that are either vowels or consonants. In this problem, we consider a, e, i, o, and u to be vowels, and the other 21 letters to be consonants.

A tribe living in the Greatest Colorful Jungle has a tradition of naming their members using English letters. But it is not easy to come up with a good name for a new member because it reflects the member's social status within the tribe. It is believed that the less common the name he or she is given, the more socially privileged he or she is.

The leader of the tribe is a professional linguist. He notices that hard-to-pronounce names are uncommon, and the reason is that they have too many consecutive consonants. Therefore, he announces that the social status of a member in the tribe is determined by its n-value, which is the number of substrings with at least n consecutive consonants in the name. For example, when n = 3, the name "quartz" has the n-value of 4 because the substrings quartz, uartz, artz, and rtz have at least 3 consecutive consonants each. A greater n-value means a greater social status in the tribe. Two substrings are considered different if they begin or end at a different point (even if they consist of the same letters), for instance "tsetse" contains 11 substrings with two consecutive consonants, even though some of them (like "tsetse" and "tsetse") contain the same letters.

All members in the tribe must have their names and n given by the leader. Although the leader is a linguist and able to ensure that the given names are meaningful, he is not good at calculating the n-values. Please help the leader determine the n-value of each name. Note that different names may have different values of n associated with them.*/
package main

import (
	"fmt"
	"strings"
)

func solve(name string, n int) (value int64) {
	run := 0 // run of consecutive consonants
	last_group_start_pos := -1

	for i, letter := range name {
		if IsConsonant(letter) {
			run += 1
			if run >= n {
				last_group_start_pos = i - n + 1
			}
		} else {
			run = 0
		}

		if last_group_start_pos < 0 {
			continue
		}

		// substrings of at least n consecutive consonants
		// for j := 0; j <= last_group_start_pos; j++ {
		// fmt.Println(name[j : i+1])
		// }

		value += int64(last_group_start_pos + 1)
	}

	return
}

func IsConsonant(r rune) bool {
	return !strings.ContainsRune("aeiou", r)
}

func main() {
	var T int
	fmt.Scan(&T)
	for i := 1; i <= T; i++ {
		var name string
		var n int
		fmt.Scan(&name)
		fmt.Scan(&n)
		answer := solve(name, n)
		fmt.Printf("Case #%d: %d\n", i, answer)
	}
}
