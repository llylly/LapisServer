### 阿里文档勘误

无

### 项目文档勘误

无

### 文档差别

完全相同

### 不适合放在swagger中的内容（不是常见属性）

#### 存储访问日志记录的object命名规则
 
<TargetPrefix><SourceBucket>-YYYY-mm-DD-HH-MM-SS-UniqueString
命名规则中，TargetPrefix由用户指定；YYYY, mm, DD, HH, MM和SS分别是该Object被创建时的阿拉伯数字的年，月，日，小时，分钟和秒（注意位数）；UniqueString为OSS系统生成的字符串。一个实际的用于存储 OSS访问日志的Object名称例子如下：
 
MyLog-oss-example-2012-09-10-04-00-00-0000
上例中，“MyLog-”是用户指定的Object前缀；“oss-example”是源bucket的名称；“2012-09-10-04-
00-00”是该Object被创建时的北京时间；“0000” 是OSS系统生成的字符串。
 
 
#### LOG文件格式
 
|名 称|	例 子	|含 义|
|:-:|:-:|:-:|
|Remote IP|	119.140.142.11	|请求发起的IP地址（Proxy代理或用户防火墙可能会屏蔽该字段）|
|Reserved|	-	|保留字段|
|Reserved|	-|	保留字段|
|Time	|[02/May/2012:00:00:04+0800]	|OSS收到请求的时间|
|Request-URI	|“GET /aliyun-logo.pngHTTP/1.1“	|用户请求的URI(包括query-string)|
|HTTP Status|	200|	OSS返回的HTTP状态码|
|SentBytes|	5576	|用户从OSS下载的流量|
|RequestTime (ms)|	71	|完成本次请求的时间（毫秒）|
|Referer	|http://www.aliyun.com/product/oss	|请求的HTTPReferer|
|User-Agent	|curl/7.15.5	|HTTP的User-Agent头|
|HostName	|oss-example.oss-cnhangzhou.aliyuncs.com	|请求访问域名|
|Request |ID|	505B01695037C2AF032593A4	|用于唯一标示该请求的UUID|
|LoggingFlag	|true	|是否开启了访问日志功能|
|Reserved	|-	|保留字段|
|Requester Aliyun ID	|1657136103983691	|请求者的阿里云ID；匿名访问为“-”|
|Operation	|GetObject	|请求类型|
|Bucket|	oss-example	|请求访问的Bucket名字|
|Key|	/aliyun-logo.png|	用户请求的Key|
|ObjectSize|	5576|	Object大小|
|Server Cost Time (ms)|	17|	OSS服务器处理本次请求所花的时间（毫秒）|
|Error Code|	NoSuchBucket|	OSS返回的错误码|
|Request Length	|302|	用户请求的长度（Byte）|
|UserID|	1657136103983691|	Bucket拥有者ID|
|Delta DataSize|	280	|Bucket大小的变化量；若没有变化为“-”|
|Sync Request|	-	|是否是CDN回源请求；若不是为“-”|
|Reserved|	-	|保留字段|
