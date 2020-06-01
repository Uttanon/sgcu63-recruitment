const {Builder, By, Key, util} = require("selenium-webdriver");
var webdriver = require('selenium-webdriver');
var name = [];
var slogan = [];
async function bann(){
    var driver = await new Builder().forBrowser("firefox").build();
    await driver.get("https://rubnongkaomai.com/baan/");
    await driver.wait(webdriver.until.elementLocated(By.className('ant-tabs-tab')), 10000);
    var allb = await driver.findElements(By.className('ant-tabs-tab'))
    let count = allb.length;
    for(i=0;i<count;i++){
      allb[i].click();
      await sleep(100);
    }
    var keep = [];
    let temp = await driver.findElements(webdriver.By.xpath('//div[@class="ant-col ant-col-8"]/a'))
    for (var i = 0; i < temp.length; i++) {
        temp[i].getAttribute("href").then(function(x){
            keep.push(x)
        })
    }
    await sleep(5000);
    for(var i = 0 ; i < keep.length ; i++){
      await sleep(100)
      driver.get(keep[i]);
      await sleep(1000)
      await driver.wait(webdriver.until.elementLocated(webdriver.By.xpath('//h1[@type="header"]')),10000)
      driver.findElement(webdriver.By.xpath('//h1[@type="header"]')).getText().then(function(x){
        name.push(x)
      })
      driver.findElement(webdriver.By.xpath('//h3[@type="header"]')).getText().then(function(x){
        slogan.push(x)
      })
    }
    await sleep(5000);
    console.log(name)
    console.log(slogan)
    driver.close()
}
function sleep(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}

bann();
