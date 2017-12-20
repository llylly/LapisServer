### 阿里文档勘误

请求参数PrivateIpAddress的类型未指定

### 项目文档勘误

请求参数PrivateIpAddress的类型未指定

### 阿里文档与项目文档差别

API描述部分以下几类请求参数的使用说明存在不一致：1）”实例规格“；2）”镜像“；3）存储；4）网络配置；5）自定义数据；6）其他。

项目文档中，请求参数缺少DataDisk.n.Encrypted、InstanceChargeType、SpotStrategy、SpotPriceLimit、Period、PeriodUnit、AutoRenew、AutoRenewPeriod、UserData、KeyPairName、DeploymentSetId、RamRoleName、SecurityEnhancementStrategy、Tag.n.Key、Tag.n.Value；

项目文档中，请求参数DataDisk.n.Device未在阿里文档中出现。

项目文档和阿里文档的错误码表差异很大，见下表

|阿里文档|项目文档|
|:-:|:-:|
|Account.Arrearage||
|IncorrectVSwitchStatus||
|InstanceDiskCategoryLimitExceed|InstanceDiskCategoryLimitExceed|
|InstanceDiskNumber.LimitExceed||
|InvalidAutoRenewPeriod.ValueNotSupported||
|InvalidDataDiskCategory.ValueNotSupported|InvalidDataDiskCategory.ValueNotSupported|
|InvalidDataDiskCategory.ValueNotSupported||
|InvalidDataDiskSize.ValueNotSupported|InvalidDataDiskSize.ValueNotSupported|
|InvalidDescription.Malformed|InvalidDescription.Malformed|
|InvalidDiskCategory.Mismatch|InvalidDiskCategory.Mismatch|
|InvalidDiskCategory.ValueNotSupported||
|InvalidDiskDescription.Malformed|InvalidDiskDescription.Malformed|
|InvalidDiskDescription.Malformed||
|InvalidDiskName.Malformed|InvalidDiskName.Malformed|
|InvalidHostName.Malformed|InvalidHostName.Malformed|
|InvalidInstanceName.Malformed|InvalidInstanceName.Malformed|
|InvalidInstanceType.ValueNotSupported|InvalidInstanceType.ValueNotSupported|
|InvalidInstanceType.ValueUnauthorized|InvalidInstanceType.ValueUnauthorized|
|InvalidInternetChargeType.ValueNotSupported|InvalidInternetChargeType.ValueNotSupported|
|InvalidIoOptimizedValue.ValueNotSupported||
|InvalidIPAddress.AlreadyUsed||
|InvalidNetworkType.Mismatch||
|InvalidSpotStrategy||
|InvalidSpotPriceLimit||
|InvalidSpotAuthorized||
|InvalidSpotPrepaid||
|InvalidSpotPriceLimit.LowerThanPublicPrice||
|InvalidNetworkType.Mismatch||
|InvalidNodeControllerId.Malformed||
|InvalidParameter|InvalidParameter|
|InvalidParameter|InvalidParameter|
|InvalidParameter.Bandwidth||
|EncryptedOption.Conflict||
|InvalidParameter.Conflict||
|InvalidParameter.Encrypted.KmsNotEnabled||
|InvalidParameter.EncryptedIllegal||
|InvalidParameter.EncryptedNotSupported||
|InvalidParameter.EncryptedNotSupported||
|InvalidParameter.Mismatch|InvalidParameter.Mismatch|
|InvalidParameter.Mismatch||
|InvalidPassword.Malformed|InvalidPassword.Malformed|
|InvalidPeriod||
|InvalidPrivateIpAddress||
|InvalidPrivateIpAddress.Duplicated||
|InvalidPrivateIpAddress.Malformed||
|InvalidSnapshotId.BasedSnapshotTooOld|InvalidSnapshotId.BasedSnapshotTooOld|
|InvalidSpotAliUid||
|InvalidSystemDiskCategory.ValueNotSupported|InvalidSystemDiskCategory.ValueNotSupported|
|InvalidUserData.NotSupported||
|InvalidUserData.SizeExceeded||
|MissingParameter|MissingParameter|
|MissingParamter||
|QuotaExceed.AfterpayInstance|QuotaExceed.AfterpayInstance|
|QuotaExceeded||
|QuotaExceeded.PrivateIpAddress||
|ResourceNotAvailable||
|CategoryNotSupported|CategoryNotSupported|
|DeleteWithInstance.Conflict|DeleteWithInstance.Conflict|
|DependencyViolation.WindowsInstance||
|DeploymentSet.NoRoom||
|Forbbiden||
|ImageNotSubscribed|ImageNotSubscribed|
|ImageNotSupportInstanceType||
|ImageRemovedInMarket||
|InstanceDiskCategoryLimitExceed|InstanceDiskCategoryLimitExceed|
|InstanceDiskNumLimitExceed|InstanceDiskNumLimitExceed|
|InvalidDiskCategory.Mismatch||
|InvalidDiskCategory.NotSupported|InvalidDiskCategory.NotSupported|
|InvalidDiskSize.TooSmall||
|InvalidInstanceType.ZoneNotSupported||
|InvalidNetworkType.MismatchRamRole||
|InvalidParameter.ResourceOwnerAccount||
|InvalidPayMethod||
|InvalidResourceType.NotSupported||
|InvalidSnapshotId.NotDataDiskSnapshot|InvalidSnapshotId.NotDataDiskSnapshot|
|InvalidSnapshotId.NotReady|InvalidSnapshotId.NotReady|
|InvalidSystemDiskCategory.ValueUnauthorized|InvalidSystemDiskCategory.ValueUnauthorized|
|InvalidUser.PassRoleForbidden||
|InvalidUserData.Forbidden||
|InvalidVSwitchId.NotFound||
|IoOptimized.NotSupported|IoOptimized.NotSupported|
|IoOptimized.NotSupported|IoOptimized.NotSupported|
|OperationDenied|OperationDenied|
|OperationDenied|OperationDenied|
|OperationDenied|OperationDenied|
|OperationDenied|OperationDenied|
|OperationDenied|OperationDenied|
|OperationDenied|OperationDenied|
|OperationDenied.NoStock||
|QuotaExceed.BuyImage|QuotaExceed.BuyImage|
|QuotaExceed.PortableCloudDisk|QuotaExceed.PortableCloudDisk|
|RegionUnauthorized|RegionUnauthorized|
|SecurityGroupInstanceLimitExceed|SecurityGroupInstanceLimitExceed|
|Zone.NotOnSale||
|Zone.NotOpen||
|ZoneId.NotFound||
|DependencyViolation.IoOptimized|DependencyViolation.IoOptimized|
|HOSTNAME_ILLEGAL||
|InvalidDataDiskSnapshotId.NotFound|InvalidDataDiskSnapshotId.NotFound|
|InvalidDataDiskSnapshotId.NotFound||
|InvalidDeploymentSetId.NotFound||
|InvalidImageId.NotFound||
|InvalidInstanceChargeType.NotFound||
|InvalidKeyPairName.NotFound||
|InvalidRamRole.NotFound||
|InvalidRegionId.NotFound|InvalidRegionId.NotFound|
|InvalidSecurityGroupId.NotFound|InvalidSecurityGroupId.NotFound|
|InvalidSystemDiskSize||
|InvalidSystemDiskSize.LessThanImageSize|InvalidSystemDiskSize.LessThanImageSize|
|InvalidSystemDiskSize.LessThanMinSize||
|InvalidSystemDiskSize.MoreThanMaxSize|InvalidSystemDiskSize.MoreThanMaxSize|
|InvalidVSwitchId.NotFound||
|InvalidZoneId.NotFound|InvalidZoneId.NotFound|
|IoOptimized.NotSupported||
|OperationDenied|OperationDenied|
|PaymentMethodNotFound||
|InternalError|InternalError|
||InvalidSystemDiskSize.LessThanMinimumSize|
||MissingParameter|
||MissingParameter|
||MissingParameter|
||InvalidParameter|
||InvalidDataDevice.Malformed|
||InvalidParameter.Conflict|
||InvalidDevice.InUse|
||ImageRemovedInMarket|
||InvalidClusterId.NotFound|
||InvalidInstanceDescription.Malformed|
||OperationDenied|
||InvalidParameter.Conflict
||CategoryNotSupported|
||OperationDenied|
||CategoryNotSupported|
||OperationDenied|
||OperationDenied|
||DependencyViolation.Image|
||InstanceTypeNotSupported|


### lapis改正建议

请求参数InternetMaxBandwidthIn类型建议改成整数类型integer，更好的描述[1,200]的取值范围
请求参数InternetMaxBandwidthOut类型建议改成整数类型integer，更好的描述[1,200]的取值范围