pub fn list()
{
	let arr = [1,3,4];
	println!("arr = [1,3,4] {:?}",arr);
	println!("leng: {}",arr.len());
	let li1:[i64;4] = [1,5,2,3];
	println!("arr:[i64;4] = [1,5,2,3] {:?}",li1);
	println!("leng: {}",li1.len());
	let li2:[i32;3] = [1;3];
	println!("li2:[i32;3] = [1;3] {:?}",li2);
	println!("len: {}",li2.len());
}