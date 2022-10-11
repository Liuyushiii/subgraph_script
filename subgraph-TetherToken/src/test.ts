


function get_random_string(len: number) {
    let res: string = '';
    let range: string = 'abcdefghijklmnopqrstuvwxyz0123456789';

    for (let i = 0; i < len; i++) {

      let index: number = Math.random() * range.length
      console.log(index)
      console.log(Math.floor(index))
      res += range.charAt(index: i32);

    }

    return res;
}

console.log(get_random_string(12))