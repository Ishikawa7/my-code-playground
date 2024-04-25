# Intuition
When searching for a substring within a larger string, the Knuth-Morris-Pratt (KMP) algorithm provides an efficient approach. It's particularly useful when the brute-force method becomes inefficient due to repeated comparisons. The key idea behind KMP is to use a "prefix table" to skip unnecessary comparisons during the search.

# Approach
1. **Building the Prefix Table**: We construct a prefix table that helps identify potential match positions in the needle without rechecking characters unnecessarily.
2. **Searching for the Needle in the Haystack**: Utilizing the prefix table, we iteratively compare characters in the haystack and needle, efficiently advancing through the haystack.

To understand the KMP algorithm in more detail, you can visit the [Wikipedia page](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm).

# Complexity
- Time complexity: $$O(n + m)$$, where $$n$$ is the length of the haystack and $$m$$ is the length of the needle.
- Space complexity: $$O(m)$$, where $$m$$ is the length of the needle.

# Code
```rust
impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        let haystack_chars: Vec<char> = haystack.chars().collect();
        let needle_chars: Vec<char> = needle.chars().collect();
        
        if needle_chars.is_empty() {
            return 0;
        }
        
        // Build the prefix table
        let mut prefix_table: Vec<usize> = vec![0; needle_chars.len()];
        let mut j = 0;
        for i in 1..needle_chars.len() {
            while j > 0 && needle_chars[i] != needle_chars[j] {
                j = prefix_table[j - 1];
            }
            if needle_chars[i] == needle_chars[j] {
                j += 1;
            }
            prefix_table[i] = j;
        }
        
        // Use the prefix table to search for the needle in the haystack
        let mut j = 0;
        for i in 0..haystack_chars.len() {
            while j > 0 && haystack_chars[i] != needle_chars[j] {
                j = prefix_table[j - 1];
            }
            if haystack_chars[i] == needle_chars[j] {
                j += 1;
            }
            if j == needle_chars.len() {
                return (i - j + 1) as i32;
            }
        }
        
        -1
    }
}
