# 接口说明

版本：`1.0`

作者：`鲁浩`

日期：`2016.2.14`

|URL|请求方法|说明|
|-|
|/test|GET|测试|
|/test|POST|测试|
|/test|PATCH|测试|
|/test|DELETE|测试|
|/test|PUT|测试|
|/captcha|POST|请求手机的验证码|
|/register|POST|新用户注册|
|/login|GET|用户登录|
|/password|PATCH|修改密码|
|/info|GET|获取用户的信息|
|/info|PATCH|修改用户的信息|
|/follow|GET|获取用户关注信息|
|/follow|POST|关注某用户|
|/follow|DELETE|取消关注某用户|
|/like|GET|获取某对象点赞情况|
|/like|POST|对某对象点赞|
|/like|DELETE|对某对象取消点赞|
|/comment|GET|获取旅程评论情况|
|/comment|POST|对某旅程评论|
|/comment|DELETE|删除旅程评论|
|/event|GET|获取某旅程的事件|
|/event|POST|添加某旅程的事件|
|/event|DELETE|删除某旅程的事件|
|/position|GET|获取附近的用户|
|/position|POST|更新所处位置，如果此时在旅程中，则自动更新路径|
|/route|GET|查看某用户的旅程|
|/route|POST|发布某旅程|
|/route|DELETE|删除某旅程|
|/route|PATCH|修改某旅程|
|/timeline|GET|查看某人时间线|
|/notification|GET|查看个人通知|
|/notification|PATCH|修改个人通知，用于标记已读|
|/feedback|POST|反馈|
|/report|POST|举报|

### 测试
用于测试网络连接，验证服务器的运行是否正常。

### 接口：
GET /test

POST /test

PATCH /test

DELETE /test

PUT /test

### 请求参数：
|名称|定义|必需|默认值|说明|
|-|
||||||

### 响应：
	{
		"code": 100,
		"msg": "OK",
		"data": ""
	}

### 请求验证码
请求一个手机验证码，用于验证用户的手机号。

### 接口
POST /captcha

### 请求参数：
|名称|定义|必需|默认值|说明|
|-|
|phone|手机号|是|||

### 响应：
	{
		"code": 100,
		"msg": "OK",
		"data": ""
	}

### 请求七牛AUTH
请求一个七牛云存储的Auth，用于上传图片。

### 接口
GET /photo

### 请求参数：
|名称|定义|必需|默认值|说明|
|-|
||||||

### 响应：
	{
		"code": 100,
		"msg": "OK",
		"data": "{{AUTH}}"
	}
	
### 点赞
对一个评论/旅程/用户点赞。

### 接口
POST /like

### 请求参数：
|名称|定义|必需|默认值|说明|
|-|
||||||

### 响应：
	{
		"code": 100,
		"msg": "OK",
		"data": "{{AUTH}}"
	}