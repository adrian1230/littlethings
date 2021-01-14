pub fn joke() {
    let mut hell = String::from("Baked");
    println!("{}",hell);
    println!("length: {}",hell.len());
    hell.push(' ');
    hell.push_str("steak");
    println!("{}",hell);
}