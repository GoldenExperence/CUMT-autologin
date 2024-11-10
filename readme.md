# 项目说明
 
这是一个使用**Python**为**CUMTer**设计的**校园网wifi**自动登录脚本。
脚本通过**ChromeDriver**实现模拟登录操作。
ChromeDriver和对应版本的Chrome已在Chrome文件夹中给出，首次使用需打开Chrome文件夹安装对应版本的Chrome。
推荐将本脚本设置为开机自启动以实现登录。

---

## 代码结构

- `login.py`：校园网自动登录脚本
- `login_script.bat`：调用`login.py`进行校园网登录，用于配置开机自启动
- `config.txt`：设定学号、密码和运营商的配置文件
- `requirements.txt`：记录了项目的第三方依赖库

---

## 功能

- 自动检测并判断是否连接到了校园网wifi。
- 如果连接到了其它无线网络则自动退出。
- 如果连接到校园网，则自动登录到校园网。
- 支持选择 ISP（互联网服务提供商）。

---

## 依赖库
- `time`
- `os`
- `subprocess`
- `datetime`
- `selenium`（需要安装ChromeDriver）
 
---

## 基本使用方法
1. 首先，安装版本号高于*130*的**Chrome**浏览器。
2. 如果还没有安装`selenium`库，在控制台执行以下命令安装：
    `pip install selenium`（使用pip安装）
    或
    `conda install selenium`（使用conda安装）
3. 打开并编辑配置文件`config.txt`，设置你的学号、密码、运营商并保存。
4. 将`login_script.bat`设置为开机自动运行的脚本，具体方法如下：  
    **方法一**：将`.bat`文件添加到启动文件夹  
        1）. 按下**Win + R**，输入`shell:startup`并按`Enter`，打开Windows启动文件夹。  
        2）. 将 `login_script.bat` 文件的快捷方式复制到文件夹中。  
    **方法二**：使用任务计划程序  
        1）打开任务计划程序：按下 **Win + R**，输入 `taskschd.msc` 并按 Enter。  
        2）在任务计划程序中选择*创建任务*。  
        3）在*常规*标签页中，设置任务名称。  
        4）切换到*触发器*标签页，点击*新建*，然后选择*在登录时*作为触发器。  
        5）切换到*操作*标签页，点击*新建*，然后选择*启动程序*，在程序或脚本框中选择`login_script.bat`文件。  
        6）点击*确定*完成设置。  

---

## 代码说明

### get_wifi_name()
 
- 功能：获取当前连接的Wi-Fi名称。
- 实现：通过调用 `netsh wlan show interfaces` 命令并解析输出。
 
### send_login_request()
 
- 功能：发送登录请求，自动填写登录表单并提交。
- 实现：
- 使用Selenium启动Chrome浏览器。
- 打开校园网登录页面。
- 自动填写用户名、密码及选择运营商。
- 点击登录按钮。
 
### main()
 
- 功能：主程序，循环检测Wi-Fi名称并在符合条件时发送登录请求。
- 实现：
- 设置脚本运行时间限制（默认150秒）。
- 循环检测当前连接的Wi-Fi名称。
- 如果Wi-Fi名称与TARGET_SSID匹配，则发送登录请求并结束循环。
- 如果不匹配或未检测到Wi-Fi名称，则结束循环。

---

## 使用说明
 
1. 将脚本和 `config.txt` 文件放置在同一目录下。
2. 确保 `config.txt` 文件中正确填写了用户名、密码和运营商信息。
3. 如果已安装其它版本的Chrome浏览器，请下载对应版本的**ChromeDriver**并放到`Chrome`文件夹内，替换掉原有的`chromedriver.exe`。
4. `Chrome`文件夹中的安装程序在安装后可以被删除以节省磁盘空间。
5. 脚本默认运行时间为150秒，如需修改请修改login.py中第16行的LIMIT变量。

---

ps：我好像忘记考虑连接有线网的cumte的自动登录了emmm......  
  
***The End***
