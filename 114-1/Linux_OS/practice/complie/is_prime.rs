
// Tell Rst to use C-compatible function export 
// rustc --crate-type=staticlib is_prime.rs

#[no_mangle]

pub extern "C" fn is_prime(n: i32) -> i32 {
    if n < 2 {
        return 0;
    }

    for i in 2..=((n as f64).sqrt() as i32){
        if n % i == 0 {
            return 0;
        }
    }

    1
}


