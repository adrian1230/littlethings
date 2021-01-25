use rand::Rng;

pub fn generate()
{
    let mut random = rand::thread_rng();
    let n1: u8 = random.gen();
    let n2: u16 = random.gen();
    println!("{}",n1);
    println!("{}",n2);
    println!("{}",random.gen::<u32>())
}