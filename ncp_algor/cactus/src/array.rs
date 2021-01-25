use rand::Rng;

pub fn generate()
{
    let mut random = rand::thread_rng();
    let n1: u8 = random.gen();
    let n2: u16 = random.gen();
    println!("{}",n1);
    println!("{}",n2);
    println!("{}",random.gen::<u32>());
    let mut v: Vec<i32> = Vec::new();
    while v.len() != 5 {
        let val = rand::thread_rng(
        ).gen_range(0..10);
        v.push(val);
    }
    println!("");
    for k in &v {
        println!("{}",k);
    }
    println!("{:?}",v);
    // println!("{:?}",v.iter().min())
    let min_v = v.iter().min();
    match min_v {
        Some(min) => println!("{:?}",min),
        None => println!("Nothing")
    }
}