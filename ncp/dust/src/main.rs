mod jo;
mod arr;

fn main() {
   jo::joke();
   jo::haha();
   arr::list();
   jo::ty();

   println!("10 => binary {:\
    b} hex {:\
    x} octal {:o\
    }",10,10,10
   );
   println!("{:?}",(12,true,"he"));
}
