# 提取隐藏信息
let zeroWidthArr = link.replace(/[^\u200b-\u200d]/g, "").split('•'); // zero-width joiner

# 将零宽字符串转成二进制数，再转成字符
function zeroWidthToStr (zeroWidthStr) {
    let binaryStr = zeroWidthStr.split('').map((zeroWidthChar) => {
        if (zeroWidthChar === '•') {
            return '1';
        } else {
            return '0';
        }
    }).join('');
        
    return binaryToStr(+binaryStr)
}

// 将二进制数转成字符
function binaryToStr(binary) {
    return String.fromCharCode(parseInt(binary, 2));
}

let myName = zeroWidthArr.map(zeroWidthToStr).join('');
console.log({myName}) // 'LvLin'