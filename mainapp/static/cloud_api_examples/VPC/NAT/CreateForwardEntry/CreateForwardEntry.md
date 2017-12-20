### 项目文档与阿里文档的差异

阿里文档中使用DNAT来表示端口转发规则；

项目文档中，API描述部分和阿里文档有差异；

项目文档中，请求参数ExternalIp的语义描述和阿里文档不一致；

阿里文档用公网私网来表示源端和目的端


### lapis建议

建议请求参数ExternalPort，InternalPort类型修改为integer，以更好地描述取值范围