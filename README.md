<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://s2.loli.net/2022/06/16/opBDE8Swad5rU3n.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://s2.loli.net/2022/06/16/xsVUGRrkbn1ljTD.png" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-who-at-me

_✨ 看看是谁又在艾特我 ✨_
</div>
  
 # 说明
 你是否遇到过这种情景：你点进一个99+的QQ群，发现有人艾特/回复过你，你满心期待地去查看，结果腾讯告诉你消息过多无法定义到上下文。现在你只需要部署一个机器人卧底即可找出到底是谁艾特了你。
 # 安装
通过`pip`或`nb`安装；
需要协议端支持转发合并消息。

命令：
```shell
pip install nonebot-plugin-who-at-me
```
```shell
nb plugin install nonebot-plugin-who-at-me
```
# 配置
记得配置SUPERUSERS
```shell
reminder_expire_time 合并转发消息记录的超时时间, 单位为天
```
# 使用
<div align="center">

（这里默认COMMAND_START为"/"）
| 命令              | 描述              |
| ------------------ | --------------- |
|/谁艾特我 | 查看到底是谁艾特了你       |
|/clear_db     | 清理当前用户的消息记录 |
|/clear_all     | 清理全部消息记录     |

<del>你将获得一张劣质的表格】</del></br>
没有图片！只有合并转发辣！
