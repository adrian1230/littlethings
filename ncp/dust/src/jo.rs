pub fn joke() {
    let mut hell = String::from("Baked");
    println!("{}",hell);
    println!("length: {}",hell.len());
    hell.push(' ');
    hell.push_str("steak");
    println!("{}",hell);
    println!("{} capacity",hell.capacity());
    println!("{} from jjj capa",String::from("jjj").capacity());
    println!("{} from jj j capa",String::from("jj j").capacity());
    println!("{} from ' ' capa",String::from(" ").capacity());
    println!(" is empty '' {}",String::from("").is_empty());
    println!(" is empty ' ' {}",String::from(" ").is_empty());
    println!(" is ' ' contain '': {}",
             String::from(
                 " "
             ).contains("")
    );
    println!(" is ' ' contain ' ':  {}",
             String::from(
                 " "
             ).contains(" ")
    );
    println!(" is ' ' contain '         ':  {}",
             String::from(
                 " "
             ).contains("        ")
    );
    println!("replace {}'s {} with {} = {}",
             String::from(
                 "Hall of Hog"
             ),"Hog","Fame",
             String::from("Hall of Hog").replace(
                 "Hog","Fame"
             )
    );
    for k in "w ta bas ic bitch".split_whitespace() {
        println!("{}",k);
    }
}

pub fn haha()
{
	let hero = "Jo";
	let mut age = 17;
	println!("'{1}' {1} {0}",hero,age);
	age = 15;
	println!("{0} {1}",age,hero);
	println!("{0} {1}",hero,age);
}

pub fn ty()
{
    let x = 1;
    let y = 2.6;
    let j : i64 = 11;
    println!("x i32 1 {} y i64 2.6 {} j i64 11 {}",
             x,y,j);
    let u: i64 = 4545445454545;
    println!("u: i64 {}",u);
    // Find max size
    println!("Max i32: {}", std::i32::MAX);
    println!("Max i64: {}", std::i32::MAX);
    println!("Max i128: {}", std::i128::MAX);
}