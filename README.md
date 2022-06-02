<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-who-at-me

_✨ 看看是谁又在艾特我 ✨_
</div>
  
 # 说明
 你是否遇到过这种情景：你点进一个99+的QQ群，发现有人艾特/回复过你，你满心期待地去查看，结果腾讯告诉你消息过多无法定义到上下文。现在你只需要部署一个机器人卧底即可找出到底是谁艾特了你。
 # 安装
通过`pip`或`nb`安装；

命令：
```shell
pip install nonebot-plugin-who-at-me
```
```shell
nb plugin install nonebot-plugin-who-at-me
```
# 配置
你需要再.env中填写配置
</br>例子：</br>
```ini
at_reminder = ["123456789", "11451461658"]
```
# 使用
（这里默认COMMAND_START为"/"）
```python
/谁艾特我    #查看到底是谁艾特了你
/clear_db    #清理记录
```
你将获得一张劣质的表格】
<div align="center">
  <p><img src=https://s2.loli.net/2022/06/02/hS76NxRYKDIALrn.png width=500 heighth=500></p>
</div>
