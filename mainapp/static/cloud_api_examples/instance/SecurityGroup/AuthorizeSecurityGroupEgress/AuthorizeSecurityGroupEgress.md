### 阿里文档与项目文档差别

项目文档中，请求参数缺少DestGroupOwnerId、SourceCidrIp、SourcePortRange、Description；

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidRegionId.NotFound|InvalidRegionId.NotFound|
|InvalidSecurityGroupId.NotFound|InvalidSecurityGroupId.NotFound|
|OperationDenied|OperationDenied|
|InvalidPortRange.Malformed||
|InvalidSourcePortRange.Malformed||
|InvalidPriority.Malformed|InvalidPriority.Malformed|
|InvalidDestCidrIp.Malformed|InvalidDestCidrIp.Malformed|
|InvalidSourceCidrIp.Malformed||
|MissingParameter|MissingParameter|
|InvalidPolicy.Malformed|InvalidPolicy.Malformed|
|InvalidNicType.ValueNotSupported|InvalidNicType.ValueNotSupported|
|InvalidDestGroupId.Mismatch|InvalidDestGroupId.Mismatch|
|InvalidDestGroupId.NotFound|InvalidDestGroupId.NotFound|
|InvalidDestGroupId.Mismatch|InvalidDestGroupId.Mismatch|
|InvalidNicType.Mismatch||
|AuthorizationLimitExceed|AuthorizationLimitExceed|
|InvalidParamter.Conflict|InvalidParamter.Conflict|
|InvalidDestGroup.NotFound||
|InvalidPriority.ValueNotSupported||
|InvalidDestCidrIp.Malformed||
|InvalidNetworkType.Conflict||
|InvalidSecurityGroup.IsSame||
|InvalidSecurityGroupDiscription.Malformed||
||MissingParameter|
||MissingParameter|
||InvalidIpProtocol.Malformed|
||MissingParameter|
||MissingParameter|
||InvalidDestGroupId.Mismatch|
||InvalidDestGroupOwnerUserAccount.Mismatch|

### lapis 建议

建议请求参数Priority为integer，以更好描述取值范围