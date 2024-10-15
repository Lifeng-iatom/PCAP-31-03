console.log('Content script running on ENAC portal...');

// 第一步：点击 "Logout" 按钮，断开当前连接
var logoutButton = document.getElementById('feedbackForm_disconnect_button');
if (logoutButton) {
    logoutButton.click();
    console.log('Logout button clicked, disconnecting...');
} else {
    console.log('Logout button not found, continuing with login...');
}

// 第二步：等待几秒钟，确保断开连接的操作完成后再执行登录
setTimeout(function() {
    // 输入账号和密码
    var loginInput = document.getElementById('uc-logonForm-login');
    var passwordInput = document.getElementById('uc-logonForm-passwd');
    var loginButton = document.getElementById('logonForm_connect_button');

    if (loginInput && passwordInput && loginButton) {
        loginInput.value = '替换为你的用户名';  // 替换为你的用户名
        passwordInput.value = '替换为你的密码';  // 替换为你的密码

        console.log('Username and password entered.');

        // 模拟点击 "Connect" 按钮
        loginButton.click();
        console.log('Login button clicked, submitting the form...');

        // 第三步：等待0.05秒，确保表单提交完成，然后关闭网页
        setTimeout(function() {
            console.log('Closing the webpage...');
            window.close();  // 尝试关闭当前页面
        }, 50);  // 延迟 0.05 秒后关闭网页
    } else {
        console.error('Login form elements not found.');
    }
}, 3000);  // 等待 3 秒后再执行登录操作
