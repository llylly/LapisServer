### lapis建议

lapis建议请求参数SystemDisk.Size的类型为integer，更好的描述取值范围这一约束。

### 阿里文档与项目文档差别

项目文档中，请求参数缺少Password、KeyPairName、SecurityEnhancementStrategy；

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidParameter.Conflict|InvalidParameter.Conflict|
|InvalidPassword.Malformed||
|InvalidSystemDiskSize||
|InvalidSystemDiskSize.ImageNotSupportResize||
|InvalidSystemDiskSize.ValueNotSupported||
|OperationDenied|OperationDenied|
|ChargeTypeViolation|ChargeTypeViolation|
|DiskCreatingSnapshot|DiskCreatingSnapshot|
|ImageNotSubscribed|ImageNotSubscribed|
|ImageNotSupportInstanceType||
|ImageRemovedInMarket|ImageRemovedInMarket|
|IncorrectInstanceStatus|IncorrectInstanceStatus|
|INST_HAS_UNPAID_ORDER||
|InstanceExpiredOrInArrears|InstanceExpiredOrInArrears|
|InstanceLockedForSecurity|InstanceLockedForSecurity|
|IoOptimized.NotSupported|IoOptimized.NotSupported|
|QuotaExceed.BuyImage|QuotaExceed.BuyImage|
|InvalidImageId.NotFound|InvalidImageId.NotFound|
|InvalidInstanceId.NotFound|InvalidInstanceId.NotFound|
|InvalidSystemDiskSize.LessThanImageSize|InvalidSystemDiskSize.LessThanImageSize|
|InvalidSystemDiskSize.LessThanMinSize||
|InvalidSystemDiskSize.MoreThanMaxSize|InvalidSystemDiskSize.MoreThanMaxSize|
|NoSuchResource||
|OperationDenied||
||MissingParameter|
||MissingParameter|
||InvalidSystemDiskSize.LessThanMinimumSize|
||InvalidInstanceId.NotFound|
||InvalidParameter.Conflict|
