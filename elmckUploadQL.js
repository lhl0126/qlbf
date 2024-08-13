/*
2024.7.10
软件：  饿了么app获取ck 上传青龙
获取ck：  打开软件-再返回后台即可

【QX】
[rewrite_local]
# 抓取ck
https://nt2.ele.me/c/b url script-request-header elmckUploadQL.js

[mitm]
nt2.ele.me

*/

// 填写青龙地址
const qlUrl = "http://ql.lhl0126.us.kg:1028";
// 填写青龙应用密钥
const clientSecret = "e_iKjSqKx32B264Ukm1p2Py-";
// 填写青龙应用id
const clientId = "Li0Y7l2lck4-";






// 以下不用填写
const $ = new Env("饿了么获取ck上传青龙");
let qlToken= "";
let userIDValue='';
let qlEnvId='';
let addData = [];
let isGetCookie = typeof $request !== 'undefined'
if (isGetCookie) {
    GetRewrite();
}

async function GetRewrite() {
    if($request.url.indexOf(`c/b`) > -1) {
        // console.log($request.headers.Cookie);
        var cookie2Value = $request.headers.Cookie.match(/cookie2=([^;]+)/)[1];

        var SIDValue = $request.headers.Cookie.match(/SID=([^;]+)/)[1];

        var nkValue = $request.headers.Cookie.match(/_nk_=([^;]+)/)[1];

// SID=X;cookie2=X;USERID=X;_tb_token_=X;
        userIDValue = $request.headers.Cookie.match(/USERID=([^;]+)/)[1];
        var tbtokenValue = $request.headers.Cookie.match(/_tb_token_=([^;]+)/)[1];

// 输出结果
        let ck = 'SID=' + SIDValue+ ';cookie2=' + cookie2Value + ';USERID=' + userIDValue + ';_tb_token_=' + tbtokenValue + ';';
        if(!SIDValue) return;
        let decodedValue = decodeURIComponent(nkValue);
        let outputStr = decodeUnicode(decodedValue);
        $.msg('饿了么Cookie', `用户${outputStr}获取成功\n\n${ck}\n\n\n`, '');
        // 上传青龙
        if (qlUrl.length > 0 && clientSecret.length > 0 && clientId.length >0){
            // console.log(`上传青龙:${JSON.stringify(addData)}`);
            await getQlToekn();
            await getAllEnvs();
            for (let i = 0; i< $.envsList.length; i++){
                if ($.envsList[i]["name"] === 'elmck' && $.envsList[i]["value"].indexOf('USERID=' + userIDValue) > -1){
                    // console.log(`【${userIDValue}】 用户已存在青龙变量\n  ${JSON.stringify($.envsList[i])} `);
                    qlEnvId = $.envsList[i]['_id'];
                    console.log(`id【${qlEnvId}】 `);
                    break;
                }
            }
            if (qlEnvId.length > 0){
                console.log(`\n更新变量`)
                const updateEnvBody = {name: 'elmck', value: ck, remarks: 'qx_'+outputStr, _id: qlEnvId};
                // console.log(`\n更新变量${JSON.stringify(updateEnvBody)}`);
                updateEnv(updateEnvBody);
            }else{
                console.log(`\n新增变量`)
                addData.push({ name: 'elmck', value: ck, remarks: 'qx_'+outputStr});
                await addEnv(addData);
            }

            // $.msg('饿了么Cookie', `上传青龙:${JSON.stringify(addData)}`, '');
        }
    }
}


function decodeUnicode(str) {
    return str.replace(/\\u([0-9a-fA-F]{4})/g, function (match, grp) {
        return String.fromCharCode(parseInt(grp, 16));
    });
}




// 获取所有变量
async function getAllEnvs(timeout = 0) {
    return new Promise((resolve) => {
        setTimeout(() => {
            let url = {
                url: qlUrl + `/open/envs`,
                headers: {
                    "Content-Type": "application/json;charset=UTF-8",
                    "Authorization": "Bearer " + qlToken
                }
            };
            $.get(url, async (err, resp, data) => {
                try {
                    // $.log(`所有变量🚩: ${data}`);
                    $.envsData = JSON.parse(data);
                    if ($.envsData.code === 200){
                        $.envsList = $.envsData.data;
                    } else {
                        $.msg(`获取变量失败~`, ``, `${$.posteventID.msg}`);
                    }
                } catch (e) {
                    $.logErr(e, resp);
                } finally {
                    resolve()
                }
            })
        }, timeout)
    })
}


// 获取所有变量
async function getQlToekn(timeout = 0) {
    return new Promise((resolve) => {
        setTimeout(() => {
            let url = {
                url: qlUrl + `/open/auth/token?client_id=${clientId}&client_secret=${clientSecret}`,
                headers: {"Content-Type": "application/json;charset=UTF-8"}
            };
            $.get(url, async (err, resp, data) => {
                try {
                    if (err) {
                        console.log(`${JSON.stringify(err)}`)
                        console.log(`${$.name} API请求失败，请检查网路重试`)
                        $.done();
                    }else{
                        qlToken = JSON.parse(data).data.token;
                    }
                } catch (e) {
                    $.logErr(e, resp);
                } finally {
                    resolve()
                }
            })
        }, timeout)
    })
}
async function addEnv(envData) {
    return new Promise(resolve => {
        const options = {
            url: qlUrl + `/open/envs`,
            headers: {
                "Content-Type": "application/json;charset=UTF-8",
                "Authorization": "Bearer " + qlToken
            },
            body: JSON.stringify(envData),
        }
        $.post(options, (err, resp, data) => {
            try {

                if (err) {
                    console.log(`${JSON.stringify(err)}`)
                    console.log(`${$.name} API请求失败，请检查网路重试`)
                } else {
                    if (JSON.parse(data).code === 200) {
                        $.msg('饿了么ck上传新增青龙成功', `用户${envData[0]["remarks"]}[id:${userIDValue}]`, '');
                    }else{
                        $.msg('饿了么ck上传新增青龙失败', `用户${data}`, '');
                    }
                }
            } catch (e) {
                $.logErr(e, resp)
            } finally {
                resolve();
                $.done();
            }
        })
    })
}
async function updateEnv(updateEnvBody) {
    return new Promise(resolve => {

        const url = qlUrl + `/open/envs`
        const method = "PUT";
        const headers = {
            "Content-Type": "application/json",
            "accept": "application/json",
            "Authorization": "Bearer " + qlToken
        };
        const myRequest = {
            url: url,
            method: method, // Optional, default GET.
            headers: headers, // Optional.
            body: JSON.stringify(updateEnvBody) // Optional.
        };

        $task.fetch(myRequest).then(response => {
            if (JSON.parse(response.body).code === 200) {
                $.msg('饿了么ck上传更新青龙成功', `用户${updateEnvBody["remarks"]}[id:${userIDValue}]`, '');
            }else{
                $.msg('饿了么ck上传更新青龙失败', `${response.body}`, '');
            }
            $.done();
        }, reason => {
            console.log(`${reason.error}`)
            console.log(`${$.name} API请求失败，请检查网路重试`)
            $done();
        });
    })
}


// prettier-ignore
function Env(t,e){"undefined"!=typeof process&&JSON.stringify(process.env).indexOf("GITHUB")>-1&&process.exit(0);class s{constructor(t){this.env=t}send(t,e="GET"){t="string"==typeof t?{url:t}:t;let s=this.get;return"POST"===e&&(s=this.post),new Promise((e,i)=>{s.call(this,t,(t,s,r)=>{t?i(t):e(s)})})}get(t){return this.send.call(this.env,t)}post(t){return this.send.call(this.env,t,"POST")}}return new class{constructor(t,e){this.name=t,this.http=new s(this),this.data=null,this.dataFile="box.dat",this.logs=[],this.isMute=!1,this.isNeedRewrite=!1,this.logSeparator="\n",this.startTime=(new Date).getTime(),Object.assign(this,e),this.log("",`🔔${this.name}, 开始!`)}isNode(){return"undefined"!=typeof module&&!!module.exports}isQuanX(){return"undefined"!=typeof $task}isSurge(){return"undefined"!=typeof $httpClient&&"undefined"==typeof $loon}isLoon(){return"undefined"!=typeof $loon}toObj(t,e=null){try{return JSON.parse(t)}catch{return e}}toStr(t,e=null){try{return JSON.stringify(t)}catch{return e}}getjson(t,e){let s=e;const i=this.getdata(t);if(i)try{s=JSON.parse(this.getdata(t))}catch{}return s}setjson(t,e){try{return this.setdata(JSON.stringify(t),e)}catch{return!1}}getScript(t){return new Promise(e=>{this.get({url:t},(t,s,i)=>e(i))})}runScript(t,e){return new Promise(s=>{let i=this.getdata("@chavy_boxjs_userCfgs.httpapi");i=i?i.replace(/\n/g,"").trim():i;let r=this.getdata("@chavy_boxjs_userCfgs.httpapi_timeout");r=r?1*r:20,r=e&&e.timeout?e.timeout:r;const[o,h]=i.split("@"),n={url:`http://${h}/v1/scripting/evaluate`,body:{script_text:t,mock_type:"cron",timeout:r},headers:{"X-Key":o,Accept:"*/*"}};this.post(n,(t,e,i)=>s(i))}).catch(t=>this.logErr(t))}loaddata(){if(!this.isNode())return{};{this.fs=this.fs?this.fs:require("fs"),this.path=this.path?this.path:require("path");const t=this.path.resolve(this.dataFile),e=this.path.resolve(process.cwd(),this.dataFile),s=this.fs.existsSync(t),i=!s&&this.fs.existsSync(e);if(!s&&!i)return{};{const i=s?t:e;try{return JSON.parse(this.fs.readFileSync(i))}catch(t){return{}}}}}writedata(){if(this.isNode()){this.fs=this.fs?this.fs:require("fs"),this.path=this.path?this.path:require("path");const t=this.path.resolve(this.dataFile),e=this.path.resolve(process.cwd(),this.dataFile),s=this.fs.existsSync(t),i=!s&&this.fs.existsSync(e),r=JSON.stringify(this.data);s?this.fs.writeFileSync(t,r):i?this.fs.writeFileSync(e,r):this.fs.writeFileSync(t,r)}}lodash_get(t,e,s){const i=e.replace(/\[(\d+)\]/g,".$1").split(".");let r=t;for(const t of i)if(r=Object(r)[t],void 0===r)return s;return r}lodash_set(t,e,s){return Object(t)!==t?t:(Array.isArray(e)||(e=e.toString().match(/[^.[\]]+/g)||[]),e.slice(0,-1).reduce((t,s,i)=>Object(t[s])===t[s]?t[s]:t[s]=Math.abs(e[i+1])>>0==+e[i+1]?[]:{},t)[e[e.length-1]]=s,t)}getdata(t){let e=this.getval(t);if(/^@/.test(t)){const[,s,i]=/^@(.*?)\.(.*?)$/.exec(t),r=s?this.getval(s):"";if(r)try{const t=JSON.parse(r);e=t?this.lodash_get(t,i,""):e}catch(t){e=""}}return e}setdata(t,e){let s=!1;if(/^@/.test(e)){const[,i,r]=/^@(.*?)\.(.*?)$/.exec(e),o=this.getval(i),h=i?"null"===o?null:o||"{}":"{}";try{const e=JSON.parse(h);this.lodash_set(e,r,t),s=this.setval(JSON.stringify(e),i)}catch(e){const o={};this.lodash_set(o,r,t),s=this.setval(JSON.stringify(o),i)}}else s=this.setval(t,e);return s}getval(t){return this.isSurge()||this.isLoon()?$persistentStore.read(t):this.isQuanX()?$prefs.valueForKey(t):this.isNode()?(this.data=this.loaddata(),this.data[t]):this.data&&this.data[t]||null}setval(t,e){return this.isSurge()||this.isLoon()?$persistentStore.write(t,e):this.isQuanX()?$prefs.setValueForKey(t,e):this.isNode()?(this.data=this.loaddata(),this.data[e]=t,this.writedata(),!0):this.data&&this.data[e]||null}initGotEnv(t){this.got=this.got?this.got:require("got"),this.cktough=this.cktough?this.cktough:require("tough-cookie"),this.ckjar=this.ckjar?this.ckjar:new this.cktough.CookieJar,t&&(t.headers=t.headers?t.headers:{},void 0===t.headers.Cookie&&void 0===t.cookieJar&&(t.cookieJar=this.ckjar))}get(t,e=(()=>{})){t.headers&&(delete t.headers["Content-Type"],delete t.headers["Content-Length"]),this.isSurge()||this.isLoon()?(this.isSurge()&&this.isNeedRewrite&&(t.headers=t.headers||{},Object.assign(t.headers,{"X-Surge-Skip-Scripting":!1})),$httpClient.get(t,(t,s,i)=>{!t&&s&&(s.body=i,s.statusCode=s.status),e(t,s,i)})):this.isQuanX()?(this.isNeedRewrite&&(t.opts=t.opts||{},Object.assign(t.opts,{hints:!1})),$task.fetch(t).then(t=>{const{statusCode:s,statusCode:i,headers:r,body:o}=t;e(null,{status:s,statusCode:i,headers:r,body:o},o)},t=>e(t))):this.isNode()&&(this.initGotEnv(t),this.got(t).on("redirect",(t,e)=>{try{if(t.headers["set-cookie"]){const s=t.headers["set-cookie"].map(this.cktough.Cookie.parse).toString();s&&this.ckjar.setCookieSync(s,null),e.cookieJar=this.ckjar}}catch(t){this.logErr(t)}}).then(t=>{const{statusCode:s,statusCode:i,headers:r,body:o}=t;e(null,{status:s,statusCode:i,headers:r,body:o},o)},t=>{const{message:s,response:i}=t;e(s,i,i&&i.body)}))}post(t,e=(()=>{})){if(t.body&&t.headers&&!t.headers["Content-Type"]&&(t.headers["Content-Type"]="application/x-www-form-urlencoded"),t.headers&&delete t.headers["Content-Length"],this.isSurge()||this.isLoon())this.isSurge()&&this.isNeedRewrite&&(t.headers=t.headers||{},Object.assign(t.headers,{"X-Surge-Skip-Scripting":!1})),$httpClient.post(t,(t,s,i)=>{!t&&s&&(s.body=i,s.statusCode=s.status),e(t,s,i)});else if(this.isQuanX())t.method="POST",this.isNeedRewrite&&(t.opts=t.opts||{},Object.assign(t.opts,{hints:!1})),$task.fetch(t).then(t=>{const{statusCode:s,statusCode:i,headers:r,body:o}=t;e(null,{status:s,statusCode:i,headers:r,body:o},o)},t=>e(t));else if(this.isNode()){this.initGotEnv(t);const{url:s,...i}=t;this.got.post(s,i).then(t=>{const{statusCode:s,statusCode:i,headers:r,body:o}=t;e(null,{status:s,statusCode:i,headers:r,body:o},o)},t=>{const{message:s,response:i}=t;e(s,i,i&&i.body)})}}time(t,e=null){const s=e?new Date(e):new Date;let i={"M+":s.getMonth()+1,"d+":s.getDate(),"H+":s.getHours(),"m+":s.getMinutes(),"s+":s.getSeconds(),"q+":Math.floor((s.getMonth()+3)/3),S:s.getMilliseconds()};/(y+)/.test(t)&&(t=t.replace(RegExp.$1,(s.getFullYear()+"").substr(4-RegExp.$1.length)));for(let e in i)new RegExp("("+e+")").test(t)&&(t=t.replace(RegExp.$1,1==RegExp.$1.length?i[e]:("00"+i[e]).substr((""+i[e]).length)));return t}msg(e=t,s="",i="",r){const o=t=>{if(!t)return t;if("string"==typeof t)return this.isLoon()?t:this.isQuanX()?{"open-url":t}:this.isSurge()?{url:t}:void 0;if("object"==typeof t){if(this.isLoon()){let e=t.openUrl||t.url||t["open-url"],s=t.mediaUrl||t["media-url"];return{openUrl:e,mediaUrl:s}}if(this.isQuanX()){let e=t["open-url"]||t.url||t.openUrl,s=t["media-url"]||t.mediaUrl;return{"open-url":e,"media-url":s}}if(this.isSurge()){let e=t.url||t.openUrl||t["open-url"];return{url:e}}}};if(this.isMute||(this.isSurge()||this.isLoon()?$notification.post(e,s,i,o(r)):this.isQuanX()&&$notify(e,s,i,o(r))),!this.isMuteLog){let t=["","==============📣系统通知📣=============="];t.push(e),s&&t.push(s),i&&t.push(i),console.log(t.join("\n")),this.logs=this.logs.concat(t)}}log(...t){t.length>0&&(this.logs=[...this.logs,...t]),console.log(t.join(this.logSeparator))}logErr(t,e){const s=!this.isSurge()&&!this.isQuanX()&&!this.isLoon();s?this.log("",`❗️${this.name}, 错误!`,t.stack):this.log("",`❗️${this.name}, 错误!`,t)}wait(t){return new Promise(e=>setTimeout(e,t))}done(t={}){const e=(new Date).getTime(),s=(e-this.startTime)/1e3;this.log("",`🔔${this.name}, 结束! 🕛 ${s} 秒`),this.log(),(this.isSurge()||this.isQuanX()||this.isLoon())&&$done(t)}}(t,e)}
