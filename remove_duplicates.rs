// main function
fn main() {
    let mut nums = vec![0,0,1,1,1,2,2,3,3,4];
    if nums.is_empty() {
        println!("0");
    } else {
        let mut k = 1;
        for i in 1..nums.len() {
            if nums[i] != nums[i - 1] {
                nums[k] = nums[i];
                k += 1;
            }
        }

        println!("{}", k);
    }
}