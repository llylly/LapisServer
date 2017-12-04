### 阿里文档勘误

响应元素(Response Elements)表中，PostResponse的描述内，“子节点：Bucket, ETag, Key, Location”，而key未出现在整个响应元素表中

### 项目文档勘误

响应元素(Response Elements)表中，PostResponse的描述内，“子节点：Bucket, ETag, Key, Location”，而key未出现在整个响应元素表中

### 文档差别

完全相同

### 其他说明

#### Post Policy
 
Post请求的policy表单域用于验证请求的合法性。 policy为一段经过UTF-8和base64编码的JSON文本，声明了Post请求必须满足的条件。虽然对于public-read-write的bucket上传时，post表单域为可选项，我们强烈建议使用该域来限制Post请求。
  
#### policy示例
 
{ "expiration": "2014-12-01T12:00:00.000Z",
"conditions": [
{"bucket": "johnsmith" },
["starts-with", "$key", "user/eric/"]
]
}
Post policy中必须包含expiration和condtions。
  
#### Expiration
 
Expiration项指定了policy的过期时间，以ISO8601 GMT时间表示。例如”2014-12-01T12:00:00.000Z”指定了Post请求必须发生在2014年12月1日12点之前。
  
#### Conditions
 
Conditions是一个列表，可以用于指定Post请求的表单域的合法值。注意：表单域对应的值在检查policy之后进行扩展，因此，policy中设置的表单域的合法值应当对应于扩展之前的表单域的值。例如，如果设置key表单
域为user/user1/${filename}，用户的文件名为a.txt，则Post policy应当设置成[“eq”, “$key”, “user/user1/\${filename}”]，而不是[“eq”, “$key”，“$key”, “user/user1/a.txt”]。Policy中支持
的conditions项见下表：
 
|名称|	描述|
|:-:|:-:|
|content-length-range|	上传文件的最小和最大允许大小。 该condition支持contion-length-range匹配方式。|
|Cache-Control, Content-Type, ContentDisposition, Content-Encoding, Expires	|HTTP请求头。 该condition支持精确匹配和 starts-with匹配方式。|
|key	|上传文件的object名称。 该condition支持精确匹配和starts-with匹配方式。|
|success_action_redirect	|上传成功后的跳转URL地址。 该condition支持精确匹配和starts-with匹配方式。|
|success_action_status	|未指定success_action_redirect时，上传成功后的返回状态码。 该condition支持精确匹配和startswith匹配方式。|
|x-oss-meta-*	|用户指定的user meta。 该condition支持精确匹配和starts-with匹配方式。|
如果Post请求中包含其他的表单域，可以将这些额外的表单域加入到policy的conditions中,conditions不涉及的表单域将不会进行合法性检查。
  
#### Conditions匹配方式
 
|Conditions匹配方式|	描述|
|:-:|:-:|
|精确匹配	|表单域的值必须精确匹配conditions中声明的值。如指定key表单域的值必须为a： {“key”: “a”} 同样可以写为： [“eq”, “$key”, “a”]|
|Starts With	|表单域的值必须以指定值开始。例如指定key的值必须以/user/user1开始： [“starts-with”, “$key”, “/user/user1”]|
|指定文件大小	|指定所允许上传的文件最大大小和最小大小，例如允许的文件大小为1到10字节： [“content-length-range”, 1, 10]|
 
####转义字符
 
于在 Post policy 中 $ 表示变量，所以如果要描述 $，需要使用转义字符\$。除此之外，JSON 将对一些字符
进行转义。下图描述了 Post policy 的 JSON 中需要进行转义的字符。
 
|转义字符	|描述|
|:-:|:-:|
|\/	|斜杠|
|\	|反斜杠|
|\”	|双引号|
|\$	|美元符|
|\b	|空格|
|\f	|换页|
|\n	|换行|
|\r	|回车|
|\t	|水平制表符|
|\uxxxx|	Unicode 字符|
 
#### Post Signature
 
对于验证的Post请求，HTML表单中必须包含policy和Signature信息。policy控制请求中那些值是允许的。计
算Signature的具体流程为：
 
1.	创建一个 UTF-8 编码的 policy。
2.	将 policy 进行 base64 编码，其值即为 policy 表单域该填入的值，将该值作为将要签名的字符串。
3.	使用 AccessKeySecret 对要签名的字符串进行签名，签名方法与Head中签名的计算方法相同（将要签名的字符串替换为 policy 即可）。
 	 
#### 示例 Demo
 
- Web 端表单直传 OSS 示例 Demo：点击这里
