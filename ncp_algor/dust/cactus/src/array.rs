// n ( 2 <= n <= 2000)
// 1 <= di <= n - 1

use rand::Rng;
// use std::convert::TryFrom;

fn typ_e<T>(_: &T) {
    println!("{}",std::any::type_name::<T>());
}

fn build() {
    let val:i32 = rand::thread_rng().gen_range(2..2001);
    return val::usize as i32;
}

pub fn generate(mut v:Vec<i32>)
{
    // let mut random = rand::thread_rng();
    // let n1: u8 = random.gen();
    // let n2: u16 = random.gen();
    // println!("{}",n1);
    // println!("{}",n2);
    // println!("{}",random.gen::<u32>());
    let n = rand::thread_rng().gen_range(2..2001);
    println!("{}",n);
    typ_e(&n);
    while v.len() != n {
        build();
        // let val = rand::thread_rng().gen_range(1..n);
        // let f = usize::try_from(val).unwrap();
        v.push(val);
    }
    // println!("");
    // for k in &v {
    //     println!("{}",k);
    // }
    // println!("{:?}",v);
    // println!("{:?}",v.iter().min())
    // let min_v = v.iter().min();
    // let max_v = v.iter().max();
    // match min_v {
    //     Some(min) => println!("{:?}",min),
    //     None => println!("Nothing")
    // }
    // match max_v {
    //     Some(max) => println!("{:?}",max),
    //     None => println!("Nothing")
    // }
}