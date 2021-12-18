package leetcode

func romanToInt(s string) int {
	var dic = map[string]int{
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000,
	}
	cur, pre := 0, 0
	ans := 0
	for i := 0; i < len(s); i++ {
		char := s[len(s)-i-1 : len(s)-i]
		cur = dic[char]
		if cur >= pre {
			ans = ans + cur
		} else {
			ans = ans - cur
		}
		pre = cur
	}
	return ans
}
