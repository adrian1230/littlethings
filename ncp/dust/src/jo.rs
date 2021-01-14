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