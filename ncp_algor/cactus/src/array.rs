use rand::Rng;

pub fn generate(mut v:Vec<i32>)
{
    // let mut random = rand::thread_rng();
    // let n1: u8 = random.gen();
    // let n2: u16 = random.gen();
    // println!("{}",n1);
    // println!("{}",n2);
    // println!("{}",random.gen::<u32>());
    while v.len() != 5 {
        let val = rand::thread_rng(
        ).gen_range(1..10);
        v.push(val);
    }
    // println!("");
    // for k in &v {
    //     println!("{}",k);
    // }
    println!("{:?}",v);
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