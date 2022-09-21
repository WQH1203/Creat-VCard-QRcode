 //1.将div转成svg
    // 获取div数据
    var getdiv = document.getElementById("div").innerHTML;
    // 把数据存为SVG
    var data = "data:image/svg+xml," 
    + "<svg xmlns='http://www.w3.org/2000/svg' width='500px' height='400px'>" 
    + "<foreignObject width='100%' height='100%'>" 
    + "<div xmlns='http://www.w3.org/1999/xhtml' >" 
    + divContent 
    + "</div>" 
    + "</foreignObject>" 
    + "</svg>";
    // 创建img
    var img = new Image();
    // 将img的属性值换成data（SVG）
    img.src = data;

//2.svg转成canvas
    //准备空画布
    var canvas = document.createElement("canvas");  
    // 把img的长宽赋予给画布的长和宽
    canvas.width = img.width;
    canvas.height = img.height;
    //取得画布的2d绘图上下文
    var context = canvas.getContext('2d');
    // 给画布上设置颜色
    context.fillStyle="rgb(57, 204, 70)"
    // 给画布上色
    context.fillRect(0, 0, canvas.width, canvas.height);
    // 绘制img
    context.drawImage(img, 0, 0);

//3. 图片导出为 png 格式

    var type = 'png';

    var imgData = canvas.toDataURL(type);


    var _fixType = function (type) {
        type = type.toLowerCase().replace(/jpg/i, 'jpeg');
        var r = type.match(/png|jpeg|bmp|gif/)[0];
        return 'image/' + r;
    };

    imgData = imgData.replace(_fixType(type), 'image/octet-stream');

    var saveFile = function (data, filename) {
        var save_link = document.createElementNS('http://www.w3.org/1999/xhtml', 'a');
        save_link.href = data;
        save_link.download = filename;

        var event = document.createEvent('MouseEvents');
        event.initMouseEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
        save_link.dispatchEvent(event);
    };

    var filename = '01' + (new Date()).getTime() + '.' + type;
