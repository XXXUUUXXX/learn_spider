// 获取网页源码

var system = require('system'); //get args
var args = system.args;
if (args.length ===2){
    var port = Number(args[1]);
}
else{
    var port = 8080;
}
var webserver = require('webserver');
var server = webserver.create()
var service = server.listen(port, function(request, response){
    try{
        var postRaw = request.postRaw;
        var aaa = new Array();
        aaa = postRaw.split('=');
        var url = aaa[0];
        var md5_url = aaa[1];
        url = decodeURIComponent(url);

        //创建page
        var webPage = require('webpage');
        var page = webPage.create();
        page.settings.resourceTimeout = 20000; //timeout is 20s

        //页面错误捕捉
        page.onError = function(msg, trace){
            console.log('[Warning]This is page.onError');
            var msgStack = ['ERROR: ' + msg];
            if (trace && trace.length) {
                msgStack.push('TRACE:');
                trace.forEach(function(t){
                    msgStack.push(' -> ' + t.file + ': ' + t.line + (t.function ? ' (in function "' + t.function +'")' : ''));
                });
            }
            // console.error(msgStack.join('\n'));
        };
        //phantomjs错误捕捉
        phantom.onError = function(msg, trace){
            console.log("[Warning]This is phantom.onError");
            var msgStack = ['PHantom ERROR: ' + msg];
            if (trace && trace.length){
                msgStack.push('TRACE:');
                trace.forEach(function(t){
                    msgStack.push(' -> ' + (t.file || t.sourceURL) + ': ' + t.line + (t.function ?'(in function ' +t.function +')':''));
                });
            }
            console.error(msgStack.join('\n'));
            phantom.exit(1);
        };
        //打开网页，获取源码
        page.open(url, function (status) {
            console.log('Target_url is ' + url); //输出待检测的网站url
            if(status == 'success'){
                var current_url = page.url;
                var body = page.conntent;
            }
            else{
                var body = '';
                var current_url = '';
            }
            response.status = 200;
            // response.write(body); //返回获取到的网页源码
            response.write(current_url); //返回当前网页的url
            page.close();
            response.close();
        });
    }
    catch(e)
    {
        console.log('[Error]' + e.message + 'happen' + e.lineNumber + 'line');
    }
};)