

## CreateInstance

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

## DeleteInstance

### 阿里文档与项目文档差别

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|IncorrectInstanceStatus|IncorrectInstanceStatus|
|ChargeTypeViolation|ChargeTypeViolation|
|InstanceLockedForSecurity||
|DependencyViolation.SLBConfiguring|DependencyViolation.SLBConfiguring|
|DependencyViolation.RouteEntry||
|InvalidParameter||
|InvalidInstanceId.NotFound||
|IncorrectInstanceStatus.Initializing||
||MissingParameter|
||InternalError|


## DescribeInstances

### 阿里文档与项目文档差别

项目文档中，请求参数缺少SpotStrategy、DeploymentSetId；

项目文档中，请求参数DeviceAvailable未出现在阿里文档中；

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidInstanceChargeType.NotFound|InvalidInstanceChargeType.NotFound|
|InvalidInternetChargeType.ValueNotSupported|InvalidInternetChargeType.ValueNotSupported|
|InvalidNetworkType.NotFound|InvalidNetworkType.NotFound|
|InvalidStatus.NotFound|InvalidStatus.NotFound|
|InvalidTag.Mismatch||
|InvalidTagCount||


## DescribeInstanceStatus

### 阿里文档与项目文档差别

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidRegionId.NotFound||
|InvalidZoneId.NotFound||
||MissingParameter|
||InvalidParameter|
||InvalidParameter|


## DescribeInstanceVncUrl

### 阿里文档与项目文档差别

描述部分不一致，差异较大，描述差异较大，错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidInstanceId.NotFound||
|InvalidRegionId.NotFound|InvalidRegionId.NotFound|
|IncorrectInstanceStatus|IncorrectInstanceStatus|
|InstanceNotReady||
||MissingParameter|
||InternalError|


## JoinSecurityGroup

### 阿里文档与项目文档差别

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidInstanceId.NotFound|InvalidInstanceId.NotFound|
|InvalidSecurityGroupId.NotFound|InvalidSecurityGroupId.NotFound|
|InstanceSecurityGroupLimitExceeded|InstanceSecurityGroupLimitExceeded|
|IncorrectInstanceStatus|IncorrectInstanceStatus|
|InstanceLockedForSecurity|InstanceLockedForSecurity|
|SecurityGroupInstanceLimitExceeded|SecurityGroupInstanceLimitExceeded|
|InvalidInstanceId.Mismatch|InvalidInstanceId.Mismatch|
|InvalidInstanceId.AlreadyExists|InvalidInstanceId.AlreadyExists|
|OperationDenied||
||MissingParameter|
||MissingParameter|


## LeaveSecurityGroup

### 阿里文档与项目文档差别

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidInstanceId.NotFound|InvalidInstanceId.NotFound|
|InvalidSecurityGroupId.NotFound|InvalidSecurityGroupId.NotFound|
|InstanceLastSecurityGroup|InstanceLastSecurityGroup|
|IncorrectInstanceStatus|IncorrectInstanceStatus|
|InstanceLockedForSecurity|InstanceLockedForSecurity|
|InstanceNotInSecurityGroup||
||MissingParameter|
||MissingParameter|


## ModifyInstanceAttribute

### 阿里文档与项目文档差别

项目文档中，请求参数缺少UserData；

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidInstanceId.NotFound|InvalidInstanceId.NotFound|
|InvalidInstanceName.Malformed|InvalidInstanceName.Malformed|
|InvalidDescription.Malformed|InvalidDescription.Malformed|
|InvalidHostPassword.Malformed|InvalidHostPassword.Malformed|
|InvalidHostName.Malformed|InvalidHostName.Malformed|
|IncorrectInstanceStatus|IncorrectInstanceStatus|
|InstanceLockedForSecurity|InstanceLockedForSecurity|
|InvalidSecurityGroupId.NotFound||
|OperationDenied||
|OperationDenied||
|OperationDenied||
|InvalidPassword.Malformed||
|HOSTNAME_ILLEGAL||
|InvalidDescription.Malformed||
|InvalidUserData.Forbidden||
|InvalidUserData.SizeExceeded||
|InvalidUserData.NotSupported||
||MissingParameter|


## ModifyInstanceVncPasswd

### 项目文档勘误

项目文档中错误码IncorrectVncPassword.Malformed没有Http 状态码

### 阿里文档与项目文档差别

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidInstanceId.NotFound||
|InvalidRegionId.NotFound|InvalidRegionId.NotFound|
|IncorrectInstanceStatus|IncorrectInstanceStatus|
|IncorrectVncPassword.Malformed|IncorrectVncPassword.Malformed|
|NoSuchResource||
||MissingParameter|
||InternalError|


## RebootInstance

### 阿里文档与项目文档差别

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidInstanceId.NotFound|InvalidInstanceId.NotFound|
|IncorrectInstanceStatus|IncorrectInstanceStatus|
|InstanceLockedForSecurity|InstanceLockedForSecurity|
|DiskError|DiskError|
||MissingParameter|
||InvalidParameter|


## StartInstance

### 阿里文档与项目文档差别

项目文档中，请求参数缺少InitLocalDisk；

错误码表中差异见下表

|阿里文档|项目文档|
|:-:|:-:|
|InvalidInstanceId.NotFound|InvalidInstanceId.NotFound|
|IncorrectInstanceStatus|IncorrectInstanceStatus|
|InstanceLockedForSecurity|InstanceLockedForSecurity|
|InsufficientBalance|InsufficientBalance|
|InternalError|InternalError|
|InstanceNotReady|InstanceNotReady|
|DiskError|DiskError|
|InstanceExpired||
||MissingParameter|


## StopInstance

### 阿里文档与项目文档差别

项目文档中，请求参数缺少ConfirmStop；

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidInstanceId.NotFound|InvalidInstanceId.NotFound|
|IncorrectInstanceStatus|IncorrectInstanceStatus|
|InstanceLockedForSecurity|InstanceLockedForSecurity|
|DiskError||
|InstanceType. Parameter Mismatch||
||MissingParameter|
||InvalidParameter|


## AttachDisk

### 阿里文档与项目文档差别

项目文档中，请求参数Device未在阿里文档中出现

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidInstanceId.NotFound|InvalidInstanceId.NotFound|
|InvalidDiskId.NotFound|InvalidDiskId.NotFound|
|InvalidDevice.InUse|InvalidDevice.InUse|
|IncorrectDiskStatus|IncorrectDiskStatus|
|DiskNotPortable|DiskNotPortable|
|InstanceLockedForSecurity|InstanceLockedForSecurity|
|ResourcesNotInSameZone|ResourcesNotInSameZone|
|InstanceExpiredOrInArrears|InstanceExpiredOrInArrears|
|DiskInArrears|DiskInArrears|
|IncorrectInstanceStatus|IncorrectInstanceStatus|
|DiskError|DiskError|
|InvalidParameter|InvalidParameter|
|DiskId.ValueNotSupported||
|InvalidDiskId.NotFound||
||MissingParameter|
||MissingParameter|
||InvalidDevice.Malformed|
||InstanceDiskLimitExceeded|


## CreateDisk

### 阿里文档与项目文档差别

项目文档中，请求参数缺少Encrypted

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|Account.Arrearage||
|InvalidDescription.Malformed|InvalidDescription.Malformed|
|InvalidDiskCategory.NotSupported||
|InvalidDiskCategory.ValueNotSupported||
|InvalidDiskName.Malformed|InvalidDiskName.Malformed|
|EncryptedOption.Conflict||
|InvalidParameter.Encrypted.KmsNotEnabled||
|InvalidParameter.EncryptedIllegal||
|InvalidParameter.EncryptedNotSupported||
|InvalidParameter.EncryptedNotSupported||
|InvalidSize.ValueNotSupported||
|MissingParameter|MissingParameter|
|InstanceDiskCategoryLimitExceed|InstanceDiskCategoryLimitExceed|
|InvalidAccountStatus.NotEnoughBalance||
|InvalidAccountStatus.SnapshotServiceUnavailable||
|InvalidDataDiskCategory.NotSupported||
|InvalidDataDiskCategory.NotSupported||
|InvalidDiskCategory.ValueUnauthorized|InvalidDiskCategory.ValueUnauthorized|
|InvalidDiskSize.NotSupported||
|InvalidDiskSize.TooSmall||
|InvalidSnapshot.NotReady||
|InvalidSnapshot.TooLarge|InvalidSnapshot.TooLarge|
|InvalidSnapshot.TooOld|InvalidSnapshot.TooOld|
|InvalidSnapshotId.NotReady|InvalidSnapshotId.NotReady|
|OperationDenied|OperationDenied|
|OperationDenied||
|QuotaExceed.PortableCloudDisk|QuotaExceed.PortableCloudDisk|
|InvalidRegionId.NotFound|InvalidRegionId.NotFound|
|InvalidRegionId.NotFound||
|InvalidSnapshotId.NotFound|InvalidSnapshotId.NotFound|
|InvalidZoneId.NotFound|InvalidZoneId.NotFound|
||MissingParameter|
||InvalidParameter|
||MissingParameter|
||InvalidSnapshotId.NotDataDiskSnapshot|
||InvalidSnapshotId.NotFound|


## DeleteDisk

### 阿里文档与项目文档差别


错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|IncorrectDiskStatus|IncorrectDiskStatus|
|DiskNotPortable|DiskNotPortable|
|DiskTypeViolation|DiskTypeViolation|
|DiskCreatingSnapshot|DiskCreatingSnapshot|
||MissingParameter|


## DescribeDisks

### 阿里文档与项目文档差别

项目文档中，请求参数缺少Encrypted

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidDiskType.ValueNotSupported|InvalidDiskType.ValueNotSupported|
|InvalidCategory.ValueNotSupported|InvalidCategory.ValueNotSupported|
|InvalidStatus.ValueNotSupported|InvalidStatus.ValueNotSupported|
|InvalidDiskIds.Malformed|InvalidDiskIds.Malformed|
|InvalidDiskChargeType.NotFound|InvalidDiskChargeType.NotFound|
|InvalidLockReason.NotFound||
|InvalidTag.Mismatch||
|InvalidTagCount||
|InvalidRegion.NotFound||
|InvalidZoneId.NotFound||
||MissingParameter|
||InvalidParameter|
||InvalidParameter|
||InvalidParameter|
||InvalidParameter|
||InvalidParameter|


## DetachDisk

### 阿里文档与项目文档差别

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidInstanceId.NotFound|InvalidInstanceId.NotFound|
|InvalidDiskId.NotFound|InvalidDiskId.NotFound|
|IncorrectDiskStatus|IncorrectDiskStatus|
|DiskNotPortable|DiskNotPortable|
|InstanceLockedForSecurity|InstanceLockedForSecurity|
|DependencyViolation|DependencyViolation|
|DiskTypeViolation|DiskTypeViolation|
|InvalidDiskId.Released||
|IncorrectInstanceStatus||
|InvalidParameter||
|InvalidDiskId.NotFound||
||MissingParameter|
||MissingParameter|


## ModifyDiskAttribute

### 阿里文档与项目文档差别

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidDiskId.NotFound|InvalidDiskId.NotFound|
|InvalidDiskName.Malformed|InvalidDiskName.Malformed|
|InvalidDescription.Malformed|InvalidDescription.Malformed|
|NoAttributeToModify|NoAttributeToModify|
|DiskNotPortable|DiskNotPortable|
|QuotaExceed.Snapshot||
|IncorrectDiskStatus||
||MissingParameter|
||InvalidParameter|


## ReInitDisk

### 阿里文档与项目文档差别

项目文档中，请求参数缺少SecurityEnhancementStrategy

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidDiskId.NotFound|InvalidDiskId.NotFound|
|IncorrectDiskStatus|IncorrectDiskStatus|
|IncorrectInstanceStatus|IncorrectInstanceStatus|
|InstanceLockedForSecurity|InstanceLockedForSecurity|
|InvalidSnapshot.TooOld|InvalidSnapshot.TooOld|
|InvalidSourceSnapshot|InvalidSourceSnapshot|
|InstanceExpiredOrInArrears|InstanceExpiredOrInArrears|
|DiskCreatingSnapshot|DiskCreatingSnapshot|
|OperationDenied||
|InvalidImageId.NotFound||
|SharedImageDeleted||
|InvalidPassword.Malformed||
|DiskCategory.OperationNotSupported||
||MissingParameter|
||IncorrectDiskStatus.NeverUsed|


## ReplaceSystemDisk

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


## ResetDisk

### 阿里文档与项目文档差别

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidDiskId.NotFound|InvalidDiskId.NotFound|
|InvalidSnapshotId.NotFound|InvalidSnapshotId.NotFound|
|IncorrectDiskStatus|IncorrectDiskStatus|
|IncorrectInstanceStatus|IncorrectInstanceStatus|
|InstanceLockedForSecurity|InstanceLockedForSecurity|
|InvalidParameter.Mismatch|InvalidParameter.Mismatch|
|InvalidSnapshot.TooOld|InvalidSnapshot.TooOld|
|InstanceExpiredOrInArrears|InstanceExpiredOrInArrears|
|OperationDenied|OperationDenied|
|InvalidSnapshotId.NotReady|InvalidSnapshotId.NotReady|
|DiskCategory.OperationNotSupported||
|InvalidAccountStatus.NotEnoughBalance||
|InvalidAccountStatus.SnapshotServiceUnavailable||
||MissingParameter|
||MissingParameter|


## ResizeDisk

### 阿里文档与项目文档差别

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidDiskSize.TooSmall|InvalidDiskSize.TooSmall|
|OperationDenied|OperationDenied|
|OperationDenied|OperationDenied|
|InvalidDiskId.NotFound|InvalidDiskId.NotFound|
|InstanceExpiredOrInArrears|InstanceExpiredOrInArrears|
|InvalidDataDiskSize.ValueNotSupported||
|InvalidInstanceId.NotFound|InvalidInstanceId.NotFound|
|InvalidDiskSize.TooLarge||
|DiskError||
|DiskInArrears||
|IncorrectInstanceStatus||
|DiskCreatingSnapshot||
||InvalidParameter|


## ApplyAutoSnapshotPolicy

### 阿里文档与项目文档差别

项目文档中无错误码表，其他部分一致

### 项目文档勘误

项目文档API列表中无此API

## CancelAutoSnapshotPolicy

### 阿里文档与项目文档差别

项目文档中无错误码表，其他部分一致

### 项目文档勘误

项目文档API列表中无此API

## CreateAutoSnapshotPolicy

### 阿里文档与项目文档差别

API描述部分有差异；

项目文档中缺错误码表；


### 项目文档勘误

项目文档API列表中无此API

## CreateSnapshot

### 阿里文档与项目文档差别

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidDiskId.NotFound|InvalidDiskId.NotFound|
|InvalidSnapshotName.Malformed|InvalidSnapshotName.Malformed|
|InvalidDescription.Malformed|InvalidDescription.Malformed|
|IncorrectInstanceStatus|IncorrectInstanceStatus|
|IncorrectDiskStatus.CreatingSnapshot|IncorrectDiskStatus.CreatingSnapshot|
|InstanceLockedForSecurity|InstanceLockedForSecurity|
|IncorrectDiskStatus.NeverAttached|IncorrectDiskStatus.NeverAttached|
|QuotaExceed.Snapshot|QuotaExceed.Snapshot|
|IncorrectDiskStatus.NeverUsed|IncorrectDiskStatus.NeverUsed|
|CreateSnapshot.Failed|CreateSnapshot.Failed|
|DiskInArrears||
|DiskId.ValueNotSupported||
|DiskCategory.OperationNotSupported||
|IncorrectDiskStatus||
|InvalidAccountStatus.NotEnoughBalance||
|InvalidAccountStatus.SnapshotServiceUnavailable||
||MissingParameter|


## DeleteAutoSnapshotPolicy

### 阿里文档与项目文档差别

项目文档中无错误码表，其他部分一致

### 项目文档勘误

项目文档API列表中无此API

## DescribeAutoSnapshotPolicyEx

### 阿里文档勘误

API名应当为DescribeAutoSnapshotPolicyEx，而在阿里网站API概览中，显示为DescribeAutoSnapshotPolicy

### 项目文档勘误

API名应当为DescribeAutoSnapshotPolicyEx，而在项目文档API概览中，显示为DescribeAutoSnapshotPolicy



## DescribeSnapshots

### 阿里文档与项目文档差别

项目文档中，请求参数缺少Encrypted；

项目文档中，返回参数RegionId未在阿里文档中出现；

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidSnapshotIds.Malformed|InvalidSnapshotIds.Malformed|
|InvalidStatus.NotFound|InvalidStatus.NotFound|
|InvalidSnapshotType.NotFound|InvalidSnapshotType.NotFound|
|InvalidUsage|InvalidUsage|
|InvalidSourceDiskType|InvalidSourceDiskType|
|InvalidTag.Mismatch||
|InvalidTagCount||
||MissingParameter|
||InvalidParameter|
||InvalidParameter|


## ModifyAutoSnapshotPolicyEx

### 阿里文档与项目文档差别

项目文档中无错误码表，其他部分一致

### 项目文档勘误

项目文档API列表中无此API

## CancelCopyImage

### 阿里文档与项目文档差别

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|IncorrectImageStatus|IncorrectImageStatus|
|InvalidRegionId.NotFound|InvalidRegionId.NotFound|
|InvalidImageId.NotFound|InvalidImageId.NotFound|
|ImageCreatedNotFromCopy||
|IncorrectImageStatus|IncorrectImageStatus|
|IncorrectImageStatus||
|IncorrectImageStatus||
|IncorrectImageStatus||
||MissingParameter|
||MissingParameter|


## CopyImage

### 阿里文档与项目文档差别

项目文档中，请求参数ClientToken未在阿里文档中出现；

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|DestinationRegion.NotFound|DestinationRegion.NotFound|
|IncorrectImageStatus|IncorrectImageStatus|
|InvalidDescription.Malformed|InvalidDescription.Malformed|
|InvalidDescription.Malformed||
|InvalidImageId.NotFound|InvalidImageId.NotFound|
|InvalidImageName.Duplicated|InvalidImageName.Duplicated|
|InvalidImageName.Malformed|InvalidImageName.Malformed|
|InvalidImageName.Malformed||
|InvalidSnapshotId.NotFound||
|SourceRegion.NotFound|SourceRegion.NotFound|
|Forbidden|Forbbiden|
|IncorrectDestinationRegion|IncorrectDestinationRegion|
|InvalidSnapshot.TooOld||
|OperationDeined.EncryptedSnapshot||
|OperationDenied||
|OperationDenied.ImageCopying|OperationDenied.ImageCopying|
|QuotaExceed.Image|QuotaExceed.Image|
|QuotaExceed.Snapshot|QuotaExceed.Snapshot|
|RegionNotSupportCopy|RegionNotSupportCopy|
||MissingParameter|
||MissingParameter|
||MissingParameter|


## CreateImage

### 阿里文档与项目文档差别

API描述部分差别较大

项目文档中，请求参数缺少InstanceId、DiskDeviceMapping.N.Size、DiskDeviceMapping.N.SnapshotId；

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|IncorrectInstanceStatus||
|InstanceLockedForSecurity||
|InvalidDescription.Malformed|InvalidDescription.Malformed|
|InvalidImageName.Duplicated||
|InvalidImageName.Malformed|InvalidImageName.Malformed|
|InvalidImageVersion.Malformed|InvalidImageVersion.Malformed|
|InvalidInstanceId.NotFound||
|InvalidInstanceId.ValueNotSupported||
|InvalidSize.ValueNotSupported||
|MissingParameter|MissingParameter|
|OperationDenied|OperationDenied|
|OperationDenied|OperationDenied|
|InvalidAccountStatus.NotEnoughBalance||
|InvalidAccountStatus.SnapshotServiceUnavailable||
|InvalidParamter.Conflict|InvalidParamter.Conflict|
|InvalidSnapshot.TooOld|InvalidSnapshot.TooOld|
|InvalidSnapshotId.NotReady|InvalidSnapshotId.NotReady|
|OperationDenied||
|OperationDenied||
|QuotaExceed.Image|QuotaExceed.Image|
|InvalidRegionId.NotFound|InvalidRegionId.NotFound|
|InvalidSnapshotId.NotFound|InvalidSnapshotId.NotFound|
|InvalidSnapshotId.NotFound||
||MissingParameter|

### lapis建议

lapis建议请求参数DiskDeviceMapping.N.Size类型改为integer，以更好地描述取值范围：[5, 2000]

## DeleteImage

### 阿里文档与项目文档差别

项目文档中，请求参数缺少Force；

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|ImageUsingByInstance|ImageUsingByInstance|
|ImageIsCreating||
|ImageUseShared||
|OperationDenied.ImageCopying||
|InvalidRegionId.NotFound|InvalidRegionId.NotFound|
||MissingParameter|
||MissingParameter|


## DescribeImages

### 阿里文档与项目文档差别

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidImageOwnerAlias.ValueNotSupported|InvalidImageOwnerAlias.ValueNotSupported|
|InvalidUsage|InvalidUsage|
|InvalidTag.Mismatch||
|InvalidTagCount||
|InvalidInstanceType.ValueNotSupported||
|InvalidOSType||
|InvalidArchitecture||
||MissingParameter|
||InvalidParameter|
||InvalidParameter|


## DescribeImageSharePermission

### 阿里文档与项目文档差别

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|MissingParameter||
|MissingParameter||
|InvalidRegionId.NotFound|InvalidRegionId.NotFound|
|InvalidImageId.NotFound|InvalidImageId.NotFound|


## ImportImage

### 阿里文档与项目文档差别

API描述中，阿里文档DiskDeviceMapping.n的n取值为[1, 16]。n 为 1 时表示系统盘，n 为 [2, 16] 时表示数据盘。
项目文档中DiskDeviceMapping.N 暂时只支持1，也就是只支持系统盘镜像，暂时不支持数据盘做镜像。

项目文档中，请求参数ClientToken在阿里文档中未出现


## ModifyImageAttribute

### 阿里文档与项目文档差别

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidImageName.Malformed|InvalidImageName.Malformed|
|MissingParameter|MissingParameter|
|InvalidRegionId.NotFound||
|InvalidImageName.Duplicated|InvalidImageName.Duplicated|
|InvalidDescription.Malformed|InvalidDescription.Malformed|
|InvalidImageId.NotFound|InvalidImageId.NotFound|
||MissingParameter|


## ModifyImageSharePermission

### 阿里文档与项目文档差别

API描述部分有差异

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|IncorrectImageStatus|IncorrectImageStatus|
|InvalidRegionId.NotFound|InvalidRegionId.NotFound|
|MissingParameter|MissingParameter|
|MissingParameter|MissingParameter|
|OperationDeined.EncryptedSnapshot||
|InvalidImageId.NotFound|InvalidImageId.NotFound|
|QuotaExceed.ShareImageUser|QuotaExceed.ShareImageUser|
|InvalidAccount.Forbbiden|InvalidAccount.Forbbiden|
|InvalidAccount.NotFound|InvalidAccount.NotFound|
||QuotaExceed.ShareImage|


## AllocatePublicIpAddress

### 阿里文档与项目文档差别

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidInstanceId.NotFound|InvalidInstanceId.NotFound|
|IncorrectInstanceStatus|IncorrectInstanceStatus|
|InstanceLockedForSecurity|InstanceLockedForSecurity|
|InstanceExpiredOrInArrears|InstanceExpiredOrInArrears|
|IpInUse|IpInUse|
|AllocatedAlready|AllocatedAlready|
|OperationDenied||
|InsufficientPublicIp||
||MissingParameter|


## ModifyInstanceNetworkSpec

### 阿里文档与项目文档差别

API描述差异较大

项目文档中，请求参数InternetMaxBandwi dthOut、InternetMaxBandwi dthIn的语义描述和阿里文档不一致；

项目文档中，请求参数缺少NetworkChargeType、AutoPay、ClientToken；

项目文档中缺少返回参数RequestId、OrderId

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|Account.Arrearage||
|DecreasedBandWidthNotAllowed||
|InvalidEndTime.ValueNotSupported||
|InvalidInstance.UnpaidOrder||
|InvalidInstanceStatus.NotStopped||
|InvalidInternetChargeType.ValueNotSupported||
|InvalidInternetMaxBandwidthIn.ValueNotSupported|InvalidInternetMaxBandwidthIn.ValueNotSupported|
|InvalidInternetMaxBandwidthOut.ValueNotSupported|InvalidInternetMaxBandwidthOut.ValueNotSupported|
|InvalidStartTime.ValueNotSupported||
|MissingParameter|MissingParameter|
|OperationDenied||
|ChargeTypeViolation|ChargeTypeViolation|
|IncorrectInstanceStatus|IncorrectInstanceStatus|
|InstanceExpiredOrInArrears|InstanceExpiredOrInArrears|
|InstanceLockedForSecurity|InstanceLockedForSecurity|
|InvalidAccountStatus.NotEnoughBalance||
|OperationDenied||
|InvalidInstanceId.NotFound|InvalidInstanceId.NotFound|
|InternalError|InternalError|
||InvalidParameter|
||InvalidParameter|


## AuthorizeSecurityGroup

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

## AuthorizeSecurityGroupEgress

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

## CreateSecurityGroup

### 阿里文档与项目文档差别

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidRegionId.NotFound|InvalidRegionId.NotFound|
|InvalidSecurityGroupName.Malformed|InvalidSecurityGroupName.Malformed|
|InvalidDescription.Malformed|InvalidDescription.Malformed|
|QuotaExceed.SecurityGroup|QuotaExceed.SecurityGroup|
|InvalidVpcId.NotFound|InvalidVpcId.NotFound|
|InvalidSecurityGroupDiscription.Malformed||
|InvalidVpcId.NotFound||
|IncorrectVpcStatus||
||MissingParameter|


## DeleteSecurityGroup

### 阿里文档与项目文档差别

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidRegionId.NotFound|InvalidRegionId.NotFound|
|DependencyViolation|DependencyViolation|
|DependencyViolation|DependencyViolation|
||MissingParameter|
||MissingParameter|
||DependencyViolation|


## DescribeSecurityGroupAttribute

### 阿里文档与项目文档差别

项目文档中，返回参数缺少InnerAccessPolicy；

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidNicType.ValueNotSupported|InvalidNicType.ValueNotSupported|
|InvalidRegionId.NotFound|InvalidRegionId.NotFound|
|InvalidSecurityGroupId.NotFound|InvalidSecurityGroupId.NotFound|
||MissingParameter|
||MissingParameter|


## DescribeSecurityGroups

### 阿里文档与项目文档差别

阿里文档无单独的错误码表，其他部分一致


## ModifySecurityGroupAttribute

### 阿里文档与项目文档差别

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidSecurityGroupName.Malformed|InvalidSecurityGroupName.Malformed|
|InvalidSecurityGroupId.NotFound||
|InvalidSecurityGroupDiscription.Malformed||
||InvalidRegionId.NotFound|
||MissingParameter|
||MissingParameter|
||InvalidRegionId.NotFound|
||InvalidDescription.Malformed|


## RevokeSecurityGroup

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


## RevokeSecurityGroupEgress

### 阿里文档与项目文档差别

项目文档中，请求参数缺少DestGroupOwnerId、SourceCidrIp、SourcePortRange；

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidRegionId.NotFound|InvalidRegionId.NotFound|
|InvalidSecurityGroupId.NotFound|InvalidSecurityGroupId.NotFound|
|InvalidIpProtocol.ValueNotSupported|InvalidIpProtocol.ValueNotSupported|
|InvalidIpPortRange.Malformed|InvalidIpPortRange.Malformed|
|InvalidDestGroupId.NotFound|InvalidDestGroupId.NotFound|
|InvalidDestCidrIp.Malformed|InvalidDestCidrIp.Malformed|
|MissingParameter|MissingParameter|
|InvalidPolicy.Malformed|InvalidPolicy.Malformed|
|InvalidNicType.ValueNotSupported|InvalidNicType.ValueNotSupported|
|InvalidNicType.Mismatch||
|InvalidGroupAuthItem.NotFound||
|InvalidDestCidrIp.sMalformed||
|InvalidDestGroupId.Mismatch|InvalidDestGroupId.Mismatch|
|InvalidSecurityGroup.IsSame||
||MissingParameter|
||MissingParameter|
||InvalidPriority.Malformed|
||MissingParameter|
||MissingParameter|
||InvalidDestGroupId.Mismatch|
||InvalidDestGroupOwnerUserAccount.Mismatch|


## DescribeRegions

### 阿里文档与项目文档差别

阿里文档无单独错误码表，其他部分一致


## DescribeZones

### 阿里文档与项目文档差别

项目文档中，请求参数缺少InstanceChargeType、SpotStrategy；

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidRegionId.NotFound||
||MissingParameter|


## DescribeDiskMonitorData

### 阿里文档与项目文档差别

关于最长查询的天数，阿里和项目文档的API描述存在差异；

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidDiskId.NotFound|InvalidDiskId.NotFound|
|InvalidStartTime.Malformed|InvalidStartTime.Malformed|
|InvalidEndTime.Malformed|InvalidEndTime.Malformed|
|InvalidPeriod.ValueNotSupported|InvalidPeriod.ValueNotSupported|
|InvalidStartTime.TooEarly|InvalidStartTime.TooEarly|
|InvalidParameter.TooManyDataQueried||
|Throttling||
||MissingParameter|
||MissingParameter|
||MissingParameter|
||InvalidParameter|


## DescribeInstanceMonitorData

### 阿里文档与项目文档差别

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidInstanceId.NotFound|InvalidInstanceId.NotFound|
|InvalidStartTime.Malformed|InvalidStartTime.Malformed|
|InvalidEndTime.Malformed|InvalidEndTime.Malformed|
|InvalidPeriod.ValueNotSupported|InvalidPeriod.ValueNotSupported|
|InvalidStartTime.TooEarly|InvalidStartTime.TooEarly|
|InvalidParameter.TooManyDataQueried||
|Throttling||
||MissingParameter|
||MissingParameter|
||MissingParameter|
||InvalidParameter|


## CancelTask

### 阿里文档与项目文档差别

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|MissingParameter|MissingParameter|
|MissingParameter|MissingParameter|
|InvalidRegionId.NotFound|RegionId.NotFound|
|InvalidTaskId.NotFound|InvalidTaskId.NotFound|
|InvalidTaskId.TaskActionNotSupport||
|InvalidTaskId.IncorrectTaskStatus||
|CancelTaskFailed|CancelTaskFailed|


## DescribeInstanceTypeFamilies

### 阿里文档与项目文档差别

项目文档无请求示例与返回示例，其他部分一致




## DescribeTasks

### 阿里文档与项目文档差别

项目文档中，请求参数Generation的语义描述和阿里文档有差异；

项目文档缺少错误码描述，其他部分一致

