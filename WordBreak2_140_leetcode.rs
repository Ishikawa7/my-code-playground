use std::collections::HashSet;
impl Solution {
    pub fn word_break(s: String, word_dict: Vec<String>) -> Vec<String> {
        let mut dp: Vec<Vec<String>> = vec![Vec::new(); s.len() + 1];
        let mut word_set: HashSet<String> = HashSet::new();
        for word in word_dict.iter() {
            word_set.insert(word.clone());
        }

        dp[0] = vec![String::new()];

        for i in 1..=s.len() {
            //println!("Checking position {}", i);
            for j in 0..i {
                let word = &s[j..i];
                //println!("    Substring from position {} to {}: '{}'", j, i, word);
                if word_set.contains(word) && !dp[j].is_empty() {
                    //println!("        Substring '{}' found in dictionary and dp[{}] is not empty", word, j);
                    for prev in dp[j].clone() {
                        if prev.is_empty() {
                            //println!("            Adding '{}'", word);
                            dp[i].push(word.to_string());
                        } else {
                            //println!("            Combining '{}' with '{}'", prev, word);
                            dp[i].push(format!("{} {}", prev, word));
                        }
                    }
                    //for sentence in &dp[i] {
                    //    println!("                  Printing element d[i]");
                    //    println!("{}", sentence);
                    //}
                }
            }
        }

        dp[s.len()].clone()
    }
}