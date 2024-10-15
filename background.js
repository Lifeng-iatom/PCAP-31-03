// 设置定时器，当扩展安装或启动时触发
chrome.runtime.onInstalled.addListener(() => {
  // 每隔 8 小时创建一个定时任务
  chrome.alarms.create("loginAlarm", { periodInMinutes: 480 });
});

// 监听定时器触发事件
chrome.alarms.onAlarm.addListener(function(alarm) {
  if (alarm.name === "loginAlarm") {
    // 打开目标网站 https://portail.enac.fr/113/portal
    chrome.tabs.create({ url: "https://portail.enac.fr/113/portal/" }, function(tab) {
      // 监听页面更新事件，确保在页面完全加载后注入内容脚本
      chrome.tabs.onUpdated.addListener(function listener(tabId, changeInfo) {
        if (tabId === tab.id && changeInfo.status === 'complete') {
          // 注入内容脚本来自动填写登录表单
          chrome.scripting.executeScript({
            target: { tabId: tab.id },
            files: ['content_script.js']   // 注入 content_script.js
          }, () => {
            console.log("Content script injected successfully.");
          });

          // 移除监听器，避免重复执行
          chrome.tabs.onUpdated.removeListener(listener);
        }
      });
    });
  }
});
