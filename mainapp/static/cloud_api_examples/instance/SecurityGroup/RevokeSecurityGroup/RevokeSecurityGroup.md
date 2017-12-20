### 阿里文档与项目文档差别

项目文档中，请求参数缺少SourceGroupOwnerId、DestCidrIp、SourcePortRange；

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidRegionId.NotFound|InvalidRegionId.NotFound|
|InvalidSecurityGroupId.NotFound|InvalidSecurityGroupId.NotFound|
|InvalidIpProtocol.ValueNotSupported|InvalidIpProtocol.ValueNotSupported|
|InvalidIpPortRange.Malformed|InvalidIpPortRange.Malformed|
|InvalidSourceGroupId.NotFound|InvalidSourceGroupId.NotFound|
|InvalidSourceCidrIp.Malformed|InvalidSourceCidrIp.Malformed|
|MissingParameter|MissingParameter|
|InvalidPolicy.Malformed|InvalidPolicy.Malformed|
|InvalidNicType.ValueNotSupported|InvalidNicType.ValueNotSupported|
|InvalidNicType.Mismatch||
|InvalidGroupAuthItem.NotFound||
|InvalidSourceGroupId.Mismatch|InvalidSourceGroupId.Mismatch|
||MissingParameter|
||MissingParameter|
||InvalidPriority.Malformed|
||MissingParameter|
||MissingParameter|
||InvalidSourceGroupId.Mismatch|
||InvalidSourceGroup|
||OwnerUserAccount.Mismatch|
