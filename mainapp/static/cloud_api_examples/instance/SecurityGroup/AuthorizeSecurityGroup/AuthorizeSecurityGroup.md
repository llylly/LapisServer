### 阿里文档与项目文档差别

项目文档中，请求参数缺少SourceGroupOwnerId、SourcePortRange、DestCidrIp；

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidRegionId.NotFound|InvalidRegionId.NotFound|
|InvalidSecurityGroupId.NotFound|InvalidSecurityGroupId.NotFound|
|OperationDenied|OperationDenied|
|InvalidIpProtocol.Malformed|InvalidIpProtocol.Malformed|
|InvalidPriority.Malformed|InvalidPriority.Malformed|
|InvalidSourceGroupId.Mismatch|InvalidSourceGroupId.Mismatch|
|InvalidSourceCidrIp.Malformed|InvalidSourceCidrIp.Malformed|
|InvalidDestCidrIp.Malformed||
|MissingParameter|MissingParameter|
|InvalidPolicy.Malformed|InvalidPolicy.Malformed|
|InvalidNicType.ValueNotSupported|InvalidNicType.ValueNotSupported|
|InvalidParamter.Conflict|InvalidParamter.Conflict|
|InvalidSourceGroupId.Mismatch|InvalidSourceGroupId.Mismatch|
|InvalidSourceGroupId.NotFound|InvalidSourceGroupId.NotFound|
|InvalidNicType.Mismatch||
|AuthorizationLimitExceed|AuthorizationLimitExceed|
|InvalidSourceGroup.NotFound||
|InvalidPriority.ValueNotSupported||
|InvalidNetworkType.Mismatch||
|InvalidSecurityGroupDiscription.Malformed||
||MissingParameter|
||MissingParameter|
||MissingParameter|
||MissingParameter|
||InvalidSourceGroupId.Mismatch|
||InvalidSourceGroup|
||OwnerUserAccount.Mismatch|

### lapis 建议

建议请求参数Priority为integer，以更好描述取值范围